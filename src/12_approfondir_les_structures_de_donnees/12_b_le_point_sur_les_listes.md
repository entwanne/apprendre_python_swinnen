## 12-B - Le point sur les listes

Nous avons déjà rencontré les listes à plusieurs reprises, depuis leur
présentation sommaire au chapitre 5. Les listes sont des collections
ordonnées d'objets. Comme les chaînes de caractères, les listes font
partie d'un type général que l'on appelle *séquences* sous Python. Comme
les caractères dans une chaîne, les objets placés dans une liste sont
rendus accessibles par l'intermédiaire d'un *index* (un nombre qui
indique l'emplacement de l'objet dans la séquence).

### 12-B-1 - Définition d'une liste - accès à ses éléments {#article.xml#Ld0e29764 .TitreSection2}

*Vous savez déjà que l'on délimite une liste à l'aide de crochets :*



```python
>>> nombres = [5, 38, 10, 25]
>>> mots = ["jambon", "fromage", "confiture", "chocolat"]
>>> stuff = [5000, "Brigitte", 3.1416, ["Albert", "René", 1947]]
```



Dans le dernier exemple ci-dessus, nous avons rassemblé un entier, une
chaîne, un réel et même une liste, pour vous rappeler que l'on peut
combiner dans une liste des données de n'importe quel type, y compris
des listes, des dictionnaires et des tuples (ceux-ci seront étudiés plus
loin).

Pour accéder aux éléments d'une liste, on utilise les mêmes méthodes
(index, découpage en tranches) que pour accéder aux caractères d'une
chaîne :



```python
>>> print(nombres[2])
10
>>> print(nombres[1:3])
[38, 10]
>>> print(nombres[2:3])
[10]
>>> print(nombres[2:])
[10, 25]
>>> print(nombres[:2])
[5, 38]
>>> print(nombres[-1])
25
>>> print(nombres[-2])
10
```



Les exemples ci-dessus devraient attirer votre attention sur le fait
qu'une *tranche* découpée dans une liste est toujours elle-même une
liste (même s'il s'agit d'une tranche qui ne contient qu'un seul
élément, comme dans notre troisième exemple), alors qu'un élément isolé
peut contenir n'importe quel type de donnée. Nous allons approfondir
cette distinction tout au long des exemples suivants.



```python
>>> nombres[0] = 17
>>> nombres
[17, 38, 10, 25]
```



### 12-B-2 - Les listes sont modifiables {#article.xml#Ld0e30064 .TitreSection2}

Contrairement aux chaînes de caractères, les listes sont des *séquences
modifiables*. Cela nous permettra de construire plus tard des listes de
grande taille, morceau par morceau, d'une manière dynamique
(c'est-à-dire à l'aide d'un algorithme quelconque). Exemples :



```python
>>> nombres[0] = 17
>>> nombres
[17, 38, 10, 25]
```



Dans l'exemple ci-dessus, on a remplacé le premier élément de la liste
**nombres**, en utilisant l'opérateur **[ ]** (opérateur d'indiçage) *à
la gauche* du signe égale.

Si l'on souhaite accéder à un élément faisant partie d'une liste,
elle-même située dans une autre liste, il suffit d'indiquer les deux
index *entre crochets successifs* :



```python
>>> stuff[3][1] = "Isabelle"
>>> stuff
[5000, 'Brigitte', 3.1415999999999999, ['Albert', 'Isabelle', 1947]]
```



Comme c'est le cas pour toutes les séquences, il ne faut jamais oublier
que la numérotation des éléments commence à partir de zéro. Ainsi, dans
l'exemple ci-dessus on remplace l'élément n^o^ 1 d'une liste, qui est
elle-même l'élément n^o^ 3 d'une autre liste : la liste **stuff**.

### 12-B-3 - Les listes sont des objets {#article.xml#Ld0e30199 .TitreSection2}

