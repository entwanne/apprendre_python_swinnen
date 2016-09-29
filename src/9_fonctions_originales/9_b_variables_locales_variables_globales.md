## 9-B - Variables locales, variables globales

Lorsque nous définissons des variables à l'intérieur du corps d'une
fonction, ces variables ne sont accessibles qu'à la fonction elle-même.
On dit que ces variables sont des *variables locales* à la fonction.
C'est par exemple le cas des variables **base**, **debut**, **fin** et
**n** dans l'exercice précédent.

Chaque fois que la fonction **tableMulti()** est appelée, Python réserve
pour elle (dans la mémoire de l'ordinateur) un nouvel *espace de
noms*[^note_33].
Les contenus des variables **base**, **debut**, **fin** et **n** sont
stockés dans cet espace de noms qui est *inaccessible depuis l'extérieur
de la fonction*. Ainsi par exemple, si nous essayons d'afficher le
contenu de la variable **base** juste après avoir effectué l'exercice
ci-dessus, nous obtenons un message d'erreur :



```python
>>> print(base) 
Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
NameError: name 'base' is not defined 
```



La machine nous signale clairement que le symbole **base** lui est
inconnu, alors qu'il était correctement imprimé par la fonction
**tableMulti()** elle-même. L'espace de noms qui contient le symbole
**base** est strictement réservé au fonctionnement interne de
**tableMulti()**, et il est automatiquement détruit dès que la fonction
a terminé son travail.

Les variables définies à l'extérieur d'une fonction sont des *variables
globales*. Leur contenu est « visible » de l'intérieur d'une fonction,
mais la fonction *ne peut pas le modifier*. Exemple :



```python
>>> def mask():
...    p = 20
...    print(p, q)
...
>>> p, q = 15, 38
>>> mask()
20 38
>>> print(p, q)
15 38 
```



***Analysons attentivement cet exemple :***

Nous commençons par définir une fonction très simple (qui n'utilise
d'ailleurs aucun paramètre). À l'intérieur de cette fonction, une
variable **p** est définie, avec **20** comme valeur initiale. Cette
variable **p** qui est définie à l'intérieur d'une fonction sera donc
une *variable locale*.

Une fois la définition de la fonction terminée, nous revenons au niveau
principal pour y définir les deux variables **p** et **q** auxquelles
nous attribuons les contenus **15** et **38**. Ces deux variables
définies au niveau principal seront donc des *variables globales*.

Ainsi le même nom de variable **p** a été utilisé ici à deux reprises,
*pour définir deux variables différentes* : l'une est globale et l'autre
est locale. On peut constater dans la suite de l'exercice que ces deux
variables sont bel et bien des variables distinctes, indépendantes,
obéissant à une règle de priorité qui veut qu'à l'intérieur d'une
fonction (où elles pourraient entrer en compétition), ce sont les
variables définies localement qui ont la priorité.

On constate en effet que lorsque la fonction **mask()** est lancée, la
variable globale **q** y est accessible, puisqu'elle est imprimée
correctement. Pour **p**, par contre, c'est la valeur attribuée
localement qui est affichée.

On pourrait croire d'abord que la fonction **mask()** a simplement
modifié le contenu de la variable globale **p** (puisqu'elle est
accessible). Les lignes suivantes démontrent qu'il n'en est rien : en
dehors de la fonction **mask()**, la variable globale **p** conserve sa
valeur initiale.

Tout ceci peut vous paraître compliqué au premier abord. Vous
comprendrez cependant très vite combien il est utile que des variables
soient ainsi définies comme étant locales, c'est-à-dire en quelque sorte
confinées à l'intérieur d'une fonction. Cela signifie en effet que vous
pourrez toujours utiliser une infinité de fonctions sans vous préoccuper
le moins du monde des noms de variables qui y sont utilisées : ces
variables ne pourront en effet jamais interférer avec celles que vous
aurez vous-même définies par ailleurs.

Cet état de choses peut toutefois être modifié si vous le souhaitez. Il
peut se faire par exemple que vous ayez à définir une fonction qui soit
capable de modifier une variable globale. Pour atteindre ce résultat, il
vous suffira d'utiliser l'instruction **global**. Cette instruction
permet d'indiquer - à l'intérieur de la définition d'une fonction -
quelles sont les variables à traiter globalement.

Dans l'exemple ci-dessous, la variable **a** utilisée à l'intérieur de
la fonction **monter()** est non seulement accessible, mais également
modifiable, parce qu'elle est signalée explicitement comme étant une
variable qu'il faut traiter globalement. Par comparaison, essayez le
même exercice en supprimant l'instruction **global** : la variable **a**
n'est plus incrémentée à chaque appel de la fonction.



```python
>>> def monter():
...    global a
...    a = a+1
...    print(a)
...
>>> a = 15
>>> monter()
16
>>> monter()
17
>>>
```




[^note_33]: Ce concept d'*espace de noms* sera approfondi progressivement. Vous apprendrez également plus loin que les fonctions sont en fait des *objets* dont on crée à chaque fois une nouvelle *instance* lorsqu'on les appelle.
