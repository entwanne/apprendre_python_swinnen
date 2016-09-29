## 10-G - Modification des propriétés d'un objet - Animation

À ce stade de votre apprentissage, vous souhaitez probablement pouvoir
faire apparaître un petit dessin quelconque dans un canevas, et puis le
déplacer à volonté, par exemple à l'aide de boutons.

Veuillez donc écrire, tester, puis analyser
le script ci-dessous :



```python
from tkinter import *
 
# procédure générale de déplacement :
def avance(gd, hb):
 global x1, y1
 x1, y1 = x1 +gd, y1 +hb
 can1.coords(oval1, x1,y1, x1+30,y1+30)
 
# gestionnaires d'événements :
def depl_gauche():
 avance(-10, 0)
 
def depl_droite():
 avance(10, 0)
 
def depl_haut():
 avance(0, -10)
 
def depl_bas():
 avance(0, 10)	  
#------ Programme principal -------
 
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10        # coordonnées initiales
 
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
 
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=300,width=300)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
can1.pack(side=LEFT)
Button(fen1,text='Quitter',command=fen1.quit).pack(side=BOTTOM)
Button(fen1,text='Gauche',command=depl_gauche).pack()
Button(fen1,text='Droite',command=depl_droite).pack()
Button(fen1,text='Haut',command=depl_haut).pack()
Button(fen1,text='Bas',command=depl_bas).pack()
 
# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()
```





![](images/image27.png)



Le corps de ce programme reprend de nombreux éléments connus : nous y
créons une fenêtre **fen1**, dans laquelle nous installons un canevas
contenant lui-même un cercle coloré, plus cinq boutons de contrôle.
Veuillez remarquer au passage que nous n'instancions pas les widgets
boutons dans des variables (c'est inutile, puisque nous n'y faisons plus
référence par la suite) : nous devons donc appliquer la méthode
**pack()** directement au moment de la création de ces objets.

La vraie nouveauté de ce programme réside dans la fonction **avance()**
définie au début du script. Chaque fois qu'elle sera appelée, cette
fonction redéfinira les coordonnées de l'objet « cercle coloré » que
nous avons installé dans le canevas, ce qui provoquera l'animation de
cet objet.

Cette manière de procéder est tout à fait caractéristique de la
programmation « orientée objet » : on commence par créer des objets,
puis *on agit sur ces objets en modifiant leurs propriétés, par
l'intermédiaire de méthodes*.

En programmation impérative « à l'ancienne » (c'est-à-dire sans
utilisation d'objets), on anime des figures en les effaçant à un endroit
pour les redessiner ensuite un petit peu plus loin. En programmation «
orientée objet », par contre, ces tâches sont prises en charge
automatiquement par les classes dont les objets dérivent, et il ne faut
donc pas perdre son temps à les reprogrammer.

Exercices

.Écrivez un programme qui fait apparaître une fenêtre avec un canevas.
Dans ce canevas on verra deux cercles (de tailles et de couleurs
différentes), qui sont censés représenter deux astres. Des boutons
doivent permettre de les déplacer à volonté tous les deux dans toutes
les directions. Sous le canevas, le programme doit afficher en
permanence : a) la distance séparant les deux astres; b) la force
gravitationnelle qu'ils exercent l'un sur l'autre (penser à afficher en
haut de fenêtre les masses choisies pour chacun d'eux, ainsi que
l'échelle des distances). Dans cet exercice, vous utiliserez évidemment
la loi de la gravitation universelle de Newton (cf. exercice 6.16, page
, et un manuel de Physique générale).

.En vous inspirant du programme qui détecte les clics de souris dans un
canevas, modifiez le programme ci-dessus pour y réduire le nombre de
boutons : pour déplacer un astre, il suffira de le choisir avec un
bouton, et ensuite de cliquer sur le canevas pour que cet astre se
positionne à l'endroit où l'on a cliqué.

.Extension du programme ci-dessus. Faire apparaître un troisième astre,
et afficher en permanence la force résultante agissant sur chacun des
trois (en effet : chacun subit en permanence l'attraction
gravitationnelle exercée par les deux autres !).

.Même exercice avec des charges électriques (loi de Coulomb). Donner
cette fois une possibilité de choisir le signe des charges.

.Écrivez un petit programme qui fait apparaître une fenêtre avec deux
champs : l'un indique une température en degrés *Celsius*, et l'autre la
même température exprimée en degrés *Fahrenheit*. Chaque fois que l'on
change une quelconque des deux températures, l'autre est corrigée en
conséquence. Pour convertir les degrés *Fahrenheit* en *Celsius* et
vice-versa, on utilise la formule ![](images/formule06.png) . Revoyez
aussi le petit programme concernant la calculatrice simplifiée (page ).

.Écrivez un programme qui fait apparaître une fenêtre avec un canevas.
Dans ce canevas, placez un petit cercle censé représenter une balle.
Sous le canevas, placez un bouton. Chaque fois que l'on clique sur le
bouton, la balle doit avancer d'une petite distance vers la droite,
jusqu'à ce qu'elle atteigne l'extrémité du canevas. Si l'on continue à
cliquer, la balle doit alors revenir en arrière jusqu'à l'autre
extrémité, et ainsi de suite.

.Améliorez le programme ci-dessus pour que la balle décrive cette fois
une trajectoire circulaire ou elliptique dans le canevas (lorsque l'on
clique continuellement). Note : pour arriver au résultat escompté, vous
devrez nécessairement définir une variable qui représentera l'angle
décrit, et utiliser les fonctions *sinus* et *cosinus* pour positionner
la balle en fonction de cet angle.

.Modifiez le programme ci-dessus de telle manière que la balle, en se
déplaçant, laisse derrière elle une trace de la trajectoire décrite.

.Modifiez le programme ci-dessus de manière à tracer d'autres figures.
Consultez votre professeur pour des suggestions (courbes de
*Lissajous*).

.Écrivez un programme qui fait apparaître une fenêtre avec un canevas et
un bouton. Dans le canevas, tracez un rectangle gris foncé, lequel
représentera une route, et par-dessus, une série de rectangles jaunes
censés représenter un passage pour piétons. Ajoutez quatre cercles
colorés pour figurer les feux de circulation concernant les piétons et
les véhicules. Chaque utilisation du bouton devra provoquer le
changement de couleur des feux : ![](images/image28.png)

.Écrivez un programme qui montre un canevas
dans lequel est dessiné un circuit électrique simple (générateur +
interrupteur + résistance). La fenêtre doit être pourvue de champs
d'entrée qui permettront de paramétrer chaque
élément (c'est-à-dire choisir les valeurs des résistances et
tensions). L'interrupteur doit être fonctionnel (prévoyez un
bouton « Marche/arrêt » pour cela). Des « étiquettes » doivent afficher
en permanence les tensions et intensités résultant des choix effectués
par l'utilisateur. 

