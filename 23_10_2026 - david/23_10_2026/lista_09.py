"""
. Tipo de plano de internet

Solicite o consumo mensal de internet em GB. 
Classifique o consumo como baixo (até 20 GB),
moderado (acima de 20 até 100 GB) ou alto (acima de 100 GB).
"""
horas = int(input("Qual o consumo mensal de internet\n"))

if horas >= 101:
    print("alto consumo.")
elif horas >= 21 or horas == 100:
    print("consumo moderado.")
elif horas >= 1 or horas == 20:
    print("baixo consumo.")