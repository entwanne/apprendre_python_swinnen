## 10-B - Premiers pas avec tkinter

Pour la suite des explications, nous supposerons bien évidemment que le
module *tkinter*[^note_36]
a déjà été installé sur votre système. Pour pouvoir en utiliser les
fonctionnalités dans un script Python, il faut que l'une des premières
lignes de ce script contienne l'instruction d'importation :



```python
from tkinter import *
```



Comme toujours sous Python, il n'est même pas nécessaire d'écrire un
script. Vous pouvez faire un grand nombre d'expériences directement à la
ligne de commande, en ayant simplement lancé Python en mode interactif.

Dans l'exemple qui suit, nous allons créer une fenêtre très simple, et y
ajouter deux *widgets*[^note_37]
typiques : un bout de texte (ou *label*) et un bouton (ou *button*).



```python
>>> from tkinter import *
>>> fen1 = Tk()
>>> tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
>>> tex1.pack()
>>> bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
>>> bou1.pack()
>>> fen1.mainloop()
```





![](images/image14.png)



> Suivant la version de Python utilisée, vous verrez déjà apparaître la
> fenêtre d*'*application immédiatement après avoir entré la deuxième
> commande de cet exemple, ou bien seulement après la septième[^note_38].

### 10-B-1 - Examinons à présent plus en détail chacune des lignes de commandes exécutées {#article.xml#Ld0e15219 .TitreSection2}

1.  Comme cela a déjà été expliqué précédemment, il est aisé de
    construire différents modules Python, qui contiendront des scripts,
    des définitions de fonctions, des classes d'objets, etc. On peut
    alors importer tout ou partie de ces modules dans n'importe quel
    programme, ou même dans l'interpréteur fonctionnant en mode
    interactif (c'est-à-dire directement à la ligne de commande). C'est
    ce que nous faisons à la première ligne de notre exemple : **from
    tkinter import \*** consiste à importer toutes les classes contenues
    dans le module *tkinter*.\
     Nous devrons de plus en plus souvent parler de ces *classes*. En
    programmation, on appelle ainsi des *générateurs d'objets*, lesquels
    sont eux-mêmes des morceaux de programmes réutilisables. Nous
    n'allons pas essayer de vous fournir dès à présent une définition
    définitive et précise de ce que sont les objets et les classes, mais
    plutôt vous proposer d'en utiliser directement quelques-un(e)s. Nous
    affinerons notre compréhension petit à petit par la suite.
2.  À la deuxième ligne de notre exemple : **fen1 = Tk()**, nous
    utilisons l'une des classes du module *tkinter*, la classe **Tk()**,
    et nous en créons une *instance* (autre terme désignant un objet
    spécifique), à savoir la fenêtre **fen1**.\
     Ce processus d'*instanciation d'un objet à partir d'une classe* est
    une opération fondamentale dans les techniques actuelles de
    programmation. Celles-ci font en effet de plus en plus souvent appel
    à une méthodologie que l'on appelle *programmation orientée objet*
    (ou OOP : *Object Oriented Programming*).\
     La **classe** est en quelque sorte un modèle général (ou un moule)
    à partir duquel on demande à la machine de construire un objet
    informatique particulier. La classe contient toute une série de
    définitions et d'options diverses, dont nous n'utilisons qu'une
    partie dans l'objet que nous créons à partir d'elle. Ainsi la classe
    **Tk()**, qui est l'une des classes les plus fondamentales de la
    bibliothèque *tkinter*, contient tout ce qu'il faut pour engendrer
    différents types de fenêtres d'application, de tailles ou de
    couleurs diverses, avec ou sans barre de menus, etc.\
     Nous nous en servons ici pour créer notre objet graphique de base,
    à savoir la fenêtre qui contiendra tout le reste. Dans les
    parenthèses de **Tk()**, nous pourrions préciser différentes
    options, mais nous laisserons cela pour un peu plus tard.\
     L'instruction d'*instanciation* ressemble à une simple affectation
    de variable. Comprenons bien cependant qu'il se passe ici deux
    choses à la fois :
    1.  *la création d'un nouvel objet*, (lequel peut être fort complexe
        dans certains cas, et par conséquent occuper un espace mémoire
        considérable) ;
    2.  *l'affectation d'une variable,* qui va désormais servir de
        *référence* pour manipuler l'objet[^note_39].

3.  À la troisième ligne :\
    **tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')**,\
     nous créons un autre objet (un *widget*), cette fois à partir de la
    classe **Label()**.\
     Comme son nom l'indique, cette classe définit toutes sortes
    d'*étiquettes* (ou de *libellés*). En fait, il s'agit tout
    simplement de fragments de texte quelconques, utilisables pour
    afficher des informations et des messages divers à l'intérieur d'une
    fenêtre.\
     Nous efforçant d'apprendre au passage la manière correcte
    d'exprimer les choses, nous dirons que nous créons ici l'objet
    **tex1** par *instanciation* de la classe **Label()**.\
     Remarquons que nous faisons appel à une classe, de la même manière
    que nous faisons appel à une fonction : c'est-à-dire en fournissant
    un certain nombre d'arguments dans des parenthèses. Nous verrons
    plus loin qu'une classe est en fait une sorte de « conteneur » dans
    lequel sont regroupées des fonctions et des données.\
     Quels arguments avons-nous donc fournis pour cette instanciation ?
    1.  Le premier argument transmis (**fen1**), indique que le nouveau
        *widget* que nous sommes en train de créer sera contenu *dans un
        autre widget préexistant*, que nous désignons donc ici comme son
        « maître » : l'objet **fen1** est le *widget maître* de l'objet
        **tex1**. On pourra dire aussi que l'objet **tex1** est un
        *widget esclave* de l'objet **fen1.**
    2.  Les deux arguments suivants servent à préciser la forme exacte
        que doit prendre notre *widget*. Ce sont en effet deux options
        de création, chacune fournie sous la forme d'une chaîne de
        caractères : d'abord le texte de l'étiquette, ensuite sa couleur
        d'avant-plan (ou *foreground*, en abrégé **fg**). Ainsi le texte
        que nous voulons afficher est bien défini, et il doit apparaître
        coloré en rouge.\
         Nous pourrions encore préciser bien d'autres caractéristiques :
        la police à utiliser, ou la couleur d'arrière-plan, par exemple.
        Toutes ces caractéristiques ont cependant une valeur par défaut
        dans les définitions internes de la classe **Label()**. Nous ne
        devons indiquer des options que pour les caractéristiques que
        nous souhaitons différentes du modèle standard.

