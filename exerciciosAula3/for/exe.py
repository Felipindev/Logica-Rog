#1
for i in range(10):
    print(float(input("digite um numero: ")))

#2
soma = 0
for i in range(0, 101):
    if i % 2 == 0:
        soma += i
else: 
    print(soma)

# 3 (que é 4)
soma = 0
for i in range(0, 31):
    if i % 2 != 0:
        soma += i
else:
    print(soma)

#4 (que é a 5)
while True:
    print('-------------')
    print("É a tabuada")
    print("-------------")

    valor = float(input("digite um valor pra saber a tabuada ai: "))

    print('---------------------------------')
    print(f'tabuada de {valor}')
    for x in range(11):
        print(f"{valor} x {x} = {valor * x}")