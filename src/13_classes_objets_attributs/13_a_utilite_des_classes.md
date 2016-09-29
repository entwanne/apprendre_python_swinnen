## 13-A - Utilité des classes

Les classes sont les principaux outils de la programmation orientée
objet (*Object Oriented Programming ou OOP*). Ce type de programmation
permet de structurer les logiciels complexes en les organisant comme des
ensembles d'objets qui interagissent, entre eux et avec le monde
extérieur.

Le premier bénéfice de cette approche de la programmation réside dans le
fait que les différents objets utilisés peuvent être construits
indépendamment les uns des autres (par exemple par des programmeurs
différents) sans qu'il n'y ait de risque d'interférence. Ce résultat est
obtenu grâce au concept d'*encapsulation* : la fonctionnalité interne de
l'objet et les variables qu'il utilise pour effectuer son travail, sont
en quelque sorte « enfermées » dans l'objet. Les autres objets et le
monde extérieur ne peuvent y avoir accès qu'à travers des procédures
bien définies : l'*interface* de l'objet.

En particulier, l'utilisation de classes dans vos programmes va vous
permettre - entre autres avantages -*d'éviter au maximum l'emploi de
variables globales*. Vous devez savoir en effet que l'utilisation de
variables globales comporte des risques, d'autant plus importants que
les programmes sont volumineux, parce qu'il est toujours possible que de
telles variables soient modifiées, ou même redéfinies, n'importe où dans
le corps du programme (ce risque s'aggrave particulièrement si plusieurs
programmeurs différents travaillent sur un même logiciel).

Un second bénéfice résultant de l'utilisation des classes est la
possibilité qu'elles offrent de *construire de nouveaux objets à partir
d'objets préexistants*, et donc de réutiliser des pans entiers d'une
programmation déjà écrite (sans toucher à celle-ci !), pour en tirer une
fonctionnalité nouvelle. Cela est rendu possible grâce aux concepts de
*dérivation* et de *polymorphisme :*

-   La *dérivation* est le mécanisme qui permet de construire une classe
    « enfant » au départ d'une classe « parente ». L'enfant ainsi obtenu
    hérite toutes les propriétés et toute la fonctionnalité de son
    ancêtre, auxquelles on peut ajouter ce que l'on veut.
-   Le *polymorphisme* permet d'attribuer des comportements différents à
    des objets dérivant les uns des autres, ou au même objet ou en
    fonction d'un certain contexte.

Avant d'aller plus loin, signalons ici que la programmation orientée
objet est *optionnelle* sous Python. Vous pouvez donc mener à bien de
nombreux projets sans l'utiliser, avec des outils plus simples tels que
les fonctions. Sachez cependant que si vous faites l'effort d'apprendre
à programmer à l'aide de classes, vous maîtriserez un niveau
d'abstraction plus élevé, ce qui vous permettra de traiter des problèmes
de plus en plus complexes. En d'autres termes, vous deviendrez un
programmeur beaucoup plus compétent. Pour vous en convaincre,
rappelez-vous les progrès que vous avez déjà réalisés au long de ce
cours :

-   Au début de votre étude, vous avez d'abord utilisé de simples
    instructions. Vous avez en quelque sorte « programmé à la main »
    (c'est-à-dire pratiquement sans outils).
-   Lorsque vous avez découvert les fonctions prédéfinies (cf. chapitre
    6), vous avez appris qu'il existait ainsi de vastes collections
    d'outils spécialisés, réalisés par d'autres programmeurs.
-   En apprenant à écrire vos propres fonctions (cf. chapitre 7 et
    suivants), vous êtes devenu capable de créer vous-même de nouveaux
    outils, ce qui vous a donné un surcroît de puissance considérable.
-   Si vous vous initiez maintenant à la programmation par classes, vous
    allez apprendre à construire des machines productrices d'outils.
    C'est évidemment plus complexe que de fabriquer directement ces
    outils, mais cela vous ouvre des perspectives encore bien plus
    larges !

Une bonne compréhension des classes vous aidera notamment à bien
maîtriser le domaine des interfaces graphiques (*tkinter*, *wxPython*)
et vous préparera efficacement à aborder d'autres langages modernes,
tels que *C++* ou *Java*.

