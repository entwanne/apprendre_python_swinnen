## 9-A - Définir une fonction

Les scripts que vous avez écrits jusqu'à présent étaient à chaque fois
très courts, car leur objectif était seulement de vous faire assimiler
les premiers éléments du langage. Lorsque vous commencerez à développer
de véritables projets, vous serez confrontés à des problèmes souvent
fort complexes, et les lignes de programme vont commencer à
s'accumuler...

L'approche efficace d'un problème complexe consiste souvent à le
décomposer en plusieurs sous-problèmes plus simples qui seront étudiés
séparément (ces sous-problèmes peuvent éventuellement être eux-mêmes
décomposés à leur tour, et ainsi de suite). Or il est important que
cette décomposition soit représentée fidèlement dans les
algorithmes[^note_29]
pour que ceux-ci restent clairs.

D'autre part, il arrivera souvent qu'une même séquence d'instructions
doive être utilisée à plusieurs reprises dans un programme, et on
souhaitera bien évidemment ne pas avoir à la reproduire
systématiquement.

Les *fonctions*[^note_30]
et les *classesd'objets* sont différentes structures de sous-programmes
qui ont été imaginées par les concepteurs des langages de haut niveau
afin de résoudre les difficultés évoquées ci-dessus. Nous allons
commencer par décrire ici la *définitiondefonctions* sous Python. Les
*objets* et les *classes* seront examinés plus loin.

Nous avons déjà rencontré diverses fonctions pré-programmées. Voyons à
présent comment en définir nous-mêmes de nouvelles.

La syntaxe Python pour la définition d'une fonction est la suivante :



```python
def nomDeLaFonction(liste de paramètres):
 ... 
 bloc d'instructions
 ...
```



-   Vous pouvez choisir n'importe quel nom pour la fonction que vous
    créez, à l'exception des mots réservés du langage[^note_31],
    et à la condition de n'utiliser aucun caractère spécial ou accentué
    (le caractère souligné « \_ » est permis). Comme c'est le cas pour
    les noms de variables, il vous est conseillé d'utiliser surtout des
    lettres minuscules, notamment au début du nom (les noms commençant
    par une majuscule seront réservés aux *classes* que nous étudierons
    plus loin).
-   Comme les instructions **if** et **while** que vous connaissez déjà,
    l'instruction **def** est une *instructioncomposée*. La ligne
    contenant cette instruction se termine obligatoirement par un double
    point, lequel introduit un bloc d'instructions que vous ne devez pas
    oublier *d'indenter*.
-   La *listedeparamètres* spécifie quelles informations il faudra
    fournir en guise *d'arguments* lorsque l'on voudra utiliser cette
    fonction (les parenthèses peuvent parfaitement rester vides si la
    fonction ne nécessite pas d'arguments).
-   Une fonction s'utilise pratiquement comme une instruction
    quelconque. Dans le corps d'un programme, un *appel de fonction* est
    constitué du nom de la fonction suivi de parenthèses.\
     Si c'est nécessaire, on place dans ces parenthèses le ou les
    arguments que l'on souhaite transmettre à la fonction. Il faudra en
    principe fournir un argument pour chacun des paramètres spécifiés
    dans la définition de la fonction, encore qu'il soit possible de
    définir pour ces paramètres des valeurs par défaut (voir plus loin).

### 9-A-1 - Fonction simple sans paramètres {#article.xml#Ld0e11426 .TitreSection2}

Pour notre première approche concrète des fonctions, nous allons
travailler à nouveau en mode interactif. Le mode interactif de Python
est en effet idéal pour effectuer des petits tests comme ceux qui
suivent. C'est une facilité que n'offrent pas tous les langages de
programmation !



```python
>>> def table7():
...    n = 1
...    while n <11 :
...	  print(n * 7, end =' ')
...	  n = n +1
...
```



En entrant ces quelques lignes, nous avons défini une fonction très
simple qui calcule et affiche les 10 premiers termes de la table de
multiplication par 7. Notez bien les parenthèses[^note_32],
le double point, et l'indentation du bloc d'instructions qui suit la
ligne d'en-tête (c'est ce bloc d'instructions qui constitue le corps de
la fonction proprement dite).

Pour utiliser la fonction que nous venons de définir, il suffit de
l'appeler par son nom. Ainsi :



```python
>>> table7()
```



provoque l'affichage de :



```python
7 14 21 28 35 42 49 56 63 70
```



Nous pouvons maintenant réutiliser cette fonction à plusieurs reprises,
autant de fois que nous le souhaitons. Nous pouvons également
l'incorporer dans la définition d'une autre fonction, comme dans
l'exemple ci-dessous :



