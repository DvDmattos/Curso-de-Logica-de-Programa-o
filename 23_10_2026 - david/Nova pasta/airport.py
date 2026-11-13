
destino1 = "rio janeiro"
destino2 = "salvador"
destino3 = "recife"

#preços
valor1 = 350
valor2 = 650
valor3 = 800

nome_passageiro = input("Digite o nome do passageiro:\n")
local_destino = input("Digite o local de destino: (RJ/BA/PE)\n")
quantidade_passagem = int(input("Digite a quantas passagem deseja comprar:\n"))

#descontos

if quantidade_passagem >= 3 and quantidade_passagem <= 4:
    desconto1 = 0.05

if quantidade_passagem >= 5 and quantidade_passagem <= 7:
    desconto2 = 0.10

if quantidade_passagem >7:
    desconto3 = 0.15
    
    
#calcular valor total. sem descontos. local x quantidade de passagem

totalrj = valor1*quantidade_passagem
totalba = valor2*quantidade_passagem
totalpe = valor3*quantidade_passagem

#valor total com desconto 
#total - o desconto

#valor total com DESCONTO RIO DE JANEIRO
valor_desconto05 = totalrj - (desconto1*totalrj) #5%
valor_desconto10 = totalrj - (desconto2*totalrj) #10%
valor_desconto15 = totalrj - (desconto3*totalrj) #15%

#valor total com DESCONTO SALVADOR 
    
valor_desconto05 = totalpe - (desconto1*totalpe) #5%
valor_desconto10 = totalpe - (desconto2*totalpe) #10%
valor_desconto15 = totalpe - (desconto3*totalpe) #15%

#valor total com DESCONTO RECIFE
    
valor_desconto05 = totalba - (desconto1*totalba) #5%
valor_desconto10 = totalba - (desconto2*totalba) #10%
valor_desconto15 = totalba - (desconto3*totalba) #15%

#se local

#resumo
RESUMO = f""" ---RESUMO DA COMPRA---
Nome: {nome_passageiro}
Destino: {local_destino}
Quantidade: {quantidade_passagem}
Total da compra:"""

print(RESUMO)
