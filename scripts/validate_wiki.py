#!/usr/bin/env python3
"""Check catalog, local links, PDF provenance, and bidirectional synthesis coverage.

Uses only the standard library. With Poppler installed, also verifies PDF page
counts and successful text extraction. This checks artifact integrity, not the
scientific correctness of the notes or reproduction of a paper's results.
"""
from __future__ import annotations
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlsplit, unquote
sys.dont_write_bytecode = True
from build_index import build_catalog

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / 'wiki'


def field(text: str, name: str) -> str:
    fm = re.match(r'^---\n(.*?)\n---', text, re.S)
    if not fm:
        return ''
    match = re.search(r'^' + re.escape(name) + r':\s*(.*)$', fm[1], re.M)
    if not match:
        return ''
    value = match[1].strip()
    try:
        return str(json.loads(value))
    except (ValueError, TypeError):
        return value.strip('\"\'')


def wiki_targets(text: str, pages: list[Path]) -> tuple[set[Path], list[str]]:
    resolved, errors = set(), []
    for raw in re.findall(r'\[\[([^\]]+)\]\]', text):
        target = raw.split('|', 1)[0].split('#', 1)[0]
        if not target:
            continue
        candidates = ([WIKI / (target + '.md')] if '/' in target
                      else [p for p in pages if p.stem == target])
        candidates = [p for p in candidates if p.is_file()]
        if len(candidates) != 1:
            errors.append(f'Unresolved or ambiguous wiki link: {raw}')
        else:
            resolved.add(candidates[0])
    return resolved, errors


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    pages = sorted(WIKI.rglob('*.md'))
    refs = {}
    for path in sorted(ROOT.rglob('*.md')):
        if '.git' in path.parts:
            continue
        text = path.read_text(encoding='utf-8')
        targets, problems = wiki_targets(text, pages)
        errors.extend(f'{path.relative_to(ROOT)}: {x}' for x in problems)
        if path in pages:
            refs[path] = targets
        # Current repository links use ordinary Markdown destinations, with no
        # nested parentheses in local paths. Ignore fragments and external URIs.
        for raw in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^\s)]+)\)', text):
            u = urlsplit(raw)
            if u.scheme or u.netloc or not u.path:
                continue
            dest = (ROOT / unquote(u.path).lstrip('/') if u.path.startswith('/')
                    else path.parent / unquote(u.path))
            if not dest.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing local link {raw}')
    if (ROOT / 'index.md').read_text(encoding='utf-8') != build_catalog():
        errors.append('index.md is stale; run scripts/build_index.py --apply')
    manifest = json.loads((ROOT / 'papers/manifest.json').read_text())['papers']
    stems, ids = set(), set()
    for record in manifest:
        stem = record['stem']
        canonical_id = re.sub(r'v\d+$', '', record['arxiv_version'])
        if stem in stems or canonical_id in ids:
            errors.append(f'Duplicate manifest record: {stem} / {canonical_id}')
        stems.add(stem); ids.add(canonical_id)
        pdf = ROOT / record['pdf_path']
        if not pdf.is_file() or pdf.is_symlink():
            errors.append(f'{stem}: canonical PDF missing or symlinked'); continue
        data = pdf.read_bytes()
        if not data.startswith(b'%PDF-'):
            errors.append(f'{stem}: invalid PDF signature')
        if len(data) != record['bytes'] or hashlib.sha256(data).hexdigest() != record['sha256']:
            errors.append(f'{stem}: PDF bytes/hash do not match manifest')
        if shutil.which('pdfinfo'):
            result = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True)
            match = re.search(r'^Pages:\s*(\d+)', result.stdout, re.M)
            if result.returncode or not match or int(match[1]) != record['pages']:
                errors.append(f'{stem}: PDF page count differs or cannot be read')
        else:
            warnings.append('pdfinfo unavailable: page counts not independently checked')
        if shutil.which('pdftotext'):
            result = subprocess.run(['pdftotext', '-layout', str(pdf), '-'], capture_output=True)
            if result.returncode or len(result.stdout.strip()) < 100:
                errors.append(f'{stem}: PDF extraction failed or empty')
        else:
            warnings.append('pdftotext unavailable: extraction not checked')
        source = ROOT / 'sources' / (stem + '.md')
        paper = WIKI / 'self-improving-agents' / (stem + '.md')
        for path, required in [(source, ['One-line Summary', '1. Document Information',
                    '2. Key Contributions', '3. Methodology and Architecture',
                    '4. Key Results and Benchmarks', '5. Limitations and Future Work',
                    '6. Related Work', '7. Glossary']),
                (paper, ['Summary', 'Key Contributions', 'Methodology and Architecture',
                         'Results', 'Related Papers'])]:
            if not path.is_file():
                errors.append(f'{stem}: missing {path.relative_to(ROOT)}'); continue
            text = path.read_text(encoding='utf-8')
            for heading in required:
                if not re.search(r'^## ' + re.escape(heading) + r'\s*$', text, re.M):
                    errors.append(f'{path.relative_to(ROOT)}: missing section {heading}')
            for key, expected in [('source_format', 'pdf'), ('text_extractor', 'pdftotext-layout'),
                                  ('arxiv_version', record['arxiv_version']),
                                  ('pdf_sha256', record['sha256']),
                                  ('pdf_pages', str(record['pages']))]:
                if field(text, key) != expected:
                    errors.append(f'{path.relative_to(ROOT)}: incorrect {key}')
            if not re.search(re.escape(record['url']) + r'#page=\d+', text):
                errors.append(f'{path.relative_to(ROOT)}: no pinned PDF page citation')
        anchors = [p for p in refs.get(paper, set()) if p.parent.name in ('concepts', 'overviews')]
        if not any(paper in refs.get(anchor, set()) for anchor in anchors):
            errors.append(f'{stem}: no bidirectional synthesis link')
    paper_stems = {p.stem for p in (WIKI / 'self-improving-agents').glob('*.md')}
    source_stems = {p.stem for p in (ROOT / 'sources').glob('*.md')}
    pdf_stems = {p.stem for p in (ROOT / 'papers').glob('*.pdf')}
    for label, actual in [('paper pages', paper_stems), ('sources', source_stems), ('PDFs', pdf_stems)]:
        if actual != stems:
            errors.append(f'{label} differ from manifest: {sorted(actual ^ stems)}')
    for warning in sorted(set(warnings)):
        print('WARNING:', warning)
    for error in errors:
        print('ERROR:', error)
    if errors:
        print(f'FAIL: {len(errors)} integrity error(s)'); return 1
    print(f'PASS: {len(manifest)} PDF/source/wiki triples; {len(pages)} wiki pages; '
          'catalog current; local links and bidirectional synthesis links valid.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
