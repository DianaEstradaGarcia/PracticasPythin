import random
first_12= []
for numero in range(0,12): 
    x=random.randint(0,100)
    first_12.append(x)
sum_1=sum(first_12)
print(str(sum_1) + " this is the sum" )
mean=sum_1/12
print(str(mean)+ " this is the mean")

second_12= []
for numero in range(0,12): 
    x=random.randint(0,100)
    second_12.append(x)
sum_2=sum(second_12)
print(str(sum_2) + " this is the sum 2" )
mean_2=sum_2/12
print(str(mean_2)+ " this is the mean 2")

if mean > mean_2:
    print(str(mean) + " is bigger than " + str(mean_2))
else:
    print(str(mean_2) + " is bigger than " + str(mean))

#Usando funciones esta vez:

def generate_mean():
    twelve= []
    for numero in range(0,12): 
        x=random.randint(0,100)
        twelve.append(x)
    sum_1=sum(twelve)
    print(str(sum_1) + " this is the sum" )
    mean=sum_1/12
    print(str(mean)+ " this is the mean")
    return mean

mean_1= generate_mean()
mean_2=generate_mean()

if mean_1 > mean_2:
    print(str(mean_1) + " is bigger than " + str(mean_2))
else:
    print(str(mean_2) + " is bigger than " + str(mean_1))

