## 11-A - Utilité des fichiers

Imaginons par exemple que nous voulions écrire un petit programme
exerciseur qui fasse apparaître à l'écran des questions à choix
multiple, avec traitement automatique des réponses de l'utilisateur.
Comment allons-nous mémoriser le texte des questions elles-mêmes ?

L'idée
la plus simple consiste à placer chacun de ces textes dans une variable,
en début de programme, avec des instructions d'affectation du genre :



```python
a = "Quelle est la capitale du Guatemala ?"
b = "Qui à succédé à Henri IV ?"
c = "Combien font 26 x 43 ?"
     ... etc.
```



Cette idée est malheureusement beaucoup
trop simpliste. Tout va se compliquer en effet lorsque nous essayerons
d'élaborer la suite du programme,
c'est-à-dire les instructions qui
devront servir à sélectionner au hasard l'une ou l'autre de ces questions pour les présenter à
l'utilisateur. Employer par exemple
une longue suite d'instructions
**if** ... **elif** ... **elif**
... comme dans l'exemple ci-dessous
n'est certainement pas la bonne
solution (ce serait d'ailleurs bien
pénible à écrire : n'oubliez pas que
nous souhaitons traiter un grand nombre de questions !) :



```python
if choix == 1:
 selection = a
elif choix == 2:
 selection = b
elif choix == 3:
 selection = c
     ... etc.
```



La situation se présente déjà beaucoup
mieux si nous faisons appel à une liste :



```python
liste = ["Qui a vaincu Napoléon à Waterloo ?",
      "Comment traduit-on 'informatique' en anglais ?",
      "Quelle est la formule chimique du méthane ?", ... etc ...]
```



On peut en effet extraire n'importe quel élément de cette liste à
l'aide de son indice. Exemple
:

Rappel -

> L'indiçage commence toujours à partir de
> zéro.

Même si cette façon de procéder est déjà nettement meilleure que la
précédente, nous sommes toujours confrontés à plusieurs problèmes
gênants :

-   La lisibilité du programme va se détériorer très vite lorsque le
    nombre de questions deviendra important. En corollaire, nous
    accroîtrons la probabilité d'insérer une erreur de syntaxe dans la
    définition de cette longue liste. De telles erreurs seront bien
    difficiles à débusquer.
-   L'ajout de nouvelles questions, ou la modification de certaines
    d'entre elles, imposeront à chaque fois de rouvrir le code source du
    programme. En corollaire, il deviendra malaisé de retravailler ce
    même code source, puisqu'il comportera de nombreuses lignes de
    données encombrantes.
-   L'échange de données avec d'autres programmes (peut-être écrits dans
    d'autres langages) est tout simplement impossible, puisque ces
    données font partie du programme lui-même.

Cette dernière remarque nous suggère la direction à prendre : il est
temps que nous apprenions à *séparer les données et les programmes qui
les traitent dans des fichiers différents*.

Pour que cela devienne possible, nous devrons doter nos programmes de
divers mécanismes permettant de créer des fichiers, d'y envoyer des
données et de les récupérer par la suite.

Les langages de programmation proposent des
jeux d'instructions plus ou moins
sophistiqués pour effectuer ces tâches. Lorsque les quantités de données
deviennent très importantes, il devient d'ailleurs rapidement nécessaire de structurer les
relations entre ces données, et l'on
doit alors élaborer des systèmes appelés
*basesdedonnéesrelationnelles*, dont
la gestion peut s'avérer très
complexe. Lorsque l'on est confronté
à ce genre de problème, il est d'usage de déléguer une bonne part du travail à des
logiciels très spécialisés tels que *Oracle*, *IBMDB2*,
*Sybase*, *Adabas*, *PostgreSQL*, *MySQL*,
etc. Python est parfaitement capable de dialoguer avec ces systèmes,
mais nous laisserons cela pour un peu plus tard (voir : *gestion
d'une base de données*.

Nos ambitions présentes sont plus modestes.
Nos données ne se comptent pas encore par centaines de milliers, aussi
nous pouvons nous contenter de mécanismes simples pour les enregistrer
dans un fichier de taille moyenne, et les en extraire ensuite.

