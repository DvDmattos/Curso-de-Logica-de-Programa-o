media_turma = 0
media = 0
contador = 1


while contador <=5:
    notas = int(input(f"Informe a nota do aluno {contador}:\n"))
                      
    media += notas
    contador += 1

media_turma = media/contador


print("Media da turma:" media_turma)