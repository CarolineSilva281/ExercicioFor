# Exercício 10 : Pedir nomes de frutas
frutas = []
while True:
    #. O programa deve continuar até que o nome digitado tenha mais de 10 letras
    fruta = input("Digite o nome de uma fruta: ")
    frutas.append(fruta)
    if len(fruta) > 10:
        break  # Para se a fruta tiver mais de 10 letras
print(f"Foram digitadas {len(frutas)} frutas.")
