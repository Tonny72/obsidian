"""
Basic converter from a draw.io (mxGraphModel) file to a Mermaid flowchart.
- Extracts vertex cells with textual labels as nodes
- Extracts edge cells as links from source id to target id
- Produces a simple 'flowchart LR' Mermaid diagram

Limitations:
- This is a heuristic converter. Complex shapes, ports, styles, HTML labels may not convert cleanly.
- For HTML-like labels the script will strip tags and try to extract readable text.

Usage:
    python convert_drawio_to_mermaid.py sequentie.drawio sequentie.mmd

"""

import sys
import re
import xml.etree.ElementTree as ET
from html import unescape


def text_from_html_label(label):
    # labels in draw.io can be HTML fragments like '<div><font>Text</font></div>'
    # strip tags and unescape
    if label is None:
        return ''
    # remove xml/HTML tags
    text = re.sub(r'<[^>]+>', '', str(label))
    text = unescape(text)
    text = text.replace('\n', ' ').strip()
    return text


def parse_drawio(path):
    tree = ET.parse(path)
    root = tree.getroot()

    # find all mxCell elements
    cells = root.findall('.//mxCell')

    vertices = {}
    edges = []

    for c in cells:
        cid = c.get('id')
        value = c.get('value')
        # vertex attribute is represented as vertex="1"
        is_vertex = c.get('vertex') == '1'
        is_edge = c.get('edge') == '1'

        if is_vertex:
            label = text_from_html_label(value)
            # ensure label is string and non-empty; fallback to id
            if not label:
                vertices[cid] = str(cid)
            else:
                vertices[cid] = label
        elif is_edge:
            # edges may have source/target attributes
            source = c.get('source')
            target = c.get('target')
            edges.append((source, target, text_from_html_label(value)))

    return vertices, edges


def to_mermaid(vertices, edges, out_path):
    lines = ["flowchart LR"]

    # create safe ids and map
    id_map = {}
    existing = set()
    for vid, label in vertices.items():
        lbl = str(label)
        safe = re.sub(r'[^A-Za-z0-9_]', '_', lbl) or f'node_{vid}'
        # ensure unique
        if safe in existing:
            safe = f'{safe}_{vid}'
        existing.add(safe)
        id_map[vid] = safe
        # node line
        # use label in quotes if contains spaces or is empty
        esc = lbl.replace('"', '\\"')
        if ' ' in esc or esc == '':
            lines.append(f'    {safe}["{esc}"]')
        else:
            lines.append(f'    {safe}[{esc}]')

    for s, t, vlabel in edges:
        if s is None or t is None:
            continue
        if s not in id_map or t not in id_map:
            continue
        src = id_map[s]
        tgt = id_map[t]
        # if edge has label put it as |label|
        if vlabel:
            vl = str(vlabel).replace('"', '\\"')
            lines.append(f'    {src} --|{vl}|--> {tgt}')
        else:
            lines.append(f'    {src} --> {tgt}')

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


def main():
    if len(sys.argv) < 3:
        print('Usage: convert_drawio_to_mermaid.py input.drawio output.mmd')
        sys.exit(1)
    inp = sys.argv[1]
    out = sys.argv[2]

    vertices, edges = parse_drawio(inp)
    to_mermaid(vertices, edges, out)
    print(f'Wrote {out} with {len(vertices)} nodes and {len(edges)} edges')


if __name__ == '__main__':
    main()
