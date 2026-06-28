"""Builds programmatic_flashcards.py - part 2: verbs + crase + punctuation + figures"""
import os

path = r'D:\Prevcom\prevcom_app\programmatic_flashcards.py'

def write(s):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(s + '\n')

# Irregular verbs
write('''    verbos_irregulares = [
        ("ser", "sou, es, e, somos, sois, sao"),
        ("estar", "estou, estas, esta, estamos, estais, estao"),
        ("ter", "tenho, tens, tem, temos, tendes, tem"),
        ("vir", "venho, vens, vem, vimos, vindes, vem"),
        ("poder", "posso, podes, pode, podemos, podeis, podem"),
        ("fazer", "faco, fazes, faz, fazemos, fazeis, fazem"),
        ("dizer", "digo, dizes, diz, dizemos, dizeis, dizem"),
        ("trazer", "trago, trazes, traz, trazemos, trazeis, trazem"),
        ("saber", "sei, sabes, sabe, sabemos, sabeis, sabem"),
        ("querer", "quero, queres, quer, queremos, quereis, querem"),
        ("ver", "vejo, ves, ve, vemos, vedes, veem"),
        ("ouvir", "ouco, ouves, ouve, ouvimos, ouvis, ouvem"),
        ("perder", "perco, perdes, perde, perdemos, perdeis, perdem"),
        ("medir", "meco, medes, mede, medimos, medis, medem"),
        ("pedir", "peco, pedes, pede, pedimos, pedis, pedem"),
        ("seguir", "sigo, segues, segue, seguimos, seguis, seguem"),
        ("sentir", "sinto, sentes, sente, sentimos, sentis, sentem"),
        ("dormir", "durmo, dormes, dorme, dormimos, dormis, dormem"),
        ("ir", "vou, vas, vai, vamos, ides, vao"),
        ("dar", "dou, das, da, damos, dais, dao"),
        ("ler", "leio, les, le, lemos, ledes, leem"),
        ("crer", "creio, cres, cre, cremos, credes, creem"),
        ("rir", "rio, ris, ri, rimos, rides, riem"),
        ("cair", "caio, cais, cai, caimos, cais, caem"),
        ("valer", "valho, vales, vale, valemos, valeis, valem"),
        ("caber", "cabo, cabes, cabe, cabemos, cabeis, cabem"),
    ]
    for verbo, conjugacao in verbos_irregulares:
        LP.append((f"Conjugacao de '{verbo}' no presente do indicativo", conjugacao))

    verbos_preterito = [
        ("ser/ir", "fui, foste, foi, fomos, fostes, foram"),
        ("estar", "estive, estiveste, esteve, estivemos, estivestes, estiveram"),
        ("ter", "tive, tiveste, teve, tivemos, tivestes, tiveram"),
        ("fazer", "fiz, fizeste, fez, fizemos, fizestes, fizeram"),
        ("dizer", "disse, disseste, disse, dissemos, dissestes, disseram"),
        ("poder", "pude, pudeste, pode, pudemos, pudestes, puderam"),
        ("trazer", "trouxe, trouxeste, trouxe, trouxemos, trouxestes, trouxeram"),
        ("saber", "soube, soubeste, soube, soubemos, soubestes, souberam"),
        ("querer", "quis, quiseste, quis, quisemos, quisestes, quiseram"),
        ("ver", "vi, viste, viu, vimos, vistes, viram"),
        ("vir", "vim, vieste, veio, viemos, viestes, vieram"),
        ("dar", "dei, deste, deu, demos, destes, deram"),
        ("ler", "li, leste, leu, lemos, lestes, leram"),
        ("caber", "coube, coubeste, coube, coubemos, coubestes, couberam"),
    ]
    for verbo, conjugacao in verbos_preterito:
        LP.append((f"Conjugacao de '{verbo}' no preterito perfeito do indicativo", conjugacao))

    verbos_futuro = [
        ("ser", "serei, seras, sera, seremos, sereis, serao"),
        ("estar", "estarei, estaras, estara, estaremos, estareis, estarao"),
        ("ter", "terei, teras, tera, teremos, tereis, terao"),
        ("fazer", "farei, faras, fara, faremos, fareis, farao"),
        ("dizer", "direi, diras, dira, diremos, direis, dirao"),
        ("poder", "poderei, poderas, podera, poderemos, podereis, poderao"),
        ("trazer", "trarei, traras, trara, traremos, trareis, trarao"),
        ("saber", "saberei, saberas, sabera, saberemos, sabereis, saberao"),
        ("querer", "querrei, querras, querra, querremos, querreis, querrao"),
        ("ver", "verei, veras, vera, veremos, vereis, verao"),
        ("vir", "virei, viras, vira, viremos, vireis, virao"),
        ("dar", "darei, daras, dara, daremos, dareis, darao"),
        ("ler", "lerei, leras, lera, leremos, lereis, lerao"),
        ("caber", "caberei, caberas, cabera, caberemos, cabereis, caberao"),
        ("ir", "irei, iras, ira, iremos, ireis, irao"),
    ]
    for verbo, conjugacao in verbos_futuro:
        LP.append((f"Conjugacao de '{verbo}' no futuro do presente do indicativo", conjugacao))
''')

