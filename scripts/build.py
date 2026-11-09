"""Builds Rodrigo Blanco's personal site (EN at /, ES at /es/) into ../rodrigo-site.

Facts come from terrafunded/terrafunded scripts/_company.data.mjs and the
founder profile copy (src/locales/*/common.json, author.*). Keep them in sync.
Land photos come from the TerraFunded properties table (property-images bucket).

Usage: python3 build.py https://esrodrigoblanco.com
"""
import json, html, sys, pathlib

SITE = sys.argv[1] if len(sys.argv) > 1 else "https://esrodrigoblanco.com"
OUT = pathlib.Path(__file__).resolve().parent.parent
TF = "https://terrafunded.com"
LINKEDIN = "https://www.linkedin.com/in/rodrigoblancomarroquin/"
INSTAGRAM = "https://www.instagram.com/esrodrigoblanco/"
TF_PERSON = f"{TF}/authors/rodrigo-blanco"
EMAIL = "rodrigo@terrafunded.com"
PHONE = "(216) 630-4560"
PHONE_E164 = "+12166304560"
ADDRESS = "3838 Oak Lawn Avenue, Suite 1000, Dallas, TX 75219"
MODIFIED = "2026-11-08"

PRESS = [
    ("The Title Report", {"en": "Apr 30, 2026", "es": "30 abr 2026"},
     "TerraFunded eclipses $15 million in cumulative land sales",
     "https://www.thetitlereport.com/TTR/Articles/97176.aspx", "article"),
    ("XPR Media", {"en": "May 8, 2026", "es": "8 may 2026"},
     "Rodrigo Blanco's TerraFunded Launches Bilingual Land Buyer Education Platform",
     "https://xpr.media/?p=788051", "release"),
    ("National Law Review", {"en": "Apr 2026", "es": "abr 2026"},
     "TerraFunded Surpasses $15M in Texas Land Sales, Serving 350+ U.S. Families",
     "https://natlawreview.com/press-releases/terrafunded-surpasses-15m-texas-land-sales-serving-350-us-families", "release"),
    ("The Weekly Voice", {"en": "Apr 2026", "es": "abr 2026"},
     "TerraFunded Surpasses $15M in Texas Land Sales, Serving 350+ U.S. Families",
     "https://weeklyvoice.com/terrafunded-surpasses-15m-in-texas-land-sales-serving-350-u-s-families/", "release"),
]

ARTICLES = [
    ("Owner-Financed Land in Texas: The Complete 2026 Guide", f"{TF}/owner-financed-land-texas", ("Guide", "Guía")),
    ("How to Verify Any Texas Land Seller Is Legitimate: The 7 Free Checks I Tell My Own Buyers to Run on Me", f"{TF}/blog/how-to-verify-texas-land-seller-legitimate-2026", ("Trust", "Confianza")),
    ("Owner Financing vs Bank Mortgage for Texas Land: The Real Math Nobody Shows You", f"{TF}/blog/owner-financing-vs-bank-mortgage-texas-land-2026", ("Financing", "Financiamiento")),
    ("What Happens If You Stop Paying on Owner-Financed Land in Texas? The Honest Answer", f"{TF}/blog/stop-paying-owner-financed-land-texas-2026", ("Financing", "Financiamiento")),
    ("Warranty Deed vs Contract for Deed vs Rent-to-Own in Texas", f"{TF}/blog/warranty-deed-vs-contract-for-deed-texas-2026", ("Legal", "Legal")),
    ("How Much Does 10 Acres of Land Cost in Texas? Real 2026 Prices by Region", f"{TF}/blog/how-much-does-10-acres-cost-texas-2026", ("Market", "Mercado")),
]

# (file, width, height, EN caption, ES caption, grid class)
LAND = [
    ("coryell-county", 1200, 899, "Coryell County", "Condado de Coryell", "tall"),
    ("franklin-county", 1200, 542, "Franklin County", "Condado de Franklin", ""),
    ("red-river-county", 1200, 542, "Red River County", "Condado de Red River", ""),
    ("eastland-county", 1200, 542, "Eastland County", "Condado de Eastland", ""),
    ("titus-county", 1200, 800, "Titus County", "Condado de Titus", "tall"),
    ("cass-county", 1200, 664, "Cass County", "Condado de Cass", ""),
    ("titus-county-lake", 1200, 664, "Titus County", "Condado de Titus", ""),
]

