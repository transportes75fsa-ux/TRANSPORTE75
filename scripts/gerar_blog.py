#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera os 5 artigos do blog Transportes75 + atualiza a página /blog.html
Cada artigo:
  - palavras-chave estratégicas (BA↔SP)
  - Article schema + FAQPage schema + BreadcrumbList
  - Assinatura Sergio Torres (40 anos no setor)
  - 5 elementos AEO: resposta-rapida, article-lead, faqs, speakable, hidden block
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import config as C
from gerar_site_base import NAV, FOOTER, CSS_INLINE, AUTHOR_BOX, js, org_schema, speakable_schema

OUT = Path(__file__).parent.parent

# ============================================================
# DEFINIÇÃO DOS 5 ARTIGOS
# ============================================================
ARTIGOS = [
    {
        "slug": "como-funciona-cegonha-bahia-sao-paulo",
        "titulo_curto": "Como Funciona a Cegonha BA ↔ SP",
        "title": "Como Funciona a Cegonha Bahia ↔ São Paulo — Guia Completo | Transportes75",
        "desc": "Entenda como funciona o transporte de carro via cegonha de Salvador a São Paulo: processo, prazos, capacidade da carreta e o que esperar do serviço.",
        "h1": "Como Funciona a <em>Cegonha</em> Bahia ↔ São Paulo",
        "data": "02 JUN, 2026",
        "lead": "Transportar um carro pela rota Bahia ↔ São Paulo via cegonha é o método mais seguro e econômico para mover veículos entre os dois estados. Veja como funciona o processo do começo ao fim.",
        "resposta_rapida": "A cegonha é um caminhão especializado em transporte de veículos, com capacidade de até 10 carros por viagem. Na rota Bahia ↔ São Paulo, a Transportes75 percorre cerca de 2.000 km pela BR-116 em 3 a 4 dias úteis, com rastreamento em tempo real e equipe liderada por Sergio Torres, com 40 anos de experiência no setor.",
        "keywords": "como funciona cegonha, transporte carro bahia são paulo, cegonha ba sp, transportar carro salvador são paulo, br-116",
        "body": """<h2 id="o-que-e-cegonha">O Que É uma Cegonha?</h2>
<p>A cegonha é um <strong>caminhão de carga especializado em transportar veículos</strong>, projetado com plataformas em dois andares que comportam de 1 a 10 carros por viagem, dependendo do modelo. É o método mais usado no Brasil para mover veículos entre concessionárias, leilões, oficinas e clientes finais entre cidades distantes.</p>
<p>Na rota <strong>Bahia ↔ São Paulo</strong>, a cegonha é praticamente a única forma viável e econômica de transportar carros — a alternativa (transportar o veículo dirigindo) consome combustível, depreciação e tempo do motorista, além de aumentar o risco de avarias.</p>

<h2 id="processo">O Processo Passo a Passo</h2>
<p>Quando você contrata a <strong>Transportes75</strong> para transportar um veículo entre Bahia e São Paulo, o processo segue 6 etapas:</p>
<ol>
  <li><strong>Cotação:</strong> você envia origem, destino, modelo, ano e prazo desejado pelo WhatsApp. Em minutos recebe um orçamento.</li>
  <li><strong>Agendamento:</strong> definimos data de coleta e entrega. Para a maioria das rotas BA ↔ SP, a coleta acontece em até 48h.</li>
  <li><strong>Coleta:</strong> a cegonha vai até o endereço de origem. Fazemos inspeção visual e fotográfica do veículo antes de carregar.</li>
  <li><strong>Embarque:</strong> o veículo é fixado na plataforma da cegonha com cintas e travas específicas. Esse processo é técnico e exige treinamento.</li>
  <li><strong>Trajeto:</strong> percorremos cerca de 2.000 km pela BR-116, passando por Minas Gerais. Rastreamento em tempo real compartilhado pelo WhatsApp.</li>
  <li><strong>Entrega:</strong> o veículo é descarregado e entregue ao destinatário com nova inspeção visual e assinatura de recebimento.</li>
</ol>

<h2 id="prazo-rota">Prazo da Rota BA ↔ SP</h2>
<p>O prazo padrão para o trajeto Bahia ↔ São Paulo é de <strong>3 a 4 dias úteis</strong> contados a partir da coleta. Esse prazo considera:</p>
<ul>
  <li>Carregamento e inspeção (algumas horas)</li>
  <li>Trajeto pela BR-116, com paradas obrigatórias de descanso do motorista</li>
  <li>Eventuais consolidações de carga em pontos estratégicos (Feira de Santana, Belo Horizonte)</li>
  <li>Descarregamento e entrega no destino</li>
</ul>
<p>Para rotas específicas como <strong>Salvador ↔ São Paulo capital</strong>, o prazo médio é de 3 a 4 dias úteis. Para cidades menores ou no interior, pode chegar a 4 a 5 dias úteis.</p>

<h2 id="capacidade">Capacidade e Tipos de Veículos</h2>
<p>Nossas cegonhas comportam <strong>até 10 veículos por viagem</strong>. Trabalhamos com:</p>
<ul>
  <li>Carros de passeio (hatch, sedan, SUV)</li>
  <li>Picapes leves e médias</li>
  <li>Utilitários compactos</li>
  <li>Veículos sinistrados (que não andam)</li>
</ul>
<p>Para cargas pesadas (caminhões, ônibus, máquinas), consulte cotação específica pelo WhatsApp.</p>

<h2 id="vantagens">Por Que Escolher Cegonha na Rota BA ↔ SP</h2>
<ul>
  <li><strong>Custo menor</strong> que dirigir o veículo (sem combustível, sem desgaste, sem hospedagem)</li>
  <li><strong>Zero quilometragem adicional</strong> no seu carro</li>
  <li><strong>Risco controlado</strong> — cegonha é mais segura que dirigir 2.000 km</li>
  <li><strong>Tempo do cliente preservado</strong> — você não perde 3 dias dirigindo</li>
  <li><strong>Rastreamento</strong> em tempo real pelo WhatsApp</li>
</ul>
""",
        "faqs": [
            ("Quanto tempo leva uma cegonha de Salvador a São Paulo?", "Em média 3 a 4 dias úteis. O trajeto de 2.000 km pela BR-116 inclui carregamento, descanso obrigatório do motorista e descarga no destino."),
            ("Quantos carros cabem em uma cegonha?", "De 1 a 10 veículos, dependendo do modelo da carreta. A Transportes75 opera com cegonhas de média e alta capacidade na rota BA ↔ SP."),
            ("A cegonha entrega na minha porta?", "Sim, fazemos coleta e entrega em endereços específicos, tanto na origem quanto no destino. Locais sem acesso para carreta podem ter pontos de coleta combinados."),
            ("Posso colocar pertences dentro do carro?", "Não recomendamos. A Transportes75 não se responsabiliza por objetos pessoais deixados dentro do veículo durante o transporte."),
            ("Como acompanho a viagem do meu carro?", "Pelo WhatsApp. Compartilhamos rastreamento em tempo real ao longo do trajeto Bahia ↔ São Paulo."),
        ],
    },
    {
        "slug": "quanto-custa-transportar-carro-bahia-sao-paulo",
        "titulo_curto": "Quanto Custa Transportar Carro BA ↔ SP",
        "title": "Quanto Custa Transportar um Carro da Bahia para São Paulo? | Transportes75",
        "desc": "Saiba quanto custa transportar um veículo entre Bahia e São Paulo via cegonha. Fatores que influenciam o preço, faixas de valor e como cotar.",
        "h1": "Quanto Custa <em>Transportar um Carro</em> Bahia ↔ São Paulo?",
        "data": "22 MAI, 2026",
        "lead": "O custo de transportar um veículo pela rota Bahia ↔ São Paulo varia conforme distância, tipo de veículo, época do ano e modalidade. Veja os principais fatores que influenciam o preço.",
        "resposta_rapida": "O custo de transporte de carro Bahia ↔ São Paulo via cegonha varia conforme distância, modelo do veículo e modalidade. Para cotação personalizada da Transportes75, fale pelo WhatsApp (75) 99285-2199 informando origem, destino, modelo e prazo.",
        "keywords": "quanto custa transportar carro bahia são paulo, preço cegonha ba sp, valor transporte veículo, cotação cegonha salvador são paulo",
        "body": """<h2 id="fatores">Fatores que Influenciam o Preço</h2>
<p>O valor do transporte de carro pela rota <strong>Bahia ↔ São Paulo</strong> não é fixo. Cinco variáveis principais entram no cálculo:</p>

<h3 id="distancia">1. Distância da Rota</h3>
<p>O trajeto principal Salvador ↔ São Paulo é de aproximadamente <strong>2.000 km pela BR-116</strong>. Rotas a partir de cidades do interior baiano (Vitória da Conquista, Feira de Santana, Jequié) podem reduzir ou aumentar o trajeto em centenas de quilômetros.</p>

<h3 id="tipo-veiculo">2. Tipo e Tamanho do Veículo</h3>
<p>Um sedan compacto ocupa um espaço menor na cegonha que uma SUV grande ou picape estendida. Quanto maior o veículo, maior o "peso" relativo na cubagem da carreta.</p>

<h3 id="urgencia">3. Prazo e Urgência</h3>
<p>Transporte dedicado (cegonha que sai apenas com o seu carro) custa mais que transporte consolidado (cegonha cheia, dividindo o frete entre vários clientes). Para o cliente final que pode esperar 3-4 dias úteis, o consolidado é mais econômico.</p>

<h3 id="origem-destino">4. Cidade de Origem e Destino</h3>
<p>Capitais com grande movimento (Salvador, São Paulo, Campinas) têm tarifas mais competitivas que cidades remotas. Locais sem ponto de coleta podem exigir taxa de "guincho parcial".</p>

<h3 id="sazonalidade">5. Época do Ano</h3>
<p>Em períodos de pico (fim de ano, férias, leilões de seguradoras concentrados), há demanda maior e preços tendem a subir. Em meses normais, o valor é estável.</p>

<h2 id="cotacao">Como Obter uma Cotação Real</h2>
<p>Não trabalhamos com tabela fixa porque cada caso é único. Para receber um <strong>orçamento personalizado de transporte BA ↔ SP</strong>, envie pelo WhatsApp:</p>
<ul>
  <li>Cidade de origem (bairro se for SP capital ou Salvador)</li>
  <li>Cidade de destino</li>
  <li>Modelo, ano e versão do veículo</li>
  <li>Prazo desejado (urgência ou flexível)</li>
  <li>Se o veículo está em condições de andar (importante para sinistrados)</li>
</ul>
<p>Em até algumas horas no horário comercial você recebe uma proposta com valor, prazo e condições.</p>

<h2 id="economia">Vale Mais a Pena que Dirigir?</h2>
<p>Vamos comparar transportar via cegonha vs dirigir Salvador → São Paulo (2.000 km):</p>
<ul>
  <li><strong>Combustível:</strong> ~R$ 1.200 (carro 1.0 fazendo 12 km/l)</li>
  <li><strong>Pedágios:</strong> ~R$ 250 na BR-116</li>
  <li><strong>Hospedagem:</strong> 2 noites de hotel ~R$ 500</li>
  <li><strong>Alimentação:</strong> ~R$ 300</li>
  <li><strong>Depreciação do veículo:</strong> 2.000 km de uso</li>
  <li><strong>Tempo do motorista:</strong> 3 dias inteiros</li>
</ul>
<p>Total estimado dirigindo: <strong>R$ 2.250 + tempo + desgaste</strong>. Em geral, a cegonha sai mais barato e poupa tempo, especialmente para quem trabalha.</p>

<h2 id="formas-pagamento">Formas de Pagamento</h2>
<p>A Transportes75 aceita PIX, cartão de crédito (parcelamento via maquininha), boleto bancário e dinheiro. Para empresas, faturamento conforme acordo.</p>
""",
        "faqs": [
            ("Tem tabela fixa de preço para a rota BA ↔ SP?", "Não. Cada cotação é personalizada porque depende de origem exata, destino, modelo do veículo, prazo e disponibilidade da frota. Cotação grátis pelo WhatsApp (75) 99285-2199."),
            ("Qual a faixa de preço média para transportar um carro de Salvador a São Paulo?", "O valor varia bastante conforme o veículo e a modalidade. Para receber um orçamento real, envie os dados do veículo pelo WhatsApp."),
            ("Posso parcelar o transporte?", "Sim, parcelamos no cartão de crédito conforme aprovação da operadora. Para empresas, faturamento a combinar."),
            ("O preço inclui carga e descarga?", "Sim. Carga, descarga e inspeção visual estão inclusas no valor da cotação."),
            ("Tem desconto para mais de um carro?", "Sim. Transportes consolidados (vários veículos em uma única cegonha) podem ter desconto progressivo. Consulte pelo WhatsApp."),
        ],
    },
    {
        "slug": "prazo-cegonha-salvador-sao-paulo",
        "titulo_curto": "Prazo Cegonha Salvador → SP",
        "title": "Quanto Tempo Demora uma Cegonha de Salvador a São Paulo? | Transportes75",
        "desc": "Veja o prazo real de uma cegonha entre Salvador e São Paulo pela BR-116. Fatores que afetam o tempo, paradas obrigatórias e rastreamento.",
        "h1": "Quanto Tempo <em>Demora uma Cegonha</em> de Salvador a São Paulo?",
        "data": "28 ABR, 2026",
        "lead": "O trajeto Salvador ↔ São Paulo via cegonha leva em média 3 a 4 dias úteis pela BR-116. Entenda quais fatores impactam o prazo e como acompanhar a viagem em tempo real.",
        "resposta_rapida": "Uma cegonha leva em média 3 a 4 dias úteis para percorrer Salvador ↔ São Paulo (2.000 km pela BR-116). O prazo considera tempo de carregamento, descanso obrigatório do motorista pela Lei do Motorista, eventuais paradas técnicas e descarga.",
        "keywords": "prazo cegonha salvador são paulo, quanto tempo leva cegonha ba sp, tempo transporte carro bahia são paulo, br-116 prazo",
        "body": """<h2 id="prazo-padrao">Prazo Padrão da Rota</h2>
<p>O trajeto <strong>Salvador ↔ São Paulo via cegonha</strong> leva em média <strong>3 a 4 dias úteis</strong>. Esse prazo é contado a partir da coleta do veículo na origem até a entrega no destino. Não inclui o tempo de agendamento e cotação inicial.</p>

<h2 id="distancia">A Distância Real do Trajeto</h2>
<p>A rota mais usada é a BR-116 (também chamada de Rio-Bahia), que conecta as duas regiões em aproximadamente <strong>2.000 km</strong>. Cidades de passagem importantes:</p>
<ul>
  <li><strong>Bahia:</strong> Feira de Santana, Vitória da Conquista, Jequié</li>
  <li><strong>Minas Gerais:</strong> Montes Claros, Governador Valadares, Belo Horizonte, Juiz de Fora</li>
  <li><strong>São Paulo:</strong> entrada via Rodovia Presidente Dutra, passando por São José dos Campos</li>
</ul>

<h2 id="fatores">Fatores que Afetam o Prazo</h2>

<h3 id="lei-motorista">Lei do Motorista (Lei 13.103/2015)</h3>
<p>A legislação brasileira obriga descansos obrigatórios:</p>
<ul>
  <li>30 minutos de descanso a cada 6 horas de direção</li>
  <li>11 horas consecutivas de descanso em 24 horas</li>
  <li>Repouso semanal de 35 horas</li>
</ul>
<p>Para um trajeto de 2.000 km, isso significa <strong>pelo menos 2 noites de descanso</strong> obrigatório no caminho.</p>

<h3 id="rodoviario">Condições da Rodovia</h3>
<p>A BR-116 tem trechos com obras frequentes, pedágios e regiões serranas (especialmente no sul de Minas e norte de SP). Chuvas fortes podem causar pequenos atrasos.</p>

<h3 id="consolidacao">Consolidação de Carga</h3>
<p>Cegonhas tipicamente fazem rotas com múltiplos veículos. Se sua cegonha precisa fazer paradas em Belo Horizonte ou em outras cidades para coletar/entregar outros carros, isso pode adicionar 1 dia ao prazo total.</p>

<h2 id="agendamento">Tempo de Agendamento (antes da coleta)</h2>
<p>O tempo entre o pedido e o início do transporte varia:</p>
<ul>
  <li><strong>Rotas regulares</strong> (semanal): coleta em 2-5 dias</li>
  <li><strong>Pedido urgente</strong> (dedicado): coleta no mesmo dia ou no dia seguinte, com tarifa diferenciada</li>
  <li><strong>Períodos de pico</strong> (fim de ano, leilões): pode estender em alguns dias</li>
</ul>

<h2 id="rastreamento">Como Acompanhar a Viagem</h2>
<p>A Transportes75 fornece <strong>rastreamento em tempo real</strong> pelo WhatsApp. Você recebe:</p>
<ul>
  <li>Confirmação do embarque com foto do veículo carregado</li>
  <li>Atualizações de localização ao longo do trajeto</li>
  <li>Aviso de chegada antecipado para preparar a recepção</li>
  <li>Foto do veículo descarregado no destino</li>
</ul>

<h2 id="urgencia">Quando Preciso de Prazo Menor</h2>
<p>Para quem tem urgência, oferecemos transporte <strong>dedicado expresso</strong> — a cegonha sai apenas com seu veículo, sem paradas para consolidação. Reduz o prazo para 2-3 dias úteis, com tarifa diferenciada. Consulte disponibilidade.</p>
""",
        "faqs": [
            ("Em quantos dias chega minha cegonha em São Paulo?", "Em média 3 a 4 dias úteis a partir da coleta em Salvador, pela BR-116."),
            ("Posso ter o carro entregue no mesmo dia?", "Não para a rota BA ↔ SP. A distância de 2.000 km e a Lei do Motorista exigem no mínimo 2-3 dias de trajeto."),
            ("Como sei se a cegonha está atrasada?", "Você recebe atualizações em tempo real pelo WhatsApp. Se houver imprevisto (rodovia interditada, problema mecânico), avisamos imediatamente com novo prazo."),
            ("Posso escolher data específica de entrega?", "Sim, agendamos coleta e entrega conforme sua necessidade, respeitando os prazos mínimos da rota."),
            ("E se chover ou tiver feriado no caminho?", "Chuvas leves não atrasam. Feriados nacionais e estaduais podem postergar 1 dia. Em ambos os casos, comunicamos pelo WhatsApp."),
        ],
    },
    {
        "slug": "transporte-veiculos-leilao-bahia-sao-paulo",
        "titulo_curto": "Transporte de Veículos de Leilão",
        "title": "Transporte de Veículos de Leilão Bahia ↔ São Paulo | Como Retirar | Transportes75",
        "desc": "Como receber seu carro arrematado em leilão da Bahia para São Paulo (ou vice-versa). Documentação, prazo, processo de retirada e entrega.",
        "h1": "Transporte de <em>Veículos de Leilão</em> Bahia ↔ São Paulo",
        "data": "02 ABR, 2026",
        "lead": "Arrematou um carro em leilão na Bahia e mora em São Paulo (ou vice-versa)? Veja como funciona o transporte de veículo de leilão pela Transportes75 — documentação, processo e prazos.",
        "resposta_rapida": "A Transportes75 retira veículos arrematados em leilões de seguradoras, bancos e DETRAN na Bahia e entrega em São Paulo (e vice-versa). Cuidamos da documentação de retirada e do transporte via cegonha pela BR-116 em 3 a 4 dias úteis.",
        "keywords": "transporte carro leilão bahia são paulo, retirar veículo leilão, cegonha leilão BA SP, carro arrematado leilão transporte",
        "body": """<h2 id="por-que">Por Que Comprar em Leilão e Transportar?</h2>
<p>Leilões de <strong>seguradoras, bancos e DETRAN</strong> oferecem veículos com desconto significativo em comparação ao mercado tradicional. Muitas vezes, os melhores lotes estão em pátios distantes do comprador — comprar na Bahia e ter o veículo em São Paulo (ou o contrário) é prática comum.</p>
<p>O <strong>transporte via cegonha</strong> é a forma mais econômica e segura de receber esse veículo. Dirigir o carro recém-arrematado por 2.000 km significa risco, combustível, desgaste e tempo. A cegonha resolve tudo em 3-4 dias.</p>

<h2 id="processo">Processo de Retirada e Transporte</h2>
<p>A <strong>Transportes75</strong> cuida de todo o processo para você. Etapas:</p>
<ol>
  <li><strong>Apresentação dos documentos:</strong> você envia comprovante de arrematação, RG/CNH e nota fiscal de leilão pelo WhatsApp.</li>
  <li><strong>Cotação:</strong> com base no pátio de origem e endereço de destino, geramos cotação.</li>
  <li><strong>Procuração (se necessário):</strong> você nos autoriza a retirar o veículo no pátio. Em muitos leilões, é exigida procuração específica.</li>
  <li><strong>Retirada no pátio:</strong> nossa equipe vai ao pátio do leiloeiro, apresenta documentação e retira o veículo.</li>
  <li><strong>Carregamento na cegonha:</strong> inspeção visual e fotográfica antes do embarque.</li>
  <li><strong>Transporte pela BR-116:</strong> rastreamento em tempo real.</li>
  <li><strong>Entrega no destino:</strong> conforme combinado (sua casa, oficina, revenda).</li>
</ol>

<h2 id="documentos">Documentação Necessária</h2>
<ul>
  <li>Comprovante de arrematação do leilão (com seu nome e dados do veículo)</li>
  <li>Documento de identidade ou CNH</li>
  <li>Nota fiscal de venda emitida pelo leiloeiro</li>
  <li>Para PJ: contrato social</li>
  <li>Procuração com firma reconhecida (alguns leilões exigem) — orientamos como fazer</li>
</ul>

<h2 id="leiloes">Leilões Atendidos</h2>
<p>Trabalhamos com retiradas em:</p>
<ul>
  <li><strong>Leilões de seguradoras</strong> (Bradesco, SulAmérica, Porto Seguro, Mapfre, etc.)</li>
  <li><strong>Leilões judiciais</strong> (Tribunais Estaduais, Vara Cível)</li>
  <li><strong>Leilões do DETRAN</strong> (veículos apreendidos)</li>
  <li><strong>Leilões de bancos</strong> (alienações fiduciárias)</li>
  <li><strong>Leilões corporativos</strong> (frotas de empresas)</li>
</ul>

<h2 id="veiculos-sinistrados">E se o Veículo Está Sinistrado?</h2>
<p>Muitos lotes de leilão são <strong>veículos sinistrados</strong> que não andam. A cegonha resolve esse problema também — carregamos veículos travados, sem combustível ou com avarias, desde que tenham rodas funcionando.</p>
<p>Para casos mais graves (carro batido, sem rodas, totalmente destruído), pode ser necessário guincho até o ponto de carregamento — orientamos caso a caso.</p>

<h2 id="prazo">Prazo Total: Da Arrematação à Entrega</h2>
<ul>
  <li><strong>Análise e documentação:</strong> 1-2 dias úteis</li>
  <li><strong>Agendamento da retirada:</strong> 2-3 dias úteis</li>
  <li><strong>Transporte BA ↔ SP:</strong> 3-4 dias úteis</li>
  <li><strong>Total estimado:</strong> 7 a 10 dias úteis</li>
</ul>
""",
        "faqs": [
            ("Vocês retiram carro de qualquer leilão?", "Sim, atendemos leilões de seguradoras, bancos, DETRAN e judiciais, tanto na Bahia quanto em São Paulo. Basta enviar o comprovante de arrematação."),
            ("Preciso ir ao pátio do leilão?", "Não. Com a documentação correta e procuração quando exigida, nossa equipe vai ao pátio em seu nome. Você só precisa receber o veículo no destino."),
            ("E se o carro arrematado está batido?", "Transportamos veículos sinistrados que tenham rodas funcionando. Para casos extremos (carro destruído), avaliamos com guincho complementar."),
            ("Qual o custo de retirar e transportar de leilão BA ↔ SP?", "O valor depende do pátio de origem, modelo do veículo e endereço de destino. Cotação gratuita pelo WhatsApp (75) 99285-2199."),
            ("Em quantos dias chega meu carro de leilão?", "De 7 a 10 dias úteis no total — incluindo análise de documentos, retirada no pátio e transporte pela BR-116."),
        ],
    },
    {
        "slug": "br-116-rio-bahia-corredor-cegonhas",
        "titulo_curto": "BR-116: Corredor de Cegonhas",
        "title": "BR-116 (Rio-Bahia): O Principal Corredor de Cegonhas BA ↔ SP | Transportes75",
        "desc": "Entenda a importância da BR-116 (Rio-Bahia) para o transporte de veículos entre Bahia e São Paulo. História, paradas estratégicas e desafios da rota.",
        "h1": "BR-116 (Rio-Bahia): O Principal <em>Corredor de Cegonhas</em> BA ↔ SP",
        "data": "15 MAR, 2026",
        "lead": "A BR-116 (Rio-Bahia) é a espinha dorsal do transporte rodoviário entre o Nordeste e o Sudeste. Conheça o trajeto, paradas estratégicas e por que essa rodovia é fundamental para o transporte de veículos via cegonha.",
        "resposta_rapida": "A BR-116 (Rio-Bahia) é a principal rodovia federal que conecta a Bahia a São Paulo, com aproximadamente 2.000 km entre Salvador e São Paulo capital. É o principal corredor de cegonhas do país, usado pela Transportes75 e pelo setor automotivo para mover veículos entre o Nordeste e o Sudeste.",
        "keywords": "br-116 rio-bahia, cegonha br-116, transporte veículos br-116, rodovia bahia são paulo, corredor rodoviário ba sp",
        "body": """<h2 id="historia">A Importância Histórica da BR-116</h2>
<p>A <strong>BR-116</strong>, popularmente chamada de <strong>Rio-Bahia</strong>, é uma das rodovias federais mais importantes do Brasil. Com mais de 4.500 km no total (do Rio Grande do Sul ao Ceará), o trecho entre Salvador e São Paulo é fundamental para a economia brasileira.</p>
<p>Construída em fases ao longo do século XX, a BR-116 conectou regiões antes isoladas — especialmente o interior da Bahia, Minas Gerais e Rio de Janeiro. É hoje o principal corredor logístico do país para transporte rodoviário de cargas, incluindo veículos.</p>

<h2 id="trajeto">O Trajeto Salvador ↔ São Paulo pela BR-116</h2>
<p>Para uma cegonha saindo de <strong>Salvador rumo a São Paulo</strong>, o trajeto típico passa por:</p>
<ul>
  <li><strong>Salvador → Feira de Santana</strong> (~110 km): saída via BR-324, entrada na BR-116</li>
  <li><strong>Feira de Santana → Vitória da Conquista</strong> (~510 km): trecho baiano da BR-116, com serras e vegetação característica</li>
  <li><strong>Vitória da Conquista → Montes Claros</strong> (~280 km): entrada em Minas Gerais</li>
  <li><strong>Montes Claros → Governador Valadares</strong> (~300 km): vale do Rio Doce</li>
  <li><strong>Governador Valadares → Juiz de Fora</strong> (~440 km): região central de MG</li>
  <li><strong>Juiz de Fora → São Paulo</strong> (~410 km): via Rio de Janeiro ou via Belo Horizonte/Campinas</li>
</ul>

<h2 id="por-que-cegonha">Por Que a BR-116 é o Caminho das Cegonhas?</h2>
<p>A BR-116 concentra o tráfego de cegonhas por três razões principais:</p>
<ol>
  <li><strong>Conectividade:</strong> é a única rodovia federal contínua entre o Nordeste e o Sudeste, sem necessidade de desvios significativos.</li>
  <li><strong>Infraestrutura:</strong> conta com postos de combustível 24h, oficinas mecânicas e áreas de descanso ao longo de todo o trajeto.</li>
  <li><strong>Pavimentação:</strong> apesar de trechos com obras frequentes, é uma das rodovias melhor pavimentadas do país nos segmentos federais.</li>
</ol>

<h2 id="paradas">Paradas Estratégicas para Cegonhas</h2>
<p>Cegonhas precisam de paradas técnicas regulares. Os pontos mais usados pela Transportes75:</p>
<ul>
  <li><strong>Feira de Santana (BA):</strong> base operacional da Transportes75 — onde fica nossa sede</li>
  <li><strong>Vitória da Conquista (BA):</strong> meio do trecho baiano, com postos amplos</li>
  <li><strong>Montes Claros (MG):</strong> primeira parada após entrar em Minas</li>
  <li><strong>Governador Valadares (MG):</strong> ponto médio em Minas Gerais</li>
  <li><strong>Juiz de Fora (MG):</strong> última grande parada antes de SP</li>
</ul>

<h2 id="desafios">Desafios e Particularidades</h2>

<h3 id="serras">Trechos Serranos</h3>
<p>Há trechos com declividade significativa, especialmente entre Vitória da Conquista e Montes Claros, e entre Juiz de Fora e São Paulo. Cegonhas trafegam mais lentamente nessas áreas, o que afeta o prazo total.</p>

<h3 id="obras">Obras Frequentes</h3>
<p>Por ser uma das rodovias mais movimentadas, há sempre obras de melhoria, duplicação ou manutenção. O motorista experiente conhece os trechos e planeja desvios quando necessário.</p>

<h3 id="seguranca">Segurança</h3>
<p>Algumas regiões da BR-116 exigem atenção especial. A Transportes75 opera com motoristas treinados, rastreamento em tempo real e protocolos de segurança em cada trecho.</p>

<h2 id="futuro">Futuro da BR-116</h2>
<p>Há projetos de duplicação em vários trechos da BR-116 que devem reduzir o prazo de viagem nos próximos anos. Para o transporte de veículos via cegonha, isso significa entregas mais rápidas e custos potencialmente menores.</p>
""",
        "faqs": [
            ("Quantos quilômetros tem a BR-116 entre Salvador e São Paulo?", "Aproximadamente 2.000 km, dependendo do trajeto exato dentro de cada cidade."),
            ("A BR-116 é segura para cegonhas?", "Sim, é a principal rodovia federal usada por todo o setor automotivo. A Transportes75 opera com motoristas experientes, rastreamento em tempo real e protocolos de segurança."),
            ("Tem pedágio na BR-116?", "Há pedágios em vários trechos, especialmente em Minas Gerais e São Paulo. Os valores estão inclusos no custo do transporte."),
            ("Por que não usar outra rodovia?", "A BR-116 é a rota mais direta e melhor estruturada. Alternativas (como BR-101 pelo litoral) são mais longas e com menos infraestrutura para cegonhas."),
            ("Quanto tempo leva pela BR-116 de Salvador a São Paulo?", "Para cegonha, 3 a 4 dias úteis em média, respeitando o descanso obrigatório do motorista pela Lei do Motorista."),
        ],
    },
]

