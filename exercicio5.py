num = int(input("Quantas palavras deseja armazenar? "))
listPalavras = []
for i in range(num):
    listPalavras.append(input("informe a palavra: "))
maiorPalavra = max(listPalavras, key=len)
print(f'A Maior palavra foi: {maiorPalavra} com {len(maiorPalavra)} caracteres')