# Crase rules
write('''    crase_regras = [
        ("Crase facultativa: pronome possessivo feminino", "Facultativa: 'Entreguei a (a) minha irma.' Ambas aceitaveis."),
        ("Crase obrigatoria: nomes de lugares femininos", "Obrigatoria se admite 'a': 'Fui a Franca.' (voltei DA Franca) vs 'Fui a Lisboa.' (voltei DE Lisboa)"),
        ("Crase proibida: nomes de santas", "Nunca: 'Fiz promessa a Santa Aparecida.'"),
        ("Crase proibida: 'a' + verbo", "Nunca: 'Passei a estudar', 'Ficou a ver navios'."),
        ("Crase proibida: 'casa' sem especificador", "Nunca: 'Voltei a casa.' Especifico: 'Fui a casa da Maria' (tem crase)."),
        ("Crase proibida: 'terra' oposicao bordo", "Nunca: 'Voltaram a terra.' Especifico: 'Fui a terra do meu pai' (tem crase)."),
        ("Crase proibida: palavras repetidas", "Nunca: 'Frente a frente', 'Cara a cara', 'Gota a gota'."),
        ("Crase: locucao adverbial de modo", "Com crase: 'as claras', 'as escondidas', 'as custas'."),
        ("Crase: locucao adverbial de tempo", "Com crase: 'as vezes', 'as dez horas', 'a tarde' (quando=duracao)."),
        ("Crase: locucao prepositiva", "Com crase: 'a fim de', 'a partir de', 'a base de', 'a merce de'."),
        ("Crase: 'aquele/aquela/aquilo'", "Obrigatoria: 'Refiro-me aquela situacao.' (a + aquela)"),
        ("Crase: 'ate' facultativa", "Facultativa: 'Fui ate a praia' ou 'Fui ate a praia'."),
        ("Crase: antes de numerais", "Nao ha crase, exceto horas: 'As 14h' tem crase."),
        ("Crase: 'a distancia'", "Sem crase se indeterminada. Com crase se especificada: 'A distancia de 10km'."),
    ]
    LP.extend(crase_regras)
''')

