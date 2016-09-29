## 9-H - Arguments avec étiquettes

Dans la plupart des langages de programmation, les arguments que l'on
fournit lors de l'appel d'une fonction doivent être fournis *exactement
dans le même ordre* que celui des paramètres qui leur correspondent dans
la définition de la fonction.

Python autorise cependant une souplesse beaucoup plus grande. Si les
paramètres annoncés dans la définition de la fonction ont reçu chacun
une valeur par défaut, sous la forme déjà décrite ci-dessus, on peut
faire appel à la fonction en fournissant les arguments correspondants
*dans n'importe quel ordre, à la condition de désigner nommément les
paramètres correspondants*. Exemple :



```python
>>> def oiseau(voltage=100, etat='allumé', action='danser la java'):
...    print('Ce perroquet ne pourra pas', action)
 
...    print('si vous le branchez sur', voltage, 'volts !')
...    print("L'auteur de ceci est complètement", etat)
...
 
>>> oiseau(etat='givré', voltage=250, action='vous approuver')
Ce perroquet ne pourra pas vous approuver
si vous le branchez sur 250 volts !
L'auteur de ceci est complètement givré
 
>>> oiseau()
Ce perroquet ne pourra pas danser la java
si vous le branchez sur 100 volts !
L'auteur de ceci est complètement allumé
```



Exercices

.Modifiez la fonction **volBoite(x1,x2,x3)** que vous avez définie dans
un exercice précédent, de manière à ce qu'elle puisse être appelée avec
trois, deux, un seul, ou même aucun argument. Utilisez pour ceux ci des
valeurs par défaut égales à 10.\
 Par exemple :\
`print(volBoite())`doit donner le
résultat : `1000`\
`print(volBoite(5.2))`doit donner
le résultat : `520.0`\
`print(volBoite(5.2, 3))`doit
donner le résultat : `156.0`

.Modifiez la fonction **volBoite(x1,x2,x3)** ci-dessus de manière à ce
qu'elle puisse être appelée avec un, deux, ou trois arguments. Si un
seul est utilisé, la boîte est considérée comme cubique (l'argument
étant l'arête de ce cube). Si deux sont utilisés, la boîte est
considérée comme un prisme à base carrée (auquel cas le premier argument
est le côté du carré, et le second la hauteur du prisme). Si trois
arguments sont utilisés, la boîte est considérée comme un
parallélépipède. Par exemple :\
`print(volBoite())`doit donner le
résultat :` -1` (indication d'une
erreur)\
`print(volBoite(5.2))`doit donner
le résultat :` 140.608`\
`print(volBoite(5.2, 3))`doit
donner le résultat :` 81.12`\
`print(volBoite(5.2, 3, 7.4))`doit
donner le résultat :` 115.44`

.Définissez une fonction **changeCar(ch,ca1,ca2,debut,fin)** qui
remplace tous les caractères **ca1** par des caractères **ca2** dans la
chaîne de caractères **ch**, à partir de l'indice **debut** et jusqu'à
l'indice **fin**, ces deux derniers arguments pouvant être omis (et dans
ce cas la chaîne est traitée d'une extrémité à l'autre). Exemples de
la fonctionnalité attendue :

**\>\>\> phrase = 'Ceci est une
toute petite phrase.'**\
**\>\>\> print(changeCar(phrase,
'',
'\*'))**\
`Ceci*est*une*toute*petite*phrase.`\
**\>\>\> print(changeCar(phrase,
'',
'\*', 8,
12))**\
**Ceci est\*une\*toute petite
phrase.**\
**\>\>\> print(changeCar(phrase,
'',
'\*',
12))**\
**Ceci est
une\*toute\*petite\*phrase.**\
**\>\>\> print(changeCar(phrase,
'',
'\*', fin =
12))**\
**Ceci\*est\*une\*toute petite
phrase.**

.Définissez une fonction **eleMax(liste,debut,fin)** qui renvoie
l'élément ayant la plus grande valeur dans la liste transmise. Les deux
arguments **debut** et **fin** indiqueront les indices entre lesquels
doit s'exercer la recherche, et chacun d'eux pourra être omis (comme
dans l'exercice précédent). Exemples de la fonctionnalité attendue :

**\>\>\> serie = [9, 3, 6, 1, 7, 5, 4, 8,
2]**\
`>>> print(eleMax(serie))`\
`9`\
**\>\>\> print(eleMax(serie, 2,
5))**\
`7`\
`>>> print(eleMax(serie, 2))`\
`8 `\
**\>\>\> print(eleMax(serie, fin =3, debut
=1))**\
`6`

