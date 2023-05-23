""" Auteur :        André Da Costa Dias (DACA22099407)
    Date et lieu :  23 mai 2023, Ecole de technologie de Montréal
    Description :   Ce script permet à l'utilisateur de jouer en ligne de commande au jeu du pendu contre
                    le programme. Ce dernier sélectionne aléatoirememnt un mot à partir du fichier texte
                    "mots_pendu.txt" (qui doit obligatoirement être dans le même sous-dossier que ce script
                    "jeu_du_pendu.py"). et guide l'utilisateur sur les actions à mener pour jouer.
"""

import random

def selectionner_mot():
    """ Sélectionne un mot aléatoire à partir du fichier "mots_pendu.txt" contenant une liste de mots """
    with open("mots_pendu.txt", 'r') as fileToRead:
        mots = fileToRead.readlines()
    return random.choice(mots).strip()          # strip() = sécurité qui supprime les éventuels espaces en début et en fin de mot choisi

def initialiser_jeu(mot_a_deviner):
    """ Initialise les variables du jeu en créant les deux listes permettant d'afficher les lettres trouvées et les lettres erronées """
    bonnes_lettres = []
    mauvaises_lettres = []
    for _ in range(len(mot_a_deviner)):
        bonnes_lettres.append("_")              # Prépare le mot à deviner en fonction du nombre de lettres à deviner que compose le mot séléctionné aléatoirement
    return bonnes_lettres, mauvaises_lettres

def afficher_etat_jeu(bonnes_lettres, mauvaises_lettres):
    """ Affiche les états actuels du jeu en affichant les deux listes (lettre trouvées et lettres erronées)"""
    print("\n**************************************************************\n")
    print("Mot à deviner : " + " ".join(bonnes_lettres))    # join() concatène la liste des caractères séparés en une chaîne de caractères avec un espace entre chaque
    if mauvaises_lettres:                                   # teste si la liste des mauvaises lettres entrées n'est plus vide pour commencer à afficher ce message
        print("Ces lettres précédemment entrées qui ne font pas partis du mot : " + " ".join(mauvaises_lettres))

def entrer_lettre(numero_tentative):
   """ Demande à l'utilisateur d'entrer la lettre qu'il souhaite vérifier et retourne la lettre en minuscule et le numéro de la tentative  """
   numero_tentative += 1
   lettre_utilisateur = input(f"Tentative n°{numero_tentative} - Entrez une lettre : ")
   while not lettre_utilisateur.isalpha():      # vérifie que le caractère entré par l'utilisateur est bien une lettre de l'alphabète, sinon demande d'entrer à nouveau une lettre
        print("/!\ Le caractère entré n'est pas une lettre de l'alphabète. Réessayez : ") # Je considère ceci la même tentative
        lettre_utilisateur = input("Entrez à nouveau une lettre : ")
   return numero_tentative, lettre_utilisateur.lower() # Convertit en minuscule au cas ou l'utilisateur a entré une majuscule

def vérifier_lettre(lettre_utilisateur, mot_a_deviner, bonnes_lettres, mauvaises_lettres):
   """ Vérifie et indique si la lettre entrée par l'utilisateur fait partie du mot ou non. """
   if lettre_utilisateur in mot_a_deviner:
       for i in range(len(mot_a_deviner)):              # Afin d'ajouter la bonne lettre utilisateur partout où elle apparait dans le mot à deviner
           if mot_a_deviner[i] == lettre_utilisateur:
               bonnes_lettres[i] = lettre_utilisateur   # Ajoute le bonne lettre utilisateur à l'intérieur de la liste du mot à trouver
       return bonnes_lettres, mauvaises_lettres         # Retourne les deux listes mises-à-jour contenant les lettres trouvées et les lettres manquées
   else:
       mauvaises_lettres.append(lettre_utilisateur)     # Ajoute la mauvaise lettre en fin de liste des mauvaises lettres
       return bonnes_lettres, mauvaises_lettres         # Retourne les deux listes mise-à-jour contenant les lettres trouvées et les lettres manquées

def jouer_au_pendu():
   mot_a_deviner = selectionner_mot()                                   # un mot aléatoire est séléctionné
   bonnes_lettres, mauvaises_lettres = initialiser_jeu(mot_a_deviner)   # initialisation des états du jeu
   numero_tentative = 0
   nb_chances_restantes = 6

   # Jeu qui boucle tant que l'utilisateur n'a pas commis 6 erreurs ou qu'il a fini par trouver toutes les lettres
   while nb_chances_restantes > 0:
       afficher_etat_jeu(bonnes_lettres, mauvaises_lettres)                     # Affiche l'état courant des deux listes
       numero_tentative, lettre_utilisateur = entrer_lettre(numero_tentative)   # Demande à l'utilisateur de rentrer une lettre et retourne le numéro de tentative mis-à-jour
       bonnes_lettres, mauvaises_lettres = vérifier_lettre(lettre_utilisateur, mot_a_deviner, bonnes_lettres, mauvaises_lettres) # Vérification de la lettre entrée pas l'utilisateur
       if "_" not in bonnes_lettres:  # vérifie s'il n'y a plus de lettres manquantes dans le mot a deviner, si c'est le cas, l'utilisateur a gagné
           print("\n------------------------------------------------------------------------------------------------------------------")
           print(f"Félicitation, vous avez trouvez le bon mot. Le mot était effectivement '{mot_a_deviner}' et il vous restait {nb_chances_restantes} chance(s).")
           print("------------------------------------------------------------------------------------------------------------------")
           return   # Met fin au programme si l'utilisateur a gagné (plus de '_')
       if lettre_utilisateur not in bonnes_lettres:     # Si la lettre entrée n'est pas dans le mot à deviner,
           nb_chances_restantes -= 1                    # réduit la nb de chances restantes, afficher les messages à l'utilisateur et reboucle
           print(f"Incorrect, la lettre '{lettre_utilisateur}' ne fait pas partie du mot.")
           print(f"Il vous reste {nb_chances_restantes} chance(s).")
       # Si nb_chance_restante n'est pas encore 0 et qu'il reste des '_' à trouver (condition précédente, ligne 63), boucle ici.
   # Si nb_chance_restante est égal à 0, sort de la boucle et l'utilisateur a perdu.
   print("\n-------------------------------------------------------------------------------------------------------")
   print(f"Vous avez perdu. Il ne vous reste plus de chance. Le mot qu'il fallait deviner était : {mot_a_deviner}")
   print("-------------------------------------------------------------------------------------------------------")

jouer_au_pendu()