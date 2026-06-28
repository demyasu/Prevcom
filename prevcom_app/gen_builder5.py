"""Builds programmatic_flashcards.py - part 5: RLP + Previdencia + TI"""
import os

path = r'D:\Prevcom\prevcom_app\programmatic_flashcards.py'

def write(s):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(s + '\n')

write('''    estatistica = [
        ("Media aritmetica", "Soma/n. Ex: media 2,4,6 = 4."),
        ("Media ponderada", "Σ(xi*pi)/Σpi."),
        ("Mediana", "Valor central dados ordenados."),
        ("Moda", "Valor que mais se repete."),
        ("Variancia amostral", "s^2 = Σ(xi-x̄)^2/(n-1)."),
        ("Desvio padrao", "s = √s^2."),
        ("Coeficiente variacao", "CV = s/x̄."),
        ("Quartis", "Q1=25%, Q2/mediana=50%, Q3=75%."),
        ("IQR", "Q3-Q1. Dispersao 50% centrais."),
        ("Boxplot", "Min, Q1, Med, Q3, Max, Outliers."),
        ("Correlacao r", "Forca relacao linear. -1≤r≤1."),
        ("Regressao linear Y=β0+β1X+ε", "Minimos quadrados."),
        ("R2", "Proporcao variancia Y explicada."),
        ("Teste hipotese", "H0 vs H1. Nivel α."),
        ("Erro tipo I", "Rejeitar H0 verdadeira. α."),
        ("Erro tipo II", "Nao rejeitar H0 falsa. β."),
        ("p-valor", "Prob. de resultado mais extremo dado H0."),
        ("IC", "Estimativa ± margem erro."),
    ]
    RL.extend(estatistica)

    matrizes = [
        ("Matriz: definicao", "Tabela m linhas x n colunas."),
        ("Identidade I", "1 diagonal, 0 demais."),
        ("Transposta", "Linhas viram colunas. A^T."),
        ("Matriz simetrica", "A = A^T."),
        ("Soma matrizes", "Termo a termo."),
        ("Multiplicacao", "Linha x coluna. Am×n * Bn×p = Cm×p."),
        ("Determinante 2x2", "det[[a,b],[c,d]] = ad - bc."),
        ("Determinante 3x3", "Regra Sarrus."),
        ("Sistema Cramer", "x = det(Ax)/det(A)."),
    ]
    RL.extend(matrizes)

    funcoes = [
        ("Funcao definicao", "Cada x tem exatamente um y."),
        ("Dominio", "Valores de entrada (x)."),
        ("Contradominio", "Valores possiveis saida."),
        ("Imagem", "Valores efetivamente assumidos."),
        ("Injetora", "x1≠x2 => f(x1)≠f(x2)."),
        ("Sobrejetora", "Todo y tem algum x."),
        ("Bijetora", "Injetora + sobrejetora."),
        ("Par", "f(-x)=f(x). Simetria y. Ex: x^2."),
        ("Impar", "f(-x)=-f(x). Simetria origem. Ex: x^3."),
        ("Inversa", "f^-1(f(x)) = x."),
        ("Composta", "f∘g(x) = f(g(x))."),
        ("Afim f(x)=ax+b", "Reta. a=angular, b=linear."),
        ("Quadratica f(x)=ax^2+bx+c", "Parabola. V(-b/2a, -Δ/4a)."),
        ("Exponencial f(x)=a^x", "Cresce se a>1, decresce 0<a<1."),
        ("Logaritmica f(x)=log_a(x)", "Inversa da exponencial."),
        ("Modular f(x)=|x|", "x se x>=0, -x se x<0."),
    ]
    RL.extend(funcoes)

    matematica_fin = [
        ("Juros simples: M = C(1+in)", "J=C*i*n."),
        ("Juros compostos: M = C(1+i)^n", "Crescimento exponencial."),
        ("Desconto simples D = N*i*n", "Valor atual = N(1-in)."),
        ("Desconto composto A = N/(1+i)^n", "Racional composto."),
        ("Taxa proporcional (JS)", "Anual = 12 * mensal."),
        ("Taxa equivalente (JC)", "(1+ia)=(1+im)^12."),
        ("Serie postecipada PMT", "PMT = PV*i/(1-(1+i)^-n)."),
        ("Serie antecipada PMT", "PMT = PV*i/((1+i)*(1-(1+i)^-n))."),
        ("VPL = ΣFCt/(1+i)^t - Inv", "Aceita se VPL>0."),
        ("TIR", "Taxa i que zera VPL."),
        ("SAC", "Amortizacao constante. Prestacao decrescente."),
        ("Price", "Prestacao constante. Amortizacao crescente."),
    ]
    RL.extend(matematica_fin)

    print(f"  Raciocinio Logico programatico: {len(RL)} cards")

    # ================================================================
    # 4. PREVIDENCIA COMPLEMENTAR NO BRASIL
    # ================================================================

    lc108 = [
        ("LC 108/2001: art. 1", "Relacao Uniao/estados/municipios e EFPC."),
        ("LC 108/2001: art. 2 paridade", "Contribuicao patrocinador ≤ participante."),
        ("LC 108/2001: art. 3", "Minimo 3 anos ente publico."),
        ("LC 108/2001: art. 5 conselhos", "Participantes e assistidos nos conselhos."),
        ("LC 108/2001: art. 6 CD", "Min 4: metade eleita, metade indicada."),
        ("LC 108/2001: art. 7 presidente CD", "Indicado patrocinador. Voto qualidade."),
        ("LC 108/2001: art. 9 CF", "Min 3: 1 patrocinador, 1 participantes, 1 assistidos."),
        ("LC 108/2001: art. 11 DIREX", "Indicada patrocinador, aprovada CD."),
        ("LC 108/2001: art. 13 investimentos", "Conforme regulamento e politicas."),
        ("LC 108/2001: art. 14 transparencia", "Informar participantes."),
        ("LC 108/2001: art. 16 deficit", "Patrocinador responde por deficit."),
        ("LC 108/2001: art. 17 retirada", "Cancelamento patrocinio."),
        ("LC 108/2001: art. 19 contrib. extra", "Para equacionamento deficit."),
        ("LC 108/2001: art. 21 subsidiaria", "LC 109/2001 no que nao dispoe."),
    ]
    PR.extend(lc108)
''')

