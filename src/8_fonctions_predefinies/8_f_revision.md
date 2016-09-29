## 8-F - Révision

Dans ce qui suit, nous n'allons pas apprendre de nouveaux concepts mais
simplement utiliser tout ce que nous connaissons déjà, pour réaliser de
vrais petits programmes.

### 8-F-1 - Contrôle du flux - utilisation d'une liste simple {#article.xml#Ld0e9425 .TitreSection2}

Commençons par un petit retour sur les branchements conditionnels (il
s'agit peut-être là du groupe d'instructions le plus important, dans
n'importe quel langage !) :



```python
# Utilisation d'une liste et de branchements conditionnels
 
print("Ce script recherche le plus grand de trois nombres")
print("Veuillez entrer trois nombres séparés par des virgules : ")
ch =input()
# Note : l'association des fonctions eval() et list() permet de convertir
# en liste toute chaîne de valeurs séparées par des virgules :29En fait, la fonction eval() évalue le contenu de la chaîne fournie en argument comme étant une expression Python
 dont elle doit renvoyer le résultat. Par exemple :  eval("7 + 5") renvoie l'entier 12. Si on lui fournit une chaîne de valeurs séparées par des virgules, cela correspond pour
 elle à un tuple. Les tuples sont des séquences apparentées aux listes. Ils seront abordés au chapitre 10 (cf. page 199).
nn = list(eval(ch))
max, index = nn[0], 'premier'
if nn[1] > max: 	    # ne pas omettre le double point !
 max = nn[1]
 index = 'second'
if nn[2] > max:
 max = nn[2]
 index = 'troisième'
print("Le plus grand de ces nombres est", max)
print("Ce nombre est le", index, "de votre liste.")
```



Dans cet exercice, vous retrouvez à nouveau le concept de « bloc
d*'*instructions », déjà abondamment commenté aux chapitres 3 et 4, et
que vous devez absolument assimiler. Pour rappel, les blocs
d*'*instructions sont délimités par *l'indentation*. Après la première
instruction **if**, par exemple, il y a deux lignes indentées
définissant un bloc d*'*instructions. Ces instructions ne seront
exécutées que si la condition **nn[1] \>
max **est vraie.

La ligne suivante, par contre (celle qui contient la deuxième
instruction **if** ) n'est pas indentée. Cette ligne se situe donc au
même niveau que celles qui définissent le corps principal du programme.
L'instruction contenue dans cette ligne est donc toujours exécutée,
alors que les deux suivantes (qui constituent encore un autre bloc) ne
sont exécutées que si la condition **
nn[2] \> max ** est vraie.

En suivant la même logique, on voit que les instructions des deux
dernières lignes font partie du bloc principal et sont donc toujours
exécutées.

### 8-F-2 - Boucle while - instructions imbriquées {#article.xml#Ld0e10236 .TitreSection2}

Continuons dans cette voie en imbriquant d'autres structures :



1.  ``` {.LignePreCode}
    # Instructions composées  -  -  -  
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    print('Choisissez un nombre de 1 à 3 (ou 0 pour terminer) ', end=' ') 
    ```

4.  ``` {.LignePreCode}
    ch = input() 
    ```

5.  ``` {.LignePreCode}
    a = int(ch)	   # conversion de la chaîne entrée en entier 
    ```

6.  ``` {.LignePreCode}
    while a:	# équivalent à : < while a != 0: > 
    ```

7.  ``` {.LignePreCode}
      if a == 1: 
    ```

8.  ``` {.LignePreCode}
          print("Vous avez choisi un :") 
    ```

9.  ``` {.LignePreCode}
          print("le premier, l'unique, l'unité ..." 
    ```

10. ``` {.LignePreCode}
      elif a == 2: 
    ```

11. ``` {.LignePreCode}
          print("Vous préférez le deux :") 
    ```

12. ``` {.LignePreCode}
          print("la paire, le couple, le duo ...") 
    ```

13. ``` {.LignePreCode}
      elif a == 3: 
    ```

14. ``` {.LignePreCode}
          print("Vous optez pour le plus grand des trois :") 
    ```

15. ``` {.LignePreCode}
          print("le trio, la trinité, le triplet ...") 
    ```

16. ``` {.LignePreCode}
      else : 
    ```

17. ``` {.LignePreCode}
          print("Un nombre entre UN et TROIS, s.v.p.") 
    ```

18. ``` {.LignePreCode}
      print('Choisissez un nombre de 1 à 3 (ou 0 pour terminer) ', end =' ') 
    ```

19. ``` {.LignePreCode}
      a = int(input()) 
    ```

20. ``` {.LignePreCode}
    print("Vous avez entré zéro :") 
    ```

21. ``` {.LignePreCode}
    print("L'exercice est donc terminé.") 
    ```



Nous retrouvons ici une boucle **while**, associée à un groupe
d'instructions **if**, **elif** et **else**. Notez bien cette fois
encore comment la structure logique du programme est créée à l'aide des
indentations (... et n'oubliez pas le caractère « : » à la fin de chaque
ligne d'en-tête !).

À la ligne 6, l'instruction **while** est utilisée de la manière
expliquée à la page : pour la comprendre, il suffit de vous rappeler que
toute valeur numérique autre que zéro est considérée comme « vraie » par
l'interpréteur Python. Vous pouvez remplacer cette forme d'écriture par
: «` while a != 0 `: » si vous
préférez (rappelons à ce sujet que l'opérateur de comparaison `!=` signifie « est différent de »), mais
c'est moins efficace.

Cette « boucle while » relance le questionnement après chaque réponse de
l'utilisateur (du moins jusqu'à ce que celui-ci décide de « quitter » en
entrant une valeur nulle : ).

Dans le corps de la boucle, nous trouvons le groupe d'instructions
**if**, **elif** et **else** (de la ligne 7 à la ligne 17), qui aiguille
le flux du programme vers les différentes réponses, ensuite une
instruction **print()** et une instruction **input()** (lignes 18 & 19)
qui seront exécutées dans tous les cas de figure : notez bien leur
niveau d'indentation, qui est le même que celui du bloc **if**, **elif**
et **else**. Après ces instructions, le programme boucle et l'exécution
reprend à l'instruction **while** (ligne 6).

À la ligne 19, nous utilisons la composition pour écrire un code plus
compact, qui est équivalent aux lignes 4 & 5 rassemblées en une seule.

Les deux dernières instructions **print()** (lignes 20 & 21) ne sont
exécutées qu'à la sortie de la boucle.

Exercices

.Que fait le programme ci-dessous, dans les quatre cas où l'on aurait
défini au préalable que la variable **a** vaut 1, 2, 3 ou 15 ?

`if a !=2:`\
**print('perdu')**\
`elif a ==3:`\
**print('un instant,
s.v.p.')**\
`else :`\
**print('gagné')**

.Que font ces programmes ?\
**a) a
= 5**\
`b = 2`\
`if (a==5) & (b<2):`\
**print('"&" signifie
"et"; on peut aussi utiliser\\**\
**le mot "and"')**\
**b) a,
b = 2, 4**\
`if (a==4) or (b!=4):`\
**print('gagné')**\
`elif (a==4) or (b==4):`\
**print('presque
gagné')**\
**c) a
= 1**\
`if not a:`\
**print('gagné')**\
`elif a:`\
**print('perdu')**

.Reprendre le programme c) avec a = 0 au lieu de a = 1.\
 Que se passe-t-il ? Conclure !

.Écrire un programme qui, étant données deux bornes entières a et b,
additionne les nombres multiples de 3 et de 5 compris entre ces bornes.
Prendre par exemple a = 0, b = 32 ; le résultat devrait être alors 0 +
15 + 30 = 45.\
 Modifier légèrement ce programme pour qu'il additionne les nombres
multiples de 3 ou de 5 compris entre les bornes a et b. Avec les bornes
0 et 32, le résultat devrait donc être : 0 + 3 + 5 + 6 + 9 + 10 + 12 +
15 + 18 + 20 + 21 + 24 + 25 + 27 + 30 = 225.

.Déterminer si une année (dont le millésime est introduit par
l'utilisateur) est bissextile ou non. Une année A est bissextile si A
est divisible par 4. Elle ne l'est cependant pas si A est un multiple de
100, à moins que A ne soit multiple de 400.

.Demander à l'utilisateur son nom et son sexe (M ou F). En fonction de
ces données, afficher « Cher Monsieur » ou « Chère Mademoiselle » suivi
du nom de la personne.

.Demander à l'utilisateur d'entrer trois longueurs a, b, c. À l'aide de
ces trois longueurs, déterminer s'il est possible de construire un
triangle. Déterminer ensuite si ce triangle est rectangle, isocèle,
équilatéral ou quelconque. Attention : un triangle rectangle peut être
isocèle.

.Demander à l'utilisateur qu'il entre un nombre. Afficher ensuite : soit
la racine carrée de ce nombre, soit un message indiquant que la racine
carrée de ce nombre ne peut être calculée.

.Convertir une note scolaire N quelconque, entrée par l'utilisateur sous
forme de points (par exemple 27 sur 85), en une note standardisée
suivant le code ci-dessous :\
**Note Appréciation**\
**N \>= 80 % A**\
**80 % \> N \>= 60 % B**\
**60 % \> N \>= 50 % C**\
**50 % \> N \>= 40 % D**\
**N \< 40 % E**

.Soit la liste suivante :\
**['Jean-Michel',
'Marc',
'Vanessa',
'Anne',
'Maximilien',**\
**'Alexandre-Benoît',
'Louise']**\
 Écrivez un script qui affiche chacun de ces noms avec le nombre de
caractères correspondant.

.Écrire une boucle de programme qui demande à l'utilisateur d'entrer des
notes d'élèves. La boucle se terminera seulement si l'utilisateur entre
une valeur négative. Avec les notes ainsi entrées, construire
progressivement une liste. Après chaque entrée d'une nouvelle note (et
donc à chaque itération de la boucle), afficher le nombre de notes
entrées, la note la plus élevée, la note la plus basse, la moyenne de
toutes les notes.

.Écrivez un script qui affiche la valeur de la force de gravitation
s'exerçant entre deux masses de 10 000 kg , pour des distances qui
augmentent suivant une progression géométrique de raison 2, à partir de
5 cm (0,05 mètre).

La force de gravitation est régie par la formule
![](images/formule04.png)

Exemple d'affichage :

**d = .05 m : la force vaut 2.668 N**\
**d = .1 m : la force
vaut 0.667 N**\
**d = .2 m : la force
vaut 0.167 N**\
**d = .4 m : la force
vaut 0.0417 N**

etc.

