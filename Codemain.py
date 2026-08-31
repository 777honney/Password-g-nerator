import random
import string 

motdepasse=""
caracteres = string.ascii_letters + string.digits + string.punctuation

long=int(input("Qu'elle est la longueur de votre mot de passe ? : "))

for i in range (long):
    motdepasse +=random.choice(caracteres)
    
print (motdepasse)

