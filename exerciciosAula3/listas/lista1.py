# notas = [0, 0, 0, 0] #os itens sao separados por virgula
# qtd_alunos = 4

# for i in range(qtd_alunos):
#     notas[i] = float(input(f"informe a nota do aluno {i + 1}: "))

# print(notas)
# soma_notas = 0
# for i in range(qtd_alunos):
#     soma_notas += notas[i]

# media_turma = soma_notas / qtd_alunos
# print(f"A media da turma é: {media_turma:.2f}")

# alunos_acima = 0
# for i in range(qtd_alunos):
#     if notas[i] >= media_turma:
#         alunos_acima += 1

# print(f"Quantidade de alunos acima da media: {alunos_acima}")

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

#imprimindo lista
print(carrinho[-1]) #imprime a ultima (na ordem inversa)
print(carrinho[0].title()) #usando o indice e deixando bunitin
print(carrinho) #imprime a lista toda


#insert
carrinho.insert(2, "teste") #insert adiciona o item no local q tu quiser
print(carrinho)

#del
del carrinho[3] #remove o item do indice que tu botar
print(carrinho)

#pop 
carrin_popped = carrinho.pop() #remove o ultimo item da lista (e adiciona na variavel)

#remove
carrinho.remove("arroz") #remove pelo nome e nao pela posicao
print(carrinho)

numeros = [1,2,3,4,5]
print(max(numeros)) #retornar valor maximo
print(min(numeros)) #valor minimo
print(sum(numeros)) #retorna a soma dos elemento
print(len(numeros)) #retorna o tamanho da lista

cars = ["bmw", "audi", "toyota", "honda"]
cars.sort() #ordena por ordem alfabetica (maisculos primeiros) na própria lista
numeros.sort()
print(cars)
print(numeros)

cars.sort(reverse=True) #ordena em ordem decrescente tudo e salva na propria lista
numeros.sort(reverse=True) #ordena em ordem decrescente tudo
print(cars)
print(numeros)

print(sorted(cars)) #ordena só pra visualização (nao salva certin)

cars.reverse() #só inverte a ordem da lista
print(cars)

lista = list(range(2, 11, 2)) #cria uma lista começanod do dois, até o 11, indo de 2 em 2
# output: [2, 4, 6, 8, 10]

squares = []

for i in range(1, 11):
    valor = i**2
    squares.append(valor)
print(squares)

squares = [value**2 for value in range(1,11)] #mema coisa

cars = ["bmw", "audi", "toyota", "honda"]
print(cars[0:3]) #printa do indice 0 até pegar 3 elementos
print(cars[2:]) #printa do indice 2 até o ultimo
print(cars[:3]) #printa todo mundo do começo até ter 3 elementos