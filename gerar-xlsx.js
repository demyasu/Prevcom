const ExcelJS = require('exceljs');

async function gerarXLSX() {
  const wb = new ExcelJS.Workbook();
  wb.creator = 'Macetes VUNESP PREVCOM';
  wb.created = new Date();

  const materias = {
    'Portugues': { cor: '4472C4', topicos: [
      ['#', 'Topico', 'Descricao', 'Incidencia', 'Macete'],
      [1,'Compreensao textual','Identificacao explicita de informacoes no texto','Muito Alta','A resposta esta no texto. Sublinhe palavras-chave. Desconfie de extrapolacoes.'],
      [2,'Inferencia textual','Informacoes implicitas, subentendidos e pressupostos','Alta','Pergunte: "O que o texto permite concluir?" Nao invente fora do texto.'],
      [3,'Intencionalidade discursiva','Finalidade do texto: informar, convencer, instruir, entreter','Media','Identifique o genero textual. Artigo de opiniao defende tese; charge critica.'],
      [4,'Tipologia textual','Narracao, descricao, dissertacao, exposicao, injuncao','Media','Dissertacao = defesa de ponto de vista; Injuncao = instrucao/ordem.'],
      [5,'Generos textuais','Reportagem, editorial, cronica, carta, e-mail, oficio, charge','Media','VUNESP adora charge e tirinha. Pergunta: "Qual a critica?"'],
      [6,'Relacoes intertextuais','Parafrase, parodia, citacao, epigrafe','Baixa','Parafrase = mesma ideia, palavras diferentes. Parodia = imitacao critica.'],
      [7,'Coerencia textual','Continuidade de sentido, progressao tematica, contradicoes','Media','Verifique se ha contradicao entre periodos. Se houver, o texto eh incoerente.'],
      [8,'Coesao referencial','Anafora (retomar), catafora (antecipar) por pronomes, sinonimos, elipses','Alta','"O qual", "cujo", "isso", "este" — identifique a que termo se referem.'],
      [9,'Coesao sequencial','Conectores que ligam oracoes: causa, consequencia, condicao, conclusao','Alta','Tabela: causa (pois/ja que), consequencia (portanto), condicao (se), conclusao (logo).'],
      [10,'Ambiguidade e polissemia','Duplo sentido de palavras ou construcoes','Media','A VUNESP pergunta: "Em qual alternativa ha ambiguidade?"'],
      [11,'Substantivo','Classificacao, flexao de genero e numero, grau','Media','Plural de compostos: so o primeiro varia (couve-flor → couves-flores) ou os dois (pao-de-mel → paes-de-mel).'],
      [12,'Adjetivo','Flexao, locucao adjetiva, grau comparativo e superlativo','Media','Locucao adjetiva = de + substantivo (amor de mae = amor materno).'],
      [13,'Artigo','Definido (o/a) e indefinido (um/uma). Emprego e omissao','Media','Artigo indefinido pode indicar aproximacao (uns 10 anos).'],
      [14,'Numeral','Cardinal, ordinal, multiplicativo, fracionario','Baixa','"Ambos" = numeral. "Milhao" exige artigo (o milhao).'],
      [15,'Pronomes pessoais','Retos (eu, tu) e obliquos (me, te, se, o, lhe). Uso de "o" vs "lhe"','Muito Alta','"O" = objeto direto. "Lhe" = objeto indireto (a ele/a ela).'],
      [16,'Pronomes relativos','Que, quem, cujo, onde, o qual. Funcao sintatica','Muito Alta','"Cujo" indica posse. "Onde" = lugar fisico. "Que" = universal.'],
      [17,'Colocacao pronominal','Proclise (atrativos), enclise (inicio), mesoclise (futuro)','Alta','Palavras atrativas: nao, nunca, ninguem, que, se, ja, talvez.'],
      [18,'Verbos — tempos e modos','Presente, preteritos, futuro. Indicativo, subjuntivo, imperativo','Muito Alta','Subjuntivo = duvida/hipotese (talvez, se, quando). Indicativo = certeza.'],
      [19,'Verbos — vozes verbais','Ativa, passiva (analitica e sintetica), reflexiva','Alta','Passar para passiva: objeto direto vira sujeito. Voz sintetica = verbo + "se".'],
      [20,'Conjuncoes','Coordenativas e subordinativas. Valores semanticos','Alta','Coordenativas: aditivas (e), adversativas (mas), alternativas (ou), conclusivas (logo), explicativas (pois).'],
      [21,'Concordancia verbal','Verbo com sujeito. Casos especiais: "mais de um", "haver", "fazer"','Muito Alta','"Haver" no sentido de existir eh impessoal (singular). "Fazer" temporal tambem.'],
      [22,'Concordancia nominal','Adjetivo com substantivo. Casos: "mesmo", "proprio", "anexo", "obrigado"','Alta','"Anexo" concorda (anexa). "Em anexo" eh invariável. "Eh proibido entrada" (sem artigo = invariável).'],
      [23,'Regencia verbal','Verbo + preposicao. Assistir, aspirar, implicar, proceder, visar','Muito Alta','Assistir o filme = ver (A). Assistir ao filme = ver (AI). Assistir o doente = ajudar (A).'],
      [24,'Regencia nominal','Nome + preposicao. Apto a, capaz de, junto a, em vez de','Alta','Decore as preposicoes que cada nome exige: "acessivel a", "contente com", "curioso de".'],
      [25,'Crase','Fusao "a + a". Regra pratica: substituir por "ao"','Muito Alta','Se trocar por "ao" e soar bem, usa crase. "As pressas", "a noite", "a medida que".'],
      [26,'Pontuacao — virgula','Separacao de oracoes, enumeracoes, vocativos, apostos','Muito Alta','Virgula NAO separa sujeito de verbo. Separa oracoes coordenadas.'],
      [27,'Pontuacao — travessao, aspas, parenteses','Destaque, citacao, intercalacao','Media','Travessao pode substituir virgula ou parenteses para dar enfase.'],
      [28,'Ortografia e acentuacao','Novo Acordo Ortografico. Acentuacao de proparoxitonas, paroxitonas, oxitonas','Alta','Proparoxitonas sao todas acentuadas. Paroxitonas tem regras especificas.'],
      [29,'Reescrita de frases','Substituir trechos mantendo sentido e correcao','Muito Alta','Tipica questao VUNESP. Verifique: (1) sentido, (2) regencia, (3) concordancia, (4) pontuacao.'],
      [30,'Figuras de linguagem','Metafora, metonimia, hiperbole, eufemismo, ironia, antitese','Media','Metafora = comparacao implicita. Metonimia = parte pelo todo (ler Machado de Assis = ler a obra).'],
    ]},
    'Etica': { cor: 'ED7D31', topicos: [
      ['#', 'Topico', 'Descricao', 'Incidencia', 'Macete'],
      [1,'Regras deontologicas (Decreto 1.171/94, I a V)','Dignidade, decoro, zelo, eficacia, consciencia moral','Muito Alta','Decore o inciso I: "A dignidade, o decoro, o zelo, a eficacia e a consciencia dos principios morais sao primados maiores."'],
      [2,'Distincao legal vs etico (inciso II)','Nao basta o legal; eh preciso o honesto','Muito Alta','A VUNESP explora: "Nao tera que decidir somente entre o legal e o ilegal, mas principalmente entre o honesto e o desonesto."'],
      [3,'Deveres do servidor (inciso XIV)','Exercer com zelo, ser assiduo, tratar bem o publico, representar irregularidades','Alta','Use a mnemônica "ZASTRE": Zelar, Assiduidade, Sigilo (quando necessario), Tratar bem, Representar.'],
      [4,'Proibicoes ao servidor (inciso XV)','Retirar documentos, fazer comercio entre colegas, coagir subordinados, aceitar presentes','Alta','"Nao retirar documentos sem autorizacao", "nao fazer comercio na reparticao".'],
      [5,'Comissao de Etica (inciso XIV)','3 membros titulares + 3 suplentes. Mandato coincidente. Pena de censura','Muito Alta','A Comissao NAO demite. Aplica censura etica. Decore: 3 + 3.'],
      [6,'Procedimento etico','Representacao, apuracao, defesa, julgamento, recurso','Media','Prazo para defesa: 10 dias. Recurso para a Comissao Superior de Etica.'],
      [7,'Censura etica (inciso XV)','Unica penalidade prevista no Codigo','Alta','Censura eh publica e divulgada no boletim interno. Nao confundir com suspensao ou demissao.'],
      [8,'Aplicacao a terceirizados','O codigo se aplica a quem preste servicos de natureza permanente','Media','Inclui estagiarios, terceirizados, contratados.'],
      [9,'Principios da Adm. Publica (CF art. 37)','Legalidade, Impessoalidade, Moralidade, Publicidade, Eficiencia','Muito Alta','Mnemônico LIMPE. Cai em 90% das provas.'],
      [10,'Moralidade administrativa','Honestidade, boa-fe, probidade. Distincao entre legal e moral','Alta','Legal = conforme a lei. Moral = honesto, probo, justo. Um ato pode ser legal e imoral.'],
      [11,'Atos de enriquecimento ilicito (LIA art. 9)','Receber vantagem indevida, superfaturamento, desvio','Alta','Vantagem economica direta ou indireta. Exigencia de dolo especifico.'],
      [12,'Atos que causam dano ao erario (LIA art. 10)','Perda patrimonial publica por acao ou omissao dolosa','Alta','Antes admitia culpa. Apos Lei 14.230/21 so dolo.'],
      [13,'Atos contra principios (LIA art. 11)','Violar principios da administracao publica','Alta','Exige dolo + lesividade relevante. Ex: nomear parente (nepotismo).'],
      [14,'Sancoes (LIA art. 12)','Perda da funcao publica, suspensao de direitos politicos, multa','Muito Alta','As sancoes variam conforme o tipo de ato. As mais graves: art. 9 (enriquecimento).'],
      [15,'Alteracoes Lei 14.230/2021','Fim da improbidade culposa, necessidade de dolo, prescricao intercorrente','Muito Alta','So improbidade DOLOSA. Decore: "Improbidade nao eh erro, eh ma-fe."'],
      [16,'Lei 12.813/2013 - Conflito de Interesses','Servidor nao pode atuar onde haja interesse pessoal ou de familiares','Alta','Quarentena de 6 meses para ex-ocupantes de cargos. Parentes ate 3o grau.'],
      [17,'Lei 12.846/2013 - Anticorrupcao','Responsabilidade objetiva da pessoa juridica. Multa de 0,1% a 20%','Alta','Objetiva = nao precisa provar dolo. Acordo de leniencia.'],
      [18,'Lei 12.527/2011 - Acesso a Informacao','Transparencia ativa (publicar) e passiva (responder pedidos)','Media','Prazo: 20 dias + 10 de prorrogacao. Informacao sigilosa tem prazos de classificacao.'],
      [19,'Decreto 9.203/2017 - Governanca Publica','Integridade, transparencia, accountability, lideranca','Media','"Integridade eh principio da governanca publica." Decore os principios.'],
      [20,'Processo Adm. Disciplinar (PAD)','Sindicancia (30d) → PAD (60d). Penalidades: advertencia, suspensao, demissao','Alta','Sindicancia investiga; PAD julga. Ampla defesa e contraditorio.'],
      [21,'Comissoes de Etica','Atribuicoes: orientar, aconselhar, apurar. Nao sancionam alem da censura','Alta','3 membros. Orgao consultivo e deliberativo. Pode recomendar demissao ao superior.'],
      [22,'Estimulo a integridade','Programa de integridade (compliance), canal de denuncia, codigo de conduta','Media','Compliance = conjunto de mecanismos para evitar desvios. Pilares: prevencao, deteccao, correcao.'],
    ]},
    'RaciocinioLogico': { cor: '70AD47', topicos: [
      ['#', 'Topico', 'Descricao', 'Incidencia', 'Macete'],
      [1,'Proposicoes simples e compostas','Frases declarativas (V ou F). Conectivos logicos','Muito Alta','"Que horas sao?" NAO eh proposicao. "x > 5" eh sentenca aberta.'],
      [2,'Conectivo "E" (conjuncao)','p ^ q. Verdadeiro so se ambos forem V','Muito Alta','Tabela: V^V=V; V^F=F; F^V=F; F^F=F.'],
      [3,'Conectivo "OU" (disjuncao inclusiva)','p v q. Falso so se ambos forem F','Muito Alta','Tabela: VvV=V; VvF=V; FvV=V; FvF=F.'],
      [4,'Conectivo "OU...OU" (disjuncao exclusiva)','p ⊻ q. Verdadeiro quando os valores forem diferentes','Alta','"Ou come ou nao come." Um exclui o outro.'],
      [5,'Conectivo "SE...ENTAO" (condicional)','p → q. Falso APENAS quando V → F','Muito Alta','Decore: "Vera Fischer eh FALSA" (V→F = F).'],
      [6,'Conectivo "SE E SOMENTE SE" (bicondicional)','p ↔ q. Verdadeiro quando valores sao iguais','Alta','V↔V=V; F↔F=V; V↔F=F; F↔V=F. "Iguais = V".'],
      [7,'Tabelas-verdade','Construcao e interpretacao. Numero de linhas = 2n','Muito Alta','n = numero de proposicoes. 2 proposicoes = 4 linhas; 3 = 8; 4 = 16.'],
      [8,'Tautologia, contradicao e contingencia','Tautologia = sempre V. Contradicao = sempre F. Contingencia = V e F','Alta','Resolva a tabela completa. Se tudo V = tautologia. Tudo F = contradicao.'],
      [9,'Equivalencias logicas','p→q ≡ ~q→~p (contrapositiva). p→q ≡ ~p v q','Muito Alta','"Se chover, a rua fica molhada" ≡ "Se a rua nao esta molhada, nao choveu."'],
      [10,'Negacao de proposicoes','~(p^q) ≡ ~p v ~q. ~(pvq) ≡ ~p ^ ~q. ~(p→q) ≡ p ^ ~q','Muito Alta','Negacao do "E" = "OU" negado. Negacao do "SE...ENTAO" = "E" (Vera Fischer).'],
      [11,'Negacao de quantificadores','~(Todo A eh B) = Algum A nao eh B. ~(Nenhum A eh B) = Algum A eh B','Alta','Para negar "Todo", basta um "Algum... nao". Para negar "Nenhum", basta um "Algum... eh".'],
      [12,'Argumentacao logica','Premissas → conclusao. Validade: se premissas V, conclusao deve ser V','Alta','Um argumento valido NAO significa que a conclusao eh verdadeira na realidade.'],
      [13,'Diagramas logicos (Venn)','Conjuntos, intersecoes, "Todo", "Algum", "Nenhum"','Muito Alta','Desenhe SEMPRE. "Todo A eh B" = circulo A dentro de B. Comece pela intersecao.'],
      [14,'Problemas de associacao','Tabela de dupla entrada com nomes, objetos, caracteristicas','Alta','Monte a tabela. Preencha com V/F. Uma linha contradizendo = hipotese errada.'],
      [15,'Sequencias numericas','PA, PG, Fibonacci, alternadas, intercaladas','Muito Alta','Calcule a diferenca entre termos. Se constante = PA. Se constante na divisao = PG.'],
      [16,'Sequencias de letras e figuras','Posicao no alfabeto, padrao visual, rotacao, cores','Alta','A=1, B=2, C=3... Veja a distancia entre letras consecutivas.'],
      [17,'Analise combinatoria — PFC','Principio fundamental da contagem. Multiplicar possibilidades','Alta','"De quantas maneiras?" → multiplique as opcoes de cada etapa.'],
      [18,'Permutacao, arranjo e combinacao','Permutacao: n!. Arranjo: A(n,p) = n!/(n-p)!. Combinacao: C(n,p) = n!/(p!(n-p)!)','Media','Combinacao = ordem NAO importa (equipe). Arranjo = ordem importa (senha).'],
      [19,'Probabilidade','P = favoraveis / totais. Eventos independentes (multiplica). Mutuamente exclusivos (soma)','Media','"E" = multiplica. "OU" = soma. Probabilidade de algo NAO ocorrer = 1 - P(ocorrer).'],
      [20,'Raciocinio matematico','Regra de tres, porcentagem, proporcao, grandezas diretas/inversas','Alta','Desconfie de grandezas inversas: quanto mais de uma, menos da outra (velocidade x tempo).'],
      [21,'Estruturas logicas','"Se...entao" no raciocinio cotidiano. Silogismos. Condicoes necessarias e suficientes','Muito Alta','A → B: A eh suficiente para B. B eh necessaria para A.'],
      [22,'Raciocinio critico e analitico','Analisar argumentos, identificar falacias, conclusoes implicitas','Media','VUNESP adota questoes com textos curtos e pergunta: "qual a conclusao?"'],
    ]},
    'Previdencia': { cor: 'FFC000', topicos: [
      ['#', 'Topico', 'Descricao', 'Incidencia', 'Macete'],
      [1,'Regime Geral de Previdencia Social (RGPS)','INSS. Trabalhadores celetistas. Regime publico, obrigatorio, solidario','Muito Alta','RGPS = setor privado e celetistas publicos. Teto INSS (2026: ~R$ 8.157,41).'],
      [2,'Regime Proprio de Previdencia Social (RPPS)','Servidores publicos titulares de cargo efetivo. Cada ente tem seu regime','Muito Alta','RPPS = Uniao, Estados, DF, Municipios. Regime financeiro: reparticao simples ou capitalizacao.'],
      [3,'Regime de Previdencia Complementar (RPC)','Facultativo, capitalizacao individual, contribuicao definida','Muito Alta','Eh o regime da PREVCOM. Baseado na LC 109/2001.'],
      [4,'Diferencas entre os regimes','RGPS (publico, obrigatorio, solidario) x RPPS (publico, obrigatorio, servidores) x RPC (privado, facultativo, capitalizacao)','Alta','Quadro mental: RGPS = todos; RPPS = servidores; RPC = complementar facultativo.'],
      [5,'Art. 201 da CF/88','Dispoe sobre o RGPS. Cobertura: aposentadoria, pensao, auxilios','Media','"Plano geral de previdencia social." Organizado pelo INSS.'],
      [6,'Art. 202 da CF/88','Dispoe sobre a previdencia complementar. Natureza privada, facultativa, capitalizacao','Muito Alta','"A previdencia complementar eh facultativa, organizada de forma autonoma independente."'],
      [7,'EC 103/2019 (Reforma da Previdencia)','Instituiu o regime de previdencia complementar para servidores federais (Funpresp). Limite ao teto do INSS','Muito Alta','Servidor que ganha acima do teto do INSS DEVE ter complementar. Estados podem instituir.'],
      [8,'LC 109/2001','Lei principal do RPC. EFPC, EAPC, planos de beneficios, portabilidade, resgate','Muito Alta','Conhecida como "Lei da Previdencia Complementar". Decore: EFPC = fechada; EAPC = aberta.'],
      [9,'LC 108/2001','Relacao entre entes publicos e suas EFPC. Patrocinio publico','Alta','Aplica-se quando Uniao, Estados ou Municipios sao patrocinadores.'],
      [10,'Lei 14.653/2011','Autorizou a criacao da SP-PREVCOM','Alta','"Lei de criacao da PREVCOM." Decore o numero.'],
      [11,'PREVIC (Superintendencia Nacional de Previdencia Complementar)','Autarquia federal. Regula e fiscaliza as EFPC','Muito Alta','PREVIC fiscaliza. Eh vinculada ao Ministerio da Previdencia.'],
      [12,'CNPC (Conselho Nacional de Previdencia Complementar)','Orgao normativo do RPC. Define diretrizes e regulamentos','Alta','CNPC eh NORMATIVO. PREVIC eh FISCALIZADOR. Nao confunda.'],
      [13,'Diferenca PREVIC x CNPC','CNPC = normas, diretrizes. PREVIC = execucao, fiscalizacao','Alta','CNPC "cria regras"; PREVIC "faz cumprir".'],
      [14,'CVM (Comissao de Valores Mobiliarios)','Regula investimentos dos planos. Aplica-se as EFPC','Media','Os recursos dos planos devem seguir as regras da CVM e do CMN.'],
      [15,'EFPC (Entidade Fechada de Previdencia Complementar)','Sem fins lucrativos. Acesso restrito a empregados do patrocinador','Muito Alta','A PREVCOM eh uma EFPC. Ex: Funpresp, Previ, Petros, Postalis.'],
      [16,'EAPC (Entidade Aberta de Previdencia Complementar)','Fins lucrativos. Acesso universal. Operadas por bancos e seguradoras','Media','Ex: PGBL, VGBL (bancos). Qualquer pessoa pode contratar.'],
      [17,'Patrocinador','Empresa ou ente publico que institui o plano e contribui','Alta','Patrocinador contribui para o plano dos empregados. Pode ser publico ou privado.'],
      [18,'Instituidor','Entidade de classe que institui plano para seus associados','Media','Sindicatos, associacoes, conselhos profissionais.'],
      [19,'Participante','Pessoa fisica que adere ao plano. Ativo (contribui) ou assistido (recebe beneficio)','Alta','Ativo = ainda contribui. Assistido = ja esta recebendo (aposentado/pensionista).'],
      [20,'Assistido','Participante ou beneficiario em gozo de beneficio','Media','Sinonimo: "beneficiario em manutencao."'],
      [21,'Plano de Contribuicao Definida (CD)','Contribuicao definida, beneficio depende do saldo acumulado. Risco do participante','Alta','CD = "voce sabe quanto contribui, mas nao sabe quanto vai receber."'],
      [22,'Plano de Beneficio Definido (BD)','Beneficio predefinido. Risco atuarial da entidade','Media','BD = "voce sabe quanto vai receber." Mais comum em planos antigos.'],
      [23,'Plano Misto','Combina CD + BD. Parte contribuicao definida, parte beneficio definido','Baixa','Ex: PREVCOM tem planos mistos.'],
      [24,'Portabilidade','Direito de transferir recursos entre planos sem perda','Alta','Prazo: 30 dias para pedir. Disponível para quem nao esta assistido.'],
      [25,'Resgate','Direito de sacar recursos acumulados ao sair do plano','Alta','Resgate parcial ou total. Incide IR.'],
      [26,'Beneficio proporcional diferido (BPD)','Congela o beneficio futuro ate a data de elegibilidade','Media','Opcao para quem sai do plano antes de se aposentar.'],
      [27,'Estatuto Social da PREVCOM','Estrutura, governanca, competencias do CD, CF e DIREX','Alta','CD = Conselho Deliberativo. CF = Conselho Fiscal. DIREX = Diretoria Executiva.'],
      [28,'Planos de beneficios PREVCOM','Prevcom RP, RG, RG-UNIS, RO, MULTI, MS, MT, PA, SP Previdencia','Alta','Cada plano atende a um grupo de servidores. Verifique o edital para detalhes.'],
      [29,'Regimento Interno da PREVCOM','Normas de funcionamento do CD, CF e DIREX','Media','O CD eh o orgao maximo. O CF fiscaliza. A DIREX executa.'],
      [30,'Lei 11.053/2004 e Resolucao Previc 23/2023','Tributacao: progressiva (tabela IR) ou regressiva (35% a 10%). Resolucao Previc define regras para EFPC','Media','No regressivo, a aliquota diminui com o tempo. Opta-se na inscricao.'],
    ]},
    'TI': { cor: '5B9BD5', topicos: [
      ['#', 'Topico', 'Descricao', 'Incidencia', 'Macete'],
      [1,'Ciclo de vida do software','Fases: requisitos, analise, projeto, implementacao, testes, implantacao, manutencao','Muito Alta','Modelos: cascata (sequencial), espiral (iterativo com riscos), incremental (entregas parciais).'],
      [2,'Modelo Cascata','Sequencial: requisitos → projeto → implementacao → testes → manutencao','Alta','Rigido, dificil de mudar. Bom para projetos com requisitos estaveis.'],
      [3,'Modelo Incremental','Entregas parciais ao longo do projeto. Cada incremento agrega funcionalidade','Alta','"Entregar valor mais cedo." Cada incremento passa por todas as fases.'],
      [4,'Modelo Espiral','Iterativo com analise de riscos a cada ciclo','Media','Enfase em riscos. Cada volta da espiral produz um prototipo.'],
      [5,'Metodologias Ageis — Manifesto Agil','4 valores: individuos > processos, software > docs, colaboracao > contrato, responder a mudancas > seguir plano','Muito Alta','VUNESP pergunta: "Qual dos itens faz parte dos valores ageis?"'],
      [6,'Scrum — Papeis','Product Owner (dono do produto), Scrum Master (facilitador), Dev Team (desenvolvedores)','Muito Alta','PO = prioriza o backlog. SM = remove impedimentos. Time = auto-organizado.'],
      [7,'Scrum — Cerimonias','Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective','Alta','Sprint = 2-4 semanas. Daily = 15 min. Review = demonstracao. Retro = melhoria continua.'],
      [8,'Scrum — Artefatos','Product Backlog, Sprint Backlog, Incremento','Alta','Product Backlog = lista priorizada. Sprint Backlog = itens da sprint. Incremento = entregavel pronto.'],
      [9,'Kanban','Quadro visual (To Do, Doing, Done). Limite de WIP (Work in Progress)','Alta','WIP limitado = nao comecar tarefa nova sem terminar as em andamento. Fluxo continuo.'],
      [10,'Extreme Programming (XP)','Praticas: TDD, programacao em par, refatoracao, integracao continua, ritmo sustentavel','Media','"Codigo sempre pronto para entrega." TDD: testa antes de codificar.'],
      [11,'Engenharia de requisitos','Elicitacao, analise, especificacao, validacao, gestao','Muito Alta','Elicitar = levantar com stakeholders. Validar = confirmar se esta correto.'],
      [12,'Requisitos funcionais','Funcoes que o sistema deve executar. "O sistema deve..."','Alta','Ex: "O sistema deve emitir nota fiscal." Descrevem comportamento.'],
      [13,'Requisitos nao-funcionais','Qualidades/restricoes: desempenho, seguranca, usabilidade, escalabilidade','Alta','Ex: "O sistema deve responder em ate 2 segundos."'],
      [14,'Historias de usuario (User Stories)','Formato: "Como [papel], quero [funcionalidade] para [beneficio]"','Alta','Criterios de aceitacao = "Definition of Done".'],
      [15,'Casos de uso (Use Cases)','Diagrama UML. Ator + sistema + fluxo principal + fluxos alternativos','Alta','Ator = quem interage com o sistema. Caso de uso = uma funcionalidade completa.'],
      [16,'UML — Diagrama de Classes','Classes, atributos, metodos, relacionamentos (associacao, heranca, dependencia)','Muito Alta','Heranca = triangulo vazio. Associacao = linha simples. Dependencia = seta tracejada.'],
      [17,'UML — Diagrama de Sequencia','Interacao entre objetos no tempo. Mensagens, lifelines, ativacoes','Alta','Linha vertical = vida do objeto. Seta = mensagem. Caixa = ativacao.'],
      [18,'UML — Diagrama de Casos de Uso','Ator, caso de uso, sistema. Visao geral das funcionalidades','Alta','Nao mostra ordem nem detalhes internos. So o que o sistema faz para cada ator.'],
      [19,'UML — Diagrama de Atividades','Fluxo de atividades. Decisoes, forks, joins','Media','Parece fluxograma. Mostra logica de processo.'],
      [20,'UML — Diagrama de Estado','Ciclo de vida de um objeto. Estados, eventos, transicoes','Media','Ex: Pedido: Novo → Processando → Enviado → Entregue.'],
      [21,'Padroes de Projeto (GoF)','Criacionais (Singleton, Factory), Estruturais (Adapter), Comportamentais (Observer, Strategy)','Alta','Singleton = unica instancia. Factory = cria objetos. Observer = notifica mudancas.'],
      [22,'Arquitetura MVC','Model (dados), View (interface), Controller (controle)','Alta','Separa responsabilidades. VUNESP adora perguntar: "Em qual camada fica a regra de negocio?" (Model).'],
      [23,'Arquitetura em camadas','Apresentacao → Negocio → Persistencia → Banco de Dados','Media','Cada camada se comunica apenas com a adjacente. Baixo acoplamento.'],
      [24,'Testes de software','Unitario (menor parte), Integracao (modulos juntos), Sistema (tudo), Aceitacao (usuario)','Muito Alta','Decore a piramide: base = unitarios (muitos), topo = aceitacao (poucos).'],
      [25,'Qualidade de software (ISO 9126/25010)','Caracteristicas: funcionalidade, confiabilidade, usabilidade, eficiencia, manutenibilidade, portabilidade','Media','A nova norma ISO 25010 substitui a 9126. VUNESP costuma cobrar a 9126.'],
      [26,'Modelo Entidade-Relacionamento (MER)','Entidades, atributos, relacionamentos. Cardinalidade (1:1, 1:N, N:N)','Muito Alta','Entidade = "coisa" do mundo real. Atributo = caracteristica. Relacionamento = ligacao.'],
      [27,'Modelo Relacional','Tabelas, linhas, colunas. Chave primaria (PK), chave estrangeira (FK)','Muito Alta','PK = identificador unico. FK = referencia a outra tabela.'],
      [28,'Normalizacao — 1FN','Atributos atomicos (indivisiveis). Sem grupos repetitivos','Alta','Cada celula = um valor. Sem listas dentro de colunas.'],
      [29,'Normalizacao — 2FN','Dependencia funcional total da chave. Remover dependencias parciais','Alta','Toda coluna nao-chave deve depender da chave COMPLETA.'],
      [30,'Normalizacao — 3FN','Dependencia transitiva. Remover colunas que dependem de outras nao-chave','Alta','"A coluna X depende da coluna Y, que nao eh chave." Separar em outra tabela.'],
      [31,'Modelagem dimensional','Star schema (tabela fato + tabelas dimensao). Data Warehouse','Media','Fato = medidas (vendas, quantidade). Dimensao = contexto (tempo, produto, cliente).'],
      [32,'NoSQL — Tipos','Documento (MongoDB), Chave-Valor (Redis), Colunas (Cassandra), Grafos (Neo4j)','Alta','NoSQL = Not Only SQL. Nao relacional. Escalabilidade horizontal.'],
      [33,'DDL — Data Definition Language','CREATE, ALTER, DROP, TRUNCATE','Muito Alta','CREATE = criar tabela/banco. ALTER = modificar. DROP = excluir. TRUNCATE = limpar.'],
      [34,'DML — Data Manipulation Language','SELECT, INSERT, UPDATE, DELETE','Muito Alta','INSERT INTO, UPDATE SET, DELETE FROM. SELECT = o mais cobrado.'],
      [35,'SELECT — Clausulas','WHERE, GROUP BY, HAVING, ORDER BY','Muito Alta','WHERE = filtro antes do grupo. HAVING = filtro depois do grupo.'],
      [36,'JOINs','INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN','Muito Alta','INNER = so registros correspondentes. LEFT = todos da esquerda + correspondentes a direita.'],
      [37,'Subconsultas','SELECT dentro de SELECT. Correlacionadas e nao correlacionadas','Media','Subconsulta pode retornar valor unico (escalar), linha, ou tabela.'],
      [38,'Funcoes de agregacao','COUNT, SUM, AVG, MAX, MIN','Alta','COUNT(*) = total de linhas. AVG = media. GROUP BY + agregacao = padrao.'],
      [39,'Indices','Aceleram consultas. Clusterizado (ordena dados) e nao clusterizado','Media','Indice = catalogo. Muitos indices = lentidao em INSERT/UPDATE.'],
      [40,'Transacoes ACID','Atomicidade, Consistencia, Isolamento, Durabilidade','Alta','Atomicidade = tudo ou nada. Isolamento = transacoes simultaneas nao interferem.'],
      [41,'Backup e Recovery','Full (tudo), Diferencial (desde o ultimo full), Incremental (desde o ultimo backup)','Alta','Recovery = restaurar dados apos falha. WAL = log antes da escrita.'],
      [42,'SGBD','Oracle, SQL Server, MySQL, PostgreSQL, MongoDB','Alta','PostgreSQL = open source avancado. MySQL = popular. Oracle = corporativo.'],
      [43,'Big Data — Conceitos','4 Vs: Volume, Velocidade, Variedade, Veracidade. Hadoop, Spark, Hive','Media','Hadoop = HDFS + MapReduce. Spark = processamento em memoria (mais rapido).'],
      [44,'Data Warehouse e Data Lake','DW = dados estruturados, modelados para analise. Data Lake = dados brutos, qualquer formato','Media','DW = pronto para BI. Data Lake = "guarda tudo", depois organiza.'],
      [45,'ETL vs ELT','Extract, Transform, Load (transforma antes de carregar). ELT (carrega depois transforma)','Media','ETL = tradicional. ELT = mais comum em Big Data (processa dentro do banco).'],
      [46,'Modelo OSI','7 camadas: Fisica, Enlace, Rede, Transporte, Sessao, Apresentacao, Aplicacao','Muito Alta','Mnemônico: "Fisica Enlace Rede Transporte Sessao Apresentacao Aplicacao" ou "FERA no Tunel S/A"'],
      [47,'Modelo TCP/IP','4 camadas: Acesso a Rede (Enlace), Internet (Rede), Transporte, Aplicacao','Muito Alta','Nao confundir com OSI (7 camadas). TCP/IP = modelo da internet.'],
      [48,'Enderecamento IPv4','Classes A, B, C. Mascara de sub-rede. CIDR (ex: /24)','Muito Alta','Classe A: 1-126. B: 128-191. C: 192-223. /24 = 255.255.255.0.'],
      [49,'Enderecamento IPv6','128 bits, hexadecimal, 8 grupos. :: para zeros consecutivos','Media','IPv6 = 2^128 enderecos. Nao tem NAT como padrao.'],
      [50,'Sub-rede e CIDR','Dividir rede em sub-redes. Mascara variavel','Alta','Calcular: 2^(bits de sub-rede) = numero de sub-redes.'],
      [51,'HTTP/HTTPS','HTTP = 80, HTTPS = 443. GET, POST, PUT, DELETE. Codigos: 200 (OK), 404, 500','Muito Alta','HTTPS = HTTP + SSL/TLS. Criptografado.'],
      [52,'DNS','Traduz nomes de dominio para IP. Porta 53. Hierarquico','Alta','Raiz → .com, .br → google.com. Cache DNS acelera.'],
      [53,'DHCP','Atribui IP automaticamente. Portas 67/68. DORA: Discover, Offer, Request, Acknowledge','Alta','Decore DORA. Concede IP por leasing (aluguel).'],
      [54,'SMTP, POP3, IMAP','SMTP (envio, 25), POP3 (download, 110), IMAP (sincronizacao, 143)','Alta','SMTP envia; POP3 baixa e apaga; IMAP mantem no servidor.'],
      [55,'FTP/TFTP','FTP = transferencia de arquivos (20/21). TFTP = trivial, sem autenticacao (69)','Media','FTP tem controle (21) e dados (20). TFTP eh mais simples.'],
      [56,'TCP vs UDP','TCP = orientado a conexao, confiavel, ordenado. UDP = nao confiavel, rapido, sem conexao','Muito Alta','TCP usado em HTTP, email. UDP usado em streaming, VoIP, DNS.'],
      [57,'NAT (Network Address Translation)','Traduz IP privado para publico. Permite que varios dispositivos compartilhem um IP','Media','NAT economiza IPv4. Mascara IP interno na saida para internet.'],
      [58,'Equipamentos de rede','Hub (fisico), Switch (enlace), Roteador (rede), Firewall (seguranca)','Alta','Hub = repete sinal. Switch = comuta quadros. Roteador = encaminha pacotes.'],
      [59,'VLAN','Redes virtuais dentro de um switch. Isolamento logico. 802.1Q','Media','VLAN = dominio de broadcast separado. Tags nos quadros.'],
      [60,'VPN','Tunel criptografado sobre rede publica. PPTP, L2TP, IPSec, OpenVPN','Alta','VPN = seguranca em transito. IPSec eh o mais seguro.'],
      [61,'Pilares da Seguranca (CIDA)','Confidencialidade, Integridade, Disponibilidade, Autenticidade','Muito Alta','Confidencialidade = so quem pode ver. Integridade = nao alterado. Disponibilidade = acessivel.'],
      [62,'ISO 27001','SGSI — Sistema de Gestao de Seguranca da Informacao. Certificavel','Alta','Requer: politica de seguranca, avaliacao de riscos, melhoria continua (PDCA).'],
      [63,'ISO 27002','Guia de boas praticas. Codigo de pratica. Nao certificavel','Media','Complementa a 27001. Recomenda controles especificos.'],
      [64,'ISO 27005','Gestao de riscos de seguranca da informacao','Baixa','Risco = ameaca x vulnerabilidade x impacto.'],
      [65,'Criptografia simetrica','Mesma chave para cifrar e decifrar. AES, DES, 3DES, Blowfish','Alta','Rapida, mas problema de compartilhamento de chave. AES = padrao atual.'],
      [66,'Criptografia assimetrica','Par de chaves: publica (cifra) e privada (decifra). RSA, ECC','Alta','Mais segura, mais lenta. Usada em certificacao digital e SSL/TLS.'],
      [67,'Funcao hash','MD5, SHA-1, SHA-256. Unidirecional. Usada para integridade e senhas','Alta','Hash nao pode ser revertido. MD5 e SHA-1 sao inseguros (colisoes).'],
      [68,'Certificacao Digital — ICP-Brasil','AC (Autoridade Certificadora) emite, AR valida. A3 (token/cartao)','Alta','ICP-Brasil = infraestrutura de chave publica brasileira. Padrao: X.509.'],
      [69,'Assinatura digital','Hash + criptografia assimetrica. Garante autenticidade e irretratabilidade','Alta','Assinar = cifrar o hash com a chave privada. Verificar = decifrar com a chave publica.'],
      [70,'OWASP Top 10','SQL Injection, XSS, CSRF, Broken Authentication','Alta','SQL Injection = inserir SQL malicioso. XSS = script malicioso no navegador.'],
      [71,'Tipos de malware','Virus (hospedeiro), Worm (autonomo), Trojan (falso), Ransomware (sequestro), Spyware (espionagem)','Alta','Worm se propaga sem intervencao. Trojan parece legitimo.'],
      [72,'Ataques comuns','Phishing (engana usuario), DDoS (sobrecarga), Brute Force (tenta senhas), MITM (intercepta)','Alta','Phishing = email falso. DDoS = muitos acessos simultaneos.'],
      [73,'Firewall','Filtra trafego com base em regras. Pode ser de rede, aplicacao, estado','Alta','Firewall de estado = Stateful Inspection. WAF = Web Application Firewall.'],
      [74,'LGPD — Lei 13.709/2018','Dados pessoais, consentimento, direitos do titular. Sancoes: multa de ate 2% do faturamento','Media','Dado pessoal = identifica a pessoa. Dado sensivel = raca, religiao, saude.'],
      [75,'Backup — Estrategias','Completo, Diferencial, Incremental. Regra 3-2-1: 3 copias, 2 midias, 1 offsite','Alta','3-2-1 = padrao ouro. Testar restore periodicamente.'],
      [76,'ITIL 4 — Praticas','Gerenciamento de Incidente, Problema, Mudanca, Nivel de Servico, Catalogo de Servico','Alta','Incidente = interrompe servico. Problema = causa raiz. Mudanca = alteracao controlada.'],
      [77,'ITIL 4 — Service Desk','Central de atendimento. Funcao: registrar, categorizar, priorizar, resolver ou escalar incidentes','Alta','Service Desk ≠ Help Desk. Service Desk eh mais estrategico.'],
      [78,'COBIT 2019','Governanca corporativa de TI. Objetivos de controle. EDM (Avaliar, Dirigir, Monitorar)','Media','COBIT = foco em governanca (controles). ITIL = foco em servicos (processos).'],
      [79,'PMBOK — Areas de conhecimento','Escopo, Tempo, Custo, Qualidade, RH, Comunicacao, Riscos, Aquisições','Alta','Decore as 10 areas. Exame: "Qual area gerencia os prazos?" (Tempo).'],
      [80,'PMBOK — Grupos de processos','Iniciacao, Planejamento, Execucao, Monitoramento/Controle, Encerramento','Alta','Todo projeto passa por esses 5 grupos. Nao sao fases, sao processos.'],
      [81,'BPM (Business Process Management)','Gerenciamento de processos de negocio. Ciclo: modelar, executar, monitorar, otimizar','Media','BPMN = notacao para modelar processos. Elementos: evento, atividade, gateway.'],
      [82,'Contratacao de TI — IN 04/2014 (SLTI)','Fases: planejamento, selecao de fornecedor, gestao do contrato','Baixa','Planejar antes de contratar. Analise de viabilidade. Equipe de planejamento.'],
      [83,'MPS-BR (Melhoria de Processo do Software Brasileiro)','Niveis: G (parcial) → F (gerenciado) → E (definido) → D → C → B → A (otimizacao)','Baixa','Modelo brasileiro baseado em CMMI. 7 niveis de maturidade.'],
      [84,'E-PING / E-MAG','E-PING = padroes de interoperabilidade. E-MAG = modelo de acessibilidade governamental','Baixa','E-PING conecta sistemas publicos. E-MAG torna sites acessiveis.'],
      [85,'Controle de versao — Git','Commit, branch, merge, pull, push. GitHub, GitLab','Alta','Git = distribuido. Branch = ramificacao paralela. Merge = unir branches.'],
      [86,'Linux — Comandos essenciais','ls, cd, mkdir, rm, cp, mv, chmod, chown, grep, ps, kill, systemctl','Alta','chmod 755 = dono tudo, grupo leitura/execucao, outros leitura/execucao. grep = filtrar texto.'],
      [87,'Linux — Permissoes','rwx (leitura, escrita, execucao). Dono, Grupo, Outros. 4 (r), 2 (w), 1 (x)','Alta','Mnemônico: ugo (user, group, others). 755 = rwxr-xr-x.'],
      [88,'Processos — Estados e Escalonamento','Novo, Pronto, Executando, Bloqueado, Terminado. FIFO, SJF, Round-Robin','Media','Round-Robin = cada processo recebe um quantum de tempo.'],
      [89,'Windows Server — AD, DNS, DHCP','Active Directory = diretorio de usuarios e recursos. GPO = politicas de grupo','Media','AD usa LDAP e Kerberos. GPO aplica configuracoes em massa.'],
      [90,'Virtualizacao','Hypervisor: Tipo 1 (bare-metal: VMware ESXi, Hyper-V) e Tipo 2 (hospedado: VirtualBox)','Media','Tipo 1 = roda direto no hardware (servidores). Tipo 2 = roda sobre SO (estacoes).'],
    ]},
  };

  for (const [nome, data] of Object.entries(materias)) {
    const ws = wb.addWorksheet(nome, { views: [{ state: 'frozen', ySplit: 1 }] });
    const rows = data.topicos;
    
    // Column widths
    ws.getColumn(1).width = 6;
    ws.getColumn(2).width = 35;
    ws.getColumn(3).width = 55;
    ws.getColumn(4).width = 14;
    ws.getColumn(5).width = 65;

    // Style header
    const headerStyle = {
      font: { bold: true, color: { argb: 'FFFFFFFF' }, size: 11 },
      fill: { type: 'pattern', pattern: 'solid', fgColor: { argb: data.cor } },
      alignment: { vertical: 'middle', horizontal: 'center', wrapText: true },
      border: { top: { style: 'thin' }, bottom: { style: 'thin' }, left: { style: 'thin' }, right: { style: 'thin' } }
    };

    // Style data
    const dataStyle = {
      font: { size: 10 },
      alignment: { vertical: 'top', wrapText: true },
      border: { top: { style: 'thin' }, bottom: { style: 'thin' }, left: { style: 'thin' }, right: { style: 'thin' } }
    };

    const altFill = { type: 'pattern', pattern: 'solid', fgColor: { argb: 'FFF2F2F2' } };

    for (let i = 0; i < rows.length; i++) {
      const row = ws.addRow(rows[i]);
      if (i === 0) {
        row.eachCell((cell) => { cell.style = headerStyle; });
        row.height = 25;
      } else {
        row.eachCell((cell) => {
          cell.style = dataStyle;
          if (i % 2 === 0) cell.fill = altFill;
        });
        row.height = 35;
        // Center the # and Incidencia columns
        row.getCell(1).alignment = { vertical: 'top', horizontal: 'center' };
        row.getCell(4).alignment = { vertical: 'top', horizontal: 'center', wrapText: true };
      }
    }
  }

  await wb.xlsx.writeFile('C:\\Prevcom\\macetes-vunesp-analista-ti-prevcom.xlsx');
  console.log('XLSX gerado com sucesso!');
}

gerarXLSX().catch(console.error);
