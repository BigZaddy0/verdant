from pathlib import Path

root = Path(__file__).resolve().parent.parent
property_list = [
    {'slug':'desire-home','title':'Desire Home','image':'img/desirehome.jpg','location':'Ijanikin, Lagos State','price':'₦8.25M','status':'For Sale','summary':'A premium family estate with modern amenities and quick access to the city.'},
    {'slug':'harmony-home','title':'Harmony Home','image':'img/ibeji.png','location':'Eleranigbe b/s Ibeji Lekki, Lagos','price':'₦5M','status':'For Sale','summary':'A serene residential community designed for comfort, security, and harmony.'},
    {'slug':'iremide-gardens','title':'Iremide Gardens','image':'img/iremide.png','location':'Ibogun, Ifo','price':'₦2M','status':'For Sale','summary':'Well-planned garden estate offering a peaceful lifestyle near major transport links.'},
    {'slug':'move-ibafo','title':'Move/Ibafo','image':'img/move.png','location':'Mowe adjacent to Deeper Life Camp','price':'₦7M','status':'For Sale','summary':'Strategic plots close to premium road networks and future development zones.'},
    {'slug':'treasure-home','title':'Treasure Home','image':'img/comfort.jpg','location':'Abeokuta Rounda','price':'₦400K','status':'For Sale','summary':'Affordable land parcels with great resale value and secure neighbourhood.'},
    {'slug':'country-home','title':'Country Home','image':'img/property.jpg','location':'Atan Otta','price':'₦3.5M','status':'For Sale','summary':'Classic country living with spacious plots and elegant estate planning.'},
    {'slug':'country-home-extension','title':'Country Home Extension','image':'img/atan.png','location':'Atan Otta','price':'₦770K','status':'For Sale','summary':'Extension plots offering extra affordability in a trusted estate location.'},
    {'slug':'irewamiri-garden','title':'Irewamiri Garden','image':'img/header.jpg','location':'Papalatoro, Ilaro Road, Ogun State','price':'₦850K','status':'For Sale','summary':'A growing community built for families seeking value and security.'},
    {'slug':'new-life-garden','title':'New Life Garden','image':'img/sango.jpg','location':'Ekundayo, Ibogun, Coker b/s, Ogun State','price':'₦900K','status':'For Sale','summary':'Modern garden estate with strong infrastructure and neighbourhood charm.'},
    {'slug':'treasure-island','title':'Treasure Island','image':'img/treasure.jpg','location':'Ibeju Lekki','price':'₦15M','status':'For Sale','summary':'High-end waterfront-inspired development designed for premium buyers.'},
    {'slug':'iremide-garden','title':'Iremide Garden','image':'img/ibogun.jpg','location':'Beside OOU Engineering Campus, Ibogun Ifo Ogun State','price':'₦1.32M','status':'For Sale','summary':'Campus-adjacent estate ideal for investors and academic professionals.'},
    {'slug':'florish-home','title':'Florish Home','image':'img/header.jpg','location':'Itori, Ewekoro Ogun State','price':'₦595K','status':'For Sale','summary':'Economical estate in an emerging growth corridor of Ogun State.'},
    {'slug':'mega-city','title':'Mega City','image':'img/header.jpg','location':'Papa Ajegunle','price':'₦800K','status':'For Sale','summary':'Urban-supportive plot options positioned for fast neighbourhood expansion.'},
]

