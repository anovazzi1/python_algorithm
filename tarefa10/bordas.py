from modulo import *

def criar_matriz_nula(largura, altura):
    bordas = []
    zeros = largura*['0']
    t = 0
    while t <= altura:
        bordas.append(zeros)
        t += 1
    return bordas


def destacar_bordas(largura, altura, imagem):
    zeros = largura*['0']
    imagem.append(zeros)
    for i in range(altura+1):
        a='0'
        imagem[i].append(a)
    bordas = criar_matriz_nula(largura,altura)
    for i in range(altura):#altura
        bordas[i+1] = largura*['0'] 
        for j in range(largura):#largura
            if imagem[i][j] == "1":
                if imagem[i][j-1] == '0':
                    bordas[i][j] = '1'
                if imagem[i][j+1] == '0':
                    bordas[i][j] =='1'
                if imagem[i-1][j] == '0':
                    bordas[i][j] = '1'
                if imagem[i+1][j] == '0':
                   bordas[i][j] = '1' 
                if imagem[i-1][j-1] == '0':
                    bordas[i][j] = '1'
                if imagem[i-1][j+1] == '0':
                    bordas[i][j] = '1'
                if imagem[i+1][j-1] == '0':
                    bordas[i][j] = '1'
                if imagem[i+1][j+1] == '0':
                    bordas[i][j]= '1'
    bordas = bordas[0:-1]
    return bordas


def main():

    arquivo_entrada = input()
    arquivo_saida = input()

    largura, altura, codificacao = carregar_imagem_codificada(arquivo_entrada)
    imagem = decodificar(largura, altura, codificacao)
    nova_imagem = destacar_bordas(largura, altura, imagem)

    codificacao = codificar(largura, altura, nova_imagem)
    escrever_imagem_codificada(largura, altura, codificacao, arquivo_saida)


if __name__ == '__main__':
    main()
