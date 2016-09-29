## 6-C - Premiers scripts, ou comment conserver nos programmes

Jusqu'à présent, vous avez toujours utilisé Python *en mode interactif*
(c'est-à-dire que vous avez à chaque fois entré les commandes
directement dans l'interpréteur, sans les sauvegarder au préalable dans
un fichier). Cela vous a permis d'apprendre très rapidement les bases du
langage, par expérimentation directe. Cette façon de faire présente
toutefois un gros inconvénient : toutes les séquences d'instructions que
vous avez écrites disparaissent irrémédiablement dès que vous fermez
l'interpréteur. Avant de poursuivre plus avant votre étude, il est donc
temps que vous appreniez à sauvegarder vos programmes dans des fichiers,
sur disque dur ou clef USB, de manière à pouvoir les retravailler par
étapes successives, les transférer sur d'autres machines, etc.

Pour ce faire, vous allez désormais rédiger vos séquences d'instructions
dans un *éditeur de texte* quelconque (par exemple *Kate*, *Gedit*,
*Geany*,... sous *Linux*, *Wordpad, Geany, Komodo editor, ...* sous
*Windows*, ou encore l'éditeur incorporé dans l'interface de
développement *IDLE* qui fait partie de la distribution de Python pour
Windows). Ainsi vous écrirez *unscript*, que vous pourrez ensuite
sauvegarder, modifier, copier, etc. comme n'importe quel autre texte
traité par ordinateur[^note_15].
La figure ci-dessus illustre l'utilisation de l'éditeur *Gedit* sous
*Linux (Ubuntu)* :



![](images/image5.png)



Par la suite, lorsque vous voudrez tester l'exécution de votre
programme, il vous suffira de lancer l'interpréteur Python en lui
fournissant (comme argument) le nom du fichier qui contient le script.
Par exemple, si vous avez placé un script dans un fichier nommé «
MonScript », il suffira d'entrer la commande suivante dans une fenêtre
de terminal pour que ce script s'exécute :

python3 MonScript [^note_16]

Pour faire mieux encore, veillez à choisir pour votre fichier un nom qui
se termine par l'extension .**py**

Si vous respectez cette convention, vous pourrez aussi lancer
l'exécution du script, simplement en cliquant sur son nom ou sur l'icône
correspondante dans le gestionnaire de fichiers (c'est-à-dire
l'explorateur, sous *Windows*, ou bien *Nautilus*, *Konqueror*... sous
*Linux*).

