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


def find_div_block(text: str, start: int) -> int:
    depth = 0
    pos = start
    while True:
        open_match = re.search(r'<div\b', text[pos:])
        close_match = re.search(r'</div>', text[pos:])
        if not close_match:
            return -1
        close_pos = pos + close_match.start()
        if open_match and open_match.start() < close_match.start():
            depth += 1
            pos = start + open_match.end()
            if pos <= start:
                pos = close_pos + 6
        else:
            depth -= 1
            pos = close_pos + 6
            if depth < 0:
                return pos


def patch_block(block: str) -> str:
    title_match = re.search(r'<a[^>]+class="(?:property-title|d-block h5 mb-2)[^"]*"[^>]*href="([^"]*)"[^>]*>([^<]+)</a>', block)
    if not title_match:
        return block
    url = title_match.group(1).strip()
    title = title_match.group(2).strip()
    if not url or url == '#':
        url = slug_map.get(title, url)
    if url and 'href=""' in block:
        block = re.sub(r'(<a[^>]*?)href=""([^>]*>\s*<img[^>]*>)', rf'\1href="{url}"\2', block, count=1)
    if 'View Property' not in block and url and url != '#':
        insert_pos = None
        for section in ['property-info', 'p-4 pb-0']:
            match = re.search(rf'(<div class="{section}">[\s\S]*?</div>)', block)
            if match:
                insert_pos = match.end() - len('</div>')
                break
        if insert_pos is not None:
            block = block[:insert_pos] + BUTTON_HTML.format(url=url) + block[insert_pos:]
    return block


for file_name in ['property-list.html', 'index.html']:
    file_path = root / file_name
    content = file_path.read_text(encoding='utf-8')
    result = ''
    pos = 0
    while True:
        start = content.find('<div class="property-item', pos)
        if start == -1:
            result += content[pos:]
            break
        result += content[pos:start]
        end = find_div_block(content, start)
        if end == -1:
            result += content[start:]
            break
        block = content[start:end]
        patched = patch_block(block)
        result += patched
        pos = end
    if result != content:
        file_path.write_text(result, encoding='utf-8')
        print(f'Patched {file_name}')
    else:
        print(f'No changes for {file_name}')