Sous Python, les listes sont des objets à part entière, et vous pouvez
donc leur appliquer un certain nombre de *méthodes* particulièrement
efficaces. En voici quelques-unes :



```python
>>> nombres = [17, 38, 10, 25, 72]
>>> nombres.sort()	       # trier la liste
>>> nombres
[10, 17, 25, 38, 72]
 
>>> nombres.append(12)		   # ajouter un élément à la fin
>>> nombres
[10, 17, 25, 38, 72, 12]
 
>>> nombres.reverse()		  # inverser l'ordre des éléments
>>> nombres
[12, 72, 38, 25, 17, 10]
 
>>> nombres.index(17)		  # retrouver l'index d'un élément
4
 
>>> nombres.remove(38)		   # enlever (effacer) un élément
>>> nombres
[12, 72, 25, 17, 10]
```



En plus de ces méthodes, vous disposez encore de l'instruction intégrée
**del**, qui vous permet d'effacer un ou plusieurs éléments à partir de
leur(s) index :



```python
>>> del nombres[2]
>>> nombres
[12, 72, 17, 10]
>>> del nombres[1:3]
>>> nombres
[12, 10]
```



Notez bien la différence entre la méthode **remove()** et l'instruction
**del** : **del** travaille avec *unindex* ou *unetranched'index*,
tandis que **remove()** recherche *unevaleur* (si plusieurs éléments de
la liste possèdent la même valeur, seul le premier est effacé).

Exercices

.Écrivez un script qui génère la liste des carrés et des cubes des
nombres de 20 à 40.

.Écrivez un script qui crée automatiquement la liste des *sinus* des
angles de 0° à 90°, par pas de 5°. Attention : la fonction **sin()** du
module **math** considère que les angles sont fournis en *radians* (360°
= 2 π radians).

.Écrivez un script qui permette d'obtenir à l'écran les 15 premiers
termes des tables de multiplication par 2, 3, 5, 7, 11, 13, 17, 19 (ces
nombres seront placés au départ dans une liste) sous la forme d'une
table similaire à la suivante :\
**2 4
6 8 10
12 14 16
18 20 22
24 26 28
30**\
**3 6
9 12 15
18 21 24
27 30 33
36 39 42
45**\
**5 10
15 20 25
30 35 40
45 50 55
60 65 70
75**\
 etc.

.Soit la liste suivante : **['Jean-Michel',
'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît',
'Louise']**\
 Écrivez un script qui affiche chacun de ces noms avec le nombre de
caractères correspondant.

.Vous disposez d'une liste de nombres entiers quelconques, certains
d'entre eux étant présents en plusieurs exemplaires. Écrivez un script
qui recopie cette liste dans une autre, *en omettant les doublons*. La
liste finale devra être *triée*.

.Écrivez un script qui recherche le mot le plus long dans une phrase
donnée (l'utilisateur du programme doit pouvoir entrer une phrase de son
choix).

.Écrivez un script capable d'afficher la liste de tous les jours d'une
année imaginaire, laquelle commencerait un jeudi. Votre script utilisera
lui-même trois listes : une liste des noms de jours de la semaine, une
liste des noms des mois, et une liste des nombres de jours que
comportent chacun des mois (ne pas tenir compte des années
bissextiles).\
 Exemple de sortie :\
**jeudi 1 janvier vendredi 2 janvier samedi 3 janvier dimanche 4 janvier**\
 ... et ainsi de suite, jusqu'au jeudi 31 décembre.

.Vous avez à votre disposition un fichier texte qui contient un certain
nombre de noms d'élèves. Écrivez un script qui effectue une copie
*triée* de ce fichier.

.Écrivez une fonction permettant de trier une liste. Cette fonction ne
pourra pas utiliser la méthode intégrée **sort()** de Python : vous
devez donc *définir vous-même l'algorithme de tri*.

### 12-B-4 - Techniques de slicing avancé pour modifier une liste {#article.xml#Ld0e30751 .TitreSection2}

