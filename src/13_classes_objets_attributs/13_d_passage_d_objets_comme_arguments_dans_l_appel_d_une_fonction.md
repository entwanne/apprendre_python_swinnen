## 13-D - Passage d'objets comme arguments dans l'appel d'une fonction

Les fonctions peuvent utiliser des objets comme paramètres, et elles
peuvent également fournir un objet comme valeur de retour. Par exemple,
vous pouvez définir une fonction telle que celle-ci :



```python
>>> def affiche_point(p):
...    print("coord. horizontale =", p.x, "coord. verticale =", p.y)
```



Le paramètre **p** utilisé par cette fonction doit être un objet de type
**Point()**, dont l'instruction qui suit utilisera les variables
d'instance **p.x** et **p.y**. Lorsqu'on appelle cette fonction, il faut
donc lui fournir un objet de type **Point()** comme argument. Essayons
avec l'objet **p9** :



```python
>>> affiche_point(p9)
coord. horizontale = 3.0 coord. verticale = 4.0
```



Exercice

.Écrivez une fonction **distance()**
qui permette de calculer la distance entre deux points. (Il faudra vous
rappeler le théorème de Pythagore !)\
 Cette fonction attendra évidemment deux objets **Point()** comme
arguments.

