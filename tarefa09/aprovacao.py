''' entrada:
entrada: nota em cada tarefa e presença

critério aprovação: 0,75 presença
menor nota c
menor MEDIA 4
a = 10
b = 7
c = 5
d = 0

saida: aprovadx reprovadx
'''

def verificar_nota_mínima(lista):
    for o in lista:
        if o != 'D':
            aprovadx = True
        else:
            aprovadx = False
            break
    return aprovadx

def somar_todos_intens_lista(lista):
    t=0
    for i in range(len(lista)):
        t += lista[i]
    return t

def ler_notas():
    n= input()
    return n

def computar_presenca():
    try:
        presenca = []
        while True :
            a = input()
            if a == "presente":
                a = 1
            else:
                a= 0
            presenca.append(a)
    except EOFError:
        return presenca

def verificar_criterio(nota, presenca):
    obteve_nota_minima = verificar_nota_mínima(nota)
    frequencia = somar_todos_intens_lista(presenca) / len(presenca)
    if frequencia < 0.75 :
        frequencia = False
    else:
        frequencia = True
    if frequencia and obteve_nota_minima :
        situacao = 'Aprovadx'
    else:
        situacao = 'Reprovadx'
    return situacao

def main():
    notas = ler_notas()
    presenca = computar_presenca()
    situacao = verificar_criterio(notas, presenca)
    print(situacao)

main()