Comme nous venons de le signaler, vous pouvez ajouter ou supprimer des
éléments dans une liste en utilisant une instruction (**del**) et une
méthode (**append()**) intégrées. Si vous avez bien assimilé le principe
du « découpage en tranches » (*slicing*), vous pouvez cependant obtenir
les mêmes résultats à l'aide du seul opérateur **[ ]**. L'utilisation de
cet opérateur est un peu plus délicate que celle d'instructions ou de
méthodes dédiées, mais elle permet davantage de souplesse :

#### 12-B-4-A - Insertion d'un ou plusieurs éléments n'importe où dans une liste {#article.xml#Ld0e30768 .TitreSection3}



```python
>>> mots = ['jambon', 'fromage', 'confiture', 'chocolat']
>>> mots[2:2] =["miel"]
>>> mots
['jambon', 'fromage', 'miel', 'confiture', 'chocolat']
 
>>> mots[5:5] =['saucisson', 'ketchup']
>>> mots
['jambon', 'fromage', 'miel', 'confiture', 'chocolat', 'saucisson', 'ketchup']
```



Pour utiliser cette technique, vous devez prendre en compte les
particularités suivantes :

-   Si vous utilisez l'opérateur **[ ]***à la gauche du signe égale*
    pour effectuer une insertion ou une suppression d'élément(s) dans
    une liste, vous devez obligatoirement y indiquer une « tranche »
    dans la liste cible (c'est-à-dire deux index réunis par le symbole
    **:** ), et non un élément isolé dans cette liste.
-   L'élément que vous fournissez à la droite du signe égale *doit
    lui-même être une liste*. Si vous n'insérez qu'un seul élément, il
    vous faut donc le présenter entre crochets pour le transformer
    d'abord en une liste d'un seul élément. Notez bien que l'élément
    **mots[1]** n'est pas une liste (c'est la chaîne 'fromage' ), alors
    que l'élément **mots[1:3]** en est une.

Vous comprendrez mieux ces contraintes en analysant ce qui suit :

#### 12-B-4-B - Suppression/remplacement d'éléments {#article.xml#Ld0e30987 .TitreSection3}



```python
>>> mots[2:5] = []		   # [] désigne une liste vide
>>> mots
['jambon','fromage','saucisson', 'ketchup']
 
>>> mots[1:3] = ['salade']
>>> mots
['jambon', 'salade', 'ketchup']
 
>>> mots[1:] = ['mayonnaise', 'poulet', 'tomate']
>>> mots
['jambon', 'mayonnaise', 'poulet', 'tomate'] 
```



-   À la première ligne de cet exemple, nous remplaçons la tranche [2:5]
    par une liste vide, ce qui correspond à un effacement.
-   À la quatrième ligne, nous remplaçons une tranche par un seul
    élément. Notez encore une fois que cet élément doit lui-même être «
    présenté » comme une liste.
-   À la 7^e^ ligne, nous remplaçons une tranche de deux éléments par
    une autre qui en comporte 3.

### 12-B-5 - Création d'une liste de nombres à l'aide de la fonction range() {#article.xml#Ld0e31195 .TitreSection2}

Si vous devez manipuler des séquences de nombres, vous pouvez les créer
très aisément à l'aide de cette fonction intégrée. Elle renvoie une
séquence d'entiers[^note_66]
que vous pouvez utiliser directement, ou convertir en une *liste* avec
la fonction **list()**, ou convertir en *tuple* avec la fonction
**tuple()** (les tuples seront décrits un peu plus loin) :



```python
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```



