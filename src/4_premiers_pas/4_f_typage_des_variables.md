## 4-F - Typage des variables

Sous Python, il n'est pas nécessaire d'écrire des lignes de programme
spécifiques pour définir le type des variables avant de pouvoir les
utiliser. Il vous suffit en effet d'assigner une valeur à un nom de
variable pour que celle-ci soit *automatiquement créée avec le type qui
correspond au mieux à la valeur fournie*. Dans l'exercice précédent, par
exemple, les variables **n**, **msg** et **pi** ont été créées
automatiquement chacune avec un type différent (« nombre entier » pour
**n**, « chaîne de caractères » pour **msg**, « nombre à virgule
flottante » (ou « *float* », en anglais) pour **pi**).

Ceci constitue une particularité intéressante de Python, qui le rattache
à une famille particulière de langages où l'on trouve aussi par exemple
*Lisp*, *Scheme*, et quelques autres. On dira à ce sujet que *le typage
des variables sous Python est un typage dynamique*, par opposition au
*typage statique* qui est de règle par exemple en C++ ou en Java. Dans
ces langages, il faut toujours - par des instructions distinctes -
d'abord déclarer (définir) le nom et le type des variables, et ensuite
seulement leur assigner un contenu, lequel doit bien entendu être
compatible avec le type déclaré.

Le typage statique est préférable dans le cas des langages compilés,
parce qu'il permet d'optimiser l'opération de compilation (dont le
résultat est un code binaire « figé »).

Le typage dynamique quant à lui permet d'écrire plus aisément des
constructions logiques de niveau élevé (métaprogrammation, réflexivité),
en particulier dans le contexte de la programmation orientée objet
(polymorphisme). Il facilite également l'utilisation de structures de
données très riches telles que les listes et les dictionnaires.

