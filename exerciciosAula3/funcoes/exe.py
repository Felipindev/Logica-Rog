# #1
def oi():
    print("OI")

oi()

# #2
def tela(texto):
    print(texto)
tela("testando a função")

# #3
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