4.  À la quatrième ligne de notre exemple : **tex1.pack()**, nous
    activons une *méthode* associée à l'objet **tex1** : la méthode
    **pack()**. Nous avons déjà rencontré ce terme de méthode (à propos
    des listes, notamment). Une méthode est une fonction intégrée à un
    objet (on dira aussi qu'elle est *encapsulée* dans l'objet). Nous
    apprendrons bientôt qu'un ***objet*** informatique est en fait un
    élément de programme contenant toujours :
    1.  un certain nombre de *données* (numériques ou autres), contenues
        dans des variables de types divers : on les appelle les
        *attributs* (ou les *propriétés*) de l'objet ;
    2.  un certain nombre de *procédures* ou de *fonctions* (qui sont
        donc des algorithmes) : on les appelle les *méthodes* de
        l'objet.\
         La méthode **pack()** fait partie d'un ensemble de méthodes qui
        sont applicables non seulement aux widgets de la classe
        **Label()**, mais aussi à la plupart des autres widgets
        *tkinter*, et qui agissent sur leur disposition géométrique dans
        la fenêtre. Comme vous pouvez le constater par vous-même si vous
        entrez les commandes de notre exemple une par une, la méthode
        **pack()** réduit automatiquement la taille de la fenêtre «
        maître » afin qu'elle soit juste assez grande pour contenir les
        widgets « esclaves » définis au préalable.

5.  À la cinquième ligne :\
    **bou1 = Button(fen1, text='Quitter',
    command = fen1.destroy)**,\
     nous créons notre second widget « esclave » : un bouton.\
    Z\
     Comme nous l'avons fait pour le widget précédent, nous appelons la
    classe **Button()** en fournissant entre parenthèses un certain
    nombre d'arguments. Étant donné qu'il s'agit cette fois d'un objet
    interactif, nous devons préciser avec l'option **command** ce qui
    devra se passer lorsque l'utilisateur effectuera un clic sur le
    bouton. Dans ce cas précis, nous actionnerons la méthode **destroy**
    associée à l'objet **fen1**, ce qui devrait provoquer l'effacement
    de la fenêtre[^note_40].
6.  La sixième ligne utilise la méthode **pack()** pour adapter la
    géométrie de la fenêtre au nouvel objet que nous venons d'y
    intégrer.
7.  La septième ligne : **fen1.mainloop()** est très importante, parce que
    c'est elle qui provoque le démarrage du *réceptionnaire
    d'événements* associé à la fenêtre. Cette instruction est nécessaire
    pour que votre application soit « à l'affût » des clics de souris,
    des pressions exercées sur les touches du clavier, etc. C'est donc
    cette instruction qui « la met en marche », en quelque sorte.\
     Comme son nom l'indique (*mainloop*), il s'agit d'une méthode de
    l'objet **fen1**, qui active une *boucle* de programme, laquelle «
    tournera » en permanence en tâche de fond, dans l'attente de
    messages émis par le système d'exploitation de l'ordinateur.
    Celui-ci interroge en effet sans cesse son environnement, notamment
    au niveau des périphériques d'entrée (souris, clavier, etc.).
    Lorsqu'un événement quelconque est détecté, divers *messages*
    décrivant cet événement sont expédiés aux programmes qui souhaitent
    en être avertis. Voyons cela un peu plus en détail.


[^note_36]: Dans les versions de Python antérieures à la version 3.0, le nom de ce module commençait par une majuscule.

[^note_37]: « *widget »* est le résultat de la contraction de l'expression « *window gadget »*. Dans certains environnements de programmation, on appellera cela plutôt un « contrôle » ou un « composant graphique ». Ce terme désigne en fait toute entité susceptible d'être placée dans une fenêtre d'application, comme par exemple un bouton, une case à cocher, une image, etc., et parfois aussi la fenêtre elle-même.

[^note_38]: Si vous effectuez cet exercice sous *Windows*, nous vous conseillons d'utiliser de préférence une version standard de Python dans une fenêtre DOS ou dans IDLE plutôt que *PythonWin.* Vous pourrez mieux observer ce qui se passe après l'entrée de chaque commande.

[^note_39]: Cette concision du langage est une conséquence du typage dynamique des variables en vigueur sous Python. D'autres langages utilisent une instruction particulière (telle que **new**) pour instancier un nouvel objet. Exemple : **maVoiture = new Cadillac** (instanciation d'un objet de classe **Cadillac**, référencé dans la variable **maVoiture**).

[^note_40]: Attention : l'appel de cette méthode *destroy* n'a pas lieu ici (c'est-à-dire dans l'instruction décrivant le bouton). Il ne faut donc pas accoler des parenthèses à son nom. C'est tkinter qui se chargera d'effectuer l''appel de destroy(), lorsqu'un utilisateur cliquera sur ce bouton.
