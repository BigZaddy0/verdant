from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
slug_map = {
    'Desire Home': 'property-desire-home.html',
    'Harmony Home': 'property-harmony-home.html',
    'Iremide Gardens': 'property-iremide-gardens.html',
    'Move/Ibafo': 'property-move-ibafo.html',
    'Treasure Home': 'property-treasure-home.html',
    'Country Home': 'property-country-home.html',
    'Country Home Extension': 'property-country-home-extension.html',
    'Irewamiri Garden': 'property-irewamiri-garden.html',
    'New Life Garden': 'property-new-life-garden.html',
    'Treasure Island': 'property-treasure-island.html',
    'Iremide Garden': 'property-iremide-garden.html',
    'Florish Home': 'property-florish-home.html',
    'Mega City': 'property-mega-city.html',
}

BUTTON_HTML = '                                        <a href="{url}" class="btn btn-primary mt-3">View Property</a>\n'


def find_block_end(text: str, start_idx: int) -> int:
    depth = 0
    idx = start_idx
    while idx < len(text):
        next_open = text.find('<div', idx)
        next_close = text.find('</div>', idx)
        if next_close == -1:
            return -1
        if next_open != -1 and next_open < next_close:
            depth += 1
            idx = next_open + 4
        else:
            depth -= 1
            idx = next_close + 6
            if depth == 0:
                return idx
    return -1


def patch_property_item(block: str) -> str:
    title_match = re.search(r'<a[^>]+class="(?:property-title|d-block h5 mb-2)[^"]*"[^>]*href="([^"]*)"[^>]*>([^<]+)</a>', block)
    if not title_match:
        return block
    url = title_match.group(1).strip()
    title = title_match.group(2).strip()
    if not url or url == '#':
        url = slug_map.get(title, url)
    if url and url != '#':
        block = re.sub(r'(<a[^>]*href=")[^"]*("[^>]*>\s*<img)', rf'\1{url}\2', block, count=1)
        if 'View Property' not in block:
            # insert button in property-info or p-4 pb-0
            for section_class in ['property-info', 'p-4 pb-0']:
                start = block.find(f'<div class="{section_class}">')
                if start != -1:
                    end = find_block_end(block, start)
                    if end != -1:
                        inner = block[start:end]
                        if 'View Property' not in inner:
                            block = block[:end-6] + BUTTON_HTML.format(url=url) + block[end-6:]
                        break
    return block


for file_name in ['property-list.html', 'index.html']:
    path = root / file_name
    text = path.read_text(encoding='utf-8')
    orig = text
    blocks = list(re.finditer(r'<div class="property-item[\s\S]*?</div>\s*</div>', text))
    if not blocks:
        print(f'No property-item blocks found in {file_name}')
        continue
    new_text = ''
    last = 0
    for m in blocks:
        new_text += text[last:m.start()]
        block = m.group(0)
        new_text += patch_property_item(block)
        last = m.end()
    new_text += text[last:]
    if new_text != orig:
        path.write_text(new_text, encoding='utf-8')
        print(f'Patched {file_name}')
    else:
        print(f'No changes for {file_name}')
