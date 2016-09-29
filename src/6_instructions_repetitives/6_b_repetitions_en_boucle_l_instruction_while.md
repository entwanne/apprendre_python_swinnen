## 6-B - Répétitions en boucle - l'instruction while

L'une des tâches que les machines font le mieux est la répétition sans
erreur de tâches identiques. Il existe bien des méthodes pour programmer
ces tâches répétitives. Nous allons commencer par l'une des plus
fondamentales : la boucle construite à partir de l'instruction
**while**.

Veuillez donc entrer les commandes ci-dessous :



```python
>>> a = 0
>>> while (a < 7):     # (n'oubliez pas le double point !)
...    a = a + 1     # (n'oubliez pas l'indentation !)
...    print(a)
```



Frappez encore une fois \<*Enter*\>.

Que se passe-t-il ?

Avant de lire les commentaires de la page suivante, prenez le temps
d'ouvrir votre cahier et d'y noter cette série de commandes. Décrivez
aussi le résultat obtenu, et essayez de l'expliquer de la manière la
plus détaillée possible.

### 6-B-1 - Commentaires {#article.xml#Ld0e4185 .TitreSection2}

Le mot **while** signifie « tant que » en anglais. Cette instruction
utilisée à la seconde ligne indique à Python qu'il lui faut *répéter
continuellement le bloc d'instructions qui suit, tant que* le contenu de
la variable a reste inférieur à 7.