```python
>>> def table7triple():
...    print('La table par 7 en triple exemplaire :')
...    table7()
...    table7()
...    table7()
...
```



Utilisons cette nouvelle fonction, en entrant la commande :



```python
>>> table7triple()
```



l'affichage résultant devrait être :



```python
La table par 7 en triple exemplaire :
7 14 21 28 35 42 49 56 63 70
7 14 21 28 35 42 49 56 63 70
7 14 21 28 35 42 49 56 63 70
```



Une première fonction peut donc appeler une deuxième fonction, qui
elle-même en appelle une troisième, etc. Au stade où nous sommes, vous
ne voyez peut-être pas encore très bien l'utilité de tout cela, mais
vous pouvez déjà noter deux propriétés intéressantes :

-   Créer une nouvelle fonction vous offre l'opportunité de donner un
    nom à tout un ensemble d'instructions. De cette manière, vous pouvez
    simplifier le corps principal d'un programme, en dissimulant un
    algorithme secondaire complexe sous une commande unique, à laquelle
    vous pouvez donner un nom très explicite, en français si vous
    voulez.
-   Créer une nouvelle fonction peut servir à raccourcir un programme,
    par élimination des portions de code qui se répètent. Par exemple,
    si vous devez afficher la table par 7 plusieurs fois dans un même
    programme, vous n'avez pas à réécrire chaque fois l'algorithme qui
    accomplit ce travail.

Une fonction est donc en quelque sorte une nouvelle instruction
personnalisée, que vous ajoutez vous-même librement à votre langage de
programmation.

### 9-A-2 - Fonction avec paramètre {#article.xml#Ld0e11613 .TitreSection2}

Dans nos derniers exemples, nous avons défini et utilisé une fonction
qui affiche les termes de la table de multiplication par 7. Supposons à
présent que nous voulions faire de même avec la table par 9. Nous
pouvons bien entendu réécrire entièrement une nouvelle fonction pour
cela. Mais si nous nous intéressons plus tard à la table par 13, il nous
faudra encore recommencer. Ne serait-il donc pas plus intéressant de
définir une fonction qui soit capable d'afficher n'importe quelle table,
à la demande ?

Lorsque nous appellerons cette fonction, nous devrons bien évidemment
pouvoir lui indiquer quelle table nous souhaitons afficher. Cette
information que nous voulons transmettre à la fonction au moment même où
nous l'appelons s'appelle un ***argument***. Nous avons déjà rencontré à
plusieurs reprises des fonctions intégrées qui utilisent des arguments.
La fonction **sin(a)**, par exemple, calcule le sinus de l'angle **a**.
La fonction **sin()** utilise donc la valeur numérique de **a** comme
argument pour effectuer son travail.

Dans la définition d'une telle fonction, il faut prévoir une variable
particulière pour recevoir l'argument transmis. Cette variable
particulière s'appelle un ***paramètre***. On lui choisit un nom en
respectant les mêmes règles de syntaxe que d'habitude (pas de lettres
accentuées, etc.), et on place ce nom entre les parenthèses qui
accompagnent la définition de la fonction.

Voici ce que cela donne dans le cas qui nous intéresse :



```python
>>> def table(base):
...    n = 1
...    while n <11 :
...	print(n * base, end =' ')
...	n = n +1
```



La fonction **table()** telle que définie ci-dessus utilise le paramètre
**base** pour calculer les dix premiers termes de la table de
multiplication correspondante.

Pour tester cette nouvelle fonction, il nous suffit de l'appeler avec un
argument. Exemples :



```python
>>> table(13)
13 26 39 52 65 78 91 104 117 130
 
>>> table(9)
9 18 27 36 45 54 63 72 81 90
```



Dans ces exemples, la valeur que nous indiquons entre parenthèses lors
de l'appel de la fonction (et qui est donc un argument) est
automatiquement affectée au paramètre **base**. Dans le corps de la
fonction, **base** joue le même rôle que n'importe quelle autre
variable. Lorsque nous entrons la commande `table(9)`, nous signifions à la machine
que nous voulons exécuter la fonction **table()** en affectant la valeur
**9** à la variable **base**.

### 9-A-3 - Utilisation d'une variable comme argument {#article.xml#Ld0e11817 .TitreSection2}

Dans les 2 exemples qui précèdent, l'argument que nous avons utilisé en
appelant la fonction **table()** était à chaque fois une constante (la
valeur 13, puis la valeur 9). Cela n'est nullement obligatoire.
*L'argument que nous utilisons dans l'appel d'une fonction peut être une
variable* lui aussi, comme dans l'exemple ci-dessous. Analysez bien cet
exemple, essayez-le concrètement, et décrivez le mieux possible dans
votre cahier d'exercices ce que vous obtenez, en expliquant avec vos
propres mots ce qui se passe. Cet exemple devrait vous donner un premier
aperçu de l'utilité des fonctions pour accomplir simplement des tâches
complexes :



