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
        self.nb_zappers = 0

    def choix_difficulte(self,reponse:int):
        self.difficulte = self.liste_difficulte[int(reponse)-1]
        print("difficulte: "+self.difficulte)

    def creer_niveau(self):
        self.niveau += 1
        self.nb_zappers += 1
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

    def collision_docteur(self):
        for i in self.liste_daleks:
            if self.doc.x == i.x and self.doc.y == i.y:
                print("BAM BAM DEAD")
                #Faire un ecran de mort

    def collision(self):
        #self.liste_daleks
        mort = set()

        for i in self.liste_daleks:
            for j in self.liste_daleks:
                if i != j and i.x == j.x and i.y == j.y:
                    mort.add(i)
                    self.liste_ferrailles.append(i)

        for i in mort:
            if i in self.liste_daleks:
                self.liste_daleks.remove(i)
                print(self.liste_daleks)
    ##Validation de fin de niveau 
        if self.liste_daleks == []:
            self.creer_niveau()

    def teleportage(self):

        x = random.randrange(self.largeur)
        y = random.randrange(self.hauteur)

        #pos_invalide = [[self.doc.x, self.doc.y], self.liste_daleks,self.liste_ferrailles]
        pos_invalide = [[self.doc.y,self.doc.x]]
        pos_invalide.extend(self.liste_ferrailles) #Permet d'append une liste
        #Ajout des Daleks et 2 Unités au tour des Daleks
        if self.difficulte == "Facile":
            for dalek in self.liste_daleks:
                for dalek_x in range(-2,3): # de -2 a +2
                    for dalek_y in range(-2,3):
                        dx =  dalek.x + dalek_x
                        dy = dalek.y + dalek_y
                        #Regarder si la position est dans l'aire de jeu
                        #Entre 0 et les max (hauteur et largeur)
                        if 0 <= dx < self.largeur and 0 <= dy < self.hauteur:
                            pos_invalide.append([dx,dy])
        elif self.difficulte == "Modéré":
            pos_invalide.extend(self.liste_daleks)

        while [x,y] in pos_invalide:
            x = random.randrange(self.largeur)
            y = random.randrange(self.hauteur)

        if [x, y] not in pos_invalide:
            self.doc.x = x
            self.doc.y = y

    def zapper(self):
        positions_zapped = []
        for doc_x in range(-1,2):
            for doc_y in range(-1,2):
                zap_x = self.doc.x + doc_x
                zap_y = self.doc.x + doc_x
                for daleks in self.liste_daleks:
                    if daleks.x == zap_x and daleks.y == zap_y:
                        self.liste_daleks.remove(daleks)
                        self.liste_ferrailles.append(daleks)
                        


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
        elif reponse == 'z' or reponse == 'Z':
            self.zapper()



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
        #while True:
        #    choix = input("Votre Choix: ")
        #    if choix in ['1','2','3']:
        #        return choix
        
    def afficher_menu_principal(self):
        print("\nJEU DE DALEK\n")
        print("MENU PRINCIPAL\n")
        print("1. Commencer une partie")
        print("2. Leaderboard")
        print("3. Quitter\n")

    def afficher_aire_de_jeu(self, largeur:int, hauteur:int, doc:list, liste_daleks:list, liste_ferrailles:list, nb_zappers:int,niveau):
        # display the game board
        matrice_jeu = [["[   ]" for _ in range(largeur)] for _ in range(hauteur)]
        matrice_jeu[doc.y][doc.x] = "[ ¤ ]"  
        for dalek in liste_daleks:
            matrice_jeu[dalek.y][dalek.x] = "[ Ð ]"  
        for ferraille in liste_ferrailles:
            matrice_jeu[ferraille.y][ferraille.x] = "[ † ]"  
        for row in matrice_jeu:
            print("".join(row))
        print(f"Position du Docteur: [{doc.x+1}, {doc.y+1}] || Nombre de zappeurs: "+str(nb_zappers)+" || NIVEAU "+str(niveau))

class Controleur():  # À déjà créé l'objet # self # __init__ créé avec la l'objet
    def __init__(self):
        self.modele = Modele()
        self.vue = Vue()

    def demarrer_jeu(self):
        self.demander_choix_menu()

    def demander_choix_menu(self):
        self.vue.afficher_menu_principal()
        while True:
            reponse = input("Choix : ")
            if reponse in ['1','2','3']:
                match reponse:
                    case '1':
                        self.choisir_difficulte()
                    case '2':
                        ##TODO: AJOUTER LEADERBOARD
                        self.choisir_difficulte()
                    case '3':
                        exit()

    def choisir_difficulte(self):
        self.vue.afficher_difficulte()
        is_valid =  True
        while is_valid:
            reponse = input("Votre Choix: ")
            if reponse in ['1','2','3']:
                self.modele.choix_difficulte(reponse)
                c.modele.creer_niveau()
                c.demander_refraichissement_vue()
                

    def demander_refraichissement_vue(self):
        self.vue.afficher_aire_de_jeu(self.modele.largeur, self.modele.hauteur, self.modele.doc, self.modele.liste_daleks, self.modele.liste_ferrailles,self.modele.nb_zappers,self.modele.niveau)
        reponse = input("Votre choix (1-9 for movement, 't' to teleport): ")
        self.modele.mise_a_jour_jeu(reponse,self.modele.difficulte)
        self.modele.collision()
        self.demander_refraichissement_vue()


if __name__ == "__main__":
    c = Controleur()  # creation objet

    #c.vue.afficher_menu_principal()
    c.demarrer_jeu()
    


