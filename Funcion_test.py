
def valid(texto):
    if texto.isdigit():
        numero1=int(texto)
        if not (numero1>=0 and numero1<100):
            return False, -1
    else:
        return False, -1
    return True, numero1

condition=True

while condition: 
    texto=input("enter a number between 0 to 100 ")
    valid, numero1=valid(texto)
    if not valid:
        print( "enter a valid number")
        continue


    texto2=input("enter another number between 0 to 100 ") 
    if texto2.isdigit():
        numero2=int(texto2)
        if numero2<0 or numero2>100:
            print( "enter a valid number")
            continue
    break

suma=numero1+numero2
print(str(suma) + " this is the sum")
resta=numero1-numero2
print(str(resta) + " this is the substraction")
mult=numero1*numero2
print(str(mult) + " this is the product")

try:
    div=numero1//numero2
    resto=numero1%numero2
except ZeroDivisionError:
    print ("This can't be divided")
else:
    print(str(div) + " this is the int division")
    print(str(resto) + " this is the remainder")
    
pot=numero1**numero2
print(str(pot) + " this is the power")