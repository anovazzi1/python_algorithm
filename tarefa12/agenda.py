'''criar um programa por linha de codigo usando argpass, esse programa criará uma agenda.csv, que armazenará os dados.
comandos que serão passados:
incializar, criar, alterar,remover,listar'''

# inicializar:
#     cria o arquivo agenda.csv e retorna 'Uma agenda vazia `agenda.csv` foi criada!' 

# criar:
#     cria um evento na agenda com as informações que foram passadas como argumento
#     informações:
#         nome
#         descrição
#         data
#         hora
#     evento tem um identificador de valor t=1 inicialmente, a cada novo evento t+=1

# alterar:
#     pode alterar dado de algum evento criado anteriormente (função da classe eventos)

# remover:
#     remove um evento escolhido (função da classe evento)

#listar:
#     apresenta todos os eventos de 1 dia, em ordem de criação
    
#     formato de saida necessário:
#     Eventos do dia 13/06/2020
#     -----------------------------------------------
#     Evento 1 - MC102
#     Descrição: Aula de laboratório
#     Data: 01/06/2020
#     Hora: 16:50
#     -----------------------------------------------
#     caso não haja evento no dia a mensagem apresentada deve ser:
#     Não existem eventos para o dia 13/06/2020!


import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--agenda_csv", help="nome da agenda desejada",required = True, type=str)
parser.add_argument("comando", help="comando desejado", type=str)
parser.add_argument('--nome', action = 'store', dest = 'nome', required = False,help = 'nome do evento')
parser.add_argument('--descricao', action = 'store', dest = 'descricao', required = False,help = 'descricao do evento')
parser.add_argument('--data', action = 'store', dest = 'data_evento', required = False,help = 'data do evento')
parser.add_argument('--hora', action = 'store', dest = 'hora', required = False,help = 'hora do evento')
parser.add_argument('--evento', action = 'store', dest = 'evento', required = False,help = 'identificador do evento',type= str)

args = parser.parse_args()
lista_agenda = []

def escrever_arquivo(arquivo): # sobrescreve antiga agenda.csv com nova agenda.csv contendo os dados atualizados
    with open(arquivo,'w',encoding='UTF-8',newline='') as csv_file:
        colunas = ["id","nome", "descricao","data","hora"]
        escrever = csv.DictWriter(csv_file, fieldnames=colunas, delimiter=';', lineterminator='\n')
        escrever.writeheader()   
        for evento in lista_agenda:            
            escrever.writerow({'id':evento['id'],'nome': evento['nome'], 'descricao':evento['descricao'],'data':evento['data'],'hora':evento['hora']})
        pass
    

def printar_agenda(lista_dia, data): #printa eventos do dia fornecido no formato desejado
    print(f"Eventos do dia {data}")
    print("-----------------------------------------------")  
    for o in lista_dia:
        print(f"Evento {o['id']} - {o['nome']}")
        print(f"Descrição: {o['descricao']}")
        print(f"Data: {o['data']}")
        print(f"Hora: {o['hora']}")
        print("-----------------------------------------------")
    pass

def adicinonar_evento(evento): #adiciona evento a lista de dicts, e cria seu id
    lista_agenda.append(evento)
    evento_atual = lista_agenda[-1]
    if evento_atual["id"] == None:
        evento_atual["id"] = len(lista_agenda)
    lista_agenda[-1] = evento_atual
    pass

def ler_arquivo_atualizar_lista(nome_arquivo): #lê arquivo e gera uma lista de dicts com os eventos
    with open(nome_arquivo,'r',encoding= "UTF-8", newline= '') as csv_file:
        leitor = csv.DictReader(csv_file, delimiter=';')
        for o in leitor:
            lista_agenda.append(o)
        pass

def criar_arquivo(nome_arquivo): #cria uma agenda.csv com cabeçalho
    mensagem = f'Uma agenda vazia {nome_arquivo} foi criada!'
    with open(nome_arquivo,'w',encoding= "UTF-8",newline='') as csv_file:
        colunas = ["id","nome", "descricao","data","hora"]
        escrever = csv.DictWriter(csv_file, fieldnames=colunas, delimiter=';', lineterminator='\n')
        escrever.writeheader()
    print(mensagem)
    return True

def criar_evento(nome_arquivo, identificador, nome, descricao, data, hora): #cria dict que representa evento
    mensagem = 'evento foi criado e adicionado na agenda'
    ler_arquivo_atualizar_lista(nome_arquivo)
    evento = {
        "id": identificador,
        "nome": nome,
        "descricao": descricao,
        "data": data,
        "hora": hora,
    }
    adicinonar_evento(evento)
    escrever_arquivo(nome_arquivo)
    print(mensagem)
    return True

def alterar(nome_arquivo, identificador,nome,descricao,data,hora): #verifica qual falor deve ser alterado e o altera
    k = [nome,descricao,data,hora]
    for o in k:
        if o != None:
            mudanca = o
    if mudanca == nome:
        alteracao = "nome"
    elif mudanca == descricao:
        alteracao = "descricao"
    elif mudanca == data:
        alteracao = "data"
    elif mudanca == hora:
        alteracao = "hora"
    
    ler_arquivo_atualizar_lista(nome_arquivo)
    for z in lista_agenda:
        if z["id"] != identificador:
            pass
        else:
            g = z
            evento_antigo = g
            break
    evento_antigo[alteracao] = mudanca
    evento_novo = evento_antigo
    o = evento_novo
    escrever_arquivo(nome_arquivo)
    mensagem = 'o evento foi alterado'
    print(mensagem)
    return True

def remover_evento(nome_arquivo, identificador): #remove evento da lista de dicts com os eventos
    ler_arquivo_atualizar_lista(nome_arquivo)
    for o in lista_agenda:
        if o['id'] == identificador:                
            lista_agenda.remove(o)
    escrever_arquivo(nome_arquivo)
    print("o evento foi removido")
    return True

def listar(nome_arquivo,data): # gera uma lista com todos os dictcs que tem eventos no mesmo dia
    lista_meio = []
    ler_arquivo_atualizar_lista(nome_arquivo)
    for o in lista_agenda:
        if o['data'] == data:
            lista_meio.append(o)
    if lista_meio == []:
        print(f"Não existem eventos para o dia {data}!")
    else:
        printar_agenda(lista_meio, data)
    return True

def main():
    nome_arquivo, comando = args.agenda_csv, args.comando
    nome , descricao, data = args.nome , args.descricao , args.data_evento
    hora = args.hora
    identificador = args.evento

    if comando == 'inicializar':
        nova_agenda = criar_arquivo(nome_arquivo)
    
    elif comando == 'criar':
        novo_evento = criar_evento(nome_arquivo, None, nome, descricao, data, hora)

    elif comando == 'alterar':
        alterar_evento = alterar(nome_arquivo, identificador,nome,descricao,data,hora)

    elif comando == 'remover':
        rmvr_evento = remover_evento(nome_arquivo,identificador)
    
    elif comando == 'listar':
        lista_eventos = listar(nome_arquivo, data)

main()