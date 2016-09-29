## 9-C - Vraies fonctions et procédures

Pour les puristes, les fonctions que nous avons décrites jusqu'à présent
ne sont pas tout à fait des fonctions au sens strict, mais plus
exactement des *procédures*[^note_34].
Une « vraie » fonction (au sens strict) doit en effet
*renvoyerunevaleur* lorsqu'elle se termine. Une « vraie » fonction peut
s'utiliser à la droite du signe égale dans des expressions telles que
`y = sin(a)`. On comprend aisément
que dans cette expression, la fonction **sin()** renvoie une valeur (le
sinus de l'argument **a**) qui est directement affectée à la variable
**y**.

Commençons par un exemple extrêmement simple :



```python
>>> def cube(w):
...    return w*w*w
...
```



L'instruction **return** définit ce que doit être la valeur renvoyée par
la fonction. En l'occurrence, il s'agit du cube de l'argument qui a été
transmis lors de l'appel de la fonction. Exemple :



```python
>>> b = cube(9)
>>> print(b)
729
```



À titre d'exemple un peu plus élaboré, nous allons maintenant modifier
quelque peu la fonction **table()** sur laquelle nous avons déjà pas mal
travaillé, afin qu'elle renvoie elle aussi une valeur. Cette valeur sera
en l'occurrence une liste (la liste des dix premiers termes de la table
de multiplication choisie). Voilà donc une occasion de reparler des
listes. Dans la foulée, nous en profiterons pour apprendre encore un
nouveau concept :



```python
>>> def table(base):
...    resultat = []	     # resultat est d'abord une liste vide
...    n = 1
...    while n < 11:
...	b = n * base
...	resultat.append(b)     # ajout d'un terme à la liste
...	n = n +1	 # (voir explications ci-dessous)
...    return resultat
...
```



Pour tester cette fonction, nous pouvons entrer par exemple :



```python
>>> ta9 = table(9)
```



Ainsi nous affectons à la variable **ta9** les dix premiers termes de la
table de multiplication par 9, sous la forme d'une liste :



```python
>>> print(ta9)
[9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
>>> print(ta9[0])
9
>>> print(ta9[3])
36
>>> print(ta9[2:5])
[27, 36, 45]
>>> 
```



(Rappel : le premier élément d'une liste correspond à l'indice 0).

### 9-C-1 - Notes {#article.xml#Ld0e12927 .TitreSection2}

-   Comme nous l'avons vu dans l'exemple précédent, l'instruction
    **return** définit ce que doit être la valeur « renvoyée » par la
    fonction. En l'occurrence, il s'agit ici du contenu de la variable
    **resultat**, c'est-à-dire la liste des nombres générés par la
    fonction[^note_35].
-   L'instruction **resultat.append(b)** est notre second exemple de
    l'utilisation d'un concept important sur lequel nous reviendrons
    encore abondamment par la suite : dans cette instruction, nous
    appliquons la *méthode***append()** à l'*objet***resultat**.\
    \
     Nous préciserons petit à petit ce qu'il faut entendre par *objet*
    en programmation. Pour l'instant, admettons simplement que ce terme
    très général s'applique notamment aux *listes* de Python. Une
    *méthode* n'est en fait rien d'autre qu'une fonction (que vous
    pouvez d'ailleurs reconnaître comme telle à la présence des
    parenthèses), mais *une fonction qui est associée à un objet*. Elle
    fait partie de la définition de cet objet, ou plus précisément de la
    *classe* particulière à laquelle cet objet appartient (nous
    étudierons ce concept de classe plus tard).\
    \
    *Mettre en œuvre une méthode associée à un objet* consiste en
    quelque sorte à « faire fonctionner » cet objet d'une manière
    particulière. Par exemple, on met en œuvre la méthode **methode4()**
    d'un objet **objet3**, à l'aide d'une instruction du type :
    **objet3.methode4()** , c'est-à-dire le nom de l'objet, puis le nom
    de la méthode, reliés l'un à l'autre par un point. Ce point joue un
    rôle essentiel : on peut le considérer comme un véritable
    *opérateur*.\
    \
     Dans notre exemple, nous appliquons donc la méthode **append()** à
    l'objet **resultat**, qui est une liste. Sous Python, les *listes*
    constituent donc une *classe* particulière d'objets, auxquels on
    peut effectivement appliquer toute une série de *méthodes*. En
    l'occurrence, la méthode **append()** des objets « listes » sert à
    leur ajouter un élément par la fin. L'élément à ajouter est transmis
    entre les parenthèses, comme tout argument qui se respecte.
-   ***Remarque :*** nous aurions obtenu un résultat similaire si nous
    avions utilisé à la place de cette instruction une expression telle
    que « **resultat = resultat +
    [b]** » (l'opérateur de concaténation fonctionne en effet
    aussi avec les listes). Cette façon de procéder est cependant moins
    rationnelle et beaucoup moins efficace, car elle consiste à
    redéfinir à chaque itération de la boucle une nouvelle liste
    **resultat**, dans laquelle la totalité de la liste précédente est à
    chaque fois recopiée avec ajout d'un élément supplémentaire.\
     Lorsque l'on utilise la méthode **append()**, par contre,
    l'ordinateur procède bel et bien à une modification de la liste
    existante (sans la recopier dans une nouvelle variable). Cette
    technique est donc préférable, car elle mobilise moins lourdement
    les ressources de l'ordinateur, et elle est plus rapide (surtout
    lorsqu'il s'agit de traiter des listes volumineuses).
-   Il n'est pas du tout indispensable que la valeur renvoyée par une
    fonction soit affectée à une variable (comme nous l'avons fait
    jusqu'ici dans nos exemples par souci de clarté). Ainsi, nous
    aurions pu tester les fonction **cube()** et **table()** en entrant
    les commandes :\
    `>>> print(cube(9))`\
    `>>> print(table(9))`\
    `>>> print(table(9)[3])`\
     ou encore plus simplement encore :\
    `>>> cube(9)`...


[^note_34]: Dans certains langages de programmation, les fonctions et les procédures sont définies à l'aide d'instructions différentes. Python utilise la même instruction **def** pour définir les unes et les autres.

[^note_35]: **return** peut également être utilisé sans aucun argument, à l'intérieur d'une fonction, pour provoquer sa fermeture immédiate. La valeur retournée dans ce cas est l'objet **None** (objet particulier, correspondant à « rien »).
