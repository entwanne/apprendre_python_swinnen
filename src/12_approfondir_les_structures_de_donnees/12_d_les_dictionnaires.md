## 12-D - Les dictionnaires

Les types de données composites que nous avons abordés jusqu'à présent
(*chaînes*, *listes* et *tuples*) étaient tous des *séquences*,
c'est-à-dire des suites ordonnées d'éléments. Dans une séquence, il est
facile d'accéder à un élément quelconque à l'aide d'un index (un nombre
entier), mais à la condition expresse de connaître son emplacement.

Les ***dictionnaires*** que nous découvrons ici constituent un autre
*type composite*. Ils ressemblent aux listes dans une certaine mesure
(ils sont modifiables comme elles), mais ce ne sont pas des séquences.
Les éléments que nous allons y enregistrer ne seront pas disposés dans
un ordre immuable. En revanche, nous pourrons accéder à n'importe lequel
d'entre eux à l'aide d'un index spécifique que l'on appellera une
***clé***, laquelle pourra être alphabétique, numérique, ou même d'un
type composite sous certaines conditions.

Comme dans une liste, les éléments mémorisés dans un dictionnaire
peuvent être de n'importe quel type. Ce peuvent être des valeurs
numériques, des chaînes, des listes, des tuples, des dictionnaires, et
même aussi des fonctions, des *classes* ou des *instances* (voir plus
loin)[^note_68].

### 12-D-1 - Création d'un dictionnaire {#article.xml#Ld0e34259 .TitreSection2}

À titre d'exemple, nous allons créer un dictionnaire de langue, pour la
traduction de termes informatiques anglais en français.

Puisque le type *dictionnaire* est un type modifiable, nous pouvons
commencer par créer un dictionnaire vide, puis le remplir petit à petit.
Du point de vue de la syntaxe, on reconnaît un dictionnaire au fait que
ses éléments sont enfermés dans une paire d'accolades. Un dictionnaire
vide sera donc noté **{ }** :



```python
>>> dico = {}
>>> dico['computer'] = 'ordinateur'
>>> dico['mouse'] ='souris'
>>> dico['keyboard'] ='clavier'
 
>>> print(dico)
{'computer': 'ordinateur', 'keyboard': 'clavier', 'mouse': 'souris'}
```



Comme vous pouvez l'observer dans la dernière ligne ci-dessus, un
dictionnaire apparaît dans la syntaxe Python sous la forme d'une série
d'éléments séparés par des virgules, le tout étant enfermé entre deux
accolades. Chacun de ces éléments est lui-même constitué d'une paire
d'objets : un index et une valeur, séparés par un double point.

Dans un dictionnaire, les index s'appellent des *clés*, et les éléments
peuvent donc s'appeler des *pairesclé-valeur.* Dans notre dictionnaire
d'exemple, les clés et les valeurs sont des chaînes de caractères.

Veuillez à présent constater que l'ordre dans lequel les éléments
apparaissent à la dernière ligne ne correspond pas à celui dans lequel
nous les avons fournis. Cela n'a strictement aucune importance : nous
n'essaierons jamais d'extraire une valeur d'un dictionnaire à l'aide
d'un index numérique. Au lieu de cela, nous utiliserons les clés :



```python
>>> print(dico['mouse'])
souris
```



Remarquez aussi que contrairement à ce qui se passe avec les listes, il
n'est pas nécessaire de faire appel à une méthode particulière (telle
que **append()**) pour ajouter de nouveaux éléments à un dictionnaire :
il suffit de créer une nouvelle paire clé-valeur.

### 12-D-2 - Opérations sur les dictionnaires {#article.xml#Ld0e34444 .TitreSection2}

Vous savez déjà comment ajouter des éléments à un dictionnaire. Pour en
enlever, vous utiliserez l'instruction intégrée **del**. Créons pour
l'exemple un autre dictionnaire, destiné cette fois à contenir
l'inventaire d'un stock de fruits. Les index (ou clés) seront les noms
des fruits, et les valeurs seront les masses de ces fruits répertoriées
dans le stock (les valeurs sont donc cette fois des données de type
numérique).



