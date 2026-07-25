from pathlib import Path

root = Path(__file__).resolve().parent.parent
replacements = {
    'index.html': {
        '<a href=""><img class="img-fluid" src="img/desirehome.jpg" alt=""></a>': '<a href="property-desire-home.html"><img class="img-fluid" src="img/desirehome.jpg" alt=""></a>',
        '<a href=""><img class="img-fluid" src="img/ibeji.png" ></a>': '<a href="property-harmony-home.html"><img class="img-fluid" src="img/ibeji.png" ></a>',
        '<a href=""><img class="img-fluid" src="img/iremide.png" alt=""></a>': '<a href="property-iremide-gardens.html"><img class="img-fluid" src="img/iremide.png" alt=""></a>',
        '<a href=""><img class="img-fluid" src="img/move.png" alt=""></a>': '<a href="property-move-ibafo.html"><img class="img-fluid" src="img/move.png" alt=""></a>',
        '<a href=""><img class="img-fluid" src="img/comfort.jpg" alt=""></a>': '<a href="property-treasure-home.html"><img class="img-fluid" src="img/comfort.jpg" alt=""></a>',
        '<a href=""><img class="img-fluid" src="img/property.jpg" alt=""></a>': '<a href="property-country-home.html"><img class="img-fluid" src="img/property.jpg" alt=""></a>',
        '<a href=""><img class="img-fluid" src="img/atan.png" alt=""></a>': '<a href="property-country-home-extension.html"><img class="img-fluid" src="img/atan.png" alt=""></a>',
        '<a href=""><img class="img-fluid" src="" alt="Itori"></a>': '<a href="property-irewamiri-garden.html"><img class="img-fluid" src="" alt="Itori"></a>',
        '<a href=""><img class="img-fluid" src="img/sango.jpg" alt=""></a>': '<a href="property-new-life-garden.html"><img class="img-fluid" src="img/sango.jpg" alt=""></a>',
        '<a href=""><img class="img-fluid" src="img/treasure.jpg" alt=""></a>': '<a href="property-treasure-island.html"><img class="img-fluid" src="img/treasure.jpg" alt=""></a>',
        '<a href=""><img class="img-fluid" src="img/ibogun.jpg" alt=""></a>': '<a href="property-iremide-garden.html"><img class="img-fluid" src="img/ibogun.jpg" alt=""></a>',
        '<a href=""><img class="img-fluid" src="" alt=""></a>': None,  # handle later for ambiguous matches
    },
    'property-list.html': {
        '<a href=""><img class="img-fluid" src="" alt="Itori"></a>': '<a href="property-irewamiri-garden.html"><img class="img-fluid" src="" alt="Itori"></a>',
        '<a href=""><img class="img-fluid" src="" alt=""></a>': None,
    },
}
# Specific unambiguous replacements by context
property_specific = [
    ('index.html', '<a href=""><img class="img-fluid" src="" alt=""></a>', '<a href="property-florish-home.html"><img class="img-fluid" src="" alt=""></a>', 'Florish Home'),
    ('index.html', '<a href=""><img class="img-fluid" src="" alt=""></a>', '<a href="property-mega-city.html"><img class="img-fluid" src="" alt=""></a>', 'Mega City'),
    ('property-list.html', '<a href=""><img class="img-fluid" src="" alt=""></a>', '<a href="property-florish-home.html"><img class="img-fluid" src="" alt=""></a>', 'Florish Home'),
    ('property-list.html', '<a href=""><img class="img-fluid" src="" alt=""></a>', '<a href="property-mega-city.html"><img class="img-fluid" src="" alt=""></a>', 'Mega City'),
]

for file_name, map_data in replacements.items():
    path = root / file_name
    content = path.read_text(encoding='utf-8')
    original = content
    for old, new in map_data.items():
        if new is None:
            continue
        content = content.replace(old, new)
    # ambiguous blank src replacements by title context
    for fn, old, new, title in property_specific:
        if fn != file_name:
            continue
        if old not in content:
            continue
        loc = content.find(title)
        if loc != -1:
            # ensure near the title we have the blank image anchor
            start = content.rfind('<a href=""><img class="img-fluid" src="" alt=""></a>', 0, loc)
            if start != -1 and content.find(old, start, loc) != -1:
                content = content.replace(old, new, 1)
    if content != original:
        path.write_text(content, encoding='utf-8')
        print(f'Updated {file_name}')
    else:
        print(f'No changes in {file_name}')
