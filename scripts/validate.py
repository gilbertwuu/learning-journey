#!/usr/bin/env python3
"""Validate this distributable learning plugin without third-party packages."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []
def require(ok, message):
    if not ok:
        errors.append(message)
def read_json(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))

def main():
    portable = read_json('plugin.json')
    codex = read_json('.codex-plugin/plugin.json')
    claude = read_json('.claude-plugin/plugin.json')
    for manifest in (codex, claude):
        for key in ('name', 'version', 'description', 'license', 'repository'):
            require(manifest.get(key) == portable.get(key), f'Manifest mismatch: {key}')
    require(codex['skills'] == './skills/', 'Codex skill path must resolve to bundled skills')
    require(portable['extensions']['com.openai']['interface'] == codex['interface'], 'UI metadata differs')
    for file in ('.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json'):
        market = read_json(file)
        require(len(market['plugins']) == 1, f'{file}: expected one plugin')
        entry = market['plugins'][0]
        require(entry['name'] == portable['name'], f'{file}: plugin name mismatch')
        source = entry['source']
        relative = source['path'] if isinstance(source, dict) else source
        require(relative == './', f'{file}: unexpected source root')
    skills = sorted(p.parent.name for p in (ROOT / 'skills').glob('*/SKILL.md'))
    require(skills == ['plan','probe','teach'], f'Unexpected skill entrypoints: {skills}')
    for name in skills:
        text = (ROOT/'skills'/name/'SKILL.md').read_text(encoding='utf-8')
        require(text.startswith('---\n'), f'{name}: missing frontmatter')
        header = text.split('---', 2)[1]
        require(re.search(r'^name: '+re.escape(name)+r'\s*$', header, re.M), f'{name}: name mismatch')
        require(re.search(r'^description: .+', header, re.M), f'{name}: missing description')
    for path in ROOT.rglob('*'):
        if '.git' in path.parts or '.build' in path.parts or '__pycache__' in path.parts:
            continue
        require(not path.is_symlink(), f'Symlink in package: {path.relative_to(ROOT)}')
        if not path.is_file() or 'vendor' in path.parts:
            continue
        if path.suffix not in ('.md','.json','.yaml','.yml','.py','.js','.css','.html'):
            continue
        text = path.read_text(encoding='utf-8')
        if path.name != 'validate.py':
            require(not re.search(r'/Users/[^/\s]+/|/home/[^/\s]+/|[A-Z]:\\Users\\', text), f'Local user path: {path.relative_to(ROOT)}')
        if path.suffix == '.md':
            for match in re.finditer(r'\]\(([^)]+)\)', text):
                link = match.group(1).split('#',1)[0].strip('<>')
                if not link or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',link):
                    continue
                require((path.parent/unquote(link)).exists(), f'Broken link in {path.relative_to(ROOT)}: {link}')
    candidate = read_json('examples/python-basics/candidate.json')
    notes = read_json('examples/python-basics/notes.json')
    ids = [node['id'] for node in candidate['nodes']]
    require(len(ids)==len(set(ids)) and set(ids)==set(notes), 'Example nodes/notes differ')
    require(all(e['from'] in ids and e['to'] in ids for e in candidate['edges']), 'Broken example edge')
    for rel, expected in read_json('vendor-lock.json')['sha256'].items():
        path = ROOT/rel
        require(path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest()==expected, f'Vendor integrity: {rel}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print('PASS: manifests, 3 skills, document links, portable paths, example topology, vendor integrity')
    return 0
if __name__ == '__main__':
    try:
        sys.exit(main())
    except (KeyError,ValueError,OSError) as exc:
        print(f'Validation failed: {exc}', file=sys.stderr)
        sys.exit(1)
