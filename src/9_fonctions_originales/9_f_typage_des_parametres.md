## 9-F - Typage des paramètres

Vous avez appris que le *typage* des variables sous Python est un
*typage dynamique*, ce qui signifie que le type d'une variable est
défini au moment où on lui affecte une valeur. Ce mécanisme fonctionne
aussi pour les paramètres d'une fonction. Le type d'un paramètre devient
automatiquement le même que celui de l'argument qui a été transmis à la
fonction. Exemple :



```python
>>> def afficher3fois(arg):
...    print(arg, arg, arg)
...
 
>>> afficher3fois(5)
5 5 5
 
>>> afficher3fois('zut')
zut zut zut
 
>>> afficher3fois([5, 7])
[5, 7] [5, 7] [5, 7]
 
>>> afficher3fois(6**2)
36 36 36
```



Dans cet exemple, vous pouvez constater que la même fonction
**afficher3fois()** accepte dans tous les cas l'argument qu'on lui
transmet, que cet argument soit un nombre, une chaîne de caractères, une
liste, *ou même une expression*. Dans ce dernier cas, Python commence
par évaluer l'expression, et c'est le résultat de cette évaluation qui
est transmis comme argument à la fonction.

