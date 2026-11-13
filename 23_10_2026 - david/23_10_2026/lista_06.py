"""Horário de funcionamento

Solicite a hora atual, em formato de 0 a 23.
Informe se é madrugada (0–5),manhã (6–11), tarde (12–17) ou noite (18–23). 
Trate valores fora desse intervalo como inválidos. """

horas = int(input("Qual a hora atual, em formato de 0 a 23.:\n"))

if horas >= 18 or horas == 23:
    print("noite.")
elif horas >= 12 or horas == 17:
    print("tarde.")
elif horas >= 6 or horas == 11:
    print("manhã.")
elif horas >= 0 or horas == 5:
    print("madrugada.")