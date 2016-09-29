## 3-F - Mise au point d'un programme - Recherche des erreurs (debug)

La programmation est une démarche très complexe, et comme c'est le cas
dans toute activité humaine, on y commet de nombreuses erreurs. Pour des
raisons anecdotiques, les erreurs de programmation s'appellent des «
*bugs* » (ou « bogues », en Français)[^note_4],
et l'ensemble des techniques que l'on met en œuvre pour les détecter et
les corriger s'appelle « *debug* » (ou « débogage »).

En fait, il peut exister dans un programme trois types d'erreurs assez
différentes, et il convient que vous appreniez à bien les distinguer.

### 3-F-1 - Erreurs de syntaxe {#article.xml#Ld0e896 .TitreSection2}

Python ne peut exécuter un programme que si sa syntaxe est parfaitement
correcte. Dans le cas contraire, le processus s'arrête et vous obtenez
un message d'erreur. Le terme syntaxe se réfère aux règles que les
auteurs du langage ont établies pour la structure du programme.

Tout langage comporte sa syntaxe. Dans la langue française, par exemple,
une phrase doit toujours commencer par une majuscule et se terminer par
un point. ainsi cette phrase comporte deux erreurs de syntaxe

Dans les textes ordinaires, la présence de quelques petites fautes de
syntaxe par-ci par-là n'a généralement pas d'importance. Il peut même
arriver (en poésie, par exemple), que des fautes de syntaxe soient
commises volontairement. Cela n'empêche pas que l'on puisse comprendre
le texte.

Dans un programme d'ordinateur, par contre, la moindre erreur de syntaxe
produit invariablement un arrêt de fonctionnement (un « plantage »)
ainsi que l'affichage d'un message d'erreur. Au cours des premières
semaines de votre carrière de programmeur, vous passerez certainement
pas mal de temps à rechercher vos erreurs de syntaxe. Avec de
l'expérience, vous en commettrez beaucoup moins.

Gardez à l'esprit que les mots et les symboles utilisés n'ont aucune
signification en eux-mêmes : ce ne sont que des suites de codes destinés
à être convertis automatiquement en nombres binaires. Par conséquent, il
vous faudra être très attentifs à respecter scrupuleusement la syntaxe
du langage.

Finalement, souvenez-vous que **tous** les détails ont de l'importance.
Il faudra en particulier faire très attention à la *casse* (c'est-à-dire
l'emploi des majuscules et des minuscules) et à la *ponctuation*. Toute
erreur à ce niveau (même minime en apparence, tel l'oubli d'une virgule,
par exemple) peut modifier considérablement la signification du code, et
donc le déroulement du programme.

Il est heureux que vous fassiez vos débuts en programmation avec un
langage interprété tel que Python. La recherche des erreurs y est facile
et rapide. Avec les langages compilés (tel le C++), il vous faudrait
recompiler l'intégralité du programme après chaque modification, aussi
minime soit-elle.

### 3-F-2 - Erreurs sémantiques {#article.xml#Ld0e922 .TitreSection2}

Le second type d'erreur est l'erreur sémantique ou erreur de logique.
S'il existe une erreur de ce type dans un de vos programmes, celui-ci
s'exécute parfaitement, en ce sens que vous n'obtenez aucun message
d'erreur, mais le résultat n'est pas celui que vous attendiez : vous
obtenez autre chose.

En réalité, le programme fait exactement ce que vous lui avez dit de
faire. Le problème est que ce que vous lui avez dit de faire ne
correspond pas à ce que vous vouliez qu'il fasse. La séquence
d'instructions de votre programme ne correspond pas à l'objectif
poursuivi. La sémantique (la logique) est incorrecte.

Rechercher des fautes de logique peut être une tâche ardue. C'est là que
se révélera votre aptitude à démonter toute forme résiduelle de « pensée
magique » dans vos raisonnements. Il vous faudra analyser patiemment ce
qui sort de la machine et tâcher de vous représenter une par une les
opérations qu'elle a effectuées, à la suite de chaque instruction.

### 3-F-3 - Erreurs à l'exécution {#article.xml#Ld0e931 .TitreSection2}

Le troisième type d'erreur est l'erreur en cours d'exécution (*Run-time
error*), qui apparaît seulement lorsque votre programme fonctionne déjà,
mais que des circonstances particulières se présentent (par exemple,
votre programme essaie de lire un fichier qui n'existe plus). Ces
erreurs sont également appelées des *exceptions*, parce qu'elles
indiquent généralement que quelque chose d'exceptionnel (et de
malencontreux) s'est produit. Vous rencontrerez davantage ce type
d'erreurs lorsque vous programmerez des projets de plus en plus
volumineux, et vous apprendrez plus loin dans ce cours qu'il existe des
techniques particulières pour les gérer.


[^note_4]: *bug* est à l'origine un terme anglais servant à désigner de petits insectes gênants, tels les punaises. Les premiers ordinateurs fonctionnaient à l'aide de « lampes » radios qui nécessitaient des tensions électriques assez élevées. Il est arrivé à plusieurs reprises que des petits insectes s'introduisent dans cette circuiterie complexe et se fassent électrocuter, leurs cadavres calcinés provoquant alors des court-circuits et donc des pannes incompréhensibles. Le mot français « *bogue* » a été choisi par homonymie approximative. Il désigne la coque épineuse de la châtaigne.
