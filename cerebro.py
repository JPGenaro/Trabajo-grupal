from math import trunc


palabras = {
    0:['ping'],
    1:['pong'],
}

for i in range(0,trunc(len(palabras)),2):
    print(f'Preguntas',palabras[i])
    print(f'Respuestas',palabras[i+1])