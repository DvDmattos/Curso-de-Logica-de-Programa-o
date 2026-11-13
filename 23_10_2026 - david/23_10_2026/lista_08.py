""" 
. Classificação de velocidade

Solicite a velocidade de um veículo em km/h. 
Classifique-a como baixa (abaixo de 30), moderada (de 30 a 60), 
alta (acima de 60 até 100) ou muito alta (acima de 100).
"""

horas = int(input("Qual a velocidade do veiculo em km/h:\n"))

if horas >= 101:
    print("muito alta.")
elif horas >= 61 or horas == 100:
    print("alta.")
elif horas >= 31 or horas == 60:
    print("moderada.")
elif horas >= 1 or horas == 30:
    print("baixa.")