# 1 – Crie um programa que ajude um professor a analisar o desempenho de uma turma.
# O programa deve pedir ao usuário o nome e a nota de vários alunos. O programa para de
# pedir dados quando o usuário digitar "sair" no nome. Essas notas devem ser salvas em
# uma lista.
# Em seguida crie uma função chamada calcular_estatisticas(lista_notas) que recebe a
# lista de notas e retorne:
# A média aritmética da turma.
# A maior e a menor nota (sem usar as funções prontas max() e min()).
# Crie uma função chamada exibir_ranking(lista_notas) que ordene as notas de forma
# decrescente (do maior para o menor) e exiba o resultado na tela.


def calcular_estatisticas(lista_notas):
    media = sum(lista_notas) / len(lista_notas)
    maior = 0
    menor = 0

    for i in range(len(lista_notas)):
        if lista_notas[i] > maior:
            maior = lista_notas[i]
        if lista_notas[i] < menor:
            menor = lista_notas[i]
    return media, maior, menor 

def exibir_ranking(lista_notas):
    print("-------- Ranking ----------")
    print(sorted(lista_notas, reverse=True))

lista_notas = []

while True:
    nome = input("Digite o nome do aluno: (sair para encerrar) ")
    if nome == "sair":
        break
    lista_notas.append(float(input("digite a nota do aluno: ")))
estatisticas = calcular_estatisticas(lista_notas[:])
exibir_ranking(lista_notas)

# 2 - Um investidor quer registrar suas transações diárias (lucros e prejuízos) e entender o
# comportamento do seu saldo.
# Crie uma função que peça ao usuário para digitar 7 valores (números reais),
# representando o resultado financeiro de cada dia da semana. Valores positivos são
# lucros, valores negativos são prejuízos (ex: 150.50, -50.00, 200.00). Salve-os em uma
# lista.
# Crie uma função chamada analisar_carteira(lista_valores) que:
# Calcule o saldo final acumulado (soma de todos os itens).
# Calcule a porcentagem de dias que foram lucrativos (valores maiores que zero) em
# relação ao total de dias.
# Crie uma função chamada filtrar_e_ordenar(lista_valores) que:
# -Separe apenas os dias de prejuízo (valores menores que zero).
# -Ordene esses prejuízos do pior para o melhor (ou seja, em ordem crescente: o número
# mais negativo primeiro).
# Mostre o saldo final, a taxa de sucesso e a lista de prejuízos ordenados.