# Lista de Compras: Faça um programa que permita ao usuário adicionar itens a uma lista de compras e, ao final, imprima a lista completa.

lista = []

while True:
    print("Deseja adicionar um produto? sim ou nao")
    continuar = input()

    if continuar == "sim":
        print("Adicione um produto: ")
        produto = input()
        lista.append(produto)
    elif continuar == "nao":
        break  # Sai do loop while se a resposta for "nao"
    else:
        print("Opção inválida. Digite 'sim' ou 'nao'.")

if lista:  # Verifica se a lista não está vazia antes de imprimir
    print("Sua lista contém os seguintes itens:")
    for item in lista:
        print(f'- {item}')
else:
    print("Sua lista está vazia.")       
   
    