base_template = """<!DOCTYPE html>
<html lang=\"en\">

<head>
    <meta charset=\"utf-8\">
    <title>{title} | Verdant World Global Limited</title>
    <meta content=\"width=device-width, initial-scale=1.0\" name=\"viewport\">
    <meta content=\"{summary}\" name=\"description\">
    <link href=\"img/favicon.ico\" rel=\"icon\">
    <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
    <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
    <link href=\"https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600&family=Inter:wght@700;800&display=swap\" rel=\"stylesheet\">
    <link href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.0/css/all.min.css\" rel=\"stylesheet\">
    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.1/font/bootstrap-icons.css\" rel=\"stylesheet\">
    <link href=\"lib/animate/animate.min.css\" rel=\"stylesheet\">
    <link href=\"lib/owlcarousel/assets/owl.carousel.min.css\" rel=\"stylesheet\">
    <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">
    <link href=\"css/style.css\" rel=\"stylesheet\">
    <style>
        .property-hero-gallery .carousel-item img {{ height: 520px; object-fit: cover; }}
        .sticky-whatsapp-cta {{ position: fixed; right: 20px; bottom: 20px; z-index: 1050; }}
        .estate-faq .accordion-button::after {{ filter: invert(1); }}
    </style>
</head>

<body>
    <div class=\"container-xxl bg-white p-0\">
        <div class=\"container-fluid nav-bar bg-transparent\">
            <nav class=\"navbar navbar-expand-lg bg-white navbar-light py-0 px-4\">
                <a href=\"index.html\" class=\"navbar-brand d-flex align-items-center text-center\">
                    <h1 class=\"m-0 text-primary\">Verdant World</h1>
                </a>
                <button type=\"button\" class=\"navbar-toggler\" data-bs-toggle=\"collapse\" data-bs-target=\"#navbarCollapse\">
                    <span class=\"navbar-toggler-icon\"></span>
                </button>
                <div class=\"collapse navbar-collapse\" id=\"navbarCollapse\">
                    <div class=\"navbar-nav ms-auto\">
                        <a href=\"index.html\" class=\"nav-item nav-link\">Home</a>
                        <a href=\"about.html\" class=\"nav-item nav-link\">About</a>
                        <a href=\"property-list.html\" class=\"nav-item nav-link active\">Property List</a>
                        <a href=\"gallery.html\" class=\"nav-item nav-link\">Gallery</a>
                        <a href=\"contact.html\" class=\"nav-item nav-link\">Contact</a>
                    </div>
                    <a href=\"https://whas.me/GsfTPbvQek\" class=\"btn btn-primary px-3 d-none d-lg-flex\">Send DM</a>
                </div>
            </nav>
        </div>

        <div class=\"container-fluid header bg-white p-0\">
            <div class=\"row g-0 align-items-center flex-column-reverse flex-md-row\">
                <div class=\"col-md-6 p-5 mt-lg-5\">
                    <h1 class=\"display-5 animated fadeIn mb-4\">{title}</h1>
                    <p class=\"mb-4\">{summary}</p>
                    <nav aria-label=\"breadcrumb animated fadeIn\">
                        <ol class=\"breadcrumb text-uppercase\">
                            <li class=\"breadcrumb-item\"><a href=\"index.html\">Home</a></li>
                            <li class=\"breadcrumb-item\"><a href=\"property-list.html\">Property List</a></li>
                            <li class=\"breadcrumb-item text-body active\" aria-current=\"page\">{title}</li>
                        </ol>
                    </nav>
                </div>
                <div class=\"col-md-6 animated fadeIn\">
                    <img class=\"img-fluid\" src=\"{image}\" alt=\"{title}\">
                </div>
            </div>
        </div>

        <div class=\"container-xxl py-5\">
            <div class=\"container\">
                <div class=\"row g-4\">
                    <div class=\"col-lg-7\">
                        <div class=\"property-hero-gallery owl-carousel owl-theme mb-5\">
                            <div class=\"item\"><img src=\"{image}\" class=\"img-fluid rounded\" alt=\"{title}\"></div>
                            <div class=\"item\"><img src=\"img/header.jpg\" class=\"img-fluid rounded\" alt=\"Estate view\"></div>
                            <div class=\"item\"><img src=\"img/bg1.png\" class=\"img-fluid rounded\" alt=\"Estate view\"></div>
                        </div>
                        <div class=\"mb-5\">
                            <h2>Virtual Tour</h2>
                            <div class=\"ratio ratio-16x9\">
                                <iframe src=\"https://www.youtube.com/embed/ScMzIvxBSi4\" title=\"Virtual Tour\" allowfullscreen></iframe>
                            </div>
                        </div>
                        <div class=\"mb-5\">
                            <h2>Amenities</h2>
                            <div class=\"row g-3\">
                                <div class=\"col-sm-6\">
                                    <ul class=\"list-unstyled\">
                                        <li><i class=\"fa fa-check text-primary me-2\"></i>24/7 Security</li>
                                        <li><i class=\"fa fa-check text-primary me-2\"></i>Good road network</li>
                                        <li><i class=\"fa fa-check text-primary me-2\"></i>Drainage system</li>
                                    </ul>
                                </div>
                                <div class=\"col-sm-6\">
                                    <ul class=\"list-unstyled\">
                                        <li><i class=\"fa fa-check text-primary me-2\"></i>Street lighting</li>
                                        <li><i class=\"fa fa-check text-primary me-2\"></i>Recreational park</li>
                                        <li><i class=\"fa fa-check text-primary me-2\"></i>Community shopping area</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class=\"mb-5\">
                            <h2>Payment Plans</h2>
                            <div class=\"table-responsive\">
                                <table class=\"table table-bordered\">
                                    <thead>
                                        <tr>
                                            <th>Plan</th>
                                            <th>Duration</th>
                                            <th>Deposit</th>
                                            <th>Monthly</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr><td>Standard</td><td>12 months</td><td>30%</td><td>Flexible</td></tr>
                                        <tr><td>Premium</td><td>18 months</td><td>25%</td><td>Lower monthly</td></tr>
                                        <tr><td>Investor</td><td>24 months</td><td>20%</td><td>Best value</td></tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div class=\"mb-5\">
                            <h2>Plot Sizes & Prices</h2>
                            <div class=\"row g-3\">
                                <div class=\"col-md-4\"><div class=\"bg-light rounded p-4\"><h5>200 SQM</h5><p>{price} from 200 SQM</p></div></div>
                                <div class=\"col-md-4\"><div class=\"bg-light rounded p-4\"><h5>300 SQM</h5><p>Price varies by sector</p></div></div>
                                <div class=\"col-md-4\"><div class=\"bg-light rounded p-4\"><h5>450 SQM</h5><p>Most popular size</p></div></div>
                            </div>
                        </div>
                        <div class=\"mb-5\">
                            <h2>Nearby Landmarks</h2>
                            <ul class=\"list-unstyled\">
                                <li><i class=\"fa fa-map-marker-alt text-primary me-2\"></i>Nearby market and shops</li>
                                <li><i class=\"fa fa-map-marker-alt text-primary me-2\"></i>School within 5 minutes</li>
                                <li><i class=\"fa fa-map-marker-alt text-primary me-2\"></i>Health centre nearby</li>
                                <li><i class=\"fa fa-map-marker-alt text-primary me-2\"></i>Easy motorway access</li>
                            </ul>
                        </div>
                        <div class=\"mb-5\">
                            <h2>Estate Layout Plan</h2>
                            <img src=\"img/header.jpg\" class=\"img-fluid rounded\" alt=\"Estate layout plan\">
                        </div>
                    </div>
                    <div class=\"col-lg-5\">
                        <div class=\"bg-light rounded p-4 mb-5\">
                            <h2>Quick facts</h2>
                            <p><strong>Location:</strong> {location}</p>
                            <p><strong>Price:</strong> {price}</p>
                            <p><strong>Status:</strong> {status}</p>
                            <p><strong>Plot range:</strong> 200–450 SQM</p>
                        </div>
                        <div class=\"estate-faq mb-5\">
                            <h2>FAQs</h2>
                            <div class=\"accordion\" id=\"faqAccordion\">
                                <div class=\"accordion-item\">
                                    <h2 class=\"accordion-header\" id=\"faqOne\">
                                        <button class=\"accordion-button collapsed\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#collapseOne\" aria-expanded=\"false\" aria-controls=\"collapseOne\">
                                            What is the minimum deposit?
                                        </button>
                                    </h2>
                                    <div id=\"collapseOne\" class=\"accordion-collapse collapse\" aria-labelledby=\"faqOne\" data-bs-parent=\"#faqAccordion\">
                                        <div class=\"accordion-body\">A minimum deposit of 20–30% secures your plot.</div>
                                    </div>
                                </div>
                                <div class=\"accordion-item\">
                                    <h2 class=\"accordion-header\" id=\"faqTwo\">
                                        <button class=\"accordion-button collapsed\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#collapseTwo\" aria-expanded=\"false\" aria-controls=\"collapseTwo\">
                                            Are titles ready?
                                        </button>
                                    </h2>
                                    <div id=\"collapseTwo\" class=\"accordion-collapse collapse\" aria-labelledby=\"faqTwo\" data-bs-parent=\"#faqAccordion\">
                                        <div class=\"accordion-body\">Yes, titles can be issued upon full payment and documentation.</div>
                                    </div>
                                </div>
                                <div class=\"accordion-item\">
                                    <h2 class=\"accordion-header\" id=\"faqThree\">
                                        <button class=\"accordion-button collapsed\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"#collapseThree\" aria-expanded=\"false\" aria-controls=\"collapseThree\">
                                            Can I view the estate before purchase?
                                        </button>
                                    </h2>
                                    <div id=\"collapseThree\" class=\"accordion-collapse collapse\" aria-labelledby=\"faqThree\" data-bs-parent=\"#faqAccordion\">
                                        <div class=\"accordion-body\">Absolutely. Schedule a site visit through the enquiry form.</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class=\"mb-5\">
                            <h2>Enquiry</h2>
                            <form>
                                <div class=\"mb-3\"><input type=\"text\" class=\"form-control\" placeholder=\"Full name\"></div>
                                <div class=\"mb-3\"><input type=\"email\" class=\"form-control\" placeholder=\"Email address\"></div>
                                <div class=\"mb-3\"><input type=\"tel\" class=\"form-control\" placeholder=\"Phone number\"></div>
                                <div class=\"mb-3\"><textarea class=\"form-control\" rows=\"4\" placeholder=\"Tell us what you need\"></textarea></div>
                                <button class=\"btn btn-primary w-100 py-3\" type=\"submit\">Submit Enquiry</button>
                            </form>
                        </div>
                        <div class=\"sticky-whatsapp-cta\">
                            <a href=\"https://whas.me/GsfTPbvQek\" target=\"_blank\" class=\"btn btn-success btn-lg rounded-pill\"><i class=\"fab fa-whatsapp me-2\"></i>Chat on WhatsApp</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class=\"container-xxl py-5 bg-light\">
            <div class=\"container\">
                <div class=\"text-center mb-5\">
                    <h2>Similar Properties</h2>
                    <p>Other estates you may like.</p>
                </div>
                <div class=\"row g-4\">{similar_html}
                </div>
            </div>
        </div>

        <div class=\"container-fluid bg-dark text-white-50 footer pt-5 mt-5 wow fadeIn\" data-wow-delay=\"0.1s\">
            <div class=\"container py-5\">
                <div class=\"row g-5\">
                    <div class=\"col-lg-3 col-md-6\">
                        <h5 class=\"text-white mb-4\">Get In Touch</h5>
                        <p class=\"mb-2\"><i class=\"fa fa-map-marker-alt me-3\"></i>KM 38, Abeokuta Express way, Moshalashi, Lagos.</p>
                        <p class=\"mb-2\"><i class=\"fa fa-phone-alt me-3\"></i>0813 670 8583</p>
                        <p class=\"mb-2\"><i class=\"fa fa-envelope me-3\"></i>info@verdantworld.com</p>
                    </div>
                    <div class=\"col-lg-3 col-md-6\">
                        <h5 class=\"text-white mb-4\">Quick Links</h5>
                        <a class=\"btn btn-link text-white-50\" href=\"about.html\">About Us</a>
                        <a class=\"btn btn-link text-white-50\" href=\"contact.html\">Contact Us</a>
                        <a class=\"btn btn-link text-white-50\" href=\"property-list.html\">Property List</a>
                    </div>
                </div>
            </div>
            <div class=\"container\">
                <div class=\"copyright\">
                    <div class=\"row\">
                        <div class=\"col-md-6 text-center text-md-start mb-3 mb-md-0\">&copy; <a class=\"border-bottom\" href=\"#\">Verdant World Global Limited</a>, All Right Reserved.</div>
                    </div>
                </div>
            </div>
        </div>

        <a href=\"#\" class=\"btn btn-lg btn-primary btn-lg-square back-to-top\"><i class=\"bi bi-arrow-up\"></i></a>
    </div>

    <script src=\"https://code.jquery.com/jquery-3.4.1.min.js\"></script>
    <script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js\"></script>
    <script src=\"lib/wow/wow.min.js\"></script>
    <script src=\"lib/easing/easing.min.js\"></script>
    <script src=\"lib/waypoints/waypoints.min.js\"></script>
    <script src=\"lib/owlcarousel/owl.carousel.min.js\"></script>
    <script>
        $('.property-hero-gallery').owlCarousel({{
            loop:true,
            margin:10,
            items:1,
            nav:true,
            dots:true,
            autoplay:true,
            autoplayTimeout:4000,
            autoplayHoverPause:true
        }});
    </script>
</body>
</html>
"""

