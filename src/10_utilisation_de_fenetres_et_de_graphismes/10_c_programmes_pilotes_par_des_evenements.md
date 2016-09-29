## 10-C - Programmes pilotés par des événements

Vous venez d'expérimenter votre premier programme utilisant une
interface graphique. Ce type de programme est structuré d'une manière
différente des scripts « textuels » étudiés auparavant.



Tous les programmes d'ordinateur comportent *grosso*-*modo* trois phases
principales : *unephased'initialisation*, laquelle contient les
instructions qui préparent le travail à effectuer (appel des modules
externes nécessaires, ouverture de fichiers, connexion à un serveur de
bases de données ou à l'Internet, etc.), *unephasecentrale* où l'on
trouve la véritable fonctionnalité du programme (c'est-à-dire tout ce
qu'il est censé faire : afficher des données à l'écran, effectuer des
calculs, modifier le contenu d'un fichier, imprimer, etc.), et enfin
*unephasedeterminaison* qui sert à clôturer « proprement » les
opérations (c'est-à-dire fermer les fichiers restés ouverts, couper les
connexions externes, etc.).\
 Dans un programme « en mode texte », ces trois phases sont simplement
organisées suivant un schéma *linéaire* comme dans l'illustration
ci-contre. En conséquence, ces programmes se caractérisent par une
*interactivitétrèslimitée* avec l'utilisateur. Celui-ci ne dispose
pratiquement d'aucune liberté : il lui est demandé de temps à autre
d'entrer des données au clavier, mais toujours dans un ordre
prédéterminé correspondant à la séquence d'instructions du programme.







Dans le cas d'un programme qui utilise une interface graphique, par
contre, l'organisation interne est différente. On dit d'un tel programme
qu'il est *pilotéparlesévénements*. Après sa phase d'initialisation, un
programme de ce type se met en quelque sorte « en attente », et passe la
main à un autre logiciel, lequel est plus ou moins intimement intégré au
système d'exploitation de l'ordinateur et « tourne » en permanence.

Ce *réceptionnaired'événements* scrute sans cesse tous les périphériques
(clavier, souris, horloge, modem, etc.) et réagit immédiatement
lorsqu'un événement y est détecté.\
 Un tel événement peut être une action quelconque de l'utilisateur :
déplacement de la souris, appui sur une touche, etc., mais aussi un
événement externe ou un automatisme (top d'horloge, par exemple).



![](images/image16.png)



Lorsqu'il détecte un événement, le réceptionnaire envoie un message
spécifique au programme[^note_41],
lequel doit être conçu pour réagir en conséquence.

La phase d'initialisation d'un programme utilisant une interface
graphique comporte un ensemble d'instructions qui mettent en place les
divers composants interactifs de cette interface (fenêtres, boutons,
cases à cocher, etc.). D'autres instructions définissent les messages
d'événements qui devront être pris en charge : on peut en effet décider
que le programme ne réagira qu'à certains événements en ignorant tous
les autres.

Alors que dans un programme « textuel », la phase centrale est
constituée d'une suite d'instructions qui décrivent à l'avance l'ordre
dans lequel la machine devra exécuter ses différentes tâches (même s'il
est prévu des cheminements différents en réponse à certaines conditions
rencontrées en cours de route), on ne trouve dans la phase centrale d'un
programme avec interface graphique qu'un ensemble de fonctions
indépendantes. Chacune de ces fonctions est appelée spécifiquement
lorsqu'un événement particulier est détecté par le système
d'exploitation : elle effectue alors le travail que l'on attend du
programme en réponse à cet événement, et rien d'autre[^note_42].

Il est important de bien comprendre ici que pendant tout ce temps, le
réceptionnaire continue à « tourner » et à guetter l'apparition d'autres
événements éventuels.

S'il arrive d'autres événements, il peut donc se faire qu'une deuxième
fonction (ou une 3^e^, une 4^e^...) soit activée et commence à effectuer
son travail « en parallèle » avec la première qui n'a pas encore terminé
le sien[^note_43].
Les systèmes d'exploitation et les langages modernes permettent en effet
ce parallélisme que l'on appelle aussi *multitâche*.

Au chapitre précédent, nous avons déjà remarqué que la structure du
texte d'un programme n'indique pas directement l'ordre dans lequel les
instructions seront finalement exécutées. Cette remarque s'applique
encore bien davantage dans le cas d'un programme avec interface
graphique, puisque l'ordre dans lequel les fonctions sont appelées n'est
plus inscrit nulle part dans le programme. Ce sont les événements qui
pilotent !

Tout ceci doit vous paraître un peu compliqué. Nous allons l'illustrer
dans quelques exemples.

### 10-C-1 - Exemple graphique :tracé de lignes dans un canevas {#article.xml#Ld0e15610 .TitreSection2}



Le script décrit ci-dessous crée une fenêtre comportant trois boutons et
un *canevas*. Suivant la terminologie de *tkinter*, un *canevas* est une
surface rectangulaire délimitée, dans laquelle on peut installer ensuite
divers dessins et images à l'aide de méthodes spécifiques[^note_44].\
 Lorsque l'on clique sur le bouton « Tracer une ligne », une nouvelle
ligne colorée apparaît sur le canevas, avec à chaque fois une
inclinaison différente de la précédente.\
 Si l'on actionne le bouton « Autre couleur », une nouvelle couleur est
tirée au hasard dans une série limitée. Cette couleur est celle qui
s'appliquera aux tracés suivants.







Le bouton « Quitter » sert bien évidemment à terminer l'application en
refermant la fenêtre.



```python
# Petit exercice utilisant la bibliothèque graphique tkinter
 
from tkinter import *
from random import randrange
 
# --- définition des fonctions gestionnaires d'événements : ---
def drawline():
 "Tracé d'une ligne dans le canevas can1"
 global x1, y1, x2, y2, coul
 can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
 
 # modification des coordonnées pour la ligne suivante :
 y2, y1 = y2+10, y1-10
 
def changecolor():
 "Changement aléatoire de la couleur du tracé"
 global coul
 pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
 c = randrange(8)      # => génère un nombre aléatoire de 0 à 7
 coul = pal[c]
 
#------ Programme principal -------
 
# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 10, 190, 190, 10      # coordonnées de la ligne
coul = 'dark green'	      # couleur de la ligne
 
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=200,width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
 
fen1.mainloop()        # démarrage du réceptionnaire d'événements
 
fen1.destroy()	       # destruction (fermeture) de la fenêtre
```



Conformément à ce que nous avons expliqué dans le texte des pages
précédentes, la fonctionnalité de ce programme est essentiellement
assurée par les deux fonctions **drawline()** et **changecolor()**, qui
seront activées par des événements, ceux-ci étant eux-mêmes définis dans
la phase d'initialisation.

Dans cette phase d'initialisation, on commence par importer
l'intégralité du module tkinter ainsi qu'une fonction du module *random*
qui permet de tirer des nombres au hasard. On crée ensuite les
différents widgets par instanciation à partir des classes **Tk()**,
**Canvas()** et **Button()**. Remarquons au passage que la même classe
**Button()** sert à instancier plusieurs boutons, qui sont des objets
similaires pour l'essentiel, mais néanmoins individualisés grâce aux
options de création et qui pourront fonctionner indépendamment l'un de
l'autre.

L'initialisation se termine avec l'instruction **fen1.mainloop()** qui
démarre le réceptionnaire d'événements. Les instructions qui suivent ne
seront exécutées qu'à la sortie de cette boucle, sortie elle-même
déclenchée par la méthode **fen1.quit()** (voir ci-après).

L'option **command** utilisée dans l'instruction d'instanciation des
boutons permet de désigner la fonction qui devra être appelée lorsqu'un
événement « *clic gauche de la souris sur le widget* » se produira. Il
s'agit en fait d'un raccourci pour cet événement particulier, qui vous
est proposé par *tkinter* pour votre facilité parce que cet événement
est celui que l'on associe naturellement à un widget de type bouton.
Nous verrons plus loin qu'il existe d'autres techniques plus générales
pour associer n'importe quel type d'événement à n'importe quel widget.

Les fonctions de ce script peuvent modifier les valeurs de certaines
variables qui ont été définies au niveau principal du programme. Cela
est rendu possible grâce à l'instruction **global** utilisée dans la
définition de ces fonctions. Nous nous permettrons de procéder ainsi
pendant quelque temps encore (ne serait-ce que pour vous habituer à
distinguer les comportements des variables locales et globales), mais
comme vous le comprendrez plus loin, *cette pratique n'est pas vraiment
recommandable,* surtout lorsqu'il s'agit d'écrire de grands programmes.
Nous apprendrons une meilleure technique lorsque nous aborderons l'étude
des classes.

Dans notre fonction **changecolor()**, une couleur est choisie au hasard
dans une liste. Nous utilisons pour ce faire la fonction **randrange()**
importée du module *random*. Appelée avec un argument **N**, cette
fonction renvoie un nombre entier, tiré au hasard entre **0** et
**N-1**.

La commande liée au bouton « Quitter » appelle la méthode **quit()** de
la fenêtre **fen1**. Cette méthode sert à fermer (quitter) le
réceptionnaire d'événements (**mainloop**) associé à cette fenêtre.
Lorsque cette méthode est activée, l'exécution du programme se poursuit
avec les instructions qui suivent l'appel de **mainloop**. Dans notre
exemple, cela consiste donc à effacer (**destroy**) la fenêtre.

Exercices

.Comment faut-il modifier le programme pour ne plus avoir que des lignes
de couleur *cyan, maroon* et *green* ?

.Comment modifier le programme pour que toutes les lignes tracées soient
horizontales et parallèles ?

.Agrandissez le canevas de manière à lui donner une largeur de 500
unités et une hauteur de 650. Modifiez également la taille des lignes,
afin que leurs extrémités se confondent avec les bords du canevas.

.Ajoutez une fonction **drawline2** qui tracera deux lignes rouges en
croix au centre du canevas : l'une horizontale et l'autre verticale.
Ajoutez également un bouton portant l'indication « viseur ». Un clic sur
ce bouton devra provoquer l'affichage de la croix.

.Reprenez le programme initial. Remplacez la méthode **create\_line**
par **create\_rectangle**. Que se passe-t-il ?\
 De la même façon, essayez aussi **create\_arc**, **create\_oval**, et
**create\_polygon**.\
 Pour chacune de ces méthodes, notez ce qu'indiquent les coordonnées
fournies en paramètres.\
 (Remarque : pour le polygone, il est nécessaire de modifier légèrement
le programme !)

.- Supprimez la ligne **global x1, y1, x2, y2** dans la fonction
**drawline** du programme original. Que se passe-t-il ? Pourquoi ?\
 - Si vous placez plutôt « x1, y1, x2, y2 » entre les parenthèses, dans
la ligne de définition de la fonction **drawline**, de manière à
transmettre ces variables à la fonction en tant que paramètres, le
programme fonctionne-t-il encore ? N'oubliez pas de modifier aussi la
ligne du programme qui fait appel à cette fonction !\
 - Si vous définissez **x1, y1, x2, y2 = 10, 390, 390, 10** à la place
de **global x1, y1, ...**, que se passe-t-il ? Pourquoi ? Quelle
conclusion pouvez-vous tirer de tout cela ?

.a) Créez un court programme qui dessinera les 5 anneaux olympiques dans
un rectangle de fond blanc (white). Un bouton « Quitter » doit permettre
de fermer la fenêtre.\
 b) Modifiez le programme ci-dessus en y ajoutant 5 boutons. Chacun de
ces boutons provoquera le tracé de chacun des 5 anneaux

.Dans votre cahier de notes, établissez un tableau à deux colonnes. Vous
y noterez à gauche les définitions des classes d'objets déjà rencontrées
(avec leur liste de paramètres), et à droite les méthodes associées à
ces classes (également avec leurs paramètres). Laissez de la place pour
compléter ultérieurement.

### 10-C-2 - Exemple graphique : deux dessins alternés {#article.xml#Ld0e16494 .TitreSection2}

Cet autre exemple vous montrera comment vous pouvez exploiter les
connaissances que vous avez acquises précédemment, concernant les
boucles, les listes et les fonctions, afin de réaliser de nombreux
dessins avec seulement quelques lignes de code. Il s'agit d'une petite
application qui affiche l'un ou l'autre des deux dessins reproduits
ci-dessous, en fonction du bouton choisi :

![](images/image18.png)![](images/image19.png)



```python
from tkinter import *
 
def cercle(x, y, r, coul ='black'):
  "tracé d'un cercle de centre (x,y) et de rayon r"
  can.create_oval(x-r, y-r, x+r, y+r, outline=coul)
 
def figure_1():
  "dessiner une cible"
  # Effacer d'abord tout dessin préexistant :
  can.delete(ALL)
  # tracer les deux lignes (vert. Et horiz.) :
  can.create_line(100, 0, 100, 200, fill ='blue')
  can.create_line(0, 100, 200, 100, fill ='blue')
  # tracer plusieurs cercles concentriques :
  rayon = 15
  while rayon < 100:
      cercle(100, 100, rayon)
      rayon += 15 
 
def figure_2():
  "dessiner un visage simplifié"
  # Effacer d'abord tout dessin préexistant :
  can.delete(ALL)
  # Les caractéristiques de chaque cercle sont
  # placées dans une liste de listes :
  cc =[[100, 100, 80, 'red'],	   # visage
    [70, 70, 15, 'blue'],      # yeux
    [130, 70, 15, 'blue'],	
    [70, 70, 5, 'black'],      
    [130, 70, 5, 'black'],
    [44, 115, 20, 'red'],      # joues
    [156, 115, 20, 'red'],
    [100, 95, 15, 'purple'],   # nez
    [100, 145, 30, 'purple']]  # bouche
  # on trace tous les cercles à l'aide d'une boucle :
  i =0
  while i < len(cc):	  # parcours de la liste
      el = cc[i]      # chaque élément est lui-même une liste
      cercle(el[0], el[1], el[2], el[3])
      i += 1
 
##### Programme principal : ############
 
fen = Tk()
can = Canvas(fen, width =200, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(fen, text ='dessin 1', command =figure_1)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(fen, text ='dessin 2', command =figure_2)
b2.pack(side =RIGHT, padx =3, pady =3)
fen.mainloop()
```



Commençons par analyser le programme principal, à la fin du script :

Nous y créons une fenêtre, par instanciation d'un objet de la classe
**Tk()** dans la variable **fen**.\
 Ensuite, nous installons 3 widgets dans cette fenêtre : un canevas et
deux boutons. Le canevas est instancié dans la variable **can**, et les
deux boutons dans les variables **b1** et **b2**. Comme dans le script
précédent, les widgets sont mis en place dans la fenêtre à l'aide de
leur méthode **pack()**, mais cette fois nous utilisons celle-ci avec
des options :

-   l'option **side** peut accepter les valeurs TOP, BOTTOM, LEFT ou
    RIGHT, pour « pousser » le widget du côté correspondant dans la
    fenêtre. Ces noms écrits en majuscules sont en fait ceux d'une série
    de variables importées avec le module tkinter, et que vous pouvez
    considérer comme des « pseudo-constantes ».
-   les options **padx** et **pady** permettent de réserver un petit
    espace autour du widget. Cet espace est exprimé en nombre de pixels
    : **padx** réserve un espace à gauche et à droite du widget,
    **pady** réserve un espace au-dessus et au-dessous du widget.

Les boutons commandent l'affichage des deux dessins, en invoquant les
fonctions **figure\_1()** et **figure\_2()**. Considérant que nous
aurions à tracer un certain nombre de cercles dans ces dessins, nous
avons estimé qu'il serait bien utile de définir d'abord une fonction
**cercle()** spécialisée. En effet, vous savez probablement déjà que le
canevas tkinter est doté d'une méthode **create\_oval()** qui permet de
dessiner des ellipses quelconques (et donc aussi des cercles), mais
cette méthode doit être invoquée avec quatre arguments qui seront les
coordonnées des coins supérieur gauche et inférieur droit d'un rectangle
fictif, dans lequel l'ellipse viendra alors s'inscrire. Cela n'est pas
très pratique dans le cas particulier du cercle : il nous semblera plus
naturel de commander ce tracé en fournissant les coordonnées de son
centre ainsi que son rayon. C'est ce que nous obtiendrons avec notre
fonction **cercle()**, laquelle invoque la méthode **create\_oval()** en
effectuant la conversion des coordonnées. Remarquez aussi que cette
fonction attend un argument facultatif en ce qui concerne la couleur du
cercle à tracer (noir par défaut).

L'efficacité de cette approche apparaît clairement dans la fonction
**figure\_1()**, ou nous trouvons une simple boucle de répétition pour
dessiner toute la série de cercles (de même centre et de rayon
croissant). Notez au passage l'utilisation de l'opérateur **+=** qui
permet d'incrémenter une variable (dans notre exemple, la variable **r**
voit sa valeur augmenter de 15 unités à chaque itération).

