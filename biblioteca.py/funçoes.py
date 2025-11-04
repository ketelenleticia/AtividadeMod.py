from tabulate import tabulate
def adicionar_livro(listaLivros):
    titulo=input("digite o titulo do livri: ")
    autor=input("digite o autor do livro: ")
    status="disponivel"
    listaLivros.append ( {
        "titulo": titulo,
        "autor": autor,
        "status": status
     })
    print("livro adicionado com sucesso")
def emprestar_livro(listaLivros):
    titulo= input("digite um livro que deseja tirar: ")  
    for livro in listaLivros:
        if livro["status"]==titulo:
            livro["status"]="emprestado"
            print(F"livro {titulo}, emprestado com sucesso")
            return
        else:
            print("livro ja esta emprestado ou nao encontrado.")

def devolver_livro(listaLivros):
    titulo= input("digite um livro que deseja devolver: ")  
    for livro in listaLivros:
        if livro["status"]==titulo:
            livro["status"]=="disponivel"
            print(F"livro {titulo}, devolvido com sucesso")
            return
        else:
            print("esse livro nao foi devolvido")

def exibir_livros(listaLivros):
    if not listaLivros:
        print("nao a livro registrado")
    else:
        tabela = []
        for a in listaLivros:
            tabela.append([a["titulo"],  a["autor"], a["status"]])

            print(" RELATÓRIO DA BIBLIOTECA ")
            print(tabulate(
                tabela,
                headers=["titulo", "autor", "status"],
                tablefmt="fancy_grid"
            ))
