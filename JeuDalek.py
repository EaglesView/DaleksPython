import random


# print(__name__)
# pass
# dunder , tupple, list, dictionnaire
# MVC

class Modele():  # Logique
    def __init__(self):
        self.largeur = 10  # 10
        self.hauteur = 8  # 8
        self.doc = Docteur(random.randrange(self.largeur), random.randrange(self.hauteur))

        self.dalek = []  # liste
        self.niveau = 0
        self.nb_daleks_par_niveau = 5


    def creer_niveau(self):
        self.niveau += 1
        nb_daleks = self.niveau * self.nb_daleks_par_niveau
        pos_possible = [[self.doc.x, self.doc.y]] # list

        while nb_daleks:
            x = random.randrange(self.largeur)
            y = random.randrange(self.hauteur)

            if [x, y] not in pos_possible:
                pos_possible.append([x, y])
                nb_daleks -= 1

            pos_possible.pop(0) # pop doc
            for i in pos_possible:
                d = Dalek(i[0], i[1])
                self.dalek.append(d)

    def deplacement_dalek(self):

        for i in range(0, self.dalek.__len__()):
            #self.dalek[i] =
            if self.dalek[i].x > self.doc.x:
                self.dalek[i].x -= 1
            elif self.dalek[i].x < self.doc.x:
                self.dalek[i].x += 1

            if self.dalek[i].y > self.doc.y:
                self.dalek[i].y -= 1
            elif self.dalek[i].y < self.doc.y:
                self.dalek[i].y += 1

    def collision(self):
        #self.dalek
        mort = set()

        for i in self.dalek:
            for j in self.dalek:
                if i != j and i.x == j.x and i.y == j.y:
                    mort.add(i)

        for i in mort:
            if i in self.dalek:
                self.dalek.remove(i)

    def teleportage(self):

        x = random.randrange(self.largeur)
        y = random.randrange(self.hauteur)
        pos_invalide = [[self.doc.x, self.doc.y], self.dalek]

        if [x, y] not in pos_invalide:
            self.doc.x = x
            self.doc.y = y

    # def collision2(self): UNE HONTE
    #     # self.dalek
    #     index = set()
    #
    #     for i in range(0, self.dalek.__len__()):
    #         for j in range(0, self.dalek.__len__()):
    #             if i != j and self.dalek[i].x == self.dalek[j].x and self.dalek[i].y == self.dalek[j].y:
    #                 index.add(i)
    #
    #     for i in index:
    #         self.dalek.pop(i)

    def mise_a_jour_jeu(self, reponse):  # blinder le choix
        dico_valeur = {"1": [-1, 1],
                       "2": [0, 1],
                       "3": [1, 1],
                       "4": [-1, 0],
                       "5": [0, 0],
                       "6": [1, 0],
                       "7": [-1, -1],
                       "8": [0, -1],
                       "9": [1, 1],
                       '': [0, 0]}  # si vide, passe son tour

        self.doc.deplacer(dico_valeur[reponse])

        self.deplacement_dalek() # DEPLACEMENT DES DALEKS  A REVOIR ***********


class Docteur():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer(self, param):
        x, y = param
        self.x += x
        self.y += y



class Dalek():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vue():
    def __init__(self):
        pass

    def afficher_menu_principal(self):
        print("\nJEU DE DALEK\n")
        print("MENU PRINCIPAL\n")
        print("1. Commencer une partie")
        print("2. Leaderboard")
        print("3. Quitter\n")
        while True:
            choix = input("Choix : ")
            if choix in ['1', '2', '3']:
                return choix


    def afficher_aire_de_jeu(self, largeur, hauteur, doc, dalek):
        matrice_jeu = []
        for i in range(hauteur):
            ligne = []
            for j in range(largeur):
                ligne.append("-")  # append = ajouter
            matrice_jeu.append(ligne)

        matrice_jeu[doc.y][doc.x] = "D"  # position docteur

        for i in range(0, dalek.__len__()):
            matrice_jeu[dalek[i].y][dalek[i].x] = "X"

        for i in matrice_jeu:
            print(i)

        pos_demandee = input(
            "[z] : zapper \n" "[t] : teleporter\n"  "[1-9] : mouvement \n"  "Votre choix : ")  # input est une string
        print(pos_demandee)
        return pos_demandee


class Controleur():  # À déjà créé l'objet # self # __init__ créé avec la l'objet
    def __init__(self):
        self.modele = Modele()
        self.vue = Vue()

    def demander_refraichissement_vue(self):
        reponse = self.vue.afficher_aire_de_jeu(self.modele.largeur, self.modele.hauteur, self.modele.doc, self.modele.dalek)  # reponse  pour le return pos_demandee
        self.modele.mise_a_jour_jeu(reponse)
        self.modele.collision()
        self.demander_refraichissement_vue()


if __name__ == "__main__":
    c = Controleur()  # creation objet

    #c.vue.afficher_menu_principal()
    c.modele.creer_niveau()
    c.demander_refraichissement_vue()


