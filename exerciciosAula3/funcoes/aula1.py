def mostrar_disciplina():
    print("Algoritmos")
    oi()

def oi():
    print("oi")

mostrar_disciplina()

def mostrar_disciplina(nome, curso):
    print(f"Disciplina, {nome}! Do curso {curso}.")

mostrar_disciplina("teste", "TADS")

def somar(val1, val2):  #variaveis locais (só existem dentro da função)
    soma = val1 + val2  
    print(f'soma: {soma}')

somar(3,10)

def realizar_prova(tentativas=3, tempo=30):
    print(f"prova feita em {tentativas} tentativas e em {tempo} minutos")

realizar_prova()
realizar_prova(4)
realizar_prova(4, 10)

def calcular_dobro(n):
    return n * 2 #devolve a conta pra quem chamou a função

resultado = calcular_dobro(8)
print(f"o dobro é: {resultado}")