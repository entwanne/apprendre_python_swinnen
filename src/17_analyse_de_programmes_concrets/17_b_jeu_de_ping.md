## 17-B - Jeu de Ping

Dans les pages qui suivent, vous trouverez le script correspondant à un
petit programme complet. Ce programme vous est fourni à titre d'exemple
de ce que vous pouvez envisager de développer vous-même comme projet
personnel de synthèse. Il vous montre encore une fois comment vous
pouvez utiliser plusieurs classes afin de construire un script bien
structuré. Il vous montre également comment vous pouvez paramétrer une
application graphique de manière à ce que tout y soit
*redimensionnable*.

### 17-B-1 - Principe {#article.xml#Ld0e70931 .TitreSection2}

Le «jeu» mis en œuvre ici est plutôt une sorte d'exercice mathématique.
Il se joue sur un panneau où est représenté un quadrillage de dimensions
variables, dont toutes les cases sont occupées par des pions. Ces pions
possèdent chacun une face blanche et une face noire (comme les pions du
jeu *Othello/Reversi*), et au début de l'exercice ils présentent tous
leur face blanche par-dessus.

Lorsque l'on clique sur un pion à l'aide de la souris, les 8 pions
adjacents se retournent. Le jeu consiste alors à essayer de retourner
tous les pions, en cliquant sur certains d'entre eux.

L'exercice est très facile avec une grille de 2 × 2 cases (il suffit de
cliquer sur chacun des 4 pions). Il devient plus difficile avec des
grilles plus grandes, et est même tout à fait impossible avec certaines
d'entre elles. À vous de déterminer lesquelles !

Ne négligez pas d'étudier le cas des grilles 1 × n.

> Vous trouverez la discussion complète du jeu de Ping, sa théorie et
> ses extensions, dans la revue « Pour la science » n^o^ 298 du mois
> d'Août 2002, pages 98 à 102. Une copie de cet article est disponible
> en ligne, sur :\
>  http://www2.lifl.fr/\~delahaye/dnalor/JeuAEpisodes.pdf

### 17-B-2 - Programmation {#article.xml#Ld0e70952 .TitreSection2}

Lorsque vous développez un projet logiciel, veillez toujours à faire
l'effort de décrire votre démarche le plus clairement possible.
Commencez par établir un cahier des charges détaillé, et ne négligez pas
de commenter ensuite très soigneusement votre code, au fur et à mesure
de son élaboration (et non après coup !).

En procédant ainsi, vous vous forcez vous-même à exprimer ce que vous
souhaitez que la machine fasse, ce qui vous aide à analyser les
problèmes et à structurer convenablement votre code.

#### 17-B-2-A - Cahier des charges du logiciel à développer {#article.xml#Ld0e70959 .TitreSection3}

-   L'application sera construite sur la base d'une fenêtre principale
    comportant le panneau de jeu et une barre de menus.
-   L'ensemble devra être extensible à volonté par l'utilisateur, les
    cases du panneau devant cependant rester carrées.
-   Les options du menu permettront de :
-   La programmation fera appel à trois classes :
-   Le panneau de jeu sera dessiné dans un canevas, lui-même installé
    dans un cadre (*frame*). En fonction des redimensionnements opérés
    par l'utilisateur, le cadre occupera à chaque fois toute la place
    disponible : il se présentera donc au programmeur comme un rectangle
    quelconque, dont les dimensions doivent servir de base au calcul des
    dimensions de la grille à dessiner.
-   Puisque les cases de cette grille doivent rester carrées, il est
    facile de commencer par calculer leur taille maximale, puis
    d'établir les dimensions du canevas en fonction de celle-ci.
-   Gestion du clic de souris : on liera au canevas une
    méthode-gestionnaire pour l'événement \. Les
    coordonnées de l'événement serviront à déterminer dans quelle case
    de la grille (n^o^ de ligne et n^o^ de colonne) le clic a été
    effectué, quelles que soient les dimensions de cette grille. Dans
    les 8 cases adjacentes, les pions présents seront alors « retournés
    » (échange des couleurs noire et blanche).
-   choisir les dimensions de la grille (en nombre de cases) ;
-   réinitialiser le jeu (c'est-à-dire disposer tous les pions avec leur
    face blanche au-dessus) ;
