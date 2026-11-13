idade = int(input("informe a sua idade:\n"))
estudante = input("vocé é estudante?")

ingresso = 30
desconto = 0

if idade >=60:
    desconto = ingresso * 0.5
elif estudante == "s" and idade < 60:   
    desconto = ingresso * 0.3
else:
    desconto = 0

ingresso = ingresso - desconto

print ("seu ingresso")