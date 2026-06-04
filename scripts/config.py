#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuração central do site Transportes75.

>>> ALTERE AQUI <<< quando tiver as definições finais. Depois rode:
    py -3 gerar_site_base.py

Tudo na pasta /var/www/transportes75/ na VPS Contabo.
"""

# ============================================================
# IDENTIDADE
# ============================================================
SITE_NOME = "Transportes75"
SITE_TAGLINE = "Transporte de Veículos Bahia ↔ São Paulo"
SITE_DESC_CURTA = "Transporte de veículos na rota Bahia ↔ São Paulo. Cegonha, sinistrados, leilão e particular. Frota rastreada na BR-116."

# ============================================================
# DOMÍNIO E URLS (TROCAR depois do registro)
# ============================================================
DOMINIO = "transportes75.com.br"          # ← AJUSTAR após registro
URL_BASE = f"https://{DOMINIO}"
URL_BASE_SLASH = f"{URL_BASE}/"

# ============================================================
# CONTATO
# ============================================================
WHATSAPP_NUMERO = "5575992852199"          # WhatsApp oficial Transportes75
TELEFONE_EXIBIR = "(75) 99285-2199"
WA_URL = f"https://wa.me/{WHATSAPP_NUMERO}"
EMAIL = "contato@transportes75.com.br"    # ← AJUSTAR

# ============================================================
# EMPRESA
# ============================================================
CNPJ = "65.499.243/0001-61"               # CNPJ do grupo
RAZAO_SOCIAL = "Transportes75"
ANO_FUNDACAO = "2026"                      # ← AJUSTAR se necessário

# Endereço
ENDERECO_RUA = "Rua Professor Fernando São Paulo, 944"
ENDERECO_BAIRRO = "São João"
ENDERECO_CIDADE = "Feira de Santana"
ENDERECO_UF = "BA"
ENDERECO_ESTADO = "Bahia"
ENDERECO_CEP = "44051-706"
LAT = -12.2739
LON = -38.9618

# ============================================================
# ÁREA DE ATENDIMENTO — Rota BA ↔ SP
# ============================================================
ESTADOS_ATENDIDOS = ["Bahia", "Minas Gerais", "São Paulo"]   # rota e passagem
CIDADES_PRINCIPAIS = [
    "Salvador", "Feira de Santana", "Vitória da Conquista", "Jequié",   # BA
    "Belo Horizonte", "Governador Valadares", "Montes Claros",            # MG (passagem)
    "São Paulo", "Campinas", "São José dos Campos", "Ribeirão Preto"     # SP
]
ROTA_PRINCIPAL = "Bahia ↔ São Paulo"
RODOVIA_PRINCIPAL = "BR-116 (Rio-Bahia)"
DISTANCIA_KM_APROX = 2000   # Salvador → São Paulo

# ============================================================
# CORES E BRANDING — paleta LARANJA + CINZA (Transportes75)
# ============================================================
COR_PRIMARIA = "#f97316"           # laranja vibrante (orange-500)
COR_PRIMARIA_2 = "#fb923c"         # laranja claro (orange-400)
COR_DESTAQUE = "#3db870"           # verde mantido (combina com laranja)
COR_FUNDO = "#1f2937"              # cinza escuro (gray-800)
COR_FUNDO_2 = "#374151"            # cinza médio (gray-700) — cards
COR_FUNDO_3 = "#4b5563"            # cinza claro (gray-600) — accents
COR_TEXTO = "#e5e7eb"              # cinza muito claro (gray-200) — texto
LOGO_PATH = "/logomarca_redonda.webp"   # ← trocar quando tiver logo Transportes75

# ============================================================
# AUTOR
# ============================================================
AUTOR_NOME = "Sergio Torres"
AUTOR_CARGO = "Especialista · Transportes75 — Feira de Santana, BA"
AUTOR_BIO = "40 anos de experiência no setor de transporte de pessoas e cargas. Especialista em logística rodoviária, operações de cegonha e transporte de veículos na rota Bahia ↔ São Paulo. Sergio é responsável pela operação técnica e estratégica da Transportes75."
AUTOR_FOTO = "/img/sergio-torres-transportes75.webp"

# ============================================================
# REDES SOCIAIS (opcional)
# ============================================================
INSTAGRAM = ""          # ← preencher se houver
FACEBOOK = ""
YOUTUBE = ""
LINKEDIN = ""

# ============================================================
# SERVIÇOS PRINCIPAIS
# ============================================================
SERVICOS = [
    {
        "slug": "cegonha",
        "titulo": "Cegonha",
        "desc": "Transporte de veículos novos e seminovos para concessionárias, revendas e clientes finais."
    },
    {
        "slug": "sinistrados",
        "titulo": "Veículos Sinistrados",
        "desc": "Remoção e transporte de veículos batidos para seguradoras, oficinas e centros de desmonte."
    },
    {
        "slug": "leilao",
        "titulo": "Veículos de Leilão",
        "desc": "Retirada e entrega de veículos arrematados em leilões — cobertura nacional."
    },
    {
        "slug": "particular",
        "titulo": "Particular",
        "desc": "Transporte de carros entre cidades para clientes finais com agendamento e rastreamento."
    },
]

# ============================================================
# HOSPEDAGEM / DEPLOY
# ============================================================
VPS_HOST = "161.97.91.64"
VPS_USER = "root"
VPS_PATH = "/var/www/transportes75"
