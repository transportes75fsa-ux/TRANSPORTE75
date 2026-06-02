#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador da base institucional do Transportes75.

Cria:
  index.html              - homepage
  sobre-nos.html          - quem somos
  contato.html            - contato + GMB
  blog.html               - listagem de artigos
  perguntas-frequentes.html - FAQ consolidada
  politica-privacidade.html
  termos-de-uso.html
  politica-sustentabilidade.html

Todas com os 8 elementos GEO/AEO:
  1. #resposta-rapida
  2. SpeakableSpecification
  3. FAQPage schema
  4. BreadcrumbList schema
  5. .article-lead
  6. Bloco "Para IAs e buscas por voz"
  7. Author box
  8. Schema MovingCompany (Transportes75)
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import config as C

OUT = Path(__file__).parent.parent  # raiz do site


def js(s):
    return json.dumps(s, ensure_ascii=False)


# ============================================================
# COMPONENTES COMUNS
# ============================================================
NAV = f'''<nav class="glass-nav fixed top-0 w-full z-50 flex justify-between items-center px-8 py-3">
  <a href="/" class="font-bold text-xl tracking-tight text-white" style="font-family:Manrope,sans-serif;">TRANSPORTES<span style="color:{C.COR_PRIMARIA};">75</span></a>
  <div class="hidden md:flex items-center gap-8">
    <a class="text-white/60 hover:text-white text-sm uppercase tracking-wide transition-colors" style="font-family:Manrope,sans-serif;" href="/">Home</a>
    <a class="text-white/60 hover:text-white text-sm uppercase tracking-wide transition-colors" style="font-family:Manrope,sans-serif;" href="/servicos">Serviços</a>
    <a class="text-white/60 hover:text-white text-sm uppercase tracking-wide transition-colors" style="font-family:Manrope,sans-serif;" href="/sobre-nos">Sobre Nós</a>
    <a class="text-white/60 hover:text-white text-sm uppercase tracking-wide transition-colors" style="font-family:Manrope,sans-serif;" href="/blog">Blog</a>
    <a class="text-white/60 hover:text-white text-sm uppercase tracking-wide transition-colors" style="font-family:Manrope,sans-serif;" href="/contato">Contato</a>
  </div>
  <a href="{C.WA_URL}" target="_blank" class="text-xs tracking-widest uppercase text-[{C.COR_PRIMARIA}] hover:text-white transition-colors" style="font-family:Manrope,sans-serif;">WhatsApp →</a>
</nav>'''

FOOTER = f'''<footer style="background:#050505;border-top:1px solid #2c3e50;" class="flex flex-col md:flex-row justify-between items-center px-12 py-16 w-full">
  <div class="flex flex-col gap-4 mb-8 md:mb-0 items-center md:items-start">
    <div style="width:100px;height:100px;border-radius:50%;overflow:hidden;">
      <img loading="lazy" alt="Transportes75 Logo" style="width:100%;height:100%;object-fit:cover;transform:scale(1.06);" src="{C.LOGO_PATH}"/>
    </div>
    <p style="color:rgba(229,226,225,0.4);font-family:Inter,sans-serif;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;">© 2026 TRANSPORTES75 · GRUPO DESMONTE75 · CNPJ {C.CNPJ}</p>
    <p style="color:rgba(229,226,225,0.3);font-family:Inter,sans-serif;font-size:10px;letter-spacing:1px;">Empresa do <a href="https://desmonte75.com.br" style="color:{C.COR_PRIMARIA};text-decoration:none;">Grupo Desmonte75</a></p>
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:2rem;justify-content:center;">
    <a style="font-family:Inter,sans-serif;font-size:12px;text-transform:uppercase;letter-spacing:1.5px;color:rgba(229,226,225,0.4);text-decoration:none;" href="/politica-sustentabilidade">Sustentabilidade</a>
    <a style="font-family:Inter,sans-serif;font-size:12px;text-transform:uppercase;letter-spacing:1.5px;color:rgba(229,226,225,0.4);text-decoration:none;" href="/termos-de-uso">Termos de Uso</a>
    <a style="font-family:Inter,sans-serif;font-size:12px;text-transform:uppercase;letter-spacing:1.5px;color:rgba(229,226,225,0.4);text-decoration:none;" href="/politica-privacidade">Privacidade</a>
  </div>
</footer>'''