# Punctuation
write('''    pontuacao = [
        ("Virgula: adjuntos adverbiais deslocados", "Isolados por virgula: 'Ontem, fui ao teatro.'"),
        ("Virgula: enumeracao", "Separa itens de mesma funcao: 'Comprei pao, leite, queijo.'"),
        ("Virgula: elipse do verbo", "Indica omissao: 'Eu gosto de cafe; ela, de cha.'"),
        ("Virgula: oracao adjetiva explicativa", "Ex: 'O presidente, que assinou o decreto, viajou.'"),
        ("Virgula: oracao coordenada assindetica", "Ex: 'Chegou, viu, venceu.'"),
        ("Virgula: zeugma", "Ex: 'Ela prefere praia; ele, montanha.'"),
        ("Ponto final: encerramento", "Encerra periodo declarativo: 'O estudo e importante.'"),
        ("Ponto de interrogacao", "Pergunta direta: 'Voce estudou?'"),
        ("Ponto de exclamacao", "Surpresa, admiração, ordem: 'Que otimo!'"),
        ("Dois-pontos: citacao", "Introduz fala: 'Ele disse: Estou cansado.'"),
        ("Dois-pontos: explicacao", "Introduz esclarecimento: 'Nao fui: estava doente.'"),
        ("Dois-pontos: enumeracao", "Ex: 'Faltam tres itens: foco, disciplina, persistencia.'"),
        ("Ponto e virgula: itens de lei", "Separa itens em artigos de lei e enumeracoes complexas."),
        ("Ponto e virgula: oracoes longas", "Separa oracoes extensas que ja contem virgulas internas."),
        ("Aspas: citacao textual", "Ex: 'Conforme disse o autor: A educacao e a arma mais poderosa.'"),
        ("Aspas: estrangeirismo", "Ex: 'O feedback' ou sem aspas (consagrado)."),
        ("Aspas: destaque de palavra", "Ex: 'O termo compliance refere-se a conformidade.'"),
        ("Travessao: fala de personagem", "Ex: 'Nao estou bem' disse o medico."),
        ("Travessao duplo: intercalacao", "Ex: 'O candidato - e todos os presentes - concordaram.'"),
        ("Parenteses: explicacao", "Ex: 'A LGPD (Lei 13.709/2018) entrou em vigor em 2020.'"),
        ("Reticencias: interrupcao", "Ex: 'Eu so queria dizer...' (deixou no ar)."),
        ("Reticencias: suspense", "Ex: 'E de repente, a porta se abriu...'"),
    ]
    LP.extend(pontuacao)
''')

# Figures of speech
write('''    figuras = [
        ("Sinestesia", "Mistura de sentidos: 'Cores quentes', 'Som azedo', 'Olhar doce'."),
        ("Elipse", "Omissao de termo: 'No quarto, apenas o silencio.' (havia)"),
        ("Zeugma", "Elipse de termo ja expresso: 'Ele gosta de musica; ela, de pintura.'"),
        ("Assindeto", "Ausencia de conectivos: 'Vim, vi, venci.'"),
        ("Polissindeto", "Repeticao de conectivos: 'E canta, e chora, e ri.'"),
        ("Anafora", "Repeticao no inicio: 'Amei o mar, amei a vida, amei tudo.'"),
        ("Epistrofe", "Repeticao no fim: 'Ela estuda, trabalha, vive muito.'"),
        ("Anadiplose", "Fim de uma no inicio da outra: 'So quem tem poder agride. Agride e destroi.'"),
        ("Pleonasmo", "Repeticao enfatica: 'Vi com meus proprios olhos.'"),
        ("Polipoto", "Variacao morfologica: 'O amor que ama e sofre.'"),
        ("Paronomasia", "Palavras parecidas: 'Quem cospe no ceu, na cara lhe cai.'"),
        ("Onomatopeia", "Som: 'tique-taque', 'cocorico', 'atchim'."),
        ("Aliteracao", "Repeticao de consoantes: 'O rato roeu a roupa do rei de Roma.'"),
        ("Assonancia", "Repeticao de vogais: 'A marola e a viola'."),
        ("Pleonasmo vicioso", "Repeticao desnecessaria: 'subir para cima', 'entrar para dentro'."),
        ("Metafora x comparacao", "Metafora: sem conectivo. Comparacao: com 'como', 'tal qual'."),
        ("Metonimia x catacrese", "Metonimia: substituicao poetica. Catacrese: metafora desgastada."),
        ("Paradoxo x antitese", "Paradoxo: ideias contraditorias. Antitese: ideias opostas."),
        ("Apelacao a autoridade", "Usa citacao de autoridade para validar ideia."),
        ("Apelacao a emocao", "Apela aos sentimentos do receptor."),
    ]
    LP.extend(figuras)
''')

