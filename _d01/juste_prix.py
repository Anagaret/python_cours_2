import random

guess=random.randint(0, 10000)
score = 10
print("Un nombre aleatoire entre 0 et 10000 a été généré, essaies de le trouver en moins de 10 coups !")


while True:
    answer = input()
    if int(answer) == r:
        print("Bien joué ! Ton score est de : ", score, " points")
        break
    else:
        if int(answer) > r:
            score = score - 1
            print("Nope, c'est inferieur a ", answer)


        else:
            print("Nope,c'est superieur a", answer)
            score = score - 1