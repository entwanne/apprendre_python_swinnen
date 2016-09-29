## 2-B - Présentation du langage Python

> Ce texte de Stéfane Fermigier date un
> peu, mais il reste d'actualité pour l'essentiel. Il est extrait d'un
> article paru dans le magazine Programmez! en décembre 1998. Il
> est également disponible sur
> http://www.linux-center.org/articles/9812/python.html. Stéfane
> Fermigier est le co-fondateur de l'AFUL (Association Francophone des
> Utilisateurs de Linux et des logiciels libres).

Python est un langage portable, dynamique, extensible, gratuit, qui
permet (sans l'imposer) une approche modulaire et orientée objet de la
programmation. Python est développé depuis 1989 par Guido van Rossum et
de nombreux contributeurs bénévoles.

### 2-B-1 - Caractéristiques du langage {#article.xml#Ld0e389 .TitreSection2}

Détaillons un peu les principales caractéristiques de Python, plus
précisément, du langage et de ses deux implantations actuelles:

-   Python est **portable**, non seulement sur les différentes variantes
    d'*Unix*, mais aussi sur les OS propriétaires : *Mac OS*, *BeOS*,
    *NeXTStep*, *MS-DOS* et les différentes variantes de *Windows*. Un
    nouveau compilateur, baptisé *JPython*, est écrit en Java et génère
    du *bytecode* Java.
-   Python est **gratuit**, mais on peut l'utiliser sans restriction
    dans des projets commerciaux.
-   Python convient aussi bien à des **scripts** d'une dizaine de lignes
    qu'à des **projets complexes** de plusieurs dizaines de milliers de
    lignes.
-   La **syntaxe** de Python est **très simple** et, combinée à des
    **types de données évolués** (listes, dictionnaires...), conduit à
    des programmes à la fois très compacts et très lisibles. À
    fonctionnalités égales, un programme Python (abondamment commenté et
    présenté selon les canons standards) est souvent de 3 à 5 fois plus
    court qu'un programme C ou C++ (ou même Java) équivalent, ce qui
    représente en général un temps de développement de 5 à 10 fois plus
    court et une facilité de maintenance largement accrue.
-   Python gère ses ressources (mémoire, descripteurs de fichiers...)
    sans intervention du programmeur, par un mécanisme de **comptage de
    références** (proche, mais différent, d'un *garbage collector*).
-   Il n'y a **pas de pointeurs** explicites en Python.
-   Python est (optionnellement) **multi-threadé**.
-   Python est **orienté-objet**. Il supporte **l'héritage multiple** et
    **la surcharge des opérateurs**. Dans son modèle objets, et en
    reprenant la terminologie de C++, toutes les méthodes sont
    virtuelles.
-   Python intègre, comme Java ou les versions récentes de C++, un
    système **d'exceptions**, qui permettent de simplifier
    considérablement la gestion des erreurs.
-   Python est **dynamique** (l'interpréteur peut évaluer des chaînes de
    caractères représentant des expressions ou des instructions Python),
    **orthogonal** (un petit nombre de concepts suffit à engendrer des
    constructions très riches), **réflectif** (il supporte la
    métaprogrammation, par exemple la capacité pour un objet de se
    rajouter ou de s'enlever des attributs ou des méthodes, ou même de
    changer de classe en cours d'exécution) et **introspectif** (un
    grand nombre d'outils de développement, comme le *debugger* ou le
    *profiler*, sont implantés en Python lui-même).
-   Comme *Scheme* ou *SmallTalk*, Python est dynamiquement typé. Tout
    objet manipulable par le programmeur possède un type bien défini à
    l'exécution, qui n'a pas besoin d'être déclaré à l'avance.
-   Python possède actuellement deux implémentations. L'une,
    **interprétée**, dans laquelle les programmes Python sont compilés
    en instructions portables, puis exécutés par une machine virtuelle
    (comme pour Java, avec une différence importante : Java étant
    statiquement typé, il est beaucoup plus facile d'accélérer
    l'exécution d'un programme Java que d'un programme Python). L'autre
    génère directement du *bytecode* Java.
-   Python est **extensible** : comme *Tcl* ou *Guile*, on peut
    facilement l'interfacer avec des bibliothèques C existantes. On peut
    aussi s'en servir comme d'un langage d'extension pour des systèmes
    logiciels complexes.
-   La **bibliothèque standard** de Python, et les paquetages
    contribués, donnent accès à une grande variété de services : chaînes
    de caractères et expressions régulières, services UNIX standards
    (fichiers, *pipes*, signaux, sockets, threads...), protocoles
    Internet (Web, News, FTP, CGI, HTML...), persistance et bases de
    données, interfaces graphiques.
-   Python est un langage qui **continue à évoluer**, soutenu par une
    communauté d'utilisateurs enthousiastes et responsables, dont la
    plupart sont des supporters du logiciel libre. Parallèlement à
    l'interpréteur principal, écrit en C et maintenu par le créateur du
    langage, un deuxième interpréteur, écrit en Java, est en cours de
    développement.
-   Enfin, Python est un langage de choix pour traiter le XML.

