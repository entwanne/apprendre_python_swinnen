## 7-A - Les données numériques

Dans les exercices réalisés jusqu'à présent, nous avons déjà utilisé des
données de deux types : les nombres *entiers* ordinaires et les nombres
*réels* (aussi appelés nombres *à virgule flottante*). Tâchons de mettre
en évidence les caractéristiques (et les limites) de ces concepts.

### 7-A-1 - Le type integer {#article.xml#Ld0e5108 .TitreSection2}

Supposons que nous voulions modifier légèrement notre précédent exercice
sur la suite de Fibonacci, de manière à obtenir l'affichage d'un plus
grand nombre de termes. A priori, il suffit de modifier la condition de
bouclage, dans la deuxième ligne. Avec `while c <50: `, nous devrions obtenir
quarante-neuf termes. Modifions donc légèrement l'exercice, de manière à
afficher aussi le type de la variable principale :



```python
>>> a, b, c = 1, 1, 1
>>> while c <50:
     print(c, ":", b, type(b))
     a, b, c = b, a+b, c+1
...
...
...  (affichage des 43 premiers termes)
... 
44 : 1134903170 <class 'int'> 
45 : 1836311903 <class 'int'> 
46 : 2971215073 <class 'int'> 
47 : 4807526976 <class 'int'> 
48 : 7778742049 <class 'int'> 
49 : 12586269025 <class 'int'>
```



Que pouvons-nous constater ?

Il semble que Python soit capable de traiter des nombres entiers de
taille illimitée. La fonction **type()** nous permet de vérifier à
chaque itération que le type de la variable **b** reste bien en
permanence de ce type.

L'exercice que nous venons de réaliser pourrait cependant intriguer ceux
d'entre vous qui s'interrogent sur la représentation « interne » des
nombres dans un ordinateur. Vous savez probablement en effet que le «
cœur » de celui-ci est constitué par un circuit intégré électronique
(une « puce » de silicium) à très haut degré d'intégration, qui peut
effectuer plus d'un milliard d'opérations en une seule seconde, mais
seulement sur des nombres binaires de taille limitée : 32 bits
actuellement[^note_19].
Or, la gamme de valeurs décimales qu'il est possible d'encoder sous
forme de nombres binaires de 32 bits s'étend de -2147483648
à +2147483647.

Les opérations effectuées sur des entiers compris entre ces deux limites
sont donc toujours très rapides, parce que le processeur est capable de
les traiter directement. En revanche, lorsqu'il est question de traiter
des nombres entiers plus grands, ou encore des nombres réels (nombres «
à virgule flottante »), les logiciels que sont les interpréteurs et
compilateurs doivent effectuer un gros travail de codage/décodage, afin
de ne présenter en définitive au processeur que des opérations binaires
sur des nombres entiers, de 32 bits au maximum.

Vous n'avez pas à vous préoccuper de ces considérations techniques.
Lorsque vous lui demandez de traiter des entiers quelconques, Python les
transmet au processeur sous la forme de nombres binaires de 32 bits
chaque fois que cela est possible, afin d'optimiser la vitesse de calcul
et d'économiser l'espace mémoire. Lorsque les valeurs à traiter sont des
nombres entiers se situant au-delà des limites indiquées plus haut, leur
encodage dans la mémoire de l'ordinateur devient plus complexe, et leur
traitement par le processeur nécessite alors plusieurs opérations
successives, mais tout cela se fait automatiquement, sans que vous
n'ayez à vous en soucier[^note_20].

Vous pouvez donc effectuer avec Python des calculs impliquant des
valeurs entières comportant un nombre de chiffres significatifs
quelconque. Ce nombre n'est limité en effet *que par la taille de la
mémoire disponible sur l'ordinateur utilisé.* Il va de soi cependant que
les calculs impliquant de très grands nombres devront être décomposés
par l'interpréteur en calculs multiples sur des nombres plus simples, ce
qui pourra nécessiter un temps de traitement considérable dans certains
cas.

***Exemple :***



```python
>>> a, b, c = 3, 2, 1
>>> while c < 15:
     print(c, ": ", b)
     a, b, c = b, a*b, c+1
 
1 :  2
2 :  6
3 :  12
4 :  72
5 :  864
6 :  62208
7 :  53747712
8 :  3343537668096
9 :  179707499645975396352
10 :  600858794305667322270155425185792
11 :  107978831564966913814384922944738457859243070439030784
12 :  64880030544660752790736837369104977695001034284228042891827649456186234
582611607420928
13 :  70056698901118320029237641399576216921624545057972697917383692313271754
88362123506443467340026896520469610300883250624900843742470237847552
14 :  45452807645626579985636294048249351205168239870722946151401655655658398
64222761633581512382578246019698020614153674711609417355051422794795300591700
96950422693079038247634055829175296831946224503933501754776033004012758368256
>>> 
```



Dans l'exemple ci-dessus, la valeur des nombres affichés augmente très
rapidement, car chacun d'eux est égal au produit des deux termes
précédents.

Vous pouvez bien évidemment continuer cette suite mathématique plus loin
si vous voulez. La progression continue avec des nombres de plus en plus
gigantesques, mais la vitesse de calcul diminue au fur et à mesure.

Note complémentaire : les entiers de valeur comprise entre les deux
limites indiquées plus haut occupent chacun 32 bits dans la mémoire de
l'ordinateur. Les très grands entiers occupent une place variable, en
fonction de leur taille.


[^note_19]: La plupart des ordinateurs de bureau actuels contiennent un microprocesseur à registres de 32 bits (même s'il s'agit d'un modèle « dual core ». Les processeurs « 64 bits » seront cependant bientôt monnaie courante.

[^note_20]: Les précédentes versions de Python disposaient de deux types d'entiers : « integer » et « long integer », mais la conversion entre ces deux types est devenue automatique dès la version 2.2.
