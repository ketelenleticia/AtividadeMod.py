from funcoes import *
from tabulate import tabulate

listaalunos=[]

def menu():
    print(" GERENCIADOR DE NOTAS ")
    print("1 - Cadastrar aluno e notas")
    print("2 - Exibir relatório")
    print("0 - Sair")


while True:
    listanotas=[]
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Encerrando o programa... Até logo! ")
        break
    elif opcao == '1':
        nome=input("digite um nome: ")
        for i in range(1,4):
            nota=float(input(f"digite {i} nota: "))
            listanotas.append(nota)
        media_aluno=calcular_media(listanotas) 
        status=verificar_situacao(media_aluno)   
        dictaluno={
            nome:[listanotas,media_aluno,status]
        }
        
        listaalunos.append(dictaluno) 
    else:
     print(listaalunos)
            
          
    
