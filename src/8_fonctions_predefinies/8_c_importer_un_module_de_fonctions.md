## 8-C - Importer un module de fonctions

Vous avez déjà rencontré des *fonctionsintégrées* au langage lui-même,
comme la fonction **len()**, par exemple, qui permet de connaître la
longueur d'une chaîne de caractères. Il va de soi cependant qu'il n'est
pas possible d'intégrer toutes les fonctions imaginables dans le corps
standard de Python, car il en existe virtuellement une infinité : vous
apprendrez d'ailleurs très bientôt comment en créer vous-même de
nouvelles. Les fonctions intégrées au langage sont relativement peu
nombreuses : ce sont seulement celles qui sont susceptibles d'être
utilisées très fréquemment. Les autres sont regroupées dans des fichiers
séparés que l'on appelle des *modules*.

> Les modules sont des fichiers qui regroupent des ensembles de
> fonctions[^note_26].

Vous verrez plus loin combien il est commode de découper un programme
important en plusieurs fichiers de taille modeste pour en faciliter la
maintenance. Une application Python typique sera alors constituée d'un
programme principal, accompagné de un ou plusieurs modules contenant
chacun les définitions d'un certain nombre de fonctions accessoires.

Il existe un grand nombre de modules pré-programmés qui sont fournis
d'office avec Python. Vous pouvez en trouver d'autres chez divers
fournisseurs. Souvent on essaie de regrouper dans un même module des
ensembles de fonctions apparentées, que l'on appelle des
*bibliothèques*.

Le module *math*, par exemple, contient les définitions de nombreuses
fonctions mathématiques telles que *sinus*, *cosinus*, *tangente*,
*racinecarrée*, etc. Pour pouvoir utiliser ces fonctions, il vous suffit
d'incorporer la ligne suivante au début de votre script :



```python
from math import *
```



Cette ligne indique à Python qu'il lui faut inclure dans le programme
courant *toutes* les fonctions (c'est là la signification du symbole «
joker » \* ) du module *math*, lequel contient une bibliothèque de
fonctions mathématiques pré-programmées.

Dans le corps du script lui-même, vous écrirez par exemple :\
`racine = sqrt(nombre)` pour
assigner à la variable `racine` la
racine carrée de `nombre`,\
`sinusx = sin(angle)` pour
assigner à la variable `sinusx` le
sinus de `angle` (en radians !),
etc.

***Exemple :***



```python
# Démo : utilisation des fonctions du module <math>
 
from math import *
 
nombre = 121
angle = pi/6	   # soit 30°
	  # (la bibliothèque math inclut aussi la définition de pi)
print("racine carrée de", nombre, "=", sqrt(nombre))
print("sinus de", angle, "radians", "=", sin(angle))
```



L'exécution de ce script provoque l'affichage suivant :



```python
racine carrée de 121 = 11.0
sinus de 0.523598775598 radians = 0.5
```



Ce court exemple illustre déjà fort bien quelques caractéristiques
importantes des fonctions :

-   une fonction apparaît sous la forme d'*un nom quelconque associé à
    des parenthèses*\
     exemple : **sqrt()**
-   dans les parenthèses, on *transmet* à la fonction un ou plusieurs
    *arguments*\
     exemple : **sqrt(121)**
-   la fonction fournit une *valeurderetour* (on dira aussi qu'elle «
    retourne », ou mieux : qu'elle « renvoie » une valeur)\
     exemple : **11.0**

Nous allons développer tout ceci dans les pages suivantes. Veuillez
noter au passage que les fonctions mathématiques utilisées ici ne
représentent qu'un tout premier exemple. Un simple coup d'œil dans la
documentation des bibliothèques Python vous permettra de constater que
de très nombreuses fonctions sont d'ores et déjà disponibles pour
réaliser une multitude de tâches, y compris des algorithmes
mathématiques très complexes (Python est couramment utilisé dans les
universités pour la résolution de problèmes scientifiques de haut
niveau). Il est donc hors de question de fournir ici une liste
détaillée. Une telle liste est aisément accessible dans le système
d'aide de Python :

*Documentation HTML →Python documentation →Modules index →math*

Au chapitre suivant, nous apprendrons comment créer nous-mêmes de
nouvelles fonctions.

Exercices

> **Note :** dans tous ces exercices, utilisez la fonction **input()**
> pour l'entrée des données.

.Écrivez un programme qui convertisse en mètres par seconde et en km/h
une vitesse fournie par l'utilisateur en miles/heure. (*Rappel : 1 mile
= 1609 mètres*)

.Écrivez un programme qui calcule le périmètre et l'aire d'un triangle
quelconque dont l'utilisateur fournit les 3 côtés.\
*(Rappel : l'aire d'un triangle quelconque se calcule à l'aide de la
formule :*\
![](images/formule02.png)\
*dans laquelle d désigne la longueur du demi-périmètre, et a, b, c
celles des trois côtés.)*

.Écrivez un programme qui calcule la période d'un pendule simple de
longueur donnée.\
 La formule qui permet de calculer la période d'un pendule simple est
![](images/formule03.png) ,\
***l*** représentant la longueur du pendule et ***g*** la valeur de
l'accélération de la pesanteur au lieu d'expérience.

.Écrivez un programme qui permette d'encoder des valeurs dans une liste.
Ce programme devrait fonctionner en boucle, l'utilisateur étant invité à
entrer sans cesse de nouvelles valeurs, jusqu'à ce qu'il décide de
terminer en frappant \<*Enter*\> en guise d'entrée. Le programme se
terminerait alors par l'affichage de la liste. Exemple de fonctionnement
:

`Veuillez entrer une valeur : 25`\
`Veuillez entrer une valeur : 18`\
**Veuillez entrer une valeur :
6284**\
`Veuillez entrer une valeur :`\
`[25, 18, 6284]`


[^note_26]: En toute rigueur, un module peut contenir aussi des définitions de variables ainsi que des *classes*. Nous pouvons toutefois laisser ces précisions de côté, provisoirement.
