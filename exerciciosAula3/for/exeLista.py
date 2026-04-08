#1
n = int(input("digite um valor ai: "))
soma = 1

for i in range (1, n):
    soma = soma + 1 / i
else: 
    print(soma)

#2
n = int(input("digite um valor ai2: "))
soma = 1
for i in range(1, n):
    soma = soma + 1 * i
else:
    print(f"Resultado: {soma / n}")

#3
lista = []
for i in range(5):
    lista.append(int(input("digite um numero ai: ")))
else:
    lista.sort()
    print(lista)
    lista.reverse()
    print(lista)

#4
for i in range(10):
    valor = float(input("digite ai: "))
    if valor > 25:
        if valor < 85:
            print(f"> 25 e < 85: {valor}")
        else:
            print(f"> 25: {valor}")
    elif valor < 85:
        print(f'< 85: {valor}') 

#5
soma = 0
while True:
    valor = float(input("digite um valor (digite 0 pra parar): "))
    match valor:
        case 0:
            print(soma)
            break
        case _:
            soma += valor
            print(soma)
