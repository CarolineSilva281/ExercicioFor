# Exercício 5: Imprimir números pares de 0 a 20 e mostrar quantos foram exibidos
contador_pares = 0
print("Números pares de 0 a 20:")
# Para cada número de 0 a 20
for i in range(0, 21):
    # Verifica se é par
    if i % 2 == 0:
        print(i)
        contador_pares += 1
print(f"Total de números pares exibidos: {contador_pares}")