La fonction **range()** génère par défaut une séquence de nombres
entiers de valeurs croissantes, et différant d'une unité. Si vous
appelez **range()** avec un seul argument, la liste contiendra un nombre
de valeurs égal à l'argument fourni, mais en commençant *à partir de
zéro* (c'est-à-dire que **range(n)** génère les nombres de 0 à n-1).\
 Notez bien que l'argument fourni n'est jamais dans la liste générée.

On peut aussi utiliser **range()** avec deux, ou même trois arguments
séparés par des virgules, afin de générer des séquences de nombres plus
spécifiques :



```python
>>> list(range(5,13))
[5, 6, 7, 8, 9, 10, 11, 12]
>>> list(range(3,16,3))
[3, 6, 9, 12, 15]
```



Si vous avez du mal à assimiler l'exemple ci-dessus, considérez que
**range()** attend toujours de un à trois arguments, que l'on pourrait
intituler *FROM, TO et STEP*. *FROM* est la première valeur à générer,
*TO* est la dernière (ou plutôt la dernière + un), et *STEP* le « pas »
à sauter pour passer d'une valeur à la suivante. S'ils ne sont pas
fournis, les paramètres *FROM* et *STEP* prennent leurs valeurs par
défaut, qui sont respectivement 0 et 1.

Les arguments négatifs sont autorisés :



```python
>>> list(range(10, -10, -3)) 
[10, 7, 4, 1, -2, -5, -8] 
```



### 12-B-6 - Parcours d'une liste à l'aide de for, range() et len() {#article.xml#Ld0e31457 .TitreSection2}

L'instruction **for** est l'instruction idéale pour parcourir une liste
:



```python
>>> prov = ['La','raison','du','plus','fort','est','toujours','la','meilleure']
>>> for mot in prov:
...    print(mot, end =' ')
...
La raison du plus fort est toujours la meilleure
```



Si vous voulez parcourir une gamme d'entiers, la fonction **range()**
s'impose :



```python
>>> for n in range(10, 18, 3):
...    print(n, n**2, n**3)
... 
10 100 1000 
13 169 2197 
16 256 4096 
```



Il est très pratique de combiner les fonctions **range()** et **len()**
pour obtenir automatiquement tous les indices d'une séquence (liste ou
chaîne). Exemple :



```python
fable = ['Maître','Corbeau','sur','un','arbre','perché']
for index in range(len(fable)):
 print(index, fable[index])
```



L'exécution de ce script donne le résultat :



```python
0 Maître
1 Corbeau
2 sur
3 un
4 arbre
5 perché
```



### 12-B-7 - Une conséquence importante du typage dynamique {#article.xml#Ld0e31740 .TitreSection2}

Comme nous l'avons déjà signalé plus haut (page ), le type de la
variable utilisée avec l'instruction **for***estredéfinicontinuellement*
au fur et à mesure du parcours : même si les éléments d'une liste sont
de types différents, on peut parcourir cette liste à l'aide de **for**
sans qu'il ne s'ensuive une erreur, car le type de la variable de
parcours s'adapte automatiquement à celui de l'élément en cours de
lecture. Exemple :



```python
>>> divers = [3, 17.25, [5, 'Jean'], 'Linux is not Windoze']
>>> for item in divers:
...    print(item, type(item))
...
3 <class 'int'>
17.25 <class 'float'>
[5, 'Jean'] <class 'list'>
Linux is not Windoze <class 'str'>
```



Dans l'exemple ci-dessus, on utilise la fonction intégrée **type()**
pour montrer que la variable **item***change effectivement de type* à
chaque itération (ceci est rendu possible grâce au typage dynamique des
variables Python).

### 12-B-8 - Opérations sur les listes {#article.xml#Ld0e31915 .TitreSection2}

On peut appliquer aux listes les opérateurs **+** (concaténation) et
**\*** (multiplication) :



```python
>>> fruits = ['orange','citron']
>>> legumes = ['poireau','oignon','tomate']
>>> fruits + legumes
['orange', 'citron', 'poireau', 'oignon', 'tomate']
>>> fruits * 3
['orange', 'citron', 'orange', 'citron', 'orange', 'citron']
```



L'opérateur **\*** est particulièrement utile pour créer une liste de n
éléments identiques :



```python
>>> sept_zeros = [0]*7
>>> sept_zeros
[0, 0, 0, 0, 0, 0, 0]
```



