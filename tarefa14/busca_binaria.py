
def busca_binaria(vetor,min,max,numero):
    if min <= max:
        kick = (min+max)//2
        if numero > vetor[kick]:
            return busca_binaria(vetor,kick+1,max, numero)
        elif numero < vetor[kick]:
            return busca_binaria(vetor,min,kick-1,numero)
        else:
            return kick
    return -1


def main():
    i = int()
    vetor = input()
    vetor = vetor.split()
    vetor = list(map(int,vetor))
    numero = input()
    numero = int(numero)
    resultado = busca_binaria(vetor,0,len(vetor)-1,numero)
    print(resultado)
main()