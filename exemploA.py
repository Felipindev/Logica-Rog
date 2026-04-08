print("Hello world!")

"""
string docs

"""

n1 = 1
n2 = 3
resultado = n1 + n2

print("o resultado é: " + str(resultado))

print("teste de \n quebra de linha")
print("teste de")
print()
print("quebra de linha")

preco = 49.90
quantidade = 5

print(f"o preço total é de: R$ {preco * quantidade}")

nome = input("digite seu nome: ")
print(nome)

numero = int(input("digite um numero: "))
print(numero)

def operacoes():
    print("--------------------------------------")
    valor1 = float(input("digite o primeiro valor: "))
    print("--------------------------------------")
    valor2 = float(input("digite o segundo valor: "))
    print("--------------------------------------")

    print(f"soma: {valor1 + valor2}")
    print(f"subtração: {valor1 - valor2}")
    print(f"multiplicação: {valor1 * valor2}")
    print(f"divisão: {valor1 / valor2}")

operacoes()
