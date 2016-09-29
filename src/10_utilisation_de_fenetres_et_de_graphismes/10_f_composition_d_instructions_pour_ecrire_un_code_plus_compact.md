## 10-F - Composition d'instructions pour écrire un code plus compact

Python étant un langage de programmation de haut niveau, il est souvent
possible (et souhaitable) de retravailler un script afin de le rendre
plus compact.

Vous pouvez par exemple assez fréquemment utiliser la composition
d'instructions pour appliquer la méthode de mise en page des widgets
(**grid()**, **pack()** ou **place()**) au moment même où vous créez ces
widgets. Le code correspondant devient alors un peu plus simple, et
parfois plus lisible. Vous pouvez par exemple remplacer les deux lignes
:\
\
**txt1 = Label(fen1, text ='Premier
champ :')**\
`txt1.grid(row =1, sticky =E)`

du script précédent par une seule, telle que :

**Label(fen1, text ='Premier
champ :').grid(row =1, sticky =E)**

Dans cette nouvelle écriture, vous pouvez constater que nous faisons
l'économie de la variable intermédiaire **txt1**. Nous avions utilisé
cette variable pour bien dégager les étapes successives de notre
démarche, mais elle n'est pas toujours indispensable. Le simple fait
d'invoquer la classe **Label()** provoque en effet l'instanciation d'un
objet de cette classe, même si l'on ne mémorise pas la référence de cet
objet dans une variable (tkinter la conserve de toute façon dans sa
représentation interne de la fenêtre). Si l'on procède ainsi, la
référence est perdue pour le restant du script, mais elle peut tout de
même être transmise à une méthode de mise en page telle que **grid()**
au moment même de l'instanciation, en une seule instruction composée.
Voyons cela un peu plus en détail.

Jusqu'à présent, nous avons créé des objets divers (par instanciation à
partir d'une classe quelconque), en les affectant à chaque fois à des
variables. Par exemple, lorsque nous avons écrit :

**txt1 = Label(fen1, text ='Premier
champ :')**

nous avons créé une instance de la classe **Label()**, que nous avons
assignée à la variable **txt1.**

La variable **txt1** peut alors être utilisée pour faire référence à
cette instance, partout ailleurs dans le script, mais dans les faits
nous ne l'utilisons qu'une seule fois pour lui appliquer la méthode
**grid()**, le widget dont il est question n'étant rien d'autre qu'une
simple étiquette descriptive. Or, créer ainsi une nouvelle variable pour
n'y faire référence ensuite qu'une seule fois (et directement après sa
création) n'est pas une pratique très recommandable, puisqu'elle
consiste à réserver inutilement un certain espace mémoire.

Lorsque ce genre de situation se présente, il est plus judicieux
d'utiliser la composition d'instructions. Par exemple, on préférera le
plus souvent remplacer les deux instructions :

`somme = 45 + 72`\
`print(somme)`

par une seule instruction composée, telle que :

`print(45 + 72)`

on fait ainsi l'économie d'une variable.

De la même manière, lorsque l'on met en place des widgets auxquels on ne
souhaite plus revenir par la suite, comme c'est souvent le cas pour les
widgets de la classe **Label()**, on peut en général appliquer la
méthode de mise en page (**grid()** , **pack()** ou **place()**)
directement au moment de la création du widget, en une seule instruction
composée.

Cela s'applique seulement aux widgets qui ne sont plus référencés après
qu'on les ait créés. *Tous les autres doivent impérativement être
assignés à des variables, afin que l'on puisse encore interagir avec eux
ailleurs dans le script.*

Et dans ce cas, il faut obligatoirement utiliser deux instructions
distinctes, l'une pour instancier le widget, et l'autre pour lui
appliquer ensuite la méthode de mise en page. Vous ne pouvez pas, par
exemple, construire une instruction composée telle que :

**entree =
Entry(fen1).pack()***\# faute de
programmation !!!*

En apparence, cette instruction devrait instancier un nouveau widget et
l'assigner à la variable **entree**, la mise en page s'effectuant dans
la même opération à l'aide de la méthode **pack()**.\
 Dans la réalité, cette instruction produit bel et bien un nouveau
widget de la classe **Entry()**, et la méthode **pack()** effectue bel
et bien sa mise en page dans la fenêtre, mais la valeur qui est
mémorisée dans la variable **entree** n'est pas la référence du widget !
C'est *la valeur de retour de la méthode***pack()** : vous devez vous
rappeler en effet que les méthodes, comme les fonctions, renvoient
toujours une valeur au programme qui les appelle. Et vous ne pouvez rien
faire de cette valeur de retour : il s'agit en l'occurrence d'un objet
vide (**None**).

Pour obtenir une vraie référence du widget, vous devez obligatoirement
utiliser deux instructions :



```python
entree = Entry(fen1)	   # instanciation du widget
entree.pack()	      # application de la mise en page
```



> Lorsque vous utilisez la méthode grid(),
> vous pouvez simplifier encore un peu votre code, en omettant
> l'indication de nombreux numéros de lignes et de colonnes. À partir du
> moment où c'est la la méthode grid()qui est utilisée pour positionner
> les widgets, tkinter considère en effet qu'il existe forcément des
> lignes et des colonnes[^note_49]. Si un numéro de ligne ou de colonne n'est pas
> indiqué, le widget correspondant est placé dans la première case vide
> disponible.

Le script ci-dessous intègre les
simplifications que nous venons d'expliquer
:


[^note_49]: Surtout, n'utilisez pas plusieurs méthodes de positionnement différentes dans la même fenêtre ! Les méthodes **grid()**, **pack()** et **place()** sont mutuellement exclusives.
