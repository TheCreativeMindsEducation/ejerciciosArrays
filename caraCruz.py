import random
numeroDeRachas = 0 # cantidad de veces en las que tenemos 6 caras o cruces seguidas
monedaAnterior = 'S' # acumulo el resultado de la "tirada" anterior
listaMonedas = [] # lista en la que guardare las monedas tiradas por aleatoriedad 
generarMoneda = ' ' # aqui guardaré los valores de random.randint
cuentaRacha = 1 #veces en las que sale cara o cruz seguidas

for i in range(100):
    generarMoneda = random.randint(0, 1) #genero numero aleatorio (0 == cara)(1 == cruz)
    if generarMoneda == 0: # si es cero
        listaMonedas.append('C') #añado una cara al final
    elif generarMoneda == 1: # si es uno
        listaMonedas.append('S') #añado una cruz al final

for i in range(len(listaMonedas)): # desde i =0 hasta la longituda de la lista
    if i == 0: # primera iteracion, solo guardo que ha salido
        monedaAnterior = listaMonedas[i]
    else: # si no 
        if listaMonedas[i] == monedaAnterior: #si la mondaAnterior es igual a la iteracion actual
            cuentaRacha += 1 # sumo uno a la racha
        else: # sino
             monedaAnterior = listaMonedas[i] #cambiamos el valor de moneda anterior al cambiar
             cuentaRacha = 1 # reinicio la racha
        if cuentaRacha >=6: # cada vez que haya mas de el numero de racha
            numeroDeRachas +=1 # sumo uno al número de rachas
        
print(listaMonedas) # imprimo la lista
print(numeroDeRachas) # imprimo el numero de rachas
