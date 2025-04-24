
# Palíndromo

# def palindromo(texto):
#     texto.lower().replace(" ","")
#     return texto == texto[::-1]


# print(palindromo("ana"))


# Fatorial de números positivos inteiros

print("Digite o numero que você deseja saber o fatorial")
numero = int(input())

def fatorial(n):
    if n < 0:
        print("Fatorial não definido para números negativos")
    elif n == 0:
        return 1
    else:
        resultado = 1 
        for i in range(1, n + 1):
            resultado = resultado * i
            
        return resultado
        
#print(f'O fatorial de {numero} é {fatorial(numero)}')
print(f'O fatorial de {numero} é {fatorial(numero)}')