```python
>>> invent = {'pommes': 430, 'bananes': 312, 'oranges' : 274, 'poires' : 137}
>>> print(invent)
{'oranges': 274, 'pommes': 430, 'bananes': 312, 'poires': 137}
```



Si le patron décide de liquider toutes les pommes et de ne plus en
vendre, nous pouvons enlever cette entrée dans le dictionnaire :



```python
>>> del invent['pommes']
>>> print(invent)
{'oranges': 274, 'bananes': 312, 'poires': 137}
```



La fonction intégrée **len()** est utilisable avec un dictionnaire :
elle en renvoie le nombre d'éléments :



```python
>>> print(len(invent))
3 
```



### 12-D-3 - Test d'appartenance {#article.xml#Ld0e34642 .TitreSection2}

D'une manière analogue à ce qui se passe pour les chaînes, les listes et
les tuples, l'instruction **in** est utilisable avec les dictionnaires.
Elle permet de savoir si un dictionnaire comprend une **clé** bien
déterminée[^note_69]
:



```python
>>> if "pommes" in invent:
...    print("Nous avons des pommes")
... else:
...    print("Pas de pommes. Sorry")
... 
Pas de pommes. Sorry
```



### 12-D-4 - Les dictionnaires sont des objets {#article.xml#Ld0e34731 .TitreSection2}

On peut appliquer aux dictionnaires un certain nombre de *méthodes*
spécifiques :

La méthode **keys()** renvoie la séquence des *clés* utilisées dans le
dictionnaire. Cette séquence peut être utilisée telle quelle dans les
expressions, ou convertie en liste ou en tuple si nécessaire, avec les
fonctions intégrées correspondantes **list()** et **tuple()** :



```python
>>> print(dico.keys())
dict_keys(['computer', 'mouse', 'keyboard']) 
>>> for k in dico.keys():
...    print("clé :", k, " --- valeur :", dico[k])
... 
clé : computer	  --- valeur : ordinateur 
clé : mouse  --- valeur : souris 
clé : keyboard	  --- valeur : clavier
>>> list(dico.keys())
['computer', 'mouse', 'keyboard'] 
>>> tuple(dico.keys())
('computer', 'mouse', 'keyboard') 
```



De manière analogue, la méthode **values()** renvoie la séquence des
*valeurs* mémorisées dans le dictionnaire :



```python
>>> print(invent.values())
dict_values([274, 312, 137])
```



Quant à la méthode **items()**, elle extrait du dictionnaire une
séquence équivalente de tuples. Cette méthode se révélera très utile
plus loin, lorsque nous voudrons parcourir un dictionnaire à l'aide
d'une boucle :



```python
>>> invent.items() 
dict_items([('poires', 137), ('bananes', 312), ('oranges', 274)]) 
>>> tuple(invent.items()) 
(('poires', 137), ('bananes', 312), ('oranges', 274))
```



La méthode **copy()** permet d'effectuer une *vraie copie* d'un
dictionnaire. Il faut savoir en effet que la simple affectation d'un
dictionnaire existant à une nouvelle variable crée seulement *une
nouvelle référence* vers le même objet, et non un nouvel objet. Nous
avons déjà discuté ce phénomène (*aliasing*) à propos des listes (voir
page ). Par exemple, l'instruction ci-dessous ne définit pas un nouveau
dictionnaire (contrairement aux apparences) :



```python
>>> stock = invent
>>> stock
{'oranges': 274, 'bananes': 312, 'poires': 137}
```