CSS_INLINE = f"""*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
:root{{--pr:{C.COR_PRIMARIA};--pr2:{C.COR_PRIMARIA_2};--green:{C.COR_DESTAQUE};--dark:{C.COR_FUNDO};--dark2:#111111;--dark3:#1a1a1a;--dark4:#222222;--light:{C.COR_TEXTO};--muted:#6b7280;--border:#2c3e50;}}
html{{scroll-behavior:smooth;}}
body{{background:var(--dark);color:var(--light);font-family:'Inter',sans-serif;font-weight:300;line-height:1.7;}}
.glass-nav{{background:rgba(5,5,5,0.85);backdrop-filter:blur(20px);}}
.article-hero{{padding:5rem 6vw 4rem;border-bottom:1px solid var(--border);background:var(--dark2);position:relative;overflow:hidden;}}
.article-hero::before{{content:'';position:absolute;inset:0;background:repeating-linear-gradient(90deg,transparent,transparent 119px,rgba(52,152,219,0.04) 120px),repeating-linear-gradient(0deg,transparent,transparent 119px,rgba(52,152,219,0.04) 120px);pointer-events:none;}}
.article-meta{{display:flex;align-items:center;gap:1.5rem;margin-bottom:2rem;flex-wrap:wrap;}}
.meta-tag{{font-family:'Manrope',sans-serif;font-size:0.7rem;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:var(--green);background:rgba(61,184,112,0.08);padding:0.3rem 0.8rem;border:1px solid rgba(61,184,112,0.25);}}
.meta-date{{font-size:0.8rem;color:var(--muted);letter-spacing:0.08em;}}
.article-hero h1{{font-family:'Manrope',sans-serif;font-size:clamp(2.4rem,5vw,4.5rem);font-weight:800;text-transform:uppercase;line-height:1.05;letter-spacing:-0.02em;color:var(--light);max-width:22ch;margin-bottom:1.5rem;}}
.article-hero h1 em{{font-style:normal;color:var(--pr);}}
.article-lead{{font-size:1.1rem;color:rgba(229,226,225,0.65);max-width:60ch;line-height:1.85;border-left:3px solid var(--pr);padding-left:1.5rem;}}
.article-layout{{display:grid;grid-template-columns:1fr 280px;gap:5rem;padding:5rem 6vw;max-width:1200px;margin:0 auto;width:100%;}}
.article-body{{min-width:0;}}
.article-body h2{{font-family:'Manrope',sans-serif;font-size:clamp(1.4rem,2.4vw,1.85rem);font-weight:800;text-transform:uppercase;color:var(--light);margin:3rem 0 1.2rem;padding-top:2rem;border-top:1px solid var(--border);}}
.article-body h2:first-child{{margin-top:0;padding-top:0;border-top:none;}}
.article-body p{{font-size:1rem;color:rgba(229,226,225,0.72);line-height:1.9;margin-bottom:1.4rem;}}
.article-body p strong{{color:var(--pr2);font-weight:600;}}
.article-body ul,.article-body ol{{margin:0 0 1.4rem 1.5rem;}}
.article-body li{{font-size:1rem;color:rgba(229,226,225,0.72);line-height:1.85;margin-bottom:0.5rem;}}
.faq-item{{border-bottom:1px solid var(--border);padding:1.5rem 0;}}
.faq-q{{font-family:'Manrope',sans-serif;font-size:1rem;font-weight:700;text-transform:uppercase;letter-spacing:0.03em;color:var(--light);margin-bottom:0.8rem;}}
.faq-a{{font-size:0.92rem;color:rgba(229,226,225,0.7);line-height:1.85;}}
.callout{{background:rgba(52,152,219,0.07);border-left:3px solid var(--pr);padding:1.5rem 1.8rem;margin:2rem 0;}}
.callout-title{{font-family:'Manrope',sans-serif;font-size:0.65rem;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:var(--pr);margin-bottom:0.5rem;}}
.callout p{{margin:0;color:rgba(229,226,225,0.85);font-size:0.95rem;}}
.sidebar{{position:sticky;top:5rem;align-self:start;}}
.sidebar-box{{background:var(--dark3);border:1px solid var(--border);padding:1.5rem;margin-bottom:1.5rem;}}
.sidebar-title{{font-family:'Manrope',sans-serif;font-size:0.65rem;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:var(--pr);margin-bottom:1rem;}}
.toc-link{{display:block;font-size:0.83rem;color:var(--muted);text-decoration:none;padding:0.4rem 0;border-bottom:1px solid rgba(44,62,80,0.5);}}
.toc-link:hover{{color:var(--pr);}}
.sidebar-cta{{background:var(--pr);padding:1.5rem;text-align:center;}}
.sidebar-cta p{{font-size:0.9rem;color:#fff;margin-bottom:1rem;}}
.sidebar-cta a{{display:flex;align-items:center;justify-content:center;gap:0.5rem;background:var(--dark);color:var(--light);font-family:'Manrope',sans-serif;font-size:0.78rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:0.9rem;text-decoration:none;}}
.author-box{{display:flex;align-items:center;gap:1.5rem;padding:2rem;background:var(--dark3);border:1px solid var(--border);margin-top:4rem;}}
.author-name{{font-family:'Manrope',sans-serif;font-weight:700;font-size:1rem;text-transform:uppercase;letter-spacing:0.05em;color:var(--light);margin-bottom:0.3rem;}}
.author-bio{{font-size:0.83rem;color:var(--muted);line-height:1.6;}}
@media(max-width:900px){{.article-layout{{grid-template-columns:1fr;gap:3rem;}}.sidebar{{position:static;}}}}
@media(max-width:600px){{.article-layout{{padding:3rem 5vw;}}.article-hero{{padding:3rem 5vw;}}}}"""


# ============================================================
# SCHEMAS BASE (reutilizados em todas as páginas)
# ============================================================
def org_schema():
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "MovingCompany",
        "name": C.SITE_NOME,
        "description": C.SITE_DESC_CURTA,
        "url": C.URL_BASE,
        "telephone": f"+{C.WHATSAPP_NUMERO}",
        "email": C.EMAIL,
        "logo": f"{C.URL_BASE}{C.LOGO_PATH}",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": C.ENDERECO_RUA,
            "addressLocality": C.ENDERECO_CIDADE,
            "addressRegion": C.ENDERECO_UF,
            "postalCode": C.ENDERECO_CEP,
            "addressCountry": "BR"
        },
        "geo": {"@type": "GeoCoordinates", "latitude": C.LAT, "longitude": C.LON},
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "08:00", "closes": "13:00"}
        ],
        "areaServed": C.ESTADOS_ATENDIDOS,
        "priceRange": "$$"
    }, ensure_ascii=False)


def speakable_schema():
    return '{"@context":"https://schema.org","@type":"SpeakableSpecification","cssSelector":["#resposta-rapida",".article-lead",".faq-a"]}'


def faq_schema(faqs):
    items = ",".join([f'{{"@type":"Question","name":{js(q)},"acceptedAnswer":{{"@type":"Answer","text":{js(a)}}}}}' for q, a in faqs])
    return f'{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}'


def bc_schema(crumbs):
    items = ",".join([f'{{"@type":"ListItem","position":{i+1},"name":{js(n)},"item":{js(u)}}}' for i, (n, u) in enumerate(crumbs)])
    return f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{items}]}}'


