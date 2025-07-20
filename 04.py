# Exercício 4: Verificar números divisíveis por 7 entre 1 e o número digitado
num = int(input("Digite um número inteiro: "))
print(f"Números divisíveis por 7 entre 1 e {num}:")
# Para cada número entre 1 e num
for i in range(1, num + 1):
    # Verifica se o resto da divisão por 7 é zero
    if i % 7 == 0:
        print(i)
