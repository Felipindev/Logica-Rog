# contador regressivo com media no final
valorAlto = int(input("digite um valor máximo: "))
valorBaixo = int(input("digite um valor mínimo: "))

soma = 0
quantidade = 0

for valor in range(valorAlto, valorBaixo - 1 , -3):
    if valorBaixo >= valorAlto:
        print("digita um valor menor ô cabeção")
        break
    print(valor)
    soma += valor
    quantidade += 1

print(f"media aritmetica: {soma / quantidade}")

# contador bla bla bla
total = 0
preferemFiccao = 0
preferemNaoFiccao = 0

for i in range(6):  
    nome = input("digite o seu nominho: ")
    quantidade= int(input("digite a quantidade de livros que leu no ano: "))
    if quantidade < 0:
        print("tu leu negativos livros foi?")
        break
    total += quantidade
    preferido = int(input("Prefere oq?: \n ficção (digite 1) \n nao-ficção (digite 2)"))
    if preferido == 1:
        preferemFiccao += 1
    elif preferido == 2:
        preferemNaoFiccao += 1
    else: 
        print("cara tu é cego?")
        break

print(f"total de livros lidos: {total}")
print(f"porcentagem que prefere ficção: {(preferemFiccao / 6) * 100}%")
print(f"quantidade que prefere não-ficção: {preferemNaoFiccao}")

# while pro crofin
contador = 0
while True:
    if contador == 5:
        print("Acesso Bloqueado")
        print("ja eraaaaaaaa")
        break

    print("adivinha a senha ai..... \n \n")
    senha = int(input("tenta: "))
    if senha > 2024:
        print("é menor")
    elif senha < 2024:
        print("é maior")
    else:
        print(f"Cofre Aberto em {contador} tentativas")
        break

    contador += 1

#trem do mercadin ai
totalItems = 0
totalCompra = 0
maiorCinquenta = 0
while True:
    valor = float(input("Digite o valor do item: (0 para parar) "))
    if valor == 0:
        break
    elif valor > 50:
        maiorCinquenta += 1
        totalCompra += valor
        totalItems += 1
    else:
        totalItems += 1
        totalCompra += valor

print(f"total itens cadastrados: {totalItems}")
print(f"valor total: R${totalCompra}")
print(f"média de preco dos produto: R${totalCompra / totalItems}")
print(f"maiores que 50: {maiorCinquenta}")

#trem do triangulo de n linhas
# valor = int(input("DIGITE O VALOR DE N: "))
# lista = []
# for i in range(valor + 1):
#     if i <= valor:
#         lista.append(i)
#         print(lista)

valor = int(input("DIGITE O VALOR DE N: "))
for i in range(valor):
    for j in range(i + 1):
        print(f"{j + 1} ", end="")
    print()

#trem dos analisador de triangulo
lado1 = int(input("valor lado 1: "))
lado2 = int(input("valor lado 2: "))
lado3 = int(input("valor lado 3: "))
maiorAngulo = int(input("digite o valor do maior angulo interno (em graus): "))
if (lado1 + lado2) < lado3 or (lado2 + lado3) < lado1 or (lado1 + lado3) < lado2:
    print('triangulo nao existe')
else:
    if lado1 == lado2 and lado2 == lado3:
        print("é equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("é isoceles")
    else:
        print("é escaleno")
if maiorAngulo > 90:
    print("é um obtsuangulo")
elif maiorAngulo == 90:
    print("é um retangulo")
else:
    print("acutangulo")