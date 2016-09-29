## 13-F - Objets composés d'objets

Supposons maintenant que nous voulions définir une classe qui servira à
représenter des *rectangles*. Pour simplifier, nous allons considérer
que ces rectangles seront toujours orientés horizontalement ou
verticalement, et jamais en oblique.

De quelles informations avons-nous besoin pour définir de tels
rectangles ?

Il existe plusieurs possibilités. Nous pourrions par exemple spécifier
la position du centre du rectangle (deux coordonnées) et préciser sa
taille (largeur et hauteur). Nous pourrions aussi spécifier les
positions du coin supérieur gauche et du coin inférieur droit. Ou encore
la position du coin supérieur gauche et la taille. Admettons ce soit
cette dernière convention qui soit retenue.

Définissons donc notre nouvelle classe :



```python
>>> class Rectangle(object):
     "définition d'une classe de rectangles"
```



... et servons nous-en tout de suite pour créer une instance :



```python
>>> boite = Rectangle()
>>> boite.largeur = 50.0
>>> boite.hauteur = 35.0
```



Nous créons ainsi un nouvel objet **Rectangle()** et lui donnons ensuite
deux attributs. Pour spécifier le coin supérieur gauche, nous allons à
présent utiliser une nouvelle instance de la classe **Point()** que nous
avons définie précédemment. Ainsi nous allons créer un objet, à
l'intérieur d'un autre objet !



```python
>>> boite.coin = Point()
>>> boite.coin.x = 12.0
>>> boite.coin.y = 27.0
```



À la première de ces trois instructions, nous créons un nouvel attribut
**coin** pour l'objet **boite**. Ensuite, pour accéder à cet objet qui
se trouve lui-même à l'intérieur d'un autre objet, nous utilisons la
*qualification des noms hiérarchisée* (à l'aide de points) que nous
avons déjà rencontrée à plusieurs reprises.

Ainsi l'expression `boite.coin.y`
signifie « Aller à l'objet référencé dans la variable **boite**. Dans
cet objet, repérer l'attribut **coin**, puis aller à l'objet référencé
dans cet attribut. Une fois cet autre objet trouvé, sélectionner son
attribut **y**. »

Vous pourrez peut-être mieux vous représenter tout cela à l'aide d'un
diagramme tel que celui-ci :



![](images/image34.jpg)



Le nom **boite** se trouve dans *l'espace de noms principal*. Il
référence un autre *espace de noms* réservé à l'objet correspondant,
dans lequel sont mémorisés les noms **largeur**, **hauteur** et
**coin**. Ceux-ci référencent à leur tour, soit *d'autres espaces de
noms* (cas du nom « **coin** »), soit *des valeurs* bien déterminées,
lesquelles sont mémorisées ailleurs.

Python réserve des espaces de noms différents pour chaque module, chaque
classe, chaque instance, chaque fonction. Vous pouvez tirer parti de
tous ces espaces de noms bien compartimentés afin de réaliser des
*programmes robustes*, c'est-à-dire des programmes dont les différents
composants ne peuvent pas facilement interférer.

