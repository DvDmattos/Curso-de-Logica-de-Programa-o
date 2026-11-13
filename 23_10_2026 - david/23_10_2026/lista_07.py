"""
. Frete de uma compra

Solicite o valor da compra. Calcule o frete de acordo com as regras:
compras abaixo de R$ 50 pagam R$ 15; compras de R$ 50 até menos de R$ 150 pagam R$ 8; 
compras a partir de R$ 150 têm frete grátis.
"""

valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra < 50:
    frete = 15
elif valor_compra < 150:
    frete = 8
else:
    frete = 0


valor_total = valor_compra + frete


print(f"\nResumo do Pedido:")
print(f"Valor da compra: R$ {valor_compra:.2f}")
if frete == 0:
    print("Frete: GRÁTIS")
else:
    print(f"Frete: R$ {frete:.2f}")
print(f"Valor total a pagar: R$ {valor_total:.2f}")