Supposons par exemple que vous voulez créer une liste **B** qui
contienne le même nombre d'éléments qu'une autre liste **A**. Vous
pouvez obtenir ce résultat de différentes manières, mais l'une des plus
simples consistera à effectuer : **B =
[0]\*len(A).**

### 12-B-9 - Test d'appartenance {#article.xml#Ld0e32145 .TitreSection2}

Vous pouvez aisément déterminer si un élément fait partie d'une liste à
l'aide de l'instruction **in** (cette instruction puissante peut être
utilisée avec toutes les séquences) :



```python
>>> v = 'tomate'
>>> if v in legumes:
...    print('OK')
...
OK
```



### 12-B-10 - Copie d'une liste {#article.xml#Ld0e32195 .TitreSection2}

Considérons que vous disposez d'une liste **fable** que vous souhaitez
recopier dans une nouvelle variable que vous appellerez **phrase**. La
première idée qui vous viendra à l'esprit sera certainement d'écrire une
simple affectation telle que :



```python
>>> phrase = fable
```



En procédant ainsi, sachez que *vous ne créez pas une véritable copie*.
À la suite de cette instruction, il n'existe toujours qu'une seule liste
dans la mémoire de l'ordinateur. Ce que vous avez créé est seulement
*une nouvelle référence* vers cette liste. Essayez par exemple :



```python
>>> fable = ['Je','plie','mais','ne','romps','point']
>>> phrase = fable
>>> fable[4] ='casse'
>>> phrase
['Je', 'plie', 'mais', 'ne', 'casse', 'point']
```



Si la variable **phrase** contenait une véritable copie de la liste,
cette copie serait indépendante de l'original et ne devrait donc pas
pouvoir être modifiée par une instruction telle que celle de la
troisième ligne, qui s'applique à la variable **fable.** Vous pouvez
encore expérimenter d'autres modifications, soit au contenu de
**fable**, soit au contenu de **phrase.** Dans tous les cas, vous
constaterez que les modifications de l'une sont répercutées dans
l'autre, et vice-versa.



![](images/image31.jpg)



Nous verrons plus tard l'utilité des alias. Pour l'instant, nous
voudrions disposer d'une technique pour effectuer une véritable copie
d'une liste. Avec les notions vues précédemment, vous devriez pouvoir en
trouver une par vous-même.

#### 12-B-10-A - Petite remarque concernant la syntaxe {#article.xml#Ld0e32373 .TitreSection3}

Python vous autorise à « étendre » une longue instruction sur plusieurs
lignes, si vous continuez à encoder quelque chose qui est délimité par
une paire de parenthèses, de crochets ou d'accolades. Vous pouvez
traiter ainsi des expressions parenthésées, ou encore la définition de
longues listes, de grands tuples ou de grands dictionnaires (voir plus
loin). Le niveau d'indentation n'a pas d'importance : l'interpréteur
détecte la fin de l'instruction là où la paire syntaxique est refermée.

Cette fonctionnalité vous permet d'améliorer la lisibilité de vos
programmes. Exemple :



```python
couleurs = ['noir', 'brun', 'rouge',
     'orange', 'jaune', 'vert',
     'bleu', 'violet', 'gris', 'blanc']
```



Exercices

.Soient les listes suivantes :

**t1 =
[31,28,31,30,31,30,31,31,30,31,30,31]**\
**t2 = ['Janvier','Février','Mars','Avril','Mai','Juin',**\
**'Juillet','Août','Septembre','Octobre','Novembre','Décembre']**

Écrivez un petit programme qui insère dans la seconde liste tous les
éléments de la première, de telle sorte que chaque nom de mois soit
suivi du nombre de jours correspondant : **['Janvier',31,'Février',28,'Mars',31,
etc.]**.