Comme l'instruction if abordée au chapitre précédent, l'instruction
**while** amorce une *instructioncomposée*. Le double point à la fin de
la ligne introduit le bloc d'instructions à répéter, lequel doit
obligatoirement se trouver en retrait. Comme vous l'avez appris au
chapitre précédent, toutes les instructions d'un même bloc doivent être
indentées exactement au même niveau (c'est-à-dire décalées à droite d'un
même nombre d'espaces).

Nous avons ainsi construit notre première *boucle de programmation*,
laquelle répète un certain nombre de fois le bloc d'instructions
indentées. Voici comment cela fonctionne :

-   Avec l'instruction **while**, Python commence par évaluer la
    validité de la *condition* fournie entre parenthèses (celles-ci sont
    optionnelles, nous ne les avons utilisées que pour clarifier notre
    explication).
-   Si la condition se révèle fausse, alors tout le bloc qui suit est
    ignoré et l'exécution du programme se termine[^note_14].
-   Si la condition est vraie, alors Python exécute tout le bloc
    d'instructions constituant *le corps de la boucle*, c'est-à-dire :
    -   l'instruction **a = a + 1** qui incrémente d'une unité le
        contenu de la variable **a** (ce qui signifie que l'on affecte à
        la variable **a** une nouvelle valeur, qui est égale à la valeur
        précédente augmentée d'une unité).
    -   l'appel de la fonction**print()** pour afficher la valeur
        courante de la variable **a**.
-   lorsque ces deux instructions ont été exécutées, nous avons assisté
    à une première *itération*, et le programme boucle, c'est-à-dire que
    l'exécution reprend à la ligne contenant l'instruction **while**. La
    condition qui s'y trouve est à nouveau évaluée, et ainsi de suite.\
     Dans notre exemple, si la condition **a \< 7** est encore vraie, le
    corps de la boucle est exécuté une nouvelle fois et le bouclage se
    poursuit.

### 6-B-2 - Remarques {#article.xml#Ld0e4264 .TitreSection2}

-   La variable évaluée dans la condition doit exister au préalable (il
    faut qu'on lui ait déjà affecté au moins une valeur).
-   Si la condition est fausse au départ, le corps de la boucle n'est
    jamais exécuté.
-   Si la condition reste toujours vraie, alors le corps de la boucle
    est répété indéfiniment (tout au moins tant que Python lui-même
    continue à fonctionner). Il faut donc veiller à ce que le corps de
    la boucle contienne au moins une instruction qui change la valeur
    d'une variable intervenant dans la condition évaluée par while, de
    manière à ce que cette condition puisse devenir fausse et la boucle
    se terminer.\
     Exemple de boucle sans fin (à éviter !) :



```python
>>> n = 3
>>> while n < 5:
...    print("hello !")
```



### 6-B-3 - Élaboration de tables {#article.xml#Ld0e4321 .TitreSection2}

Recommencez à présent le premier exercice, mais avec la petite
modification ci-dessous :



```python
>>> a = 0
>>> while a < 12:
...    a = a +1
...    print(a , a**2 , a**3)
```



Vous devriez obtenir la liste des carrés et des cubes des nombres de 1 à
12.\
 Notez au passage que la fonction **print()** permet d'afficher
plusieurs expressions l'une à la suite de l'autre sur la même ligne : il
suffit de les séparer par des virgules. Python insère automatiquement un
espace entre les éléments affichés.

### 6-B-4 - Construction d'une suite mathématique {#article.xml#Ld0e4390 .TitreSection2}

Le petit programme ci-dessous permet d'afficher les dix premiers termes
d'une suite appelée « *Suite de Fibonacci* ». Il s'agit d'une suite de
nombres dont chaque terme est égal à la somme des deux termes qui le
précèdent. Analysez ce programme (qui utilise judicieusement
l'affectation parallèle) et décrivez le mieux possible le rôle de
chacune des instructions.



```python
>>> a, b, c = 1, 1, 1
>>> while c < 11 :
...    print(b, end =" ")
...    a, b, c = b, a+b, c+1
```



Lorsque vous lancez l'exécution de ce programme, vous obtenez :



```python
1 2 3 5 8 13 21 34 55 89
```



Les termes de la suite de Fibonacci sont affichés sur la même ligne.
Vous obtenez ce résultat grâce au second argument `end =" " ` fourni à la fonction
**print()**. Par défaut, la fonction **print()** ajoute en effet un
caractère de saut à la ligne à toute valeur qu'on lui demande
d'afficher. L'argument `end =" " `
signifie que vous souhaitez remplacer le saut à la ligne par un simple
espace. Si vous supprimez cet argument, les nombres seront affichés l'un
en-dessous de l'autre.

Dans vos programmes futurs, vous serez très souvent amenés à mettre au
point des boucles de répétition comme celle que nous analysons ici. Il
s'agit d'une question essentielle, que vous devez apprendre à maîtriser
parfaitement. Soyez sûr que vous y arriverez progressivement, à force
d'exercices.

Lorsque vous examinez un problème de cette nature, vous devez considérer
les lignes d'instruction, bien entendu, mais surtout décortiquer *les
états successifs des différentes variables* impliquées dans la boucle.
Cela n'est pas toujours facile, loin de là. Pour vous aider à y voir
plus clair, prenez la peine de dessiner sur papier une table d'états
similaire à celle que nous reproduisons ci-dessous pour notre programme
« suite de Fibonacci » :



  ------------------ ------------------ ------------------ ------------------
  Variables          a                  b                  c

  Valeurs initiales  1                  1                  1

  Valeurs prises     1                  2                  2
  successivement, au                                       
  cours des                                                
  itérations                                               

  2                  3                  3                  

  3                  5                  4                  

  5                  8                  5                  

  …                  …                  …                  

  Expression de      b                  a+b                c+1
  remplacement                                             
  ------------------ ------------------ ------------------ ------------------



Dans une telle table, on effectue en quelque sorte « à la main » le
travail de l'ordinateur, en indiquant ligne par ligne les valeurs que
prendront chacune des variables au fur et à mesure des itérations
successives. On commence par inscrire en haut du tableau les noms des
variables concernées. Sur la ligne suivante, les valeurs initiales de
ces variables (valeurs qu'elles possèdent avant le démarrage de la
boucle). Enfin, tout en bas du tableau, les expressions utilisées dans
la boucle pour modifier l'état de chaque variable à chaque itération.

On remplit alors quelques lignes correspondant aux premières itérations.
Pour établir les valeurs d'une ligne, il suffit d'appliquer à celles de
la ligne précédente, l'expression de remplacement qui se trouve en bas
de chaque colonne. On vérifie ainsi que l'on obtient bien la suite
recherchée. Si ce n'est pas le cas, il faut essayer d'autres expressions
de remplacement.

Exercices

.Écrivez un programme qui affiche les 20 premiers termes de la table de
multiplication par 7.

.Écrivez un programme qui affiche une table
de conversion de sommes d'argent exprimées en euros, en dollars
canadiens. La progression des sommes de la table sera « géométrique »,
comme dans l'exemple ci-dessous :\



```python
1 euro(s) = 1.65 dollar(s)
2 euro(s) = 3.30 dollar(s)
4 euro(s) = 6.60 dollar(s)
8 euro(s) = 13.20 dollar(s)
```



\
 etc. (S'arrêter à 16384 euros.)

.Écrivez un programme qui affiche une suite de 12 nombres dont chaque
terme soit égal au triple du terme précédent.


[^note_14]: ... du moins dans cet exemple. Nous verrons un peu plus loin qu'en fait l'exécution continue avec la première instruction qui suit le bloc indenté, et qui fait partie du même bloc que l'instruction **while** elle-même.
