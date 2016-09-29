## 10-E - Utilisation de la méthode grid() pour contrôler la disposition des widgets

Jusqu'à présent, nous avons toujours disposé les widgets dans leur
fenêtre à l'aide de la méthode **pack()**. Cette méthode présentait
l'avantage d'être extraordinairement simple, mais elle ne nous donnait
pas beaucoup de liberté pour disposer les widgets à notre guise. Comment
faire, par exemple, pour obtenir la fenêtre ci-contre ?
![](images/image23.png)

Nous pourrions effectuer un certain nombre
de tentatives en fournissant à la méthode **pack()** des arguments de type « side = », comme nous
l'avons déjà fait précédemment, mais
cela ne nous mène pas très loin. Essayons par exemple :



```python
from tkinter import *
 
fen1 = Tk()
txt1 = Label(fen1, text = 'Premier champ :')
txt2 = Label(fen1, text = 'Second :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
txt1.pack(side =LEFT)
txt2.pack(side =LEFT)
entr1.pack(side =RIGHT)
entr2.pack(side =RIGHT)
 
fen1.mainloop()
```



... mais le résultat n'est pas vraiment celui que nous recherchions
!



![](images/image24.png)





![](images/10000000000001870000002E0999B977.png)



Il est temps que nous apprenions à utiliser
une autre approche du problème. Veuillez donc analyser le script
ci-dessous : il contient en effet (presque) la solution :



```python
from tkinter import *
 
fen1 = Tk()
txt1 = Label(fen1, text = 'Premier champ :')
txt2 = Label(fen1, text = 'Second :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
txt1.grid(row =0)
txt2.grid(row =1)
entr1.grid(row =0, column =1)
entr2.grid(row =1, column =1)
fen1.mainloop()
```





![](images/image25.gif)



Dans ce script, nous avons donc remplacé la méthode **pack()** par la
méthode **grid()**. Comme vous pouvez le constater, l'utilisation de la
méthode **grid()** est très simple. Cette méthode considère la fenêtre
comme un tableau (ou une grille). Il suffit alors de lui indiquer dans
quelle ligne (**row**) et dans quelle colonne (**column**) de ce tableau
on souhaite placer les widgets. On peut numéroter les lignes et les
colonnes comme on veut, en partant de zéro, ou de un, ou encore d'un
nombre quelconque : tkinter ignorera les lignes et colonnes vides. Notez
cependant que si vous ne fournissez aucun numéro pour une ligne ou une
colonne, la valeur par défaut sera zéro.

*Tkinter* détermine automatiquement le
nombre de lignes et de colonnes nécessaire. Mais ce n'est pas tout : si vous examinez en détail la
petite fenêtre produite par le script ci-dessus, vous constaterez que
nous n'avons pas encore tout à fait
atteint le but poursuivi. Les deux chaînes apparaissant dans la partie
gauche de la fenêtre sont *centrées*, alors que nous souhaitions les
*aligner* l'une et l'autre par la droite. Pour obtenir ce résultat, il
nous suffit d'ajouter un argument
dans l'appel de la méthode
**grid()** utilisée pour ces
widgets. L'option
**sticky** peut prendre
l'une des quatre valeurs **N,
S, W, E** (les quatre points cardinaux en
anglais). En fonction de cette valeur, on obtiendra un alignement des
widgets par le haut, par le bas, par la gauche ou par la droite.
Remplacez donc les deux premières instructions **grid()** du script par :



```python
txt1.grid(row =0, sticky =E)
txt2.grid(row =1, sticky =E)
```



.,. et vous atteindrez enfin exactement le
but recherché.

***Analysons à présent la fenêtre suivante :***



![](images/image26.png)



Cette fenêtre comporte 3 colonnes : une première avec les 3 chaînes de
caractères, une seconde avec les 3 champs d'entrée, et une troisième
avec l'image. Les deux premières colonnes comportent chacune 3 lignes,
mais l'image située dans la dernière colonne *s'étale* en quelque sorte
sur les trois.

Le code correspondant est le suivant :



