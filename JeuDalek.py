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

        self.liste_daleks = []  # liste
        self.liste_ferrailles = []
        self.niveau = 0
        self.nb_daleks_par_niveau = 5
        self.liste_difficulte = ["Facile","Modéré","Difficile"]
        self.difficulte = "Facile"


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
        #NOTE: Il y avait une erreur d'intentation qui poppais des Daleks au hasard, pourquoi on avait juste 3 daleks desfois
        pos_possible.pop(0) # pop doc
        for i in pos_possible:
            d = Dalek(i[0], i[1])
            self.liste_daleks.append(d)

    def deplacement_dalek(self):

        for i in range(0, self.liste_daleks.__len__()):
            #self.liste_daleks[i] =
            if self.liste_daleks[i].x > self.doc.x:
                self.liste_daleks[i].x -= 1
            elif self.liste_daleks[i].x < self.doc.x:
                self.liste_daleks[i].x += 1

            if self.liste_daleks[i].y > self.doc.y:
                self.liste_daleks[i].y -= 1
            elif self.liste_daleks[i].y < self.doc.y:
                self.liste_daleks[i].y += 1

    def collision(self):
        #self.liste_daleks
        mort = set()

        #TODO : Créer le système de ferraille
        for i in self.liste_daleks:
            for j in self.liste_daleks:
                if i != j and i.x == j.x and i.y == j.y:
                    mort.add(i)
                    self.liste_ferrailles.append(i)


        for i in mort:
            if i in self.liste_daleks:
                self.liste_daleks.remove(i)

    def teleportage(self,difficulte:str):

        x = random.randrange(self.largeur)
        y = random.randrange(self.hauteur)

        #pos_invalide = [[self.doc.x, self.doc.y], self.liste_daleks,self.liste_ferrailles]
        pos_invalide = [[self.doc.y,self.doc.x]]
        pos_invalide.extend(self.liste_ferrailles) #Permet d'append une liste
        #Ajout des Daleks et 2 Unités au tour des Daleks
        if difficulte == "Facile":
            for dalek in self.liste_daleks:
                for dalek_x in range(-2,3): # de -2 a +2
                    for dalek_y in range(-2,3):
                        dx =  dalek.x + dalek_x
                        dy = dalek.y + dalek_y
                        #Regarder si la position est dans l'aire de jeu
                        #Entre 0 et les max (hauteur et largeur)
                        if 0 <= dx < self.largeur and 0 <= dy < self.hauteur:
                            pos_invalide.append([dx,dy])
        elif difficulte == "Modéré":
            pos_invalide.extend(self.liste_daleks)

        while [x,y] in pos_invalide:
            x = random.randrange(self.largeur)
            y = random.randrange(self.hauteur)

        if [x, y] not in pos_invalide:
            self.doc.x = x
            self.doc.y = y
       


    # def collision2(self): UNE HONTE
    #     # self.liste_daleks
    #     index = set()
    #
    #     for i in range(0, self.liste_daleks.__len__()):
    #         for j in range(0, self.liste_daleks.__len__()):
    #             if i != j and self.liste_daleks[i].x == self.liste_daleks[j].x and self.liste_daleks[i].y == self.liste_daleks[j].y:
    #                 index.add(i)
    #
    #     for i in index:
    #         self.liste_daleks.pop(i)

    def mise_a_jour_jeu(self, reponse : chr,difficulte:str):  # blinder le choix
        dico_valeur = {"1": [-1, 1],
                       "2": [0, 1],
                       "3": [1, 1],
                       "4": [-1, 0],
                       "5": [0, 0],
                       "6": [1, 0],
                       "7": [-1, -1],
                       "8": [0, -1],
                       "9": [1, -1],
                       '': [0, 0]}  # si vide, passe son tourt
        if reponse in dico_valeur:
            self.doc.deplacer(dico_valeur[reponse])
            self.deplacement_dalek() ## COMPORTEMENT: AUCUN DEPLACEMENT DE DALEK LORS DUN TELEPORT
        elif reponse == 't' or reponse == 'T':
            self.teleportage(difficulte)
        #TODO:  Ajouter zapper
        #if reponse == 'z' or reponse == 'Z':



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

class Ferraille():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Vue():
    def __init__(self):
        pass

    def afficher_difficulte(self):
        print("Choisissez votre difficulté:\n")
        print("1. Facile\n2. Modéré\n3. Difficile\n")
        while True:
            choix = input("Votre Choix: ")
            if choix in ['1','2','3']:
                return choix
        
    def afficher_menu_principal(self,difficulte):
        print("\nJEU DE DALEK\n")
        print("MENU PRINCIPAL\n")
        print("1. Commencer une partie")
        print("2. Leaderboard")
        print("3. Quitter\n")
        while True:
            choix = input("Choix : ")
            if choix in ['1', '2', '3']:
                return choix
    #def debug_affichage(nb_daleks,nb_daleks_par_niveau):
    #    print("Affichage Debug \nNombre de Daleks: " + str(nb_daleks))
    #    print("\nNiveau : " + str(niveau) + " Nombre de Daleks pour le niveau " + str(niveau) + ": " + str(nb_daleks_par_niveau*niveau))
    #    print("\nNombre de collisions: " + str(nb_collisions))

    def afficher_aire_de_jeu(self, largeur, hauteur, doc, liste_daleks,liste_ferrailles):
        matrice_jeu = []
        for i in range(hauteur):
            ligne = []
            for j in range(largeur):
                ligne.append("-")  # append = ajouter
            matrice_jeu.append(ligne)

        matrice_jeu[doc.y][doc.x] = "D"  # position docteur
        print("Position du Docteur [x,y] : " + "[" + str(doc.x+1) + "," + str(doc.y+1) + "]")
        for i in range(0, liste_daleks.__len__()):
            matrice_jeu[liste_daleks[i].y][liste_daleks[i].x] = "X"
        #TODO Ajouter les positions de ferraille
        for i in range(0, liste_ferrailles.__len__()):
            matrice_jeu[liste_ferrailles[i].y][liste_ferrailles[i].x] = "F"
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

    def choisir_difficulte(self):
        reponse = self.vue.afficher_difficulte()
        self.modele.difficulte = self.modele.liste_difficulte[reponse-1]

    def demander_refraichissement_vue(self):
        reponse = self.vue.afficher_aire_de_jeu(self.modele.largeur, self.modele.hauteur, self.modele.doc, self.modele.liste_daleks, self.modele.liste_ferrailles)  # reponse  pour le return pos_demandee
        self.modele.mise_a_jour_jeu(reponse)
        self.modele.collision()
        self.demander_refraichissement_vue()


if __name__ == "__main__":
    c = Controleur()  # creation objet

    c.vue.afficher_menu_principal()
    c.modele.creer_niveau()
    c.demander_refraichissement_vue()


