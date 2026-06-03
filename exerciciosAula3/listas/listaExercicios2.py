# 1 - Crie duas listas vazias: nomes e medias. Escreva um programa que peça ao usuário
# para digitar o nome de 5 alunos e a média final de cada um. Guarde os nomes na
# primeira lista e as médias na segunda lista.
# Cálculos exigidos: Após o cadastro, o programa deve percorrer as listas e calcular a
# média geral da turma.
# Saída: Imprima o nome de cada aluno ao lado de sua nota e, ao final, informe quantos
# alunos ficaram acima da média geral da turma.

# nomes = []
# medias = []

# for i in  range(5):
#     nomes.append(input(f"Digite o nome do {i + 1} aluno: "))
#     medias.append(float(input("digite o valor da media dele: \n")))

# media_alunos = sum(medias) / 5

# acima_media = 0
# for media in medias:
#     if media < media_alunos:
#         acima_media += 1

# for i in range(5):
#     print(f"Aluno: {nomes[i]}    |    Nota: {medias[i]}")
# print(f"alunos acima da média: {acima_media}")

# 2 - Um pequeno comércio quer analisar as movimentações do dia. Crie um programa
# que receba várias entradas financeiras e armazene-as em uma única lista chamada
# movimentações.
# Valores positivos representam vendas (receitas) e valores negativos representam
# pagamentos (despesas). Pare de registrar quando o usuário digitar 0.
# Cálculos exigidos: Percorra a lista para calcular o total arrecadado (soma dos
# positivos), o total gasto (soma dos negativos) e o saldo final do dia (receitas +
# despesas).
# Saída: Imprima um relatório financeiro simples mostrando esses três valores. Mostre
# também uma mensagem de "Lucro" se o saldo for positivo, ou "Prejuízo" se for
# negativo.
# movimentacoes = []

# valor = 0
# while True:
#     valor = float(input("digite o valor: "))
#     if valor == 0:
#         break
#     movimentacoes.append(valor)

# total_arrecadado = 0
# total_gasto = 0

# for i in movimentacoes:
#     if i > 0:
#         total_arrecadado += i
#     else:
#         total_gasto += i

# saldo_final = total_arrecadado + total_gasto

# print(f"-----  Relatorio -------- \n")
# print(f" Total ARRECADADO: {total_arrecadado}   |   total GASTO: {total_gasto}  --->  SALDO FINAL: {saldo_final}")
# if saldo_final > 0:
#     print("LUCRO !!!")
# else:
#     print("PREJUIZO !!!!")

# 3 - Dadas duas listas já preenchidas no código, uma com os nomes dos funcionários
# (funcionarios = ['Ana', 'Bruno', 'Carlos', 'Diana']) e outra com seus respectivos salários
# (salarios = [1500.0, 3200.0, 1800.0, 4500.0]).
# Cálculos exigidos: A empresa dará um aumento. Quem ganha até R$ 2000,00 receberá
# 15% de aumento. Quem ganha mais de R$ 2000,00 receberá 10%. Modifique os valores
# diretamente na lista salarios aplicando a regra matemática adequada.

funcionarios = ['Ana', 'Bruno', 'Carlos', 'Diana']
salarios = [1500.0, 3200.0, 1800.0, 4500.0]

for i in range(len(salarios)):
    if salarios[i] <= 2000:
        salarios[i] = salarios[i] * 1.15
    elif salarios[i] > 2000:
        salarios[i] = salarios[i] * 1.1

for i in salarios:
    print(f"nome: {funcionarios[i]} novo salario: {salarios[i]}")