Si nous modifions **invent**, alors **stock** est également modifié, et
vice-versa (ces deux noms désignent en effet le même objet dictionnaire
dans la mémoire de l'ordinateur) :



```python
>>> del invent['bananes']
>>> stock
{'oranges': 274, 'poires': 137}
```



Pour obtenir une vraie copie (indépendante) d'un dictionnaire
préexistant, il faut employer la méthode **copy()** :



```python
>>> magasin = stock.copy()
>>> magasin['prunes'] = 561
>>> magasin
{'oranges': 274, 'prunes': 561, 'poires': 137}
>>> stock
{'oranges': 274, 'poires': 137}
>>> invent
{'oranges': 274, 'poires': 137}
```



### 12-D-5 - Parcours d'un dictionnaire {#article.xml#Ld0e35351 .TitreSection2}

Vous pouvez utiliser une boucle **for** pour traiter successivement tous
les éléments contenus dans un dictionnaire, mais attention :

-   au cours de l'itération, ce sont les *clés* utilisées dans le
    dictionnaire qui seront successivement affectées à la variable de
    travail, et non les *valeurs* ;
-   l'ordre dans lequel les éléments seront extraits est *imprévisible*
    (puisqu'un dictionnaire n'est pas une séquence).

Exemple :



```python
>>> invent ={"oranges":274, "poires":137, "bananes":312}
>>> for clef in invent: 
...    print(clef)
... 
poires 
bananes 
oranges
```



Si vous souhaitez effectuer un traitement sur les valeurs, il vous
suffit alors de récupérer chacune d'elles à partir de la clé
correspondante :



```python
>>> for clef in invent: 
...    print(clef, invent[clef])
... 
poires 137
bananes 312
oranges 274 
```



Cette manière de procéder n'est cependant pas idéale, ni en termes de
performances ni même du point de vue de la lisibilité. Il est recommandé
de plutôt faire appel à la méthode **items()** décrite à la section
précédente :



```python
for clef, valeur in invent.items():
 print(clef, valeur)
... 
poires 137
bananes 312
oranges 274 
```



Dans cet exemple, la méthode **items()** appliquée au dictionnaire
**invent** renvoie une séquence de tuples (clef, valeur). Le parcours
effectué sur cette liste à l'aide de la boucle **for** permet d'examiner
chacun de ces tuples un par un.

### 12-D-6 - Les clés ne sont pas nécessairement des chaînes de caractères {#article.xml#Ld0e35506 .TitreSection2}

Jusqu'à présent nous avons décrit des dictionnaires dont les clés
étaient à chaque fois des valeurs de type *string*. En fait nous pouvons
utiliser en guise de clés n'importe quel type de données *non
modifiables* : des entiers, des réels, des chaînes de caractères, et
même des tuples.

Considérons par exemple que nous voulions répertorier les arbres
remarquables situés dans un grand terrain rectangulaire. Nous pouvons
pour cela utiliser un dictionnaire, dont les clés seront des tuples
indiquant les coordonnées **x,y** de chaque arbre :



```python
>>> arb = {}
>>> arb[(1,2)] = 'Peuplier'
>>> arb[(3,4)] = 'Platane'
>>> arb[6,5] = 'Palmier'
>>> arb[5,1] = 'Cycas'
>>> arb[7,3] = 'Sapin'
 
>>> print(arb)
{(3, 4): 'Platane', (6, 5): 'Palmier', (5, 1):
'Cycas', (1, 2): 'Peuplier', (7, 3): 'Sapin'}
 
>>> print(arb[(6,5)])
palmier
```





![](images/image32.png)



Vous pouvez remarquer que nous avons allégé l'écriture à partir de la
troisième ligne, en profitant du fait que les parenthèses délimitant les
tuples sont facultatives (à utiliser avec prudence !).

Dans ce genre de construction, il faut garder à l'esprit que le
dictionnaire contient des éléments seulement pour certains couples de
coordonnées. Ailleurs, il n'y a rien. Par conséquent, si nous voulons
interroger le dictionnaire pour savoir ce qui se trouve là où il n'y a
rien, comme par exemple aux coordonnées (2,1), nous allons provoquer une
erreur :



```python
>>> print(arb[1,2])
Peuplier
>>> print(arb[2,1])
 
    ***** Erreur : KeyError: (2, 1)  *****
```



Pour résoudre ce petit problème, nous pouvons utiliser la méthode
**get()** :



```python
>>> arb.get((1,2), 'néant')
Peuplier
>>> arb.get((2,1), 'néant')
néant
```



Le premier argument transmis à cette méthode est la clé de recherche, le
second argument est la valeur que nous voulons obtenir en retour si la
clé n'existe pas dans le dictionnaire.

### 12-D-7 - Les dictionnaires ne sont pas des séquences {#article.xml#Ld0e35893 .TitreSection2}

Comme vous l'avez vu plus haut, les éléments d'un dictionnaire ne sont
pas disposés dans un ordre particulier. Des opérations comme la
concaténation et l'extraction (d'un groupe d'éléments contigus) ne
peuvent donc tout simplement pas s'appliquer ici. Si vous essayez tout
de même, Python lèvera une erreur lors de l'exécution du code :



```python
>>> print(arb[1:3])
 
      ***** Erreur : TypeError: unhashable type *****
```



Vous avez vu également qu'il suffit d'affecter un nouvel indice (une
nouvelle clé) pour ajouter une entrée au dictionnaire. Cela ne
marcherait pas avec les listes[^note_70]
:



```python
>>> invent['cerises'] = 987
>>> print(invent)
{'oranges': 274, 'cerises': 987, 'poires': 137}
 
>>> liste =['jambon', 'salade', 'confiture', 'chocolat']
>>> liste[4] ='salami'
 
      ***** IndexError: list assignment index out of range  *****
```



Du fait qu'ils ne sont pas des séquences, les dictionnaires se révèlent
donc particulièrement précieux pour gérer des ensembles de données où
l'on est amené à effectuer fréquemment des ajouts ou des suppressions,
dans n'importe quel ordre. Ils remplacent avantageusement les listes
lorsqu'il s'agit de traiter des ensembles de données numérotées, dont
les numéros ne se suivent pas.

Exemple :



```python
>>> client = {}
>>> client[4317] = "Dupond"
>>> client[256] = "Durand"
>>> client[782] = "Schmidt"
```



etc.

Exercices

.Écrivez un script qui crée un mini-système de base de données
fonctionnant à l'aide d'un dictionnaire, dans lequel vous mémoriserez
les noms d'une série de copains, leur âge et leur taille. Votre script
devra comporter deux fonctions : la première pour le remplissage du
dictionnaire, et la seconde pour sa consultation. Dans la fonction de
remplissage, utilisez une boucle pour accepter les données entrées par
l'utilisateur.\
 Dans le dictionnaire, le nom de l'élève servira de clé d'accès, et les
valeurs seront constituées de tuples (âge, taille), dans lesquels l'âge
sera exprimé en années (donnée de type entier), et la taille en mètres
(donnée de type réel).\
 La fonction de consultation comportera elle aussi une boucle, dans
laquelle l'utilisateur pourra fournir un nom quelconque pour obtenir en
retour le couple « âge, taille » correspondant. Le résultat de la
requête devra être une ligne de texte bien formatée, telle par exemple :
« Nom : Jean Dhoute - âge : 15 ans - taille : 1.74 m ». Pour obtenir ce
résultat, servez-vous du formatage des chaînes de caractères décrit à la
page .

.Écrivez une fonction qui échange les clés et les valeurs d'un
dictionnaire (ce qui permettra par exemple de transformer un
dictionnaire anglais/français en un dictionnaire français/anglais). On
suppose que le dictionnaire ne contient pas plusieurs valeurs
identiques.

### 12-D-8 - Construction d'un histogramme à l'aide d'un dictionnaire {#article.xml#Ld0e36185 .TitreSection2}

Les dictionnaires constituent un outil très élégant pour construire des
*histogrammes*.

Supposons par exemple que nous voulions établir l'histogramme qui
représente la fréquence d'utilisation de chacune des lettres de
l'alphabet dans un texte donné. L'algorithme permettant de réaliser ce
travail est extraordinairement simple si on le construit sur base d'un
dictionnaire :



```python
>>> texte ="les saucisses et saucissons secs sont dans le saloir"
>>> lettres ={}
>>> for c in texte:
...    lettres[c] =lettres.get(c, 0) + 1 
... 
>>> print(lettres)
{'t': 2, 'u': 2, 'r': 1, 's': 14, 'n': 3, 'o': 3, 'l': 3, 'i': 3, 'd': 1, 'e': 5, 'c': 3, '': 8, 'a': 4}
```



Nous commençons par créer un dictionnaire vide : **lettres**. Ensuite,
nous allons remplir ce dictionnaire en utilisant les caractères de
l'alphabet en guise de clés. Les valeurs que nous mémoriserons pour
chacune de ces clés seront les fréquences des caractères correspondants
dans le texte. Afin de calculer celles-ci, nous effectuons un parcours
de la chaîne de caractères **texte**. Pour chacun de ces caractères,
nous interrogeons le dictionnaire à l'aide de la méthode **get()**, en
utilisant le caractère en guise de clé, afin d'y lire la fréquence déjà
mémorisée pour ce caractère. Si cette valeur n'existe pas encore, la
méthode **get()** doit renvoyer une valeur nulle. Dans tous les cas,
nous incrémentons la valeur trouvée, et nous la mémorisons dans le
dictionnaire, à l'emplacement qui correspond à la clé (c'est-à-dire au
caractère en cours de traitement).

