notas = [0, 0, 0, 0]
qtd_alunos = 4

for i in range(qtd_alunos):
    notas[i] = float(input(f"informe a nota do aluno {i + 1}: "))

print(notas)
soma_notas = 0
for i in range(qtd_alunos):
    soma_notas += notas[i]

media_turma = soma_notas / qtd_alunos
print(f"A media da turma é: {media_turma:.2f}")

alunos_acima = 0
for i in range(qtd_alunos):
    if notas[i] >= media_turma:
        alunos_acima += 1

print(f"Quantidade de alunos acima da media: {alunos_acima}")

# lista vazia
carrinho =[]

print('---- carrim (digite "sair" para encerrar) ------')
while True:
    produto = input("Informe o nome do produto: ")

    if produto.lower() == "sair":
        break
    carrinho.append(produto)

print("\n itens do carrin")
tamanho_carrin = len(carrinho)

for i in range(tamanho_carrin):
    print(f"Posição [{i}] ==> produto: {carrinho[i]}")