"""Final stretch batch: ~230 more cards"""
import os

path = r'D:\Prevcom\prevcom_app\programmatic_flashcards.py'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

marker = '    print(f"  Previdencia final2: {len(prev_final2)} cards")'

extra = '''

    # --- Final stretch (~230 cards) ---
    lp_final3 = [
        ("Gramatica: vocabulo", "Palavra."),
        ("Gramatica: fonema", "Menor unidade sonora."),
        ("Gramatica: letra", "Representacao grafia fonema."),
        ("Gramatica: encontro vocalico", "Ditongo, tritongo, hiato."),
        ("Gramatica: ditongo", "2 vogais mesma silaba. Ex: pai, peixe."),
        ("Gramatica: tritongo", "3 vogais mesma silaba. Ex: Paraguai, quais."),
        ("Gramatica: hiato", "2 vogais silabas diferentes. Ex: sa-ude, pa-is."),
        ("Gramatica: digrafo", "2 letras 1 fonema. Ex: ch, nh, lh, qu, gu."),
        ("Gramatica: silaba tonica", "Mais forte. Oxitona, paroxitona, proparoxitona."),
        ("Gramatica: silaba atona", "Mais fraca."),
        ("Gramatica: 's' sonoro vs surdo", "Sonoro: /z/ em casa. Surdo: /s/ em sapo."),
        ("Gramatica: 'x' sons", "/sh/ xarope, /ks/ taxis, /z/ exame, /s/ maximo."),
        ("Gramatica: acento tonico vs grafico", "Tonic: intensidade. Graf: marcacao."),
        ("Gramatica: acento agudo", "Vogal aberta: a, e, o, i, u."),
        ("Gramatica: acento circunflexo", "Vogal fechada: e, o."),
        ("Gramatica: acento til", "Nasalizacao: a, o."),
        ("Gramatica: trema abolido", "Acordo 1990: nao se usa mais."),
        ("Gramatica: maiuscula nomes proprios", "Obrigatoria."),
        ("Gramatica: maiuscula inicio periodo", "Obrigatoria."),
        ("Gramatica: minuscula dias semana", "Apos acordo: segunda-feira."),
        ("Gramatica: minuscula meses", "Apos acordo: janeiro."),
        ("Gramatica: plural 'ao' > 'aes/aoes/oes'", "Caes, paes, maos, leoes."),
        ("Gramatica: plural 'm' > 'ns'", "Homem > homens."),
        ("Gramatica: plural 'r/z' + 'es'", "Mar > mares, raiz > raizes."),
        ("Gramatica: plural 'il' > 'is/eis'", "Funil > funis, facil > faceis."),
        ("Gramatica: aumentativo sintetico", "Sufixo -ao, -arrao. Ex: cadeirao."),
        ("Gramatica: diminutivo sintetico", "Sufixo -inho, -zinho. Ex: caderninho."),
    ]
    LP.extend(lp_final3)
    print(f"  LP final3: {len(lp_final3)} cards")

    etica_final3 = [
        ("ESG: emissao carbono per capita", "Metrica pais."),
        ("ESG: pegada ecologica", "Impacto ambiental."),
        ("ESG: agua virtual", "Agua incorporada producao."),
        ("ESG: poluicao plastico", "Microplastico oceanos."),
        ("ESG: desmatamento ilegal", "Cadeia valor."),
        ("ESG: recuperacao area degradada", "Restauracao."),
        ("ESG: energia renovavel", "Solar, eolica, hidreletrica."),
        ("ESG: energia solar fotovoltaica", "Conversao luz."),
        ("ESG: energia eolica", "Vento."),
        ("ESG: biomassa", "Materia organica."),
        ("ESG: hidrogenio verde", "Eletrolise renovavel."),
        ("ESG: biocombustivel", "Etanol, biodiesel."),
        ("ESG: mobilidade eletrica", "Veiculos eletricos."),
        ("ESG: construcao verde", "LEED, Procel."),
        ("ESG: certificacao ambiental", "ISO 14001."),
        ("ESG: analise ciclo vida", "Cradle to grave."),
        ("ESG: economia azul", "Oceanos sustentaveis."),
        ("ESG: cidade inteligente", "Tecnologia + sustentabilidade."),
        ("ESG: infraestrutura verde", "Natureza solucoes."),
        ("ESG: telhado verde", "Cobertura vegetal."),
        ("ESG: arborizacao urbana", "Clima, qualidade ar."),
        ("ESG: educacao ambiental", "Conscientizacao."),
        ("ESG: consumo consciente", "Reduzir, reutilizar, reciclar."),
        ("ESG: economia compartilhada", "Compartilhar bens."),
        ("ESG: logistica reversa", "Retorno embalagens."),
        ("ESG: residuo solido PNRS", "Lei 12.305/2010."),
        ("ESG: residuo classe I", "Perigoso."),
        ("ESG: residuo classe II", "Nao perigoso."),
        ("ESG: compostagem", "Residuo organico."),
        ("ESG: aterro sanitario", "Disposicao final."),
        ("ESG: lixao problema", "Contaminacao solo."),
        ("ESG: cooperativa catadores", "Inclusao social."),
        ("ESG: carbono azul", "Manguezais."),
        ("ESG: reflorestamento nativo", "Mata Atlantica, Amazonia."),
        ("ESG: pagamento servicos ambientais", "PSA."),
        ("ESG: credito carbono mercado", "Voluntario, regulado."),
        ("ESG: MDL", "Mecanismo desenvolvimento limpo."),
        ("ESG: REDD+", "Reducao desmatamento."),
        ("ESG: net zero escopos", "1, 2, 3."),
        ("ESG: ciencia clima IPCC", "Painel cientifico ONU."),
        ("ESG: aquecimento global causa", "GEE."),
        ("ESG: efeito estufa GEE", "CO2, CH4, N2O, SF6."),
        ("ESG: limite 1.5C", "Acordo Paris."),
    ]
    ET.extend(etica_final3)
    print(f"  Etica final3: {len(etica_final3)} cards")

    rlp_final3 = [
        ("Matematica: mmc metodo", "Fatores primos."),
        ("Matematica: mdc metodo", "Fatores primos comuns."),
        ("Matematica: mmc x mdc", "mmc(a,b)*mdc(a,b)=a*b."),
        ("Matematica: numero primo definicao", "Divisivel por 1 e si mesmo."),
        ("Matematica: teorema fundamental aritmetica", "Todo inteiro fatora primos."),
        ("Matematica: fracoes equivalentes", "Numerador/denominador mesma razao."),
        ("Matematica: fracao irredutivel", "Maximo divisor comum."),
        ("Matematica: numero misto", "Inteiro + fracao. Ex: 1 e 1/2."),
        ("Matematica: fracao decimal", "Denominador 10, 100, 1000."),
        ("Matematica: porcentagem fracao", "% = /100."),
        ("Matematica: razao", "Comparacao dois numeros."),
        ("Matematica: proporcao", "Igualdade razoes."),
        ("Matematica: grandezas diretas", "Razao constante."),
        ("Matematica: grandezas inversas", "Produto constante."),
        ("Matematica: regra tres simples direta", "Multiplica cruzado."),
        ("Matematica: regra tres simples inversa", "Inverte e multiplica."),
        ("Matematica: regra tres composta", "Multiplas grandezas."),
        ("Matematica: funcao cresc decresc", "Derivada positiva/negativa."),
        ("Matematica: funcao concavidade", "Derivada segunda."),
        ("Matematica: ponto inflexao", "Muda concavidade."),
        ("Matematica: assintota vertical", "Denominador zero."),
        ("Matematica: assintota horizontal", "x tende infinito."),
        ("Matematica: continuidade", "Limite = valor funcao."),
        ("Matematica: diferenciabilidade", "Derivada existe."),
        ("Matematica: regra L'Hospital", "0/0 ou infinito/infinito."),
        ("Matematica: otimizacao", "Maximo/minimo funcao."),
        ("Matematica: serie convergente", "Soma limite finito."),
        ("Matematica: serie divergente", "Soma infinita."),
        ("Matematica: serie geometrica", "Soma = a/(1-r)."),
        ("Matematica: serie harmonica", "Divergente."),
    ]
    RL.extend(rlp_final3)
    print(f"  RLP final3: {len(rlp_final3)} cards")

    prev_final3 = [
        ("PREVCOM: conselho deliberativo reunioes", "Periodicidade mensal."),
        ("PREVCOM: conselho fiscal reunioes", "Periodicidade trimestral."),
        ("PREVCOM: diretoria reunioes", "Periodicidade semanal."),
        ("PREVCOM: voto qualidade presidente", "Desempate."),
        ("PREVCOM: atas reunioes", "Registro formal."),
        ("PREVCOM: arquivo documentos", "Prazos legais."),
        ("PREVCOM: politica arquivamento", "Gestao documental."),
        ("PREVCOM: processo digital", "Tramitacao eletronica."),
        ("PREVCOM: assinatura digital", "ICP-Brasil."),
        ("PREVCOM: certificado digital", "A3 ou A1."),
        ("PREVCOM: gov.br", "Acesso servicos."),
        ("PREVCOM: portal transparencia", "Dados abertos."),
        ("PREVCOM: LAI cumprimento", "Lei Acesso Informacao."),
        ("PREVCOM: dados abertos formato", "Legivel maquina."),
        ("PREVCOM: SIC", "Servico informacao cidadao."),
        ("PREVCOM: ouvidoria prazos", "Manifestacao."),
        ("PREVCOM: carta servicos", "Padrao atendimento."),
        ("PREVCOM: controle social", "Auditoria civica."),
        ("PREVCOM: programa integridade", "PREVCOM."),
        ("PREVCOM: gestao riscos", "Metodologia."),
        ("PREVCOM: controles internos COSO", "Ambiente, avaliacao, controle."),
        ("PREVCOM: codigo etica fornecedores", "Cadeia valor."),
        ("PREVCOM: due diligence parceiros", "Avaliacao previa."),
        ("PREVCOM: clausula anticorrupcao", "Contratos."),
        ("PREVCOM: treinamento etica", "Periodico."),
        ("PREVCOM: plano acao corretiva", "Nao conformidade."),
        ("PREVCOM: indicadores desempenho", "Metas."),
        ("PREVCOM: BSC", "Balanced Scorecard."),
        ("PREVCOM: planejamento estrategico", "PDCA."),
        ("PREVCOM: prestacao contas TCESP", "Tribunal Contas."),
        ("PREVCOM: relatorio gestao", "Resultados."),
        ("PREVCOM: responsabilidade fiscal LRF", "Meta fiscal."),
        ("PREVCOM: limite despesa pessoal", "LRF."),
        ("PREVCOM: gestao atuarial", "Solvencia LP."),
    ]
    PR.extend(prev_final3)
    print(f"  Previdencia final3: {len(prev_final3)} cards")
'''

idx = content.rfind(marker)
if idx != -1:
    new_content = content[:idx + len(marker)] + extra + content[idx + len(marker):]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Final stretch inserted. File size: {len(new_content)} chars")
else:
    print('ERROR: marker not found!')
