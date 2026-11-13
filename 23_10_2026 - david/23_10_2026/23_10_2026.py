"""Solicite o valor mensal de um plano de celular e a quantidade de meses contratados.
 Calcule o custo total do período e quanto será gasto em um ano nesse mesmo plano."""

mensalidade = float(input("valor mesal do plano\n"))
meses_contratados = int(input("meses do contrato\n"))
total = mensalidade * meses_contratados
ano_gastos = mensalidade * 12 

print("O valor total do plano é\n" , total, "e o gasto anual do plano sera:\n" ,ano_gastos,)