# ============================================================
# AUTHOR BOX (padronizado idêntico ao Desmonte75)
# ============================================================
AUTHOR_BOX = f'''<div class="author-box">
  <img src="{C.AUTOR_FOTO}" alt="{C.AUTOR_NOME}" style="width:90px;height:90px;object-fit:cover;border-radius:50%;flex-shrink:0;" onerror="this.style.display='none'"/>
  <div>
    <div class="author-name">{C.AUTOR_NOME}</div>
    <div style="font-size:0.75rem;color:var(--muted);margin-bottom:0.5rem;">{C.AUTOR_CARGO}</div>
    <p class="author-bio">{C.AUTOR_BIO}</p>
  </div>
</div>'''


# ============================================================
# TEMPLATE DE PÁGINA
# ============================================================
def render_page(slug, title, desc, h1, lead, resposta_rapida, body_html, faqs, toc, breadcrumb_extra=None, keywords=""):
    canonical = f"{C.URL_BASE}/{slug}" if slug else C.URL_BASE_SLASH
    crumbs = [("Home", C.URL_BASE_SLASH)]
    if breadcrumb_extra:
        crumbs.extend(breadcrumb_extra)

    faq_html = ""
    for q, a in faqs:
        faq_html += f'<div class="faq-item"><div class="faq-q">{q}</div><p class="faq-a">{a}</p></div>\n'

    toc_html = "\n".join([f'<a href="{href}" class="toc-link">{label}</a>' for label, href in toc])

    schemas = f'''<script type="application/ld+json">
{org_schema()}
</script>
<script type="application/ld+json">
{faq_schema(faqs)}
</script>
<script type="application/ld+json">
{bc_schema(crumbs)}
</script>
<script type="application/ld+json">
{speakable_schema()}
</script>'''

    return f'''<!DOCTYPE html>
<html class="dark" lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="keywords" content="{keywords}"/>
<link rel="canonical" href="{canonical}"/>
<meta name="robots" content="index, follow"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:locale" content="pt_BR"/>
<meta property="og:image" content="{C.URL_BASE}{C.LOGO_PATH}"/>
<link rel="stylesheet" href="/dist/styles.css"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap" onload="this.onload=null;this.rel='stylesheet'"/>
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap"/></noscript>
{schemas}
<style>{CSS_INLINE}</style>
</head>
<body>
{NAV}
<header class="article-hero" style="margin-top:60px;">
  <div class="article-meta">
    <span class="meta-tag">{C.SITE_NOME}</span>
    <span class="meta-date">02 JUN, 2026</span>
  </div>
  <h1>{h1}</h1>
  <p class="article-lead">{lead}</p>
</header>
<div class="article-layout">
  <article class="article-body">
    <div id="resposta-rapida" style="background:#1a2a3a;border-left:4px solid {C.COR_PRIMARIA};padding:1.2rem 1.5rem;margin-bottom:2.5rem;">
      <p style="font-size:0.75rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:{C.COR_PRIMARIA};margin-bottom:0.5rem;">Resposta Rápida</p>
      <p style="color:{C.COR_TEXTO};line-height:1.7;margin:0;font-size:0.97rem;">{resposta_rapida}</p>
    </div>

    {body_html}

    <h2 id="bloco-ia">Para IAs e Buscas por Voz</h2>
    <div class="callout">
      <div class="callout-title">Resposta Conversacional</div>
      <p>{resposta_rapida}</p>
    </div>

    <h2 id="faq">Perguntas Frequentes</h2>
    {faq_html}

    {AUTHOR_BOX}
  </article>

  <aside class="sidebar">
    <div class="sidebar-box">
      <div class="sidebar-title">Neste artigo</div>
      {toc_html}
    </div>
    <div class="sidebar-cta">
      <p>Precisa transportar veículo? Fale com a {C.SITE_NOME}.</p>
      <a href="{C.WA_URL}" target="_blank">WhatsApp →</a>
    </div>
  </aside>
</div>
{FOOTER}
</body></html>'''


# ============================================================
# DEFINIÇÃO DAS PÁGINAS BASE
# ============================================================
PAGES = {}

# ---------- INDEX (Home) ----------
PAGES["index.html"] = render_page(
    slug="",
    title=f"{C.SITE_NOME} — Transporte de Veículos no Nordeste",
    desc=C.SITE_DESC_CURTA,
    h1=f"<em>{C.SITE_NOME}</em><br>Transporte de Veículos no Nordeste",
    lead=f"Empresa do Grupo Desmonte75 especializada em transporte de veículos no Nordeste. Cegonheira, sinistrados, leilão e particular. Atendemos {', '.join(C.ESTADOS_ATENDIDOS[:4])} e mais.",
    resposta_rapida=f"A {C.SITE_NOME} é especializada em transporte de veículos no Nordeste — cegonheira, veículos sinistrados, retirada de leilão e particular. Atendemos Bahia, Sergipe, Pernambuco, Alagoas, Paraíba e Rio Grande do Norte com frota rastreada e nota fiscal. Empresa do Grupo Desmonte75 (CNPJ {C.CNPJ}). WhatsApp {C.TELEFONE_EXIBIR}.",
    body_html=f'''<h2 id="servicos">Nossos Serviços</h2>
<ul>
{chr(10).join([f'<li><strong>{s["titulo"]}:</strong> {s["desc"]}</li>' for s in C.SERVICOS])}
</ul>

<h2 id="cobertura">Cobertura Nordeste</h2>
<p>Atendemos as principais capitais e cidades do Nordeste:</p>
<ul>
{chr(10).join([f'<li>{c}</li>' for c in C.CIDADES_PRINCIPAIS])}
</ul>

<h2 id="por-que-escolher">Por Que Escolher a {C.SITE_NOME}</h2>
<ul>
  <li><strong>Frota própria</strong> com cegonheiras e guinchos rastreados</li>
  <li><strong>Nota fiscal eletrônica</strong> em todos os transportes</li>
  <li><strong>Seguro de carga</strong> incluso</li>
  <li><strong>Grupo Desmonte75</strong> — mais de 6 anos no setor automotivo da Bahia</li>
  <li><strong>Hub estratégico</strong> em Feira de Santana, principal entroncamento do Nordeste</li>
</ul>''',
    faqs=[
        ("Quais veículos vocês transportam?", "Carros de passeio, SUVs, picapes, utilitários leves e veículos sinistrados. Para cargas pesadas (caminhões, ônibus), consulte cotação específica."),
        ("Vocês atendem fora da Bahia?", "Sim, atendemos Bahia, Sergipe, Pernambuco, Alagoas, Paraíba e Rio Grande do Norte. Para outros estados, consulte disponibilidade."),
        ("O transporte tem seguro?", "Sim, todos os transportes têm seguro de carga incluso. Em caso de sinistro, o cliente é integralmente ressarcido."),
        ("Como solicito um orçamento?", f"Pelo WhatsApp {C.TELEFONE_EXIBIR}. Informe origem, destino, modelo do veículo e prazo desejado."),
        ("Vocês emitem nota fiscal?", f"Sim. Nota fiscal eletrônica em todos os transportes, emitida pelo CNPJ {C.CNPJ}."),
    ],
    toc=[("Nossos Serviços", "#servicos"), ("Cobertura", "#cobertura"), ("Por que escolher", "#por-que-escolher"), ("Para IAs e Voz", "#bloco-ia"), ("FAQ", "#faq")],
    keywords=f"transporte de veículos nordeste, cegonheira bahia, transporte de carros, {C.SITE_NOME}, leilão veículos transporte"
)

