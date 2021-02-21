
condition=True

suma=0
suma_iteracion=0
lst=[] #Esto es una lista vacia. Necesitamos definirla para posteriormente almacenar datos de longitud indeterminada.

while condition:
    numero=int(input("enter a number "))
    if numero>=0:
        lst.append(numero)
        print (str(numero) + " is positive ")
        #suma=suma + numero - método 1 para la suma
        suma+=numero
        #suma_iteracion=suma_iteracion + 1 - método para poder contar el nº de iteraciones
        suma_iteracion+=1
    else:
        break
print(str(suma) + " is the addition ")
print(str(suma/suma_iteracion) + " is the average ")

average=suma/suma_iteracion

for numero in lst:
    if numero>average:
        print(str(numero) + " is bigger than the average")
    