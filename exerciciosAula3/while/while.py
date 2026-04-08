i = 0
while i <= 10:
    i+=1
    if i == 5:
        continue
    print("iteração", i)

i = j = 1
while i <= 10:
    while j <= 10:
        print("iteração", i, " e ", j)
        j+=1
    j = 1
    i+=1

#exemplo 6

while True:
    opcao = input("digite uma opção: ")

    match opcao:
        case "":
            print("Comando invalido... tente novamente")
            continue
        case "sair":
            print("saindo do sistema...")
            break
        case "salvar":
            print("salvando arquivo...")
        case "":
            print
        case "novo":
            print("criando novo documento...")
        case "salvar":
            print("salvando arquivo...")
        case "editar":
            print("editando arquivos")
        case _:
            print("opção invalida")