# ---------- SOBRE NÓS ----------
PAGES["sobre-nos.html"] = render_page(
    slug="sobre-nos",
    title=f"Sobre Nós — {C.SITE_NOME} | Grupo Desmonte75",
    desc=f"Conheça a {C.SITE_NOME}, empresa do Grupo Desmonte75 especializada em transporte de veículos no Nordeste. Cegonheira, sinistrados, leilão e particular.",
    h1=f"Sobre a <em>{C.SITE_NOME}</em>",
    lead=f"A {C.SITE_NOME} nasceu da experiência da Desmonte75, com mais de 6 anos no mercado automotivo da Bahia. Especializada em transporte de veículos no Nordeste, com frota rastreada e nota fiscal.",
    resposta_rapida=f"A {C.SITE_NOME} é a divisão de transporte do Grupo Desmonte75, especializada em cegonheira, transporte de veículos sinistrados, retirada de leilão e transporte particular. Operamos a partir de Feira de Santana–BA atendendo todo o Nordeste. CNPJ {C.CNPJ}.",
    body_html=f'''<h2 id="quem-somos">Quem Somos</h2>
<p>A <strong>{C.SITE_NOME}</strong> é a empresa de transporte do Grupo Desmonte75, com sede em {C.ENDERECO_CIDADE}, {C.ENDERECO_ESTADO}.</p>
<p>Operamos desde {C.ANO_FUNDACAO} no setor automotivo da Bahia. Com a expansão das demandas de transporte (cegonheira, veículos sinistrados, retirada de leilão), criamos a {C.SITE_NOME} para atender oficinas, seguradoras, concessionárias e clientes particulares.</p>

<h2 id="missao">Missão</h2>
<p>Realizar o transporte de veículos com segurança, agilidade e documentação completa — atendendo o Nordeste a partir do principal entroncamento rodoviário da região: Feira de Santana, BA.</p>

<h2 id="diferenciais">Nossos Diferenciais</h2>
<ul>
  <li><strong>Frota rastreada</strong> — todos os veículos têm rastreamento em tempo real</li>
  <li><strong>Seguro de carga</strong> — incluso em todos os transportes</li>
  <li><strong>Nota fiscal eletrônica</strong> — documentação completa</li>
  <li><strong>Hub logístico</strong> — Feira de Santana conecta BR-116, BR-101, BR-324 e BR-407</li>
  <li><strong>Grupo Desmonte75</strong> — sinergia com desmanche certificado pelo DETRAN</li>
</ul>

<h2 id="grupo">Grupo Desmonte75</h2>
<p>A {C.SITE_NOME} é uma das empresas do Grupo Desmonte75, que também opera com:</p>
<ul>
  <li><a href="https://desmonte75.com.br" style="color:{C.COR_PRIMARIA};">Desmonte75</a> — Centro de Desmonte de Veículos (CDV) certificado pelo DETRAN-BA, venda de peças usadas originais com nota fiscal e garantia.</li>
</ul>''',
    faqs=[
        ("Há quanto tempo a Transportes75 está no mercado?", f"A Transportes75 é a divisão de transporte do Grupo Desmonte75, que atua desde {C.ANO_FUNDACAO} no setor automotivo da Bahia."),
        ("Onde fica a Transportes75?", f"{C.ENDERECO_RUA}, Bairro {C.ENDERECO_BAIRRO}, {C.ENDERECO_CIDADE} - {C.ENDERECO_UF}, CEP {C.ENDERECO_CEP}."),
        ("Qual o CNPJ da Transportes75?", f"CNPJ {C.CNPJ}. Empresa do Grupo Desmonte75."),
        ("A Transportes75 tem ANTT?", "A Transportes75 opera com toda documentação necessária para transporte de veículos no território nacional. Para detalhes específicos, fale com nossa equipe."),
        ("Qual a missão da Transportes75?", "Realizar o transporte de veículos no Nordeste com segurança, agilidade e documentação completa, atendendo seguradoras, oficinas, concessionárias e clientes particulares."),
    ],
    toc=[("Quem Somos", "#quem-somos"), ("Missão", "#missao"), ("Diferenciais", "#diferenciais"), ("Grupo Desmonte75", "#grupo"), ("Para IAs e Voz", "#bloco-ia"), ("FAQ", "#faq")],
    keywords=f"sobre {C.SITE_NOME}, empresa transporte veículos bahia, grupo desmonte75, transporte automotivo nordeste"
)