# ============================================================
# RENDER DE UM ARTIGO
# ============================================================
def render_article(art):
    slug = art["slug"]
    canonical = f"{C.URL_BASE}/blog/{slug}"

    faq_items = ",".join([f'{{"@type":"Question","name":{js(q)},"acceptedAnswer":{{"@type":"Answer","text":{js(a)}}}}}' for q,a in art["faqs"]])
    faq_schema = f'<script type="application/ld+json">\n{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_items}]}}\n</script>'

    crumbs = [
        ("Home", C.URL_BASE_SLASH),
        ("Blog", f"{C.URL_BASE}/blog.html"),
        (art["titulo_curto"], canonical),
    ]
    bc_items = ",".join([f'{{"@type":"ListItem","position":{i+1},"name":{js(n)},"item":{js(u)}}}' for i,(n,u) in enumerate(crumbs)])
    bc_schema = f'<script type="application/ld+json">\n{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{bc_items}]}}\n</script>'

    # Converter "02 JUN, 2026" para "2026-06-02"
    meses = {"JAN":"01","FEV":"02","MAR":"03","ABR":"04","MAI":"05","JUN":"06","JUL":"07","AGO":"08","SET":"09","OUT":"10","NOV":"11","DEZ":"12"}
    m = re.match(r"(\d+)\s+(\w+),\s+(\d+)", art["data"])
    if m:
        d, mes, y = m.groups()
        date_iso = f"{y}-{meses[mes.upper()]}-{int(d):02d}"
    else:
        date_iso = "2026-06-03"

    article_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": art["title"],
        "description": art["desc"],
        "image": f"{C.URL_BASE}/img/hero/hero-transporte-veiculos-bahia-sao-paulo.webp",
        "datePublished": date_iso,
        "dateModified": date_iso,
        "author": {
            "@type": "Person",
            "name": C.AUTOR_NOME,
            "description": "Especialista com 40 anos no setor de transporte de pessoas e cargas",
            "url": f"{C.URL_BASE}/sobre-nos.html"
        },
        "publisher": {
            "@type": "Organization",
            "name": C.SITE_NOME,
            "logo": {"@type":"ImageObject","url":f"{C.URL_BASE}/img/logo/logo-transportes75-256.png"}
        },
        "mainEntityOfPage": canonical,
    }, ensure_ascii=False)

    faq_html = "".join([f'<div class="faq-item"><div class="faq-q">{q}</div><p class="faq-a">{a}</p></div>\n' for q,a in art["faqs"]])

    return f'''<!DOCTYPE html>
<html class="dark" lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{art["title"]}</title>
<meta name="description" content="{art["desc"]}"/>
<meta name="keywords" content="{art["keywords"]}"/>
<link rel="canonical" href="{canonical}"/>
<meta name="robots" content="index, follow"/>
<meta property="og:title" content="{art["title"]}"/>
<meta property="og:description" content="{art["desc"]}"/>
<meta property="og:type" content="article"/>
<meta property="og:url" content="{canonical}"/>
<meta property="og:locale" content="pt_BR"/>
<meta property="og:image" content="{C.URL_BASE}/img/hero/hero-transporte-veiculos-bahia-sao-paulo.webp"/>
<meta property="article:published_time" content="{date_iso}"/>
<meta property="article:author" content="{C.AUTOR_NOME}"/>
<link rel="icon" type="image/png" href="/img/logo/favicon.png"/>
<link rel="apple-touch-icon" href="/img/logo/apple-touch-icon.png"/>
<link rel="stylesheet" href="/dist/styles.css"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap" onload="this.onload=null;this.rel='stylesheet'"/>
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap"/></noscript>
<script type="application/ld+json">{article_schema}</script>
{faq_schema}
{bc_schema}
<script type="application/ld+json">{speakable_schema()}</script>
<style>{CSS_INLINE}</style>
</head>
<body>
{NAV}

<header class="article-hero" style="margin-top:60px;">
  <div class="article-hero-grid">
    <div>
      <div class="article-meta">
        <span class="meta-tag">Artigo · Sergio Torres</span>
        <span class="meta-date">{art["data"]}</span>
      </div>
      <h1>{art["h1"]}</h1>
      <p class="article-lead">{art["lead"]}</p>
    </div>
    <div class="article-hero-img">
      <img src="/img/equipe/cegonha-transportes75.webp" alt="Cegonha Transportes75 na rota Bahia ↔ São Paulo" loading="lazy" width="888" height="581"/>
    </div>
  </div>
</header>

<div class="article-layout">
  <article class="article-body" itemscope itemtype="https://schema.org/Article">
    <meta itemprop="datePublished" content="{date_iso}"/>
    <meta itemprop="author" content="{C.AUTOR_NOME}"/>

    <div id="resposta-rapida" style="background:{C.COR_FUNDO_2};border-left:4px solid {C.COR_PRIMARIA};padding:1.2rem 1.5rem;margin-bottom:2.5rem;border-radius:0 4px 4px 0;">
      <p style="font-size:0.75rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:{C.COR_PRIMARIA};margin-bottom:0.5rem;">Resumo</p>
      <p style="color:{C.COR_TEXTO};line-height:1.7;margin:0;font-size:0.97rem;">{art["resposta_rapida"]}</p>
    </div>

    {art["body"]}

    <div style="position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden;" aria-hidden="true">
      <h2>Em Resumo</h2>
      <p>{art["resposta_rapida"]}</p>
    </div>

    <h2 id="faq">Perguntas Frequentes</h2>
    {faq_html}

    {AUTHOR_BOX}
  </article>

  <aside class="sidebar">
    <div class="sidebar-box">
      <div class="sidebar-title">Outros artigos</div>
      {"".join([f'<a href="/blog/{a["slug"]}" class="toc-link">{a["titulo_curto"]}</a>' for a in ARTIGOS if a["slug"] != slug])}
    </div>
    <div class="sidebar-cta">
      <p>Precisa transportar veículo BA ↔ SP?</p>
      <a href="{C.WA_URL}" target="_blank">WhatsApp →</a>
    </div>
  </aside>
</div>
{FOOTER}
</body></html>'''