```python
>>> a = 1
>>> while a <20:
...    table(a)
...    a = a +1
...
```



#### 9-A-3-A - Remarque importante {#article.xml#Ld0e11870 .TitreSection3}

Dans l'exemple ci-dessus, l'argument que nous passons à la fonction
**table()** est le contenu de la variable **a**. À l'intérieur de la
fonction, cet argument est affecté au paramètre **base**, qui est une
tout autre variable. Notez donc bien dès à présent que :

> Le nom d*'*une variable que nous passons comme argument n*'*a rien à
> voir avec le nom du paramètre correspondant dans la fonction.

Ces noms peuvent être identiques si vous le voulez, mais vous devez bien
comprendre qu'ils ne désignent pas la même chose (en dépit du fait
qu'ils puissent éventuellement contenir une valeur identique).

Exercice

.Importez le module***turtle*** pour pouvoir effectuer des dessins
simples.

Vous allez dessiner une série de triangles équilatéraux de différentes
couleurs.\
 Pour ce faire, définissez d'abord une fonction **triangle()** capable
de dessiner un triangle d'une couleur bien déterminée (ce qui signifie
donc que la définition de votre fonction doit comporter un paramètre
pour recevoir le nom de cette couleur).

Utilisez ensuite cette fonction pour reproduire ce même triangle en
différents endroits, en changeant de couleur à chaque fois.

### 9-A-4 - Fonction avec plusieurs paramètres {#article.xml#Ld0e11911 .TitreSection2}

La fonction **table()** est certainement intéressante, mais elle
n'affiche toujours que les dix premiers termes de la table de
multiplication, alors que nous pourrions souhaiter qu'elle en affiche
d'autres. Qu'à cela ne tienne. Nous allons l'améliorer en lui ajoutant
des paramètres supplémentaires, dans une nouvelle version que nous
appellerons cette fois **tableMulti()** :



```python
>>> def tableMulti(base, debut, fin):
...    print('Fragment de la table de multiplication par', base, ':')
...    n = debut
...    while n <= fin :
...	print(n, 'x', base, '=', n * base)
...	n = n +1
```



Cette nouvelle fonction utilise donc trois paramètres : la base de la
table comme dans l'exemple précédent, l'indice du premier terme à
afficher, l'indice du dernier terme à afficher.

Essayons cette fonction en entrant par exemple :



```python
>>> tableMulti(8, 13, 17)
```



ce qui devrait provoquer l'affichage de :



```python
Fragment de la table de multiplication par 8 :
13 x 8 = 104
14 x 8 = 112
15 x 8 = 120
16 x 8 = 128
17 x 8 = 136
```



#### 9-A-4-A - Notes {#article.xml#Ld0e12109 .TitreSection3}

-   Pour définir une fonction avec plusieurs paramètres, il suffit
    d'inclure ceux-ci entre les parenthèses qui suivent le nom de la
    fonction, en les séparant à l'aide de virgules.
-   Lors de l'appel de la fonction, les arguments utilisés doivent être
    fournis *dans le même ordre* que celui des paramètres correspondants
    (en les séparant eux aussi à l'aide de virgules). Le premier
    argument sera affecté au premier paramètre, le second argument sera
    affecté au second paramètre, et ainsi de suite.
-   À titre d'exercice, essayez la séquence d'instructions suivantes et
    décrivez dans votre cahier d'exercices le résultat obtenu :\



```python
>>> t, d, f = 11, 5, 10 
>>> while t<21:
...    tableMulti(t,d,f)
...    t, d, f = t +1, d +3, f +5 
...
```




[^note_29]: On appelle algorithme la séquence détaillée de toutes les opérations à effectuer pour résoudre un problème.

[^note_30]: Il existe aussi dans d'autres langages des **routines** (parfois appelés sous-programmes) et des **procédures**. Il n'existe pas de **routines** en Python. Quant au terme de **fonction**, il désigne à la fois les fonctions au sens strict (qui fournissent une valeur en retour), et les procédures (qui n'en fournissent pas).

[^note_31]: La liste complète des mots réservés Python se trouve page .

[^note_32]: Un nom de fonction doit toujours être accompagné de parenthèses, même si la fonction n'utilise aucun paramètre. Il en résulte une convention d'écriture qui stipule que dans un texte quelconque traitant de programmation d'ordinateur, un nom de fonction soit toujours accompagné d'une paire de parenthèses vides. Nous respecterons cette convention dans la suite de ce texte.
