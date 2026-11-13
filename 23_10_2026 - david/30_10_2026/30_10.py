"""
Estacionamento

Até 15 minutos: grátis.
Primeira hora: R$ 10.
Cada hora adicional iniciada: R$ 4.
Teto diário: R$ 50.
Conveniados têm 20% de desconto.

O programa deve:

Ler hora e minuto de entrada e de saída, e se é conveniado (S/N).
Converter para minutos, calcular a permanência, aplicar a regra de cobrança, o teto e o desconto.
Mostrar o tempo de permanência em h:min e o valor a pagar."""

#ENTRADA HORAS E MINUTOS    
hora_entrada = int(input("Hora de entrada (0 a 23):\n "))
minutos_entrada = int(input("minutos de entrada (0 a 59):\n"))

#SAIDA HORRAS E MINUTOS 
hora_saida = int(input("Hora de saida (0 a 23):\n "))
minutos_saida = int(input("Minutos de entrada (0 a 59):\n"))


parceiro = input("Você é conveniado (S/N):\n")
conveniado = 0.20


# EXEMPLO saida - entrada (12 - 08 = 4 horas) --- 10.30 - 10.15 = 0.15

# Transformamos tudo em minutos totais
tempo_entrada_min = (hora_entrada * 60) + minutos_entrada
tempo_saida_min = (hora_saida * 60) + minutos_saida

# Tempo total que o carro ficou no local (em minutos)
permanencia_minutos = tempo_saida_min - tempo_entrada_min

print("Tempo de permanêcia em minutos é\n", permanencia_minutos)

#se tempo no local for igual 1 hora  = 10 reais --- se for mais que 1 horas adiciona 4 reais por hora
#apos 11 horas compre 50 rais

# 3. CÁLCULO DO VALOR (Regras de Cobrança)
valor_base = 0

if permanencia_minutos <= 15:
    # Até 15 minutos: grátis
    valor_base = 0
elif permanencia_minutos <= 60:
    # Primeira hora cheia: R$ 10
    valor_base = 10
else:
    # Mais de 1 hora: R$ 10 da primeira hora + R$ 4 por hora adicional iniciada
    minutos_adicionais = permanencia_minutos - 60
    
    # Calculamos quantas horas adicionais foram iniciadas.
    # Usamos uma divisão inteira combinada com uma verificação de resto.
    horas_adicionais = minutos_adicionais // 60
    if minutos_adicionais % 60 > 0:
        horas_adicionais += 1 # Se sobrou qualquer minuto, conta como mais uma hora iniciada
        
    valor_base = 10 + (horas_adicionais * 4)

# Aplicando o teto diário de R$ 50
if valor_base > 50:
    valor_base = 50

# 4. APLICANDO O DESCONTO DE CONVENIADO
if parceiro == "S":

    valor_final = valor_base * 0.8
else:
    valor_final = valor_base

# 5. CONVERTENDO PARA H:MIN 
exibir_horas = permanencia_minutos // 60
exibir_minutos = permanencia_minutos % 60

#(Prints)
print("\n=======================================")
print(f"Tempo de permanência: {exibir_horas}h:{exibir_minutos:02d}min")
print(f"Valor total a pagar: R$ {valor_final:.2f}")
print("=======================================")



