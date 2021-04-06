import datetime
import math

# utilizamos un "bucle infinito" usando como condicion "TRUE". De esta manera podremos usar "brake" cuando mi condición se cumpla.
while True:
    text_1=input(" enter your birthday (aaaa-mm-dd): ")
    try:
        date_b = datetime.datetime.strptime(text_1,"%Y-%m-%d")
    except ValueError:
        print ("That is not correct, please, enter valid date (aaaa-mm-dd) ")
    else:
        break

date_now=datetime.date.today()
print (str(date_now))

your_age= (date_now - date_b.date())/datetime.timedelta(days=365)
print(str(math.floor(your_age)) + " ,this is your age")

next_year =  date_b.date() + datetime.timedelta(days=365.25 * math.ceil(your_age))
if date_now.month>=date_b.month:
    if date_now.month==date_b.month:
        if date_now.day>=date_b.day:
           next_year=next_year+datetime.timedelta(days=1) 
    else:
        next_year=next_year+datetime.timedelta(days=1)
print (str(next_year) + " this is your next bday")

