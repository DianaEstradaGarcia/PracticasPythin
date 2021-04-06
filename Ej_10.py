import string

def countABC(list_1,text_1):
    total_1=[0]*len(list_1)
    #idx será mi indice y "letter" será mi valor
    for idx, letter in enumerate(list_1):
        for letter_1 in text_1:
            if letter==letter_1:
               total_1[idx]=total_1[idx]+1
    return total_1

text_1=input(" enter a paragraph in lowercase: ")
print(text_1)

#list_1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
list_1=list(string.ascii_lowercase)
#print(list_1)


counting=countABC(list_1,text_1)
#print(counting)

for idx,abc in enumerate(counting):
    print (str(abc) + " = " + str(list_1[idx]))