T = {
 "en": {
  "lang": "en", "locale": "en_US", "path": "/", "other": "/es/", "other_label": "ES",
  "title": "Rodrigo Blanco | Founder & CEO of TerraFunded",
  "desc": "Rodrigo Blanco is the founder and CEO of TerraFunded, a Dallas company that sells rural Texas land directly to buyers with owner financing. 350+ land transactions and $15M+ in sales.",
  "nav": [("story", "Story"), ("vision", "Vision"), ("writing", "Writing"), ("press", "Press"), ("contact", "Contact")],
  "eyebrow": "Founder & CEO, TerraFunded",
  "lede": "I help people own rural Texas land without depending on a bank. Every sale closes at a licensed title company with a Warranty Deed, so the buyer owns the land from day one.",
  "cta1": "Visit TerraFunded", "cta2": "Follow on Instagram",
  "loc": "Dallas, Texas",
  "stats": [("350+", "land transactions closed"), ("$15M+", "in cumulative land sales"), ("40%", "of buyers are Hispanic or Latino"), ("2019", "building the owner-financing model")],
  "stats_note": "TerraFunded figures as of April 2026, as reported by",
  "band": "Land is where families build. My job is to make sure it's theirs from the first day.",
  "band_cap": "TerraFunded land in Young County, Texas",
  "story_k": "Story", "story_h": "From Guatemala to Texas land",
  "story_intro": "Rodrigo Blanco is the founder and CEO of TerraFunded, a Dallas-based company that sells rural Texas land directly to buyers with owner financing. He built it together with his wife and co-founder, Luisa de Blanco.",
  "timeline": [
   ("Origin", "Born in Guatemala", "Rodrigo is Guatemalan and builds his businesses in the United States. He works in English and Spanish, and still answers buyers personally in both."),
   ("2019", "Portafolio Diversificado", "Rodrigo and Luisa co-found Portafolio Diversificado, focused on residential real estate in the United States. It's where he starts developing the seller-financing model that later defines TerraFunded."),
   ("2020", "TerraFunded", "They found TerraFunded, a separate company that subdivides rural Texas land into parcels of about 10 acres and sells them directly to buyers with owner financing and a Warranty Deed."),
   ("2026", "350+ transactions, $15M+ in sales", "TerraFunded passes $15 million in cumulative land sales across Texas counties such as Lamar, Young, Titus, Cass, Clay and Coryell, as reported by The Title Report."),
   ("Today", "Technology built in-house", "Rodrigo leads a bilingual team of more than a dozen people that builds its own software with AI, including TerraFunded GPS, which shows buyers their lot lines through the phone camera."),
  ],
  "facts_h": "Quick facts",
  "facts": [("Full name", "Rodrigo Blanco Marroquín"), ("Role", "Founder & CEO, TerraFunded, LLC"), ("Co-founder", "Luisa de Blanco, his wife"), ("Office", ADDRESS), ("Focus", "Owner-financed rural land in Texas"), ("Languages", "English and Spanish")],
  "vision_k": "Vision", "vision_h": "How I think about this business",
  "vision": [
   ("Own it from day one.", "I don't sell with a contract for deed or rent-to-own. If you're paying for land, it should be in your name from the closing table, with title insurance, at an independent title company."),
   ("Judge the person, not the paperwork.", "Many good buyers have the income and the discipline but don't fit a bank's file. Financing the land ourselves lets more people own it, under a fixed-rate note with no prepayment penalty."),
   ("An old industry, new tools.", "Rural land is one of the least digital industries in America. We build our own software with AI, from finding land to letting a buyer stand on a lot and see its boundaries through a phone camera."),
   ("Speak the buyer's language.", "Contracts, guides and support in English and Spanish, so every buyer understands exactly what they sign."),
   ("It's not acres. It's where a family builds.", "This fall I watched a buyer raising his house with his own hands on land he bought from us. That's what this business is for."),
  ],
  "tech_links": [("TerraFunded GPS", f"{TF}/gps"), ("TerraFunded Overview", "https://overview.terrafunded.com")],
  "adn_k": "DNA", "adn_h": "What drives everything I build", "adn": ["God", "Purpose", "Entrepreneurship"],
  "land_k": "Land", "land_h": "Where TerraFunded buyers build",
  "writing_k": "Writing", "writing_h": "Guides I've written for land buyers", "writing_all": "All articles on the TerraFunded blog",
  "press_k": "Press", "press_h": "Press and mentions", "press_type": {"article": "Article", "release": "Press release"},
  "kit_h": "Press kit", "kit_p": "Bios and photos ready to use in articles, podcasts and event programs.",
  "kit_short": "Short bio", "kit_long": "Long bio", "kit_copy": "Copy", "kit_copied": "Copied",
  "kit_photo": "Headshot (JPG)", "kit_logo": "Logo (SVG)", "kit_logo_w": "Logo, white (SVG)",
  "bio_short": "Rodrigo Blanco is the founder and CEO of TerraFunded, a Dallas-based company that sells rural Texas land directly to buyers with owner financing. TerraFunded has closed more than 350 land transactions and passed $15 million in cumulative sales.",
  "bio_long": "Rodrigo Blanco is the founder and CEO of TerraFunded, a Dallas-based company that sells rural Texas land directly to buyers with owner financing and a Warranty Deed at closing. Born in Guatemala, he has been developing the seller-financing land model since 2019 and founded TerraFunded in 2020 with his wife and co-founder, Luisa de Blanco. Under his leadership, TerraFunded has closed more than 350 land transactions and passed $15 million in cumulative sales, mostly parcels of about 10 acres across Texas counties such as Lamar, Young, Titus, Cass, Clay and Coryell. About 40% of TerraFunded's buyers are Hispanic or Latino. Rodrigo leads a bilingual team that builds the company's own technology with AI, including TerraFunded GPS, which shows buyers their lot lines through a phone camera. He speaks English and Spanish. More at esrodrigoblanco.com.",
  "faq_k": "FAQ", "faq_h": "Common questions",
  "faq": [
   ("Who is Rodrigo Blanco?", "Rodrigo Blanco (Rodrigo Blanco Marroquín) is the founder and CEO of TerraFunded, a Dallas-based company that sells rural Texas land directly to buyers with owner financing. TerraFunded has closed more than 350 land transactions and passed $15 million in cumulative sales."),
   ("Who owns TerraFunded?", "TerraFunded, LLC was founded in 2020 by Rodrigo Blanco and his wife and co-founder, Luisa de Blanco. Rodrigo serves as Founder & CEO."),
   ("Is TerraFunded the same company as Portafolio Diversificado?", "No. Rodrigo and Luisa Blanco co-founded both, but they are separate companies. TerraFunded, LLC sells rural Texas land with owner financing. Portafolio Diversificado is focused on residential real estate."),
   ("Where is TerraFunded based?", f"TerraFunded's office is at {ADDRESS}. Its land is in rural Texas counties such as Lamar, Young, Titus, Cass, Clay and Coryell."),
   ("How can I verify that TerraFunded is legitimate?", "Every sale closes at an independent, licensed Texas title company, and the buyer receives a recorded Warranty Deed. TerraFunded publishes a step-by-step verification guide at terrafunded.com/verify-terrafunded."),
   ("How do I contact Rodrigo Blanco?", f"By text at {PHONE} or by email at {EMAIL}. Rodrigo answers personally in English and Spanish."),
  ],
  "contact_k": "Contact", "contact_h": "Talk to me directly", "contact_p": "The fastest way to reach me is a text message. I answer personally, in English or Spanish.",
  "sms": "Text", "email": "Email", "office": "Office",
  "footer": "TerraFunded, LLC is a Texas land company based in Dallas.", "tf_profile": "TerraFunded profile",
  "alt": "Rodrigo Blanco, founder and CEO of TerraFunded",
 },
 "es": {
  "lang": "es", "locale": "es_US", "path": "/es/", "other": "/", "other_label": "EN",
  "title": "Rodrigo Blanco | Fundador y CEO de TerraFunded",
  "desc": "Rodrigo Blanco es el fundador y CEO de TerraFunded, empresa de Dallas que vende tierra rural en Texas directamente a compradores con financiamiento del vendedor. Más de 350 transacciones y más de $15M en ventas.",
  "nav": [("story", "Historia"), ("vision", "Visión"), ("writing", "Artículos"), ("press", "Prensa"), ("contact", "Contacto")],
  "eyebrow": "Fundador y CEO, TerraFunded",
  "lede": "Ayudo a la gente a ser dueña de tierra en Texas sin depender de un banco. Cada venta se cierra en una compañía de títulos con licencia y con Warranty Deed: el comprador es dueño desde el primer día.",
  "cta1": "Visitar TerraFunded", "cta2": "Seguir en Instagram",
  "loc": "Dallas, Texas",
  "stats": [("350+", "transacciones de tierra cerradas"), ("$15M+", "en ventas acumuladas de tierra"), ("40%", "de los compradores son hispanos o latinos"), ("2019", "construyendo el modelo de financiamiento")],
  "stats_note": "Cifras de TerraFunded a abril de 2026, publicadas por",
  "band": "La tierra es donde las familias construyen. Mi trabajo es que sea suya desde el primer día.",
  "band_cap": "Tierra de TerraFunded en el condado de Young, Texas",
  "story_k": "Historia", "story_h": "De Guatemala a la tierra de Texas",
  "story_intro": "Rodrigo Blanco es el fundador y CEO de TerraFunded, una empresa con sede en Dallas que vende tierra rural en Texas directamente a compradores con financiamiento del vendedor. La construyó junto con su esposa y cofundadora, Luisa de Blanco.",
  "timeline": [
   ("Origen", "Nacido en Guatemala", "Rodrigo es guatemalteco y construye sus empresas en Estados Unidos. Trabaja en español y en inglés, y sigue atendiendo personalmente a los compradores en los dos idiomas."),
   ("2019", "Portafolio Diversificado", "Rodrigo y Luisa cofundan Portafolio Diversificado, enfocada en bienes raíces residenciales en Estados Unidos. Ahí empieza a desarrollar el modelo de financiamiento del vendedor que después define a TerraFunded."),
   ("2020", "TerraFunded", "Fundan TerraFunded, una empresa distinta que divide tierra rural de Texas en parcelas de unos 10 acres y las vende directamente a compradores con financiamiento del vendedor y Warranty Deed."),
   ("2026", "Más de 350 transacciones y $15M en ventas", "TerraFunded supera los $15 millones en ventas acumuladas de tierra en condados de Texas como Lamar, Young, Titus, Cass, Clay y Coryell, según publicó The Title Report."),
   ("Hoy", "Tecnología propia", "Rodrigo dirige un equipo bilingüe de más de una docena de personas que desarrolla su propio software con inteligencia artificial, como TerraFunded GPS, que le muestra al comprador los linderos de su lote en la cámara del teléfono."),
  ],
  "facts_h": "Datos clave",
  "facts": [("Nombre completo", "Rodrigo Blanco Marroquín"), ("Cargo", "Fundador y CEO, TerraFunded, LLC"), ("Cofundadora", "Luisa de Blanco, su esposa"), ("Oficina", ADDRESS), ("Especialidad", "Tierra rural en Texas con financiamiento del vendedor"), ("Idiomas", "Español e inglés")],
  "vision_k": "Visión", "vision_h": "Cómo pienso este negocio",
  "vision": [
   ("Dueño desde el primer día.", "No vendo con contract for deed ni rent-to-own. Si estás pagando un terreno, tiene que estar a tu nombre desde el cierre, con seguro de título y en una compañía de títulos independiente."),
   ("Evaluar a la persona, no el papeleo.", "Muchos buenos compradores tienen el ingreso y la disciplina, pero no encajan en el expediente de un banco. Financiar nosotros la tierra permite que más gente sea dueña, con un pagaré a tasa fija y sin penalidad por pago anticipado."),
   ("Una industria vieja, herramientas nuevas.", "La tierra rural es de las industrias menos digitales de Estados Unidos. Desarrollamos nuestro propio software con inteligencia artificial, desde encontrar terrenos hasta que un comprador, parado en su lote, vea los linderos en la cámara del teléfono."),
   ("Hablar el idioma del comprador.", "Contratos, guías y atención en español y en inglés, para que cada comprador entienda exactamente lo que firma."),
   ("No son acres. Es donde una familia construye.", "Este otoño vi a un comprador levantando su casa con sus propias manos en un terreno que nos compró. Para eso existe este negocio."),
  ],
  "tech_links": [("TerraFunded GPS", f"{TF}/es/gps"), ("TerraFunded Overview", "https://overview.terrafunded.com")],
  "adn_k": "ADN", "adn_h": "Lo que mueve todo lo que construyo", "adn": ["Dios", "Propósito", "Emprendimiento"],
  "land_k": "Tierra", "land_h": "Donde construyen los compradores de TerraFunded",
  "writing_k": "Artículos", "writing_h": "Guías que he escrito para compradores de tierra (en inglés)", "writing_all": "Todos los artículos en el blog de TerraFunded",
  "press_k": "Prensa", "press_h": "Prensa y menciones", "press_type": {"article": "Artículo", "release": "Comunicado"},
  "kit_h": "Kit de prensa", "kit_p": "Bios y fotos listas para usar en artículos, podcasts y programas de eventos.",
  "kit_short": "Bio corta", "kit_long": "Bio larga", "kit_copy": "Copiar", "kit_copied": "Copiado",
  "kit_photo": "Foto (JPG)", "kit_logo": "Logo (SVG)", "kit_logo_w": "Logo blanco (SVG)",
  "bio_short": "Rodrigo Blanco es el fundador y CEO de TerraFunded, una empresa con sede en Dallas que vende tierra rural en Texas directamente a compradores con financiamiento del vendedor. TerraFunded ha cerrado más de 350 transacciones de tierra y superó los $15 millones en ventas acumuladas.",
  "bio_long": "Rodrigo Blanco es el fundador y CEO de TerraFunded, una empresa con sede en Dallas que vende tierra rural en Texas directamente a compradores con financiamiento del vendedor y Warranty Deed al cierre. Guatemalteco, desarrolla el modelo de venta de tierra con financiamiento del vendedor desde 2019 y fundó TerraFunded en 2020 con su esposa y cofundadora, Luisa de Blanco. Bajo su dirección, TerraFunded ha cerrado más de 350 transacciones de tierra y superó los $15 millones en ventas acumuladas, en su mayoría parcelas de unos 10 acres en condados de Texas como Lamar, Young, Titus, Cass, Clay y Coryell. Cerca del 40% de sus compradores son hispanos o latinos. Rodrigo dirige un equipo bilingüe que desarrolla con inteligencia artificial la tecnología propia de la empresa, como TerraFunded GPS, que le muestra al comprador los linderos de su lote en la cámara del teléfono. Habla español e inglés. Más en esrodrigoblanco.com.",
  "faq_k": "Preguntas", "faq_h": "Preguntas frecuentes",
  "faq": [
   ("¿Quién es Rodrigo Blanco?", "Rodrigo Blanco (Rodrigo Blanco Marroquín) es el fundador y CEO de TerraFunded, una empresa con sede en Dallas que vende tierra rural en Texas directamente a compradores con financiamiento del vendedor. TerraFunded ha cerrado más de 350 transacciones de tierra y superó los $15 millones en ventas acumuladas."),
   ("¿Quién es el dueño de TerraFunded?", "TerraFunded, LLC fue fundada en 2020 por Rodrigo Blanco y su esposa y cofundadora, Luisa de Blanco. Rodrigo es el fundador y CEO."),
   ("¿TerraFunded y Portafolio Diversificado son la misma empresa?", "No. Rodrigo y Luisa Blanco cofundaron las dos, pero son empresas distintas. TerraFunded, LLC vende tierra rural en Texas con financiamiento del vendedor. Portafolio Diversificado está enfocada en bienes raíces residenciales."),
   ("¿Dónde está TerraFunded?", f"La oficina de TerraFunded está en {ADDRESS}. Sus terrenos están en condados rurales de Texas como Lamar, Young, Titus, Cass, Clay y Coryell."),
   ("¿Cómo verifico que TerraFunded es legítima?", "Cada venta se cierra en una compañía de títulos independiente y con licencia en Texas, y el comprador recibe una Warranty Deed registrada. TerraFunded publica una guía de verificación paso a paso en terrafunded.com/es/verify-terrafunded."),
   ("¿Cómo contacto a Rodrigo Blanco?", f"Por mensaje de texto al {PHONE} o por correo a {EMAIL}. Rodrigo responde personalmente en español y en inglés."),
  ],
  "contact_k": "Contacto", "contact_h": "Escríbeme directo", "contact_p": "La forma más rápida de contactarme es un mensaje de texto. Respondo personalmente, en español o en inglés.",
  "sms": "SMS", "email": "Correo", "office": "Oficina",
  "footer": "TerraFunded, LLC es una empresa de tierra en Texas con sede en Dallas.", "tf_profile": "Perfil en TerraFunded",
  "alt": "Rodrigo Blanco, fundador y CEO de TerraFunded",
 },
}

