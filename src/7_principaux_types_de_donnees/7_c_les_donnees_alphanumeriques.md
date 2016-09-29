## 7-C - Les données alphanumériques

Jusqu'à présent nous n'avons manipulé que des nombres. Mais un programme
d'ordinateur peut également traiter des caractères alphabétiques, des
mots, des phrases, ou des suites de symboles quelconques. Dans la
plupart des langages de programmation, il existe pour cet usage des
structures de données particulières que l'on appelle « chaînes de
caractères ».

> Nous apprendrons plus loin (au chapitre 10) qu'il ne faut pas
> confondre les notions de « chaîne de caractères » et « séquence
> d'octets » comme le faisaient abusivement les langages e programmation
> anciens (dont les premières versions de Python). Pour l'instant,
> contentons-nous de nous réjouir que Python traite désormais de manière
> parfaitement cohérente toutes les chaînes de caractères, ceux-ci
> pouvant faire partie d'alphabets quelconques[^note_21].

### 7-C-1 - Le type string {#article.xml#Ld0e5793 .TitreSection2}

Une donnée de type *string* peut se définir en première approximation
comme une suite quelconque de caractères. Dans un script python, on peut
délimiter une telle suite de caractères, soit par des apostrophes
(simple quotes), soit par des guillemets (double quotes). Exemples :



```python
>>> phrase1 = 'les oeufs durs.'
>>> phrase2 = '"Oui", répondit-il,'
>>> phrase3 = "j'aime bien"
>>> print(phrase2, phrase3, phrase1)
"Oui", répondit-il, j'aime bien les oeufs durs.
```



Les 3 variables **phrase1**, **phrase2**, **phrase3** sont donc des
variables de type *string*.

Remarquez l'utilisation des guillemets pour délimiter une chaîne dans
laquelle il y a des apostrophes, ou l'utilisation des apostrophes pour
délimiter une chaîne qui contient des guillemets. Remarquez aussi encore
une fois que la fonction **print()** insère un espace entre les éléments
affichés.

Le caractère spécial « \\ » (*antislash*) permet quelques subtilités
complémentaires :

-   En premier lieu, il permet d'écrire sur plusieurs lignes une
    commande qui serait trop longue pour tenir sur une seule (cela vaut
    pour n'importe quel type de commande).
-   À l'intérieur d'une chaîne de caractères, l'*antislash* permet
    d'insérer un certain nombre de codes spéciaux (sauts à la ligne,
    apostrophes, guillemets, etc.). Exemples :



```python
>>> txt3 = '"N\'est-ce pas ?" répondit-elle.'
>>> print(txt3)
"N'est-ce pas ?" répondit-elle.
>>> Salut = "Ceci est une chaîne plutôt longue\n contenant plusieurs lignes \
... de texte (Ceci fonctionne\n de la même façon en C/C++.\n\
...    Notez que les blancs en début\n de ligne sont significatifs.\n"
>>> print(Salut)
Ceci est une chaîne plutôt longue
 contenant plusieurs lignes de texte (Ceci fonctionne
 de la même façon en C/C++.
 Notez que les blancs en début
 de ligne sont significatifs.
```



#### 7-C-1-A - Remarques {#article.xml#Ld0e6251 .TitreSection3}

-   La séquence `\n` dans une
    chaîne provoque un saut à la ligne.
-   La séquence **\\'** permet d'insérer une apostrophe
    dans une chaîne délimitée par des apostrophes. De la même manière,
    la séquence `\"` permet
    d'insérer des guillemets dans une chaîne délimitée elle-même par des
    guillemets.
-   Rappelons encore ici que la casse est significative dans les noms de
    variables (il faut respecter scrupuleusement le choix initial de
    majuscules ou minuscules).

#### 7-C-1-B - Triple quotes {#article.xml#Ld0e6275 .TitreSection3}

Pour insérer plus aisément des caractères spéciaux ou « exotiques » dans
une chaîne, sans faire usage de l'*antislash*, ou pour faire accepter
l'*antislash* lui-même dans la chaîne, on peut encore délimiter la
chaîne à l'aide de *triplesguillemets* ou de *triplesapostrophes* :



```python
>>> a1 = """
... Usage: trucmuche[OPTIONS]
... { -h
...   -H hôte
... }"""
 
>>> print(a1)
 
Usage: trucmuche[OPTIONS]
{ -h
 -H hôte
}
```



### 7-C-2 - Accès aux caractères individuels d'une chaîne {#article.xml#Ld0e6378 .TitreSection2}

Les chaînes de caractères constituent un cas particulier d'un type de
données plus général que l'on appelle des *données composites*. Une
donnée composite est une entité qui rassemble dans une seule structure
un ensemble d'entités plus simples : dans le cas d'une chaîne de
caractères, par exemple, ces entités plus simples sont évidemment les
caractères eux-mêmes. En fonction des circonstances, nous souhaiterons
traiter la chaîne de caractères, tantôt comme un seul objet, tantôt
comme une collection de caractères distincts. Un langage de
programmation tel que Python doit donc être pourvu de mécanismes qui
permettent d'accéder séparément à chacun des caractères d'une chaîne.
Comme vous allez le voir, cela n'est pas bien compliqué.

Python considère qu'une chaîne de caractères est un objet de la
catégorie des *séquences*, lesquelles sont des *collections ordonnées
d'éléments*. Cela signifie simplement que les caractères d'une chaîne
sont toujours disposés dans un certain ordre. Par conséquent, chaque
caractère de la chaîne peut être désigné par sa place dans la séquence,
à l'aide d'un *index*.

