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

property_files = ['index.html', 'property-list.html']

for file_name in property_files:
    path = root / file_name
    content = path.read_text(encoding='utf-8')
    original = content

    def patch_block(match):
        block = match.group(0)
        title_match = re.search(r'<a[^>]+class="(?:property-title|d-block h5 mb-2)[^>]*"[^>]*href="([^"]*)"[^>]*>([^<]+)</a>', block)
        if not title_match:
            return block
        url = title_match.group(1).strip()
        title = title_match.group(2).strip()
        if not url or url == '#':
            url = slug_map.get(title, url)
        if url:
            # Fix image anchor hrefs if blank or wrong
            block = re.sub(r'(<a[^>]+href=")[^"]*("[^>]*>\s*<img)', rf'\1{url}\2', block, count=1)
        if 'View Property' not in block and url:
            # add button before closing div of property-info or p-4 pb-0
            section_match = re.search(r'(<div class="(?:property-info|p-4 pb-0)">[\s\S]*?</div>)', block)
            if section_match:
                section = section_match.group(1)
                if 'View Property' not in section:
                    block = block.replace(section, section[:-6] + BUTTON_HTML.format(url=url) + '</div>', 1)
        return block

    content = re.sub(r'<div class="property-item[\s\S]*?</div>\s*</div>', patch_block, content)

    # Specific correction for a malformed merged href
    content = content.replace('href="property-mega-city.htmlproperty-florish-home.html"', 'href="property-florish-home.html"')

    if content != original:
        path.write_text(content, encoding='utf-8')
        print(f'Updated {file_name}')
    else:
        print(f'No changes for {file_name}')
