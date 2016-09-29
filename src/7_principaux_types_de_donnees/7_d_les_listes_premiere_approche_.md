## 7-D - Les listes (première approche)

Les chaînes que nous avons abordées à la rubrique précédente
constituaient un premier exemple de *données composites*. On appelle
ainsi les structures de données qui sont utilisées pour regrouper de
manière structurée des ensembles de valeurs. Vous apprendrez
progressivement à utiliser plusieurs autres types de données composites,
parmi lesquelles les *listes*, les *tuples* et les *dictionnaires*[^note_22].
Nous n'allons cependant aborder ici que le premier de ces trois types,
et ce de façon assez sommaire. Il s'agit-là en effet d'un sujet fort
vaste, sur lequel nous devrons revenir à plusieurs reprises.

Sous Python, on peut définir une liste comme *une collection d'éléments
séparés par des virgules, l'ensemble étant enfermé dans des crochets*.
Exemple :



```python
>>> jour = ['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']
>>> print(jour)
['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']
```



Dans cet exemple, la valeur de la variable **jour** est une liste.

Comme on peut le constater dans le même exemple, les éléments
individuels qui constituent une liste peuvent être de types variés. Dans
cet exemple, en effet, les trois premiers éléments sont des chaînes de
caractères, le quatrième élément est un entier, le cinquième un réel,
etc. (nous verrons plus loin qu'un élément d'une liste peut lui-même
être une liste !). À cet égard, le concept de liste est donc assez
différent du concept de « tableau » (*array*) ou de « variable indicée »
que l'on rencontre dans d'autres langages de programmation.

Remarquons aussi que, comme les chaînes de caractères, les listes sont
des *séquences*, c'est-à-dire des *collections ordonnées d'objets*. Les
divers éléments qui constituent une liste sont en effet toujours
disposés dans le même ordre, et l'on peut donc accéder à chacun d'entre
eux individuellement si l'on connaît son *index* dans la liste. Comme
c'était déjà le cas pour les caractères dans une chaîne, il faut
cependant retenir que la numérotation de ces index commence *à partir de
zéro*, et non à partir de un.

***Exemples :***



```python
>>> jour = ['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']
>>> print(jour[2])
mercredi
>>> print(jour[4])
20.357
```



À la différence de ce qui se passe pour les chaînes, qui constituent un
type de données *non-modifiables* (nous aurons plus loin diverses
occasions de revenir là-dessus), il est possible de changer les éléments
individuels d'une liste :



```python
>>> print(jour)
['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']
>>> jour[3] = jour[3] +47
>>> print(jour)
['lundi', 'mardi', 'mercredi', 1847, 20.357, 'jeudi', 'vendredi']
```



On peut donc remplacer certains éléments d'une liste par d'autres, comme
ci-dessous :



```python
>>> jour[3] = 'Juillet'
>>> print(jour)
['lundi', 'mardi', 'mercredi', 'Juillet', 20.357, 'jeudi', 'vendredi']
```



La *fonction intégrée***len()**, que nous avons déjà rencontrée à propos
des chaînes, s'applique aussi aux listes. Elle renvoie le nombre
d'éléments présents dans la liste :



```python
>>> print(len(jour))
7
```



Une autre *fonction intégrée* permet de supprimer d'une liste un élément
quelconque (à partir de son index). Il s'agit de la fonction **del()**
[^note_23]:



```python
>>> del(jour[4])
>>> print(jour)
['lundi', 'mardi', 'mercredi', 'juillet', 'jeudi', 'vendredi']
```



Il est également tout à fait possible d'ajouter un élément à une liste,
mais pour ce faire, il faut considérer que la liste est un *objet*, dont
on va utiliser l'une des *méthodes*. Les concepts informatiques
*d'objet* et de *méthode* ne seront expliqués qu'un peu plus loin dans
ces notes, mais nous pouvons dès à présent montrer « comment ça marche »
dans le cas particulier d'une liste :



```python
>>> jour.append('samedi')
>>> print(jour)
['lundi', 'mardi', 'mercredi', 'juillet', 'jeudi', 'vendredi', 'samedi']
>>>
```



Dans la première ligne de l'exemple ci-dessus, nous avons appliqué la
*méthode***append()** à *l'objet***jour**, avec *l'argument*'samedi'. Si
l'on se rappelle que le mot « append » signifie « ajouter » en anglais,
on peut comprendre que la méthode **append()** est une sorte de
*fonction* qui est en quelque manière attachée ou intégrée aux objets du
type « liste ». L'argument que l'on utilise avec cette fonction est bien
entendu l'élément que l'on veut ajouter à la fin de la liste.