Pour fignoler notre travail, nous pouvons encore souhaiter afficher
l'histogramme dans l'ordre alphabétique. Pour ce faire, nous pensons
immédiatement à la méthode **sort()**, mais celle-ci ne peut s'appliquer
qu'aux listes. Qu'à cela ne tienne ! Nous avons vu plus haut comment
nous pouvions convertir un dictionnaire en une liste de tuples :



```python
>>> lettres_triees = list(lettres.items())
>>> lettres_triees.sort()
>>> print(lettres_triees)
[('', 8), ('a', 4), ('c', 3), ('d', 1), ('e', 5), ('i', 3), ('l', 3), ('n', 3), ('o', 3), ('r', 1), ('s', 14), ('t', 2), ('u', 2)]
```



Exercices

.Vous avez à votre disposition un fichier texte quelconque (pas trop
gros). Écrivez un script qui compte les occurrences de chacune des
lettres de l'alphabet dans ce texte (on simplifiera le problème en ne
tenant pas compte des lettres accentuées).

.Modifiez le script ci-dessus afin qu'il établisse une table des
occurrences de chaque *mot* dans le texte. Conseil : dans un texte
quelconque, les mots ne sont pas seulement séparés par des espaces, mais
également par divers signes de ponctuation. Pour simplifier le problème,
vous pouvez commencer par remplacer tous les caractères
non-alphabétiques par des espaces, et convertir la chaîne résultante en
une liste de mots à l'aide de la méthode **split()**.

