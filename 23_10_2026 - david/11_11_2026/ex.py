"""nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    print(num)
    
    """
#2------------------------------------------------------
"""numeros = [22,27,26,24,23,11,7,20,69,67,10,2,8,16]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        
print("Lista completa:",numeros)
pares.sort()
print('Lista apenas com numeros pares:',pares)"""

#3

notas = [8.5, 2.0, 10.0, 7.0, 9.5, 6.5]

aprovados = 0

for nota in notas:
    if nota >= 7.0:
        aprovados += 1
        
notas.sort()
print(f"Notas de todos os alunos:{notas}\n Total alunos aprovados:{aprovados}")