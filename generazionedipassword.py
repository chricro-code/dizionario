import random 
caratteri = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/`~"
n_caratteri = input("Quanti caratteri vuoi generare?")
password = ""
for i in range(int(n_caratteri)):
    carattere = random.choice(caratteri)
    password += carattere
print("La tua password generata è:", password)
