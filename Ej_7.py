import random
x=random.randint(2,1000)
print(x)

for numero in range(1,x+1): 
    resto=x%numero
    if resto == 0:
        print(str(numero) + " is a factor of " + str(x))

