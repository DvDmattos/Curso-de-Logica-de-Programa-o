"""
Acesso ao laboratório

Para entrar no laboratório, o estudante precisa estar matriculado e apresentar um crachá válido.
Solicite essas duas informações e determine se a entrada será permitida."""

matricula = input("voce esta matriculado?\n")
cracha =input("voce está com o crachá?\n")

if matricula == "sim" and cracha == "sim":
    print("Você tem acesso liberado ao laboratório.")
else:
    print("Você não tem acesso")


"""
f idade >=60:
    desconto = ingresso * 0.5
elif estudante == "s" and idade < 60:   
    desconto = ingresso * 0.3
else:
    desconto = 0

ingresso = ingresso - desconto

print ("seu ingresso")
"""