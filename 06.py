# Exercício 6: Ler palavras até o usuário digitar "fim" e depois mostrar todas
palavras = []
print("Digite palavras (digite 'fim' para parar):")
while True:
    palavra = input()
    if palavra.lower() == "fim":
        break  # Sai do laço quando digitar 'fim'
    palavras.append(palavra)
print("Palavras digitadas:")
for p in palavras:
    print(p)
