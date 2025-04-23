# Imprimir os números em ordem decrescente

# for num in range(10,0,-1): # os parâmetros do range são(inicio,fim,step)
#     print(num)



# palavra = "Python"

# for letra in palavra:
#     print(f'Imprimindo a letra {letra}')

#Crie um programa que receba um número e imprima a tabuada desse número de 1 a 10.

# Com laço while
print("---Com laço while---")
print("Digite o número da tabuada que você quer ver na tela")
tabuada = int(input())

contador = 1
while contador <= 10:
    result = tabuada * contador
    print(f'{tabuada } x {contador} = {result}')
    contador += 1
print("-------------------------------------------------")
# Com o laço for
print("---Com laço for---")
for cont in range(1,11):
    result2 = tabuada * cont
    result = tabuada * contador
    print(f'{tabuada } x {cont} = {result2}')