e = html.escape


def jsonld(t):
    pid = f"{SITE}/#person"
    page = f"{SITE}{t['path']}"
    person = {
        "@type": "Person", "@id": pid, "name": "Rodrigo Blanco",
        "alternateName": "Rodrigo Blanco Marroquín", "givenName": "Rodrigo", "familyName": "Blanco",
        "jobTitle": "Founder & CEO", "description": t["desc"],
        "url": f"{SITE}/", "image": f"{SITE}/rodrigo-blanco-square.jpg",
        "email": f"mailto:{EMAIL}",
        "worksFor": {"@type": "Organization", "@id": f"{TF}/#organization", "name": "TerraFunded", "legalName": "TerraFunded, LLC", "url": TF},
        "workLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "streetAddress": "3838 Oak Lawn Avenue, Suite 1000", "addressLocality": "Dallas", "addressRegion": "TX", "postalCode": "75219", "addressCountry": "US"}},
        "spouse": {"@type": "Person", "@id": f"{TF}/about-us/luisa-de-blanco#person", "name": "Luisa de Blanco"},
        "knowsAbout": ["Owner financing", "Seller financing", "Rural land in Texas", "Land subdivision", "Warranty deeds", "Real estate notes"],
        "knowsLanguage": ["en", "es"],
        "nationality": {"@type": "Country", "name": "Guatemala"},
        "subjectOf": [{"@type": "NewsArticle" if ty == "article" else "Article", "headline": ti, "url": u, "publisher": {"@type": "Organization", "name": out}} for out, d, ti, u, ty in PRESS],
        "sameAs": [TF_PERSON, LINKEDIN, INSTAGRAM],
    }
    graph = [
        {"@type": "WebSite", "@id": f"{SITE}/#website", "url": f"{SITE}/", "name": "Rodrigo Blanco", "alternateName": "Rodrigo BlanCo.", "inLanguage": ["en", "es"], "about": {"@id": pid}},
        {"@type": "ProfilePage", "@id": f"{page}#profilepage", "url": page, "name": t["title"], "description": t["desc"], "inLanguage": t["lang"],
         "isPartOf": {"@id": f"{SITE}/#website"}, "mainEntity": {"@id": pid}, "dateModified": MODIFIED},
        person,
        {"@type": "Organization", "@id": f"{TF}/#organization", "name": "TerraFunded", "legalName": "TerraFunded, LLC", "url": TF, "foundingDate": "2020",
         "founder": [{"@id": pid}, {"@type": "Person", "@id": f"{TF}/about-us/luisa-de-blanco#person", "name": "Luisa de Blanco"}]},
        {"@type": "FAQPage", "@id": f"{page}#faq", "inLanguage": t["lang"], "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)


CSS = (pathlib.Path(__file__).resolve().parent / "site.css").read_text(encoding="utf-8")

JS = """
document.querySelectorAll('[data-copy]').forEach(function(b){b.addEventListener('click',function(){
 var t=document.getElementById(b.dataset.copy).textContent,l=b.textContent;
 var done=function(){b.textContent=b.dataset.done;setTimeout(function(){b.textContent=l},1600)};
 try{navigator.clipboard.writeText(t).then(done,function(){})}catch(e){}
})});
(function(){
 var els=document.querySelectorAll('.rv');
 if(!('IntersectionObserver' in window)){els.forEach(function(x){x.classList.add('in')});return}
 var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}})},{rootMargin:'0px 0px -8% 0px'});
 els.forEach(function(x){io.observe(x)});
})();
"""


def page(code):
    t = T[code]
    o = T["es" if code == "en" else "en"]
    nav = "".join(f'<a href="#{i}">{e(n)}</a>' for i, n in t["nav"])
    stats = "".join(f'<div class="stat rv"><b>{e(v)}</b><span>{e(l)}</span></div>' for v, l in t["stats"])
    tl = "".join(f'<li class="rv"><span class="when">{e(w)}</span><h3>{e(h)}</h3><p>{e(p)}</p></li>' for w, h, p in t["timeline"])
    facts = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in t["facts"])
    vision = "".join(f'<li class="rv"><span class="vn">0{i+1}</span><div><h3>{e(h)}</h3><p>{e(p)}</p></div></li>' for i, (h, p) in enumerate(t["vision"]))
    techl = " · ".join(f'<a href="{u}" rel="noopener">{e(n)} ↗</a>' for n, u in t["tech_links"])
    ci = 1 if code == "es" else 0
    land = "".join(f'<figure class="rv {cls}"><img src="/land/{f}.webp" width="{w}" height="{h}" loading="lazy" decoding="async" alt="{e(t["land_h"])}: {e(cap_es if code=="es" else cap_en)}, Texas"><figcaption>{e(cap_es if code=="es" else cap_en)}, Texas</figcaption></figure>' for f, w, h, cap_en, cap_es, cls in LAND)
    arts = "".join(f'<li><a href="{u}" rel="author noopener"><span class=tag>{e(g[ci])}</span><span class=t>{e(ti)}</span><span class=arr>→</span></a></li>' for ti, u, g in ARTICLES)
    press = "".join(f'<li><a href="{u}" rel="noopener"><span class=tag>{e(d[code])}</span><span class=t>{e(ti)}<small>{e(out)} · {e(t["press_type"][ty])}</small></span><span class=arr>↗</span></a></li>' for out, d, ti, u, ty in PRESS)
    adn = '<span class="plus" aria-hidden="true">+</span>'.join(f'<div class="dmd rv"><span>{e(x)}</span></div>' for x in t["adn"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faq"])
    blog = f"{TF}/es/blog" if code == "es" else f"{TF}/blog"
    tf_home = f"{TF}/es" if code == "es" else TF
    canonical = f"{SITE}{t['path']}"
    k = lambda n, s: f'<p class="k"><em>0{n}</em>{e(s)}</p>'
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{SITE}/">
<link rel="alternate" hreflang="es" href="{SITE}/es/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<link rel="me" href="{LINKEDIN}">
<link rel="me" href="{INSTAGRAM}">
<link rel="me" href="{TF_PERSON}">
<meta name="author" content="Rodrigo Blanco">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#ffffff">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="Rodrigo Blanco">
<meta property="profile:first_name" content="Rodrigo">
<meta property="profile:last_name" content="Blanco">
<meta property="og:title" content="{e(t['title'])}">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/og-rodrigo-blanco.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Rodrigo Blanco, {e(t['eyebrow'])}">
<meta property="og:locale" content="{t['locale']}">
<meta property="og:locale:alternate" content="{o['locale']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(t['title'])}">
<meta name="twitter:description" content="{e(t['desc'])}">
<meta name="twitter:image" content="{SITE}/og-rodrigo-blanco.jpg">
<meta name="msvalidate.01" content="620472A22B0CA1581D997D4E8FBC1A9F">
<meta name="google-site-verification" content="-E_RcX_S4mlRN3WIIyLujaK6M_BnNBOgAqA6BPch5Zo">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-48.png" sizes="48x48" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/fonts/urbanist-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
<script type="application/ld+json">
{jsonld(t)}
</script>
</head>
<body>
<header class="nav"><div class="wrap">
 <a class="brand" href="{t['path']}" aria-label="Rodrigo Blanco"><img src="/brand/logo-dark.svg" width="190" height="25" alt="Rodrigo BlanCo."></a>
 <nav aria-label="Main">{nav}<a class="lang" href="{t['other']}" hreflang="{o['lang']}" lang="{o['lang']}">{e(t['other_label'])}</a></nav>
</div></header>
<main>
<section class="hero"><span class="wm" aria-hidden="true">Blan<br>Co.</span><div class="wrap">
 <div class="hero-txt">
  <p class="eyebrow">{e(t['eyebrow'])}</p>
  <h1>Rodrigo<br>Blanco<em>.</em></h1>
  <p class="lede">{e(t['lede'])}</p>
  <div class="ctas"><a class="btn primary" href="{tf_home}" rel="noopener">{e(t['cta1'])} →</a><a class="btn" href="{INSTAGRAM}" rel="me noopener">{e(t['cta2'])}</a></div>
 </div>
 <div class="portrait"><img src="/rodrigo-blanco.jpg" width="375" height="466" alt="{e(t['alt'])}"><span class="pin">{e(t['loc'])}</span></div>
</div></section>

<div class="stats"><div class="wrap"><div class="grid">{stats}</div>
 <p class="note">{e(t['stats_note'])} <a href="{PRESS[0][3]}" rel="noopener">The Title Report ↗</a></p></div></div>

<section class="band" aria-label="{e(t['band_cap'])}">
 <img src="/land/young-county-sunset.webp" width="1550" height="700" alt="{e(t['band_cap'])}">
 <div class="band-txt wrap"><p class="rv">“{e(t['band'])}”</p><span>{e(t['band_cap'])}</span></div>
</section>

<section class="block" id="story"><div class="wrap">
 <div class="head">{k(1, t['story_k'])}<h2>{e(t['story_h'])}</h2></div>
 <div class="story">
  <div><p class="intro">{e(t['story_intro'])}</p><ol class="tl">{tl}</ol></div>
  <dl class="facts rv"><h3>{e(t['facts_h'])}</h3>{facts}</dl>
 </div>
</div></section>

<section class="block" id="vision"><div class="wrap">
 <div class="head">{k(2, t['vision_k'])}<h2>{e(t['vision_h'])}</h2></div>
 <ol class="vision">{vision}</ol>
 <p class="techl">{techl}</p>
</div></section>

<section class="adn" aria-label="{e(t['adn_k'])}"><div class="wrap">
 <p class="k">{e(t['adn_k'])}</p><h2>{e(t['adn_h'])}</h2>
 <div class="dmds">{adn}</div>
</div></section>

<section class="block" id="land"><div class="wrap">
 <div class="head">{k(3, t['land_k'])}<h2>{e(t['land_h'])}</h2></div>
 <div class="gallery">{land}</div>
</div></section>

<section class="block" id="writing"><div class="wrap">
 <div class="head">{k(4, t['writing_k'])}<h2>{e(t['writing_h'])}</h2></div>
 <ul class="rows">{arts}</ul><a class="more" href="{blog}" rel="noopener">{e(t['writing_all'])} →</a>
</div></section>

<section class="block" id="press"><div class="wrap">
 <div class="head">{k(5, t['press_k'])}<h2>{e(t['press_h'])}</h2></div>
 <ul class="rows">{press}</ul>
 <div class="kit" id="press-kit">
  <div class="kit-head"><h3>{e(t['kit_h'])}</h3><p>{e(t['kit_p'])}</p></div>
  <div class="bios">
   <div class="bio"><div class="bio-top"><b>{e(t['kit_short'])}</b><button type="button" data-copy="bs" data-done="{e(t['kit_copied'])}">{e(t['kit_copy'])}</button></div><p id="bs">{e(t['bio_short'])}</p></div>
   <div class="bio"><div class="bio-top"><b>{e(t['kit_long'])}</b><button type="button" data-copy="bl" data-done="{e(t['kit_copied'])}">{e(t['kit_copy'])}</button></div><p id="bl">{e(t['bio_long'])}</p></div>
  </div>
  <div class="dl"><a href="/rodrigo-blanco.jpg" download>{e(t['kit_photo'])} ↓</a><a href="/brand/logo-dark.svg" download>{e(t['kit_logo'])} ↓</a><a href="/brand/logo-white.svg" download>{e(t['kit_logo_w'])} ↓</a></div>
 </div>
</div></section>

<section class="block" id="faq"><div class="wrap">
 <div class="head">{k(6, t['faq_k'])}<h2>{e(t['faq_h'])}</h2></div>
 <div class="faq">{faq}</div>
</div></section>

<div class="wrap" id="contact"><div class="contact rv">
 <div><p class="k">{e(t['contact_k'])}</p><h2>{e(t['contact_h'])}</h2><p class="cp">{e(t['contact_p'])}</p></div>
 <div class="channels">
  <a href="sms:{PHONE_E164}"><span>{e(t['sms'])}</span>{PHONE}</a>
  <a href="mailto:{EMAIL}"><span>{e(t['email'])}</span>{EMAIL}</a>
  <a href="{INSTAGRAM}" rel="me noopener"><span>Instagram</span>@esrodrigoblanco ↗</a>
  <a href="{LINKEDIN}" rel="me noopener"><span>LinkedIn</span>Rodrigo Blanco Marroquín ↗</a>
  <div><span>{e(t['office'])}</span>Dallas, TX</div>
 </div>
</div></div>
</main>
<footer><div class="wrap">
 <img class="fsym" src="/brand/symbol-dark.svg" width="44" height="36" alt="">
 <span>© 2026 Rodrigo Blanco · {e(t['footer'])}</span>
 <span><a href="{tf_home}" rel="noopener">terrafunded.com</a> · <a href="{TF_PERSON}" rel="me noopener">{e(t['tf_profile'])}</a></span>
</div></footer>
<script>{JS}</script>
</body>
</html>
"""


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "es").mkdir(exist_ok=True)
    (OUT / "index.html").write_text(page("en"), encoding="utf-8")
    (OUT / "es" / "index.html").write_text(page("es"), encoding="utf-8")
    sym = (OUT / "brand" / "symbol-white.svg").read_text(encoding="utf-8")
    inner = sym[sym.index(">", sym.index("<svg")) + 1:sym.rindex("</svg>")]
    (OUT / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#19262C"/><svg x="8" y="12" width="48" height="40" viewBox="866 467.5 179 144.8">' + inner + '</svg></svg>', encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    alt = f'<xhtml:link rel="alternate" hreflang="en" href="{SITE}/"/><xhtml:link rel="alternate" hreflang="es" href="{SITE}/es/"/>'
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n<url><loc>{SITE}/</loc><lastmod>{MODIFIED}</lastmod>{alt}</url>\n<url><loc>{SITE}/es/</loc><lastmod>{MODIFIED}</lastmod>{alt}</url>\n</urlset>\n', encoding="utf-8")
    en = T["en"]
    llms = ["# Rodrigo Blanco", "", f"> {en['desc']}", "", en["story_intro"], "",
            "## Facts"] + [f"- {a}: {b}" for a, b in en["facts"]] + [
            "- TerraFunded founded: 2020, with Luisa de Blanco",
            "- Track record: 350+ land transactions and $15M+ in cumulative land sales (April 2026, reported by The Title Report)",
            "- About 40% of TerraFunded buyers are Hispanic or Latino",
            "- Portafolio Diversificado (co-founded 2019, residential real estate) is a separate company from TerraFunded, LLC", "",
            "## Profiles", f"- TerraFunded founder profile: {TF_PERSON}", f"- LinkedIn: {LINKEDIN}", f"- Instagram: {INSTAGRAM}", f"- Spanish version of this site: {SITE}/es/", "",
            "## Writing"] + [f"- [{ti}]({u})" for ti, u, _ in ARTICLES] + ["", "## Press"] + [f"- [{ti}]({u}): {out}, {d['en']}" for out, d, ti, u, _ in PRESS] + [
            "", "## Contact", f"- Text: {PHONE}", f"- Email: {EMAIL}", ""]
    (OUT / "llms.txt").write_text("\n".join(llms), encoding="utf-8")
    vercel = {"cleanUrls": True, "trailingSlash": True, "headers": [
        {"source": "/fonts/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
        {"source": "/land/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=2592000"}]},
        {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}]},
    ]}
    (OUT / "vercel.json").write_text(json.dumps(vercel, indent=2) + "\n", encoding="utf-8")
    old = OUT / "_headers"
    if old.exists():
        old.unlink()
    print("built for", SITE, "->", OUT)


main()