write('''    lc109 = [
        ("LC 109/2001: art. 1", "Facultativo, autonomo, complementar."),
        ("LC 109/2001: art. 2 EFPC", "Fechada, sem fins lucrativos."),
        ("LC 109/2001: art. 3 EAPC", "Aberta, com fins lucrativos."),
        ("LC 109/2001: art. 5 autorizacao", "Orgao regulador autoriza EFPC."),
        ("LC 109/2001: art. 7 regulamento", "Direitos e obrigacoes."),
        ("LC 109/2001: art. 8 planos", "BD, CD, CV."),
        ("LC 109/2001: art. 14 beneficios", "Morte, invalidez, sobrevivencia."),
        ("LC 109/2001: art. 15 portabilidade", "Transferir recursos."),
        ("LC 109/2001: art. 16 resgate", "Resgatar conforme regulamento."),
        ("LC 109/2001: art. 17 BPD", "Manter recursos sem contribuir."),
        ("LC 109/2001: art. 18 autopatrocínio", "Contribuir ambas partes."),
        ("LC 109/2001: art. 20 elegibilidade", "Requisitos concessao."),
        ("LC 109/2001: art. 22 contribuicoes", "Normais e extraordinarias."),
        ("LC 109/2001: art. 24 reservas", "Tecnicas, contingencia, oscilacao."),
        ("LC 109/2001: art. 26 avaliacao", "Atuarial anual obrigatoria."),
        ("LC 109/2001: art. 27 deficit", "Equacionamento obrigatorio."),
        ("LC 109/2001: art. 28 superavit", "Reserva contingencia, revisao."),
        ("LC 109/2001: art. 31 governanca", "CD, CF, DIREX."),
        ("LC 109/2001: art. 40 transparencia", "Informar participantes."),
        ("LC 109/2001: art. 44 liquidacao", "Extrajudicial."),
        ("LC 109/2001: art. 45 intervencao", "PREVIC intervem."),
        ("LC 109/2001: art. 52 tributacao", "Beneficios fiscais."),
        ("LC 109/2001: art. 53 fiscalizacao", "PREVIC (EFPC) e SUSEP (EAPC)."),
        ("LC 109/2001: art. 64 optante", "Servidor pode optar por complementar."),
    ]
    PR.extend(lc109)

    prevcom = [
        ("PREVCOM: Lei 14.653/2011", "Autorizou criacao."),
        ("PREVCOM: Decreto 57.785/2012", "Aprovou Estatuto."),
        ("PREVCOM: natureza", "EFPC sem fins lucrativos."),
        ("PREVCOM: plano RP", "Servidores efetivos SP."),
        ("PREVCOM: plano RG", "Servidores celetistas SP."),
        ("PREVCOM: plano MULTI", "Diferentes orgaos SP."),
        ("PREVCOM: plano MS", "Seguranca publica SP."),
        ("PREVCOM: plano MT", "Magisterio SP."),
        ("PREVCOM: taxa administracao", "Percentual sobre saldo."),
        ("PREVCOM: paridade", "Patrocinador = participante."),
        ("PREVCOM: conselho deliberativo", "Governo + eleitos."),
        ("PREVCOM: conselho fiscal", "Fiscaliza administracao."),
        ("PREVCOM: diretoria", "Presidente + diretores."),
    ]
    PR.extend(prevcom)

    investimentos = [
        ("Tesouro Selic", "Pos-fixado. Baixo risco."),
        ("Tesouro Prefixado", "Taxa fixa. Marcacao mercado."),
        ("Tesouro IPCA+", "Protecao inflacao + taxa real."),
        ("CDB", "Certificado Deposito Bancario. FGC."),
        ("Debentures", "Titulos divida empresas."),
        ("CRI/CRA", "Recebiveis Imobiliario/Agro. Isentos IR."),
        ("LCI/LCA", "Letras Credito Imobiliario/Agro. Isentos IR."),
        ("Fundos acoes", "Carteira acoes. Risco alto."),
        ("Fundos multimercado", "Multiplos ativos. Gestao ativa."),
        ("Fundos RF", "Titulos RF. Baixo risco."),
        ("FII", "Fundos Imobiliarios. Aluguel + valorizacao."),
        ("Private equity", "Empresas fechadas. Longo prazo."),
        ("Venture capital", "Startups. Alto risco/retorno."),
        ("Derivativos", "Valor derivado de ativo subjacente."),
        ("Opcoes", "Direito comprar/vender. Call/Put."),
        ("Futuros", "Contrato padronizado. Bolsa."),
        ("Swaps", "Troca fluxos financeiros."),
        ("Limite RF (CMN)", "Minimo 55% renda fixa."),
        ("Limite RV (CMN)", "Maximo 40% (rating) ou 25%."),
        ("Limite Imoveis (CMN)", "Maximo 8%."),
        ("Limite Exterior (CMN)", "Maximo 10%."),
    ]
    PR.extend(investimentos)

    atuarial = [
        ("Reserva matematica", "Valor presente compromissos futuros."),
        ("Passivo atuarial", "Total obrigacoes atuariais."),
        ("Ativo liquido", "Recursos para cobertura."),
        ("Taxa juros real", "Taxa desconto. Hipotese critica."),
        ("Tabua AT-2000", "Americana mortalidade."),
        ("Tabua BR-EMS", "Brasileira sobrevivencia."),
        ("Tabua invalidez Alvaro Vindas", "Probabilidade invalidez."),
        ("Rotatividade", "Probabilidade desligamento."),
        ("Crescimento salarial", "Projecao aumento real."),
        ("Hipotese inflacao", "Projecao LP."),
        ("Hipotese composicao familiar", "% com dependentes."),
        ("Credito unitario projetado", "Projeta e distribui custo."),
        ("Metodo agregado", "Custo nivelado grupo todo."),
        ("Deficit: causas", "Hipotese errada, baixa rentabilidade, longevidade."),
        ("Superavit", "Ativos > passivo atuarial."),
        ("Provisao matematica", "Beneficios concedidos/a conceder."),
        ("Provisao risco", "Riscos nao ocorridos."),
        ("Nota tecnica atuarial", "Bases tecnicas do plano."),
    ]
    PR.extend(atuarial)

    beneficios = [
        ("Aposentadoria normal", "Idade + tempo contribuicao."),
        ("Aposentadoria antecipada", "Antes idade normal. Redutor atuarial."),
        ("Aposentadoria invalidez", "Incapacidade permanente total."),
        ("Pensao por morte", "Aos dependentes."),
        ("Auxilio-doenca", "Incapacidade temporaria."),
        ("Abono anual (13o)", "Parcela adicional anual."),
        ("Renda vitalicia", "Pagamento vitalicio."),
        ("Renda vitalicia prazo minimo", "Garantia prazo minimo."),
        ("Renda vitalicia reversivel", "Continua ao conjuge."),
        ("Renda temporaria", "Prazo determinado."),
        ("Renda certa", "Valor fixo periodo."),
        ("Peculio morte", "Pagamento unico."),
        ("BPD", "Proporcional tempo contribuicao."),
    ]
    PR.extend(beneficios)

    tributos = [
        ("PGBL", "Deducao 12% renda bruta. IR total resgate."),
        ("VGBL", "Sem deducao. IR so rendimentos."),
        ("Tabela regressiva IR", "10% (60+ meses) a 27,5% (2 anos)."),
        ("Tabela progressiva IR", "0% a 27,5% (IRPF)."),
        ("Portabilidade sem IR", "Diferimento fiscal."),
        ("Contribuicao patrocinador", "Nao tributada participante."),
        ("Rendimento do plano", "Isento durante acumulacao."),
    ]
    PR.extend(tributos)

    governanca_efpc = [
        ("CD: orgao maximo", "Politicas e estrategias."),
        ("CF: fiscaliza", "Atos e contas."),
        ("DIREX: gestao", "Operacional."),
        ("Comite investimentos", "Assessora DIREX."),
        ("Comite auditoria", "Controles internos."),
        ("Comite risco", "Gestao riscos."),
        ("Politica investimentos", "Diretrizes alocacao."),
        ("Politica riscos", "Identificar, avaliar, controlar."),
        ("Planejamento estrategico", "Plano plurianual."),
        ("Auditoria independente", "Auditoria externa."),
        ("Atuario externo", "Avaliacao atuarial."),
        ("Transparencia", "Site, extrato, assembleia."),
    ]
    PR.extend(governanca_efpc)

    previc = [
        ("PREVIC autarquia", "Vinculada MPS."),
        ("PREVIC finalidade", "Fiscalizar EFPC."),
        ("PREVIC competencias", "Autorizar, fiscalizar, sancionar."),
        ("PREVIC fiscalizacao direta", "Inspecoes in loco."),
        ("PREVIC fiscalizacao indireta", "Analise documentos."),
        ("PREVIC sancoes", "Advertencia, multa, inabilitacao, intervencao, liquidacao."),
        ("PREVIC intervencao", "Nomeia interventor."),
        ("PREVIC liquidacao", "Encerramento EFPC."),
        ("PREVIC termo ajustamento", "Ajuste conduta."),
        ("PREVIC cadastro", "Registro publico."),
        ("PREVIC ouvidoria", "Atendimento participantes."),
    ]
    PR.extend(previc)

    tipos_planos = [
        ("BD: beneficio fixo", "Risco atuarial da entidade."),
        ("CD: contribuicao fixa", "Risco do participante."),
        ("CV: misto", "Acumulacao CD, beneficio BD."),
        ("BD vantagens", "Seguranca, previsibilidade."),
        ("BD desvantagens", "Custo alto, complexo."),
        ("CD vantagens", "Simplicidade, portabilidade."),
        ("CD desvantagens", "Incerteza valor beneficio."),
    ]
    PR.extend(tipos_planos)

    participantes_direitos = [
        ("Direito informacao", "Extrato, relatorio anual."),
        ("Direito portabilidade", "Transferir recursos."),
        ("Direito resgate", "Saldo conforme regulamento."),
        ("Direito BPD", "Manter sem contribuir."),
        ("Direito autopatrocínio", "Contribuir ambas partes."),
        ("Direito voto", "Eleger conselhos."),
        ("Dever contribuir", "Conforme regulamento."),
        ("Dever informar", "Atualizar dados."),
    ]
    PR.extend(participantes_direitos)

    regimes = [
        ("Capitalizacao", "Acumulo recursos. Obrigatorio RPC."),
        ("Reparticao simples", "Contribuicoes pagam beneficios."),
        ("Reparticao capitais cobertura", "Futuro custeado futuro."),
        ("Capitalizacao vantagens", "Reserva, sustentabilidade."),
        ("Capitalizacao desvantagens", "Longo prazo, risco mercado."),
    ]
    PR.extend(regimes)

    print(f"  Previdencia programatico: {len(PR)} cards")
''')

print("Part 5 written (Raciocinio + Previdencia)")
