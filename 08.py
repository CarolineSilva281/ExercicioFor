# Exercício 8 (while): Pedir senha até o usuário acertar "liberar123"
senha_correta = "liberar123"
while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Bem-vindo")
        break  # Sai do laço quando senha estiver correta
    else:
        print("Senha incorreta")
