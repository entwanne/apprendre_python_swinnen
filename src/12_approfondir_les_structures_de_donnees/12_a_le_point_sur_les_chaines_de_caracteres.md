## 12-A - Le point sur les chaînes de caractères

Nous avons déjà rencontré les chaînes de caractères au chapitre 5. À la
différence des données numériques, qui sont des entités singulières, les
chaînes de caractères constituent *un type de donnée composite*. Nous
entendons par là une entité bien définie qui est faite elle-même d'un
ensemble d'entités plus petites, en l'occurrence : les caractères.
Suivant les circonstances, nous serons amenés à traiter une telle donnée
composite, tantôt comme un seul objet, tantôt comme une *suite ordonnée
d'éléments*. Dans ce dernier cas, nous souhaiterons probablement pouvoir
accéder à chacun de ces éléments à titre individuel.

En fait, les chaînes de caractères font partie d'une catégorie d'objets
Python que l'on appelle des *séquences*, et dont font partie aussi les
*listes* et les *tuples*. On peut effectuer sur les séquences tout un
ensemble d'opérations similaires. Vous en connaissez déjà quelques unes,
et nous allons en décrire quelques autres dans les paragraphes suivants.

### 12-A-1 - Indiçage, extraction, longueur {#article.xml#Ld0e24528 .TitreSection2}

Petit rappel du chapitre 5 : les chaînes
sont des *séquences*de caractères.
Chacun de ceux-ci occupe une place précise dans la séquence. Sous
Python, les éléments d'une séquence sont toujours *indicés*(ou numérotés) de la même manière, c'est-à-dire
*à partir de zéro*. Pour extraire un
caractère d'une chaîne, il suffit d'accoler au
nom de la variable qui contient cette chaîne, son *indice*entre crochets :



```python
>>> nom = 'Cédric'
>>> print(nom[1], nom[3], nom[5])
é r c
```



Il est souvent utile de pouvoir désigner
l'emplacement d'un caractère par rapport à la fin de la chaîne. Pour ce
faire, il suffit d'utiliser des indices négatifs : ainsi -1 désignera le
dernier caractère, -2 l'avant-dernier, etc. : 



```python
>>> print(nom[-1], nom[-2], nom[-4], nom[-6]) 
c i d C 
>>> 
```



Si l'on désire
déterminer le nombre de caractères présents dans une chaîne, on utilise
la fonction intégrée **len()**
:



```python
>>> print(len(nom))
6
```



### 12-A-2 - Extraction de fragments de chaînes {#article.xml#Ld0e24678 .TitreSection2}

Il arrive fréquemment, lorsque
l'on travaille avec des chaînes, que l'on souhaite
extraire une petite chaîne d'une chaîne
plus longue. Python propose pour cela une technique simple que
l'on appelle *slicing*(« découpage en tranches »). Elle consiste à
indiquer entre crochets les indices correspondant au début et à la fin
de la « tranche » que l'on souhaite extraire :



```python
>>> ch = "Juliette"
>>> print(ch[0:3])
Jul
```



Dans la tranche **[n,m]**, le n^ième^caractère est inclus, mais pas le m^ième^. Si
vous voulez mémoriser aisément ce mécanisme, il faut vous représenter
que les indices pointent des emplacements situés ***entre***les caractères, comme dans le schéma ci-dessous
:



![](images/image30.png)



Les indices de découpage ont des valeurs
par défaut : un premier indice non défini est considéré comme zéro,
tandis que le second indice omis prend par défaut la taille de la chaîne
complète :



```python
>>> print(ch[:3])	# les 3 premiers caractères
Jul
>>> print(ch[3:])    # tout ce qui suit les 3 premiers caractères
iette
```



Les caractères accentués ne doivent pas
faire problème :



```python
>>> ch = 'Adélaïde'
>>> print(ch[:3], ch[4:8])
Adé aïde 
```



### 12-A-3 - Concaténation, répétition {#article.xml#Ld0e24897 .TitreSection2}

Les chaînes peuvent être
*concaténées*avec l'opérateur
**+**et *répétées*avec l'opérateur
**\*** :



```python
>>> n = 'abc' + 'def'      # concaténation
>>> m = 'zut ! ' * 4	   # répétition
>>> print(n, m)
abcdef zut ! zut ! zut ! zut ! 
```



Exercices

.Déterminez vous-même ce qui se passe, dans la technique de *slicing*,
lorsque l'un ou l'autre des indices de découpage est erroné, et décrivez
cela le mieux possible. (Si le second indice est plus petit que le
premier, par exemple, ou bien si le second indice est plus grand que la
taille de la chaîne).

.Découpez une grande chaîne en fragments de 5 caractères chacun.
Rassemblez ces morceaux dans l'ordre inverse. La chaîne doit pouvoir contenir des caractères
accentués.

.Tâchez d'écrire une petite fonction **trouve()** qui fera exactement le
contraire de ce que fait l'opérateur d'indexage (c'est-à-dire les
crochets **[ ]**). Au lieu de partir d'un index donné pour retrouver le
caractère correspondant, cette fonction devra retrouver l'index
correspondant à un caractère donné.\
 En d'autres termes, il s'agit d'écrire une fonction qui attend deux
arguments : le nom de la chaîne à traiter et le caractère à
trouver. La fonction doit fournir en retour
l'index du premier caractère de ce type dans la chaîne. Ainsi par
exemple, l'instruction :\
**print(trouve("Juliette & Roméo",
"&"))**\
 devra afficher : **9**\
 Attention : il faut penser à tous les cas possibles. Il faut notamment
veiller à ce que la fonction renvoie une valeur particulière (par
exemple la valeur -1) si le caractère recherché n'existe pas dans la
chaîne traitée. Les caractères accentués doivent être acceptés.

.Améliorez la fonction de l'exercice précédent en lui ajoutant un
troisième paramètre : l'index à partir duquel la recherche doit
s'effectuer dans la chaîne. Ainsi par exemple, l'instruction :\
**print(trouve ("César & Cléopâtre", "r",
5))**\
 devra afficher : **15** (et non 4 !).

.Écrivez une fonction **compteCar()** qui compte le nombre d'occurrences
d'un caractère donné dans une chaîne. Ainsi :\
**print(compteCar("ananas au
jus","a"))**\
 devra afficher : **4**\
**print(compteCar("Gédéon est déjà
là","é"))**\
 devra afficher : **3.**

### 12-A-4 - Parcours d'une séquence : l'instruction for - in ... {#article.xml#Ld0e25088 .TitreSection2}

Il arrive très souvent que l'on doive
traiter l'intégralité d'une chaîne
caractère par caractère, du premier jusqu'au dernier,
pour effectuer à partir de chacun d'eux une
opération quelconque. Nous appellerons cette opération un
*parcours*. En nous limitant aux
outils Python que nous connaissons déjà, nous pouvons envisager
d'encoder un tel parcours à l'aide
d'une boucle, articulée autour de l'instruction
**while** :



```python
>>> nom ="Joséphine"
>>> index =0
>>> while index < len(nom):
...   print(nom[iindex] + ' *', end =' ')
...   index = index +1
...
J * o * s * é * p * h * i * n * e *
```



Cette boucle *parcourt* donc la chaîne **nom** pour en extraire un à un
tous les caractères, lesquels sont ensuite imprimés avec interposition
d'astérisques. Notez bien que la condition utilisée avec l'instruction
**while** est `index < len(nom)`,
ce qui signifie que le bouclage doit s'effectuer jusqu'à ce que l'on
soit arrivé à l'indice numéro 9 (la chaîne compte en effet 10
caractères). Nous aurons effectivement traité tous les caractères de la
chaîne, puisque ceux-ci sont indicés de 0 à 9.

