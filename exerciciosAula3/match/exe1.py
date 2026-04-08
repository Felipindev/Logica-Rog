#exe1
idade = int(input("digite sua idade: "))

# com if
if idade >= 5 and idade <=7:
    print("categoria: Infantil")
elif idade >= 8 and idade <= 10:
    print("categoria: Juvenil")
elif idade >= 11 and idade <= 15:
    print("categoria: Adolescente")
elif idade >= 16 and idade <=30:
    print("categoria: Adulto")
elif idade > 30:
    print("categoria: Senior")
else: 
    print("nao tem idade suficiente")

# com match
match idade:
    case i if i >= 5 and i <= 7:
        print("categoria: Infantil")
    case i if i >= 8 and i <= 10:
        print("categoria: Juvenil")
    case i if i >= 11 and i <= 15:
        print("categoria: Adolescente")
    case i if i >=16 and i <= 30:
        print("categoria: Adulto")
    case i if i > 30:
        print('categoria: Senior')
    case _:
        print("nao tem idade suficiente")


#exe2
codigo = int(input("digite o código: "))

#com if
if codigo == 1:
    print('sul')
elif codigo == 2:
    print('norte')
elif codigo == 3:
    print('leste')
elif codigo == 4:
    print('oeste')
elif codigo == 5 or codigo == 6:
    print('nordeste')
elif codigo == 7 or codigo == 8 or codigo == 9:
    print('sudeste')
elif codigo >= 10 and codigo <= 20:
    print('centro-oeste')
elif codigo >= 21 and codigo <= 30:
    print('noroeste')
else: 
    print("código nao existente")

#com match
match codigo:
    case 1:
        print('Sul')
    case 2: 
        print('norte')
    case 3:
        print('leste')
    case 4: 
        print('oeste')
    case c if c >=5 and c<=6:
        print('nordeste')
    case c if c >=7 and c <=9:
        print('sudeste')
    case c if c >= 10 and c <= 20:
        print("centro-oeste")
    case c if c >= 21 and c <=30:
        print('noroeste')
    case _:
        print("código inexistente") 