```python
from tkinter import *
 
fen1 = Tk()
 
# création de widgets 'Label' et 'Entry' :
txt1 = Label(fen1, text ='Premier champ :')
txt2 = Label(fen1, text ='Second :')
txt3 = Label(fen1, text ='Troisième :')
entr1 = Entry(fen1)
entr2 = Entry(fen1)
entr3 = Entry(fen1)
 
# création d'un widget 'Canvas' contenant une image bitmap :
can1 = Canvas(fen1, width =160, height =160, bg ='white')
photo = PhotoImage(file ='martin_p.gif')
item = can1.create_image(80, 80, image =photo)
 
# Mise en page à l'aide de la méthode 'grid' :
txt1.grid(row =1, sticky =E)
txt2.grid(row =2, sticky =E)
txt3.grid(row =3, sticky =E)
entr1.grid(row =1, column =2)
entr2.grid(row =2, column =2)
entr3.grid(row =3, column =2)
can1.grid(row =1, column =3, rowspan =3, padx =10, pady =5)
 
# démarrage :
fen1.mainloop()
```



Pour pouvoir faire fonctionner ce script, il vous faudra probablement
remplacer le nom du fichier image (*martin\_p.gif*) par le nom d'une
image de votre choix. Attention : la bibliothèque tkinter standard
n'accepte qu'un petit nombre de formats pour cette image. Choisissez de
préférence le format GIF[^note_48].

Nous pouvons remarquer un certain nombre de choses dans ce script :

1.  La technique utilisée pour incorporer une image :\
     tkinter ne permet pas d'insérer directement une image dans une
    fenêtre. Il faut d'abord installer un canevas, et ensuite
    positionner l'image dans celui-ci. Nous avons opté pour un canevas
    de couleur blanche, afin de pouvoir le distinguer de la fenêtre.
    Vous pouvez remplacer le paramètre **bg
    ='white'** par **bg
    ='gray'** si vous souhaitez que le canevas devienne
    invisible. Étant donné qu'il existe de nombreux types d'images, nous
    devons en outre déclarer l'objet image comme étant un bitmap GIF, à
    partir de la classe **PhotoImage()**.
2.  La ligne où nous installons l'image dans le canevas est la ligne :\
    ** item = can1.create\_image(80, 80,
    image =photo)**\
     Pour employer un vocabulaire correct, nous dirons que nous
    utilisons ici la méthode **create\_image()** associée à l'objet
    **can1** (lequel objet est lui-même une instance de la classe
    **Canvas**). Les deux premiers arguments transmis (**80**, **80**)
    indiquent les coordonnées **x** et **y**du canevas où il faut placer
    le centre de l'image. Les dimensions du canevas étant de 160x160,
    notre choix aboutira donc à un centrage de l'image au milieu du
    canevas.
3.  La numérotation des lignes et colonnes dans la méthode **grid()** :\
     On peut constater que la numérotation des lignes et des colonnes
    dans la méthode **grid()** utilisée ici commence cette fois à partir
    de 1 (et non à partir de zéro comme dans le script précédent). Comme
    nous l'avons déjà signalé plus haut, ce choix de numérotation est
    tout à fait libre.\
     On pourrait tout aussi bien numéroter : 5, 10, 15, 20... puisque
    tkinter ignore les lignes et les colonnes vides. Numéroter à partir
    de l augmente probablement la lisibilité de notre code.
4.  Les arguments utilisés avec **grid()** pour positionner le canevas
    :\
    **can1.grid(row =1, column =3, rowspan
    =3, padx =10, pady =5)**\
     Les deux premiers arguments indiquent que le canevas sera placé
    dans la première ligne de la troisième colonne. Le troisième
    (`rowspan =3`) indique qu'il
    pourra « s'étaler » sur trois lignes.\
     Les deux derniers (**padx =10, pady
    =5**) indiquent la dimension de l'espace qu'il faut réserver
    autour de ce widget (en largeur et en hauteur).
5.  Et tant que nous y sommes, profitons de cet exemple de script, que
    nous avons déjà bien décortiqué, pour apprendre à simplifier quelque
    peu notre code…


[^note_48]: D'autres formats d'image sont possibles, mais à la condition de les traiter à l'aide des modules graphiques de la bibliothèque PIL (*Python Imaging Library*), qui est une extension de Python disponible sur : *http://www.pythonware.com/products/pil/*. Cette bibliothèque permet en outre d'effectuer une multitude de traitements divers sur des images, mais l'étude de ces techniques dépasse largement le cadre que nous nous sommes fixés pour ce manuel.