.Créez une liste **A** contenant quelques éléments. Effectuez une *vraie
copie* de cette liste dans une nouvelle variable **B**. Suggestion :
créez d'abord une liste **B** de même taille que **A** mais ne contenant
que des zéros. Remplacez ensuite tous ces zéros par les éléments tirés
de **A**.

.Même question, mais autre suggestion : créez d'abord une liste **B**
vide. Remplissez-la ensuite à l'aide des éléments de **A** ajoutés l'un
après l'autre.

.Même question, autre suggestion encore : pour créer la liste **B**,
découpez dans la liste **A** une tranche incluant tous les éléments (à
l'aide de l'opérateur **[:]**).

.*Un nombre premier est un nombre qui n'est divisible que par un et par
lui-même*. Écrivez un programme qui établit la liste de tous les nombres
premiers compris entre 1 et 1000, en utilisant la méthode du *crible
d'Eratosthène* :

-   Créez une liste de 1000 éléments, chacun initialisé à la valeur 1.
-   Parcourez cette liste à partir de l'élément d'indice 2 : si
    l'élément analysé possède la valeur 1, mettez à zéro tous les autres
    éléments de la liste, dont les indices sont des multiples entiers de
    l'indice auquel vous êtes arrivé.

Lorsque vous aurez parcouru ainsi toute la liste, les indices des
éléments qui seront restés à 1 seront les nombres premiers recherchés.\
 En effet : A partir de l'indice 2, vous annulez tous les éléments
d'indices pairs : 4, 6, 8, 10, etc. Avec
l'indice 3, vous annulez les éléments d'indices 6, 9, 12, 15, etc., et
ainsi de suite. Seuls resteront à 1 les éléments dont les indices sont
effectivement des nombres premiers.

### 12-B-11 - Nombres aléatoires - histogrammes {#article.xml#Ld0e32653 .TitreSection2}

La plupart des programmes d'ordinateur font exactement la même chose
chaque fois qu'on les exécute. De tels programmes sont dits
*déterministes*. Le déterminisme est certainement une bonne chose : nous
voulons évidemment qu'une même série de calculs appliquée aux mêmes
données initiales aboutisse toujours au même résultat. Pour certaines
applications, cependant, nous pouvons souhaiter que l'ordinateur soit
imprévisible. Le cas des jeux constitue un exemple évident, mais il en
existe bien d'autres.

Contrairement aux apparences, il n'est pas facile du tout d'écrire un
algorithme qui soit réellement non-déterministe (c'est-à-dire qui
produise un résultat totalement *imprévisible*). Il existe cependant des
techniques mathématiques permettant de simuler plus ou moins bien
l'effet du hasard. Des livres entiers ont été écrits sur les moyens de
produire ainsi un hasard « de bonne qualité ». Nous n'allons évidemment
pas développer ici une telle question.

Dans son module **random**, Python propose toute une série de fonctions
permettant de générer des nombres aléatoires qui suivent différentes
distributions mathématiques. Nous n'examinerons ici que quelques-unes
d'entre elles. Veuillez consulter la documentation en ligne pour
découvrir les autres. Vous pouvez importer toutes les fonctions du
module par :



```python
>>> from random import *
```



La fonction ci-dessous permet de créer une liste de nombres réels
aléatoires, de valeur comprise entre zéro et un. L'argument à fournir
est la taille de la liste :



```python
>>> def list_aleat(n):
...    s = [0]*n 
...    for i in range(n):
...	  s[i] =random()
...    return s 
... 
>>> list_aleat(3)
[0.37584811062278767, 0.03459750519478866, 0.714564337038124]
>>> list_aleat(3)
[0.8151025790264931, 0.3772866844634689, 0.8207328556071652] 
```



Vous pouvez constater que nous avons pris le parti de construire d'abord
une liste de zéros de taille n, et ensuite de remplacer les zéros par
des nombres aléatoires.

Exercices

.Réécrivez la fonction **list\_aleat()** ci-dessus, en utilisant la
méthode **append()** pour construire la liste petit à petit à partir
d'une liste vide (au lieu de remplacer les zéros d'une liste
préexistante comme nous l'avons fait).

