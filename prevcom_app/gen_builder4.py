"""Builds programmatic_flashcards.py - part 4: Etica continuacao + RLP + Previdencia"""
import os

path = r'D:\Prevcom\prevcom_app\programmatic_flashcards.py'

def write(s):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(s + '\n')

write('''    anticorrupcao = [
        ("Lei 12.846/2013: suborno", "Prometer/offerecer/dar vantagem a agente publico."),
        ("Lei 12.846/2013: financiamento", "Financiar/custear atos ilicitos."),
        ("Lei 12.846/2013: fraude", "Fraudar licitacao ou contrato."),
        ("Lei 12.846/2013: obstrucao", "Dificultar investigacao/fiscalizacao."),
        ("Lei 12.846/2013: resp. objetiva", "Empresa responde sem dolo ou culpa."),
        ("Lei 12.846/2013: resp. solidaria", "Diretores respondem solidariamente."),
        ("Lei 12.846/2013: multa", "0,1% a 30% do faturamento bruto."),
        ("Lei 12.846/2013: multa sem faturamento", "R$6.000 a R$60.000.000."),
        ("Lei 12.846/2013: publicacao", "Publicacao extraordinaria da condenacao."),
        ("Lei 12.846/2013: proibicao", "Proibido incentivos fiscais por 1-5 anos."),
        ("Lei 12.846/2013: dissolucao", "Dissolucao compulsoria na reincidencia."),
        ("Lei 12.846/2013: leniencia", "Colaboracao: reducao multa em ate 2/3."),
        ("Lei 12.846/2013: prescricao", "5 anos da ciencia da infracao."),
        ("Lei 12.846/2013: compliance atenuante", "Programa de integridade reduz penalidades."),
    ]
    ET.extend(anticorrupcao)

    improbidade = [
        ("Lei 8.429/92: art.9 - enriquecimento", "Dolo. Penas: perda funcao, suspensao direitos 8-14 anos."),
        ("Lei 8.429/92: art.9 exemplos", "Receber vantagem, usar bens publicos, usar cargo."),
        ("Lei 8.429/92: art.10 - lesao erario", "Dolo. Perda funcao, suspensao 5-10 anos."),
        ("Lei 8.429/92: art.10 exemplos", "Liberar verba sem fiscalizacao, contrato irregular."),
        ("Lei 8.429/92: art.11 - principios", "Dolo. Perda funcao, suspensao 3-5 anos."),
        ("Lei 8.429/92: art.11 exemplos", "Ato fim proibido, omitir publicidade."),
        ("Lei 8.429/92: Lei 14.230/2021", "Exige dolo. Culpa excluida. Prescricao 8 anos."),
        ("Lei 8.429/92: sujeito ativo", "Agente publico: servidor, politico."),
        ("Lei 8.429/92: sujeito passivo", "Adm publica direta, indireta."),
        ("Lei 8.429/92: terceiro", "Terceiro beneficiado tambem responde."),
        ("Lei 8.429/92: acao", "MP ou pessoa juridica interessada."),
        ("Lei 8.429/92: cautelares", "Indisponibilidade bens, afastamento."),
        ("Lei 8.429/92: prescricao", "8 anos apos o fato."),
    ]
    ET.extend(improbidade)

    compliance_detalhes = [
        ("Compliance: definicao", "Conformidade com leis, normas, politicas."),
        ("Compliance: programa integridade", "Prevenir, detectar, corrigir desvios."),
        ("Compliance: pilares", "Alta direcao, codigo, treinamento, canal, investigacao, consequencias, monitoramento."),
        ("Compliance: risco", "Sancoes legais, perdas, dano reputacional."),
        ("Compliance: due diligence", "Verificacao integridade de parceiros."),
        ("Compliance: KYC/KYE/KYP", "Conhecer: cliente, empregado, parceiro."),
        ("Compliance: treinamento", "Periodicos sobre codigo de conduta."),
        ("Compliance: comunicacao", "Campanhas, cartilhas, intranet."),
        ("Compliance: investigacao", "Coleta provas, entrevistas, relatorio."),
        ("Compliance: consequencias", "Advertencia, suspensao, demissao."),
        ("Compliance: monitoramento", "Indicadores: denuncias, investigacoes, sancoes."),
        ("Compliance: auditoria", "Avalia efetividade do programa."),
        ("Compliance: compliance officer", "Profissional responsavel pelo programa."),
        ("Compliance: clausulas contratuais", "Anticorrupcao, auditoria, rescisao."),
        ("Compliance: controle interno", "Politicas, procedimentos para riscos."),
        ("Compliance: segregacao", "Separar funcoes para evitar conflitos."),
        ("Compliance: gestao conflitos", "Declaracao anual de conflito."),
        ("Compliance: ISO 37301", "Sistema de gestao de compliance."),
        ("Compliance: ISO 37001", "Sistema de gestao antissuborno."),
    ]
    ET.extend(compliance_detalhes)

    governanca_detalhes = [
        ("Governanca: principios", "Transparencia, equidade, prestacao contas, responsabilidade."),
        ("Governanca: Conselho Adm", "Orgao colegiado estrategico."),
        ("Governanca: conselheiro independente", "Sem vinculo com administracao."),
        ("Governanca: comites", "Auditoria, Remuneracao, Nomeacao, Sustentabilidade, Riscos."),
        ("Governanca: diretoria", "Gestao operacional. CEO e diretores."),
        ("Governanca: conselho fiscal", "Controle independente."),
        ("Governanca: auditoria independente", "Audita demonstracoes financeiras."),
        ("Governanca: auditoria interna", "Avalia controles, riscos."),
        ("Governanca: codigo conduta", "Valores e normas de conduta."),
        ("Governanca: partes relacionadas", "Transacoes com controladores."),
        ("Governanca: gestao riscos", "Identificar, avaliar, tratar, monitorar."),
        ("Governanca: relatorio integrado", "Financas + ESG."),
        ("Governanca: KPIs", "Indicadores financeiros e nao-financeiros."),
        ("Governanca: remuneracao", "Alinhada a valor de longo prazo."),
        ("Governanca: sucessao", "Plano sucessorio CEO/diretores."),
        ("Governanca: avaliacao conselho", "Autoavaliacao anual."),
    ]
    ET.extend(governanca_detalhes)

    ods_detalhes = [
        ("ODS 1: Erradicacao Pobreza", "Acabar com pobreza em todas as formas."),
        ("ODS 2: Fome Zero", "Acabar com fome, seguranca alimentar."),
        ("ODS 3: Saude Bem-Estar", "Vida saudavel e bem-estar para todos."),
        ("ODS 4: Educacao Qualidade", "Educacao inclusiva, equitativa, qualidade."),
        ("ODS 5: Igualdade Genero", "Igualdade genero, empoderar mulheres."),
        ("ODS 6: Agua Saneamento", "Disponibilidade e gestao sustentavel agua."),
        ("ODS 7: Energia Limpa", "Energia confiavel, sustentavel, moderna."),
        ("ODS 8: Trabalho Decente", "Crescimento economico e trabalho decente."),
        ("ODS 9: Industria Inovacao", "Infraestrutura resiliente, industrializacao."),
        ("ODS 10: Reducao Desigualdades", "Reduzir desigualdades dentro e entre paises."),
        ("ODS 11: Cidades Sustentaveis", "Cidades inclusivas, seguras, resilientes."),
        ("ODS 12: Consumo Responsavel", "Padroes sustentaveis consumo/producao."),
        ("ODS 13: Acao Climatica", "Combater mudancas climaticas."),
        ("ODS 14: Vida na Agua", "Conservar oceanos e recursos marinhos."),
        ("ODS 15: Vida Terrestre", "Proteger ecossistemas terrestres."),
        ("ODS 16: Paz Justica", "Sociedades pacificas, acesso justica."),
        ("ODS 17: Parcerias", "Fortalecer meios implementacao, parcerias."),
    ]
    ET.extend(ods_detalhes)

    lideranca_etica = [
        ("Tone at the top", "Alta direcao comprometida com etica."),
        ("Tone from the middle", "Lideranca media reforca etica."),
        ("Cultura etica: medicao", "Pesquisas clima, indicadores integridade."),
        ("Etica contratacoes", "Entrevista comportamental, verificacao antecedentes."),
        ("Etica avaliacao", "Metas integridade na avaliacao anual."),
        ("Etica terceirizacao", "Clausulas integridade com fornecedores."),
        ("Etica M&A", "Due diligence integridade em fusoes."),
        ("IA etica", "Nao discriminacao, transparencia, supervisao humana."),
        ("Whistleblower: protecao", "Lei 13.608/2018: protecao contra retalhacao."),
        ("Canal denuncia: externo", "Operado por independente. Credibilidade."),
        ("Canal denuncia: interno", "Operado pela organizacao. Menor custo."),
        ("Investigacao: fases", "Planejamento, provas, entrevistas, relatorio, recomendacoes."),
        ("LAI: transparencia ativa", "Dever divulgar independente de solicitacao."),
        ("LAI: transparencia passiva", "Fornecer quando solicitado."),
        ("LAI: prazos", "20 dias + 10 prorogacao."),
        ("Classificacao ultrassecreta", "25 anos. Prorogavel uma vez."),
        ("Classificacao secreta", "15 anos."),
        ("Classificacao reservada", "5 anos."),
        ("Principio razoabilidade", "Adequacao meios e fins."),
        ("Principio proporcionalidade", "Equilibrio restricao e objetivo."),
        ("Principio autotutela", "Adm anula proprios atos ilegais."),
        ("Principio motivacao", "Atos devem ser motivados."),
    ]
    ET.extend(lideranca_etica)

    print(f"  Etica programatico: {len(ET)} cards")

    # ================================================================
    # 3. RACIOCINIO LOGICO E ANALITICO
    # ================================================================

    logic_patterns = [
        ("Tabela: ~p (negacao)", "p V -> ~p F. p F -> ~p V."),
        ("Tabela: p ^ q (conjuncao)", "V^V=V, V^F=F, F^V=F, F^F=F."),
        ("Tabela: p v q (inclusiva)", "VvV=V, VvF=V, FvV=V, FvF=F."),
        ("Tabela: p -> q (condicional)", "V->V=V, V->F=F, F->V=V, F->F=V."),
        ("Tabela: p <-> q (bicondicional)", "V<->V=V, V<->F=F, F<->V=F, F<->F=V."),
        ("Tabela: p v q (exclusivo)", "VvV=F, VvF=V, FvV=V, FvF=F."),
        ("Tabela: p ^ ~p", "Sempre F (contradicao)."),
        ("Tabela: p v ~p", "Sempre V (tautologia)."),
    ]
    RL.extend(logic_patterns)
''')

