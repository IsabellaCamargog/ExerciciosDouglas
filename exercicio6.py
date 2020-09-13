num = int(input("Informe um número de sequências do Fibonacci? "))
first = 0
second = 1
if num <= 0:
    print("Número deve ser positivo")
else:
    print(first, second, end=" ")
    for x in range(2, num):
        next = first + second
        print(next, end=" ")
        first = second
        second = next