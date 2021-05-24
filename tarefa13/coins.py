def dividir_notas(valor):
    notas = {"100.00":0,"50.00":0,"20.00":0,"10.00":0,"5.00":0,"2.00":0,}
    while valor >= 100:
        valor -= 100
        notas["100.00"] +=1
    
    while valor >= 50:
        valor -= 50
        notas["50.00"] +=1

    while valor >= 20:
        valor -= 20
        notas["20.00"] +=1

    while valor >= 10:
        valor -= 10
        notas["10.00"] +=1

    while valor >= 5:
        valor -= 5
        notas["5.00"] +=1

    while valor >= 2:
        valor -= 2
        notas["2.00"] +=1

    resto = valor
    return notas, resto

def divir_moedas(resto):
    moedas = {"1.00":0,"0.50":0,"0.25":0,"0.10":0,"0.05":0,"0.01":0,}

    while resto >= 1:
        resto-= 1
        moedas["1.00"] += 1

    while resto >= 0.50:
        resto-= 0.50
        moedas["0.50"] += 1

    while resto >= 0.25:
        resto -= 0.25
        moedas["0.25"] += 1

    while resto >= 0.10:
        resto-= 0.10
        moedas["0.10"] += 1

    while resto >= 0.05:
        resto-= 0.05
        moedas["0.05"] += 1

    while resto >= 0.01:
        resto-= 0.01
        moedas["0.01"] += 1
    
    return moedas

def filtrar_dict(notas, moedas):
    for keys in list(notas):
        if notas[keys] == 0:
            del notas[keys]
    
    for key in list(moedas):
        if moedas[key] == 0:
            del moedas[key]

    return notas, moedas

def imprimir(notas,moedas):
    if notas != {}:
        print("NOTAS:")
        for key in notas.keys():
            print(f"{notas[key]} nota(s) de R$ {key}")
    
    if moedas != {}:
        print("MOEDAS:")
        for keys in moedas.keys():
            print(f"{moedas[keys]} moeda(s) de R$ {keys}")

def main():
    valor = input()
    valor = float(valor)
    notas, resto = dividir_notas(valor)
    moedas = divir_moedas(resto)
    notas, moedas = filtrar_dict(notas,moedas)
    imprimir(notas,moedas)

main()