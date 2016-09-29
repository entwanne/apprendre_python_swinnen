## 15-B - Petit train : héritage, échange d'informations entre classes

Dans l'exercice précédent, nous n'avons exploité qu'une seule
caractéristique des classes : *l'encapsulation*. Celle-ci nous a permis
d'écrire un programme dans lequel les différentes fonctions (qui sont
donc devenues des *méthodes*) peuvent chacune accéder à un même *pool*
de variables : toutes celles qui sont définies comme étant attachées à
**self**. Toutes ces variables peuvent être considérées en quelque sorte
comme des variables globales à l'intérieur de l'objet.

Comprenez bien toutefois qu'il ne s'agit pas de véritables variables
globales. Elles restent en effet strictement confinées à l'intérieur de
l'objet, et il est déconseillé de vouloir y accéder de l'extérieur[^note_75].
D'autre part, tous les objets que vous instancierez à partir d'une même
classe posséderont chacun leur propre jeu de ces variables, qui sont
donc bel et bien *encapsulées* dans ces objets. On les appelle pour
cette raison des *attributsd'instance*.

Nous allons à présent passer à la vitesse supérieure, et réaliser une
petite application sur la base de plusieurs classes, afin d'examiner
comment différents objets peuvent *s'échanger des informations par
l'intermédiaire de leurs méthodes*. Nous allons également profiter de
cet exercice pour vous montrer comment vous pouvez définir la classe
principale de votre application graphique par dérivation d'une classe
tkinter préexistante, mettant ainsi à profit le mécanisme d'*héritage*.



![](images/image37.png)



Le projet développé ici est très simple, mais il pourrait constituer une
première étape dans la réalisation d'un logiciel de jeu : nous en
fournissons d'ailleurs des exemples plus loin (voir page ). Il s'agit
d'une fenêtre contenant un canevas et deux boutons. Lorsque l'on
actionne le premier de ces deux boutons, un petit train apparaît dans le
canevas. Lorsque l'on actionne le second bouton, quelques petits
personnages apparaissent à certaines fenêtres des wagons.

### 15-B-1 - Cahier des charges {#article.xml#Ld0e44080 .TitreSection2}

L'application comportera deux classes :

-   La classe **Application()** sera obtenue par dérivation d'une des
    classes de base de tkinter : elle mettra en place la fenêtre
    principale, son canevas et ses deux boutons.
-   Une classe **Wagon()**, indépendante, permettra d'instancier dans le
    canevas 4 objets-wagons similaires, dotés chacun d'une méthode
    **perso()**. Celle-ci sera destinée à provoquer l'apparition d'un
    petit personnage à l'une quelconque des trois fenêtres du wagon.
    L'application principale invoquera cette méthode différemment pour
    différents objets-wagons, afin de faire apparaître un choix de
    quelques personnages.

### 15-B-2 - Implémentation {#article.xml#Ld0e44099 .TitreSection2}



```python
from tkinter import *
 
def cercle(can, x, y, r):
  "dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
  can.create_oval(x-r, y-r, x+r, y+r)
 
class Application(Tk):
  def __init__(self):
      Tk.__init__(self)    # constructeur de la classe parente
      self.can =Canvas(self, width =475, height =130, bg ="white")
      self.can.pack(side =TOP, padx =5, pady =5)
      Button(self, text ="Train", command =self.dessine).pack(side =LEFT)
      Button(self, text ="Hello", command =self.coucou).pack(side =LEFT)
 
  def dessine(self):
      "instanciation de 4 wagons dans le canevas"
      self.w1 = Wagon(self.can, 10, 30)
      self.w2 = Wagon(self.can, 130, 30)
      self.w3 = Wagon(self.can, 250, 30)
      self.w4 = Wagon(self.can, 370, 30)
 
  def coucou(self):
      "apparition de personnages dans certaines fenêtres"
      self.w1.perso(3)	      # 1er wagon, 3e fenêtre
      self.w3.perso(1)	      # 3e wagon, 1e fenêtre
      self.w3.perso(2)	      # 3e wagon, 2e fenêtre
      self.w4.perso(1)	      # 4e wagon, 1e fenêtre
 
class Wagon(object):
  def __init__(self, canev, x, y):
      "dessin d'un petit wagon en <x,y> dans le canevas <canev>"
      # mémorisation des paramètres dans des variables d'instance :
      self.canev, self.x, self.y = canev, x, y
      # rectangle de base : 95x60 pixels :
      canev.create_rectangle(x, y, x+95, y+60)
      # 3 fenêtres de 25x40 pixels, écartées de 5 pixels :
      for xf in range(x+5, x+90, 30):
      canev.create_rectangle(xf, y+5, xf+25, y+40)
      # 2 roues de rayon égal à 12 pixels  :
      cercle(canev, x+18, y+73, 12)
      cercle(canev, x+77, y+73, 12)
 
  def perso(self, fen):
      "apparition d'un petit personnage à la fenêtre <fen>"
      # calcul des coordonnées du centre de chaque fenêtre :
      xf = self.x + fen*30 -12
      yf = self.y + 25
      cercle(self.canev, xf, yf, 10)	  # visage
      cercle(self.canev, xf-5, yf-3, 2)   # oeil gauche       
      cercle(self.canev, xf+5, yf-3, 2)   # oeil droit
      cercle(self.canev, xf, yf+5, 3)	   # bouche
 
app = Application()
app.mainloop()
```



### 15-B-3 - Commentaires {#article.xml#Ld0e45140 .TitreSection2}

-   Lignes 3 à 5 : Nous projetons de dessiner une série de petits
    cercles. Cette petite fonction nous facilitera le travail en nous
    permettant de définir ces cercles à partir de leur centre et leur
    rayon.
