## 13-B - Définition d'une classe élémentaire

Pour créer une nouvelle classe d'objets Python, on utilise l'instruction
**class**. Nous allons donc apprendre à utiliser cette instruction, en
commençant par définir un type d'objet très rudimentaire, lequel sera
simplement un nouveau type de donnée. Nous avons déjà utilisé différents
types de données jusqu'à présent, mais il s'agissait à chaque fois de
types intégrés dans le langage lui-même. Nous allons maintenant créer un
nouveau type composite : le type **Point**.

Ce type correspondra au concept de *point* en géométrie plane. Dans un
plan, un point est caractérisé par deux nombres (ses coordonnées suivant
x et y). En notation mathématique, on représente donc un point par ses
deux coordonnées x et y enfermées dans une paire de parenthèses. On
parlera par exemple du point (25, 17). Une manière naturelle de
représenter un point sous Python serait d'utiliser pour les coordonnées
deux valeurs de type *float.* Nous voudrions cependant combiner ces deux
valeurs dans une seule entité, ou un seul objet. Pour y arriver, nous
allons définir une *classe***Point()** :



```python
>>> class Point(object): 
...    "Définition d'un point géométrique" 
```



Les définitions de classes peuvent être situées n'importe où dans un
programme, mais on les placera en général au début (ou bien dans un
module à importer). L'exemple ci-dessus est probablement le plus simple
qui se puisse concevoir. Une seule ligne nous a suffi pour définir le
nouveau type d'objet **Point()**.

Remarquons d'emblée que :

-   L'instruction **class** est un nouvel exemple d'*instruction
    composée*. N'oubliez pas le double point obligatoire à la fin de la
    ligne, et l'indentation du bloc d'instructions qui suit. Ce bloc
    doit contenir au moins une ligne. Dans notre exemple
    ultra-simplifié, cette ligne n'est rien d'autre qu'un simple
    commentaire. Comme nous l'avons vu précédemment pour les fonctions
    (cf. page ), vous pouvez insérer une chaîne de caractères
    directement après l'instruction **class**, afin de mettre en place
    un commentaire qui sera automatiquement incorporé dans le dispositif
    de documentation interne de Python. Prenez donc l'habitude de
    toujours placer une chaîne décrivant la classe à cet endroit.
-   Les parenthèses sont destinées à contenir la référence d'une classe
    préexistante. Cela est requis pour permettre le mécanisme
    d'*héritage*. Toute classe nouvelle que nous créons peut en effet
    hériter d'une *classe parente* un ensemble de caractéristiques,
    auxquelles elle ajoutera les siennes propres. Lorsque l'on désire
    créer une classe fondamentale - c'est-à-dire ne dérivant d'aucune
    autre, comme c'est le cas ici avec notre classe **Point()** - la
    référence à indiquer doit être par convention le nom spécial
    **object**, lequel désigne l'ancêtre de toutes les classes[^note_71].
-   Une convention très répandue veut que l'on donne aux classes *des
    noms qui commencent par une majuscule*. Dans la suite de ce texte,
    nous respecterons cette convention, ainsi qu'une autre qui demande
    que dans les textes explicatifs, on associe à chaque nom de classe
    une paire de parenthèses, comme nous le faisons déjà pour les noms
    de fonctions.

Nous venons donc de définir une *classe***Point()**. Nous pouvons à
présent nous en servir pour *créer des objets de cette classe*, que l'on
appellera aussi des *instances* de cette classe. L'opération s'appelle
pour cette raison une *instanciation*. Créons par exemple un nouvel
objet **p9**[^note_72]
:



```python
>>> p9 = Point()
```



Après cette instruction, la variable **p9** contient la référence d'un
nouvel *objet***Point()**. Nous pouvons dire également que **p9** est
une nouvelle *instance* de la classe **Point()**.

> **-Attention -**

comme les fonctions, les classes auxquelles on fait appel dans une
instruction doivent toujours être accompagnées de parenthèses (même si
aucun argument n*'*est transmis). Nous verrons un peu plus loin que les
classes peuvent effectivement être appelées avec des arguments.

Voyons maintenant si nous pouvons faire quelque chose avec notre nouvel
objet **p9** :



```python
>>> print(p9) 
<__main__.Point object at 0xb76f132c> 
```



Le message renvoyé par Python indique, comme vous l'aurez certainement
bien compris tout de suite, que **p9** est une instance de la classe
**Point()**, laquelle est définie elle-même au niveau principal (*main*)
du programme. Elle est située dans un emplacement bien déterminé de la
mémoire vive, dont l'adresse apparaît ici en notation hexadécimale.



```python
>>> print(p9.__doc__) 
Définition d'un point géométrique 
```



Comme nous l'avons expliqué pour les fonctions (cf. page ), les chaînes
de documentation de divers objets Python sont associées à l'attribut
prédéfini **\_\_doc\_\_**. Il est donc toujours possible de retrouver la
documentation associée à un objet Python quelconque, en invoquant cet
attribut.


[^note_71]: Lorsque vous définissez une classe fondamentale, vous pouvez omettre les parenthèses et la référence à la classe « ancêtre » **object** : ces indications sont devenues facultatives sous Python 3. Nous continuerons cependant à les utiliser nous-mêmes dans la suite de ce texte, afin de bien marquer l'importance du concept d'héritage.

[^note_72]: Sous Python, on peut donc instancier un objet à l'aide d'une simple instruction d'affectation. D'autres langages imposent l'emploi d'une instruction spéciale, souvent appelée **new** pour bien montrer que l'on crée un nouvel objet à partir d'un moule. Exemple : **p9 = new Point().**