# Prepositions and conjunctions
write('''    prep_relacoes = [
        ("Preposicao 'a' - destino", "Ex: 'Fui a escola.' Direcao/destino."),
        ("Preposicao 'com' - companhia", "Ex: 'Sai com amigos.' Companhia/instrumento."),
        ("Preposicao 'de' - origem", "Ex: 'Sou de SP.' Origem, posse, materia."),
        ("Preposicao 'em' - lugar", "Ex: 'Estou em casa.' Lugar, tempo, meio."),
        ("Preposicao 'para' - finalidade", "Ex: 'Estudo para passar.' Finalidade/direcao."),
        ("Preposicao 'por' - causa", "Ex: 'Nao fui por doenca.' Causa, meio, autoria."),
        ("Preposicao 'sem' - ausencia", "Ex: 'Sai sem dinheiro.' Privacao/exclusao."),
        ("Preposicao 'sob' - subordinacao", "Ex: 'Trabalho sob pressao.' Subordinacao."),
        ("Preposicao 'sobre' - assunto", "Ex: 'Falamos sobre o projeto.' Assunto/posicao."),
        ("Preposicao 'entre' - intervalo", "Ex: 'Entre 10h e 11h.' Intervalo."),
    ]
    LP.extend(prep_relacoes)

    conjuncoes = [
        ("Conjuncao aditiva: 'e'/'nem'", "Soma: 'Estudou e passou.' Negativa: 'Nem estudou.'"),
        ("Conjuncao adversativa: 'mas'/'porem'", "Oposicao: 'Quis ir, mas nao pude.' 'Estudou, porem nao passou.'"),
        ("Conjuncao alternativa: 'ou'/'ora...ora'", "Alternancia: 'Ou estuda ou trabalha.' 'Ora ria, ora chorava.'"),
        ("Conjuncao conclusiva: 'logo'/'portanto'", "Conclusao: 'Estudou, logo passou.' 'Choveu, portanto nao fui.'"),
        ("Conjuncao explicativa: 'porque'/'pois'", "Explicacao: 'Nao fui, pois estava doente.'"),
        ("Conjuncao causal: 'porque'/'ja que'", "Causa: 'Chorou porque caiu.' 'Ja que esta cansado, descanse.'"),
        ("Conjuncao condicional: 'se'/'caso'", "Condicao: 'Se estudar, passara.' 'Caso chova, nao irei.'"),
        ("Conjuncao concessiva: 'embora'/'ainda que'", "Concessao: 'Embora cansado, foi.' 'Ainda que chova, irei.'"),
        ("Conjuncao temporal: 'quando'/'enquanto'", "Tempo: 'Quando chegar, avise.' 'Enquanto estudava, ouvia musica.'"),
        ("Conjuncao final: 'para que'/'a fim de que'", "Finalidade: 'Estudou para que passasse.'"),
        ("Conjuncao consecutiva: 'tanto...que'", "Consequencia: 'Estudou tanto que passou.'"),
        ("Conjuncao comparativa: 'como'", "Comparacao: 'Estuda como um guerreiro.'"),
        ("Conjuncao conformativa: 'conforme'/'segundo'", "Conformidade: 'Fez conforme foi orientado.'"),
        ("Conjuncao proporcional: 'a medida que'", "Proporcao: 'A medida que estudava, aprendia.'"),
    ]
    LP.extend(conjuncoes)
''')

