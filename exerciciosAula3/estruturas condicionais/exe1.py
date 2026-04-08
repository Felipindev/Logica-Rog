#exe 1
valor1 = float(input("digite o primeiro valor"))
valor2 = float(input("digite o segundo valor"))

if valor1 < valor2:
    print(f"menor valor: {valor1}")
else: 
    print(f"menor valor: {valor2}")

#exe 2
valor1 = float(input("digite um valor: "))
valor2 = float(input("digite um valor: "))
valor3 = float(input("digite um valor: "))
menor = None

if valor1 == valor2 and valor1 == valor3:
    print("é tudo igual")
elif valor1 < valor2 and valor1 < valor3:
    menor = valor1
elif valor2 < valor3:
    menor = valor2
else:
    menor = valor3
print(f"menor é: {menor}")

#exe 3
numeros = []
for i in range(4):
    numeros.append(float(input("digite um valor: ")))

menor = min(numeros)
print (f'menor numero é: {menor}')

#exe 4
numeros = []
for i in range(3):
    numeros.append(float(input("digite um valor: ")))
numeros.sort()
print(f' os menores numeros são: {numeros[0]} e {numeros[1]}')

#exe 5
numeros_maiores = 0
for i in range(5):
    numero =float(input("digite um valor: "))
    if numero > 100:
        numeros_maiores += 1
print(f'quantidade de números maiores: {numeros_maiores}')
            
#exe 6
valor = float(input("digite uma valor"))
if valor > 10:
    print("É MAIOR QUE 10!")
else:
    print("NÃO É MAIOR QUE 10!")

#exe 7
valor = float(input("digite um numero pra saber se é par ou impar: "))
if valor % 2 == 0 :
    print("É PAR!")
else: 
    print("É IMPAR!")

# exe 8
anoAtual = int(input("Qual é o ano atual?"))
anoNascimento = int(input("qual o ano do seu nascimento"))

if anoAtual - anoNascimento >= 16:
    print("pode votar!")
else:
    print("nao pode votar")

#exe 9
idade = int(input("digite sua idade: "))
massa = float(input("digite quanto vc pesa: "))

if idade < 18 or idade > 69:
    print("não pode doar sangue")
elif massa < 50:
    print("não tem peso o suficiente para doar sangue")
else: 
    print("pode doar sangue!!")

#exe 10
print("Qual o seu genero? ")
genero = int(input("Digite 1 para masculino ou 2 para feminino: "))
idade = int(input("qual sua idade: "))

match genero:
    case 1:
        if idade < 18:
            print("nao pode se alistar")
        else:
            print("você está apto ao alistamento militar")
    case 2:
        print("é muié nao pode alistar")
    case _:
        print("digita um numero válido")    

#exe 11
numero = float(input("digite um numero par: "))
if numero % 2 != 0:
    print("não é um número par")
else:
    print(f"o quadrado desse numero é: {numero * numero}")

#exe 12
contador = 0
for i in range(5):
    valor = int(input("digite um valor: "))
    if valor < 17 and valor > 10:
        contador += 1
print(f"a quantidade de numeros é: {contador}")