## 15-E - Intégration de widgets composites dans une application synthèse

Dans les exercices précédents, nous avons construit deux nouvelles
classes de widgets : le widget **OscilloGraphe()**, canevas spécialisé
pour le dessin de sinusoïdes, et le widget **ChoixVibra()**, panneau de
contrôle à trois curseurs permettant de choisir les paramètres d'une
vibration.

Ces widgets sont désormais disponibles dans les modules **oscillo.py**
et **curseurs.py**[^note_79].

Nous allons à présent les utiliser dans une application synthèse : un
widget **OscilloGraphe()** y affiche un, deux, ou trois graphiques
superposés, de couleurs différentes, chacun d'entre eux étant soumis au
contrôle d'un widget **ChoixVibra().**

Le script correspondant est reproduit ci-après.

Nous attirons votre attention sur la technique mise en œuvre pour
provoquer un rafraîchissement de l'affichage dans le canevas par
l'intermédiaire d'un événement, chaque fois que l'utilisateur effectue
une action quelconque au niveau de l'un des panneaux de contrôle.

Rappelez-vous que les applications destinées à fonctionner dans une
interface graphique doivent être conçues comme des « programmes pilotés
par les événements » (voir page ).

En préparant cet exemple, nous avons arbitrairement décidé que
l'affichage des graphiques serait déclenché par un événement
particulier, tout à fait similaire à ceux que génère le système
d'exploitation lorsque l'utilisateur accomplit une action quelconque.
Dans la gamme (très étendue) d'événements possibles, nous en avons
choisi un qui ne risque guère d'être utilisé pour d'autres raisons,
pendant que notre application fonctionne : la combinaison de touches
\<Maj-Ctrl-Z\>.



![](images/image46.png)





```python
from oscillo import *
from curseurs import *
 
class ShowVibra(Frame):
  """Démonstration de mouvements vibratoires harmoniques"""
  def __init__(self, boss =None):
      Frame.__init__(self)	# constructeur de la classe parente
      self.couleur = ['dark green', 'red', 'purple']
      self.trace = [0]*3      # liste des tracés (courbes à dessiner)
      self.controle = [0]*3	 # liste des panneaux de contrôle
 
      # Instanciation du canevas avec axes X et Y : 
      self.gra = OscilloGraphe(self, larg =400, haut=200)
      self.gra.configure(bg ='white', bd=2, relief=SOLID)
      self.gra.pack(side =TOP, pady=5)
 
      # Instanciation de 3 panneaux de contrôle (curseurs) : 
      for i in range(3):
      self.controle[i] = ChoixVibra(self, self.couleur[i])
      self.controle[i].pack()
 
      # Désignation de l'événement qui déclenche l'affichage des tracés :    
      self.master.bind('<Control-Z>', self.montreCourbes)
      self.master.title('Mouvements vibratoires harmoniques')
      self.pack()
 
  def montreCourbes(self, event):
      """(Ré)Affichage des trois graphiques élongation/temps"""   
      for i in range(3):
 
      # D'abord, effacer le tracé précédent (éventuel) :
      self.gra.delete(self.trace[i])
 
      # Ensuite, dessiner le nouveau tracé :  
      if self.controle[i].chk.get():
	  self.trace[i] = self.gra.traceCourbe(
		  coul = self.couleur[i],
		  freq = self.controle[i].freq,
		  phase = self.controle[i].phase,
		  ampl = self.controle[i].ampl) 	  
 
#### Code pour tester la classe : ###
 
if __name__ == '__main__':    
  ShowVibra().mainloop()
```



### 15-E-1 - Commentaires {#article.xml#Ld0e48661 .TitreSection2}

-   Lignes 1-2 : Nous pouvons nous passer d'importer le module tkinter :
    chacun de ces deux modules s'en charge déjà.
-   Ligne 4 : Puisque nous commençons à connaître les bonnes techniques,
    nous décidons de construire l'application elle-même sous la forme
    d'une nouvelle classe de widget, dérivée de la classe **Frame()** :
    ainsi nous pourrons plus tard l'intégrer toute entière dans d'autres
    projets, si le cœur nous en dit.
-   Lignes 8-10 : Définition de quelques variables d'instance (3 listes)
    : les trois courbes tracées seront des objets graphiques, dont les
    couleurs sont pré-définies dans la liste **self.couleur** ; nous
    devons préparer également une liste **self.trace** pour mémoriser
    les références de ces objets graphiques, et enfin une liste
    **self.controle** pour mémoriser les références des trois panneaux
    de contrôle.
