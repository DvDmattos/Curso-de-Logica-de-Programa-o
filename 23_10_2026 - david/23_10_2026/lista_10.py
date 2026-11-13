"""
	
21. Tarifa de estacionamento

Um estacionamento cobra R$ 8 por até 1 hora, 
R$ 15 por mais de 1 até 3 horas e R$ 25 por mais de 3 até 6 horas. 
Acima de 6 horas, cobra R$ 40.
Solicite o tempo estacionado e informe o valor a pagar. 
Considere valores inválidos.
"""
horas = int(input("Quantas tempo estacionado:\n"))

if horas >6 and horas <= 24:
    print("Você pagará R$ 40")
elif horas >3 and horas <= 6:
    print("Você pagará R$ 25")
elif horas >1 and horas <= 3:
    print("Você pagará R$ 15")
elif horas == 1 or horas == 0:
    print("Você pagará R$ 8")
else:
    print("valor inválido")