Le *parcours d'une séquence* est une opération très fréquente en
programmation. Pour en faciliter l'écriture, Python vous propose une
structure de boucle plus appropriée que la boucle **while**, basée sur
le couple d'instructions **for ... in ... :**

Avec ces instructions, le programme
ci-dessus devient :



```python
>>> nom ="Cléopâtre" 
>>> for car in nom:
...    print(car + ' *', end =' ')
... 
C * l * é * o * p * â * t * r * e *
```



Comme vous pouvez le constater, cette structure de boucle est plus
compacte. Elle vous évite d'avoir à définir et à incrémenter une
variable spécifique (un « compteur ») pour gérer l'indice du caractère
que vous voulez traiter à chaque itération (c'est Python qui s'en
charge). La structure **for ... in ...** ne montre donc que l'essentiel,
à savoir que variable **car** contiendra successivement tous les
caractères de la chaîne, du premier jusqu'au dernier.

L'instruction
**for**permet donc d'écrire des
boucles, dans lesquelles *l'itération traite successivement tous
les éléments d'une séquence donnée*. Dans
l'exemple ci-dessus, la séquence était une chaîne
de caractères. L'exemple ci-après démontre que l'on peut
appliquer le même traitement aux *listes*(et il en sera de même pour les
*tuples*étudiés plus loin) :



```python
liste = ['chien', 'chat', 'crocodile', u'éléphant']
for animal in liste:
 print('longueur de la chaîne', animal, '=', len(animal))
```



L'exécution de
ce script donne :



```python
longueur de la chaîne chien = 5
longueur de la chaîne chat = 4
longueur de la chaîne crocodile = 9
longueur de la chaîne éléphant = 8
```



L'instruction **for ... in ... :** est un nouvel exemple d'*instruction
composée*. N'oubliez donc pas le double point obligatoire à la fin de la
ligne, et l'indentation pour le bloc d'instructions qui suit.

Le nom qui suit le mot réservé
**in**est celui de la séquence
qu'il faut traiter. Le nom qui suit le mot
réservé**for**est celui que vous
choisissez pour la *variable*destinée à contenir successivement tous les
éléments de la séquence. Cette variable est définie automatiquement
(c'est-à-dire qu'il est
inutile de la définir au préalable), et *son type est
automatiquement adapté*à celui de
l'élément de la séquence qui est en cours de
traitement (rappelons en effet que dans le cas d'une liste,
tous les éléments ne sont pas nécessairement du même type). Exemple
:



```python
divers = ['lézard', 3, 17.25, [5, 'Jean']]
for e in divers:
 print(e, type(e))
```



L'exécution de
ce script donne :



```python
lézard <class 'str'> 
3 <class 'int'>
17.25 <class 'float'>
[5, 'Jean'] <class 'list'>
```



Bien que les éléments de la liste
**divers**soient tous de types
différents (une chaîne de caractères, un entier, un réel, une liste), on
peut affecter successivement leurs contenus à la variable
**e**, sans qu'il
s'ensuive des erreurs (ceci est rendu possible
grâce au *typage dynamique*des
variables Python).

Exercices

.Dans un conte américain, huit petits canetons s'appellent
respectivement : *Jack, Kack, Lack, Mack, Nack, Oack, Pack et Qack*.
Écrivez un petit script qui génère tous ces noms à partir des deux
chaînes suivantes :

**prefixes = 'JKLMNOP'** et **suffixe = 'ack'**

Si vous utilisez une instruction **for ... in ...**, votre script ne
devrait comporter que deux lignes.

.Dans un script, écrivez une fonction qui recherche le nombre de mots
contenus dans une phrase donnée.

.Écrivez un script qui recherche le nombre de caractères "e", "é", "è",
"ê", "ë" contenus dans une phrase donnée.

### 12-A-5 - Appartenance d'un élément à une séquence : l'instruction in utilisée seule {#article.xml#Ld0e25721 .TitreSection2}

L'instruction
**in**peut être utilisée
indépendamment de **for**, pour
*vérifier si un élément donné fait partie ou non d'une
séquence*. Vous pouvez par exemple vous
servir de **in**pour vérifier si tel
caractère alphabétique fait partie d'un groupe
bien déterminé :



```python
car = "e"
voyelles = "aeiouyAEIOUYàâéèêëùîï"
if car in voyelles:
 print(car, "est une voyelle")
```



D'une manière
similaire, vous pouvez vérifier l'appartenance
d'un élément à une liste :



```python
n = 5
premiers = [1, 2, 3, 5, 7, 11, 13, 17]
if n in premiers:
 print(n, "fait partie de notre liste de nombres premiers")
```



> Cette instruction très puissante effectue
> donc à elle seule un véritable parcours de la séquence. À titre
> d*'*exercice, écrivez les instructions qui
> effectueraient le même travail à l*'*aide
> d*'*une boucle classique utilisant l*'*instruction while.

Exercices

.Écrivez une fonction
**estUnChiffre()**qui renvoie « vrai
», si l'argument transmis est un chiffre, et « faux » sinon. Tester
ainsi tous les caractères d'une chaîne en parcourant celle-ci à l'aide
d'une boucle **for**.

.Écrivez une fonction **estUneMaj()** qui renvoie « vrai » si l'argument
transmis est une majuscule. Tâchez de tenir compte des majuscules
accentuées !

.Écrivez une fonction **chaineListe()** qui convertisse une phrase en
une liste de mots.

.Utilisez les fonctions définies dans les exercices précédents pour
écrire un script qui puisse extraire d'un texte tous les mots qui
commencent par une majuscule.

.Utilisez les fonctions définies dans les
exercices précédents pour écrire une fonction qui renvoie le nombre de
caractères majuscules contenus dans une phrase donnée en
argument.

### 12-A-6 - Les chaînes sont des séquences non modifiables {#article.xml#Ld0e25946 .TitreSection2}

Vous ne pouvez pas modifier le contenu
d'une chaîne existante. En d'autres
termes, vous ne pouvez pas utiliser l'opérateur
**[ ]**dans la partie gauche
d'une instruction d'affectation.
Essayez par exemple d'exécuter le petit script suivant (qui cherche
intuitivement à remplacer une lettre dans une chaîne) :



```python
salut = 'bonjour à tous'
salut[0] = 'B'
print(salut)
```



Le résultat attendu par le programmeur qui a écrit ces instructions est
« Bonjour à tous » (avec un B majuscule). Mais contrairement à ses
attentes, ce script *lève* une erreur du genre : *TypeError: 'str'
object does not support item assignment*. Cette erreur est provoquée à
la deuxième ligne du script. On y essaie de remplacer une lettre par une
autre dans la chaîne, mais cela n'est pas permis.

Par contre, le script ci-dessous fonctionne
parfaitement :



```python
salut = 'bonjour à tous'
salut = 'B' + salut[1:]
print salut
```



