## 2-A - Choix d'un premier langage de programmation

Il existe un très grand nombre de langages de programmation, chacun avec
ses avantages et ses inconvénients. Il faut bien en choisir un. Lorsque
nous avons commencé à réfléchir à cette question, durant notre
préparation d'un curriculum pour la nouvelle option Sciences &
Informatique, nous avions personnellement accumulé une assez longue
expérience de la programmation sous *Visual Basic* (*Microsoft*) et sous
*Clarion* (*Topspeed*). Nous avions également expérimenté quelque peu
sous *Delphi* (*Borland*). Il était donc naturel que nous pensions
d'abord exploiter l'un ou l'autre de ces langages. Si nous souhaitions
les utiliser comme outils de base pour un apprentissage général de la
programmation, ces langages présentaient toutefois deux gros
inconvénients :

-   Ils sont liés à des environnements de programmation (c'est-à-dire
    des logiciels) propriétaires.\
     Cela signifiait donc, non seulement que l'institution scolaire
    désireuse de les utiliser devrait acheter une licence de ces
    logiciels pour chaque poste de travail (ce qui pouvait se révéler coûteux),
    mais surtout que les élèves souhaitant utiliser leurs compétences de
    programmation ailleurs qu'à l'école seraient implicitement forcés
    d'acquérir eux aussi des licences, ce que nous ne pouvions pas
    accepter. Un autre grave inconvénient
    de ces produits propriétaires est qu'ils comportent de nombreuses «
    boîtes noires » dont on ne peut connaître le contenu. Leur
    documentation est donc incomplète, et leur évolution incertaine.
    
-   Ce sont des langages spécifiquement liés au seul système
    d'exploitation *Windows*. Ils ne sont pas « portables » sur d'autres
    systèmes (*Unix*, *Mac OS*, *etc*.). Cela ne cadrait pas avec notre
    projet pédagogique qui ambitionne d'inculquer une formation générale
    (et donc diversifiée) dans laquelle les invariants de l'informatique
    seraient autant que possible mis en évidence.

Nous avons alors décidé d'examiner l'offre alternative, c'est-à-dire
celle qui est proposée gratuitement dans la mouvance de l'informatique
libre[^note_1].
Ce que nous avons trouvé nous a enthousiasmés : non seulement il existe
dans le monde de *l'OpenSource* des interpréteurs et des compilateurs
gratuits pour toute une série de langages, mais surtout ces langages
sont modernes, performants, portables (c'est-à-dire utilisables sur
différents systèmes d'exploitation tels que *Windows*, *Linux*, *Mac OS*
...), et fort bien documentés.

Le langage dominant y est sans conteste *C/C++*. Ce langage s'impose
comme une référence absolue, et tout informaticien sérieux doit s'y
frotter tôt ou tard. Il est malheureusement très rébarbatif et
compliqué, trop proche de la machine. Sa syntaxe est peu lisible et fort
contraignante. La mise au point d'un gros logiciel écrit en *C/C++* est
longue et pénible. (Les mêmes remarques valent aussi dans une large
mesure pour le langage *Java.*)

D'autre part, la pratique moderne de ce langage fait abondamment appel à
des générateurs d'applications et autres outils d'assistance très
élaborés tels *C++Builder*, *Kdevelop*, etc. Ces environnements de
programmation peuvent certainement se révéler très efficaces entre les
mains de programmeurs expérimentés, mais ils proposent d'emblée beaucoup
trop d'outils complexes, et ils présupposent de la part de l'utilisateur
des connaissances qu'un débutant ne maîtrise évidemment pas encore. Ce
seront donc aux yeux de celui-ci de véritables « usines à gaz » qui
risquent de lui masquer les mécanismes de base du langage lui-même. Nous
laisserons donc le *C/C++* pour plus tard.

Pour nos débuts dans l'étude de la programmation, il nous semble
préférable d'utiliser un langage de plus haut niveau, moins
contraignant, à la syntaxe plus lisible. Après avoir successivement
examiné et expérimenté quelque peu les langages *Perl* et *Tcl*/*Tk* ,
nous avons finalement décidé d'adopter Python, langage très moderne à la
popularité grandissante.


[^note_1]: Un logiciel libre (*Free Software*) est avant tout un logiciel dont le code source est accessible à tous (*Open source*). Souvent gratuit (ou presque), copiable et modifiable librement au gré de son acquéreur, il est généralement le produit de la collaboration bénévole de centaines de développeurs enthousiastes dispersés dans le monde entier. Son code source étant « épluché » par de très nombreux spécialistes (étudiants et professeurs universitaires), un logiciel libre se caractérise la plupart du temps par un très haut niveau de qualité technique. Le plus célèbre des logiciels libres est le système d'exploitation ***GNU/Linux***, dont la popularité ne cesse de s'accroître de jour en jour.
