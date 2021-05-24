''' entrada
sequencia de numeros inteiros positivos

saida: soma dos quadrados
dos numeros primos dessa sequencia

se sequencia for vazia ou não tiver nenhum primo
saida = 0 '''

''' algoritmo :
percorre lista
seleciona os numeros primos
eleva ao quadrado os numeros primos
soma
devolve a soma
printa '''
def eh_primo(n):
    if n != 1:
        eh_primo = True
        for d in range(2, n):
            if n % d == 0:
                eh_primo = False
                break
        return eh_primo
    else:
        return False
#checa se numero é primo

def soma(a,b):
   n = a+b
   return n

def lista_de_int(chegada):
    for i in range(len(chegada)):
        chegada[i] = int(chegada[i])
    return chegada
#converte os strings da lista de entrada em inteiros

def filtra(lista_original):
    l = []
    for i in lista_original:   
        if eh_primo(i):
            l.append(i)
    return l
#aplica função f a cada elemento de uma lista e retorna
#os elementos para os quais o retorno de f é true

def mapeia(lista1):
    lista_quadrada = []
    for i in range(len(lista1)):
        a = lista1[i]*lista1[i]
        lista_quadrada.append(a)
    return lista_quadrada       
#aplica para cada elemento da lista 1 função
#devolvee uma nova lista

def reduz(lista_fim,soma):
    t = 0
    for i in range(len(lista_fim)):
        t += lista_fim[i]
    return t

#acumula os valores de 1 lista e produz 1 unico valor
#entrada:
#1 lista e 1 função que recebe 2 valores e retorna 1

def main():
    chegada = input()
    if chegada == "":
        print (0)
    else:
        chegada = chegada.split(" ")
        chegada = lista_de_int(chegada)
        chegada = filtra(chegada)
        if chegada != []:
            chegada = mapeia(chegada)
            chegada = reduz(chegada,soma)
            print(chegada)
        else:
            print(0)
main()

