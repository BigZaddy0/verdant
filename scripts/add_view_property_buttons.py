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

button_html = '                                        <a href="{url}" class="btn btn-primary mt-3">View Property</a>\n'

changes = []

for path in sorted(root.glob('*.html')):
    text = path.read_text(encoding='utf-8')
    orig = text

    # patch title hrefs using known slugs
    for title, url in slug_map.items():
        text = re.sub(
            rf'(<a[^>]+class="[^"]*property-title[^"]*"[^>]*href=")[^"]*("[^>]*>{re.escape(title)}</a>)',
            rf'\1{url}\2',
            text,
        )
        text = re.sub(
            rf'(<a[^>]+class="[^"]*d-block h5 mb-2[^"]*"[^>]*href=")[^"]*("[^>]*>{re.escape(title)}</a>)',
            rf'\1{url}\2',
            text,
        )

    # patch image links within property-item blocks if blank and title is known
    def patch_image_block(match):
        block = match.group(0)
        title_match = re.search(r'<a[^>]+class="[^"]*(?:property-title|d-block h5 mb-2)[^"]*"[^>]*href="([^"]*)"[^>]*>([^<]+)</a>', block)
        if not title_match:
            return block
        title = title_match.group(2).strip()
        url = slug_map.get(title)
        if not url:
            return block
        block_new = re.sub(r'(<a[^>]*href=")[^"]*("[^>]*>\s*<img)', rf'\1{url}\2', block)
        return block_new

    text = re.sub(r'<div class="property-item[\s\S]*?</div>\s*</div>', patch_image_block, text)

    # add View Property button if missing in property-info / p-4 pb-0 blocks
    def add_button(match):
        block = match.group(0)
        if 'View Property' in block:
            return block
        title_match = re.search(r'<a[^>]+href="([^"]+)"[^>]*>([^<]+)</a>', block)
        if not title_match:
            return block
        url = title_match.group(1)
        if not url or url == '#':
            title = title_match.group(2).strip()
            url = slug_map.get(title, url)
        if url and url != '#':
            # insert button before closing div
            return block.replace('</div>', button_html.format(url=url) + '</div>', 1)
        return block

    text = re.sub(r'(<div class="(?:property-info|p-4 pb-0)">[\s\S]*?</div>)', add_button, text)

    if text != orig:
        changes.append(path.name)
        path.write_text(text, encoding='utf-8')

print('Updated files:', ', '.join(changes))