.Vous avez à votre disposition un fichier texte quelconque (pas trop
gros). Écrivez un script qui analyse ce texte, et mémorise dans un
dictionnaire l'emplacement exact de chacun des mots (compté en nombre de
caractères à partir du début). Lorsqu'un même mot apparaît plusieurs
fois, tous ses emplacements doivent être mémorisés : chaque valeur de
votre dictionnaire doit donc être une liste d'emplacements.

### 12-D-9 - Contrôle du flux d'exécution à l'aide d'un dictionnaire {#article.xml#Ld0e36656 .TitreSection2}

Il arrive fréquemment que l'on ait à diriger l'exécution d'un programme
dans différentes directions, en fonction de la valeur prise par une
variable. Vous pouvez bien évidemment traiter ce problème à l'aide d'une
série d'instructions **if - elif - else** , mais cela peut devenir assez
lourd et inélégant si vous avez affaire à un grand nombre de
possibilités. Exemple :



```python
materiau = input("Choisissez le matériau : ")
 
if materiau == 'fer':
 fonctionA()
elif materiau == 'bois':
 fonctionC()
elif materiau == 'cuivre':
 fonctionB()
elif materiau == 'pierre':
 fonctionD()
elif   ... etc ...
```



Les langages de programmation proposent souvent des instructions
spécifiques pour traiter ce genre de problème, telles les instructions
*switch* ou *case* du *C* ou du *Pascal*. Python n'en propose aucune,
mais vous pouvez vous tirer d'affaire dans bien des cas à l'aide d'une
liste (nous en donnons un exemple détaillé à la page ), ou mieux encore
à l'aide d'un dictionnaire. Exemple :



