# exercicio 1

varInt = 1
varStr = "teste"
varFloat = 2.0

print(varInt, varStr, varFloat)

# exercicio 2

valor = float(input("escreva um valor pra ver seu antecessor: "))
print(valor - 1)

# exercicio 3
def CalcularArea():
    base = float(input("valor da base: "))
    altura = float(input("valor da altura: "))
    print(f"o valor da área é: {base * altura} m²")

CalcularArea()

# exercicio 4

contador = 0
soma = 0
while contador < 4:
    soma += int(input("digite um numero para saber a média: "))
    contador += 1
print(f"a média é igual a: {soma // 4}")


