# Exercício 2 : Mostrar os quadrados dos números de 1 até o número digitado
num = int(input("Digite um número inteiro: "))
# Percorrer de 1 até o número (inclusive)
for i in range(1, num + 1):
    quadrado = i ** 2
    print(f"O quadrado de {i} é {quadrado}")
