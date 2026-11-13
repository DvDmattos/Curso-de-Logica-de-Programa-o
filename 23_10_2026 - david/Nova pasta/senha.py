senha = "Dinamarca@2025"
information = input("Qual a senha:\n")

while information != senha:
    print("Acesso negado")
    information = input("Qual a senha:\n")

if information == senha:
    print("Senha certa. Acesso permetido")