Le second dessin est un peu plus complexe, parce qu'il est composé de
cercles de tailles variées centrés sur des points différents. Nous
pouvons tout de même tracer tous ces cercles à l'aide d'une seule boucle
de répétition, si nous mettons à profit nos connaissances concernant les
listes.

En effet, ce qui différencie les cercles que nous voulons tracer tient
en quatre caractéristiques : coordonnées **x** et **y** du centre, rayon
et couleur. Pour chaque cercle, nous pouvons placer ces quatre
caractéristiques dans une petite liste, et rassembler toutes les petites
listes ainsi obtenues dans une autre liste plus grande. Nous disposerons
ainsi d'une liste de listes, qu'il suffira ensuite de parcourir à l'aide
d'une boucle pour effectuer les tracés correspondants.\

Exercices

.Inspirez-vous du script précédent pour écrire une petite application
qui fait apparaître un damier (dessin de cases noires sur fond blanc)
lorsque l'on clique sur un bouton : ![](images/image20.png)

.À l'application de l'exercice précédent, ajoutez un bouton qui fera
apparaître des pions au hasard sur le damier (chaque pression sur le
bouton fera apparaître un nouveau pion).

### 10-C-3 - Exemple graphique : calculatrice minimaliste {#article.xml#Ld0e17488 .TitreSection2}



