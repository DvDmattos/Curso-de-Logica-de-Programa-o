""""Sistema de avaliação

Solicite uma nota de 0 a 10 e apresente a classificação: 
excelente (9 a 10), bom (7 a menos de 9), regular (5 a menos de 7) ou insuficiente (abaixo de 5).
Considere também notas inválidas."""

nota = int(input("Uma nota de 0 a 10:\n"))

if nota >= 9 or nota <= 10:
    print("excelente.")
elif nota >= 7 or nota == 9:
    print("bom.")
elif nota >= 5 or nota == 7:
    print("regular.")
elif nota < 5:
    print("insuficiente.")
else:
    print("nota invalida")