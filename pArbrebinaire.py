class ArbreBinaire:
    def __init__(self,v=None,g=None,d=None):
        assert g is None or type(g)==ArbreBinaire, "le paramètre g est un objet ArbreBinaire ou None"
        assert d is None or type(d)==ArbreBinaire, "le paramètre d est un objet ArbreBinaire ou None"
        self.valeur=v
        self.gauche=g
        self.droit=d
        
    def taille(self):
        if self.valeur is None:
            return 0
        else:
            return 1 + self.gauche.taille() + self.droit.taille()
    
    def hauteur(self):
        if self.valeur is None:
            return 0
        else:
            return 1+max(self.gauche.hauteur(),self.droit.hauteur())
        
    def infixe(self):
        if self.valeur is None:
            pass
        else:
            self.gauche.infixe()
            print(self.valeur, end=", ")
            self.droit.infixe()
            
        
    def prefixe(self):
        if self.valeur is None:
            pass
        else:
            print(self.valeur, end=", ")
            self.gauche.prefixe()
            self.droit.prefixe()
        
    def postfixe(self):
        if self.valeur is None:
            pass
        else:
            self.gauche.postfixe()
            self.droit.postfixe()
            print(self.valeur, end=", ")
    
    def largeur(self):
        h = hauteur(self)
        for i in range(1, h+1):
            Niveau(self, i)
 
 
    def Niveau(abr, niveau):
        if abr is None:
            return
        if niveau == 1:
            print(abr.valeur,end=', ')
        elif niveau > 1:
            Niveau(abr.gauche, niveau-1)
            Niveau(abr.droit, niveau-1)
        
    
