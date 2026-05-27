# 1. Faça um programa que carregue uma lista de seis elementos numéricos inteiros e
# mostre:
# a. A quantidade de números pares;
# b. Quais são os números pares;
# c. A quantidade de números ímpares;
# d. Quais são os números ímpares.

# numeros = [1,2,3,4,5,6]
# numeros_pares = []
# numeros_impares = []
# qtd_pares = 0
# qtd_impares = 0

# for i in range(len(numeros)):
#     if numeros[i] % 2 == 0:
#         numeros_pares.append(numeros[i])
#         qtd_pares += 1
#     else:
#         numeros_impares.append(numeros[i])
#         qtd_impares += 1
# print(f"a) {qtd_pares}")
# print(f"b) {numeros_pares}")
# print(f"c) {qtd_impares}")
# print(f"d) {numeros_impares}")

# 2. Faça um programa que carregue uma lista com oito números inteiros e mostre:
# a. Os números múltiplos de dois;
# b. Os números múltiplos de três;

# numeros = [1,2,3,4,5,6,7,8]
# multiplos2 = []
# multiplos3 = []

# for i in range(len(numeros)):
#     if numeros[i] % 2 == 0:
#         multiplos2.append(numeros[i])
#     else:
#         multiplos3.append(numeros[i])
# print(f"a) {multiplos2}")
# print(f"b) {multiplos3}")

# 3. Uma escola deseja saber se existem alunos cursando, simultaneamente, as disciplinas
# Lógica e Linguagem de Programação. Coloque os números das matrículas dos alunos
# que cursam Lógica em uma lista, no máximo 10 alunos. Coloque os números das
# matrículas dos alunos que cursam Linguagem de Programação em outra lista, no
# máximo 8 alunos. Mostre o número de matrícula que aparece nas duas listas.

# matriculas_alunos_logica = [1,2,3,4,5,6,7,8,9,10]
# matriculas_alunos_ling = [1,12,3,23,4,45,5,56]
# aparece_duas = []

# for i in range(len(matriculas_alunos_ling)):
#     for n in range(len(matriculas_alunos_logica)):
#         if matriculas_alunos_logica[n] == matriculas_alunos_ling[i]:
#             aparece_duas.append(matriculas_alunos_ling[i])
# print(f"aparece nas duas: {aparece_duas}")

# 4. Dado uma lista A de tamanho 8 e do tipo inteiro faça um programa em Python que,
# utilizando um laço de repetição, receba os valores de entrada e, utilizando outro laço
# de repetição, verifique qual o maior valor da lista e apresente esse valor
listaA = []

for i in range(8):
    listaA.append(int(input("digite o valor de entrada da lista")))
for i in range(len(listaA)):
    if listaA[i] == max(listaA):
        print(max(listaA))