## 11-C - Noms de fichiers - le répertoire courant

Pour simplifier les explications qui vont suivre, nous indiquerons
seulement des noms simples pour les fichiers que nous allons manipuler.
Si vous procédez ainsi dans vos exercices, les fichiers en question
seront créés et/ou recherchés par Python *dans le répertoire courant*.
Celui-ci est habituellement le répertoire où se trouve le script
lui-même, sauf si vous lancez ce script depuis la fenêtre d'un shell
*IDLE*, auquel cas le répertoire courant est défini au lancement de
*IDLE* lui-même (sous *Windows*, la définition de ce répertoire fait
partie des propriétés de l'icône de lancement).

Si vous travaillez avec *IDLE*, vous souhaiterez donc certainement forcer
Python à changer son répertoire courant, afin que celui-ci corresponde à
vos attentes. Pour ce faire, utilisez les commandes suivantes en début
de session. Nous supposons pour la démonstration que le répertoire visé
est le répertoire `/home/jules/exercices` . Même si vous travaillez sous
*Windows* (où ce n'est pas la règle), vous pouvez utiliser cette
syntaxe (c'est-à-dire des caractères
**/** et non **\\** en guise de séparateurs : c'est la convention en vigueur dans le monde
*Unix*). Python effectuera
automatiquement les conversions nécessaires, suivant que vous travaillez
sous *Mac OS*, *Linux*, ou *Windows*[^note_51].



```python
>>> from os import chdir
>>> chdir("/home/jules/exercices")
```



La première commande importe la fonction **chdir()** du module **os**.
Le module **os** contient toute une série de fonctions permettant de
dialoguer avec le système d'exploitation (**os** = *operatingsystem*),
quel que soit celui-ci.

La seconde commande provoque le changement
de répertoire (**chdir =***changedirectory*).

-   Vous avez également la possibilité d'insérer ces commandes en début
    de script, ou encore d'indiquer le chemin d'accès complet dans le
    nom des fichiers que vous manipulez, mais cela risque peut-être
    d'alourdir l'écriture de vos programmes.
-   Choisissez de préférence des noms de
    fichiers courts. Évitez dans toute la mesure du possible les
    caractères accentués, les espaces et les signes typographiques
    spéciaux. Dans les environnements de travail de type Unix (MacOS,
    Linux, BSD ...), il est souvent recommandé aussi de n'utiliser que
    des caractères minuscules.


[^note_51]: Dans le cas de *Windows*, vous pouvez également inclure dans ce chemin la lettre qui désigne le périphérique de stockage où se trouve le fichier. Par exemple : **D:/home/jules/exercices**.
