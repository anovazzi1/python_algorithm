""" concatena duas listas em em 
que os elementos são separados pelos espacos"""

def concatenar_listas(j,k):
    assert len(j) == len(k)
    lista_concatenada = ""
    for p in range(len(j)):
        for p in range(len(k)):
            a = j[p]+k[p] +" "
            lista_concatenada += a
        return (lista_concatenada)


def main():
    n= input()
    x= input()
    lista1 = []
    lista2 = []
    lista1 = n.split(" ")
    lista2 = x.split(" ")
    fim = concatenar_listas(lista1,lista2)
    print(fim)

main()
