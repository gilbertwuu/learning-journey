#!/usr/bin/env python3
"""Build a study board through a private Archify renderer copy, preserving provenance."""
import argparse, json, os, pathlib, shutil, subprocess, sys


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('candidate', type=pathlib.Path)
    ap.add_argument('notes', type=pathlib.Path)
    ap.add_argument('output_directory', type=pathlib.Path)
    ap.add_argument('--archify', type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1]/'vendor/archify')
    args = ap.parse_args()
    skill = pathlib.Path(__file__).resolve().parents[1]
    data = json.loads(args.candidate.read_text())
    # Learning details live in node popovers; omit the duplicate card grid.
    data['cards'] = []
    notes = json.loads(args.notes.read_text())
    if data.get('diagram_type') != 'workflow' or data.get('schema_version') != 2:
        raise ValueError('Requires Archify workflow schema v2.')
    ids = [n['id'] for n in data['nodes']]
    if len(set(ids)) != len(ids) or set(ids) != set(notes):
        raise ValueError('Each unique node must have exactly one matching learning note.')
    for key, note in notes.items():
        if not isinstance(note, list) or len(note) != 3 or not all(isinstance(x,str) and x.strip() for x in note):
            raise ValueError(f'{key}: expected [current level, understood content, remaining uncertainty].')
    if any(n['type'] not in ['frontend','external'] for n in data['nodes']):
        raise ValueError('Use frontend for needs learning and external for related prior knowledge.')
    dst = args.output_directory.resolve()
    if dst.exists():
        raise ValueError('Output directory already exists; use a new directory. For repairs edit its candidate and rerun its renderer finalize.')
    if not (args.archify/'assets/template.html').is_file():
        raise ValueError('Archify skill not found; provide --archify PATH.')
    template = (args.archify/'assets/template.html').read_text()
    compiler = (args.archify/'renderers/workflow/workflow-compiler.mjs').read_text()
    anchors = ['<div class="semantic-passport-meta" id="focus-passport-meta"','function renderPassport(id, node) {','</style>']
    if (any(template.count(a) != 1 for a in anchors[:2]) or '</style>' not in template) or compiler.count('  const sub = hasSub\n') != 1:
        raise ValueError('Archify template changed; review the adapter before building. No files written.')
    for n in data['nodes']:
        n.pop('tag',None)
        n['icon'] = 'none'
    meta = data['meta']
    meta.update(locale='zh-CN', animation='trace', visual_preset='signal-flow', quality_profile='showcase', output=dst.name+'/board.html')
    meta['legend'] = {'entries':{'frontend':{'label':'需要学习'},'external':{'label':'已有相关认识'}}}
    meta.setdefault('translations',{}).update({
        'viewer.passport.eyebrow':'这个知识点的学习情况',
        'viewer.passport.close':'关闭学习情况', 'viewer.passport.move':'移动学习情况窗口',
        'viewer.passport.metadata':'所在学习阶段',
        'viewer.passport.relationship.group.out':'接下来可以学什么',
        'viewer.passport.relationship.group.in':'从哪些认识接过来',
        'viewer.passport.relationship.summary':'接下来连接 {out} 项 · 前面连接 {in} 项{loops}',
        'viewer.passport.relations':'知识之间的连接',
        'viewer.passport.relations.show':'查看前后知识点',
        'viewer.passport.relations.hide':'收起前后知识点'})
    # Escape script delimiters without interpreting authored learning notes as HTML.
    payload = json.dumps(notes,ensure_ascii=False).replace('<','\\u003c').replace('\u2028','\\u2028').replace('\u2029','\\u2029')
    js = (skill/'assets/learning-panel.js').read_text().replace('__LEARNING_NOTES__',payload)
    template = template.replace(anchors[0],'<div id="learning-description"></div>\n'+anchors[0],1)
    template = template.replace(anchors[1],anchors[1]+'\n'+js,1)
    template = template.replace('</style>',(skill/'assets/learning-panel.css').read_text()+'\n</style>',1)
    compiler = compiler.replace('  const sub = hasSub\n',"  if (node.icon === 'none' && !node.tag) {\n    labelLayout.x = node.width / 2;\n    labelLayout.ys = hasSub ? [node.height / 2 - 5, node.height / 2 + 12] : [node.height / 2 + labelFontSize * 0.35];\n  }\n  const sub = hasSub\n",1)
    dst.mkdir(parents=True)
    shutil.copytree(args.archify,dst/'renderer',ignore=shutil.ignore_patterns('.git','node_modules','__pycache__'))
    (dst/'renderer/assets/template.html').write_text(template)
    (dst/'renderer/renderers/workflow/workflow-compiler.mjs').write_text(compiler)
    (dst/'candidate.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
    (dst/'learning-notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2))
    result = subprocess.run(['node',str(dst/'renderer/bin/archify.mjs'),'finalize','workflow',str(dst/'candidate.json'),str(dst/'board.html'),'--quality','showcase','--json'],cwd=dst.parent, env={**os.environ, 'ARCHIFY_UPDATE_CHECK_DISABLED': '1'})
    return result.returncode

if __name__ == '__main__':
    try:
        sys.exit(main())
    except (ValueError, OSError, KeyError) as exc:
        print(str(exc),file=sys.stderr)
        sys.exit(1)
