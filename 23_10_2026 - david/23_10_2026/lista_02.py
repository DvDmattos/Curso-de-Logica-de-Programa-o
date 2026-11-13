"""4. Conversor de tempo

Solicite uma quantidade de minutos e converta esse valor para horas completas e minutos restantes.
 Exemplo: 135 minutos correspondem a 2 horas e 15 minutos.
 """


mensalidade = float(input("Coloque a quantidade de minutos que sera passado para horas\n"))
horas = mensalidade//60
minutos = mensalidade % 60
print("Os minutos foram convertidos em", horas,"horas e" , minutos, "minutos\n")