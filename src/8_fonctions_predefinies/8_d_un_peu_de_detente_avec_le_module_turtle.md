## 8-D - Un peu de détente avec le module turtle

Comme nous venons de le voir, l'une des grandes qualités de Python est
qu'il est extrêmement facile de lui ajouter de nombreuses
fonctionnalités par importation de divers *modules*.

Pour illustrer cela, et nous amuser un peu avec d'autres objets que des
nombres, nous allons explorer un module Python qui permet de réaliser
des « graphiques tortue », c'est-à-dire des dessins géométriques
correspondant à la piste laissée derrière elle par une petite « tortue »
virtuelle, dont nous contrôlons les déplacements sur l'écran de
l'ordinateur à l'aide d'instructions simples.

Activer cette tortue est un vrai jeu d'enfant. Plutôt que de vous donner
de longues explications, nous vous invitons à essayer tout de suite :



![](images/image6.png)





```python
>>> from turtle import *
>>> forward(120)
>>> left(90)
>>> color('red')
>>> forward(80)
```



L'exercice est évidemment plus riche si l'on utilise des boucles :



```python
>>> reset()
>>> a = 0
>>> while a <12:
     a = a +1
     forward(150)
     left(150)
```



Attention cependant : avant de lancer un tel script, assurez-vous
toujours qu'il ne comporte pas de boucle sans fin (voir page ), car si
c'est le cas vous risquez de ne plus pouvoir reprendre le contrôle des
opérations (en particulier sous *Windows*).

Amusez-vous à écrire des scripts qui réalisent des dessins suivant un
modèle imposé à l'avance. Les principales fonctions mises à votre
disposition dans le module *turtle* sont les suivantes :

**reset()**On efface tout et on recommence\
**goto(x, y)**Aller à l'endroit de coordonnées x, y\
**forward(distance)**Avancer d'une distance donnée\
**backward(distance)**Reculer\
**up()**Relever le crayon (pour pouvoir avancer sans dessiner)\
**down()**Abaisser le crayon (pour recommencer à dessiner)\
**color(couleur)***couleur* peut être une chaîne prédéfinie ('red',
'blue', etc.)\
**left(angle)**Tourner à gauche d'un angle donné (exprimé en degrés)\
**right(angle)**Tourner à droite\
**width(épaisseur)**Choisir l'épaisseur du tracé\
**fill(1)**Remplir un contour fermé à l'aide de la couleur sélectionnée\
**write(texte)***texte* doit être une chaîne de caractères

