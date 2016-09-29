## 8-A - Affichage : la fonction print()

Nous avons bien évidemment déjà rencontré cette fonction. Précisons
simplement ici qu'elle permet d'afficher n'importe quel nombre de
valeurs fournies en arguments (c'est-à-dire entre les parenthèses). Par
défaut, ces valeurs seront séparées les unes des autres par un espace,
et le tout se terminera par un saut à la ligne.

Vous pouvez remplacer le séparateur par défaut (l'espace) par un autre
caractère quelconque (ou même par aucun caractère), grâce à l'argument «
sep ». Exemple :



```python
>>> print("Bonjour", "à", "tous", sep ="*") 
Bonjour*à*tous
 >>> print("Bonjour", "à", "tous", sep ="") 
Bonjouràtous 
```



De même, vous pouvez remplacer le saut à la ligne terminal avec
l'argument « end » :



```python
>>> n =0
>>> while n<6: 
...    print("zut", end ="") 
...    n = n+1 
... 
zutzutzutzutzut
```



