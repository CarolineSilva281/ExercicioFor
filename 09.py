# Exercício 9: Contar de um número inicial até um final, somando de 2 em 2
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
print(f"Contando de {inicio} até {fim} de 2 em 2:")
while inicio <= fim:
    print(inicio)
    inicio += 2  # Incrementa de 2 em 2
