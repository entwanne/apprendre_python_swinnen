## 13-E - Similitude et unicité

Dans la langue parlée, les mêmes mots peuvent avoir des significations
fort différentes suivant le contexte dans lequel on les utilise. La
conséquence en est que certaines expressions utilisant ces mots peuvent
être comprises de plusieurs manières différentes (expressions ambiguës).

Le mot « même », par exemple, a des significations différentes dans les
phrases : « Charles et moi avons la même voiture » et « Charles et moi
avons la même mère ». Dans la première, ce que je veux dire est que la
voiture de Charles et la mienne sont du même modèle. Il s'agit pourtant
de deux voitures distinctes. Dans la seconde, j'indique que la mère de
Charles et la mienne constituent en fait une seule et unique personne.

Lorsque nous traitons d'objets logiciels, nous pouvons rencontrer la
même ambiguïté. Par exemple, si nous parlons de l'égalité de deux objets
**Point()**, cela signifie-t-il que ces deux objets contiennent les
mêmes données (leurs attributs), ou bien cela signifie-t-il que nous
parlons de deux références à un même et unique objet ? Considérez par
exemple les instructions suivantes :



```python
>>> p1 = Point()
>>> p1.x = 3
>>> p1.y = 4
>>> p2 = Point()
>>> p2.x = 3
>>> p2.y = 4
>>> print(p1 == p2)
False
```



Ces instructions créent deux objets **p1** et **p2** qui restent
distincts, même s'ils font partie d'une même classe et ont des contenus
similaires. La dernière instruction teste l'égalité de ces deux objets
(double signe égale), et le résultat est **False** (faux) : il n'y a
donc pas égalité.

On peut confirmer cela d'une autre manière encore :



```python
>>> print(p1)
<__main__.Point instance at 00C2CBEC>
>>> print(p2)
<__main__.Point instance at 00C50F9C>
```



L'information est claire : les deux variables **p1** et **p2**
référencent bien des objets différents, mémorisés à des emplacements
différents dans la mémoire de l'ordinateur.

Essayons autre chose, à présent :



```python
>>> p2 = p1
>>> print(p1 == p2)
True
```



Par l'instruction `p2 = p1 `, nous
assignons le contenu de **p1** à **p2**. Cela signifie que désormais ces
deux variables *référencent le même objet*. Les variables **p1** et
**p2** sont des *alias*[^note_74]
l'une de l'autre.

Le test d'égalité dans l'instruction suivante renvoie cette fois la
valeur **True**, ce qui signifie que l'expression entre parenthèses est
vraie : **p1** et **p2** désignent bien toutes deux un seul et unique
objet, comme on peut s'en convaincre en essayant encore :



```python
>>> p1.x = 7
>>> print(p2.x)
7
```



Lorsqu'on modifie l'attribut **x** de **p1**, on constate que l'attribut
**x** de **p2** a changé, lui aussi.



```python
>>> print(p1)
<__main__.Point instance at 00C2CBEC>
>>> print(p2)
<__main__.Point instance at 00C2CBEC>
```



Les deux références **p1** et **p2** pointent vers le même emplacement
dans la mémoire.


[^note_74]: Concernant ce phénomène d'aliasing, voir également page .