Bien que très court, le petit script ci-dessous implémente une
calculatrice complète, avec laquelle vous pourrez même effectuer des
calculs comportant des parenthèses et des fonctions scientifiques. N'y
voyez rien d'extraordinaire. Toute cette fonctionnalité n'est qu'une
conséquence du fait que vous utilisez un interpréteur plutôt qu'un
compilateur pour exécuter vos programmes.







Comme vous le savez, le compilateur n'intervient qu'une seule fois, pour
traduire l'ensemble de votre code source en un programme exécutable. Son
rôle est donc terminé *avant même* l'exécution du programme.
L'interpréteur, quant à lui, est toujours actif *pendant* l'exécution du
programme, et donc tout à fait disponible pour traduire un nouveau code
source quelconque, comme une expression mathématique entrée au clavier
par l'utilisateur.

Les langages interprétés disposent donc toujours de fonctions permettant
d'évaluer une chaîne de caractères comme une suite d'instructions du
langage lui-même. Il devient alors possible de construire en peu de
lignes des structures de programmes très dynamiques. Dans l'exemple
ci-dessous, nous utilisons la fonction intégrée **eval()** pour analyser
l'expression mathématique entrée par l'utilisateur dans le champ prévu à
cet effet, et nous n'avons plus ensuite qu'à afficher le résultat.



