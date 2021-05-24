#entrada:linha de elementos separados por espaços
#serão dadas duas listas que tem elementos em comum, esses elementos em comum serão
#colocados em uma nova lista uma unica vez
#A saída deve ser uma única linha (sem quebra de linha) com os elementos separados por espaço.
n= input()
listinha = []
x= input()
listinha2= []
lista_final= []
listinha= n.split(" ")
listinha2= x.split(" ")
for l in listinha:
    for k in listinha2:
        if l==k and l not in lista_final:
            lista_final.append(l)
print(' '.join(lista_final))