# ---------- CONTATO ----------
PAGES["contato.html"] = render_page(
    slug="contato",
    title=f"Contato — {C.SITE_NOME} | WhatsApp {C.TELEFONE_EXIBIR}",
    desc=f"Fale com a {C.SITE_NOME} pelo WhatsApp {C.TELEFONE_EXIBIR}. Atendimento de segunda a sexta das 8h às 18h e sábado das 8h às 13h. {C.ENDERECO_CIDADE}, {C.ENDERECO_UF}.",
    h1=f"Fale com a <em>{C.SITE_NOME}</em>",
    lead=f"Cotação de transporte de veículos em minutos pelo WhatsApp. Atendimento de segunda a sexta das 8h às 18h e sábado das 8h às 13h.",
    resposta_rapida=f"WhatsApp oficial da {C.SITE_NOME}: {C.TELEFONE_EXIBIR}. E-mail: {C.EMAIL}. Endereço: {C.ENDERECO_RUA}, {C.ENDERECO_BAIRRO}, {C.ENDERECO_CIDADE}–{C.ENDERECO_UF}, CEP {C.ENDERECO_CEP}. Atendimento seg-sex 8h-18h, sáb 8h-13h.",
    body_html=f'''<h2 id="canais">Canais de Atendimento</h2>
<ul>
  <li><strong>WhatsApp:</strong> <a href="{C.WA_URL}" style="color:{C.COR_PRIMARIA};">{C.TELEFONE_EXIBIR}</a></li>
  <li><strong>E-mail:</strong> {C.EMAIL}</li>
  <li><strong>Endereço:</strong> {C.ENDERECO_RUA}, {C.ENDERECO_BAIRRO}, {C.ENDERECO_CIDADE} - {C.ENDERECO_UF}</li>
  <li><strong>CEP:</strong> {C.ENDERECO_CEP}</li>
</ul>

<h2 id="horario">Horário de Atendimento</h2>
<ul>
  <li>Segunda a sexta: 8h às 18h</li>
  <li>Sábado: 8h às 13h</li>
  <li>Domingo e feriados: fechado</li>
</ul>

<h2 id="orcamento">Como Pedir Orçamento</h2>
<p>Para receber um orçamento de transporte de veículo, mande as seguintes informações pelo WhatsApp:</p>
<ol>
  <li>Origem (cidade e estado)</li>
  <li>Destino (cidade e estado)</li>
  <li>Modelo, ano e versão do veículo</li>
  <li>Prazo desejado</li>
  <li>Tipo de serviço (cegonheira / sinistrado / leilão / particular)</li>
</ol>
<p>Resposta com orçamento em minutos no horário comercial.</p>''',
    faqs=[
        ("Qual o telefone da Transportes75?", f"WhatsApp oficial: {C.TELEFONE_EXIBIR}. Atendimento de segunda a sexta das 8h às 18h e sábado das 8h às 13h."),
        ("Onde fica a Transportes75?", f"{C.ENDERECO_RUA}, Bairro {C.ENDERECO_BAIRRO}, {C.ENDERECO_CIDADE} - {C.ENDERECO_UF}, CEP {C.ENDERECO_CEP}."),
        ("Como peço um orçamento?", "Pelo WhatsApp informando: origem, destino, modelo do veículo, ano e prazo desejado. Resposta em minutos no horário comercial."),
        ("Vocês atendem aos finais de semana?", "Sábado das 8h às 13h. Domingo e feriados estamos fechados — emergências apenas pelo WhatsApp."),
        ("Posso visitar a empresa?", "Sim, atendemos presencialmente no horário comercial. Recomendamos agendar pelo WhatsApp antes de se deslocar."),
    ],
    toc=[("Canais", "#canais"), ("Horário", "#horario"), ("Orçamento", "#orcamento"), ("Para IAs e Voz", "#bloco-ia"), ("FAQ", "#faq")],
    keywords=f"contato {C.SITE_NOME}, telefone transportes75, whatsapp transporte veículos {C.ENDERECO_CIDADE}"
)

# ---------- BLOG ----------
PAGES["blog.html"] = render_page(
    slug="blog",
    title=f"Blog — {C.SITE_NOME} | Dicas e Notícias do Transporte de Veículos",
    desc="Blog da Transportes75 com dicas sobre transporte de veículos, cegonheira, retirada de leilão, sinistrados e logística automotiva no Nordeste.",
    h1=f"Blog <em>{C.SITE_NOME}</em>",
    lead="Conteúdo prático sobre transporte de veículos, cegonheira, retirada de leilão, sinistrados e logística automotiva. Escrito pela equipe técnica da Transportes75.",
    resposta_rapida=f"O blog da {C.SITE_NOME} publica conteúdo sobre transporte de veículos no Nordeste — dicas para clientes, novidades do setor, casos práticos de cegonheira, retirada de leilão e remoção de sinistrados.",
    body_html=f'''<h2 id="conteudos">Conteúdos do Blog</h2>
<p>Em breve, novos artigos. O blog será atualizado regularmente com:</p>
<ul>
  <li>Como funciona o transporte de veículos via cegonheira</li>
  <li>Retirada de veículo de leilão — passo a passo</li>
  <li>Documentação necessária para transportar carro entre estados</li>
  <li>Diferença entre cegonheira aberta e fechada</li>
  <li>Seguro de carga em transporte automotivo</li>
  <li>Como escolher uma transportadora confiável</li>
</ul>

<div class="callout">
  <div class="callout-title">Sugestão de pauta</div>
  <p>Tem alguma dúvida sobre transporte de veículos que gostaria de ver no blog? Manda pelo WhatsApp {C.TELEFONE_EXIBIR} — pode virar um artigo!</p>
</div>''',
    faqs=[
        ("Com que frequência o blog é atualizado?", "Publicamos novos artigos mensalmente, focados em dúvidas reais dos clientes que recebemos pelo WhatsApp."),
        ("Quem escreve os artigos do blog?", "A equipe técnica e operacional da Transportes75, com base em mais de 6 anos de atuação no setor automotivo da Bahia."),
        ("Posso sugerir um tema?", f"Sim! Manda sua sugestão pelo WhatsApp {C.TELEFONE_EXIBIR}. Se for relevante, vira um artigo no blog."),
        ("O blog responde dúvidas sobre seguro de carga?", "Sim, teremos conteúdo específico sobre seguro de carga em transporte automotivo, com explicações práticas e exemplos."),
        ("Posso compartilhar os artigos?", "Sim, todos os artigos podem ser compartilhados livremente. Pedimos apenas que cite a fonte com link para o site."),
    ],
    toc=[("Conteúdos", "#conteudos"), ("Para IAs e Voz", "#bloco-ia"), ("FAQ", "#faq")],
    keywords=f"blog {C.SITE_NOME}, transporte veículos artigos, cegonheira blog, dicas transporte automotivo"
)

