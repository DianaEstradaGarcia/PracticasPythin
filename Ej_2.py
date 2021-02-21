'''
numero1=int(input("enter first value "))
numero2=int(input("enter second value "))

mayor_que=numero1>numero2

if mayor_que:
    print(str(numero1) + " is bigger than " + str(numero2))
elif numero1==numero2:
    print(str(numero1) + " is equal to " + str(numero2))
else:
    print(str(numero2) + " is bigger than " + str(numero1))
'''
condition=True #con true garantizo un bucle infinito

while condition: #para conseguir que el programa siga ejecutando
    # mientras se encuentre la condición, usamos un bucle ("while"). En este introducimos
    # todo el bloque de código que necesitamos que se repita. El códgio anterior
    # podremos eliminarlo para que no sea redundante.
    texto=input("enter first value ")
    # texto.isdigit() # será la llamada que debo ejecutar en el "if". La funcion devuelve
    # un valor que debe ser asignado para que su valor no se pierda.
    if texto.isdigit():
        numero1=int(texto)
        if numero1<0:
            break
        texto2=input("enter second value ") 
        if texto2.isdigit():
            numero2=int(texto2)
            if numero2<0:
                break
    
            mayor_que=numero1>numero2

            if mayor_que:
                print(str(numero1) + " is bigger than " + str(numero2))
            elif numero1==numero2:
                print(str(numero1) + " is equal to " + str(numero2))
            else:
                print(str(numero2) + " is bigger than " + str(numero1))
        else:
            condition=False
    else:
        condition=False
  