write('''    equivs = [
        ("p->q ≡ ~p v q", "Negar antecedente OU afirmar consequente."),
        ("p->q ≡ ~q->~p", "Contrapositiva: inverte e nega ambas."),
        ("~(p->q) ≡ p ^ ~q", "MANE: MAntem 1a, NEga 2a."),
        ("p<->q ≡ (p->q)^(q->p)", "Duas condicionais."),
        ("p<->q ≡ (p^q)v(~p^~q)", "Ambos V ou ambos F."),
        ("~(p^q) ≡ ~p v ~q", "1a Lei De Morgan."),
        ("~(p v q) ≡ ~p ^ ~q", "2a Lei De Morgan."),
        ("p v p ≡ p / p^p ≡ p", "Idempotencia."),
        ("p^(qvr) ≡ (p^q)v(p^r)", "Distributiva conjuncao."),
        ("pv(q^r) ≡ (pvq)^(pvr)", "Distributiva disjuncao."),
        ("p^(pvq) ≡ p / pv(p^q) ≡ p", "Absorcao."),
        ("~~p ≡ p", "Dupla negacao."),
        ("(p^q)->r ≡ p->(q->r)", "Exportacao."),
        ("p->(q->r) ≡ (p^q)->r", "Importacao."),
    ]
    RL.extend(equivs)

    inferencia = [
        ("Modus Ponens", "p->q, p ⊢ q."),
        ("Modus Tollens", "p->q, ~q ⊢ ~p."),
        ("Silogismo Hipotetico", "p->q, q->r ⊢ p->r."),
        ("Silogismo Disjuntivo", "p v q, ~p ⊢ q."),
        ("Dilema Construtivo", "(p->q)^(r->s), pvr ⊢ qvs."),
        ("Dilema Destrutivo", "(p->q)^(r->s), ~qv~s ⊢ ~pv~r."),
        ("Prova por casos", "p->r, q->r, pvq ⊢ r."),
        ("Reductio ad absurdum", "Assume ~p, deriva contradicao, logo p."),
        ("Simplificacao", "p^q ⊢ p."),
        ("Conjuncao", "p, q ⊢ p^q."),
        ("Adicao", "p ⊢ p v q."),
    ]
    RL.extend(inferencia)

    falacias = [
        ("Falacia: afirmacao consequente", "p->q, q ⊢ p (INVALIDO)."),
        ("Falacia: negacao antecedente", "p->q, ~p ⊢ ~q (INVALIDO)."),
        ("Falacia ad hominem", "Atacar a pessoa, nao o argumento."),
        ("Falacia apelo autoridade", "Autoridade irrelevante."),
        ("Falacia apelo emocao", "Manipular emocao no lugar de razao."),
        ("Falacia apelo ignorancia", "Verdade porque nao provado falso."),
        ("Falacia apelo maioria", "Verdade porque muitos acreditam."),
        ("Falacia causa falsa (post hoc)", "A antes de B, logo A causa B."),
        ("Falacia generalizacao", "Poucos exemplos, conclusao geral."),
        ("Falacia espantalho", "Deturpar argumento para atacar."),
        ("Falacia circulo vicioso", "Premissa ja contem conclusao."),
        ("Falacia falsa dicotomia", "So duas opcoes quando ha mais."),
        ("Falacia ladeira escorregadia", "Acao leva a extremos sem prova."),
        ("Falacia composicao", "Parte -> todo."),
        ("Falacia divisao", "Todo -> parte."),
        ("Falacia do jogador", "Eventos aleatorios passados afetam futuros."),
    ]
    RL.extend(falacias)

    conjuntos = [
        ("Conjunto: definicao", "Colecao bem definida de elementos."),
        ("Pertinencia ∈", "'x ∈ A' = x e elemento de A."),
        ("Subconjunto ⊆", "A ⊆ B = todo elem de A esta em B."),
        ("Uniao (U)", "Elementos em A OU em B."),
        ("Intersecao (∩)", "Elementos em A E em B."),
        ("Diferenca (-)", "Elementos de A que nao estao em B."),
        ("Complementar (c)", "Universo - conjunto."),
        ("Leis De Morgan", "(AUB)^c = A^c∩B^c. (A∩B)^c = A^cUB^c."),
        ("Distributiva conjuntos", "A∩(BUC) = (A∩B)U(A∩C). A∪(B∩C) = (A∪B)∩(A∪C)."),
        ("Cardinalidade n(AUB)", "n(A)+n(B)-n(A∩B)."),
        ("Cardinalidade n(AUBUC)", "n(A)+n(B)+n(C)-n(A∩B)-n(A∩C)-n(B∩C)+n(A∩B∩C)."),
        ("Conjunto partes", "P(A) = todos subconjuntos. n(P(A))=2^n."),
        ("Produto cartesiano", "AxB = {(a,b)}. n(AxB)=n(A)*n(B)."),
    ]
    RL.extend(conjuntos)

    analise_comb = [
        ("Permutacao: Pn = n!", "Ordenar n elementos: 5! = 120."),
        ("Permutacao com repeticoes", "n!/(r1!*...*rk!). Ex: 'banana'."),
        ("Permutacao circular", "Pc(n) = (n-1)!."),
        ("Arranjo: A(n,p) = n!/(n-p)!", "Ordem importa. Ex: senhas."),
        ("Combinacao: C(n,p) = n!/(p!(n-p)!)", "Ordem nao importa. Ex: comissoes."),
        ("Combinacao com repeticoes", "CR(n,p) = C(n+p-1, p)."),
        ("Principio multiplicativo", "Eventos A e B: m*n formas."),
        ("Principio aditivo", "Evento A ou B (disjuntos): m+n."),
    ]
    RL.extend(analise_comb)

    prob = [
        ("Probabilidade: definicao", "P(E) = favoraveis / possiveis. 0 ≤ P ≤ 1."),
        ("Espaco amostral", "Conjunto de todos resultados possiveis."),
        ("Evento", "Subconjunto do espaco amostral."),
        ("Axiomas Kolmogorov", "P(E)>=0, P(U)=1, mut ex: P(UEi)=ΣP(Ei)."),
        ("Complementar", "P(~A)=1-P(A)."),
        ("Uniao", "P(AUB)=P(A)+P(B)-P(A∩B)."),
        ("Condicional", "P(A|B)=P(A∩B)/P(B)."),
        ("Independencia", "P(A∩B)=P(A)*P(B)."),
        ("Mutualmente exclusivos", "P(AUB)=P(A)+P(B)."),
        ("Teorema Bayes", "P(A|B)=P(B|A)*P(A)/P(B)."),
        ("Binomial", "P(X=k)=C(n,k)*p^k*(1-p)^(n-k)."),
        ("Poisson", "P(X=k)=e^(-λ)*λ^k/k!."),
        ("Normal", "Continua, sino. Media μ, desvio σ."),
        ("Regra 68-95-99,7", "68% 1σ, 95% 2σ, 99,7% 3σ."),
        ("Teorema Central Limite", "Soma i.i.d. aproxima normal."),
    ]
    RL.extend(prob)

    sequencias = [
        ("PA: an = a1 + (n-1)*r", "Ex: 2,5,8,... a10 = 29."),
        ("PA: Sn = (a1+an)*n/2", "Ex: 1+...+100 = 5050."),
        ("PG: an = a1*q^(n-1)", "Ex: 2,4,8,... a5 = 32."),
        ("PG: Sn = a1*(q^n-1)/(q-1)", "Ex: 1+2+4+8 = 15."),
        ("PG infinita: S∞ = a1/(1-q)", "|q|<1. Ex: 1+1/2+1/4+... = 2."),
        ("Fibonacci", "0,1,1,2,3,5,8,13,21,34,55,89..."),
        ("Numeros triangulares", "n(n+1)/2: 1,3,6,10,15,21,28,36,45,55..."),
        ("Numeros quadrados", "n^2: 1,4,9,16,25,36,49,64,81,100..."),
        ("Numeros primos", "2,3,5,7,11,13,17,19,23,29,31,37,41,43,47..."),
    ]
    RL.extend(sequencias)
''')

print("Part 4 written (Etica + RLP)")
