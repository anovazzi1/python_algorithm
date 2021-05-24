''' ler uma lista de numeros escrita pelo usuario e retornar uma outra lista com os mesmos numeros sem repetição,
ordenando-os em ordem crescente de frequencia e caso varios numeros tenham a mesma frequencia, coloca-los em ordem crescente'''

def insertionSort(frequencia, index): 
    for i in range(1, len(frequencia)): 

        key = frequencia[i] 
        key2 = index[i]
        j = i-1
        while j >=0 and key < frequencia[j] : 
            frequencia[j+1] = frequencia[j] 
            index[j+1] = index[j] 
            j -= 1
        frequencia[j+1] = key
        index[j+1] = key2
    return index
#usa o insertion sort para ordenar associada usando os valores da lista de frequencia
def lista_de_int(chegada):
    for i in range(len(chegada)):
        chegada[i] = int(chegada[i])
    return chegada
#converte os strings da lista de entrada em inteiros
def maximo(lista):
    maior = 0
    for i in lista:
        if(maior < i):
            maior = i
    return maior
#encontra o valor maximo da lista
def lista_de_frequencia(chegada,maior):
    frequencia = [0] * (maior+1)
    for i in chegada:
        frequencia[i] = frequencia[i]+1
    return frequencia
#cria uma lista com a frequencia dos numeros da lista inserida
def lista_associada(frequencia,maior):
    zeros = 0
    index = []
    for x in range(maior+1):
        index.append(x)
        if frequencia[x] == 0:
            zeros +=1
    return index, zeros
#cria uma nova lista com os numeros inseridos eliminando as repetições que vai ser reorganizada usando a frequencia 
def int_para_strg(lista_int):
    lista_str = []
    for e in lista_int:
        i = str(e)
        lista_str.append(i)  
    return lista_str
#converte os inteiros da lista de saida para strings
def main():
    chegada = input()
    chegada = chegada.split(" ")
    chegada = lista_de_int(chegada)
    numero_maximo = maximo(chegada)
    f = lista_de_frequencia(chegada,numero_maximo)
    index, z = lista_associada(f,numero_maximo)
    ordenação = insertionSort(f,index)
    final = []
    final = ordenação[z:]
    final = int_para_strg(final)
    print(' '.join(final))
#programa principal

main()