# Pronouns
write('''    pronomes = [
        ("Pronome pessoal reto: 'eu'/'tu'/'ele'", "Sujeito: 'Eu estudo.' 'Tu estudas.' 'Ele estuda.'"),
        ("Pronome obliquo atomo: 'me'/'te'/'se'", "Sem prep.: 'Ele me viu.' 'Eu te amo.' 'Ele se cortou.'"),
        ("Pronome obliquo atomo: 'lhe'/'o'/'a'", "'Dei-lhe um livro.' 'Vi-o ontem.' 'Chamei-a.'"),
        ("Pronome obliquo tonico: 'mim'/'ti'/'si'", "Com prep.: 'Isso e para mim.' 'Falou de si.'"),
        ("Pronome obliquo: 'consigo'", "Reflexivo: 'Trouxe o documento consigo.'"),
        ("Pronome demonstrativo: 'este/esse/aquele'", "Prox./med./dist.: 'Este aqui', 'Esse ai', 'Aquele la'."),
        ("Pronome demonstrativo: 'isto/isso/aquilo'", "Invariáveis: 'Isto e meu.' 'Isso e seu.' 'Aquilo e dele.'"),
        ("Pronome demonstrativo neutro: 'o/a'", "Equivale a 'aquilo': 'Nao entendi o que ele disse.'"),
        ("Pronome relativo: 'que'/'o qual'", "'O livro que li e otimo.' 'O livro o qual li...'"),
        ("Pronome relativo: 'cujo'", "Posse: 'O autor cujo livro li e famoso.'"),
        ("Pronome relativo: 'onde'/'quando'/'como'", "'A casa onde moro.' 'O dia quando te vi.' 'O modo como fez.'"),
        ("Pronome indefinido: 'alguem'/'ninguem'", "'Alguem ligou.' 'Ninguem veio.'"),
        ("Pronome indefinido: 'tudo'/'nada'/'cada'", "'Ele faz tudo.' 'Nada o abala.' 'Cada um sabe.'"),
        ("Pronome indefinido: 'qualquer'/'outrem'", "'Qualquer pessoa pode.' 'Nao fale de outrem.'"),
        ("Pronome interrogativo: 'quem'/'que'/'qual'", "'Quem esta ai?' 'Que quer?' 'Qual e seu nome?'"),
        ("Pronome interrogativo: 'quanto'", "Quantidade: 'Quanto custa?'"),
    ]
    LP.extend(pronomes)
''')

