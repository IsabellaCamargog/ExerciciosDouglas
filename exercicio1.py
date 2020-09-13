def exercicio1():
    continuar = True
    listaNumeros = []
    while continuar:
        numero = int(input("Informe o número que deseja incluir na lista"))
        listaNumeros.append(numero)
        continuar = input("Deseja continuar inserindo números na lista? (S/N)").upper() == "S"
    print(f' O primeiro elemento da lista foi: {listaNumeros[0]} ')
    print(f' O ultimo elemento da lista foi: {listaNumeros[-1]}')


if __name__ == '__main__':
    exercicio1()