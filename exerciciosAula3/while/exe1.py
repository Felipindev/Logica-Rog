# 1
i = 0
while i <= 20:
    print(f"numeros naturais: {i}")
    i += 1

# 2
i = -13
while i <= 25:
    print(f'numeros naturais: {i}')
    i += 1

# 3
numero = 0 
contador = 0
while True:
    if contador > 50:
        break
    if numero % 2 == 0:
        print(f'posição {contador}: numero natural par: {numero}')
        contador += 1
    numero += 1

# 4
soma = 0 
numero = 0
while True:
    if numero == 100:
        print(f'valor da soma: {soma + 100}')
        break
    if numero % 2 == 0:
        soma = soma + numero
    numero += 1