# Adverbs, numerals, interjections, word formation
write('''    adverbios = [
        ("Advrbio de modo: 'bem'/'mal'/'depressa'/'devagar'", "'Canta bem.' 'Sente-se mal.' 'Fale depressa.' 'Ande devagar.'"),
        ("Advrbio de lugar: 'aqui'/'ai'/'la'/'acola'", "'Venha aqui.' 'Fique ai.' 'Vamos la.' 'Esta acola.'"),
        ("Advrbio de lugar: 'perto'/'longe'/'dentro'/'fora'", "'Moro perto.' 'Fica longe.' 'Entre dentro.' 'Sai fora.'"),
        ("Advrbio de tempo: 'hoje'/'ontem'/'amanha'", "'Hoje e o dia.' 'Ontem choveu.' 'Amanha vou.'"),
        ("Advrbio de tempo: 'cedo'/'tarde'/'ja'/'ainda'", "'Acordo cedo.' 'Chegou tarde.' 'Ja estudei.' 'Ainda nao.'"),
        ("Advrbio de tempo: 'sempre'/'nunca'", "'Sempre estudo.' 'Nunca desista.'"),
        ("Advrbio de intensidade: 'muito'/'pouco'/'demais'", "'Estudei muito.' 'Dormi pouco.' 'Trabalhei demais.'"),
        ("Advrbio de intensidade: 'bastante'/'tanto'/'quase'/'apenas'", "'Comi bastante.' 'Chorou tanto.' 'Quase cai.' 'Apenas olhou.'"),
        ("Advrbio de afirmacao: 'sim'/negacao: 'nao'", "'Sim, vou.' 'Nao, obrigado.'"),
        ("Advrbio de duvida: 'talvez'/'provavelmente'/'acaso'/'porventura'", "'Talvez va.' 'Provavelmente sim.' 'Acaso ele veio?'"),
    ]
    LP.extend(adverbios)

    numerais = [
        ("Numeral cardinal: 'um'/'dois'", "Quantidade: 'Um livro.' 'Dois carros.'"),
        ("Numeral ordinal: 'primeiro'/'segundo'", "Ordem: 'Primeiro lugar.' 'Segundo colocado.'"),
        ("Numeral multiplicativo: 'dobro'/'triplo'/'quadruplo'/'quintuplo'", "'Dobro de 5=10.' 'Triplo de 3=9.' 'Quadruplo de 2=8.' 'Quintuplo de 4=20.'"),
        ("Numeral fracionario: 'metade'/'terco'/'quarto'", "'Metade de 10=5.' 'Terco de 9=3.' 'Quarto de 100=25.'"),
        ("Numeral coletivo: 'dezena'/'centena'/'milhar'/'milhao'", "'Uma dezena' (10). 'Centena' (100). 'Milhar' (1000). 'Milhao' (1M)."),
        ("Numeral: flexao de genero", "Cardinais invariáveis: 'um/uma', 'dois/duas'."),
        ("Numeral: algarismos romanos", "I=1, V=5, X=10, L=50, C=100, D=500, M=1000."),
    ]
    LP.extend(numerais)

    interjeicoes = [
        ("Interjeicao de alegria: 'Oba!'", "Exprime alegria."),
        ("Interjeicao de alerta: 'Cuidado!'", "Exprime alerta/perigo."),
        ("Interjeicao de alivio: 'Ufa!'", "Exprime alivio."),
        ("Interjeicao de animacao: 'Forca!'", "Exprime incentivo."),
        ("Interjeicao de aplauso: 'Bravo!'", "Exprime aprovacao."),
        ("Interjeicao de chamamento: 'Psiu!'", "Solicita atencao."),
        ("Interjeicao de dor: 'Ai!'", "Exprime dor fisica."),
        ("Interjeicao de espanto: 'Nossa!'", "Exprime surpresa."),
        ("Interjeicao de desejo: 'Oxala!'", "Exprime desejo: 'Oxala eu passe!'"),
        ("Interjeicao: locucao interjetiva", "'Meu Deus!', 'Valha-me Deus!', 'Pelo amor de Deus!'"),
    ]
    LP.extend(interjeicoes)

    formacao = [
        ("Derivacao prefixal: 'in-'/'des-'/'re-'", "Neg/rep: 'infeliz', 'desfazer', 'refazer'."),
        ("Derivacao prefixal: 'pre-'/'sub-'/'super-'/'inter-'", "'prever', 'submarino', 'supermercado', 'internacional'."),
        ("Derivacao sufixal: '-mente'/'-dade'/-cao'", "'felizmente', 'bondade', 'educacao'."),
        ("Derivacao sufixal: '-eiro'/'-ista'/'-vel'", "'pedreiro', 'dentista', 'viavel'."),
        ("Derivacao sufixal: '-inho'/-zao'", "Diminutivo: 'casinha'. Aumentativo: 'paredao'."),
        ("Derivacao parassintetica", "Pref+rad+suf simultaneo: 'entristecer', 'anoitecer'."),
        ("Composicao: justaposicao", "Sem perda: 'guarda-chuva', 'passatempo'."),
        ("Composicao: aglutinacao", "Com perda: 'planalto' (plano+alto), 'vinagre' (vinho+acre)."),
        ("Abreviacao/siglas", "'foto' (fotografia). Siglas: INSS, SUS, ONU, STF."),
        ("Neologismo/arcaismo/hibridismo", "Novas: 'printar'. Antigas: 'botica'. Hibridas: 'automovel'."),
    ]
    LP.extend(formacao)
''')

