for i in range(0, 12, 3):
    print(i)

for i in range(10, 0, -2):
    print(i)
    
for i in range(0, 10):
    print(i)

for _ in range(0, 10):
    print("oi")

for i in range(11):
    for y in range(11):
        print(f'{i} x {y} = { i * y}')

for i in range(11):
    print(i)
else:
    print("Fim")

for i in range(1, 11):
    print(i)
    if i+ 1 == 4:
        break

for i in range(1, 11):
    if i == 5:
        continue
    print("iteração", i)