"""

Uma loja oferece desconto para clientes que possuem cupom ou fazem compras acima de R$ 200. 
Solicite se o cliente tem cupom e o valor da compra.
Informe se ele tem direito ao desconto
"""
# Solicita as informações do cliente
tem_cupom = input("Você possui cupom de desconto? (sim/nao): ").strip().lower()
valor_compra = float(input("Digite o valor total da compra (R$): "))

# Verifica as condições para ganhar o desconto
# O cliente ganha se tiver cupom OU se a compra for maior que 200
if tem_cupom == "sim" or valor_compra > 200:
    print("\nParabéns! Você tem direito ao desconto. 🎉")
else:
    print("\nInfelizmente você não tem direito ao desconto desta vez. 😔")