# Syntax, voices, concordancia, regencia
write('''    sintaxe = [
        ("Sujeito simples", "Um nucleo: 'O funcionario entregou o relatorio.'"),
        ("Sujeito composto", "Dois+ nucleos: 'O gerente e o analista aprovaram.'"),
        ("Sujeito oculto/desinencial", "Identificado pela desinencia: 'Entregamos o relatorio.' (nos)"),
        ("Sujeito indeterminado: 3a plural", "Verbo 3a plural: 'Falaram mal de voce.'"),
        ("Sujeito indeterminado: indice SE", "VTI+SE+3a sing: 'Precisa-se de funcionarios.'"),
        ("Sujeito inexistente: impessoais", "Haver (existir), Fazer (tempo), Fenomenos: 'Ha muitos alunos.'"),
        ("Predicado verbal", "Nucleo = verbo: 'O aluno estudou.'"),
        ("Predicado nominal", "Nucleo = predicativo: 'O ceu esta azul.'"),
        ("Predicado verbo-nominal", "Dois nucleos: 'O aluno chegou cansado.'"),
        ("Objeto direto (OD)", "Sem preposicao: 'Comprei um livro.'"),
        ("Objeto indireto (OI)", "Com preposicao: 'Gosto de musica.'"),
        ("Complemento nominal", "Paciente: 'Respeito as leis' (leis sao respeitadas)."),
        ("Adjunto adnominal", "Agente: 'Respeito do cidadao' (cidadao respeita)."),
        ("Agente da passiva", "'O livro foi escrito pelo autor.'"),
        ("Adjunto adverbial de causa", "'Morreu de fome.' (causa)"),
        ("Adjunto adverbial de instrumento", "'Cortou com a faca.' (instrumento)"),
        ("Adjunto adverbial de companhia", "'Saiu com os amigos.' (companhia)"),
        ("Adjunto adverbial de assunto", "'Falamos sobre politica.' (assunto)"),
    ]
    LP.extend(sintaxe)

    vozes = [
        ("Voz ativa", "Sujeito pratica: 'O analista elaborou o relatorio.'"),
        ("Voz passiva analitica", "Sujeito sofre: 'O relatorio foi elaborado pelo analista.'"),
        ("Voz passiva sintetica", "VTD+SE: 'Vendem-se casas.' (casas=sujeito)"),
        ("Voz reflexiva", "Sujeito pratica e sofre: 'O menino cortou-se.'"),
        ("Voz reflexiva reciproca", "Acao mutua: 'Os noivos beijaram-se.'"),
    ]
    LP.extend(vozes)

    concordancia = [
        ("Sujeito composto anteposto", "Verbo plural: 'O pai e a mae chegaram.'"),
        ("Sujeito composto posposto", "Opcional: 'Chegou o pai e a mae' ou 'Chegaram...'"),
        ("'Ou' exclusivo/inclusivo", "Exclusao: singular. Inclusao: plural."),
        ("'Com' aditivo", "Verbo plural se 'com'=adicao: 'O pai com a mae chegaram.'"),
        ("'Um dos que'", "Verbo plural: 'Foi um dos que chegaram.'"),
        ("'Mais de um'", "Singular: 'Mais de um faltou.' Plural c/ numeral: 'Mais de dois faltaram.'"),
        ("Verbo 'ser' com pronome", "'Sou eu', 'Eram eles'. Concorda com pronome."),
        ("Verbo 'ser' horas", "Singular ate 1h: 'E 1h.' Plural: 'Sao 2h.'"),
        ("Indice de indeterminacao SE", "VTI+SE: 3a singular: 'Precisa-se de ajudantes.'"),
        ("Particula apassivadora SE", "VTD+SE: verbo concorda: 'Aluga-se casa.'"),
        ("Adjetivo composto", "So ultimo flexiona: 'azul-claros', 'verde-escuras'."),
    ]
    LP.extend(concordancia)

    regencias = [
        ("Regencia: 'agradar'", "VTD (contentar) ou VTI(a) (causar prazer)."),
        ("Regencia: 'aspirar'", "VTI(a) desejar: 'Aspirava ao cargo.' VTD sorver: 'Aspirou o ar.'"),
        ("Regencia: 'assistir'", "VTI(a) ver: 'Assistiu ao filme.' VTD ajudar: 'Assistiu o paciente.' VI morar: 'Assiste em SP.'"),
        ("Regencia: 'chamar'", "VTD + predicativo: 'Chamou-lhe de incompetente.'"),
        ("Regencia: 'custar'", "VTI(a) ser custoso: 'Custou-lhe aceitar.' VI preco: 'Custa R$50.'"),
        ("Regencia: 'implicar'", "VTD: 'Implica novas despesas.' Nao usar 'em'."),
        ("Regencia: 'obedecer'", "VTI(a): 'Obedeceu ao regulamento.'"),
        ("Regencia: 'preferir'", "VTD+OI: 'Prefere praia a montanha.' Nao usar 'do que'."),
        ("Regencia: 'proceder'", "VTI(a) executar: 'Procedeu a analise.' VI fundamento: 'Nao procede.'"),
        ("Regencia: 'visar'", "VTI(a) objetivar: 'Visava ao sucesso.' VTD mirar/visto: 'Visou o alvo/documento.'"),
        ("Regencia: 'lembrar'/'esquecer'", "VTD: 'Lembrou o passado.' VTI(de): 'Lembrou-se do passado.'"),
    ]
    LP.extend(regencias)
''')

