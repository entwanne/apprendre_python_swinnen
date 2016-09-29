# 14 - Classes, méthodes, héritage

*Les classes que nous avons définies dans le chapitre précédent peuvent
être considérées comme des espaces de noms particuliers, dans lesquels
nous n'avons placé jusqu'ici que des variables (les attributs
d'instance). Il nous faut à présent doter ces classes d'une
fonctionnalité.*

L'idée de base de la programmation orientée objet consiste en effet à
regrouper dans un même ensemble (l'objet), à la fois un certain nombre
de données (ce sont les *attributs d'instance*), et les algorithmes
destinés à effectuer divers traitements sur ces données (ce sont les
*méthodes*, à savoir des fonctions particulières encapsulées dans
l'objet).

***Objet = [ attributs + méthodes ]***

Cette façon d'associer dans une même « capsule » les propriétés d'un
objet et les fonctions qui permettent d'agir sur elles, correspond chez
les concepteurs de programmes à une volonté de construire des entités
informatiques dont le comportement se rapproche du comportement des
objets du monde réel qui nous entoure.

Considérons par exemple un *widget* « bouton » dans une application
graphique. Il nous paraît raisonnable de souhaiter que l'objet
informatique que nous appelons ainsi ait un comportement qui ressemble à
celui d'un bouton d'appareil quelconque dans le monde réel. Or nous
savons que la fonctionnalité d'un bouton réel (sa capacité de fermer ou
d'ouvrir un circuit électrique) est bien intégrée dans l'objet lui-même
(au même titre que d'autres propriétés, telles que sa taille, sa
couleur, etc.). De la même manière, nous souhaiterons donc que les
différentes caractéristiques de notre bouton logiciel (sa taille, son
emplacement, sa couleur, le texte qu'il supporte), mais aussi la
définition de ce qui se passe lorsque l'on effectue différentes actions
de la souris sur ce bouton, soient regroupés dans une entité bien
précise à l'intérieur du programme, de telle sorte qu'il n'y ait pas de
confusion entre ce bouton et un autre, ou *a fortiori* entre ce bouton
et d'autres entités.

