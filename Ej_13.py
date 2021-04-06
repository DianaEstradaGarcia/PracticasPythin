import math
import random

def generate_primes():
    thousands = []
    number = 1
    while len(thousands) < 1000:
        is_prime = True # "is_prime es una variable bandera que guarda un estado que necesito saber, en este caso si es o no primo"
        for div in range(2,number):
            is_div = number % div == 0 #operación lógica (booleana) que devuelve TRUE O FALSE. Puedo nombrar mi variable antes o en el propio "if"
            if is_div:
            # si es div sabemos que es divisor, por tanto, no es primo
                is_prime=False
                break
        if is_prime:
            thousands.append(number)
        number = number + 1    
    return thousands 
            
f_thousands = generate_primes()
#print (generate_primes())

random_n = random.randint(2,7919)
print(random_n)

is_prime = False
for prime in f_thousands:
    if prime == random_n:
        is_prime= True
        print (str(random_n) + " is prime")
        break
if not is_prime:
    print(str(random_n) + " is not prime")

    


    