# ============================================================
# RENDER DA LISTAGEM /blog.html
# ============================================================
def render_blog_index():
    canonical = f"{C.URL_BASE}/blog.html"

    cards_html = ""
    for a in ARTIGOS:
        cards_html += f'''<a href="/blog/{a["slug"]}" class="blog-card" style="display:block;background:{C.COR_FUNDO_2};border:1px solid #4b5563;padding:1.8rem;text-decoration:none;color:inherit;transition:border-color 0.2s,transform 0.2s;border-radius:8px;">
  <div style="font-family:'Manrope',sans-serif;font-size:0.7rem;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:{C.COR_PRIMARIA};margin-bottom:0.8rem;">{a["data"]} · Sergio Torres</div>
  <h2 style="font-family:'Manrope',sans-serif;font-size:1.25rem;font-weight:700;color:#fff;margin-bottom:0.8rem;line-height:1.3;">{a["titulo_curto"]}</h2>
  <p style="font-size:0.93rem;color:rgba(229,231,235,0.75);line-height:1.7;margin:0;">{a["desc"]}</p>
</a>
'''

    return f'''<!DOCTYPE html>
<html class="dark" lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Blog — {C.SITE_NOME} | Dicas sobre Transporte de Veículos BA ↔ SP</title>
<meta name="description" content="Blog da Transportes75: 5 artigos completos sobre cegonha, leilão, prazos, custos e BR-116 na rota Bahia ↔ São Paulo. Escritos por Sergio Torres, 40 anos no setor."/>
<meta name="keywords" content="blog transportes75, artigos cegonha, transporte veículos BA SP, sergio torres"/>
<link rel="canonical" href="{canonical}"/>
<meta name="robots" content="index, follow"/>
<meta property="og:title" content="Blog — {C.SITE_NOME}"/>
<meta property="og:description" content="5 artigos sobre transporte de veículos BA ↔ SP por Sergio Torres."/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="{canonical}"/>
<link rel="icon" type="image/png" href="/img/logo/favicon.png"/>
<link rel="apple-touch-icon" href="/img/logo/apple-touch-icon.png"/>
<link rel="stylesheet" href="/dist/styles.css"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap" onload="this.onload=null;this.rel='stylesheet'"/>
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap"/></noscript>
<script type="application/ld+json">{org_schema()}</script>
<style>{CSS_INLINE}
.blog-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.5rem;max-width:1200px;margin:3rem auto;padding:0 6vw;}}
.blog-card:hover{{border-color:{C.COR_PRIMARIA} !important;transform:translateY(-4px);}}
</style>
</head>
<body>
{NAV}

<header class="article-hero" style="margin-top:60px;">
  <div class="article-hero-grid">
    <div>
      <div class="article-meta">
        <span class="meta-tag">Blog Transportes75</span>
        <span class="meta-date">Atualizado 03 JUN, 2026</span>
      </div>
      <h1>Blog <em>Transportes75</em><br>Tudo sobre Cegonha BA ↔ SP</h1>
      <p class="article-lead">Artigos completos sobre transporte de veículos pela BR-116, escritos por <strong>Sergio Torres</strong> com 40 anos de experiência no setor de transporte de pessoas e cargas.</p>
    </div>
    <div class="article-hero-img">
      <img src="/img/equipe/cegonha-transportes75.webp" alt="Cegonha Transportes75" loading="lazy" width="888" height="581"/>
    </div>
  </div>
</header>

<div class="blog-grid">
{cards_html}
</div>

{FOOTER}
</body></html>'''


# ============================================================
# EXECUÇÃO
# ============================================================
if __name__ == "__main__":
    # 1. Cria pasta blog/
    blog_dir = OUT / "blog"
    blog_dir.mkdir(exist_ok=True)

    # 2. Gera cada artigo em /blog/{slug}.html
    for art in ARTIGOS:
        html = render_article(art)
        path = blog_dir / f'{art["slug"]}.html'
        path.write_text(html, encoding="utf-8")
        print(f'+ blog/{art["slug"]}.html')

    # 3. Atualiza /blog.html (listagem)
    blog_index = render_blog_index()
    (OUT / "blog.html").write_text(blog_index, encoding="utf-8")
    print('+ blog.html (listagem)')

    print(f'\n{len(ARTIGOS)} artigos + listagem gerados.')
