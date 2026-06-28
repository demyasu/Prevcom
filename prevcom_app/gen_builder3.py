"""Builds programmatic_flashcards.py - part 3: Etica + RLP + Previdencia"""
import os

path = r'D:\Prevcom\prevcom_app\programmatic_flashcards.py'

def write(s):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(s + '\n')

write('''    print(f"  LP programatico: {len(LP)} cards")

    # ================================================================
    # 2. ETICA E INTEGRIDADE
    # ================================================================

    codigo_etica = [
        ("Decreto 1.171/94: campo", "Servidores publicos civis do Executivo Federal."),
        ("Decreto 1.171/94: regra moral", "Dignidade, decoro, zelo, eficacia."),
        ("Decreto 1.171/94: bem publico", "Vedado usar bem publico para fins privados."),
        ("Decreto 1.171/94: hierarquia", "Respeito sem temor reverencial."),
        ("Decreto 1.171/94: ilegalidade", "Representar contra ilegalidade ou omissao."),
        ("Decreto 1.171/94: omissao", "Comunicar superior sobre ato ilegal imediatamente."),
        ("Decreto 1.171/94: pressao", "Resistir a pressao para obter vantagens indevidas."),
        ("Decreto 1.171/94: participacao", "Proibido participar de atos que beneficiem terceiros."),
        ("Decreto 1.171/94: sindicancia", "Colaborar com processos administrativos."),
        ("Decreto 1.171/94: publicidade", "Divulgar informacoes de interesse publico."),
        ("Decreto 1.171/94: colegas", "Cortesia e respeito com colegas e publico."),
        ("Decreto 1.171/94: nome da adm", "Nao usar nome da adm para criticar."),
        ("Decreto 1.171/94: beneficios", "Nao receber vantagens ou presentes indevidos."),
        ("Decreto 1.171/94: comercio", "Proibido comercio entre colegas durante servico."),
        ("Decreto 1.171/94: emprego privado", "Proibido aceitar emprego de entidade privada."),
        ("Decreto 1.171/94: comentarios", "Vedado comentarios depreciativos."),
        ("Decreto 1.171/94: cessao", "Vedado cessao a entidade privada."),
        ("Decreto 1.171/94: censura", "Pena: censura etica pela Comissao."),
        ("Decreto 1.171/94: comissao", "Apura condutas, aplica censura, orienta."),
        ("Decreto 1.171/94: termo de compromisso", "Assinado na posse."),
        ("Decreto 1.171/94: contraditorio", "Ampla defesa nos processos eticos."),
    ]
    ET.extend(codigo_etica)

    lgpd_detalhes = [
        ("LGPD: dado pessoal", "Relacionado a pessoa natural identificada/identificavel."),
        ("LGPD: dado anonimizado", "Nao permite identificacao. Nao e dado pessoal."),
        ("LGPD: dado pseudonimizado", "Perda de associacao direta, mas reversivel."),
        ("LGPD: agentes de tratamento", "Controlador (decide) e Operador (executa)."),
        ("LGPD: controlador", "Toma decisoes sobre tratamento de dados."),
        ("LGPD: operador", "Realiza tratamento em nome do controlador."),
        ("LGPD: encarregado (DPO)", "Canal entre controlador, titulares e ANPD."),
        ("LGPD: bases legais", "Consentimento, obrigacao legal, adm publica, pesquisa, contrato, direito, vida, saude, interesse legitimo, credito."),
        ("LGPD: consentimento", "Livre, informado e inequivoco. Revogavel a qualquer momento."),
        ("LGPD: dados sensiveis", "Racial, religiao, politica, sindical, saude, sexual, genetico, biometrico."),
        ("LGPD: direitos do titular", "Confirmacao, acesso, correcao, anonimizacao, bloqueio, eliminacao, portabilidade."),
        ("LGPD: portabilidade", "Transferir dados a outro fornecedor."),
        ("LGPD: eliminacao", "Solicitar eliminacao de dados com consentimento."),
        ("LGPD: revisao automatizada", "Solicitar revisao de decisoes automatizadas."),
        ("LGPD: seguranca", "Medidas tecnicas e adm contra acesso nao autorizado."),
        ("LGPD: incidente", "Comunicar ANPD e titular em caso de risco/dano."),
        ("LGPD: RIPD", "Relatorio de Impacto. Riscos e mitigacoes."),
        ("LGPD: transferencia internacional", "Paises com nivel adequado ou garantias contratuais."),
        ("LGPD: ANPD", "Regulamenta, fiscaliza, sanciona, orienta."),
        ("LGPD: sancoes", "Advertencia, multa (ate 2% faturamento/R$50M), bloqueio, suspensao."),
        ("LGPD: prescricao", "5 anos para pretensao punitiva da ANPD."),
    ]
    ET.extend(lgpd_detalhes)

    esg_detalhes = [
        ("ESG: E - mudancas climaticas", "Reducao GEE, net-zero, precificacao carbono."),
        ("ESG: E - recursos hidricos", "Gestao agua, reducao consumo, efluentes."),
        ("ESG: E - biodiversidade", "Protecao ecossistemas, compensacao, TNFD."),
        ("ESG: E - economia circular", "Reciclagem, reuso, residuos, logistica reversa."),
        ("ESG: S - direitos humanos", "Respeito na cadeia de valor."),
        ("ESG: S - diversidade", "Inclusao genero, raca, PcD, LGBTQIA+."),
        ("ESG: S - saude e seguranca", "Saude ocupacional, seguranca trabalho."),
        ("ESG: S - comunidades", "Dialogo, impacto social, investimento social."),
        ("ESG: S - trabalho decente", "Salario justo, proibicao trabalho escravo/infantil."),
        ("ESG: G - transparencia", "Relatorios integrados, comunicacao."),
        ("ESG: G - conselho", "Diversidade, independencia, separacao CEO/Chairman."),
        ("ESG: G - remuneracao", "Vinculada a metas ESG de longo prazo."),
        ("ESG: G - etica/compliance", "Codigo, canal denuncia, integridade."),
        ("ESG: G - riscos", "Riscos ESG integrados a gestao corporativa."),
        ("ESG: relato integrado", "Financas + ESG em unica narrativa."),
        ("ESG: GRI Standards", "Global Reporting Initiative. Padrao de sustentabilidade."),
        ("ESG: SASB", "Sustainability Accounting Standards Board. Por setor."),
        ("ESG: TCFD", "Task Force Climate. Riscos e oportunidades climaticas."),
        ("ESG: PRI", "Principles Responsible Investment. Integracao ESG."),
        ("ESG: green bonds", "Titulos para projetos ambientais."),
        ("ESG: social bonds", "Titulos para projetos sociais."),
        ("ESG: sustainability-linked bonds", "KPIs de sustentabilidade. Penalidades se nao cumprir."),
        ("ESG: rating", "Sustainalytics, MSCI, ISS, S&P."),
        ("ESG: materialidade", "Topicos ESG com impacto financeiro."),
        ("ESG: double materiality", "Financeira + impacto da empresa no mundo."),
        ("ESG: greenwashing", "Falsa propaganda ambiental."),
    ]
    ET.extend(esg_detalhes)
''')
print("Part 3a written (Etica inicio)")
