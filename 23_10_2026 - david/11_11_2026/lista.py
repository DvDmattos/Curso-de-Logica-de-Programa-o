#5
lista = ["Rola", "Balança-rabo-leitoso" , "Calcinha-branca", "João-corta-pau", "Pica-pau peluno"]
print(lista)
lista[1] = "Cachorro"

print(lista)

#6

lista1 = [22,27,26,24,23,11,7,20,69,67,]
tamanho = len(lista1)
print('tamanho do lista é', tamanho)

#7
lista2 = ["ryzen 7 5800x3d", "RTX 9060XT 16GB", "Placa mãe X570", "Fonte MSI MAG A650BN", "XPG Gammix D35"]
print(lista2)

lista2.append("LG UltraGear")
lista2.append("Redragon Fizz (K617")

print(lista2)

#8
lista3 = ["SP", "RJ", "DF","CE"]

lista3.insert(1,"SC")
print(lista3)

#9
lista4 = ["david","valeria","joelma","joao","arthur","maria"]
lista4.remove("arthur")
print(lista4)

#10
lista5 = [22,27,26,24,23,]
ultimo = lista5.pop()
print(lista5)

#11
lista6 = ["Como Se Fosse a Primeira Vez", 'Gente Grande', 'O Paizão', 'Click','Esposa de Mentirinha']
print(lista6)
filme_novo = input("Fale um filme do Adam Sandler, que nao seja um que ja esteja na lista:\n")
lista6.append(filme_novo)

tamanho2 = len(lista6)
print('tamanho do lista é', tamanho2)
#12

lista7 = [12,5,8,20,3,15]
lista7.sort()
print(lista7)

