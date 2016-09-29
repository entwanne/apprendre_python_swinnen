## 11-D - Les deux formes d'importation

Les lignes d'instructions que nous venons d'utiliser sont l'occasion
d'expliquer un mécanisme intéressant. Vous savez qu'en complément des
fonctions intégrées dans le module de base, Python met à votre
disposition une très grande quantité de fonctions plus spécialisées, qui
sont regroupées dans des *modules*. Ainsi vous connaissez déjà fort bien
le module *math* et le module *tkinter*.

Pour utiliser les fonctions d'un module, il suffit de les importer. Mais
cela peut se faire de deux manières différentes, comme nous allons le
voir ci-dessous. Chacune des deux méthodes présente des avantages et des
inconvénients.

Voici un exemple de la première méthode
:



```python
>>> import os
>>> rep_cour = os.getcwd()
>>> print rep_cour
C:\Python22\essais
```



La première ligne de cet exemple importe
l'*intégralité*du module
**os**, lequel contient de
nombreuses fonctions intéressantes pour l'accès au système
d'exploitation. La seconde ligne utilise la fonction
**getcwd()**du module
**os**[^note_52]. Comme vous pouvez le constater, la fonction
**getcwd()**renvoie le nom du
répertoire courant (*getcwd = get current working directory*). Par comparaison, voici un exemple similaire
utilisant la seconde méthode d'importation :



```python
>>> from os import getcwd
>>> rep_cour = getcwd() 
>>> print(rep_cour)
C:\Python31\essais
```



Dans ce nouvel exemple, nous n'avons importé du module **os** que la
fonction **getcwd()**. Importée de cette manière, la fonction s'intègre
à notre propre code comme si nous l'avions écrite nous-mêmes. Dans les
lignes où nous l'utilisons, il n'est pas nécessaire de rappeler qu'elle
fait partie du module **os**.

Nous pouvons de la même manière importer
plusieurs fonctions du même module :



```python
>>> from math import sqrt, pi, sin, cos
>>> print(pi)
3.14159265359
>>> print(sqrt(5))	# racine carrée de 5
2.2360679775
>>> print(sin(pi/6))	  # sinus d'un angle de 30°
0.5
```



Nous pouvons même importer
*toutes* les fonctions
d'un module, comme dans :



```python
from tkinter import *
```



Cette méthode d'importation présente l'avantage d'alléger l'écriture du
code. Elle présente l'inconvénient (surtout dans sa dernière forme,
celle qui importe toutes les fonctions d'un module) d'encombrer l'espace
de noms courant. Il se pourrait alors que certaines fonctions importées
aient le même nom que celui d'une variable définie par vous-même, ou
encore le même nom qu'une fonction importée depuis un autre module. Si
cela se produit, l'un des deux noms en conflit n'est évidemment plus
accessible.

Dans les programmes d'une certaine importance, qui font appel à un grand
nombre de modules d'origines diverses, il sera donc toujours préférable
de privilégier la première méthode, c'est-à-dire celle qui utilise des
noms pleinement qualifiés.

On fait généralement exception à cette règle dans le cas particulier du
module tkinter, parce que les fonctions qu'il contient sont très
sollicitées (dès lors que l'on décide d'utiliser ce module).


[^note_52]: Le point séparateur exprime donc ici une relation d'appartenance. Il s'agit d'un exemple de la ***qualification des noms*** qui sera de plus en plus largement exploitée dans la suite de ce cours. Relier ainsi des noms à l'aide de points est une manière de désigner sans ambiguïté des éléments faisant partie d'ensembles, lesquels peuvent eux-mêmes faire partie d'ensembles plus vastes, etc. Par exemple, l'étiquette **systeme.machin.truc** désigne l'élément **truc**, qui fait partie de l'ensemble **machin**, lequel fait lui-même partie de l'ensemble **systeme**. Nous verrons de nombreux exemples de cette technique de désignation, notamment lors de notre étude des **classes** d'objets.
