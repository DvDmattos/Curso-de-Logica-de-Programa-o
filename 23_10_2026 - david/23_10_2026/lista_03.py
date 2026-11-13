""""Classificação de temperatura

Solicite a temperatura atual em graus Celsius. Classifique-a como:
- Abaixo de 15 °C: frio.
- De 15 °C até 25 °C: agradável.
- Acima de 25 °C: quente."""

celsius = int(input("Qual a temperatura em graus Celsius:\n"))

if celsius >=25:
    print("quente.")
elif celsius < 15:
    print("frio.")
elif celsius >15 or celsius < 25:
    print("agradável.")