Ces gestionnaires graphiques « savent » en effet qu'il doivent lancer
l'interpréteur Python chaque fois que leur utilisateur essaye d'ouvrir
un fichier dont le nom se termine par .py (cela suppose bien entendu
qu'ils aient été correctement configurés). La même convention permet en
outre aux éditeurs « intelligents » de reconnaître automatiquement les
scripts Python, et d'adapter leur coloration syntaxique en conséquence.

Un script Python contiendra des séquences d'instructions identiques à
celles que vous avez expérimentées jusqu'à présent. Puisque ces
séquences sont destinées à être conservées et relues plus tard par
vous-même ou par d'autres, *il vous est très fortement recommandé
d'expliciter vos scripts le mieux possible, en y incorporant de nombreux
commentaires*. La principale difficulté de la programmation consiste en
effet à mettre au point des algorithmes corrects. Afin que ces
algorithmes puissent être vérifiés, corrigés, modifiés, etc. dans de
bonnes conditions, il est essentiel que leur auteur les décrive le plus
complètement et le plus clairement possible. Et le meilleur emplacement
pour cette description est le corps même du script (ainsi elle ne peut
pas s'égarer).

> Un bon programmeur veille toujours à insérer un grand nombre de
> commentaires dans ses scripts. En procédant ainsi, non seulement il
> facilite la compréhension de ses algorithmes pour d'autres lecteurs
> éventuels, mais encore il se force lui-même à avoir les idées plus
> claires.

On peut insérer des commentaires quelconques à peu près n'importe où
dans un script. Il suffit de les faire précéder d'un caractère \#.
Lorsqu'il rencontre ce caractère, l'interpréteur Python ignore tout ce
qui suit, jusqu'à la fin de la ligne courante.

Comprenez bien qu'il est important d'inclure des commentaires *au fur et
à mesure de l'avancement de votre travail de programmation*. N'attendez
pas que votre script soit terminé pour les ajouter « après coup ». Vous
vous rendrez progressivement compte qu'un programmeur passe *énormément
de temps* à relire son propre code (pour le modifier, y rechercher des
erreurs, etc.). Cette relecture sera grandement facilitée si le code
comporte de nombreuses explications et remarques.

Ouvrez donc un éditeur de texte, et rédigez le script ci-dessous :



```python
# Premier essai de script Python
# petit programme simple affichant une suite de Fibonacci, c.à.d. une suite
# de nombres dont chaque terme est égal à la somme des deux précédents.
 
a, b, c = 1, 1, 1	# a & b servent au calcul des termes successifs
	     # c est un simple compteur
print(b)	   # affichage du premier terme
while c<15:	      # nous afficherons 15 termes au total
 a, b, c = b, a+b, c+1
 print(b)
```



Afin de vous montrer tout de suite le bon exemple, nous commençons ce
script par trois lignes de commentaires, qui contiennent une courte
description de la fonctionnalité du programme. Prenez l'habitude de
faire de même dans vos propres scripts.

Certaines lignes de code sont également elle-mêmes documentées. Si vous
procédez comme nous l'avons fait, c'est-à-dire en insérant des
commentaires à la droite des instructions correspondantes, veillez à les
écarter suffisamment de celles-ci, afin de ne pas gêner leur lisibilité.

Lorsque vous aurez bien vérifié votre texte, sauvegardez-le et
exécutez-le.

> Bien que ce ne soit pas indispensable, nous vous recommandons une fois
> encore de choisir pour vos scripts des noms de fichiers se terminant
> par l'extension .py. Cela aide beaucoup à les identifier comme tels
> dans un répertoire. Les gestionnaires graphiques de fichiers
> (explorateur Windows, Nautilus, Konqueror) se servent d'ailleurs de
> cette extension pour leur associer une icône spécifique. **Évitez
> cependant de choisir des noms qui risqueraient d'être déjà attribués à
> des modules python existants** : des noms tels que math.py ou
> tkinter.py, par exemple, sont à proscrire !

Si vous travaillez en mode texte sous *Linux*, ou dans une fenêtre
*MS-DOS*, vous pouvez exécuter votre script à l'aide de la commande
python3 suivie du nom du script. Si vous travaillez en mode graphique
sous *Linux*, vous pouvez ouvrir une fenêtre de terminal et faire la
même chose :



```python
python3 monScript.py
```



Dans un gestionnaire graphique de fichiers, vous pouvez en principe
lancer l'exécution de votre script en effectuant un (double ?) clic de
souris sur l'icône correspondante. Ceci ne pourra cependant fonctionner
que si c'est bien **Python 3** qui a été désigné comme interpréteur par
défaut pour les fichiers comportant l'extension .py (des problèmes
peuvent en effet apparaître si plusieurs versions de Python sont
installées sur votre machine - voyez votre professeur ou votre gourou
local pour détailler ces questions).

Si vous travaillez avec *IDLE*, vous pouvez lancer l'exécution du script
en cours d'édition, directement à l'aide de la combinaison de touches
\<**Ctrl**-**F5**\>. Dans d'autres environnements de travail
spécifiquement dédiés à Python, tels que *Geany*, vous trouverez
également des icônes et/ou des raccourcis clavier pour lancer
l'exécution (il s'agit souvent de la touche F5). Consultez votre
professeur ou votre *gourou* local concernant les autres possibilités de
lancement éventuelles sur différents systèmes d'exploitation.

### 6-C-1 - Problèmes éventuels liés aux caractères accentués {#article.xml#Ld0e5006 .TitreSection2}

Si vous avez rédigé votre script avec un logiciel éditeur récent (tels
ceux que nous avons déjà indiqués), le script décrit ci-dessus devrait
s'exécuter sans problème avec la version actuelle de Python 3. Si votre
logiciel éditeur est ancien ou mal configuré, par contre, il se peut que
vous obteniez un message d'erreur similaire à celui-ci :



```python
File "fibo2.py", line 2 
SyntaxError: Non-UTF-8 code starting with '\xe0' in file fibo2.py on line 2, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```



Ce message vous indique que le script contient des caractères
typographiques encodés suivant une norme ancienne (vraisemblablement la
norme ISO-8859-1 ou Latin-1).

Nous détaillerons les différentes normes d'encodage plus loin dans ce
livre. Pour l'instant, il vous suffit de savoir que vous devez dans ce
cas :