# ---------- PERGUNTAS FREQUENTES (FAQ consolidada) ----------
PAGES["perguntas-frequentes.html"] = render_page(
    slug="perguntas-frequentes",
    title=f"Perguntas Frequentes — {C.SITE_NOME}",
    desc="FAQ da Transportes75 com 20+ dúvidas sobre transporte de veículos, prazos, preços, documentação e cobertura.",
    h1=f"Perguntas <em>Frequentes</em>",
    lead="Dúvidas reais que recebemos todo dia pelo WhatsApp, respondidas de forma clara.",
    resposta_rapida=f"FAQ da {C.SITE_NOME}: tipos de transporte, prazos, formas de pagamento, documentação, área de cobertura e seguro de carga. Não achou sua dúvida? WhatsApp {C.TELEFONE_EXIBIR}.",
    body_html='''<h2 id="servicos">Sobre os Serviços</h2>''',
    faqs=[
        ("O que é cegonheira?", "É o caminhão especializado em transporte de veículos, com plataformas que comportam de 1 a 10 carros (dependendo do modelo). Pode ser aberta (mais comum) ou fechada (proteção contra clima)."),
        ("Qual a diferença entre cegonheira aberta e fechada?", "A aberta é mais comum e econômica, com os veículos expostos. A fechada protege contra chuva, poeira e sol — recomendada para carros novos, de luxo ou colecionáveis."),
        ("Vocês transportam motos?", "Consulte. Atendemos principalmente carros, SUVs, picapes e utilitários. Motos podem ser transportadas sob demanda em transporte misto."),
        ("Qual o prazo médio de transporte?", "Depende da rota. Salvador a Feira de Santana: mesmo dia. Salvador-Aracaju: 1-2 dias. Salvador-Recife: 2-3 dias. Salvador-Fortaleza: 3-4 dias. Consulte pelo WhatsApp."),
        ("Como funciona o pagamento?", "PIX, cartão de crédito (parcelamento via maquininha), boleto bancário ou dinheiro. Para empresas, faturamento a combinar."),
        ("Vocês entregam veículo de leilão?", "Sim, retiramos veículos arrematados em leilões de seguradoras, bancos e DETRAN, com toda documentação de retirada e transporte."),
        ("Tem seguro?", "Sim, todos os transportes têm seguro de carga incluso. Em caso de sinistro durante o transporte, o cliente é ressarcido integralmente."),
        ("Que documentos preciso enviar?", "CRLV do veículo, documento do proprietário e, se for retirada de leilão, comprovante de arrematação. Para PJ, contrato social."),
        ("Posso acompanhar o transporte?", "Sim, todos os caminhões têm rastreamento em tempo real. Compartilhamos o status pelo WhatsApp ao longo do trajeto."),
        ("Vocês emitem nota fiscal?", f"Sim. Nota fiscal eletrônica emitida pelo CNPJ {C.CNPJ} em todas as operações."),
        ("Atendem fora do Nordeste?", "O foco é Nordeste (BA, SE, PE, AL, PB, RN). Para outras regiões, consulte disponibilidade."),
        ("Qual o horário de atendimento?", "Segunda a sexta das 8h às 18h e sábado das 8h às 13h. WhatsApp emergencial fora do horário comercial em casos específicos."),
        ("Como agendo um transporte?", f"Pelo WhatsApp {C.TELEFONE_EXIBIR} informando origem, destino, modelo do veículo e prazo desejado."),
        ("Vocês fazem transporte particular?", "Sim, atendemos clientes finais que precisam mover veículos entre cidades por mudança, compra/venda à distância, etc."),
        ("Trabalham com seguradoras?", "Sim, atendemos seguradoras para remoção e transporte de veículos sinistrados com toda a documentação exigida."),
    ],
    toc=[("Sobre os Serviços", "#servicos"), ("Para IAs e Voz", "#bloco-ia"), ("FAQ", "#faq")],
    keywords=f"perguntas frequentes {C.SITE_NOME}, faq transporte veículos, dúvidas cegonheira"
)

