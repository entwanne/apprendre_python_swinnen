## 9-E - Modules de fonctions

Afin que vous puissiez mieux comprendre encore la distinction entre la
définition d'une fonction et son utilisation au sein d'un programme,
nous vous suggérons de placer fréquemment vos définitions de fonctions
dans un module Python, et le programme qui les utilise dans un autre.

***Exemple :***

*On souhaite réaliser la série de dessins ci-dessous, à l'aide du
**moduleturtle****:***



![](images/image7.png)



Écrivez les lignes de code suivantes, et sauvegardez-les dans un fichier
auquel vous donnerez le nom***dessins\_tortue.py** **:***



```python
from turtle import *
 
def carre(taille, couleur):
 "fonction qui dessine un carré de taille et de couleur déterminées"
 color(couleur)
 c =0
 while c <4:
     forward(taille)
     right(90)
     c = c +1
```



Vous pouvez remarquer que la définition de la fonction **carre()**
commence par une chaîne de caractères. Cette chaîne ne joue aucun rôle
fonctionnel dans le script : elle est traitée par Python *comme un
simple commentaire*, mais qui est mémorisé à part dans un système de
documentation interne automatique, lequel pourra ensuite être exploité
par certains utilitaires et éditeurs « intelligents ».

Si vous programmez dans l'environnement IDLE, par exemple, vous verrez
apparaître cette chaîne documentaire dans une « bulle d'aide », chaque
fois que vous ferez appel aux fonctions ainsi documentées.

En fait, Python place cette chaîne dans une variable spéciale dont le
nom est \_\_doc\_\_ (le mot « doc » entouré de deux paires de caractères
« souligné »), et qui est associée à l'objet fonction comme étant l'un
de ses attributs (vous en apprendrez davantage au sujet de ces attributs
lorsque nous aborderons les classes d'objets). Ainsi, vous pouvez
vous-même retrouver la chaîne de documentation d'une fonction quelconque
en affichant le contenu de cette variable. Exemple :



```python
>>> def essai():
...    "Cette fonction est bien documentée mais ne fait presque rien."
...    print("rien à signaler")
...
>>> essai()
rien à signaler
>>> print(essai.__doc__)
Cette fonction est bien documentée mais ne fait presque rien.
```



Prenez donc la peine d'incorporer une telle chaîne explicative dans
toutes vos définitions de fonctions futures : il s'agit là d'une
pratique hautement recommandable.

Le fichier que vous aurez créé ainsi est dorénavant un véritable module
de fonctions Python, au même titre que les modules turtle ou math que
vous connaissez déjà. Vous pouvez donc l'utiliser dans n'importe quel
autre script, comme celui-ci, par exemple, qui effectuera le travail
demandé :



```python
from dessins_tortue import *
 
up()		# relever le crayon
goto(-150, 50)	      # reculer en haut à gauche
 
# dessiner dix carrés rouges, alignés :
i = 0
while i < 10:
 down() 	# abaisser le crayon
 carre(25, 'red')    # tracer un carré
 up()		  # relever le crayon
 forward(30)	     # avancer + loin
 i = i +1
a = input()	   # attendre
```



> Attention -

> Vous pouvez à priori nommer vos modules de fonctions comme bon vous
> semble. Sachez cependant qu'il vous sera impossible d'importer un
> module si son nom est l'un des 33 mots réservés Python signalés à la
> page , car le nom du module importé deviendrait une variable dans
> votre script, et les mots réservés ne peuvent pas être utilisés comme
> noms de variables. Rappelons aussi qu'il vous faut éviter de donner à
> vos modules - et à tous vos scripts en général - le même nom que celui
> d'un module Python préexistant, sinon vous devez vous attendre à des
> conflits. Par exemple, si vous donnez le nom turtle.py à un exercice
> dans lequel vous avez placé une instruction d'importation du module
> turtle, c'est l'exercice lui-même que vous allez importer !



![](images/image08.png)



Exercices

.Définissez une fonction **ligneCar(n, ca)** qui renvoie une chaîne de
**n** caractères **ca**.

.Définissez une fonction **surfCercle(R)**. Cette fonction doit renvoyer
la surface (l'aire) d'un cercle dont on lui a fourni le rayon **R** en
argument. Par exemple, l'exécution de l'instruction :\
`print(surfCercle(2.5)) ` doit
donner le résultat : `19.63495...`

.Définissez une fonction **volBoite(x1,x2,x3)** qui renvoie le volume
d'une boîte parallélépipédique dont on fournit les trois dimensions
**x1, x2, x3** en arguments.\
 Par exemple, l'exécution de l'instruction :\
`print(volBoite(5.2, 7.7, 3.3)) `
doit donner le résultat : `132.132.`

.Définissez une fonction **maximum(n1,n2,n3)** qui renvoie le plus grand
de 3 nombres **n1, n2, n3** fournis en arguments. Par exemple,
l'exécution de l'instruction :\
`print(maximum(2,5,4)) ` doit
donner le résultat : `5.`

.Complétez le module de fonctions graphiques **dessins\_tortue.py**
décrit à la page .\
 Commencez par ajouter un paramètre **angle** à la fonction **carre()**,
de manière à ce que les carrés puissent être tracés dans différentes
orientations.\
 Définissez ensuite une fonction **triangle(taille, couleur, angle)**
capable de dessiner un triangle équilatéral d'une taille, d'une couleur
et d'une orientation bien déterminées.\
 Testez votre module à l'aide d'un programme qui fera appel à ces
fonctions à plusieurs reprises, avec des arguments variés pour dessiner
une série de carrés et de triangles :



![](images/image09.png)



.Ajoutez au module de l'exercice précédent une fonction **etoile5()**
spécialisée dans le dessin d'étoiles à 5 branches. Dans votre programme
principal, insérez une boucle qui dessine une rangée horizontale de de 9
petites étoiles de tailles variées :



![](images/image10.png)



.Ajoutez au module de l'exercice précédent une fonction **etoile6()**
capable de dessiner une étoile à 6 branches, elle-même constituée de
deux triangles équilatéraux imbriqués. Cette nouvelle fonction devra
faire appel à la fonction **triangle()** définie précédemment.\
 Votre programme principal dessinera également une série de ces étoiles
:
![](images/image11.png)![](images/100000000000017B0000018165DE3236.png)



![](images/1000000000000103000000ED1B2B553A.png)



.Définissez une fonction **indexMax(liste)** qui renvoie l'index de
l'élément ayant la valeur la plus élevée dans la liste transmise en
argument. Exemple d'utilisation :\
**serie = [5, 8, 2, 1, 9, 3, 6,
7]**\
`print(indexMax(serie))`\
`4`

.Définissez une fonction **nomMois(n)** qui renvoie le nom du n-ième
mois de l'année.\
 Par exemple, l'exécution de l'instruction :\
`print(nomMois(4))` doit donner le
résultat : `Avril.`

.Définissez une fonction **inverse(ch)** qui permette d'inverser les
l'ordre des caractères d'une chaîne quelconque. La chaîne inversée sera
renvoyée au programme appelant.

.Définissez une fonction **compteMots(ph)** qui renvoie le nombre de
mots contenus dans la phrase **ph**. On considère comme mots les
ensembles de caractères inclus entre des espaces.

