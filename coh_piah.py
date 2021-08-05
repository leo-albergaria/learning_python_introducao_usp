import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("\nBem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    print("")

    return [wal, ttr, hlr, sal, sac, pal]
    #return [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        print ("")  
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    xTam_Medio = 0
    for i in range(len(as_a)):
        xTam_Medio = xTam_Medio + abs(as_a[i] - as_b[i])
    return xTam_Medio / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # return [wal, ttr, hlr, sal, sac, pal] e Texto --> Textos()

    sentencas_lida = separa_sentencas(texto)
    lista_frases = []
    for i in sentencas_lida:
        separar_frases = separa_frases(i)
        for ii in separar_frases:
            lista_frases.append(ii)

    palavras_lida = []
    for i in lista_frases:
        separar_palavras = separa_palavras(i)
        for ii in separar_palavras:
            palavras_lida.append(ii)

    assinatura_lida = []
    assinatura_lida.append(tamanho_medio_palavras(palavras_lida))
    assinatura_lida.append(relacao_type_token(palavras_lida))
    assinatura_lida.append(razao_hapax_legomana(palavras_lida))
    assinatura_lida.append(tamanho_medio_de_sentenca(sentencas_lida))
    assinatura_lida.append(complexidade_de_sentenca(lista_frases, sentencas_lida))
    assinatura_lida.append(tamanho_medio_de_frase(lista_frases))
    return assinatura_lida

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    valor = ass_cp[0]
    for i in range(len(ass_cp)):
        if ass_cp[i] < valor:
            valor = ass_cp[i]
            indice = i
    return indice


# return [wal, ttr, hlr, sal, sac, pal]
def tamanho_medio_palavras(palavras):
    tamanho_das_palavras = 0
    total_de_palavras = len(palavras)
    for palavra in palavras:
        tamanho_das_palavras = tamanho_das_palavras + len(palavra)
    return tamanho_das_palavras/total_de_palavras

def relacao_type_token(palavras):
    return n_palavras_diferentes(palavras) / len(palavras)

def razao_hapax_legomana(palavras):
    return n_palavras_unicas(palavras) / len(palavras)

def tamanho_medio_de_sentenca(sentencas):
    caracteres_sentenca = 0
    for sentenca in sentencas:
        caracteres_sentenca = caracteres_sentenca + len(sentenca)
    return caracteres_sentenca / len(sentencas)

def complexidade_de_sentenca(lista_frases, sentencas):
    return len(lista_frases) / len(sentencas)

def tamanho_medio_de_frase(lista_frases):
    caracteres_frase = 0
    for frases in lista_frases:
        caracteres_frase = caracteres_frase + len(frases)
    return caracteres_frase / len(lista_frases)

Comparar_Original = le_assinatura()
textos = le_textos()
assinaturas = []
for i in textos:
    assinaturas.append(calcula_assinatura(i))

assinaturas_analisadas = []
for i in assinaturas:
    assinaturas_analisadas.append(compara_assinatura(Comparar_Original, i))


xCoh_Piah = avalia_textos(textos, Comparar_Original)
print("\nO autor do texto", xCoh_Piah, "está infectado com COH-PIAH.")