```python
materiau = input("Choisissez le matériau : ")
 
dico = {'fer':fonctionA,
     'bois':fonctionC,
     'cuivre':fonctionB,
     'pierre':fonctionD,
     ... etc ...}
 
dico[materiau]()
```



Les deux instructions ci-dessus pourraient être condensées en une seule,
mais nous les laissons séparées pour bien détailler le mécanisme :

-   La première instruction définit un dictionnaire **dico** dans lequel
    les clés sont les différentes possibilités pour la variable
    **materiau**, et les valeurs, les noms des fonctions à invoquer en
    correspondance. Notez bien qu'il s'agit seulement des*noms* de ces
    fonctions, *qu'il ne faut surtout pas faire suivre de parenthèses
    dans ce cas* (sinon Python exécuterait chacune de ces fonctions au
    moment de la création du dictionnaire).
-   La seconde instruction invoque la fonction correspondant au choix
    opéré à l'aide de la variable **materiau**. Le nom de la fonction
    est extrait du dictionnaire à l'aide de la clé, puis associé à une
    paire de parenthèses. Python reconnaît alors un appel de fonction
    tout à fait classique, et l'exécute.

Vous pouvez encore améliorer la technique ci-dessus en remplaçant cette
instruction par sa variante ci-dessous, qui fait appel à la méthode
**get()** afin de prévoir le cas où la clé demandée n'existerait pas
dans le dictionnaire (vous obtenez de cette façon l'équivalent d'une
instruction **else** terminant une longue série de **elif**) :



```python
dico.get(materiau, fonctAutre)()
```



Lorsque la la valeur de la variable **materiau** ne correspond à aucune
clé du dictionnaire, c'est la fonction **fonctAutre()** qui est
invoquée.

Exercices

.Complétez l'exercice 10.46 (mini-système de base de données) en lui
ajoutant deux fonctions : l'une pour enregistrer le dictionnaire
résultant dans un fichier texte, et l'autre pour reconstituer ce
dictionnaire à partir du fichier correspondant.\
 Chaque ligne de votre fichier texte correspondra à un élément du
dictionnaire. Elle sera formatée de manière à bien séparer :\
 - la clé et la valeur (c'est-à-dire le nom de la personne, d'une part,
et l'ensemble : « âge + taille », d'autre part ;\
 - dans l'ensemble « âge + taille », ces deux données numériques.\
 Vous utiliserez donc deux caractères séparateurs différents, par
exemple « @ » pour séparer la clé et la valeur, et « \# » pour séparer
les données constituant cette valeur :\
`Juliette@18#1.67`\
`Jean-Pierre@17#1.78`\
`Delphine@19#1.71`\
`Anne-Marie@17#1.63`etc.

.Améliorez encore le script de l'exercice précédent, en utilisant un
dictionnaire pour diriger le flux d'exécution du programme au niveau du
menu principal.\
 Votre programme affichera par exemple :\
`Choisissez :`\
**(R)écupérer un dictionnaire préexistant
sauvegardé dans un fichier**\
**(A)jouter des données au dictionnaire
courant**\
**(C)onsulter le dictionnaire
courant**\
**(S)auvegarder le dictionnaire courant
dans un fichier**\
`(T)erminer :`\
 Suivant le choix opéré par l'utilisateur, vous effectuerez alors
l'appel de la fonction correspondante en la sélectionnant dans un
dictionnaire de fonctions.


[^note_68]: Les listes et les tuples peuvent eux aussi contenir des dictionnaires, des fonctions, des classes ou des instances, Nous n'avions pas mentionné tout cela jusqu'ici, afin de ne pas alourdir l'exposé.

[^note_69]: Dans les versions de Python antérieures à la version 3.0, il fallait faire appel à une méthode particulière (la méthode **has\_key()**)pour effectuer ce test.

[^note_70]: Rappel : les méthodes permettant d'ajouter des éléments à une liste sont décrites page .