-   Lignes 13 à 15 : Instanciation du widget d'affichage. Étant donné
    que la classe **OscilloGraphe()** a été obtenue par dérivation de la
    classe **Canvas()**, il est toujours possible de configurer ce
    widget en redéfinissant les options spécifiques de cette classe
    (ligne 13).
-   Lignes 18 à 20 : Pour instancier les trois widgets « panneau de
    contrôle », on utilise une boucle. Leurs références sont mémorisées
    dans la liste **self**.**controle** préparée à la ligne 10. Ces
    panneaux de contrôle sont instanciés comme esclaves du présent
    widget, par l'intermédiaire du paramètre **self**. Un second
    paramètre leur transmet la couleur du tracé à contrôler.
-   ![](images/image44.gif)
-   Lignes 27 à 40 : La méthode décrite ici est le gestionnaire des
    événements \<Maj-Ctrl-Z\> spécifiquement déclenchés par nos widgets
    **ChoixVibra()** (ou « panneaux de contrôle »), chaque fois que
    l'utilisateur exerce une action sur un curseur ou une case à cocher.
    Dans tous les cas, les graphiques éventuellement présents sont
    d'abord effacés (ligne 28) à l'aide de la méthode **delete()** : le
    widget **OscilloGraphe()** a hérité cette méthode de sa classe
    parente **Canvas()**.\
     Ensuite, de nouvelles courbes sont retracées, pour chacun des
    panneaux de contrôle dont on a coché la case « Afficher ». Chacun
    des objets ainsi dessinés dans le canevas possède un numéro de
    référence, renvoyé par la méthode **traceCourbe()** de notre widget
    **OscilloGraphe()**.\
     Les numéros de référence de nos dessins sont mémorisés dans la
    liste **self.trace**. Ils permettent d'effacer individuellement
    chacun d'entre eux (cf. instruction de la ligne 28).
-   Lignes 38-40 : Les valeurs de fréquence, phase et amplitude que l'on
    transmet à la méthode **traceCourbe()** sont les attributs
    d'instance correspondants de chacun des trois panneaux de contrôle,
    eux-mêmes mémorisés dans la liste **self.controle**. Nous pouvons
    récupérer ces attributs en utilisant la qualification des noms par
    points.

Exercices

.Modifiez le script, de manière à obtenir l'aspect ci-dessous (écran
d'affichage avec grille de référence, panneaux de contrôle entourés d'un
sillon) :

.Modifiez le script, de manière à faire apparaître et contrôler 4
graphiques au lieu de trois. Pour la couleur du quatrième graphique,
choisissez par exemple : 'blue', 'navy', 'maroon'...

.Aux lignes 33-35, nous récupérons les valeurs des fréquence, phase et
amplitude choisies par l'utilisateur sur chacun des trois panneaux de
contrôle, en accédant directement aux attributs d'instance
correspondants. Python autorise ce raccourci - et c'est bien pratique -
mais cette technique est dangereuse. Elle enfreint l'une des
recommandations de la théorie générale de la « programmation orientée
objet », qui préconise que l'accès aux propriétés des objets soit
toujours pris en charge par des méthodes spécifiques. Pour respecter
cette recommandation, ajoutez à la classe **ChoixVibra()** une méthode
supplémentaire que vous appellerez **valeurs()**, et qui renverra un
tuple contenant les valeurs de la fréquence, la phase et l'amplitude
choisies. Les lignes 33 à 35 du présent script pourront alors être
remplacées par quelque chose comme :

**freq, phase, ampl =
self.control[i].valeurs()**

.Écrivez une petite application qui fait apparaître une fenêtre avec un
canevas et un widget curseur (**Scale**). Dans le canevas, dessinez un
cercle, dont l'utilisateur pourra faire varier la taille à l'aide du
curseur.

.Écrivez un script qui créera deux classes : une classe Application,
dérivée de **Frame()**, dont le constructeur instanciera un canevas de
400 × 400 pixels, ainsi que deux boutons. Dans le canevas, vous
instancierez un objet de la classe **Visage** décrite ci-après.\
 La classe **Visage** servira à définir des objets graphiques censés
représenter des visages humains simplifiés. Ces visages seront
constitués d'un cercle principal dans lequel trois ovales plus petits
représenteront deux yeux et une bouche (ouverte). Une méthode « fermer »
permettra de remplacer l'ovale de la bouche par une ligne horizontale.
Une méthode « ouvrir » permettra de restituer la bouche de forme ovale.\
 Les deux boutons définis dans la classe **Application** serviront
respectivement à fermer et à ouvrir la bouche de l'objet **Visage**
installé dans le canevas. Vous pouvez vous inspirer de l'exemple de la
page pour composer une partie du code.