Dans cet autre exemple, en effet, nous ne modifions pas la chaîne
**salut**. Nous en re-créons une nouvelle, avec le même nom, à la
deuxième ligne du script (à partir d'un morceau de la précédente, soit,
mais qu'importe : il s'agit bien d'une *nouvelle* chaîne).

### 12-A-7 - Les chaînes sont comparables {#article.xml#Ld0e26076 .TitreSection2}

Tous les opérateurs de comparaison dont
nous avons parlé à propos des instructions de contrôle de flux
(c'est-à-dire les instructions **if ... elif ... else**) fonctionnent aussi avec les chaînes de
caractères. Cela peut vous être utile pour trier des mots par ordre
alphabétique :



```python
while True: 
 mot = input("Entrez un mot quelconque : (<enter> pour terminer)")
 if mot =="": 
     break
 if mot < "limonade": 
     place = "précède" 
 elif mot > "limonade": 
     place = "suit" 
 else: 
     place = "se confond avec" 
 print("Le mot", mot, place, "le mot 'limonade' dans l'ordre alphabétique")
```



Ces comparaisons sont possibles, parce que dans toutes les normes
d'encodage, les codes numériques représentant les caractères ont été
attribués dans l'ordre alphabétique, tout au moins pour les caractères
non accentués. Dans le système de codage *ASCII*, par exemple, A=65,
B=66, C=67, etc.

Comprenez cependant que cela ne fonctionne bien que pour des mots qui
sont tous entièrement en minuscules, ou entièrement en majuscules, et
qui ne comportent aucun caractère accentué. Vous savez en effet que les
majuscules et minuscules utilisent des ensembles de codes distincts.
Quant aux caractères accentués, vous avez vu qu'ils sont encodés en
dehors de l'ensemble constitué par les caractères du standard *ASCII*.
Construire un algorithme de tri alphabétique qui prenne en compte à la
fois la casse des caractères et tous leurs accents n'est donc pas une
mince affaire !

### 12-A-8 - La norme Unicode {#article.xml#Ld0e26290 .TitreSection2}

À ce stade, il peut être utile de s'intéresser aux valeurs des
identifiants numériques associés à chaque caractère. Sous Python 3, les
chaînes de caractères (données de type string) sont désormais des
chaînes Unicode[^note_58],
ce qui signifie que les identifiants numériques de leurs caractères sont
uniques (il ne peut exister qu'un seul caractère typographique pour
chaque code) et universels (les identifiants choisis couvrent la gamme
complète de tous les caractères utilisés dans les différentes langues du
monde entier).

À l'origine du développement des technologies informatiques, alors que
les capacités de mémorisation des ordinateurs étaient encore assez
limitées, on n'imaginait pas que ceux-ci seraient utilisés un jour pour
traiter d'autres textes que des communications techniques,
essentiellement en anglais. Il semblait donc tout-à-fait raisonnable de
ne prévoir pour celles-ci qu'un jeu de caractères restreint, de manière
à pouvoir représenter chacun de ces caractères avec un petit nombre de
bits, et ainsi occuper aussi peu d'espace que possible dans les
coûteuses unités de stockage de l'époque. Le jeu de caractères
*ASCII*[^note_59]
fut donc choisi en ce temps là, avec l'estimation que 128 caractères
suffiraient (à savoir le nombre de combinaisons possibles pour des
groupes de 7 bits[^note_60]).
En l'étendant par la suite à 256 caractères, on put l'adapter aux
exigences du traitement des textes écrits dans d'autres langues que
l'anglais, mais au prix d'une dispersion des normes (ainsi par exemple,
la norme *ISO-8859-1 (latin-1)* codifie tous les caractères accentués du
français ou de l'allemand (entre autres), mais aucun caractère grec,
hébreu ou cyrillique. Pour ces langues, il faudra respectivement
utiliser les normes *ISO-8859-7, ISO-8859-8, ISO-8859-5*, bien
évidemment incompatibles, et d'autres normes encore pour l'arabe, le
tchèque, le hongrois...

L'intérêt résiduel de ces normes anciennes réside dans leur simplicité.
Elles permettent en effet aux développeurs d'applications informatiques
de considérer que *chaque caractère typographique est assimilable à un
octet*, et que par conséquent une chaîne de caractères n'est rien
d'autre qu'une séquence d'octets. C'est ainsi que fonctionnait l'ancien
type de données *string* de Python (dans les versions antérieures à la
version 3.0).

Toutefois, comme nous l'avons déjà évoqué sommairement au chapitre 5,
les applications informatiques modernes ne peuvent plus se satisfaire de
ces normes étriquées. Il faut désormais pouvoir encoder, dans un même
texte, tous les caractères de n'importe quel alphabet de n'importe
quelle langue. Une organisation internationale a donc été créée : le
*Consortium Unicode*, laquelle a effectivement développé une norme
universelle sous le nom de *Unicode*. Cette nouvelle norme vise à donner
à tout caractère de n'importe quel système d'écriture de langue un nom
et un identifiant numérique, et ce de manière unifiée, quelle que soit
la plate-forme informatique ou le logiciel.

Une difficulté se présente, cependant. Se voulant universelle, la norme
*Unicode* doit attribuer un identifiant numérique *différent* à
plusieurs dizaines de milliers de caractères. Tous ces identifiants ne
pourront évidemment pas être encodés sur un seul octet. À première vue,
ils serait donc tentant de décréter qu'à l'avenir, chaque caractère
devra être encodé sur deux octets (cela ferait 65536 possibilités), ou
trois (16777216 possibilités) ou quatre (plus de 4 milliards de
possibilités). Chacun de ces choix rigides entraîne cependant son lot
d'inconvénients. Le premier, commun à tous, est que l'on perd la
compatibilité avec la multitude de documents informatiques préexistants
(et notamment de logiciels), qui ont été encodés aux normes anciennes,
sur la base du paradigme « un caractère égale un octet ». Le second est
lié à l'impossibilité de satisfaire deux exigences contradictoires : si
l'on se contente de deux octets, on risque de manquer de possibilités
pour identifier des caractères rares ou des attributs de caractères qui
seront probablement souhaités dans l'avenir ; si l'on impose trois,
quatre octets ou davantage, par contre, on aboutit à un monstrueux
gaspillage de ressources : la plupart des textes courants se
satisfaisant d'un jeu de caractères restreint, l'immense majorité de ces
octets ne contiendraient en effet que des zéros.

Afin de ne pas se retrouver piégée dans un carcan de ce genre, la norme
*Unicode* ne fixe aucune règle concernant le nombre d'octets ou de bits
à réserver pour l'encodage. Elle spécifie seulement la valeur numérique
de l'identifiant associé à chaque caractère. En fonction des besoins,
chaque système informatique est donc libre d'encoder « en interne » cet
identifiant comme bon lui semble, par exemple sous la forme d'un entier
ordinaire. Comme tous les langages de programmation modernes, Python
s'est donc pourvu d'un type de données « chaîne de caractères » (le type
*string*) qui respecte scrupuleusement la norme *Unicode*, et la
représentation « interne » des codes numériques correspondants est sans
importance pour le programmeur.

Nous verrons un peu plus loin dans ce chapitre qu'il est effectivement
possible de placer dans une chaîne de ce type un mélange quelconque de
caractères issus d'alphabets différents (qu'il s'agisse de caractères
*ASCII* standards, de caractères accentués, de symboles mathématiques ou
de caractères grecs, cyrilliques, arabes, etc.), et que chacun d'eux est
effectivement représenté « en interne » par un code numérique unique.

### 12-A-9 - Séquences d'octets : le type bytes {#article.xml#Ld0e26362 .TitreSection2}

À ce stade de nos explications, il devient urgent de préciser encore
quelque chose.

Nous avons donc vu que la norme *Unicode* ne fixe en fait rien d'autre
que des valeurs numériques, pour tous les identifiants standardisés
destinés à désigner de manière univoque les caractères des alphabets du
monde entier (plus de 240000 en novembre 2005). Elle ne précise en
aucune façon la manière dont ces valeurs numériques doivent être
encodées concrètement sous forme d'octets ou de bits.

Pour le fonctionnement *interne* des applications informatiques, cela
n'a pas d'importance. Les concepteurs de langages de programmation, de
compilateurs ou d'interpréteurs pourront décider librement de
représenter ces caractères par des entiers sur 8, 16, 24, 32, 64 bits,
ou même (bien que l'on n'en voie pas l'intérêt !) par des réels en
virgule flottante : c'est leur affaire et cela ne nous concerne pas.
Nous ne devons donc pas nous préoccuper du format réel des caractères, à
l'intérieur d'une chaîne *string* de Python.

***Il en va tout autrement, par contre, pour les entrées/sorties***. Les
développeurs que nous sommes devons absolument pouvoir préciser sous
quelle forme exacte les données sont attendues par nos programmes, que
ces données soient fournies par l'intermédiaire de frappes au clavier ou
par importation depuis une source quelconque. De même, nous devons
pouvoir choisir le format des données que nous exportons vers n'importe
quel dispositif périphérique, qu'il s'agisse d'une imprimante, d'un
disque dur, d'un écran...

Pour toutes ces entrées ou sorties de chaînes de caractères, nous
devrons donc toujours considérer qu'il s'agit *concrètement* de
séquences d'octets, et utiliser divers mécanismes pour convertir ces
séquences d'octets en chaînes de caractères, ou vice-versa.

Python met désormais à votre disposition le nouveau type de données
**bytes**, spécifiquement conçu pour traiter les séquences (ou chaînes)
d'octets. Les données de type *bytes* sont très similaires aux données
de type *string*, mais avec la différence que ce sont strictement des
séquences d'octets, et non des séquences de caractères. Les caractères
peuvent bien entendu être *encodés* en octets, et les octets *décodés*
en caractères, mais pas de manière univoque : du fait qu'il existe
plusieurs normes d'encodage/décodage, la même chaîne *string* peut être
convertie en plusieurs chaînes *bytes* différentes.

À titre d'exemple[^note_61], nous allons effectuer à la ligne de commande un
petit exercice d'écriture/lecture d'un fichier texte, en exploitant
quelques possibilités de la fonction **open()**que nous n'avions pas encore rencontrées
jusqu'ici. Nous veillerons à faire cet exercice avec une chaîne
contenant quelques caractères accentués, ou d'autres symboles
*non-ASCII* :



```python
>>> chaine = "Amélie et Eugène\n" 
>>> of =open("test.txt", "w") 
>>> of.write(chaine) 
17 
>>> of.close()
```



Avec ces quelques lignes, nous avons
enregistré la chaîne de caractères **chaine**sous la forme d'une ligne de texte dans un
fichier, de la manière habituelle. Effectuons à présent une relecture de
ce fichier, mais en veillant à ouvrir celui-ci *en mode « binaire
»*, ce qui peut se faire aisément en
transmettant l'argument `"rb"`à la
fonction **open()**. Dans ce mode,
les octets sont transférés à l'état brut, sans conversion d'aucune
sorte. La lecture avec **read()**ne
nous fournit donc plus une chaîne de caractères comme au chapitre
précédent, mais bien une chaîne d'octets, et la variable qui les
accueille est pour cette raison automatiquement typée comme variable du
type*bytes* :



```python
>>> of =open("test.txt", "rb")     # "rb" => mode lecture (r) binaire (b)
>>> octets =of.read()
>>> of.close() 
>>> type(octets) 
<class 'bytes'>
```



En procédant ainsi, nous ne récupérons donc
pas notre chaîne de caractères initiale, mais bien sa traduction
concrète en octets, dans une donnée de type *bytes*. Essayons d'afficher cette donnée à l'aide de la
fonction **print()** :



```python
>>> print(octets)
b'Am\xc3\xa9lie et Eug\xc3\xa8ne\n'
```



Que signifie ce résultat ?

Lorqu'on lui demande d'afficher une donnée de type *bytes* à l'aide la
fonction **print()**, Python nous en fournit en fait une
*représentation*, entre deux apostrophes pour indiquer qu'il s'agit
d'une chaîne, mais celles-ci précédées d'un **b** minuscule pour
spécifier qu'il s'agit d'une chaîne d'octets (*bytes)*, avec les
conventions suivantes :

-   Les octets de valeur numérique comprise entre 32 et 127 sont
    représentés par le caractère correspondant du code ASCII.
-   Certains octets de valeur numérique inférieure à 32 sont représentés
    de manière conventionnelle, comme par exemple le caractère de fin de
    ligne.
-   Les autres octets sont représentés par leur valeur hexadécimale,
    précédée de « `\x` ».

Dans le cas de notre exemple, on voit que les caractères non accentués
de la chaîne utilisée ont été encodés chacun à l'aide d'un seul octet
correspondant à son code ASCII : nous les reconnaissons donc
directement. Les caractères accentués, par contre (ils n'existent pas
dans le code ASCII), sont encodés chacun sur deux octets : \\xc3 et
\\xa9 pour le « é », \\xc3 et \\xa8 pour le « è ». Cette forme
particulière d'encodage correspond à la norme *Utf-8*, que nous
décrirons un peu plus en détail dans les pages suivantes.

La représentation obtenue avec **print()** nous aide à reconnaître notre
chaîne initiale, certes, mais elle ne nous montre pas assez bien qu'il
s'agit en fait d'octets. Essayons donc autre chose. Vous savez que l'on
peut aussi examiner le contenu d'une séquence, élément par élément, à
l'aide d'une boucle de *parcours*. Voyons ce que cela donne ici :



```python
>>> for oct in octets: 
...    print(oct, end =' ')
... 
65 109 195 169 108 105 101 32 101 116 32 69 117 103 195 168 110 101 10 
```



Cette fois, nous voyons très clairement qu'il s'agit bien d'octets : le
parcours nous en restitue toutes les valeurs numériques, en notation
décimale.

Du fait que les caractères accentués sont encodés sur deux octets en
*Utf-8*, la fonction **len()** ne nous renvoie pas la même valeur pour
la chaîne de caractères, et pour son équivalent encodé en *Utf-8* dans
une chaîne d'octets :



```python
>>> len(chaine) 
17
>>> len(octets)
19
```



Les opérations d'extraction d'éléments, de slicing, etc., fonctionnent
de manière analogue avec des données de type *byte* et de type *string*,
quoique avec des résultats différents, bien entendu :



```python
>>> print(chaine[2], chaine[12], "---", chaine[2:12]) 
é g --- élie et Eu
>>> print(octets[2], octets[12], "---", octets[2:12])
195 117 --- b'\xc3\xa9lie et E' 
```



***Attention :*** Vous ne pouvez pas *enregistrer* une chaîne d'octets
telle quelle dans un fichier texte. Exemple :



```python
>>> of =open("test.txt", "w") 
>>> of.write(octets) 
Traceback (most recent call last): 
 File "<stdin>", line 1, in <module> 
TypeError: must be str, not bytes 
```



Pour enregistrer une séquence d'octets, il faut toujours ouvrir le
fichier *en mode binaire*, en utilisant l'argument **"wb"** au lieu de
**"w"** dans l'instruction **open()**.

Remarquons pour terminer que nous pouvons définir une variable de type
*bytes* et lui affecter une valeur littérale, en utilisant la syntaxe :
`var = b'`*chaîne de caractères
ASCII*`'` .

### 12-A-10 - L'encodage Utf-8 {#article.xml#Ld0e27118 .TitreSection2}

Tout ce qui précède nous indique que la chaîne de caractères initiale de
notre exemple a dû être automatiquement convertie, lors de son
enregistrement dans un fichier, en une chaîne d'octets encodés suivant
la norme *Utf-8*. La séquence d'octets dont nous avons traité jusqu'ici
correspond donc à une forme particulière d'encodage numérique, pour la
chaîne de caractères : « Amélie et Eugène »

Même si cela peut vous paraître à première vue un peu compliqué,
dites-vous bien que malheureusement l'encodage idéal n'existe pas. En
fonction de ce que l'on veut en faire, il peut être préférable d'encoder
un même texte de plusieurs manières différentes. C'est pour cette raison
qu'ont été définies, en parallèle avec la norme *Unicode*, plusieurs
*normes d'encodage* : *Utf-8, Utf-16, Utf-32,* et quelques variantes.
Toutes ces normes utilisent les mêmes identifiants numériques pour
encoder les caractères, mais elles diffèrent sur la manière
d'enregistrer concrètement ces identifiants sous forme d'octets. Ne vous
affolez pas, cependant : vous ne serez vraisemblablement jamais
confronté qu'à la première d'entre elles (*Utf-8*). Les autres ne
concerneront que certains spécialistes de domaines « pointus ».

La norme d'encodage *Utf-8* est désormais la norme préférentielle pour
la plupart des textes courants, parce que :

-   d'une part, elle assure une parfaite compatibilité avec les textes
    encodés en « pur » *ASCII* (ce qui est le cas de nombreux codes
    sources de logiciels), ainsi qu'une compatibilité partielle avec les
    textes encodés à l'aide de ses variantes « étendues », telles que
    *Latin-1* ;
-   d'autre part, cette nouvelle norme est celle qui est la plus économe
    en ressources, tout au moins pour les textes écrits dans une langue
    occidentale.

Suivant cette norme, les caractères du jeu *ASCII* standard sont encodés
sur un seul octet. Les autres seront encodés en général sur deux octets,
parfois trois ou même quatre octets pour les caractères les plus rares.

À titre de comparaison, rappelons ici que la norme la plus couramment
utilisée avant *Utf-8* par les francophones, était la norme *Latin-1*
(elle est encore largement répandue, en particulier dans les
environnements de travail Windows). Cette norme permettait d'encoder sur
un seul octet un jeu de caractères accentués restreint, correspondant
aux principales langues de l'Europe occidentale (Français, Allemand,
Portugais, etc.).

Les normes Utf-16 et Utf-32 encodent systématiquement tous les
caractères sur deux octets pour la première, et quatre octets pour la
seconde. Ces normes ne sont utilisées que pour des usages très
spécifiques, comme par exemple pour le traitement interne des chaînes de
caractères par un compilateur. Vous ne les rencontrerez guère.

### 12-A-11 - Conversion (encodage/décodage) des chaînes {#article.xml#Ld0e27171 .TitreSection2}

Avec les versions de Python antérieures à la version 3.0, comme dans
beaucoup d'autres langages, il fallait fréquemment convertir les chaînes
de caractères d'une norme d'encodage à une autre. Du fait des
conventions et des mécanismes adoptés désormais, vous ne devrez plus
beaucoup vous en préoccuper pour vos propres programmes traitant des
données récentes.

Il vous arrivera cependant de devoir convertir des fichiers encodés
suivant une norme ancienne et/ou étrangère : un programmeur digne de ce
nom doit être capable d'effectuer ces conversions. Python vous fournit
fort heureusement les outils nécessaires, sous la forme de *méthodes*
des objets concernés.

#### 12-A-11-A - Conversion d'une chaîne bytes en chaîne string {#article.xml#Ld0e27181 .TitreSection3}

Considérons par exemple la séquence d'octets obtenue à la fin de notre
précédent petit exercice. Si nous savons que cette séquence correspond à
un texte encodé suivant la norme *Utf-8*, nous pouvons la *décoder* en
chaîne de caractères à l'aide de la méthode **decode()**, avec
l'argument `"Utf-8"` (ou
indifféremment : `"utf-8"`,
`"Utf8"` ou `"utf8"`) :



```python
>>> ch_car = octets.decode("utf8")
>>> ch_car 
'Amélie et Eugène\n' 
>>> type(ch_car)
<class 'str'>
```



Le *parcours* de la chaîne obtenue nous fournit bien des caractères,
cette fois :



```python
>>> for c in ch_car:
...    print(c, end =' ')
... 
A m é l i e   e t   E u g è n e 
```



#### 12-A-11-B - Conversion d'une chaîne string en chaîne bytes {#article.xml#Ld0e27315 .TitreSection3}

Pour convertir une chaîne de caractères en une séquence d'octets,
encodée suivant une norme particulière, on utilise la méthode
**encode()**, qui fonctionne de manière parfaitement symétrique à la
méthode **decode()** décrite précédemment. Convertissons par exemple la
même chaîne de caractères, à la fois en *Utf-8* et en *Latin-1* pour
comparaison :



```python
>>> chaine = "Bonne fête de Noël" 
>>> octets_u = chaine.encode("Utf-8") 
>>> octets_l = chaine.encode("Latin-1") 
>>> octets_u 
b'Bonne f\xc3\xaate de No\xc3\xabl' 
>>> octets_l 
b'Bonne f\xeate de No\xebl' 
```



Dans les séquences d'octets ainsi obtenues, on voit clairement que les
caractères accentués « ê » et « ë » sont encodés à l'aide de deux octets
dans le cas de la séquence *Utf-8*, et à l'aide d'un seul octet dans le
cas de la séquence *Latin-1*.

#### 12-A-11-C - Conversions automatiques lors du traitement des fichiers {#article.xml#Ld0e27492 .TitreSection3}

Il vous faut à présent reconsidérer ce qui se passe lorsque vous
souhaitez mémoriser des chaînes de caractères dans un fichier texte.

Jusqu'à présent, en effet, nous n'avons pas attiré votre attention sur
le problème constitué par la norme d'encodage de ces chaînes, parce que
la fonction **open()** de Python dispose fort heureusement d'un
paramétrage par défaut qui convient à la plupart des situations modernes
concrètes. Lorsque vous ouvrez un fichier en écriture, par exemple, en
choisissant `"w"` ou `"a"` comme deuxième argument pour
**open()**, Python encode automatiquement les chaînes à enregistrer en
suivant la norme par défaut de votre système d'exploitation (dans nos
exemples, nous avons considéré qu'il s'agissait de *Utf-8*), et la
conversion inverse est effectuée lors des opérations de lecture[^note_62].
Nous avons donc pu aborder l'étude des fichiers, au chapitre précédent,
sans vous encombrer l'esprit avec des explications trop détaillées.

