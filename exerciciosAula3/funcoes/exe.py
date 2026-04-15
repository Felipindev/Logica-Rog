#1
def oi():
    print("OI")

oi()

#2
def tela(texto):
    print(texto)
tela("testando a função")

#3
def tela2(texto):
    print(texto)
    return "Ok"
tela2("testando a função")

#4
def bhaskara(a, b, c):
    print("fazendo conta...")
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print("não há raizes reais")
    else:
        raizes = []
        raiz1 = -b + (delta ** 0.5) / (2 * a)
        raiz2 = -b - (delta ** 0.5) / (2 * a)
        raizes.append(raiz1)
        raizes.append(raiz2)
        print(f"raízes: {raizes}") 

bhaskara(-2, 2, 1)

#5

def verificar_perfeito(numero):
    soma = 0
    n = numero
    while n > 0:
        n -= 1
        if n == 0:
            if soma == numero:
                return 1
            else:
                return 0
        if numero % n == 0:
            soma += n
    
numero = float(input("digite um numero pra saber se ele é perfeito: "))
resultado = verificar_perfeito(numero)
print(resultado)

# pesquisar: Funções de string e funções da math

#lista 2 de exercicios com funções e laço de repeticção:
#1 

def calcularFahrenhait(celsius):
    fahrenhait = celsius * 1.8 + 32
    print(f"\n Celsius: {celsius} -> Fahrenhait: {fahrenhait}")

def calcularCentimetros(metros):
    centimetros = metros * 100
    print(f"\n Metros: {metros} -> Centímetros: {centimetros}")

while True:
    opcao = input("digite a opção desejada: \n \n 1) Celsius -> Fahrenhait \n 2) Metros -> Centímetros \n sair) sair do programa \n \n")
    match opcao:
        case "sair":
            print("saindo.........")
            break
        case "1":
            celsius = float(input("digite a temperatura em Celsius: "))
            calcularFahrenhait(celsius)
        case "2":
            metros = float(input("digite o valor em metros: "))
            calcularCentimetros(metros)
        case _:
            print("\n opção inválida. Selecione uma opção do menu: ")

#2
saldo_atual = 0

def depositar(quantia):
    global saldo_atual
    if quantia < 0:
        print("informe um numero positivo")
    else: 
        print("depositando......")
        saldo_atual += quantia
        return saldo_atual

def sacar(quantia):
    global saldo_atual
    if quantia < 0:
        print("informe um número positivo")
        return saldo_atual
    elif saldo_atual == 0:
        print('não é possivel sacar: Sem dinheiro na conta')
        return saldo_atual
    elif quantia > saldo_atual:
        print('não é possivel sacar: Quantia maior do que a disponivel na conta')
        return saldo_atual
    else:
        print(f'sacando R${quantia} de R${saldo_atual} disponíveis')
        saldo_atual -= quantia
        return saldo_atual   

while True:
    print("\n \n -------------- bem vindo ao caixa eletronico -------------- \n")

    opcao = int(input("selecione uma opção: \n \n 1) Ver saldo \n 2) Depositar \n 3) Sacar \n 4) Sair \n \n"))
    match opcao:
        case 1:
            print(f'\n saldo atual: R${saldo_atual}')
        case 2:
            quantia = float(input("\n Digite o valor que deseja DEPOSITAR: "))
            depositar(quantia)
        case 3:
            quantia = float(input("\n Digite o valor que deseja SACAR: "))
            sacar(quantia)
        case 4:
            print("\n \n saindo.........")
            break
        case _:
            print("\n digite um valor válido: ")