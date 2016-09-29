## 5-B - Sélection ou exécution conditionnelle

Si nous voulons pouvoir écrire des applications véritablement utiles, il
nous faut des techniques permettant d'aiguiller le déroulement du
programme dans différentes directions, en fonction des circonstances
rencontrées. Pour ce faire, nous devons disposer d'instructions capables
de *tester une certaine condition* et de modifier le comportement du
programme en conséquence.

La plus simple de ces instructions conditionnelles est l'instruction
**if**. Pour expérimenter son fonctionnement, veuillez entrer dans votre
éditeur Python les deux lignes suivantes :



```python
>>> a = 150
>>> if (a > 100):
...
```



La première commande affecte la valeur 150 à la variable **a**.
Jusqu'ici rien de nouveau.\
 Lorsque vous finissez d'entrer la seconde ligne, par contre, vous
constatez que Python réagit d'une nouvelle manière. En effet, et à moins
que vous n'ayez oublié le caractère « : » à la fin de la ligne, vous
constatez que le *prompt principal* (`>>>`) est maintenant remplacé par un
*prompt secondaire* constitué de trois points[^note_11].

Si votre éditeur ne le fait pas automatiquement, vous devez à présent
effectuer une tabulation (ou entrer 4 espaces) avant d'entrer la ligne
suivante, de manière à ce que celle-ci soit *indentée* (c'est-à-dire en
retrait) par rapport à la précédente. Votre écran devrait se présenter
maintenant comme suit :



```python
>>> a = 150
>>> if (a > 100):
...    print("a dépasse la centaine")
...
```



Frappez encore une fois \<*Enter*\>. Le programme s'exécute, et vous
obtenez :



```python
a dépasse la centaine
```



Recommencez le même exercice, mais avec **a
= 20** en guise de première ligne : cette fois Python n'affiche
plus rien.

L'expression que vous avez placée entre parenthèses est ce que nous
appellerons désormais une *condition*. L'instruction **if** permet de
tester la validité de cette condition. Si la condition est vraie, alors
l'instruction que nous avons *indentée* après le « : » est exécutée. Si
la condition est fausse, rien ne se passe. Notez que les parenthèses
utilisées ici avec l'instruction if sont optionnelles : nous les avons
utilisées pour améliorer la lisibilité. Dans d'autres langages, il se
peut qu'elles soient obligatoires.

Recommencez encore, en ajoutant deux lignes comme indiqué ci-dessous.
Veillez bien à ce que la quatrième ligne débute tout à fait à gauche
(pas d'indentation), mais que la cinquième soit à nouveau indentée (de
préférence avec un retrait identique à celui de la troisième) :



```python
>>> a = 20
>>> if (a > 100):
...    print("a dépasse la centaine")
... else:
...    print("a ne dépasse pas cent")
...
```



Frappez \<*Enter*\> encore une fois. Le programme s'exécute, et affiche
cette fois :



```python
a ne dépasse pas cent
```



Comme vous l'aurez certainement déjà compris, l'instruction **else** («
sinon », en anglais) permet de programmer une exécution alternative,
dans laquelle le programme doit choisir entre deux possibilités. On peut
faire mieux encore en utilisant aussi l'instruction **elif**
(contraction de « else if ») :



```python
>>> a = 0
>>> if a > 0 :
...    print("a est positif")
... elif a < 0 :
...    print("a est négatif")
... else:
...    print("a est nul")
...
```




[^note_11]: Dans certaines versions de l'éditeur Python pour ***Windows***, le prompt secondaire n'apparaît pas.