-   afficher le principe du jeu dans une fenêtre d'aide ;
-   terminer (fermer l'application).
-   une classe principale ;
-   une classe pour la barre de menus ;
-   une classe pour le panneau de jeu.



```python
###########################################
#  Jeu de ping		       #
#  Références : Voir article de la revue  #
#  <Pour la science>, Aout 2002      #
#		      #
# (C) Gérard Swinnen (Verviers, Belgique) #
# http://www.ulg.ac.be/cifen/inforef/swi  #
#		      #
#  Version du 29/09/2002 - Licence : GPL  #
###########################################
 
from tkinter import *
 
class MenuBar(Frame):
  """Barre de menus déroulants"""
  def __init__(self, boss =None):
      Frame.__init__(self, borderwidth =2, relief =GROOVE)
      ##### Menu <Fichier> #####
      fileMenu = Menubutton(self, text ='Fichier')
      fileMenu.pack(side =LEFT, padx =5)
      me1 = Menu(fileMenu)
      me1.add_command(label ='Options', underline =0,
	      command = boss.options)
      me1.add_command(label ='Restart', underline =0,
	      command = boss.reset)
      me1.add_command(label ='Terminer', underline =0,
	      command = boss.quit)
      fileMenu.configure(menu = me1)	
 
      ##### Menu <Aide> #####
      helpMenu = Menubutton(self, text ='Aide')
      helpMenu.pack(side =LEFT, padx =5)
      me1 = Menu(helpMenu)
      me1.add_command(label ='Principe du jeu', underline =0,
	      command = boss.principe)
      me1.add_command(label ='A propos ...', underline =0,
	      command = boss.aPropos)
      helpMenu.configure(menu = me1)	    
 
class Panneau(Frame):
  """Panneau de jeu (grille de n x m cases)"""
  def __init__(self, boss =None):
      # Ce panneau de jeu est constitué d'un cadre redimensionnable
      # contenant lui-même un canevas. A chaque redimensionnement du
      # cadre, on calcule la plus grande taille possible pour les
      # cases (carrées) de la grille, et on adapte les dimensions du
      # canevas en conséquence.
      Frame.__init__(self)
      self.nlig, self.ncol = 4, 4      # Grille initiale = 4 x 4
      # Liaison de l'événement <resize> à un gestionnaire approprié :
      self.bind("<Configure>", self.redim)
      # Canevas :
      self.can =Canvas(self, bg ="dark olive green", borderwidth =0,
	    highlightthickness =1, highlightbackground ="white")
      # Liaison de l'événement <clic de souris> à son gestionnaire :
      self.can.bind("<Button-1>", self.clic)
      self.can.pack()
      self.initJeu()
 
  def initJeu(self):
      "Initialisation de la liste mémorisant l'état du jeu"
      self.etat =[]		# construction d'une liste de listes
      for i in range(12):	  # (équivalente à un tableau 
      self.etat.append([0]*12)	 #  de 12 lignes x 12 colonnes) 
 
  def redim(self, event):
      "Opérations effectuées à chaque redimensionnement"
      # Les propriétés associées à l'événement de reconfiguration
      # contiennent les nouvelles dimensions du cadre :
      self.width, self.height = event.width -4, event.height -4
      # La différence de 4 pixels sert à compenser l'épaisseur
      # de la 'highlightbordure" entourant le canevas
      self.traceGrille()
 
  def traceGrille(self):
      "Dessin de la grille, en fonction des options & dimensions"
      # largeur et hauteur maximales possibles pour les cases :
      lmax = self.width/self.ncol     
      hmax = self.height/self.nlig
      # Le coté d'une case sera égal à la plus petite de ces dimensions :
      self.cote = min(lmax, hmax)
      # -> établissement de nouvelles dimensions pour le canevas :
      larg, haut = self.cote*self.ncol, self.cote*self.nlig
      self.can.configure(width =larg, height =haut)
      # Tracé de la grille :
      self.can.delete(ALL)	    # Effacement dessins antérieurs
      s =self.cote	       
      for l in range(self.nlig -1):	 # lignes horizontales
      self.can.create_line(0, s, larg, s, fill="white")
      s +=self.cote
      s =self.cote
      for c in range(self.ncol -1):	 # lignes verticales
      self.can.create_line(s, 0, s, haut, fill ="white")
      s +=self.cote
      # Tracé de tous les pions, blancs ou noirs suivant l'état du jeu :   
      for l in range(self.nlig):
      for c in range(self.ncol):
	  x1 = c *self.cote +5		# taille des pions = 
	  x2 = (c +1)*self.cote -5	  # taille de la case -10
	  y1 = l *self.cote +5		#
	  y2 = (l +1)*self.cote -5
	  coul =["white","black"][self.etat[l][c]]
	  self.can.create_oval(x1, y1, x2, y2, outline ="grey",
		   width =1, fill =coul)
 
  def clic(self, event):
      "Gestion du clic de souris : retournement des pions"
      # On commence par déterminer la ligne et la colonne :
      lig, col = int(event.y/self.cote), int(event.x/self.cote)
      # On traite ensuite les 8 cases adjacentes :
      for l in range(lig -1, lig+2):
      if l <0 or l >= self.nlig:
	  continue
      for c in range(col -1, col +2):
	  if c <0 or c >= self.ncol:
	  continue
	  if l ==lig and c ==col:
	  continue
	  # Retournement du pion par inversion logique :
	  self.etat[l][c] = not (self.etat[l][c])
      self.traceGrille() 
 
 
class Ping(Frame):
  """corps principal du programme"""	
  def __init__(self):
      Frame.__init__(self)
      self.master.geometry("400x300")
      self.master.title(" Jeu de Ping")
 
      self.mbar = MenuBar(self)
      self.mbar.pack(side =TOP, expand =NO, fill =X)
 
      self.jeu =Panneau(self)
      self.jeu.pack(expand =YES, fill=BOTH, padx =8, pady =8)
 
      self.pack()
 
  def options(self):
      "Choix du nombre de lignes et de colonnes pour la grille"
      opt =Toplevel(self)
      curL =Scale(opt, length =200, label ="Nombre de lignes :",
	orient =HORIZONTAL,
	from_ =1, to =12, command =self.majLignes)
      curL.set(self.jeu.nlig)	   # position initiale du curseur 
      curL.pack()
      curH =Scale(opt, length =200, label ="Nombre de colonnes :",
	orient =HORIZONTAL,
	from_ =1, to =12, command =self.majColonnes)
      curH.set(self.jeu.ncol)	    
      curH.pack()
 
  def majColonnes(self, n):
      self.jeu.ncol = int(n)
      self.jeu.traceGrille()
 
  def majLignes(self, n):
      self.jeu.nlig = int(n)	  
      self.jeu.traceGrille()
 
  def reset(self):
      self.jeu.initJeu()
      self.jeu.traceGrille()
 
  def principe(self):
      "Fenêtre-message contenant la description sommaire du principe du jeu" 
      msg =Toplevel(self)
      Message(msg, bg ="navy", fg ="ivory", width =400,
      font ="Helvetica 10 bold", 
      text ="Les pions de ce jeu possèdent chacun une face blanche et "\
      "une face noire. Lorsque l'on clique sur un pion, les 8 "\
      "pions adjacents se retournent.\nLe jeu consiste a essayer "\
      "de les retouner tous.\n\nSi l'exercice se révèle très facile "\
      "avec une grille de 2 x 2 cases. Il devient plus difficile avec "\
      "des grilles plus grandes. Il est même tout à fait impossible "\
      "avec certaines grilles.\nA vous de déterminer lesquelles !\n\n"\
      "Réf : revue 'Pour la Science' - Aout 2002")\
      .pack(padx =10, pady =10)       
 
  def aPropos(self):
      "Fenêtre-message indiquant l'auteur et le type de licence" 
      msg =Toplevel(self)
      Message(msg, width =200, aspect =100, justify =CENTER,
      text ="Jeu de Ping\n\n(C) Gérard Swinnen, Aout 2002.\n"\
      "Licence = GPL").pack(padx =10, pady =10)
 
if __name__ == '__main__':
  Ping().mainloop()
```



> - Rappel -

> Si vous souhaitez expérimenter ces programmes sans avoir à les
> réécrire, vous pouvez trouver leur code source à l*'*adresse :\
>  http://www.inforef.be/swi/python.htm.

