## 6-A - Ré-affectation

Nous ne l'avions pas encore signalé explicitement : il est permis de
ré-affecter une nouvelle valeur à une même variable, autant de fois
qu'on le souhaite.

L'effet d'une ré-affectation est de remplacer l'ancienne valeur d'une
variable par une nouvelle.



```python
>>> altitude = 320
>>> print(altitude)
320
>>> altitude = 375
>>> print(altitude)
375
```



Ceci nous amène à attirer une nouvelle fois votre attention sur le fait
que le symbole *égale* utilisé sous Python pour réaliser une affectation
ne doit en aucun cas être confondu avec un symbole d'égalité tel qu'il
est compris en mathématique. Il est tentant d'interpréter l'instruction
**altitude = 320** comme une affirmation d'égalité, mais ce n'en est pas
une !

-   Premièrement, l'égalité est *commutative*, alors que l'affectation
    ne l'est pas. Ainsi, en mathématique, les écritures **a = 7** et **7
    = a**sont équivalentes, alors qu'une instruction de programmation
    telle que **375 = altitude** serait illégale.
-   Deuxièmement, l'égalité est *permanente*, alors que l'affectation
    peut être remplacée comme nous venons de le voir. Lorsqu'en
    mathématique, nous affirmons une égalité telle que a = b au début
    d'un raisonnement, alors a continue à être égal à b durant tout le
    développement qui suit.\
     En programmation, une première instruction d'affectation peut
    rendre égales les valeurs de deux variables, et une instruction
    ultérieure en changer ensuite l'une ou l'autre. Exemple :



```python
>>> a = 5
>>> b = a     # a et b contiennent des valeurs égales
>>> b = 2     # a et b sont maintenant différentes
```



Rappelons ici que Python permet d'affecter leurs valeurs à plusieurs
variables simultanément :



```python
>>> a, b, c, d = 3, 4, 5, 7
```



Cette fonctionnalité de Python est bien plus intéressante encore qu'elle
n'en a l'air à première vue. Supposons par exemple que nous voulions
maintenant échanger les valeurs des variables **a** et **c**
(actuellement, **a** contient la valeur **3**, et **c** la valeur **5**
; nous voudrions que ce soit l'inverse). Comment faire ?

Exercice

.Écrivez les lignes d'instructions nécessaires pour obtenir ce résultat.

À la suite de l'exercice proposé ci-dessus, vous aurez certainement
trouvé une méthode, et un professeur vous demanderait certainement de la
commenter en classe. Comme il s'agit d'une opération courante, les
langages de programmation proposent souvent des raccourcis pour
l'effectuer (par exemple des instructions spécialisées, telle
l'instruction SWAP du langage *Basic*). Sous Python, *l'affectation
parallèle* permet de programmer l'échange d'une manière particulièrement
élégante :



```python
>>> a, b = b, a
```



(On pourrait bien entendu échanger d'autres variables en même temps,
dans la même instruction.)