-   soit reconfigurer votre éditeur de textes pour qu'il encode les
    caractères en Utf-8 (ou vous procurer un autre éditeur fonctionnant
    suivant cette norme). C'est la meilleure solution, car ainsi vous
    serez certain à l'avenir de travailler en accord avec les
    conventions de standardisation actuelles, qui finiront tôt ou tard
    par remplacer partout les anciennes.
-   soit inclure le pseudo-commentaire suivant au début de tous vos
    scripts (obligatoirement à la 1^e^ ou à la 2^e^ ligne) :\
    \
    `# -*- coding:Latin-1 -*-`

Le pseudo-commentaire ci-dessus indique à Python que vous utilisez dans
votre script le jeu de caractères accentués *ASCII étendu* correspondant
aux principales langues de l'Europe occidentale (Français, Allemand,
Portugais, etc.), encodé sur un seul octet suivant la norme
*ISO-8859-1*, laquelle est souvent désignée aussi par l'étiquette
*Latin-1* .

Python peut traiter correctement les caractères encodés suivant toute
une série de normes, mais il faut alors lui signaler laquelle vous
utilisez à l'aide d'un pseudo-commentaire en début de script. Sans cette
indication, Python considère que vos scripts ont été encodés en
Utf-8[^note_17],
suivant en cela la nouvelle norme *Unicode*, laquelle a été mise au
point pour standardiser la représentation numérique de tous les
caractères spécifiques des différentes langues mondiales, ainsi que les
symboles mathématiques, scientifiques, etc. Il existe plusieurs
représentations ou *encodages* de cette norme, et nous devrons
approfondir cette question plus loin[^note_18],
mais pour l'instant il vous suffit de savoir que l'encodage le plus
répandu sur les ordinateurs récents est *Utf-8*. Dans ce système, les
caractères standard (*ASCII*) sont encore encodés sur un seul octet, ce
qui assure une certaine compatibilité avec l'ancienne norme d'encodage
*Latin-1*, mais les autres caractères (parmi lesquels nos caractères
accentués) peuvent être encodés sur 2, 3, ou même parfois 4 octets.

Nous apprendrons comment gérer et convertir ces différents encodages,
lorsque nous étudierons plus en détail le traitement des fichiers texte
(au chapitre 9).

Exercices

.Écrivez un programme qui calcule le volume d'un parallélépipède
rectangle dont sont fournis au départ la largeur, la hauteur et la
profondeur.

.Écrivez un programme qui convertit un nombre entier de secondes fourni
au départ en un nombre d'années, de mois, de jours, de minutes et de
secondes (utilisez l'opérateur modulo : **%**).

.Écrivez un programme qui affiche les 20 premiers termes de la table de
multiplication par 7, en signalant au passage (à l'aide d'une
astérisque) ceux qui sont des multiples de 3.\
 Exemple : 7 14 21 \* 28 35 42 \* 49 ...

.Écrivez un programme qui calcule les 50 premiers termes de la table de
multiplication par 13, mais n'affiche que ceux qui sont des multiples de
7.

.Écrivez un programme qui affiche la suite
de symboles suivante :



```python
*
**
***
****
*****
******
*******
```




[^note_15]: Il serait parfaitement possible d'utiliser un système de traitement de textes, à la condition d'effectuer la sauvegarde sous un format « texte pur » (sans balises de mise en page). Il est cependant préférable d'utiliser un véritable éditeur « intelligent » tel que *Gedit, Geany*, ou *IDLE*, muni d'une fonction de coloration syntaxique pour Python, qui vous aide à éviter les fautes de syntaxe. Avec *IDLE*, suivez le menu : File  New window (ou tapez Ctrl-N) pour ouvrir une nouvelle fenêtre dans laquelle vous écrirez votre script. Pour l'exécuter, il vous suffira (après sauvegarde), de suivre le menu : Edit  Run script (ou de taper Ctrl-F5).

[^note_16]: Si l'interpréteur Python 3 a été installé sur votre machine comme interpréteur Python par défaut, vous devriez pouvoir aussi entrer tout simplement : `python MonScript` . Mais attention : si plusieurs versions de Python sont présentes, il se peut que cette commande active plutôt une version antérieure (Python 2.x).

[^note_17]: Dans les versions de Python antérieures à la version 3.0, l'encodage par défaut était ASCII. Il fallait donc toujours préciser en début de script les autres encodages (y compris Utf-8).

[^note_18]: Voir page
