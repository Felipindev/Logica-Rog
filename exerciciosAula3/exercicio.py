# exercicio 1

numero = -1
if numero < 0: 
    print("é menor que zero")
elif numero == 0:
    print("o numero é igual a zero")
else: 
    print("o numero é maior que zero")

# exercicio 2
lado_1 = 0
lado_2 = 10
lado_3 = 10

if lado_1 == lado_2 and lado_2 == lado_3:
    print("é equilátero")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("é isósceles")
else:
    print("é escaleno")

# exercicio 3
dia = "teste"
match dia:
    case 1:
        print("Hoje é domingo")
    case 2: 
        print("Hoje é segunda")
    case 3:
        print("hoje é terça")
    case 4:
        print("hoje é quarta")
    case 5: 
        print("hoje é quinta")
    case 6:
        print("hoje é sexta")
    case 7:
        print("hoje é sábado")
    case _:
        print("dia invalido")

#exercicio 4
print("-------------------------------")
print("calculadora básica: ")
print("-------------------------------")

valor1 = float(input("digite o primeiro valor: "))
valor2 = float(input("digite o segundo valor: "))

print('escolha uma das operações: ')
print("1- soma  2- subtração  3- multiplicação  4- divisão   5- módulo da divisão  6- raiz quadrada")
operacao = int(input("insira o número correspondente: "))

if operacao == 1:
    print(f"soma: {valor1 + valor2}")
elif operacao == 2:
    print(f"subtração: {valor1 - valor2}")
elif operacao == 3:
    print(f"multiplicação: {valor1 * valor2}")
elif operacao == 4:
    print(f"divisão: {valor1 / valor2}")
elif operacao == 5:
    print(f"módulo da divisão: {valor1 % valor2}")
elif operacao == 6:
    print(f"raiz quadrada: \n de {valor1}: {valor1 ** 0.5} \n de {valor2}: {valor2 ** 0.5}")
else:
    print("operação não disponível")