Pour accéder à un caractère bien déterminé, on utilise le nom de la
variable qui contient la chaîne et on lui accole, entre deux crochets,
l'index numérique qui correspond à la position du caractère dans la
chaîne.

*Attention cependant :* comme vous aurez l'occasion de le vérifier par
ailleurs, les données informatiques sont presque toujours numérotées *à
partir de zéro* (et non à partir de un). C'est le cas pour les
caractères d'une chaîne.

***Exemple*** :



```python
>>> ch = "Christine"
>>> print(ch[0], ch[3], ch[5])
C i t
```



Vous pouvez recommencer l'exercice de l'exemple ci-dessus en utilisant
cette fois un ou deux caractères « non-ASCII », tels que lettres
accentuées, cédilles, etc. Contrairement à ce qui pouvait se passer dans
certains cas avec les versions de Python antérieures à la version 3.0,
vous obtenez sans surprise les résultats attendus :



```python
>>> ch ="Noël en Décembre"
>>> print(ch[1],ch[2],ch[3],ch[4],ch[8],ch[9],ch[10],ch[11],ch[12])
o ë l	 D é c e m
```



Ne vous préoccupez pas pour l'instant de savoir de quelle manière exacte
Python mémorise et traite les caractères typographiques dans la mémoire
de l'ordinateur. Sachez cependant que la technique utilisée exploite la
norme internationale **unicode**. qui permet de distinguer de façon
univoque n'importe quel caractère de n'importe quel alphabet. Vous
pourrez donc mélanger dans une même chaîne des caractères latins, grecs,
cyrilliques, arabes, ... (y compris les caractères accentués), ainsi que
des symboles mathématiques, des pictogrammes, etc. Nous verrons au
chapitre 10 comment faire apparaître d'autres caractères que ceux qui
sont directement accessibles au clavier.

### 7-C-3 - Opérations élémentaires sur les chaînes {#article.xml#Ld0e6521 .TitreSection2}

Python intègre de nombreuses *fonctions* qui permettent d'effectuer
divers traitements sur les chaînes de caractères (conversions
majuscules/minuscules, découpage en chaînes plus petites, recherche de
mots, etc.). Une fois de plus, cependant, nous devons vous demander de
patienter : ces questions ne seront développées qu'à partir du chapitre
10.

Pour l'instant, nous pouvons nous contenter de savoir qu'il est possible
d'accéder individuellement à chacun des caractères d'une chaîne, comme
cela a été expliqué dans la section précédente. Sachons en outre que
l'on peut aussi :

-   assembler plusieurs petites chaînes pour en construire de plus
    grandes. Cette opération s'appelle *concaténation* et on la réalise
    sous Python à l'aide de l'opérateur **+** (cet opérateur réalise
    donc l'opération d'addition lorsqu'on l'applique à des nombres, et
    l'opération de concaténation lorsqu'on l'applique à des chaînes de
    caractères). Exemple :

**a = 'Petit
poisson'**\
**b = 'deviendra
grand'**\
`c = a + b`\
`print(c)`\
`petit poisson deviendra grand`

-   déterminer la longueur (c'est-à-dire le nombre de caractères) d'une
    chaîne, en faisant appel à la fonction intégrée **len()** :

**\>\>\> ch ='Georges'**\
`>>> print(len(ch))`\
`7`

Cela marche tout aussi bien si la chaîne contient des caractères
accentués :

**\>\>\> ch ='René'**\
`>>> print(len(ch))`\
`4`

-   Convertir en nombre véritable une chaîne de caractères qui
    représente un nombre. Exemple :

**\>\>\> ch = '8647'**\
`>>> print(ch + 45)`\
 → \*\*\* erreur \*\*\* : on ne peut pas additionner une chaîne et un
nombre\
`>>> n = int(ch) `\
`>>> print(n + 65)`\
`8712 `*\# OK : on peut additionner 2 nombres *

Dans cet exemple, la fonction intégrée **int()** convertit la chaîne en
nombre entier. Il serait également possible de convertir une chaîne de
caractères en nombre réel, à l'aide de la fonction intégrée **float()**.

Exercices

.Écrivez un script qui détermine si une chaîne contient ou non le
caractère « e ».

.Écrivez un script qui compte le nombre d'occurrences du caractère « e »
dans une chaîne.

.Écrivez un script qui recopie une chaîne
(dans une nouvelle variable), en insérant des astérisques entre les
caractères.\
Ainsi par exemple, « `gaston` » devra devenir « `g*a*s*t*o*n` »

.Écrivez un script qui recopie une
chaîne (dans une nouvelle variable) en l'inversant.\
 Ainsi par exemple, « `zorglub` »
deviendra « `bulgroz` ».

.En partant de l'exercice précédent,
écrivez un script qui détermine si une chaîne de caractères donnée est
un *palindrome*(c'est-à-dire une
chaîne qui peut se lire indifféremment dans les deux sens), comme par
exemple « radar » ou « s.o.s ».


[^note_21]: Ceci constitue donc l'une des grandes nouveautés de la version 3 de Python par rapport aux versions précédentes. Dans celles-ci, une donnée de type *string* était en réalité une *séquence d'octets* et non une *séquence de caractères*. Cela ne posait guère de problèmes pour traiter des textes contenant seulement les caractères principaux des langues d'Europe occidentale, car il était possible d'encoder chacun de ces caractères sur un seul octet (en suivant par exemple la norme Latin-1). Cela entraînait cependant de grosses difficultés si l'on voulait rassembler dans un même texte des caractères tirés d'alphabets différents, ou simplement utiliser des alphabets comportant plus de 256 caractères, des symboles mathématiques particuliers, etc. (Vous trouverez davantage d'informations à ce sujet au chapitre 10).
