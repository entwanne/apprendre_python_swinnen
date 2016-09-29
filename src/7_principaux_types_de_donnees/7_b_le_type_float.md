## 7-B - Le type float

Vous avez déjà rencontré précédemment cet autre type de donnée numérique
: le type « nombre réel », ou « nombre à virgule flottante », désigné en
anglais par l'expression *floatingpointnumber*, et que pour cette raison
on appellera type **float** sous Python.

Ce type autorise les calculs sur de très grands ou très petits nombres
(données scientifiques, par exemple), avec un degré de précision
constant.

Pour qu'une donnée numérique soit considérée par Python comme étant du
type **float**, il suffit qu'elle contienne dans sa formulation un
élément tel qu'un point décimal ou un exposant de 10.

Par exemple, les données :



```python
3.14	10.	.001	   1e100      3.14e-10
```



sont automatiquement interprétées par Python comme étant du type
***float***.

Essayons donc ce type de données dans un nouveau petit programme
(inspiré du précédent) :



```python
>>> a, b, c = 1., 2., 1 	 # => a et b seront du type 'float'
>>> while c <18:
...    a, b, c = b, b*a, c+1
...    print(b)
 
2.0
4.0
8.0
32.0
256.0
8192.0
2097152.0
17179869184.0
3.6028797019e+16
6.18970019643e+26
2.23007451985e+43
1.38034926936e+70
3.07828173409e+113
4.24910394253e+183
1.30799390526e+297
      Inf
      Inf
```



Comme vous l'aurez certainement bien compris, nous affichons cette fois
encore une série dont les termes augmentent extrêmement vite, chacun
d'eux étant égal au produit des deux précédents. Au huitième terme, nous
dépassons déjà largement la capacité d'un *integer*. Au neuvième terme,
Python passe automatiquement à la notation scientifique (« e+n »
signifie en fait : « fois dix à l'exposant n »). Après le quinzième
terme, nous assistons à nouveau à un dépassement de capacité (sans
message d'erreur) : les nombres vraiment trop grands sont tout
simplement notés « inf » (pour « infini »).

Le type *float* utilisé dans notre exemple permet de manipuler des
nombres (positifs ou négatifs) compris entre 10^-308^ et 10^308^ avec
une précision de 12 chiffres significatifs. Ces nombres sont encodés
d'une manière particulière sur 8 octets (64 bits) dans la mémoire de la
machine : une partie du code correspond aux 12 chiffres significatifs,
et une autre à l'ordre de grandeur (exposant de 10).

Exercices

.Écrivez un programme qui convertisse en radians un angle fourni au
départ en degrés, minutes, secondes.

.Écrivez un programme qui convertisse en degrés, minutes, secondes un
angle fourni au départ en radians.

.Écrivez un programme qui convertisse en degrés Celsius une température
exprimée au départ en degrés Fahrenheit, ou l'inverse.\
 La formule de conversion est : ![](images/formule01.png).

.Écrivez un programme qui calcule les intérêts accumulés chaque année
pendant 20 ans, par capitalisation d'une somme de 100 euros placée en
banque au taux fixe de 4,3 %

.Une légende de l'Inde ancienne raconte que
le jeu d'échecs a été inventé par un vieux sage, que son roi voulut
remercier en lui affirmant qu'il lui accorderait n'importe quel cadeau
en récompense. Le vieux sage demanda qu'on lui fournisse simplement un
peu de riz pour ses vieux jours, et plus précisément un nombre de grains
de riz suffisant pour que l'on puisse en déposer 1 seul sur la première
case du jeu qu'il venait d'inventer, deux sur la suivante, quatre sur la
troisième, et ainsi de suite jusqu'à la 64^e^case.\
Écrivez un programme Python qui affiche le
nombre de grains à déposer sur chacune des 64 cases du jeu. Calculez ce
nombre de deux manières :

-   le nombre exact de grains (nombre
    entier) ;
-   le nombre de grains en notation
    scientifique (nombre réel).