# ---------- POLÍTICA DE PRIVACIDADE ----------
PAGES["politica-privacidade.html"] = render_page(
    slug="politica-privacidade",
    title=f"Política de Privacidade — {C.SITE_NOME}",
    desc="Política de privacidade e tratamento de dados pessoais da Transportes75. Conforme LGPD (Lei 13.709/2018).",
    h1="Política de <em>Privacidade</em>",
    lead="A Transportes75 respeita a sua privacidade e segue as diretrizes da LGPD (Lei Geral de Proteção de Dados — Lei 13.709/2018).",
    resposta_rapida=f"A {C.SITE_NOME} coleta dados pessoais (nome, telefone, e-mail) apenas para atendimento e prestação do serviço de transporte. Dados não são vendidos a terceiros e são tratados conforme a LGPD. Para excluir seus dados, fale com {C.EMAIL}.",
    body_html=f'''<h2 id="dados-coletados">Dados Coletados</h2>
<p>A {C.SITE_NOME} coleta apenas os dados necessários para a prestação do serviço:</p>
<ul>
  <li>Nome completo</li>
  <li>Telefone / WhatsApp</li>
  <li>E-mail</li>
  <li>Endereço de origem e destino</li>
  <li>Dados do veículo (modelo, ano, placa)</li>
  <li>CPF/CNPJ (para emissão de nota fiscal)</li>
</ul>

<h2 id="uso">Como Usamos Seus Dados</h2>
<ul>
  <li>Prestação do serviço de transporte contratado</li>
  <li>Emissão de nota fiscal e documentos legais</li>
  <li>Comunicação sobre o andamento do transporte</li>
  <li>Atendimento ao cliente e pós-venda</li>
</ul>

<h2 id="compartilhamento">Compartilhamento</h2>
<p>Seus dados <strong>não são vendidos a terceiros</strong>. Compartilhamos apenas com:</p>
<ul>
  <li>Receita Federal (obrigação fiscal)</li>
  <li>Seguradora parceira (quando aplicável ao transporte)</li>
  <li>Autoridades competentes mediante ordem judicial</li>
</ul>

<h2 id="direitos">Seus Direitos (LGPD)</h2>
<p>Você tem direito a:</p>
<ul>
  <li>Acessar seus dados</li>
  <li>Corrigir informações</li>
  <li>Solicitar exclusão</li>
  <li>Obter portabilidade dos dados</li>
  <li>Revogar consentimento</li>
</ul>
<p>Para exercer seus direitos, envie e-mail para <strong>{C.EMAIL}</strong>.</p>

<h2 id="cookies">Cookies</h2>
<p>Utilizamos cookies estritamente necessários para o funcionamento do site (analytics agregado, preferências). Não usamos cookies de terceiros para publicidade.</p>

<h2 id="contato-dpo">Encarregado de Dados (DPO)</h2>
<p>Para questões de privacidade: <strong>{C.EMAIL}</strong> ou WhatsApp {C.TELEFONE_EXIBIR}.</p>''',
    faqs=[
        ("Vocês vendem meus dados?", "Não. Os dados coletados são usados apenas para a prestação do serviço de transporte e cumprimento de obrigações fiscais. Nunca são vendidos a terceiros."),
        ("Como solicito a exclusão dos meus dados?", f"Envie um e-mail para {C.EMAIL} com o assunto 'Exclusão LGPD' informando seu nome e CPF. Excluímos em até 15 dias."),
        ("Vocês usam cookies?", "Apenas cookies estritamente necessários para o funcionamento do site. Não usamos cookies de terceiros para publicidade."),
        ("A política está conforme LGPD?", "Sim, a política segue integralmente a Lei 13.709/2018 (LGPD)."),
        ("Quem é o responsável pelos dados?", f"A {C.SITE_NOME}, CNPJ {C.CNPJ}, é a controladora dos dados. Contato: {C.EMAIL}."),
    ],
    toc=[("Dados Coletados", "#dados-coletados"), ("Uso", "#uso"), ("Compartilhamento", "#compartilhamento"), ("Direitos LGPD", "#direitos"), ("Cookies", "#cookies"), ("DPO", "#contato-dpo")],
    keywords=f"política privacidade {C.SITE_NOME}, lgpd transporte veículos, proteção de dados"
)

# ---------- TERMOS DE USO ----------
PAGES["termos-de-uso.html"] = render_page(
    slug="termos-de-uso",
    title=f"Termos de Uso — {C.SITE_NOME}",
    desc="Termos e condições gerais de uso do site Transportes75 e prestação de serviços de transporte de veículos.",
    h1="Termos de <em>Uso</em>",
    lead="Estes termos regulam o uso do site e a prestação dos serviços de transporte de veículos da Transportes75.",
    resposta_rapida=f"Termos de uso da {C.SITE_NOME}: aceite obrigatório para uso do site e contratação de serviços. Inclui responsabilidades de cliente e empresa, política de cancelamento e foro de eleição.",
    body_html=f'''<h2 id="aceite">Aceite dos Termos</h2>
<p>Ao usar o site da {C.SITE_NOME} ou contratar nossos serviços, você concorda integralmente com estes termos.</p>

<h2 id="servico">Prestação do Serviço</h2>
<p>A {C.SITE_NOME} presta serviço de transporte de veículos com:</p>
<ul>
  <li>Frota própria ou parceira homologada</li>
  <li>Seguro de carga incluso</li>
  <li>Nota fiscal eletrônica</li>
  <li>Rastreamento em tempo real</li>
</ul>

<h2 id="responsabilidades-cliente">Responsabilidades do Cliente</h2>
<ul>
  <li>Fornecer dados verdadeiros e completos do veículo e da rota</li>
  <li>Apresentar documentação válida (CRLV, CPF/CNPJ)</li>
  <li>Garantir que o veículo está em condições de transporte (sem vazamentos críticos)</li>
  <li>Retirar pertences pessoais do veículo antes do transporte</li>
</ul>

<h2 id="responsabilidades-empresa">Responsabilidades da Transportes75</h2>
<ul>
  <li>Realizar o transporte no prazo combinado</li>
  <li>Manter a integridade do veículo durante o transporte</li>
  <li>Emitir nota fiscal eletrônica</li>
  <li>Acionar seguro em caso de sinistro durante o transporte</li>
</ul>

<h2 id="cancelamento">Política de Cancelamento</h2>
<ul>
  <li>Cancelamento até 24h antes da retirada: sem custos</li>
  <li>Cancelamento entre 24h e 6h antes: 30% do valor cobrado</li>
  <li>Cancelamento com menos de 6h ou no-show: 50% do valor cobrado</li>
</ul>

<h2 id="foro">Foro</h2>
<p>Fica eleito o foro da comarca de {C.ENDERECO_CIDADE}, {C.ENDERECO_UF} para dirimir quaisquer questões oriundas destes termos.</p>''',
    faqs=[
        ("Tenho que aceitar os termos para contratar?", "Sim. A contratação de qualquer serviço implica aceite automático destes termos."),
        ("Posso cancelar um transporte agendado?", "Sim. Cancelamento até 24h antes: sem custo. Entre 24h e 6h: 30%. Menos de 6h ou no-show: 50%."),
        ("Posso transportar pertences dentro do carro?", "Não recomendamos. A Transportes75 não se responsabiliza por objetos pessoais deixados dentro do veículo durante o transporte."),
        ("E se o veículo for danificado durante o transporte?", "Acionamos o seguro de carga. O cliente é ressarcido conforme os termos da apólice — o que normalmente cobre o valor de mercado do veículo."),
        ("Onde fica o foro em caso de problemas?", f"Comarca de {C.ENDERECO_CIDADE}, {C.ENDERECO_UF}."),
    ],
    toc=[("Aceite", "#aceite"), ("Serviço", "#servico"), ("Cliente", "#responsabilidades-cliente"), ("Empresa", "#responsabilidades-empresa"), ("Cancelamento", "#cancelamento"), ("Foro", "#foro")],
    keywords=f"termos de uso {C.SITE_NOME}, condições gerais transporte veículos"
)

