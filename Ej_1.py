numero1=int(input("enter first value "))
print(numero1)
#Uso "print" para comprabar que la función input funciona 
numero2=int(input("enter second value "))
print(numero2)
print(type(numero1))
# Uso la funcion "type" para ver que tipo de varibale es numero1. En este caso es un numero entero (int)


mayor_que=numero1>numero2
print(mayor_que)

if mayor_que:
    print("Number 1 is bigger than Number 2")
    # prueba nº1. Imprimo solo con cadena de texto
    print(str(numero1) + " is bigger than " + str(numero2))
    # prueba nº2. Imprimo usando las variables, convertidas de nuevo a cadena de texto,
    # concatenadas para obtener una única cadena
elif numero1==numero2:
    print(str(numero1) + " is equal to " + str(numero2))
else:
    print(str(numero2) + " is bigger than " + str(numero1))

# if not mayor_que: #equivalente a "else"
    # print(str(numero2) + " is much bigger than " + str(numero1))
