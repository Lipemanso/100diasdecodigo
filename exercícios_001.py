# Sessão de exercícios em python

#  Soma de dois números 
# F_String - f'texto {variável}'


# def soma(a,b):
    
#     result = num1+num2
#     return print(f'A soma de {num1} e {num2} é {result} ')


# print("Digite dois números para descobrir a soma")
# resp = input("Deseja continuar?"+" Sim ou Não? ")    

# if resp == "sim":
#     num1 = int(input("Digite o primeiro número "))
#     num2 = int(input("Digite o segundo número "))
#     soma(num1,num2)
# else:
#     print("Até a próxima")


# Função de média aritmética

def media_aritmetica(a,b,c):
   
    media = (a+b+c)/3
    return media


print(media_aritmetica(1,2,3))


lista = [23,56,78,13]

def media2(arr):
    tam = len(arr)
    soma = sum(arr)
    media = soma/tam
    return media

print(media2(lista))