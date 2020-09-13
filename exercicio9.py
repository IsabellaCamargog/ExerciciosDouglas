continuar = True
listaNumeros = []
while continuar:
    num = float(input("informe o número"))
    listaNumeros.append(num)
    continuar = input("Deseja continuar inserindo? (S/N)").upper() == "S"

for num in listaNumeros:
    print(f'Quadrado do número {num}: {num ** 2}')