for idx, item in enumerate(property_list):
    others = [property_list[(idx + 1 + j) % len(property_list)] for j in range(3)]
    similar_html = ''.join(f"""
                    <div class=\"col-md-4 mb-4\">
                        <div class=\"property-item rounded overflow-hidden\">
                            <div class=\"position-relative overflow-hidden\">
                                <a href=\"property-{o['slug']}.html\"><img class=\"img-fluid\" src=\"{o['image']}\" alt=\"{o['title']}\"></a>
                                <div class=\"bg-primary rounded text-white position-absolute start-0 top-0 m-4 py-1 px-3\">{o['status']}</div>
                            </div>
                            <div class=\"p-4 pb-0\">
                                <h5 class=\"text-primary mb-3\">{o['price']}</h5>
                                <a class=\"d-block h5 mb-2\" href=\"property-{o['slug']}.html\">{o['title']}</a>
                                <p><i class=\"fa fa-map-marker-alt text-primary me-2\"></i>{o['location']}</p>
                            </div>
                        </div>
                    </div>
    """ for o in others)
    html = base_template.format(
        title=item['title'],
        summary=item['summary'],
        image=item['image'],
        price=item['price'],
        location=item['location'],
        status=item['status'],
        similar_html=similar_html,
    )
    (root / f"property-{item['slug']}.html").write_text(html, encoding='utf-8')

property_list_path = root / 'property-list.html'
content = property_list_path.read_text(encoding='utf-8')
for item in property_list:
    content = content.replace(f'<a class="d-block h5 mb-2" href="">{item["title"]}</a>', f'<a class="d-block h5 mb-2" href="property-{item["slug"]}.html">{item["title"]}</a>')
    content = content.replace(f'<a href=""><img class="img-fluid" src="{item["image"]}"', f'<a href="property-{item["slug"]}.html"><img class="img-fluid" src="{item["image"]}"')
property_list_path.write_text(content, encoding='utf-8')
print('Generated', len(property_list), 'property pages.')
