def selection_sort(lista, frequencia): #ordena valores em ordem crescente de frequencia das palavras
    listas_freq_fim = []
    lista_fim = []
    for i in range(len(lista)):
        elemento_atual = frequencia[i]
        elemento_atual_str = lista[i]
        while i > 0 and  frequencia[i-1] > elemento_atual:
            frequencia[i] = frequencia[i-1]
            lista[i] = lista[i-1]
            i -= 1
        frequencia[i] = elemento_atual
        lista[i] = elemento_atual_str
    for p in range(len(frequencia)):
        if frequencia[p] > 5:
            listas_freq_fim.append(frequencia[p])
            lista_fim.append(lista[p])
    return lista_fim , listas_freq_fim

def retirar_pontuação(lista): #retira pontuação da lista
    lista_fim= []
    pontuacao = {"!","*","'",'"','?',":",";","(",")","ª","º","°",",",".",'',}
    for i in range(len(lista)):
        string = ''
        for k in range(len(lista[i])):
            if lista[i][k] in pontuacao:
                pass
            else:
                string += lista[i][k]
        lista[i] = string
    for b in lista:
        if b != '':
            lista_fim.append(b)
    return lista_fim

def retirar_stop_words(stop_words,texto): #retira stop words da lista
    checagem = set()
    texto1 = []
    stop_words = stop_words.split(' ')
    for i in stop_words:
        checagem.add(i)
    for p in texto:
        if p not in checagem:
            texto1.append(p)
    return texto1

def ler_arquivo(nome_do_arquivo): # le arquivo e devolve lista de string
    with open(nome_do_arquivo) as arquivo:
        lista_meio = []
        lista_fim = []
        string = ''
        palavras = arquivo.readlines()
        for o in palavras:
            string += o
        string = string.strip()
        string = string.split("\n")
        for i in range(len(string)):
            string[i] = string[i].split(" ")
            for j in range(len(string[i])):
                lista_meio.append(string[i][j])
    for k in lista_meio:
        if k =='':
            pass
        else:
            k = k.lower()
            lista_fim.append(k)
    return lista_fim
         
def ordenar(lista_strings): #ordena pela frequencia e lexicograficamente lista de strings dada
    lista_strings = sorted(lista_strings)
    lista_strings.reverse()
    lista = []
    lista_freq = []
    for i in range(len(lista_strings)):
        
        if lista_strings[i] not in lista:
            lista.append(lista_strings[i])
            lista_freq.append(1)
        else:
            k = len(lista) - 1
            lista_freq[k] += 1
    lista, frequencia = selection_sort(lista,lista_freq)
    return lista, frequencia

def obter_mais_frequentes(lista_ordenada): # obtem os 3 intens distintos mais frequentes em uma lista ordenada
    top_tres = (lista_ordenada[-1],lista_ordenada[-2],lista_ordenada[-3])
    return top_tres

def separar_quartil(lista_filtrada, frequencia): # devolve 1 lista que contem o indice do primeiro quartil, a frequencia do primeiro quartil, e as 2 listas originais
    lista_filtrada.reverse()
    frequencia.reverse()
    indice_quartil = round((len(frequencia)-3)/4)
    primeiro_quartil_f = frequencia[indice_quartil]
    lista_quartil = [indice_quartil, primeiro_quartil_f,lista_filtrada,frequencia]
    return lista_quartil

def contar_e_comparar_elemento_quartil(lista_quartil): #conta quantos elementos tem a frequencia maior o igual a freq do quartil
    n = lista_quartil[1]
    t=0
    resto_f = lista_quartil[3]
    for i in resto_f:
       if i >= n:
           t += 1
    return t

def  ler_1_quartil(lista_quartil):#  devolve as três primeiras palavras
    #cuja frequencia é diferente da frequencia da palavra do quartil
    resto = lista_quartil[2]
    lista_fim = []
    lista_meio = []
    freq_resto = lista_quartil[3]
    freq_ultima_palavra = lista_quartil[1]
    for i in range(len(freq_resto)):
        if freq_resto[i] < freq_ultima_palavra:
            lista_meio.append(resto[i])
    try:
        for p in range(3):
            lista_fim.append(lista_meio[p])
    except EOFError:  
        return lista_fim
    return lista_fim

def converter_e_inverte_lista_string(listinha):
    string = ''
    for o in listinha:
        string += o + ' '
    string.strip
    return string 


def main():
    nome_arquivo = input()
    stop_words = input()
    lista_texto = ler_arquivo(nome_arquivo)
    lista_texto = retirar_pontuação(lista_texto)
    lista_texto = retirar_stop_words(stop_words,lista_texto)
    lista_ordenada, frequencia = ordenar(lista_texto)
    tupla_frequencia = obter_mais_frequentes(lista_ordenada)
    print(f'{tupla_frequencia[0]} {tupla_frequencia[1]} {tupla_frequencia[2]}')
    lista_quartil = separar_quartil(lista_ordenada,frequencia)
    numero_de_palavras = contar_e_comparar_elemento_quartil(lista_quartil)
    print(numero_de_palavras)
    palavras_não_listadas = ler_1_quartil(lista_quartil)
    palavras_não_listadas = converter_e_inverte_lista_string(palavras_não_listadas)
    print(palavras_não_listadas)
main()