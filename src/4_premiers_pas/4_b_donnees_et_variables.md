## 4-B - Données et variables

Nous aurons l'occasion de détailler plus loin les différents types de
données numériques. Mais avant cela, nous pouvons dès à présent aborder
un concept de grande importance.

L'essentiel du travail effectué par un programme d'ordinateur consiste à
manipuler des *données*. Ces données peuvent être très diverses (tout ce
qui est *numérisable*, en fait[^note_6]),
mais dans la mémoire de l'ordinateur elles se ramènent toujours en
définitive à *unesuitefiniedenombresbinaires*.

Pour pouvoir accéder aux données, le programme d'ordinateur (quel que
soit le langage dans lequel il est écrit) fait abondamment usage d'un
grand nombre de *variables* de différents types.

Une variable apparaît dans un langage de programmation sous un
*nomdevariable* à peu près quelconque (voir ci-après), mais pour
l'ordinateur il s'agit d'une *référence* désignant une adresse mémoire,
c'est-à-dire un emplacement précis dans la mémoire vive.

À cet emplacement est stockée une *valeur* bien déterminée. C'est la
donnée proprement dite, qui est donc stockée sous la forme d'une suite
de nombres binaires, mais qui n'est pas nécessairement un nombre aux
yeux du langage de programmation utilisé. Cela peut être en fait à peu
près n'importe quel « objet » susceptible d'être placé dans la mémoire
d'un ordinateur, par exemple : un nombre entier, un nombre réel, un
nombre complexe, un vecteur, une chaîne de caractères typographiques, un
tableau, une fonction, etc.

Pour distinguer les uns des autres ces divers contenus possibles, le
langage de programmation fait usage de différents types de variables (le
type *entier*, le type *réel*, le type *chaînedecaractères*, le type
*liste*, etc.). Nous allons expliquer tout cela dans les pages
suivantes.


[^note_6]: *Que peut-on numériser au juste ?* Voilà une question très importante, qu'il vous faudra débattre dans votre cours d'informatique générale.
