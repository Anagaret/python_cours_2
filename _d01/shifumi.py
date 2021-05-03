import random

move = ["pierre","feuille","ciseaux"]
ordi = random.choice(move)
user = input("Choissis pierre, feuille ou ciseaux: ")
user = user.lower()

while True : 
    if user != 'pierre' or 'feuille' or 'ciseaux':
        user = input("Non, choisis pierre, feuille ou ciseaux (et écris bien): ")
    else:
        break
    
if user == 'pierre' or 'feuille' or 'ciseaux':
    print ("Vous avez choisi", user , "l'ordi a choisi" , ordi)
if user == 'pierre':
    if ordi == 'pierre':
        print ('Match nul')
    elif ordi == 'feuille':
        print ('Lordinateur a gagné')
    else:
        print ('Vous avez gagné')
if user == 'feuille':
    if ordi == 'pierre':
        print ('Vous avez gagné')
    elif ordi == 'feuille':
        print ('Match nul')
    else:
        print ('Lordinateur a gagné')
if user == 'ciseaux':
    if ordi == 'pierre':
        print ('Lordinateur a gagné')
    elif ordi == 'feuille':
        print ('Vous avez gagné')
    else:
        print ('Match nul')