.Écrivez une fonction **imprime\_liste()** qui permette d'afficher ligne
par ligne tous les éléments contenus dans une liste de taille
quelconque. Le nom de la liste sera fourni en argument. Utilisez cette
fonction pour imprimer la liste de nombres aléatoires générés par la
fonction **list\_aleat()**. Ainsi par exemple, l'instruction `imprime_liste(liste_aleat(8))` devra
afficher une colonne de 8 nombres réels aléatoires.

Les nombres ainsi générés sont-ils vraiment aléatoires ? C'est difficile
à dire. Si nous ne tirons qu'un petit nombre de valeurs, nous ne pouvons
rien vérifier. Par contre, si nous utilisons un grand nombre de fois la
fonction **random()**, nous nous attendons à ce que la moitié des
valeurs produites soient plus grandes que 0,5 (et l'autre moitié plus
petites).

Affinons ce raisonnement. Les valeurs tirées sont toujours dans
l'intervalle 0-1. Partageons cet intervalle en 4 fractions égales : de 0
à 0,25 , de 0,25 à 0,5 , de 0,5 à 0,75 , et de 0,75 à 1.\
 Si nous tirons un grand nombre de valeurs au hasard, nous nous
attendons à ce qu'il y en ait autant qui se situent dans chacune de nos
4 fractions. Et nous pouvons généraliser ce raisonnement à un nombre
quelconque de fractions, du moment qu'elles soient égales.

Exercice

.Vous allez écrire un programme destiné à vérifier le fonctionnement du
générateur de nombres aléatoires de Python en appliquant la théorie
exposée ci-dessus. Votre programme devra donc :

-   Demander à l'utilisateur le nombre de valeurs à tirer au hasard à
    l'aide de la fonction **random()**. Il serait intéressant que le
    programme propose un nombre par défaut (1000 par exemple).
-   Demander à l'utilisateur en combien de fractions il souhaite
    partager l'intervalle des valeurs possibles (c'est-à-dire
    l'intervalle de 0 à 1). Ici aussi, il faudrait proposer un nombre de
    fractions par défaut (5 par exemple). Vous pouvez également limiter
    le choix de l'utilisateur à un nombre compris entre 2 et le 1/10^e^
    du nombre de valeurs tirées au hasard.
-   Construire une liste de N compteurs (N étant le nombre de fractions
    souhaitées). Chacun d'eux sera évidemment initialisé à zéro.
-   Tirer au hasard toutes les valeurs demandées, à l'aide de la
    fonction **random()** , et mémoriser ces valeurs dans une liste.
-   Mettre en œuvre un parcours de la liste des valeurs tirées au hasard
    (boucle), et effectuer un test sur chacune d'elles pour déterminer
    dans quelle fraction de l'intervalle 0-1 elle se situe. Incrémenter
    de une unité le compteur correspondant.
-   Lorsque c'est terminé, afficher l'état de chacun des compteurs.

**Exemple de résultats affichés par un programme de ce type :**



```python
Nombre de valeurs à tirer au hasard (défaut = 1000) : 100
Nombre de fractions dans l'intervalle 0-1 (entre 2 et 10, défaut =5) : 5
Tirage au sort des 100 valeurs ...
Comptage des valeurs dans chacune des 5 fractions ...
11 30 25 14 20
Nombre de valeurs à tirer au hasard (défaut = 1000) : 10000
Nombre de fractions dans l'intervalle 0-1 (entre 2 et 1000, défaut =5) : 5
Tirage au sort des 10000 valeurs ...
Comptage des valeurs dans chacune des 5 fractions ...
1970 1972 2061 1935 2062
```



Une bonne approche de ce genre de problème consiste à essayer d'imaginer
quelles fonctions simples vous pourriez écrire pour résoudre l'une ou
l'autre partie du problème, puis de les utiliser dans un ensemble plus
vaste.

