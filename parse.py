# TLDR; the cell must start with a ### and should have a code block following it

import json

with open('visualizations/Heatmap/Heatmaps.ipynb', 'r') as fp:
    notebook = json.load(fp)

lines = []
for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown' and cell['source'][0].startswith('### '):
        print(cell['source'])
        lines.extend(cell['source'])

with open('Heatmaps.md', 'w') as fp:
    for line in lines:
        if not line.endswith(r'\n'):
            fp.write(f'{line}\n')
    # fp.writelines(lines)
    # for line in lines:
    #     fp.write(line)