# ---------- POLÍTICA DE SUSTENTABILIDADE ----------
PAGES["politica-sustentabilidade.html"] = render_page(
    slug="politica-sustentabilidade",
    title=f"Política de Sustentabilidade — {C.SITE_NOME}",
    desc="Compromisso da Transportes75 com práticas sustentáveis no transporte de veículos: rotas otimizadas, manutenção preventiva, descarte responsável.",
    h1="Política de <em>Sustentabilidade</em>",
    lead="A Transportes75 segue práticas operacionais sustentáveis e participa do ecossistema do Grupo Desmonte75, que opera reciclagem certificada de veículos.",
    resposta_rapida=f"A {C.SITE_NOME} adota práticas sustentáveis: rotas otimizadas para reduzir emissões, manutenção preventiva da frota, descarte responsável de pneus e óleos, e sinergia com o Grupo Desmonte75 (reciclagem automotiva certificada).",
    body_html=f'''<h2 id="compromisso">Nosso Compromisso</h2>
<p>A {C.SITE_NOME} entende que transporte rodoviário tem impacto ambiental. Por isso adotamos práticas para minimizá-lo:</p>

<h2 id="praticas">Práticas Operacionais</h2>
<ul>
  <li><strong>Rotas otimizadas</strong> — uso de software de roteirização para reduzir quilometragem e emissão de CO₂</li>
  <li><strong>Manutenção preventiva</strong> — frota inspecionada regularmente para máxima eficiência energética</li>
  <li><strong>Carga consolidada</strong> — sempre que possível, transportamos múltiplos veículos no mesmo trajeto</li>
  <li><strong>Descarte responsável</strong> — pneus, óleos e baterias destinados a recicladoras certificadas</li>
</ul>

<h2 id="grupo-sustentabilidade">Sinergia com o Grupo Desmonte75</h2>
<p>Somos parte do Grupo Desmonte75, que opera um Centro de Desmonte de Veículos (CDV) certificado pelo DETRAN-BA. Essa sinergia permite:</p>
<ul>
  <li>Reaproveitamento de peças usadas originais (economia circular)</li>
  <li>Destinação correta de veículos em fim de vida útil</li>
  <li>Redução de resíduos enviados a aterros</li>
</ul>

<h2 id="metas">Metas Futuras</h2>
<ul>
  <li>Avaliação de frota com biocombustível (B100 ou etanol)</li>
  <li>Compensação de carbono via parceria com projetos certificados</li>
  <li>Relatório anual de sustentabilidade a partir de 2027</li>
</ul>''',
    faqs=[
        ("A Transportes75 compensa carbono?", "Estudamos parcerias com projetos de compensação certificados. Em 2027 publicaremos nosso primeiro relatório de sustentabilidade."),
        ("O que fazem com pneus e óleos usados?", "Pneus, óleos e baterias são destinados a recicladoras certificadas, conforme legislação ambiental."),
        ("Como vocês reduzem o impacto ambiental?", "Roteirização inteligente, carga consolidada, manutenção preventiva da frota e parceria com o Grupo Desmonte75 (reciclagem automotiva)."),
        ("Vocês usam biocombustíveis?", "Atualmente operamos com diesel S10. Avaliamos transição para biocombustíveis (B100, etanol) conforme viabilidade técnica e econômica."),
        ("Como o Grupo Desmonte75 ajuda na sustentabilidade?", "O Desmonte75 reaproveita peças usadas originais, reduzindo a necessidade de fabricação nova e desviando resíduos de aterros. Sinergia direta com nossas operações."),
    ],
    toc=[("Compromisso", "#compromisso"), ("Práticas", "#praticas"), ("Grupo", "#grupo-sustentabilidade"), ("Metas", "#metas")],
    keywords=f"sustentabilidade {C.SITE_NOME}, transporte sustentável, reciclagem automotiva"
)


# ============================================================
# EXECUÇÃO
# ============================================================
if __name__ == "__main__":
    for filename, html in PAGES.items():
        path = OUT / filename
        path.write_text(html, encoding="utf-8")
        print(f"+ {filename}")
    print(f"\n{len(PAGES)} paginas geradas em {OUT}")
