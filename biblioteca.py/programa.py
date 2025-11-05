from funcoes import *
from tabulate import tabulate
def menu():
    listaLivros=[]
    while True:
        print("biblioteca de livros")
        print("1- adicionar livro")
        print("2- exibir livro") 
        print("3- emprstar livro")
        print("4- devolver livro")
        print("5- sair") 

        opçao=input("escolha uma opçao: ") 

        if opçao=="1":
            adicionar_livro(listaLivros)
        elif opçao=="2":
            exibir_livros(listaLivros)  
        elif opçao=='3':
            emprestar_livro(listaLivros)
        elif opçao=='4':
            devolver_livro(listaLivros) 
        elif opçao == "5":
            print("terminar o programa") 
            break       
menu()        