Par exemple, vous pourriez chercher à définir d'abord une fonction
**numeroFraction()** qui servirait à déterminer dans quelle fraction de
l'intervalle 0-1 une valeur tirée se situe. Cette fonction attendrait
deux arguments (la valeur tirée, le nombre de fractions choisi par
l'utilisateur) et fournirait en retour l'index du compteur à incrémenter
(c'est-à-dire le n^o^ de la fraction correspondante). Il existe
peut-être un raisonnement mathématique simple qui permette de déterminer
l'index de la fraction à partir de ces deux arguments. Pensez notamment
à la fonction intégrée **int()**, qui permet de convertir un nombre réel
en nombre entier en éliminant sa partie décimale.

Si vous ne trouvez pas, une autre réflexion intéressante serait
peut-être de construire d'abord une liste contenant les valeurs « pivots
» qui délimitent les fractions retenues (par exemple 0 - 0,25 - 0,5 -
0,75 - 1 dans le cas de 4 fractions). La connaissance de ces valeurs
faciliterait peut-être l'écriture de la fonction **numeroFraction()**
que nous souhaitons mettre au point.

Si vous disposez d'un temps suffisant, vous pouvez aussi réaliser une
version graphique de ce programme, qui présentera les résultats sous la
forme d'un histogramme (diagramme « en bâtons »).

### 12-B-12 - Tirage au hasard de nombres entiers {#article.xml#Ld0e33153 .TitreSection2}

Lorsque vous développerez des projets personnels, il vous arrivera
fréquemment de souhaiter disposer d'une fonction qui permette de tirer
au hasard un nombre entier entre certaines limites. Par exemple, si vous
voulez écrire un programme de jeu dans lequel des cartes à jouer sont
tirées au hasard (à partir d'un jeu ordinaire de 52 cartes), vous aurez
certainement l'utilité d'une fonction capable de tirer au hasard un
nombre entier compris entre 1 et 52.

Vous pouvez pour ce faire utiliser la fonction **randrange()** du module
**random**. Cette fonction peut être utilisée avec 1, 2 ou 3 arguments.

Avec un seul argument, elle renvoie un entier compris entre zéro et la
valeur de l'argument diminué d'une unité. Par exemple, **randrange(6)**
renvoie un nombre compris entre 0 et 5.

Avec deux arguments, le nombre renvoyé est compris entre la valeur du
premier argument et la valeur du second argument diminué d'une unité.
Par exemple, **randrange(2, 8)** renvoie un nombre compris entre 2 et 7.

Si l'on ajoute un troisième argument, celui-ci indique que le nombre
tiré au hasard doit faire partie d'une série limitée d'entiers, séparés
les uns des autres par un certain intervalle, défini lui-même par ce
troisième argument. Par exemple, randrange(3, 13, 3) renverra un des
nombres de la série 3, 6, 9, 12 :



```python
>>> from random import randrange 
>>> for i in range(15):
...    print(randrange(3, 13, 3), end =' ') 
... 
12 6 12 3 3 12 12 12 9 3 9 3 9 3 12
```



Exercices

.Écrivez un script qui tire au hasard des cartes à jouer. Le nom de la
carte tirée doit être correctement présenté, « en clair ». Le programme
affichera par exemple :

**Frappez \<Enter\> pour tirer une carte :
**\
`Dix de Trèfle`\
**Frappez \<Enter\> pour tirer une carte :
**\
`As de Carreau`\
**Frappez \<Enter\> pour tirer une carte :
**\
`Huit de Pique`\
**Frappez \<Enter\> pour tirer une carte :
**\
 etc.


[^note_66]: **range()** donne en réalité accès à un ***itérateur*** (un objet Python générateur de séquences), mais la description des itérateurs sort du cadre que nous nous sommes fixés pour cet ouvrage d'initiation. Veuillez donc consulter la bibliographie, page , ou la documentatio en ligne de Python, si vous souhaitez des éclaircissements.
