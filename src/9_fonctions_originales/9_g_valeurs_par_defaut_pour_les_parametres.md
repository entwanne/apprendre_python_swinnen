## 9-G - Valeurs par défaut pour les paramètres

Dans la définition d'une fonction, il est possible (et souvent
souhaitable) de définir un argument par défaut pour chacun des
paramètres. On obtient ainsi une fonction *qui peut être appelée avec
une partie seulement des arguments attendus*. Exemples :



```python
>>> def politesse(nom, vedette ='Monsieur'):
...    print("Veuillez agréer ,", vedette, nom, ", mes salutations cordiales.")
...
 
>>> politesse('Dupont')
Veuillez agréer , Monsieur Dupont , mes salutations cordiales.
>>> politesse('Durand', 'Mademoiselle')
Veuillez agréer , Mademoiselle Durand , mes salutations cordiales.
```



Lorsque l'on appelle cette fonction en ne lui fournissant que le premier
argument, le second reçoit tout de même une valeur par défaut. Si l'on
fournit les deux arguments, la valeur par défaut pour le deuxième est
tout simplement ignorée.

Vous pouvez définir une valeur par défaut pour tous les paramètres, ou
une partie d'entre eux seulement. Dans ce cas, cependant, *les
paramètres sans valeur par défaut doivent précéder les autres* dans la
liste. Par exemple, la définition ci-dessous est incorrecte :



```python
def politesse(vedette ='Monsieur', nom):
```



Autre exemple :



```python
>>> def question(annonce, essais =4, please ='Oui ou non, s.v.p.!'):
...    while essais >0:
...	 reponse = input(annonce)
...	 if reponse in ('o', 'oui','O','Oui','OUI'):
...	     return 1
...	 if reponse in ('n','non','N','Non','NON'):
...	     return 0
...	 print(please)
...	 essais = essais-1
...
>>>
```



Cette fonction peut être appelée de différentes façons, telles par
exemple :

**rep = question('Voulez-vous
vraiment terminer ? ')**

ou bien :

**rep = question('Faut-il
effacer ce fichier ? ', 3)**

ou même encore :

**rep = question('Avez-vous
compris ? ', 2, 'Répondez par
oui ou par non !')**

Prenez la peine d'essayer et de décortiquer cet exemple.

