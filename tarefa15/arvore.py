""" programa: ler arquivo em html, procurar urls dentro dessa página
devolve todos os links dentro dessa pagina,
e depois devolve novamente os links dentro dessa pagina encontrada recursivamente,
print os links em forma de arvore em hierarquia, separados por 2 espaços
cada link aparecera só uma vez.

exemplo:"""
#entrada :https://ic.unicamp.br/~lehilton/mc102qr/index.html

#saida:https://ic.unicamp.br/~lehilton/mc102qr/index.html
#   https://ic.unicamp.br/~lehilton/mc102qr/apresentacao.html
#   https://ic.unicamp.br/~lehilton/mc102qr/fixacao.html
#     https://ic.unicamp.br/~lehilton/mc102qr/fixacao/00-algoritmo.html
#       https://ic.unicamp.br/~lehilton/mc102qr/fixacao/01-variaveis.html

import re
import modulo

def criar_arvore(url,pagina,lista_fim,espacos,url_principal): #separa os links do codigo html, e printa a arvore de urls com os espaços
    matches = re.findall(r'(?<=href=["\']).+?(?=["\'])',pagina)     #encontra links no codigo html
    x = espacos + url
    lista_fim.append(x)                                 #adiciona a pagina atual a lista de paginas já acessadas
    for match in matches:
        match = modulo.resolver_url(match,url)
        if modulo.eh_url_valida(match,url_principal):
            if match not in lista_fim:                  #verifica se a pagina ja foi acessada
                k = espacos + match
                print(k[2:len(k)])                      #printa a pagina com o numero de espaços certos
                lista_fim.append(match)
                obter_html(match,lista_fim,espacos,url_principal)    #acessa a pagina recursivamente       
    return lista_fim

def obter_html(url,lista_fim,espacos,url_principal): #retira o codigo html do url da pagina, e manda para função criar_arvore
    espacos += '  '                         #adiciona novos espaços a cada recursão
    pagina = modulo.obter_html(url)
    lista_links = criar_arvore(url,pagina,lista_fim,espacos,url_principal)
    return lista_links


def main():
    url = input()
    url_principal = url
    lista_links = obter_html(url,[],'', url_principal)

main()