Nous verrons plus loin qu'il existe ainsi toute une série de ces
*méthodes* (c'est-à-dire des fonctions intégrées, ou plutôt «
encapsulées » dans les objets de type « liste »). Notons simplement au
passage que l'on applique une méthode à un objet *en reliant les deux à
l'aide d'un point*. (D'abord le nom de la variable qui référence
l'objet, puis le point, puis le nom de la méthode, cette dernière
toujours accompagnée d'une paire de parenthèses.)

Comme les chaînes de caractères, les listes seront approfondies plus
loin dans ces notes. Nous en savons cependant assez pour commencer à les
utiliser dans nos programmes. Veuillez par exemple analyser le petit
script ci-dessous et commenter son fonctionnement :



```python
jour = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']
a, b = 0, 0
while a<25:
  a = a + 1
  b = a % 7
  print(a, jour[b])
```



La 5^e^ ligne de cet exemple fait usage de l'opérateur « *modulo* » déjà
rencontré précédemment et qui peut rendre de grands services en
programmation. On le représente par % dans de nombreux langages (dont
Python). Quelle est l'opération effectuée par cet opérateur ?

Exercices

.Soient les listes suivantes :

**t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30,
31, 30, 31]**\
**t2 = ['Janvier',
'Février',
'Mars',
'Avril',
'Mai',
'Juin',**\
**'Juillet',
'Août',
'Septembre',
'Octobre', 'Novembre',
'Décembre']**

Écrivez un petit programme qui crée une nouvelle liste **t3**. Celle-ci
devra contenir tous les éléments des deux listes en les alternant, de
telle manière que chaque nom de mois soit suivi du nombre de jours
correspondant :

**['Janvier',31,'Février',28,'Mars',31,
etc...].**

.Écrivez un programme qui affiche « proprement » tous les éléments d'une
liste. Si on l'appliquait par exemple à la liste **t2** de l'exercice
ci-dessus, on devrait obtenir :

**Janvier Février Mars Avril Mai Juin
Juillet Août Septembre Octobre Novembre Décembre**

.Écrivez un programme qui recherche le plus grand élément présent dans
une liste donnée. Par exemple, si on l'appliquait à la liste `[32, 5, 12, 8, 3, 75, 2, 15]`, ce
programme devrait afficher :

**le plus grand élément de cette liste a la
valeur 75.**

.Écrivez un programme qui analyse un
par un tous les éléments d'une liste de nombres (par exemple celle de
l'exercice précédent) pour générer deux nouvelles listes. L'une
contiendra seulement les nombres *pairs* de la liste initiale, et
l'autre les nombres *impairs*. Par exemple, si la liste initiale est
celle de l'exercice précédent, le programme devra construire une liste
**pairs** qui contiendra **[32, 12, 8,
2]**, et une liste **impairs** qui contiendra `[5, 3, 75, 15]`. Astuce : pensez à
utiliser l'opérateur **modulo** (%) déjà cité précédemment.

.Écrivez un programme qui analyse un par un
tous les éléments d'une liste de mots (par exemple : **['Jean',
'Maximilien',
'Brigitte',
'Sonia',
'Jean-Pierre',
'Sandra']**) pour
générer deux nouvelles listes. L'une contiendra les mots comportant
moins de 6 caractères, l'autre les mots comportant 6 caractères ou
davantage.


[^note_22]: Vous pourrez même créer vos propres types de données composites, lorsque vous aurez assimilé le concept de ***classe*** (voir page ).

[^note_23]: Il existe en fait tout un ensemble de techniques qui permettent de découper une liste en tranches, d'y insérer des groupes d'éléments, d'en enlever d'autres, etc., en utilisant une syntaxe particulière où n'interviennent que les index. Cet ensemble de techniques (qui peuvent aussi s'appliquer aux chaînes de caractères) porte le nom générique de *slicing* (tranchage). On le met en œuvre en plaçant plusieurs indices au lieu d'un seul entre les crochets que l'on accole au nom de la variable. Ainsi jour[1:3] désigne le sous-ensemble ['mardi', 'mercredi']. Ces techniques un peu particulières sont décrites plus loin (voir pages et suivantes).
