
# Tareas de Programación para Practicar

## Coma y Código
Supongamos que tienes una lista como esta:

```python
spam = ['manzanas', 'plátanos', 'tofu', 'gatos']
```

Escribe una función que tome una lista como argumento y devuelva una cadena con todos los elementos separados por una coma y un espacio, con "y" insertado antes del último elemento. Por ejemplo, al pasar la lista anterior a la función, debería devolver `'manzanas, plátanos, tofu, y gatos'`. Pero tu función debe poder trabajar con cualquier lista que se le pase como argumento. Asegúrate de probar el caso en que se pase una lista vacía `[]`.

## Rachas de Lanzamiento de Monedas
En este ejercicio, intentaremos hacer un experimento. Si lanzas una moneda 100 veces y escribes una “C” para cada cara y una “S” para cada cruz, obtendrás una lista que se verá como “C C C C S S S S C C”. Si le pides a un humano que invente 100 lanzamientos al azar, probablemente obtendrás resultados alternantes como “C S C S C C S C S S”, que parecen aleatorios (para los humanos), pero no son matemáticamente aleatorios. Un humano casi nunca escribirá una racha de seis caras o seis cruces seguidas, aunque es muy probable que ocurra en lanzamientos verdaderamente aleatorios. Los humanos son predeciblemente malos siendo aleatorios.

Escribe un programa para averiguar cuántas veces aparece una racha de seis caras o seis cruces en una lista generada aleatoriamente de lanzamientos de monedas. Tu programa dividirá el experimento en dos partes: la primera parte genera una lista de valores aleatorios de "caras" y "cruces", y la segunda parte verifica si hay una racha en ella. Escribe todo el código en un bucle que repita el experimento 10,000 veces para averiguar qué porcentaje de los lanzamientos contiene una racha de seis caras o cruces seguidas. Como pista, la llamada a la función `random.randint(0, 1)` devolverá un valor de 0 el 50% del tiempo y un valor de 1 el otro 50% del tiempo.

Puedes empezar con el siguiente código base:

```python
import random
numeroDeRachas = 0
for experimento in range(10000):
    # Código que crea una lista de 100 valores de "caras" o "cruces".

    # Código que verifica si hay una racha de 6 caras o cruces seguidas.
print('Probabilidad de racha: %s%%' % (numeroDeRachas / 100))
```

Por supuesto, esto es solo una estimación, pero 10,000 es un tamaño de muestra decente. Algunos conocimientos de matemáticas podrían darte la respuesta exacta y ahorrarte la molestia de escribir un programa, pero los programadores son notoriamente malos en matemáticas.

## Cuadrícula de Imagen de Caracteres
Supongamos que tienes una lista de listas donde cada valor en las listas internas es una cadena de un solo carácter, como esta:

```python
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
```

Piensa en `grid[x][y]` como el carácter en las coordenadas x e y de una “imagen” dibujada con caracteres de texto. El origen (0, 0) está en la esquina superior izquierda, las coordenadas x aumentan hacia la derecha y las coordenadas y aumentan hacia abajo.

Copia el valor anterior de la cuadrícula y escribe un código que lo use para imprimir la imagen.

Salida esperada:

```
..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....
```

Pista: Necesitarás usar un bucle dentro de otro bucle para imprimir `grid[0][0]`, luego `grid[1][0]`, luego `grid[2][0]`, y así sucesivamente hasta `grid[8][0]`. Esto terminará la primera fila, por lo que entonces imprimirás un salto de línea. Luego tu programa debería imprimir `grid[0][1]`, luego `grid[1][1]`, luego `grid[2][1]`, y así sucesivamente. Lo último que imprimirá tu programa será `grid[8][5]`.

Además, recuerda pasar el argumento `end` a `print()` si no quieres que se imprima un salto de línea automáticamente después de cada llamada a `print()`.