```python
# Exercice utilisant la bibliothèque graphique tkinter et le module math
 
from tkinter import *
from math import *
 
# définition de l'action à effectuer si l'utilisateur actionne
# la touche "enter" alors qu'il édite le champ d'entrée :
 
def evaluer(event):
 chaine.configure(text = "Résultat = " + str(eval(entree.get())))
 
# ----- Programme principal : -----
 
fenetre = Tk()
entree = Entry(fenetre)
entree.bind("<Return>", evaluer)
chaine = Label(fenetre)
entree.pack()
chaine.pack()
 
fenetre.mainloop()
```



Au début du script, nous commençons par importer les modules **tkinter**
et **math**, ce dernier étant nécessaire afin que la dite calculatrice
puisse disposer de toutes les fonctions mathématiques et scientifiques
usuelles : sinus, cosinus, racine carrée, etc.

Ensuite nous définissons une fonction **evaluer()**, qui sera en fait la
commande exécutée par le programme lorsque l'utilisateur actionnera la
touche *Return* (ou *Enter*) après avoir entré une expression
mathématique quelconque dans le champ d'entrée décrit plus loin.

Cette fonction utilise la méthode **configure()** du widget
**chaine**[^note_45],
pour modifier son attribut **text**. L'attribut en question reçoit donc
ici une nouvelle valeur, déterminée par ce que nous avons écrit à la
droite du signe égale : il s'agit en l'occurrence d'une chaîne de
caractères construite dynamiquement, à l'aide de deux fonctions
intégrées dans Python : **eval()** et **str()**, et d'une méthode
associée à un widget *tkinter* : la méthode **get()**.

