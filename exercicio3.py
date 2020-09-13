def exercicio3():
    listNumeros = input('Digite 3 numeros separando-os por vírgula: \n').split(',')
    for i in range(0, len(listNumeros)):
        listNumeros[i] = int(listNumeros[i])

    if listNumeros[0] == listNumeros[1] == listNumeros[2]:
        valor = listNumeros[0]**3
    else:
        valor = listNumeros[0] + listNumeros[1] + listNumeros[2]
    return print(f'Valor total: {valor}')

if __name__ == '__main__':
    exercicio3()
