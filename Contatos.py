import time

contatos = []

def adicionar_contato():

    nome = input('\nDigite o nome do seu contato: ')
    telefone = input('Digite o telefone do seu contato: ')

    contato = {'nome': nome, 'telefone': telefone}
    contatos.append(contato)

    print(f'\nContato adicionado com sucesso:\nNome: {nome}\nTelefone: {telefone}')
    time.sleep(1.2)

def editar_contato(nome):
    for contato in contatos:
        if nome == contato['nome']:
            telefone = contato['telefone']
            novo_nome = input('\nDigite o novo nome do seu contato: ')
            novo_telefone = input('Digite o novo telefone do seu contato: ')

            contato['nome'] = novo_nome
            contato['telefone'] = novo_telefone

            print(f'Feito, agora seu contato é:\nNome: {novo_nome}\nTelefone: {novo_telefone}')
        else:
            print('\nContato não encontrado!')

def listar_contatos():
    for contato in contatos.copy():
        print(f'\nNome: {contato["nome"]}\nTelefone: {contato["telefone"]}.')
        time.sleep(1.2)

def main():
    while True:
        print('\n1. Adicionar contato')
        print("2. Editar Contato")
        print("3. Listar os Contatos")
        print("4. Sair")

        opcao = int(input('\nDigite sua opcao: '))

        if opcao == 1:
            adicionar_contato()
        elif opcao == 2:
            editar_contato_1 = input('\nDigite o nome do contato que deseja editar: ')
            editar_contato(editar_contato_1)
        elif opcao == 3:
            listar_contatos()
        elif opcao == 4:
            print('\nSaindo...')
            time.sleep(1)
            break
        else:
            print('\nOpção inválida.')

main()
