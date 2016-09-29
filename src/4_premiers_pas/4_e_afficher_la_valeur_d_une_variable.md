## 4-E - Afficher la valeur d' une variable

À la suite de l'exercice ci-dessus, nous disposons donc des trois
variables **n**, **msg** et **pi**.\
 Pour afficher leur valeur à l'écran, il existe deux possibilités. La
première consiste à entrer au clavier le nom de la variable, puis
\<*Enter*\>. Python répond en affichant la valeur correspondante :



```python
>>> n
7
>>> msg
'Quoi de neuf ?'
>>> pi
3.14159
```



Il s'agit cependant là d'une fonctionnalité secondaire de
l'interpréteur, qui est destinée à vous faciliter la vie lorsque vous
faites de simples exercices à la ligne de commande. À l'intérieur d'un
programme, vous utiliserez toujours la fonction `print()`[^note_9]
:



```python
>>> print(msg)
Quoi de neuf ?
>>> print(n)
7
```



Remarquez la subtile différence dans les affichages obtenus avec chacune
des deux méthodes. La fonction `print()` n'affiche strictement que la
valeur de la variable, telle qu'elle a été encodée, alors que l'autre
méthode (celle qui consiste à entrer seulement le nom de la variable)
affiche aussi des apostrophes afin de vous rappeler que la variable
traitée est du type « chaîne de caractères » : nous y reviendrons.

> Dans les versions de Python antérieures à la version 3.0, le rôle de
> la **fonctionprint()** était
> assuré par une **instructionprint** particulière, faisant d'ailleurs
> l'objet d'un mot réservé (voir page ). Cette instruction s'utilisait
> sans parenthèses. Dans les exercices précédents, il fallait donc
> entrer « `print n` » ou «
> `print msg` ». Si vous essayez
> plus tard de faire fonctionner sous Python 3, des programmes écrits
> dans l'une ou l'autre version ancienne, sachez donc que vous devrez
> ajouter des parenthèses après chaque instruction **print** afin de convertir celle-ci en
> fonction (des utilitaires permettent de réaliser cela
> automatiquement). Dans ces mêmes versions anciennes, les chaînes de
> caractères étaient traitées différemment (nous en reparlerons en
> détail plus loin). Suivant la configuration de votre ordinateur, vous
> pouviez alors parfois rencontrer quelques effets bizarres avec les
> chaînes contenant des caractères accentués, tels que par exemple :

> **\>\>\> msg = "Mon prénom est Chimène"
> **\
> `>>> msg `\
> **'Mon pr\\xe9nom est
> Chim\\xe8ne'**

> Ces bizarreries appartiennent désormais au passé, mais nous verrons
> plus loin qu'un programmeur digne de ce nom doit savoir de quelle
> manière sont encodés les caractères typographiques rencontrés dans
> différentes sources de données, car les normes définissant ces
> encodages ont changé au cours des années, et il faut connaître les
> techniques qui permettent de les convertir.


[^note_9]: les *fonctions* seront définies en détail dans les chapitres 6 et 7 (voir page ).
