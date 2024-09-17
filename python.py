import random

class Vue():
    def __init__(self):
        pass
    def afficherairedejeu(self, largeur, hauteur, doc):
        matrice_jeu = []
        for i in range(hauteur):
            ligne = []
            for j in range(largeur):
                ligne.append("-")
            matrice_jeu.append(ligne)
            
        matrice_jeu[doc.y][doc.x] = "D"
        
        
        for x in matrice_jeu:
            print(x)
            
        pos_demander = input("QUEL EST LE MOVE ???")
        return pos_demander

class Docteur():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def deplacer(self, param):
        x, y = param
        self.x += x
        self.y += y

class Dalek():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Modele():
    def __init__(self):
        self.largeur = 12
        self.hauteur = 8
        x = random.randrange(self.largeur)
        y = random.randrange(self.hauteur)

        self.niveau = 0
        self.nbDalek = 0
        self.doc = Docteur(x, y)
    
    def miseajourjeu(self, reponse):
        dico_valeur = {"4":[-1, 0],
                       "7":[-1,-1],
                       "1":[-1,1]}
        
        self.doc.deplacer(dico_valeur[reponse])

    def creerNiveau(self):
        self.niveau += 1
        nb_daleks = self.niveau * self.nbDaleks



class Controleur():
    def __init__(self):
        self.model = Modele()
        self.vue = Vue()
    
    def DemanderRefreshDeVue(self):
        reponse = self.vue.afficherairedejeu(self.model.largeur, self.model.hauteur, self.model.doc)
        self.model.miseajourjeu(reponse)
        self.DemanderRefreshDeVue()
        
        
if __name__ == "__main__":
    c = Controleur()
    c.DemanderRefreshDeVue()