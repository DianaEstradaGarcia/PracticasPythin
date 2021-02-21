numero1=int(input("enter first value "))
numero2=int(input("enter second value "))

if numero1 % 2==0:
    print("Es par ")

# para el "for" debo usar siempre una variable nueva. Así evito que se reescriba la variable.

for numero in range(numero1,numero2):
    if numero % 2==0:
        print( str(numero) + " is even ")

    