## 3-D - Langage machine, langage de programmation

À strictement parler, un ordinateur n'est rien d'autre qu'une machine
effectuant des opérations simples sur des séquences de signaux
électriques, lesquels sont conditionnés de manière à ne pouvoir prendre
que deux états seulement (par exemple un potentiel électrique maximum ou
minimum). Ces séquences de signaux obéissent à une logique du type «
tout ou rien » et peuvent donc être considérés conventionnellement comme
des suites de nombres ne prenant jamais que les deux valeurs 0 et 1. Un
système numérique ainsi limité à deux chiffres est appelé système
binaire.

Sachez dès à présent que dans son fonctionnement interne, un ordinateur
est totalement incapable de traiter autre chose que des nombres
binaires. Toute information d'un autre type doit être convertie, ou
codée, *en format binaire*. Cela est vrai non seulement pour les données
que l'on souhaite traiter (les textes, les images, les sons, les
nombres, etc.), mais aussi pour les programmes, c'est-à-dire les
séquences d'instructions que l'on va fournir à la machine pour lui dire
ce qu'elle doit faire avec ces données.

Le seul « langage » que l'ordinateur puisse véritablement « comprendre »
est donc très éloigné de ce que nous utilisons nous-mêmes. C'est une
longue suite de 1 et de 0 (les « bits ») souvent traités par groupes de
8 (les « octets »), 16, 32, ou même 64. Ce « langage machine » est
évidemment presque incompréhensible pour nous. Pour « parler » à un
ordinateur, il nous faudra utiliser des systèmes de traduction
automatiques, capables de convertir en nombres binaires des suites de
caractères formant des mots-clés (anglais en général) qui seront plus
significatifs pour nous.

Ces systèmes de traduction automatique seront établis sur la base de
toute une série de conventions, dont il existera évidemment de
nombreuses variantes.

Le système de traduction proprement dit s'appellera *interpréteur* ou
bien *compilateur*, suivant la méthode utilisée pour effectuer la
traduction. On appellera *langage de programmation* un ensemble de
mots-clés (choisis arbitrairement) associé à un ensemble de règles très
précises indiquant comment on peut assembler ces mots pour former des «
phrases » que l'interpréteur ou le compilateur puisse traduire en
langage machine (binaire).

Suivant son niveau d'abstraction, on pourra dire d'un langage qu'il est
« de bas niveau » (ex : *assembleur*) ou « de haut niveau » (ex :
*Pascal*, *Perl*, *Smalltalk*, *Scheme*, *Lisp*...). Un langage de bas
niveau est constitué d'instructions très élémentaires, très « proches de
la machine ». Un langage de haut niveau comporte des instructions plus
abstraites, plus « puissantes » (et donc plus « magiques »). Cela
signifie que chacune de ces instructions pourra être traduite par
l'interpréteur ou le compilateur en un grand nombre d'instructions
machine élémentaires.

Le langage que vous avez allez apprendre en premier est *Python*. Il
s'agit d'un langage de haut niveau, dont la traduction en code binaire
est complexe et prend donc toujours un certain temps. Cela pourrait
paraître un inconvénient. En fait, les avantages que présentent les
langages de haut niveau sont énormes : il est *beaucoup plus facile*
d'écrire un programme dans un langage de haut niveau ; l'écriture du
programme prend donc beaucoup moins de temps ; la probabilité d'y faire
des fautes est nettement plus faible ; la maintenance (c'est-à-dire
l'apport de modifications ultérieures) et la recherche des erreurs (les
« bugs ») sont grandement facilitées. De plus, un programme écrit dans
un langage de haut niveau sera souvent *portable*, c'est-à-dire que l'on
pourra le faire fonctionner sans guère de modifications sur des machines
ou des systèmes d'exploitation différents. Un programme écrit dans un
langage de bas niveau ne peut jamais fonctionner que sur un seul type de
machine : pour qu'une autre l'accepte, il faut le réécrire entièrement.

Dans ce que nous venons d'expliquer sommairement, vous aurez sans doute
repéré au passage de nombreuses « boîtes noires » : interpréteur,
système d'exploitation, langage, instructions machine, code binaire,
etc. L'apprentissage de la programmation va vous permettre d'en
entrouvrir quelques-unes. Restez cependant conscients que vous
n'arriverez pas à les décortiquer toutes. De nombreux *objets*
informatiques créés par d'autres resteront probablement « magiques »
pour vous pendant longtemps (à commencer par le langage de programmation
lui-même, par exemple). Vous devrez donc faire confiance à leurs
auteurs, quitte à être déçus parfois en constatant que cette confiance
n'est pas toujours méritée. Restez donc vigilants, apprenez à vérifier,
à vous documenter sans cesse. Dans vos propres productions, soyez
rigoureux et évitez à tout prix la « magie noire » (les programmes
pleins d'astuces tarabiscotées que vous êtes seul à comprendre) : un
*hacker* digne de confiance n'a rien à cacher.

