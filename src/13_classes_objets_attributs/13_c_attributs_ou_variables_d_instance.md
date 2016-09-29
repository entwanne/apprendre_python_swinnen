## 13-C - Attributs (ou variables) d'instance

L'objet que nous venons de créer est juste une coquille vide. Nous
allons à présent lui ajouter des composants, par simple assignation, en
utilisant le système de qualification des noms par points[^note_73]
:



```python
>>> p9.x = 3.0
>>> p9.y = 4.0
```



Les variables **x** et **y** que nous avons ainsi définies en les liant
d'emblée à **p9** , sont désormais des *attributs* de l'objet **p9.** On
peut également les appeler des *variables d'instance*. Elles sont en
effet incorporées, ou plutôt *encapsulées* dans cette instance (ou
objet). Le diagramme d'état ci-contre montre le résultat de ces
affectations : la variable **p9** contient la référence indiquant
l'emplacement mémoire du nouvel objet, qui contient lui-même les deux
attributs **x** et **y**. Ceux-ci contiennent les références des valeurs
3.0 et 4.0, mémorisées ailleurs.



![](images/image33.jpg)



On pourra utiliser les attributs d'un objet dans n'importe quelle
expression, exactement comme toutes les variables ordinaires :



```python
>>> print(p9.x)
3.0
>>> print(p9.x**2 + p9.y**2)
25.0
```



Du fait de leur *encapsulation* dans l'objet, les attributs sont des
variables distinctes d'autres variables qui pourraient porter le même
nom. Par exemple, l'instruction **x =
p9.x** signifie : « extraire de l'objet référencé par **p9** la
valeur de son attribut **x**, et assigner cette valeur à la variable
**x** ». Il n'y a pas de conflit entre la variable indépendante **x** ,
et l'attribut **x** de l'objet **p9**. L'objet **p9** contient en effet
son propre espace de noms, indépendant de l'espace de nom principal où
se trouve la variable **x**.

> **Important :** les exemples donnés ici sont provisoires.

> Nous venons de voir qu'il est très aisé d'ajouter un attribut à un
> objet en utilisant une simple instruction d'assignation telle que p9.x
> = 3.0 On peut se permettre cela sous Python (c'est une conséquence de
> son caractère foncièrement dynamique), mais cela n'est pas vraiment
> recommandable, comme vous le comprendrez plus loin. Nous n'utiliserons
> donc cette façon de faire que de manière anecdotique, et uniquement
> dans le but de simplifier nos premières explications concernant les
> attributs d'instances. La bonne manière de procéder sera développée
> dans le chapitre suivant.


[^note_73]: Ce système de notation est similaire à celui que nous utilisons pour désigner les variables d'un module, comme par exemple **math.pi** ou **string.ascii\_lowercase**. Nous aurons l'occasion d'y revenir plus tard, mais sachez dès à présent que les modules peuvent en effet contenir des fonctions, mais aussi des classes et des variables. Essayez par exemple : **\>\>\> import string** **\>\>\> string.capwords** **\>\>\> string.ascii\_uppercase** **\>\>\> string.punctuation** **\>\>\> string.hexdigits**
