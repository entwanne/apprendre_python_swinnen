## 4-J - Composition

Jusqu'ici nous avons examiné les différents éléments d'un langage de
programmation, à savoir : les *variables*, les *expressions* et les
*instructions*, mais sans traiter de la manière dont nous pouvons les
combiner les unes avec les autres.

Or l'une des grandes forces d'un langage de programmation de haut niveau
est qu'il permet de construire des instructions complexes par assemblage
de fragments divers. Ainsi par exemple, si vous savez comment
additionner deux nombres et comment afficher une valeur, vous pouvez
combiner ces deux instructions en une seule :



```python
>>> print(17 + 3)
>>> 20
```



Cela n'a l'air de rien, mais cette fonctionnalité qui paraît si évidente
va vous permettre de programmer des algorithmes complexes de façon
claire et concise. Exemple :



```python
>>> h, m, s = 15, 27, 34
>>> print("nombre de secondes écoulées depuis minuit = ", h*3600 + m*60 + s)
```



Attention, cependant : il y a une limite à ce que vous pouvez combiner
ainsi :

**Dans une expression**, ce que vous placez à la gauche du signe égale
doit toujours être une variable, et non une expression. Cela provient du
fait que le signe égale n'a pas ici la même signification qu'en
mathématique : comme nous l'avons déjà signalé, il s'agit d'un symbole
d'affectation (nous plaçons un certain contenu dans une variable) et non
un symbole d'égalité. Le symbole d'égalité (dans un test conditionnel,
par exemple) sera évoqué un peu plus loin.

Ainsi par exemple, l'instruction **m + 1 =
b** est tout à fait **illégale**.

Par contre, écrire `a = a + 1`est
inacceptable en mathématique, alors que cette forme d'écriture est très
fréquente en programmation. L'instruction `a = a + 1` signifie en l'occurrence «
augmenter la valeur de la variable a d'une unité » (ou encore : «
incrémenter a »).

Nous aurons l'occasion de revenir bientôt sur ce sujet. Mais auparavant,
il nous faut encore aborder un autre concept de grande importance.

