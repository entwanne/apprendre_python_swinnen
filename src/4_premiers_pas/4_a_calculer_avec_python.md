## 4-A - Calculer avec Python

Python présente la particularité de pouvoir être utilisé de plusieurs
manières différentes. Vous allez d'abord l'utiliser *en mode
interactif*, c'est-à-dire d'une manière telle que vous pourrez dialoguer
avec lui directement depuis le clavier. Cela vous permettra de découvrir
très vite un grand nombre de fonctionnalités du langage. Dans un second
temps, vous apprendrez comment créer vos premiers programmes (scripts)
et les sauvegarder sur disque.

L'interpréteur peut être lancé directement depuis la ligne de commande
(dans un « shell » *Linux*, ou bien dans une fenêtre *DOS* sous
*Windows*) : il suffit d'y taper la commande `python3` (en supposant que le logiciel
lui-même ait été correctement installé, et qu'il s'agisse d'une des
dernières versions de Python), ou `python` (si la version de Python
installée sur votre ordinateur est antérieure à la version 3.0).

Si vous utilisez une interface graphique telle que *Windows*, *Gnome*,
*WindowMaker* ou *KDE*, vous préférerez vraisemblablement travailler
dans une « fenêtre de terminal », ou encore dans un environnement de
travail spécialisé tel que *IDLE*. Voici par exemple ce qui apparaît
dans une fenêtre de terminal *Gnome* (sous *Ubuntu Linux*)[^note_5]
:



![](images/image1.png)



Avec *IDLE* sous *Windows*, votre environnement de travail ressemblera à
celui-ci :



![](images/image2.png)



Par exemple, vous pouvez tout de suite utiliser l'interpréteur comme une
simple calculatrice de bureau. Veuillez donc vous-même tester les
commandes ci-dessous (Prenez l'habitude d'utiliser votre cahier
d'exercices pour noter les résultats qui apparaissent à l'écran) :



```python
>>> 5+3
 
>>> 2 ? 9      # les espaces sont optionnels
 
>>> 7 + 3 * 4	   # la hiérarchie des opérations mathématiques
	 # est-elle respectée ?
 
>>> (7+3)*4
 
>>> 20 / 3	# attention : ceci fonctionnerait différemment sous Python 2
 
>>> 20 // 3
```



Comme vous pouvez le constater, les opérateurs arithmétiques pour
l'addition, la soustraction, la multiplication et la division sont
respectivement +, -, \* et /. Les parenthèses ont la fonction attendue.

> Sous Python 3, l'opérateur de division / effectue une division réelle.
> Si vous souhaitez obtenir une division entière (c'est-à-dire dont le
> résultat - tronqué - ne peut être qu'un entier), vous devez utiliser
> l'opérateur //. Veuillez bien noter que ceci est l'un des changements
> de syntaxe apportés à la version 3 de Python, par rapport aux versions
> précédentes. Si vous utilisez l'une de ces versions, sachez que
> l'opérateur / y effectue par défaut une division entière, si on lui
> fournit des arguments qui sont eux-mêmes des entiers, et une division
> réelle, si au moins l'un des arguments est un réel. Cet ancien
> comportement de Python a été heureusement abandonné car il pouvait
> parfois conduire à des bugs difficilement repérables.



```python
>>> 20.5 / 3
 
>>> 8,7 / 5	   # Erreur !
```



Veuillez remarquer au passage ce qui est la règle dans tous les langages
de programmation, à savoir que les conventions mathématiques de base
sont celles qui sont en vigueur dans les pays anglophones : le
séparateur décimal y est donc toujours un point, et non une virgule
comme chez nous. Notez aussi que dans le monde de l'informatique, les
nombres réels sont souvent désignés comme des nombres « à virgule
flottante » (*floating point numbers*).


[^note_5]: Sous *Windows,* vous aurez surtout le choix entre l'environnement *IDLE* développé par Guido Van Rossum, auquel nous donnons nous-même la préférence, et *PythonWin*, une interface de développement développée par Mark Hammond. D'autres environnements de travail plus sophistiqués existent aussi, tels l'excellent *Boa Constructor* par exemple (qui fonctionne de façon très similaire à *Delphi*), mais nous estimons qu'ils ne conviennent guère aux débutants. Pour tout renseignement complémentaire, veuillez consulter le site Web de Python. Sous *Linux*, nous préférons personnellement travailler dans une simple fenêtre de terminal pour lancer l'interpréteur Python ou l'exécution des scripts, et faire appel à un éditeur de texte ordinaire tel que *Gedit*, *Kate*, ou un peu plus spécialisé comme *Geany* pour l'édition de ces derniers.
