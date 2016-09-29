## 12-C - Les tuples

Nous avons étudié jusqu'ici deux types de données composites : les
*chaînes*, qui sont composées de caractères, et les *listes*, qui sont
composées d'éléments de n'importe quel type. Vous devez vous rappeler
une autre différence importante entre chaînes et listes : il n'est pas
possible de changer les caractères au sein d'une chaîne existante, alors
que vous pouvez modifier les éléments d'une liste. En d'autres termes,
les listes sont des séquences modifiables, alors que les chaînes de
caractères sont des séquences non-modifiables. Exemple :



```python
>>> liste =['jambon','fromage','miel','confiture','chocolat']
>>> liste[1:3] =['salade']
>>> print(liste)
['jambon', 'salade', 'confiture', 'chocolat']
 
>>> chaine ='Roméo préfère Juliette'
>>> chaine[14:] ='Brigitte'
 
      ***** ==> Erreur: object doesn't support slice assignment  *****
```



Nous essayons de modifier la fin de la chaîne de caractères, mais cela
ne marche pas. La seule possibilité d'arriver à nos fins est de créer
une nouvelle chaîne, et d'y recopier ce que nous voulons changer :



```python
>>> chaine = chaine[:14] +'Brigitte'
>>> print(chaine)
Roméo préfère Brigitte
```



Python propose un type de données appelé ***tuple***[^note_67],
qui est assez semblable à une liste mais qui, comme les chaînes, n'est
pas modifiable.

Du point de vue de la syntaxe, un tuple est une collection d'éléments
séparés par des virgules :



```python
>>> tup = 'a', 'b', 'c', 'd', 'e'
>>> print(tup)
('a', 'b', 'c', 'd', 'e')
```



Bien que cela ne soit pas nécessaire, il est vivement conseillé de
mettre le tuple en évidence en l'enfermant dans une paire de
parenthèses, comme la fonction print() de Python le fait elle-même. Il
s'agit simplement d'améliorer la lisibilité du code, mais vous savez que
c'est important.



```python
>>> tup = ('a', 'b', 'c', 'd', 'e')
```



### 12-C-1 - Opérations sur les tuples {#article.xml#Ld0e33722 .TitreSection2}

Les opérations que l'on peut effectuer sur des tuples sont
syntaxiquement similaires à celles que l'on effectue sur les listes, si
ce n'est que les tuples ne sont pas modifiables :



```python
>>> print(tup[2:4])
('c', 'd')
>>> tup[1:3] = ('x', 'y')	  ==> ***** erreur ! *****
Traceback (most recent call last):
 File "<stdin>", line 1, in <module> 
TypeError: 'tuple' object does not support item assignment 
>>> tup = ('André',) + tup[1:]
>>> print(tup)
('André', 'b', 'c', 'd', 'e')
```



Remarquez qu'il faut toujours au moins une virgule pour définir un tuple
(le dernier exemple ci-dessus utilise un tuple contenant un seul élément
: `'André'`).

Vous pouvez déterminer la taille d'un tuple à l'aide de **len()**, le
parcourir à l'aide d'une boucle **for**, utiliser l'instruction **in**
pour savoir si un élément donné en fait partie, etc., exactement comme
vous le faites pour une liste. Les opérateurs de concaténation et de
multiplication fonctionnent aussi. Mais puisque les tuples ne sont pas
modifiables, vous ne pouvez pas utiliser avec eux, ni l'intruction
**del** ni la méthode **remove()** :



```python
>>> tu1, tu2 = ("a","b"), ("c","d","e") 
>>> tu3 = tu1*4 + tu2 
>>> tu3
('a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'c', 'd', 'e') 
>>> for e in tu3: 
...    print(e, end=":") 
... 
a:b:a:b:a:b:a:b:c:d:e: 
>>> del tu3[2]
Traceback (most recent call last):
 File "<stdin>", line 1, in <module> 
TypeError: 'tuple' object doesn't support item deletion 
```



Vous comprendrez l'utilité des tuples petit à petit. Signalons
simplement ici qu'ils sont préférables aux listes partout où l'on veut
être certain que les données transmises ne soient pas modifiées par
erreur au sein d'un programme. En outre, les tuples sont moins «
gourmands » en ressources système (ils occupent moins de place en
mémoire, et peuvent être traités plus rapidement par l'interpréteur).


[^note_67]: Ce terme n'est pas un mot anglais ordinaire : il s'agit d'un néologisme informatique.
