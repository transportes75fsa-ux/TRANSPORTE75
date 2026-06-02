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
SITE_TAGLINE = "Transporte de Veículos — Grupo Desmonte75"
SITE_DESC_CURTA = "Transporte de veículos especializado em todo o Nordeste — cegonheira, sinistrados, leilão. Empresa do Grupo Desmonte75."

# ============================================================
# DOMÍNIO E URLS (TROCAR depois do registro)
# ============================================================
DOMINIO = "transportes75.com.br"          # ← AJUSTAR após registro
URL_BASE = f"https://{DOMINIO}"
URL_BASE_SLASH = f"{URL_BASE}/"

# ============================================================
# CONTATO (TROCAR se for número diferente)
# ============================================================
WHATSAPP_NUMERO = "557599960075"          # mesmo número Desmonte75 por enquanto
TELEFONE_EXIBIR = "(75) 9996-0075"
WA_URL = f"https://wa.me/{WHATSAPP_NUMERO}"
EMAIL = "contato@transportes75.com.br"    # ← AJUSTAR

# ============================================================
# EMPRESA
# ============================================================
CNPJ = "65.499.243/0001-61"               # ← AJUSTAR se for CNPJ separado
RAZAO_SOCIAL = "Transportes75 — Grupo Desmonte75"
ANO_FUNDACAO = "2018"

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
# ÁREA DE ATENDIMENTO
# ============================================================
ESTADOS_ATENDIDOS = ["Bahia", "Sergipe", "Pernambuco", "Alagoas", "Paraíba", "Rio Grande do Norte"]
CIDADES_PRINCIPAIS = ["Salvador", "Aracaju", "Recife", "Maceió", "João Pessoa", "Natal", "Feira de Santana", "Vitória da Conquista"]

# ============================================================
# CORES E BRANDING (paleta inicial = mesma Desmonte75)
# ============================================================
COR_PRIMARIA = "#3498db"           # azul
COR_PRIMARIA_2 = "#5dade2"
COR_DESTAQUE = "#3db870"           # verde
COR_FUNDO = "#0e0e0e"              # quase preto
COR_TEXTO = "#e5e2e1"
LOGO_PATH = "/logomarca_redonda.webp"   # ← trocar quando tiver logo Transportes75

# ============================================================
# AUTOR (mesmo padrão Desmonte75)
# ============================================================
AUTOR_NOME = "Luciano Cortes Sales"
AUTOR_CARGO = "Fundador · Transportes75 — Feira de Santana, BA"
AUTOR_BIO = "Apaixonado por veículos desde os 12 anos, Luciano tem mais de 23 anos de experiência em desmanche certificado e mais de 42 anos em recuperação automotiva. Fundador do Grupo Desmonte75, agora expandindo para transporte de veículos com a Transportes75."
AUTOR_FOTO = "/img/luciano-cortes-sales-desmonte75.webp"

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
        "titulo": "Cegonheira",
        "desc": "Transporte de veículos novos para concessionárias e revendas em todo o Nordeste."
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
