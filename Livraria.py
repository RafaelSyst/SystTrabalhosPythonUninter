print('Bem-vindo a livraria do Rafael Dias')

lista_livro = []
id_global = 0

def cadastrar_livro(id):
    print('Qual o nome do livro?')
    livro_nome = input()
    print('Qual o nome do autor?')
    autor_nome = input()
    print('Qual o nome da editora?')
    editora_nome = input()

    dicionario = {
        "id": id,
        "nome": livro_nome,
        "autor": autor_nome,
        "editora": editora_nome
    }
    lista_livro.append(dicionario.copy())
    print('Livro cadastrado')


def consultar_livro():
    
    while True:
        print('1. Consultar Todos')
        print('2. Consultar por ID')
        print('3. Consultar por Autor')
        print('4. Retornar ao menu:')
        
        consultar = int(input())

        if consultar == 1:
            print("Todos os livros cadastrados:")
            for livro_nome in lista_livro:
                print(livro_nome)  
        elif consultar == 2:
            print('Insira o ID do autor')
            id_procurar = int(input())
            livro_encontrado = None
            for dicionario in lista_livro:
                if dicionario['id'] == id_procurar:
                    livro_encontrado = dicionario

            if livro_encontrado:
                print(livro_encontrado)
            else:
                print('Livro não encontrado')
                consultar_livro()
        elif consultar == 3:
            print('Insira o nome do autor')
            autor_procurar = (input())
            autor_encontrado = None
            for dicionario in lista_livro:
                if dicionario['autor'] == autor_procurar:
                    autor_encontrado = dicionario
            if autor_encontrado:
                print(autor_encontrado)
            else:
                print('Autor não encontrado')
                consultar_livro()
        elif consultar == 4:
            break

def remover_livro():
    while True:
        id_remover = int(input("Digite o id do livro a ser removido: "))
        livro_encontrado = None
        for dicionario in lista_livro:
                if dicionario['id'] == id_remover:
                    livro_encontrado = dicionario
        if livro_encontrado:
            lista_livro.remove(livro_encontrado)
            print("Livro removido com sucesso!")
            break
        else:
            print("Id inválido")




while True:
    print('1. Cadastrar Livro')
    print('2. Consultar Livro')
    print('3. Remover Livro')
    print('4. Fechar Programa')

    menu = int(input())

    if menu == 1:
        id_global += 1
        cadastrar_livro(id_global)
    elif menu == 2:
        consultar_livro()
    elif menu == 3:
        remover_livro()
    elif menu == 4:
        print('Fechando programa...')
        break
    else:
        print('Opção inválida.')
        continue




