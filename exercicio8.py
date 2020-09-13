import numpy

continuar = True
listaNumeros = []
while continuar:
    num = float(input("informe o número"))
    listaNumeros.append(num)
    continuar = input("Deseja continuar inserindo? (S/N)").upper() == "S"

print(f'Média aritmética é: {numpy.mean(listaNumeros)}')
