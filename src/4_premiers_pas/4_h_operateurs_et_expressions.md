## 4-H - Opérateurs et expressions

On manipule les valeurs et les variables qui les référencent en les
combinant avec des *opérateurs* pour former des *expressions*. Exemple :



```python
a, b = 7.3, 12
y = 3*a + b/5
```



Dans cet exemple, nous commençons par affecter aux variables **a** et
**b** les valeurs **7,3** et **12**.\
 Comme déjà expliqué précédemment, Python assigne automatiquement le
type « réel » à la variable **a**, et le type « entier » à la variable
**b**.

La seconde ligne de l'exemple consiste à affecter à une nouvelle
variable **y** le résultat d'une expression qui combine les
*opérateurs***\*** , **+** et **/** avec les *opérandes***a**, **b**,
**3** et **5**. Les opérateurs sont les symboles spéciaux utilisés pour
représenter des opérations mathématiques simples, telles l'addition ou
la multiplication. Les opérandes sont les valeurs combinées à l'aide des
opérateurs.

Python évalue chaque expression qu'on lui soumet, aussi compliquée
soit-elle, et le résultat de cette évaluation est toujours lui-même une
valeur. À cette valeur, il attribue automatiquement un type, lequel
dépend de ce qu'il y a dans l'expression. Dans l'exemple ci-dessus, y
sera du type réel, parce que l'expression évaluée pour déterminer sa
valeur contient elle-même au moins un réel.

Les opérateurs Python ne sont pas seulement les quatre opérateurs
mathématiques de base. Nous avons déjà signalé l'existence de
l'opérateur de division entière //. Il faut encore ajouter l'opérateur
**\*\*** pour l'exponentiation, ainsi qu'un certain nombre d'opérateurs
logiques, des opérateurs agissant sur les chaînes de caractères, des
opérateurs effectuant des tests d'identité ou d'appartenance, etc. Nous
reparlerons de tout cela plus loin.

Signalons au passage la disponibilité de l'opérateur *modulo*,
représenté par le caractère typographique **%**. Cet opérateur fournit
*le reste de la division entière* d'un nombre par un autre. Essayez par
exemple :



```python
>>> 10 % 3	   # (et prenez note de ce qui se passe !)
>>> 10 % 5
```



Cet opérateur vous sera très utile plus loin, notamment pour tester si
un nombre **a** est divisible par un nombre **b**. Il suffira en effet
de vérifier que **a % b** donne un résultat égal à zéro.

**Exercice**

.Testez les lignes d'instructions
suivantes. Décrivez dans votre cahier ce qui se passe :\
**\>\>\> r , pi = 12, 3.14159**\
**\>\>\> s = pi \* r\*\*2 **\
**\>\>\> print(s)**\
**\>\>\> print(type(r), type(pi), type(s))**

Quelle est, à votre avis, l'utilité de la *fonction*type() ?\
 (Note : les *fonctions* seront décrites en détail aux chapitres 6 et
7.)

