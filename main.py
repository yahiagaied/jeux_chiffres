import random

print("__________  Jeux de chiffre V1.0  __________\n")
print(" _________ BIEN VENUE AU JEUX DES CHIFFRES ____________ \n")

try:
    chiffre_a_trouver = random.randint(1, 100)
    nombre_de_tentative = 0
    while True:
        nombre_de_tentative += 1
        chiffre_propose = int(input("Proposez un chiffre entre 1 et 100 : "))
        if chiffre_propose < 1 or chiffre_propose > 100:
            print("Veuillez entrer un nombre entre 1 et 100.")
            continue
        if chiffre_propose < chiffre_a_trouver:
            print("C'est plus !")
        elif chiffre_propose > chiffre_a_trouver:
            print("C'est moins !")
        else:
            print(f"Bravo ! Vous avez trouvé le chiffre {chiffre_a_trouver} en {nombre_de_tentative} tentatives.")
            break
        if nombre_de_tentative >= 5:
            print(f"Désolé, vous avez dépassé le nombre maximum de tentatives. Le chiffre était {chiffre_a_trouver}.")
            break
except ValueError:
         print("Veuillez entrer un nombre valide entre 1 et 100.")
    
print("Merci d'avoir joué ! À bientôt.")
input("Appuyez sur Entrée pour quitter...")