-   Lignes 7 à 13 : La classe principale de notre application est
    construite par dérivation de la classe de fenêtres **Tk()** importée
    du module **tkinter**.[^note_76]
    Comme nous l'avons expliqué au chapitre précédent, le constructeur
    d'une classe dérivée doit activer lui-même le constructeur de la
    classe parente, en lui transmettant la référence de l'instance comme
    premier argument.\
     Les lignes 10 à 13 servent à mettre en place le canevas et les
    boutons.
-   Lignes 15 à 20 : Ces lignes instancient les 4 objets-wagons,
    produits à partir de la classe correspondante. Ceci pourrait être
    programmé plus élégamment à l'aide d'une boucle et d'une liste, mais
    nous le laissons ainsi pour ne pas alourdir inutilement les
    explications qui suivent.\
     Nous voulons placer nos objets-wagons dans le canevas, à des
    emplacements bien précis : il nous faut donc transmettre quelques
    informations au constructeur de ces objets : au moins la référence
    du canevas, ainsi que les coordonnées souhaitées. Ces considérations
    nous font également entrevoir que lorsque nous définirons la classe
    **Wagon()**, un peu plus loin, nous devrons associer à sa méthode
    constructeur un nombre égal de paramètres afin de réceptionner ces
    arguments.
-   Lignes 22 à 27 : Cette méthode est invoquée lorsque l'on actionne le
    second bouton. Elle invoque elle-même la méthode **perso()** de
    certains objets-wagons, avec des arguments différents, afin de faire
    apparaître les personnages aux fenêtres indiquées. Ces quelques
    lignes de code vous montrent donc comment un objet peut communiquer
    avec un autre, en faisant appel à ses méthodes. Il s'agit-là du
    mécanisme central de la programmation par objets :

> Les objets sont des entités programmées qui s*'*échangent des messages
> et interagissent par l*'*intermédiaire de leurs méthodes.

Idéalement, la méthode **coucou()** devrait comporter quelques
instructions complémentaires, lesquelles vérifieraient d'abord si les
objets-wagons concernés existent bel et bien, avant d'autoriser
l'activation d'une de leurs méthodes. Nous n'avons pas inclus ce genre
de garde-fou afin que l'exemple reste aussi simple que possible, mais
cela entraîne la conséquence que vous ne pouvez pas actionner le second
bouton avant le premier.

-   Lignes 29-30 : La classe **Wagon()** ne dérive d'aucune autre classe
    préexistante. Étant donné qu'il s'agit d'une classe d'objets
    graphiques, nous devons cependant munir sa méthode constructeur de
    paramètres, afin de recevoir la référence du canevas auquel les
    dessins sont destinés, ainsi que les coordonnées de départ de ces
    dessins. Dans vos expérimentations éventuelles autour de cet
    exercice, vous pourriez bien évidemment ajouter encore d'autres
    paramètres : taille du dessin, orientation, couleur, vitesse, etc.
-   Lignes 31 à 51 : Ces instructions ne nécessitent guère de
    commentaires. La méthode **perso()** est dotée d'un paramètre qui
    indique celle des 3 fenêtres où il faut faire apparaître un petit
    personnage. Ici aussi nous n'avons pas prévu de garde-fou : vous
    pouvez invoquer cette méthode avec un argument égal à 4 ou 5, par
    exemple, ce qui produira des effets incorrects.
-   Lignes 53-54 : Pour cette application, contrairement à la
    précédente, nous avons préféré séparer la création de l'objet
    **app**, et son démarrage par invocation de **mainloop()**, dans
    deux instructions distinctes (en guise d'exemple). Vous pourriez
    également condenser ces deux instructions en une seule, laquelle
    serait alors : `Application().mainloop()`, et faire
    ainsi l'économie d'une variable.

Exercice

.Perfectionnez le script décrit
ci-dessus, en ajoutant un paramètre **couleur** au constructeur de la
classe **Wagon()**, lequel déterminera la couleur de la cabine du wagon.
Arrangez-vous également pour que les fenêtres soient noires au départ,
et les roues grises (pour réaliser ce dernier objectif, ajoutez aussi un
paramètre **couleur** à la fonction **cercle()**).\
 À cette même classe **Wagon()**, ajoutez encore une méthode
**allumer()**, qui servira à changer la couleur des 3 fenêtres
(initialement noires) en jaune, afin de simuler l'allumage d'un
éclairage intérieur.\
 Ajoutez un bouton à la fenêtre principale, qui puisse déclencher cet
allumage. Profitez de l'amélioration de la fonction **cercle()** pour
teinter le visage des petits personnages en rose (*pink*), leurs yeux et
leurs bouches en noir, et instanciez les objets-wagons avec des couleurs
différentes.

.Ajoutez des correctifs au programme précédent, afin que l'on puisse
utiliser n'importe quel bouton dans le désordre, sans que cela ne
déclenche une erreur ou un effet bizarre.


[^note_75]: Comme nous l'avons déjà signalé précédemment, Python vous permet d'accéder aux attributs d'instance en utilisant la qualification des noms par points. D'autres langages de programmation l'interdisent, ou bien ne l'autorisent que moyennant une déclaration particulière de ces attributs (distinction entre attributs privés et publics). Sachez en tous cas que **ce n'est pas recommandé** : le bon usage de la programmation orientée objet stipule en effet que vous ne devez pouvoir accéder aux attributs des objets que par l'intermédiaire de méthodes spécifiques (l'interface).

[^note_76]: Nous verrons plus loin que *tkinter* autorise également de construire la fenêtre principale d'une application pardérivation d'une classe de *widget* (le plus souvent, il s'agira d'un *widget***Frame()**). La fenêtre englobant ce *widget* sera automatiquement ajoutée (voir page ).
