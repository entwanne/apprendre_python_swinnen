## 9-D - Utilisation des fonctions dans un script

Pour cette première approche des fonctions, nous n'avons utilisé
jusqu'ici que le mode interactif de l'interpréteur Python.

Il est bien évident que les fonctions peuvent aussi s'utiliser dans des
scripts. Veuillez donc essayer vous-même le petit programme ci-dessous,
lequel calcule le volume d'une sphère à l'aide de la formule que vous
connaissez certainement : ![](images/formule05.png)



```python
def cube(n):
 return n**3
 
def volumeSphere(r):
 return 4 * 3.1416 * cube(r) / 3
 
r = input('Entrez la valeur du rayon : ')
print('Le volume de cette sphère vaut', volumeSphere(float(r)))
```



### 9-D-1 - Notes {#article.xml#Ld0e13202 .TitreSection2}

À bien y regarder, ce programme comporte trois parties : les deux
fonctions **cube()** et **volumeSphere()**, et ensuite le corps
principal du programme.

Dans le corps principal du programme, on appelle la fonction
**volumeSphere()**, en lui transmettant la valeur entrée par
l'utilisateur pour le rayon, préalablement convertie en un nombre réel à
l'aide de la fonction intégrée **float()**.

À l'intérieur de la fonction **volumeSphere()**, il y a un appel de la
fonction **cube()**.

Notez bien que les trois parties du programme ont été disposées dans un
certain ordre : *d'abord la définition des fonctions, et ensuite le
corps principal du programme.* Cette disposition est nécessaire, parce
que l'interpréteur exécute les lignes d'instructions du programme l'une
après l'autre, dans l'ordre où elles apparaissent dans le code source.

> Dans un script, la définition des fonctions doit précéder leur
> utilisation.

Pour vous en convaincre, intervertissez cet ordre (en plaçant par
exemple le corps principal du programme au début), et prenez note du
type de message d'erreur qui est affiché lorsque vous essayez d'exécuter
le script ainsi modifié.

En fait, le corps principal d'un programme Python constitue lui-même une
entité un peu particulière, qui est toujours reconnue dans le
fonctionnement interne de l'interpréteur sous le nom réservé
**\_\_main\_\_** (le mot « main » signifie « principal », en anglais. Il
est encadré par des caractères « souligné » en double, pour éviter toute
confusion avec d'autres symboles). L'exécution d'un script commence
toujours avec la première instruction de cette entité **\_\_main\_\_**,
où qu'elle puisse se trouver dans le listing. Les instructions qui
suivent sont alors exécutées l'une après l'autre, dans l'ordre, jusqu'au
premier appel de fonction. Un appel de fonction est comme un détour dans
le flux de l'exécution : au lieu de passer à l'instruction suivante,
l'interpréteur exécute la fonction appelée, puis revient au programme
appelant pour continuer le travail interrompu. Pour que ce mécanisme
puisse fonctionner, il faut que l'interpréteur ait pu lire la définition
de la fonction avant l'entité **\_\_main\_\_**, et celle-ci sera donc
placée en général à la fin du script.

Dans notre exemple, l'entité **\_\_main\_\_** appelle une première
fonction qui elle-même en appelle une deuxième. Cette situation est très
fréquente en programmation. Si vous voulez comprendre correctement ce
qui se passe dans un programme, vous devez donc apprendre à lire un
script, non pas de la première à la dernière ligne, mais plutôt en
suivant un cheminement analogue à ce qui se passe lors de l'exécution de
ce script. Cela signifie donc concrètement que vous devrez souvent
analyser un script en commençant par ses dernières lignes !

