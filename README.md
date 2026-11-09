# esrodrigoblanco.com

Personal site of Rodrigo Blanco, Founder & CEO of TerraFunded. Static HTML, deployed on Vercel.

- English: `/index.html` · Spanish: `/es/index.html`
- Schema.org: WebSite, ProfilePage, Person, FAQPage (in each page's `<head>`)
- `robots.txt`, `sitemap.xml`, `llms.txt`, `vercel.json`

## Editing

The HTML is generated. Edit `scripts/build.py` (text, facts, links) or `scripts/site.css` (design), then run:

```
python3 scripts/build.py https://esrodrigoblanco.com
```

Facts mirror `scripts/_company.data.mjs` in terrafunded/terrafunded. Land photos come from the TerraFunded `properties` table.