.Exercice de synthèse : élaboration d'un dictionnaire de couleurs.\
 But : réaliser un petit programme utilitaire, qui puisse vous aider à
construire facilement et rapidement un nouveau dictionnaire de couleurs,
lequel permettrait l'accès technique à une couleur quelconque par
l'intermédiaire de son nom usuel en français.

Contexte : En manipulant divers objets colorés avec tkinter, vous avez
constaté que cette bibliothèque graphique accepte qu'on lui désigne les
couleurs les plus fondamentales sous la forme de chaînes de caractères
contenant leur nom en anglais : *red, blue, yellow,* etc.

Vous savez cependant qu'un ordinateur ne peut traiter que des
informations numérisées. Cela implique que la désignation d'une couleur
quelconque doit nécessairement tôt ou tard être encodée sous la forme
d'un nombre. Il faut bien entendu adopter pour cela une une convention,
et celle-ci peut varier d'un système à un autre. L'une de ces
conventions, parmi les plus courantes, consiste à représenter une
couleur à l'aide de trois octets, qui indiqueront respectivement les
intensités des trois composantes rouge, verte et bleue de cette couleur.

Cette convention peut être utilisée avec tkinter pour accéder à
n'importe quelle nuance colorée. Vous pouvez en effet lui indiquer la
couleur d'un élément graphique quelconque, à l'aide d'une chaîne de 7
caractères telle que **'\#00FA4E'.
**Dans cette chaîne, le premier caractère (\#) signifie que ce
qui suit est une valeur hexadécimale. Les six caractères suivants
représentent les 3 valeurs hexadécimales des 3 composantes rouge, vert
et bleu.

Pour visualiser concrètement la correspondance entre une couleur
quelconque et son code, vous pouvez explorer les ressources de divers
programmes de traitement d'images, tels par exemple les excellents
programmes libres « Gimp » et « Inkscape ».

Étant donné qu'il n'est pas facile pour les humains que nous sommes de
mémoriser de tels codes hexadécimaux, tkinter est également doté d'un
dictionnaire de conversion, qui autorise l'utilisation de noms communs
pour un certain nombre de couleurs parmi les plus courantes, mais cela
ne marche que pour des noms de couleurs exprimés en anglais.

Le but du présent exercice est de réaliser un logiciel qui facilitera la
construction d'un dictionnaire équivalent en français, lequel pourrait
ensuite être incorporé à l'un ou l'autre de vos propres programmes. Une
fois construit, ce dictionnaire serait donc de la forme :\
**{'vert':'\#00FF00',
'bleu':'\#0000FF', ... etc
...}**.

***Cahier des charges :***

L'application à réaliser sera une application graphique, construite
autour d'une classe. Elle comportera une fenêtre avec un certain nombre
de champs d'entrée et de boutons, afin que l'utilisateur puisse aisément
encoder de nouvelles couleurs en indiquant à chaque fois son nom
français dans un champ, et son code hexadécimal dans un autre.\
 Lorsque le dictionnaire contiendra déjà un certain nombre de données,
il devra être possible de le tester, c'est-à-dire d'entrer un nom de
couleur en français et de retrouver le code hexadécimal correspondant à
l'aide d'un bouton (avec affichage éventuel d'une zone colorée).\
 Un bouton provoquera l'enregistrement du dictionnaire dans un fichier
texte. Un autre permettra de reconstruire le dictionnaire à partir du
fichier.

.Le script ci-dessous correspond à une ébauche de projet dessinant des
ensembles de dés à jouer disposés à l'écran de plusieurs manières
différentes (cette ébauche pourrait être une première étape dans la
réalisation d'un logiciel de jeu). L'exercice consistera à analyser ce
script et à le compléter. Vous vous placerez ainsi dans la situation
d'un programmeur chargé de continuer le travail commencé par quelqu'un
d'autre, ou encore dans celle de l'informaticien prié de participer à un
travail d'équipe.\
 A) Commencez par analyser ce script et ajoutez-y des commentaires, en
particulier aux lignes marquées : `#***`, pour montrer que vous
comprenez ce que doit faire le programme à ces emplacements :



```python
from tkinter import *
class FaceDom(object):
  def __init__(self, can, val, pos, taille =70):
      self.can =can
      # ***
      x, y, c = pos[0], pos[1], taille/2
      can.create_rectangle(x -c, y-c, x+c, y+c, fill ='ivory', width =2)
      d = taille/3
      # ***
      self.pList =[]
      # ***
      pDispo = [((0,0),), ((-d,d),(d,-d)), ((-d,-d), (0,0), (d,d))]
      disp = pDispo[val -1]
      # ***
      for p in disp:
      self.cercle(x +p[0], y +p[1], 5, 'red')
 
  def cercle(self, x, y, r, coul):
      # ***
      self.pList.append(self.can.create_oval(x-r, y-r, x+r, y+r, fill=coul))
 
  def effacer(self):
      # ***
      for p in self.pList:
      self.can.delete(p)
 
class Projet(Frame):
  def __init__(self, larg, haut):
      Frame.__init__(self)
      self.larg, self.haut = larg, haut
      self.can = Canvas(self, bg='dark green', width =larg, height =haut)
      self.can.pack(padx =5, pady =5)
      # ***
      bList = [("A", self.boutA), ("B", self.boutB),
	("C", self.boutC), ("D", self.boutD),
	("Quitter", self.boutQuit)]
      for b in bList:
      Button(self, text =b[0], command =b[1]).pack(side =LEFT)
      self.pack()
 
  def boutA(self):
      self.d3 = FaceDom(self.can, 3, (100,100), 50)
 
  def boutB(self):
      self.d2 = FaceDom(self.can, 2, (200,100), 80)
 
  def boutC(self):
      self.d1 = FaceDom(self.can, 1, (350,100), 110)
 
  def boutD(self):
      # ***
      self.d3.effacer()
 
  def boutQuit(self):
      self.master.destroy()
 
Projet(500, 300).mainloop()
```



B\) Modifiez ensuite ce script, afin qu'il corresponde au cahier des
charges suivant :\
 Le canevas devra être plus grand : 600 × 600 pixels.\
 Les boutons de commande devront être déplacés à droite et espacés
davantage.\
 La taille des points sur une face de dé devra varier
proportionnellement à la taille de cette face.

***Variante 1 :***

Ne conservez que les 2 boutons A et B. Chaque utilisation du bouton A
fera apparaître 3 nouveaux dés (de même taille, plutôt petits) disposés
sur une colonne (verticale), les valeurs de ces dés étant tirées au
hasard entre 1 et 6. Chaque nouvelle colonne sera disposée à la droite
de la précédente. Si l'un des tirages de 3 dés correspond à 4, 2, 1
(dans n'importe quel ordre), un message « gagné » sera affiché dans la
fenêtre (ou dans le canevas). Le bouton B provoquera l'effacement
complet (pas seulement les points !) de tous les dés affichés.

***Variante 2 :***

Ne conservez que les 2 boutons A et B. Le bouton A fera apparaître 5 dés
disposés en quinconce (c'est-à-dire comme les points d'une face de
valeur 5). Les valeurs de ces dés seront tirées au hasard entre 1 et 6,
mais il ne pourra pas y avoir de doublons. Le bouton B provoquera
l'effacement complet (pas seulement les points !) de tous les dés
affichés.

***Variante 3 :***

Ne conservez que les 3 boutons A, B et C. Le bouton A fera apparaître 13
dés de même taille disposés en cercle. Chaque utilisation du bouton B
provoquera un changement de valeur du premier dé, puis du deuxième, du
troisième, etc. La nouvelle valeur d'un dé sera à chaque fois égale a sa
valeur précédente augmentée d'une unité, sauf dans le cas ou la valeur
précédente était 6 : dans ce cas la nouvelle valeur est 1, et ainsi de
suite. Le bouton C provoquera l'effacement complet (pas seulement les
points !) de tous les dés affichés.

***Variante 4 :***

Ne conservez que les 3 boutons A, B et C. Le bouton A fera apparaître 12
dés de même taille disposés sur deux lignes de 6. Les valeurs des dés de
la première ligne seront dans l'ordre 1, 2, 3, 4, 5, 6. Les valeurs des
dés de la seconde ligne seront tirées au hasard entre 1 et 6. Chaque
utilisation du bouton B provoquera un changement de valeur aléatoire du
premier dé de la seconde ligne, tant que cette valeur restera différente
de celle du dé correspondant dans la première ligne. Lorsque le 1^er^ dé
de la 2^e^ ligne aura acquis la valeur de son correspondant, c'est la
valeur du 2^e^ dé de la seconde ligne qui sera changée au hasard, et
ainsi de suite, jusqu'à ce que les 6 faces du bas soient identiques à
celles du haut. Le bouton C provoquera l'effacement complet (pas
seulement les points !) de tous les dés affichés.


[^note_79]: Il va de soit que nous pourrions aussi rassembler toutes les classes que nous construisons dans un seul module.
