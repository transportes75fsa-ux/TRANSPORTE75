# Transportes75 — Status do Projeto

**Última atualização:** 03/06/2026

## ✅ Pronto

### Configuração
- `scripts/config.py` — variáveis centralizadas
- CNPJ: 65.499.243/0001-61
- WhatsApp: (75) 99285-2199 → `https://wa.me/5575992852199`
- Endereço: Rua Professor Fernando São Paulo, 944, Feira de Santana - BA
- Autor: **Sergio Torres**, 40 anos no setor de transporte de pessoas e cargas
- Cores: Laranja `#f97316` + cinza `#1f2937`
- Rota: **Bahia ↔ São Paulo** via BR-116 (~2.000 km, 3-4 dias úteis)

### Páginas geradas (todas com 8 elementos AEO)
1. `/index.html` — Home com hero foto cegonha + logo redonda 234px
2. `/sobre-nos.html`
3. `/contato.html`
4. `/blog.html` — listagem dos 5 artigos
5. `/perguntas-frequentes.html`
6. `/politica-privacidade.html`
7. `/termos-de-uso.html`
8. `/politica-sustentabilidade.html` — versão simplificada (manutenção + direção econômica)

### Blog (5 artigos por Sergio Torres)
1. `/blog/como-funciona-cegonha-bahia-sao-paulo.html` — 02 JUN, 2026
2. `/blog/quanto-custa-transportar-carro-bahia-sao-paulo.html` — 22 MAI, 2026
3. `/blog/prazo-cegonha-salvador-sao-paulo.html` — 28 ABR, 2026
4. `/blog/transporte-veiculos-leilao-bahia-sao-paulo.html` — 02 ABR, 2026
5. `/blog/br-116-rio-bahia-corredor-cegonhas.html` — 15 MAR, 2026

### Logomarca
- Original 1024×1024 (3D metálica) recortada em círculo anti-alias
- Versões: 512px, 256px, 64px, favicon 32px, apple-touch 180px
- Hero da home: 234×234px no canto superior esquerdo
- Footer: 90×90px

### Hero da home
- Foto da cegonha pôr-do-sol (139KB WebP)
- Overlay escuro gradient
- Logo grande sobreposta
- 3 badges: Cegonha BA↔SP, Frota Rastreada, BR-116
- H1 com keyword principal
- Botão WhatsApp verde grandão

### Páginas internas
- Header com layout grid: texto à esquerda + foto da CARRETA REAL (`cegonha-transportes75.webp`) à direita
- line-height 1.15 + padding-top 0.3em + overflow visible (acentos não cortam)

### Limpeza completa (ZERO menções)
- ❌ Desmonte75 / Grupo Desmonte75 / desmanche / CDV / Luciano
- ❌ Nordeste (rota correta é BA↔SP)
- ❌ nota fiscal / seguro de carga
- ❌ cegonha fechada (só aberta)
- ❌ "linha branca" (proibido)

## 🚀 No servidor local

Rodando em: **http://localhost:8888/**

Pra subir o servidor (se cair):
```powershell
cd C:\VPSLOJA\sitetransportes75
python -m http.server 8888
```

## 📦 VPS Contabo

- Pasta: `/var/www/transportes75/`
- Nginx: `/etc/nginx/sites-available/transportes75.com.br` (ativo)
- SSL: compartilhando cert do desmonte75 (Cloudflare Flexible)
- Acessível com Host header até DNS apontar

## ❌ Pendente

- [ ] Registrar domínio `transportes75.com.br` (no registro.br)
- [ ] Apontar DNS pro Cloudflare
- [ ] Ajustar cada página individualmente (em andamento)
- [ ] Subir VPS quando aprovado

## 🎯 Próximas etapas

Foi decidido: amanhã abrir contexto novo direto nessa pasta (`C:\VPSLOJA\sitetransportes75\`) para continuar página por página sem misturar com Desmonte75.

## 📂 Scripts importantes

- `scripts/config.py` — variáveis
- `scripts/gerar_site_base.py` — gera as 8 páginas base
- `scripts/gerar_blog.py` — gera os 5 artigos do blog + listagem

Para regerar tudo:
```powershell
cd C:\VPSLOJA\sitetransportes75\scripts
python gerar_site_base.py
python gerar_blog.py
```
