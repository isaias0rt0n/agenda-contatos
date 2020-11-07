# Criando uma agenda de contatos em python

AGENDA = {}


# AGENDA['aluno'] = {
#     'telefone': '999999999',
#     'email': 'aluno@email.com',
#     'endereco': 'av.1',
# }

# percorre toda a agenda e imprime contato e seus dados
def mostrar_agenda():
    if AGENDA:
        print("\n------Contatos na agenda------")
        for contato in AGENDA:
            print("Nome: {}".format(contato))
            print("Telefone: {}".format(AGENDA[contato]['telefone']))
            print("Email: {}".format(AGENDA[contato]['email']))
            print("Endereço: {}".format(AGENDA[contato]['endereco']))
            print("-----" * 6)
    else:
        print("Agenda vazia!")


# metodo para buscar um contato na agenda
def buscar_contato():
    busca_contato = input("Digite o nome do contato: ")
    for contato in AGENDA:
        if contato == busca_contato:
            print("{} esta na agenda".format(busca_contato))
            print(AGENDA[contato])
            break
        else:
            print("Nao encontrado")
            break


# metodo para incluir contato na agenda
def incluir_contato():
    input_dados()
    salvar()
    print("Contato adcionado com sucesso!")


# metodo para editar um contato da agenda
def editar_contato():
    nome = input("Nome do contato a ser editado: ")
    if nome in AGENDA:
        AGENDA.pop(nome)
        input_dados()
        salvar()
    else:
        print("Contato nao encontrado na agenda")


# metodo para deletar contato da AGENDA
def deletar_contato():
    nome = input("Contao a ser deletado: ")
    if nome in AGENDA:
        AGENDA.pop(nome)
        salvar()
        print("{} foi deletado da agenda".format(nome))
    else:
        print("{} nao encontrado na agenda".format(nome))


# metodo para exportar agenda
def exportar_agenda(exportar_contato):
    try:
        with open(exportar_contato, "w") as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("Nome:{}, Telefone:{}, Email:{}, Endereco{}\n".format(contato, telefone, email, endereco))
        print("Agenda exportada com sucesso.")
    except Exception as error:
        print("Error ao tantar exportar contatos: ", end='')
        print(error)


# metodo para importar contatos
def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.strip().split(','))
    except FileNotFoundError:
        print("Arquivo nao encontrado")
    except Exception as error:
        print("Erro inesperado: ", end='')
        print(error)


# metodo para inputs de dados na AGENDA
def input_dados():
    nome = input("Nome do contato: ")
    tel = int(input("Telefone: "))
    email = input("Email: ")
    endereco = input("Endereço: ")
    AGENDA[nome] = {
        'telefone': tel,
        'email': email,
        'endereco': endereco,
    }


# metodo para salvar contatos no arquivo
def salvar():
    exportar_agenda('database.csv')


# Metodo para dar recarregar agenda
def recarregar():
    try:
        with open('database.csv', "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print("Database carregado com sucesso")
        print("{} contatos carregados".format(len(linhas)))
    except Exception as erro:
        print("Erro ocorreu", end='')
        print(erro)


# metodo para imprimir menu
def imprimir_menu():
    print('''\n-=-=-=Agenda de contatos-=-=-=
[1] - Mostrar contatos da agenda
[2] - Buscar
[3] - Incluir
[4] - Editar
[5] - Excluir
[6] - Exportar para CSV
[7] - Importar arquivo CSV
[0] - Fechar agenda\n''')


# -------------main------------- #
recarregar()
while True:
    imprimir_menu()
    op = input("Escolha a opção: ")
    if op == '1':
        mostrar_agenda()
    elif op == '2':
        buscar_contato()
    elif op == '3':
        incluir_contato()
    elif op == '4':
        editar_contato()
    elif op == '5':
        deletar_contato()
    elif op == '6':
        nome_do_arquivo = input("Digite o nome do arquivo a ser exportado: ")
        exportar_agenda(nome_do_arquivo)
    elif op == '7':
        nome_do_arquivo = input("Digite o nome do arquivo a ser importado: ")
        importar_contatos(nome_do_arquivo)
    elif op == '0':
        print("Fechando programa...")
        break
    else:
        print("Entrada invalida")
