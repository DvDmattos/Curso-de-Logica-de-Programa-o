"""
Folha de pagamento
- Desconto do INSS por faixa:
	até R$1.500 = 8%
	de 1500 até R$3.000 = 9%
	acima = 11%	

- Vale transporte: 6% do salário bruto, se o funcionário optar
- Hora-extra: valor da hora normal + 50%

O programa deve:
1. Ler o salário bruto, horas trabalhadas no mês, horas extras e se usa vale-transporte
2. Validar o salári positivo, horas extras não negativas
3. Calcular o bruto total, descontos, e o líquido
4. Mostrar o holerite resumido.
"""

salario_bruto = float(input("Qual o salário bruto:\n"))
horas_trabalhadas = int(input("Quantas horas trabalhadas no mês:\n"))
fez_hora_extra = float(input("Quantas horas extras:\n"))
utiliza_VT = float(input("Utiliza vale-transporte:\n"))


salario_liquido = 0
desconto_inss = 0
desconto_VT = 0
valor_hora_extra = 0