# Functions of language, variation, official writing
write('''    funcoes_linguagem = [
        ("Funcao emotiva", "1a pessoa, interjeicoes. Ex: diario, poesia lirica."),
        ("Funcao referencial", "3a pessoa, denotativa. Ex: jornalismo."),
        ("Funcao conativa", "2a pessoa, imperativo. Ex: propaganda."),
        ("Funcao poetica", "Figuras, ritmo. Ex: poesia."),
        ("Funcao metalinguistica", "Explica o codigo. Ex: gramatica."),
        ("Funcao fatica", "Contato: 'Alo?', 'Entendeu?'."),
    ]
    LP.extend(funcoes_linguagem)

    variacao = [
        ("Variacao diatópica (regional)", "'Mandioca' (SP) vs 'aipim' (RJ) vs 'macaxeira' (NE)."),
        ("Variacao diastratica (social)", "Girias, jargões tecnicos por grupo social."),
        ("Variacao diacronica (historica)", "'Vosmece' > 'voce' > 'ce'."),
        ("Variacao diafasica (situacional)", "Formal (entrevista) vs informal (conversa)."),
        ("Preconceito linguistico", "Juizo negativo sobre variedades nao-padrao."),
    ]
    LP.extend(variacao)

    redacao_oficial = [
        ("Redacao oficial: impessoalidade", "Sem marcas de individualidade."),
        ("Redacao oficial: clareza", "Texto direto, sem ambiguidades."),
        ("Redacao oficial: concisao", "Maximo informacao, minimo palavras."),
        ("Redacao oficial: formalidade", "Norma culta, polidez."),
        ("Redacao oficial: padronizacao", "Modelos: oficio, memorando, etc."),
        ("Padrao oficio", "Tipo/ano, data, assunto, destinatario, texto, fecho, assinatura."),
        ("Fecho: 'Respeitosamente'/'Atenciosamente'", "Superiores: Respeitosamente. Iguais: Atenciosamente."),
        ("Ata: caracteristicas", "Resumo fiel, discurso indireto, sem rasuras."),
        ("Relatorio: estrutura", "Introducao, desenvolvimento, conclusao."),
        ("Parecer: estrutura", "Relatorio, opiniao, conclusao."),
        ("Requerimento: estrutura", "Vocativo, preambulo, pedido, fecho."),
        ("Memorando: uso", "Comunicacao entre unidades do mesmo orgao."),
    ]
    LP.extend(redacao_oficial)
''')

print("Part 2/4 written (LP complete)")
