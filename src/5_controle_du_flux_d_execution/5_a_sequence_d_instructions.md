## 5-A - Séquence d'instructions

Sauf mention explicite, les instructions d'un programme s'exécutent les
unes après les autres, *dans l'ordre où elles ont été écrites à
l'intérieur du script*.

Cette affirmation peut vous paraître banale et évidente à première vue.
L'expérience montre cependant qu'un grand nombre d'erreurs sémantiques
dans les programmes d'ordinateur sont la conséquence d'une mauvaise
disposition des instructions. Plus vous progresserez dans l'art de la
programmation, plus vous vous rendrez compte qu'il faut être extrêmement
attentif à l'ordre dans lequel vous placez vos instructions les unes
derrière les autres. Par exemple, dans la séquence d'instructions
suivantes :



```python
>>> a, b = 3, 7
>>> a = b
>>> b = a
>>> print(a, b)
```



Vous obtiendrez un résultat contraire si vous intervertissez les 2^e^ et
3^e^ lignes.

Python exécute normalement les instructions de la première à la
dernière, sauf lorsqu'il rencontre une *instruction conditionnelle*
comme l'instruction **if** décrite ci-après (nous en rencontrerons
d'autres plus loin, notamment à propos des boucles de répétition). Une
telle instruction va permettre au programme de suivre différents chemins
suivant les circonstances.

