def codificar(largura, altura, imagem):
    lista_media = []
    codificacao = ''
    for i in range(0,altura,2):
        for j in range(largura):
            codigo =f'{imagem[i][j]}{imagem[i+1][j]}'
            lista_media.append(codigo)
        lista_feita=[]
        t = 1
        for k in range(len(lista_media)):
            try:
                if lista_media[k] == lista_media[k+1]:
                    t +=1
                else:
                    lista_feita.append(t)
                    lista_feita.append(lista_media[k])
                    t = 1
            except IndexError:
                lista_feita.append(t)
                lista_feita.append(lista_media[k])
                t = 1
    for h in range(len(lista_feita)):
        p = lista_feita[h]
        p = str(p)
        codificacao += p
        codificacao +=' '
    return codificacao


def decodificar(largura, altura, codificacao):
    matriz = []
    codificacao = codificacao.split(" ")
    linha1 = []
    linha2 = []
    t = 0
    g = 0
    z = 0
    p = largura
    for i in range(len(codificacao)):
        if i % 2== 0:
            n = codificacao[i]
            n = int(n)
            t = 0
            while t<n:
                linha1.append(codificacao[i+1][0])
                linha2.append(codificacao[i+1][1])
                t += 1
    while g < altura:
        linha_1_F = linha1[z:largura]
        linha_2_f = linha2[z:largura]
        matriz.append(linha_1_F)
        matriz.append(linha_2_f)
        z = largura
        largura = largura + p
        g+=2
    imagem = matriz
    return imagem


def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        tipo_arquivo = arquivo.readline()
        tipo_arquivo = tipo_arquivo.strip()
        tamanho = arquivo.readline()
        tamanho = tamanho.strip()
        tamanho = tamanho.split(" ")
        largura = tamanho[0]
        largura = int(largura)
        altura = tamanho[1]
        altura = int(altura)
        codificacao = arquivo.readline()
        codificacao = codificacao.strip()
    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):
    imagem = []
    with open(nome_do_arquivo) as arquivo:
        arquivo.readline()
        largura_altura = arquivo.readline().strip().split()
        largura = int(largura_altura[0])
        altura = int(largura_altura[1])
        for i in range(altura):
            linha = arquivo.readline().strip()
            imagem.append([])
            for num in linha:
                imagem[i].append(num)
    return largura, altura, imagem

def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    with open(nome_do_arquivo,"w") as arquivo:
        print("P1C",file=arquivo)
        print()
        print(f"{largura} {altura}",file=arquivo)
        print()
        print(codificacao,file=arquivo)

def matriz_em_string(imagem):
    pbm = ''
    for i in range(len(imagem)):
        nova_linha = ''.join(imagem[i])
        pbm += nova_linha
        pbm += '\n'
    return pbm


def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
        with open(nome_do_arquivo,"w") as arquivo:
            print("P1",file=arquivo)
            print()
            print(f"{largura} {altura}",file=arquivo)
            print()
            imagem = matriz_em_string(imagem)
            print(imagem,file=arquivo)