**eval()** fait appel à l'interpréteur pour évaluer une expression
Python qui lui est transmise dans une chaîne de caractères. Le résultat
de l'évaluation est fourni en retour. Exemple :



```python
chaine = "(25 + 8)/3"    # chaîne contenant une expression mathématique
res = eval(chaine)     # évaluation de l'expression contenue dans la chaîne
print(res +5)	      # => le contenu de la variable res est numérique
```



**str()** transforme une expression numérique en chaîne de caractères.
Nous devons faire appel à cette fonction parce que la précédente renvoie
une valeur numérique, que nous convertissons à nouveau en chaîne de
caractères pour pouvoir l'incorporer au message `Résultat =`.

**get()** est une méthode associée aux widgets de la classe **Entry**.
Dans notre petit programme exemple, nous utilisons un widget de ce type
pour permettre à l'utilisateur d'entrer une expression numérique
quelconque à l'aide de son clavier. La méthode **get()** permet en
quelque sorte « d'extraire » du widget **entree** la chaîne de
caractères qui lui a été fournie par l'utilisateur.

Le corps du programme principal contient la phase d'initialisation, qui
se termine par la mise en route de l'observateur d'événements
(**mainloop**). On y trouve l'instanciation d'une fenêtre **Tk()**,
contenant un widget **chaine** instancié à partir de la classe
**Label()**, et un widget **entree** instancié à partir de la classe
**Entry()**.

