PROGRAMA: agenda.py

O programa agenda.py é um aplicativo, desenvolvido em python3, de agenda em modo texto, que pode ser operado usando linhas de comando, desse modo, o usuário pode criar uma agenda em formato .csv, além de poder criar eventos, remover eventos, alterar eventos, e exibir eventos de um mesmo dia em forma de lista.

O programa usa uma biblioteca e um módulo nativo do python3, a biblioteca argpass e o módulo csv

O módulo csv é usado para facilitar a manipulação de documetos.csv, foi usado para ler e alterar a agenda.csv por meio de dicionários.

A bibliotéca argpass é responsavel por interpretar as variáveis fornecidas na linha de comando. No caso do programa agenda.py ele recebe:

argumento posicional:
  comando               (criar,listar,alterar,remover,inicializar)

optional arguments:
  -h, --help            mostra a interface de ajuda padrão do argpass
  -a AGENDA_CSV         o nome da agenda desejada
  --nome NOME           nome do evento
  --descricao DESCRICAO   descricao do evento
  --data DATA_EVENTO    data do evento
  --hora HORA           hora do evento
  --evento EVENTO       identificador do evento

Após realizar a opreção a agenda fornecida na linha de comando é criado um arquivo.csv com as alterações desejadas.

O arquivo CSV:
o arquivo CSV usado como agenda tem ';' como separador e tem cabeçalho, sendo esse composto por 5 colunas, sendo ordenadas da esquerda para direita, que são:
1) id do evento: numero usado como identificador do evento
2) nome: nome do evento
3) descrição: descrição do evento
4)data: data do evento
5) hora: horario do evento

Os eventos são colocados abaixo do cabeçalho, sendo um evento por linha.

Estrutura de dados:
A estrutura de dados utilizada para criar o programa agenda.py foi uma lista de dicionarios, a agenda é uma lista e cada evento um dicionário nessa lista, que contem todos os dados do evento, a lista permite ordenar os eventos e o dicionário permite altera-los de maneira bem prática.
o dicionário tinha como chaves: 'id','nome','descricao','data','hora'.
os dados eram lidos e inseridos no arquivo por meio das funções csv.DictReader e csv.DictWriter do módulo csv.