## 5-F - Quelques règles de syntaxe Python

Tout ce qui précède nous amène à faire le point sur quelques règles de
syntaxe :

### 5-F-1 - Les limites des instructions et des blocs sont définies par la mise en page {#article.xml#Ld0e3745 .TitreSection2}

Dans de nombreux langages de programmation, il faut terminer chaque
ligne d'instructions par un caractère spécial (souvent le
point-virgule). Sous Python, c'est le caractère de fin de ligne[^note_13]
qui joue ce rôle. (Nous verrons plus loin comment outrepasser cette
règle pour étendre une instruction complexe sur plusieurs lignes.) On
peut également terminer une ligne d'instructions par un commentaire. Un
commentaire Python commence toujours par le caractère spécial **\#**.
Tout ce qui est inclus entre ce caractère et le saut à la ligne suivant
est complètement ignoré par le compilateur.

Dans la plupart des autres langages, un bloc d'instructions doit être
délimité par des symboles spécifiques (parfois même par des
instructions, telles que **begin** et **end**). En *C++* et en *Java*,
par exemple, un bloc d'instructions doit être délimité par des
accolades. Cela permet d'écrire les blocs d'instructions les uns à la
suite des autres, sans se préoccuper ni d'indentation ni de sauts à la
ligne, mais cela peut conduire à l'écriture de programmes confus,
difficiles à relire pour les pauvres humains que nous sommes. On
conseille donc à tous les programmeurs qui utilisent ces langages de se
servir *aussi* des sauts à la ligne et de l'indentation pour bien
délimiter visuellement les blocs.

Avec Python, vous *devez* utiliser les sauts à la ligne et
l'indentation, mais en contrepartie vous n'avez pas à vous préoccuper
d'autres symboles délimiteurs de blocs. En définitive, Python vous force
donc à écrire du code lisible, et à prendre de bonnes habitudes que vous
conserverez lorsque vous utiliserez d'autres langages.

### 5-F-2 - Instruction composée : en-tête, double point, bloc d'instructions indenté {#article.xml#Ld0e3778 .TitreSection2}

Nous aurons de nombreuses occasions d'approfondir le concept de « bloc
d'instructions » et de faire des exercices à ce sujet dès le chapitre
suivant.

Le schéma ci-contre en résume le principe.



![](images/image4.png)



-   Les blocs d'instructions sont toujours associés à une ligne
    d'en-tête contenant une instruction bien spécifique (if, elif, else,
    while, def, etc.) *se terminant par un double point*.
-   Les blocs sont *délimités par l'indentation* : toutes les lignes
    d'un même bloc doivent être indentées exactement de la même manière
    (c'est-à-dire décalées vers la droite d'un même nombre d'espaces).
    Le nombre d'espaces à utiliser pour l'indentation est quelconque,
    mais la plupart des programmeurs utilisent des multiples de 4.
-   Notez que le code du bloc le plus externe (bloc 1) ne peut pas
    lui-même être écarté de la marge de gauche (il n'est imbriqué dans
    rien).

> **Important :** *vous pouvez aussi indenter à l'aide de tabulations,
> mais alors vous devrez faire très attention à ne pas utiliser tantôt
> des espaces, tantôt des tabulations pour indenter les lignes d'un même
> bloc. En effet, et même si le résultat paraît identique à l'écran,
> espaces et tabulations sont des codes binaires distincts : Python
> considérera donc que ces lignes indentées différemment font partie de
> blocs différents. Il peut en résulter des erreurs difficiles à
> déboguer.*\
> *En conséquence, la plupart des programmeurs préfèrent se passer des
> tabulations. Si vous utilisez un éditeur de texte « intelligent »,
> vous avez tout intérêt à activer son option « Remplacer les
> tabulations par des espaces ».*

### 5-F-3 - Les espaces et les commentaires sont normalement ignorés {#article.xml#Ld0e3807 .TitreSection2}

À part ceux qui servent à l'indentation, en début de ligne, les espaces
placés à l'intérieur des instructions et des expressions sont presque
toujours ignorés (sauf s'ils font partie d'une chaîne de caractères). Il
en va de même pour les commentaires : ceux-ci commencent toujours par un
caractère dièse (\#) et s'étendent jusqu'à la fin de la ligne courante.


[^note_13]: Ce caractère n'apparaît ni à l'écran, ni sur les listings imprimés. Il est cependant bien présent, à un point tel qu'il fait même problème dans certains cas, parce qu'il n'est pas encodé de la même manière par tous les systèmes d'exploitation. Nous en reparlerons plus loin, à l'occasion de notre étude des fichiers texte (page ).
