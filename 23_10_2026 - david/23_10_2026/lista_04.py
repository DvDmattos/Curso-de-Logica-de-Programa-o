""". Categoria de um produto

Solicite o preço de um produto e classifique-o como econômico (até R$ 30), 
intermediário (acima de R$ 30 até R$ 100) ou premium (acima de R$ 100)."""

preco = int(input("Qual o preço do produto:\n"))

if preco >=100:
    print("premium.")
elif preco < 30:
    print("econômico.")
elif preco > 30 or preco < 100:
    print("intermediário.")