Dans les petits exercices des pages précédentes, nous avons encore
exploité sans le dire cette facilité offerte par Python. Mais voyons à
présent comment enregistrer des textes en leur appliquant un encodage
différent de celui qui est prévu par défaut, ne serait-ce que pour nous
assurer que l'encodage réalisé soit bien celui que nous voulons (nous
devons absolument procéder ainsi si nous souhaitons que nos scripts
puissent être utilisés sur différents OS).

La technique est simple. Il suffit d'indiquer cet encodage à **open()**
à l'aide d'un argument supplémentaire : `encoding ="`*norme\_choisie*`"`. À titre d'exemple, nous pouvons
refaire les exercices des pages précédentes en forçant cette fois
l'encodage en *Latin-1* :



```python
>>> chaine ="Amélie et Eugène\n" 
>>> of =open("test.txt", "w", encoding ="Latin-1")
>>> of.write(chaine)
17
>>> of.close()
>>> of =open("test.txt", "rb")
>>> octets =of.read()
>>> of.close()
>>> print(octets)
b'Am\xe9lie et Eug\xe8ne\n' 
```



… etc.

(À vous d'effectuer divers contrôles et essais sur cette séquence
d'octets, si vous le souhaitez).

C'est pareil lorsque vous ouvrez un fichier *en lecture*. Par défaut,
Python considère que le fichier est encodé suivant la norme par défaut
de votre système d'exploitation, mais ce n'est évidemment pas une
certitude. Essayons par exemple de ré-ouvrir sans précaution le fichier
*test.txt* que nous venons de créer dans les lignes précédentes :



```python
>>> of =open("test.txt", "r")
>>> ch_lue =of.read() 
Traceback (most recent call last): 
 File "<stdin>", line 1, in <module>
 File "/usr/lib/python3.1/codecs.py", line 300, in decode 
 (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf8' codec can't decode bytes in position 2-4:
invalid data 
```



Le message d'erreur est explicite : supposant que le fichier était
encodé en *Utf-8*, Python n'a pas pu le décoder[^note_63].
Tout rentre dans l'ordre si nous précisons :



```python
>>> of =open("test.txt", "r", encoding ="Latin-1") 
>>> ch_lue =of.read() 
>>> of.close() 
>>> ch_lue 
'Amélie et Eugène\n' 
```



Dans les scripts élaborés, il sera probablement toujours préférable de
préciser l'encodage supposé pour les fichiers que vous traitez, quitte à
devoir demander cette information à l'utilisateur, ou à imaginer des
tests plus ou moins élaborés pour le déterminer de façon automatique (ce
qui est loin d'être évident !).

#### 12-A-11-D - Cas des scripts Python {#article.xml#Ld0e28023 .TitreSection3}

Les scripts Python que vous écrivez sont eux-mêmes des textes, bien
entendu.\
 Suivant la configuration de votre logiciel éditeur, ou de votre OS, ces
textes pourront donc se retrouver encodés suivant différentes normes.
Afin que Python puisse les interpréter correctement, il vous est
conseillé d'y inclure toujours l'un des pseudo-commentaires suivants
(obligatoirement à la 1^e^ ou à la 2^e^ ligne) :



```python
# -*- coding:Latin-1 -*-
```



Ou bien :



```python
# -*- coding:Utf-8 -*-
```



… en indiquant l'encodage effectivement utilisé, bien évidemment !

Ainsi l'interpréteur Python sait décoder correctement les chaînes de
caractères littérales que vous avez utilisées dans le script. Notez que
vous pouvez omettre ce pseudo-commentaire si vous êtes certain que vos
scripts sont encodés en *Utf-8*, car c'est cet encodage qui est
désormais la norme par défaut pour les scripts Python[^note_64].

### 12-A-12 - Accéder à d'autres caractères que ceux du clavier {#article.xml#Ld0e28078 .TitreSection2}

Voyons à présent quel parti vous pouvez tirer du fait que tous les
caractères possèdent leur identifiant numérique universel *Unicode*.
Pour accéder à ces identifiants, Python met à votre disposition un
certain nombre de fonctions prédéfinies :

La fonction **ord(ch)** accepte n'importe quel caractère comme argument.
En retour, elle fournit la valeur de l'identifiant numérique
correspondant à ce caractère. Ainsi `ord("A")` renvoie la valeur 65, et
**ord("Ĩ")**
renvoie la valeur 296.

La fonction **chr(num)** fait exactement le contraire, en vous
présentant le caractère typographique dont l'identifiant Unicode est
égal à **num**. Pour que cela fonctionne, il faut cependant que deux
conditions soient réalisées :

-   la valeur de **num** doit correspondre effectivement à un caractère
    existant (la répartition des identifiants unicode n'est pas continue
    : certains codes ne correspondent donc à aucun caractère)
-   votre ordinateur doit disposer d'une description graphique du
    caractère, ou en d'autres termes connaître le dessin de ce
    caractère, que l'on appelle *un glyphe*. Les systèmes d'exploitation
    récents disposent cependant de bibliothèques de glyphes très
    étendues, ce qui devrait vous permettre d'en afficher des milliers à
    l'écran.

Ainsi, par exemple, `chr(65)`
renvoie le caractère **A**, et `chr(1046)` renvoie le caractère
cyrillique **Ж**.

Vous pouvez exploiter ces fonctions prédéfinies pour vous amuser à
explorer le jeu de caractères disponible sur votre ordinateur. Vous
pouvez par exemple retrouver les caractères minuscules de l'alphabet
grec, en sachant que les codes qui leur sont attribués vont de 945 à
969. Ainsi le petit script ci-dessous :



```python
s = ""	     # chaîne vide
i = 945 	   # premier code
while i <= 969:        # dernier code
 s += chr(i)
 i = i + 1
print("Alphabet grec (minuscule) : ", s)
```



devrait afficher le résultat suivant :

devrait afficher le résultat suivant :

**Alphabet grec (minuscule)
:**αβγδεζηθικλμνξοπρςστυφχψω

Exercices

.Écrivez un petit script qui affiche une table des codes *ASCII*. Le
programme doit afficher tous les caractères en regard des codes
correspondants. À partir de cette table, établissez la relation
numérique simple reliant chaque caractère majuscule au caractère
minuscule correspondant.

.Modifiez le script précédent pour explorer les codes situés entre 128
et 256, où vous retrouverez nos caractères accentués (parmi de nombreux
autres). La relation numérique trouvée dans l'exercice précédent
reste-t-elle valable aussi pour les caractères accentués du Français ?

.À partir de cette relation, écrivez une fonction qui convertit tous les
caractères minuscules en majuscules, et vice-versa (dans une phrase
fournie en argument).

.Écrivez un script qui recopie un fichier texte en remplaçant tous ses
espaces par le groupe de trois caractères` -*- `. Le fichier à copier sera fourni
encodé à la norme Latin-1, et le fichier destinataire devra être encodé
en Utf-8. Les noms des 2 fichiers devront être demandés en début de
script.

.Écrivez une fonction
**voyelle(car)**, qui renvoie « vrai
» si le caractère fourni en argument est une voyelle.

.Écrivez une fonction
**compteVoyelles(phrase)**, qui
renvoie le nombre de voyelles contenues dans une phrase donnée.

.Explorez la gamme des caractères *Unicode* disponibles sur votre
ordinateur, à l'aide de boucles de programmes similaires à celle que
nous avons nous-même utilisée pour afficher l'alphabet grec. Trouvez
ainsi les codes correspondant à l'alphabet cyrillique, et écrivez un
script qui affiche celui-ci en majuscules et en minuscules.

### 12-A-13 - Les chaînes sont des objets {#article.xml#Ld0e28295 .TitreSection2}

Dans les chapitres précédents, vous avez déjà rencontré de nombreux
*objets*. Vous savez donc que l'on peut agir sur un objet à l'aide de
*méthodes* (c'est-à-dire des fonctions associées à cet objet).\
 Sous Python, les chaînes de caractères sont des objets. On peut donc
effectuer de nombreux traitements sur les chaînes de caractères en
utilisant des méthodes appropriées. En voici quelques-unes, choisies
parmi les plus utiles[^note_65]
:

-   **split()** : convertit une chaîne en une liste de sous-chaînes. On
    peut choisir le caractère séparateur en le fournissant comme
    argument, sinon c'est un espace par défaut :

`>>> c2 ="Votez pour moi"`\
`>>> a = c2.split()`\
`>>> print(a)`\
**['Votez',
'pour',
'moi']**\
**\>\>\> c4 ="Cet exemple, parmi
d'autres, peut encore servir"**\
`>>> c4.split(",")`\
**['Cet
exemple', " parmi d'autres",
'peut encore servir']**

-   **join(liste)** : rassemble une liste de chaînes en une seule (cette
    méthode effectue donc l'action inverse de la précédente). Attention
    : la chaîne à laquelle on applique cette méthode est celle qui
    servira de séparateur (un ou plusieurs caractères) ; l'argument
    transmis est la liste des chaînes à rassembler :

**\>\>\> b =["Bête", "à", "manger", "du",
"foin"]**\
`> >> print(" ".join(b)) `\
`Bête à manger du foin`\
`>>> print("---".join(b))`\
`Bête---à---manger---du---foin `

-   **find(sch)** : cherche la position d'une sous-chaîne **sch** dans
    la chaîne :

**\>\>\> ch1 = "Cette leçon vaut bien un
fromage, sans doute ?"**\
`>>> ch2 = "fromage"`\
`>>> print(ch1.find(ch2))`\
`25 `

-   **count(sch)** : compte le nombre de sous-chaînes **sch** dans la
    chaîne :

**\>\>\> ch1 = "Le héron au long bec
emmanché d'un long cou"**\
**\>\>\> ch2 = 'long'**\
`>>> print(ch1.count(ch2))`\
`2`

-   **lower()** : convertit une chaîne en minuscules :

**\>\>\> ch = "CÉLIMÈNE est un prénom
ancien"**\
`>>> print(ch.lower())`\
`célimène est un prénom ancien `

-   **upper()** : convertit une chaîne en majuscules :

**\>\>\> ch = "Maître Jean-Noël
Hébèrt"**\
`>>> print(ch.upper())`\
`MAÎTRE JEAN-NOËL HÉBÈRT`

-   **title()** : convertit en majuscule l'initiale de chaque mot
    (suivant l'usage des titres anglais) :

**\>\>\> ch ="albert rené élise
véronique"**\
`>>> print(ch.title())`\
`Albert René Élise Véronique`

-   **capitalize()** : variante de la précédente. Convertit en majuscule
    seulement la première lettre de la chaîne :

**\>\>\> b3 = "quel beau temps,
aujourd'hui !"**\
`>>> print(b3.capitalize())`\
**"Quel beau temps, aujourd'hui
!"**

-   **swapcase()** : convertit toutes les majuscules en minuscules, et
    vice-versa :

**\>\>\> ch = "Le Lièvre Et La
Tortue"**\
`>>> print(ch.swapcase())`\
`lE lIÈVRE eT lA tORTUE`

-   **strip()** : enlève les espaces éventuels au début et à la fin de
    la chaîne :

**\>\>\> ch = " Monty Python "**\
`>>> ch.strip()`\
**'Monty Python'**

-   **replace(c1, c2) :** remplace tous les caractères **c1** par des
    caractères **c2** dans la chaîne :

**\>\>\> ch8 = "Si ce n'est toi
c'est donc ton frère"**\
**\>\>\> print(ch8.replace("
","\*"))**\
**Si\*ce\*n'est\*toi\*c'est\*donc\*ton\*frère**

-   **index(car)** : retrouve l'indice (*index*) de la première
    occurrence du caractère **car** dans la chaîne :

**\>\>\> ch9 ="Portez ce vieux whisky au
juge blond qui fume"**\
`>>> print(ch9.index("w"))`\
`16`

Dans la plupart de ces méthodes, il est possible de préciser quelle
portion de la chaîne doit être traitée, en ajoutant des arguments
supplémentaires. Exemples :



```python
>>> print(ch9.index("e"))    # cherche à partir du début de la chaîne
4		  # et trouve le premier 'e'
>>> print(ch9.index("e",5))   # cherche seulement à partir de l'indice 5
8		  # et trouve le second 'e'
>>> print(ch9.index("e",15))  # cherche à partir du caractère n° 15
29		   # et trouve le quatrième 'e'
```



Etc.

Comprenez bien qu'il n'est pas possible de décrire toutes les méthodes
disponibles, ainsi que leur paramétrage, dans le cadre restreint de ce
cours. Si vous souhaitez en savoir davantage, il vous faut consulter la
documentation en ligne de Python (*Library reference*), ou un bon
ouvrage de référence.

### 12-A-14 - Fonctions intégrées {#article.xml#Ld0e28917 .TitreSection2}

À toutes fins utiles, rappelons également ici que l'on peut aussi
appliquer aux chaînes un certain nombre de fonctions intégrées dans le
langage :

-   **len(ch)** renvoie la longueur de la chaîne **ch**, ou en d'autres
    termes, son nombre de caractères.
-   **float(ch)**convertit la chaîne **ch** en un nombre réel (*float*)
    (bien entendu, cela ne pourra fonctionner que si la chaîne
    représente bien un nombre, réel ou entier) :

`>>> a = float("12.36") `*\# Attention : pas de virgule décimale !*\
`>>> print(a + 5)`\
`17.36`

-   **int(ch)** convertit la chaîne **ch** en un nombre entier (avec des
    restrictions similaires) :

`>>> a = int("184")`\
`>>> print(a + 20)`\
`204`

-   **str(obj)** convertit (ou représente) l'objet **obj** en une chaîne
    de caractères. **obj** peut être une donnée d'à peu près n'importe
    quel type :

**\>\>\>\> a, b = 17, ["Émile", 7.65]
**\
**\>\>\> ch =str(a) +" est un entier et
" +str(b) +" est une liste."**\
`>>> print(ch) `\
**17 est un entier et ['Émile', 7.65] est
une liste.**

### 12-A-15 - Formatage des chaînes de caractères {#article.xml#Ld0e29002 .TitreSection2}

Pour terminer ce tour d'horizon des fonctionnalités associées aux
chaînes de caractères, il nous paraît judicieux de vous présenter encore
une technique de traitement très puissante, que l'on appelle *formatage
des chaînes*. Celle-ci se révèle particulièrement utile dans tous les
cas où vous devez construire une chaîne de caractères complexe à partir
d'un certain nombre de morceaux, tels que les valeurs de variables
diverses.

Considérons par exemple que vous ayez écrit un programme qui traite de
la couleur et de la température d'une solution aqueuse, en chimie. La
couleur est mémorisée dans une chaîne de caractères nommée **coul**, et
la température dans une variable de type réel nommée **temp**. Vous
souhaitez à présent que votre programme construise une chaîne de
caractères à partir de ces données, par exemple une phrase telle que la
suivante : « La solution est devenue rouge, et sa température atteint
12,7 °C ».

Vous pouvez construire cette chaîne en assemblant des morceaux à l'aide
de l'opérateur de concaténation (le symbole `+`), mais il vous faudra alors utiliser
aussi la fonction intégrée **str()** pour convertir en chaîne de
caractères la valeur numérique contenue dans la variable de type *float*
(faites l'exercice).

Python vous offre une autre possibilité.

Vous pouvez préparer une chaîne « patron » contenant l'essentiel du
texte invariable, avec des *balises* particulières aux endroits (*les
champs*) où vous souhaitez qu'apparaissent des contenus variables. Vous
appliquerez ensuite à cette chaîne la méthode **format()**, à laquelle
vous fournirez comme arguments les divers objets à convertir en
caractères et à insérer en remplacement des balises. Un exemple vaut
certainement mieux qu'un long discours
:



```python
>>> coul ="verte" 
>>> temp =1.347 + 15.9 
>>> ch ="La couleur est {} et la température vaut {} °C" 
>>> print(ch.format(coul, temp)) 
La couleur est verte et la température vaut 17.247 °C
```



Les balises à utiliser sont constituées
d'accolades, contenant ou non des indications de formatage. La méthode
**format()** doit recevoir autant
d'arguments qu'il y aura de balises dans la chaîne. Si les balises sont
vides, comme dans notre exemple, Python appliquera tout simplement la
fonction **str()** aux arguments
correspondants pour pouvoir les insérer à leur place dans la chaîne. Ces
arguments peuvent être n'importe
quel objet ou expression Python :



```python
>>> pi =3.1416
>>> r =4.7
>>> ch ="L'aire d'un disque de rayon {} est égale à {}."
>>> print(ch.format(r, pi * r**2)) 
L'aire d'un disque de rayon 4.7 est égale à 69.397944. 
```



Voilà pour le principe de base. La technique devient cependant bien plus
intéressante encore si vous insérez des indications de formatage dans
les balises. Par exemple, vous pouvez améliorer la présentation de la
chaîne, dans l'exemple précédent, en limitant la précision du résultat
final, en utilisant la notation scientifique, en fixant le nombre total
de caractères, etc.

Si vous insérez les indications suivantes
dans la dernière balise, par exemple, vous obtiendrez respectivement
:



```python
avec {:8.2f}	   :	 L'aire d'un disque de rayon 4.7 est égale à	69.40. 
avec {:6.2e}   :     L'aire d'un disque de rayon 4.7 est égale à 6.94e+01. 
```



Dans le premier essai, le résultat est formaté de manière à comporter un
total de 8 caractères, dont 2 chiffres après le point décimal. Dans le
second, le résultat est présenté en notation scientifique (e+01 signifie
: « x 10^01^ »). Veuillez constater au passage que les arrondis
éventuels sont effectués correctement.

La description complète de toutes les
possibilités de *formatage*
comporterait plusieurs pages, et cela sort largement du cadre de ces
notes. S'il vous faut un formatage
très particulier, veuillez consulter la documentation en ligne de
Python, ou des manuels plus spécialisés. Signalons simplement encore,
que le formatage permet d'afficher très facilement divers résultats
numériques en notation binaire, octale ou hexadécimale :



```python
>>> n = 789 
>>> txt ="Le nombre {:d} (décimal) vaut {:x} en hexadécimal et {:b} en binaire"
>>> print(txt.format(n,n,n)) 
Le nombre 789 (décimal) vaut 315 en hexadécimal et 1100010101 en binaire 
```



### 12-A-16 - Formatage des chaînes « à l'ancienne » {#article.xml#Ld0e29529 .TitreSection2}

Les versions de Python antérieures à la
version 3.0 utilisaient une technique de formatage légèrement différente
et un peu moins élaborée, qui reste encore utilisable. Il est cependant
fortement conseillé d'adopter plutôt celle que nous avons décrite dans
les paragraphes précédents. Nous expliquons sommairement ici l'ancienne
convention, parce que vous risquez de la rencontrer encore dans les
scripts de nombreux programmeurs. Elle consiste à formater la chaîne en
assemblant deux éléments à l'aide de l'opérateur **%** . À gauche de cet opérateur, la chaîne « patron
» contenant des balises commençant toujours par %, et à droite (entre
parenthèses) le ou les objets que Python devra insérer dans la chaîne,
en lieu et place des balises.\
***Exemple :***



```python
>>> coul ="verte"
>>> temp = 1.347 + 15.9
>>> print("La couleur est %s et la température vaut %s °C" % (coul, temp))
La couleur est verte et la température vaut 17.247 °C
```



La balise `%s` joue le même rôle
que `{}` dans la nouvelle
technique. Elle accepte n'importe quel objet (chaîne, entier, float,
liste...). Vous utiliser aussi d'autres balises plus élaborées, telles
que `%8.2f`, ou `%6.2e`, qui correspondent aux `{:8.2f}` et `{:6.2e}` de la nouvelle technique. C'est
donc équivalent pour les cas les plus simples, mais soyez persuadés que
les possibilités de la nouvelle formulation sont beaucoup plus étendues.

Exercices

.Écrivez un script qui recopie en *Utf-8* un fichier texte encodé à
l'origine en *Latin-1*, en veillant en outre à ce que chaque mot
commence par une majuscule.\
 Le programme demandera les noms des fichiers à l'utilisateur. Les
opérations de lecture et d'écriture des fichiers auront lieu en mode
texte ordinaire.

.Variante de l'exercice précédent : effectuez les opérations de lecture
et d'écriture des fichiers en mode binaire, et les opérations de
décodage/encodage sur les séquences d'octets. Au passage, vous traiterez
les lignes de manière à remplacer tous les espaces par le groupe de 3
caractères « -\*- ».

.Écrivez un script qui compte le nombre de mots contenus dans un fichier
texte.

.Écrivez un script qui recopie un fichier texte en fusionnant (avec la
précédente) les lignes qui ne commencent pas par une majuscule.

.Vous disposez d'un fichier contenant des valeurs numériques. Considérez
que ces valeurs sont les diamètres d'une série de sphères. Écrivez un
script qui utilise les données de ce fichier pour en créer un autre,
organisé en lignes de texte qui exprimeront « en clair » les autres
caractéristiques de ces sphères (surface de section, surface extérieure
et volume), dans des phrases telles que :\
**Diam. 46.20 cm Section 1676.39 cm² Surf. 6705.54 cm² Vol. 51632.67 cm³**\
**Diam. 120.00 cm Section 11309.73 cm²
Surf. 45238.93 cm² Vol. 904778.68 cm³**\
**Diam. 0.03 cm Section 0.00 cm² Surf. 0.00 cm² Vol. 0.00 cm³**\
**Diam. 13.90 cm Section 151.75 cm² Surf. 606.99 cm² Vol. 1406.19 cm³**\
**Diam. 88.80 cm Section 6193.21 cm² Surf. 24772.84 cm² Vol. 366638.04
cm³**\
`etc.`

.Vous avez à votre disposition un fichier texte dont les lignes
représentent des valeurs numériques de type réel, sans exposant (et
encodées sous forme de chaînes de caractères). Écrivez un script qui
recopie ces valeurs dans un autre fichier, en les arrondissant de telle
sorte que leur partie décimale ne comporte plus qu'un seul chiffre après
la virgule, ce chiffre ne pouvant être que 0 ou 5 (l'arrondi doit être
correct).


[^note_58]: Dans les versions de Python antérieures à la version 3.0, les chaînes de caractères de type *string* étaient en fait des séquences d'octets (qui pouvaient représenter des caractères, mais avec un certain nombre de limitations assez gênantes), et il existait un deuxième type de chaîne, le type *unicode* pour traiter les chaînes de caractères au sens où nous l'entendons désormais.

[^note_59]: ASCII = *American Standard Code for Information Interchange*

[^note_60]: En fait, on utilisait déjà les octets à l'époque, mais l'un des bits de l'octet devait être réservé comme bit de contrôle pour les systèmes de rattrapage d'erreur. L'amélioration ultérieure de ces systèmes permit de libérer ce huitième bit pour y stocker de l'information utile : cela autorisa l'extension du jeu ASCII à 256 caractères (normes ISO-8859, etc.).

[^note_61]: Pour cet exemple, nous supposons que la norme d'encodage par défaut sur votre système d'exploitation est Utf-8. Si vous utilisez un système d'exploitation ancien, utilisant par exemple la norme Latin-1 (ou Windows-1252), les résultats seront légèrement différents en ce qui concerne les nombres et valeurs des octets, mais vous ne devriez pas avoir de mal à interpréter ce que vous obtenez.

[^note_62]: Dans les versions de Python antérieures à la version 3.0, les chaînes de caractères devaient toujours être converties en séquences d'octets avant d'être enregistrées. L'ancien type *string* étant par ailleurs équivalent au type bytes actuel, aucune conversion n'était effectuée automatiquement lors des opérations de lecture/écriture de fichiers.

[^note_63]: En informatique, on appelle **codec** (*codeur/décodeur*) tout dispositif de conversion de format. Vous rencontrerez par exemple de nombreux codecs dans le monde du multimedia (codecs audio, vidéo...). Python dispose de nombreux codecs pour convertir les chaînes de caractères suivant les différentes normes en vigueur.

[^note_64]: Dans les versions de Python antérieures à la version 3.0, l'encodage par défaut était ASCII.

[^note_65]: Il s'agit de quelques exemples seulement. La plupart de ces méthodes peuvent être utilisées avec différents paramètres que nous n'indiquons pas tous ici (par exemple, certains paramètres permettent de ne traiter qu'une partie de la chaîne). Vous pouvez obtenir la liste complète de toutes les méthodes associées à un objet à l'aide de la fonction intégrée **dir()**. Veuillez consulter l'un ou l'autre des ouvrages de référence (ou la documentation en ligne de Python) si vous souhaitez en savoir davantage.
