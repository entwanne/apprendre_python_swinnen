## 5-C - Opérateurs de comparaison

La condition évaluée après l'instruction if peut contenir les
*opérateurs de comparaison* suivants :



```python
x == y	      # x est égal à y
x != y	      # x est différent de y
x > y	     # x est plus grand que y
x < y	     # x est plus petit que y
x >= y	      # x est plus grand que, ou égal à y
x <= y	      # x est plus petit que, ou égal à y
```



**Exemple**



```python
>>> a = 7
>>> if (a % 2 == 0):
...    print("a est pair")
...    print("parce que le reste de sa division par 2 est nul")
... else:
...    print("a est impair")
... 
```



Notez bien que l'opérateur de comparaison pour l'égalité de deux valeurs
est constitué de deux signes « égale » et non d'un seul[^note_12].
Le signe « égale » utilisé seul est un opérateur d'affectation, et non
un opérateur de comparaison. Vous retrouverez le même symbolisme en
*C++* et en *Java.*


[^note_12]: Rappel : l'opérateur % est l'opérateur *modulo* : il calcule le reste d'une division entière. Ainsi par exemple, **a % 2** fournit le reste de la division de **a** par 2.