***Attention :*** afin que ce dernier widget puisse vraiment faire son
travail, c'est-à-dire transmettre au programme l'expression que
l'utilisateur y aura encodée, nous lui associons un événement à l'aide
de la méthode **bind()**[^note_46]
:



```python
entree.bind("<Return>",evaluer)
```



Cette instruction signifie : « *Lier l'événement \ à l'objet \<entree\>, le gestionnaire de cet événement
étant la fonction \<evaluer\>* ».

L'événement à prendre en charge est décrit dans une chaîne de caractères
spécifique (dans notre exemple, il s'agit de la chaîne `"<Return>"`. Il existe un grand nombre
de ces événements (mouvements et clics de la souris, enfoncement des
touches du clavier, positionnement et redimensionnement des fenêtres,
passage au premier plan, etc.). Vous trouverez la liste des chaînes
spécifiques de tous ces événements dans les ouvrages de référence
traitant de tkinter.

Remarquez bien qu'il n'y a pas de parenthèses après le nom de la
fonction **evaluer**. En effet : dans cette instruction, nous ne
souhaitons pas déjà invoquer la fonction elle-même (ce serait prématuré)
; ce que nous voulons, c'est établir un lien entre un type d'événement
particulier et cette fonction, de manière à ce qu'elle soit invoquée
plus tard, chaque fois que l'événement se produira. Si nous mettions des
parenthèses, l'argument qui serait transmis à la méthode **bind()**
serait la valeur de retour de cette fonction et non sa référence.

Profitons aussi de l'occasion pour observer encore une fois la syntaxe
des instructions destinées à mettre en œuvre une méthode associée à un
objet :

***objet.méthode(arguments)***

On écrit d'abord le nom de l'objet sur lequel on désire intervenir, puis
le point (qui fait office d'opérateur), puis le nom de la méthode à
mettre en œuvre ; entre les parenthèses associées à cette méthode, on
indique enfin les arguments qu'on souhaite lui transmettre.

### 10-C-4 - Exemple graphique : détection et positionnement d'un clic souris {#article.xml#Ld0e18056 .TitreSection2}

Dans la définition de la fonction « evaluer » de l'exemple précédent,
vous aurez remarqué que nous avons fourni un argument **event** (entre
les parenthèses).

Cet argument est obligatoire[^note_47].
Lorsque vous définissez une fonction gestionnaire d'événement qui est
associée à un widget quelconque à l'aide de sa méthode **bind()**, vous
devez toujours l'utiliser comme premier argument. Cet argument désigne
en effet un objet créé automatiquement par tkinter, qui permet de
transmettre au gestionnaire d'événement un certain nombre d'attributs de
l'événement :

-   le type d'événement : déplacement de la souris, enfoncement ou
    relâchement de l'un de ses boutons, appui sur une touche du clavier,
    entrée du curseur dans une zone prédéfinie, ouverture ou fermeture
    d'une fenêtre, etc.
-   une série de propriétés de l'événement : l'instant où il s'est
    produit, ses coordonnées, les caractéristiques du ou des widget(s)
    concerné(s), etc.

Nous n'allons pas entrer dans trop de détails. Si vous voulez bien
encoder et expérimenter le petit script ci-dessous, vous aurez vite
compris le principe.



```python
# Détection et positionnement d'un clic de souris dans une fenêtre :
 
from tkinter import *
 
def pointeur(event):
 chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
	     ", Y =" + str(event.y))
 
fen = Tk()
cadre = Frame(fen, width =200, height =150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()
 
fen.mainloop()
```



Le script fait apparaître une fenêtre contenant un *cadre* (**Frame**)
rectangulaire de couleur jaune pâle, dans lequel l'utilisateur est
invité à effectuer des clics de souris.

La méthode **bind()** du widget *cadre* associe l'événement \<*clic à
l'aide du premier bouton de la souris*\> au gestionnaire d'événement «
pointeur ».

Ce gestionnaire d'événement peut utiliser les attributs **x** et **y**
de l'objet **event** généré automatiquement par tkinter, pour construire
la chaîne de caractères qui affichera la position de la souris au moment
du clic.



![](images/image22.png)



Exercice

.Modifiez le script ci-dessus de manière à
faire apparaître un petit cercle rouge à l'endroit où l'utilisateur a
effectué son clic (vous devrez d'abord remplacer le widget
**Frame**par un widget
Canvas).


[^note_41]: Ces messages sont souvent notés WM (*Window messages*) dans un environnement graphique constitué de fenêtres (avec de nombreuses zones réactives : boutons, cases à cocher, menus déroulants, etc.). Dans la description des algorithmes, il arrive fréquemment aussi qu'on confonde ces messages avec les événements eux-mêmes.

[^note_42]: Au sens strict, une telle fonction qui ne devra renvoyer aucune valeur est donc plutôt une ***procédure*** (cf. page ).

[^note_43]: En particulier, la même fonction peut être appelée plusieurs fois en réponse à l'occurrence de quelques événements identiques, la même tâche étant alors effectuée en plusieurs exemplaires concurrents. Nous verrons plus loin qu'il peut en résulter des « effets de bord » gênants.

[^note_44]: Ces dessins pourront éventuellement être animés dans une phase ultérieure.

[^note_45]: La méthode **configure()** peut s'appliquer à n'importe quel widget préexistant, pour en modifier les propriétés.

[^note_46]: En anglais, le mot *bind* signifie « lier ».

[^note_47]: La présence d'un argument est obligatoire, mais le nom *event* est une simple convention. Vous pourriez utiliser un autre nom quelconque à sa place, bien que cela ne soit pas recommandé.
