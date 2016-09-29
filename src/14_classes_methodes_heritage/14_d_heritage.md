## 14-D - Héritage

Les classes constituent le principal outil de la programmation orientée
objet (*Object Oriented Programming ou OOP*), qui est considérée de nos
jours comme la technique de programmation la plus performante. L'un des
principaux atouts de ce type de programmation réside dans le fait que
l'on peut toujours se servir d'une classe préexistante pour en créer une
nouvelle, qui *héritera* toutes ses propriétés mais pourra modifier
certaines d'entre elles et/ou y ajouter les siennes propres. Le procédé
s'appelle *dérivation*. Il permet de créer toute une hiérarchie de
classes allant du général au particulier.

Nous pouvons par exemple définir une classe **Mammifere()**, qui
contienne un ensemble de caractéristiques propres à ce type d'animal. À
partir de cette classe *parente*, nous pouvons dériver une ou plusieurs
classes *filles*, comme : une classe **Primate()**, une classe
**Rongeur()**, une classe **Carnivore()**, etc., qui hériteront toutes
les caractéristiques de la classe **Mammifere()**, en y ajoutant leurs
spécificités.

Au départ de la classe **Carnivore()**, nous pouvons ensuite dériver une
classe **Belette()**, une classe **Loup()**, une classe **Chien()**,
etc., qui hériteront encore une fois toutes les caractéristiques de la
classe parente avant d'y ajouter les leurs. Exemple :



```python
>>> class Mammifere(object):
...    caract1 = "il allaite ses petits ;"
 
>>> class Carnivore(Mammifere):
...    caract2 = "il se nourrit de la chair de ses proies ;"
 
>>> class Chien(Carnivore):
...    caract3 = "son cri s'appelle aboiement ;"
 
>>> mirza = Chien()
>>> print(mirza.caract1, mirza.caract2, mirza.caract3)
il allaite ses petits ; il se nourrit de la chair de ses proies ;
son cri s'appelle aboiement ;
```



Dans cet exemple, nous voyons que l'objet **mirza** , qui est une
instance de la classe **Chien()**, hérite non seulement l'attribut
défini pour cette classe, mais également les attributs définis pour les
classes parentes.

Vous voyez également dans cet exemple comment il faut procéder pour
dériver une classe à partir d'une classe parente : on utilise
l'instruction **class**, suivie comme d'habitude du nom que l'on veut
attribuer à la nouvelle classe, et on place entre parenthèses le nom de
la classe parente. Les classes les plus fondamentales dérivent quant à
elles de l'objet « ancêtre » **object**.

Notez bien que les attributs utilisés dans cet exemple sont des
attributs des classes (et non des attributs d'instances). L'instance
**mirza** peut accéder à ces attributs, mais pas les modifier :



```python
>>> mirza.caract2 = "son corps est couvert de poils ;"	   # 1
>>> print(mirza.caract2)		 # 2
son corps est couvert de poils ;	     # 3
>>> fido = Chien()		       # 4
>>> print(fido.caract2) 		 # 5
il se nourrit de la chair de ses proies ;	  # 6
```



Dans ce nouvel exemple, la ligne 1 ne modifie pas l'attribut **caract2**
de la classe **Carnivore()**, contrairement à ce que l'on pourrait
penser au vu de la ligne 3. Nous pouvons le vérifier en créant une
nouvelle instance **fido** (lignes 4 à 6).

Si vous avez bien assimilé les paragraphes précédents, vous aurez
compris que l'instruction de la ligne 1 crée une nouvelle variable
d'instance associée seulement à l'objet **mirza**. Il existe donc dès ce
moment deux variables avec le même nom **caract2** : l'une dans l'espace
de noms de l'objet **mirza**, et l'autre dans l'espace de noms de la
classe **Carnivore()**.

Comment faut-il alors interpréter ce qui s'est passé aux lignes 2 et 3 ?

Comme nous l'avons vu plus haut, l'instance **mirza** peut accéder aux
variables situées dans son propre espace de noms, mais aussi à celles
qui sont situées dans les espaces de noms de toutes les classes
parentes. S'il existe des variables aux noms identiques dans plusieurs
de ces espaces, laquelle sera sélectionnée lors de l'exécution d'une
instruction comme celle de la ligne 2 ?

Pour résoudre ce conflit, Python respecte une règle de priorité fort
simple. Lorsqu'on lui demande d'utiliser la valeur d'une variable nommée
**alpha**, par exemple, il commence par rechercher ce nom dans l'espace
local (le plus « interne », en quelque sorte). Si une variable **alpha**
est trouvée dans l'espace local, c'est celle-là qui est utilisée, et la
recherche s'arrête. Sinon, Python examine l'espace de noms de la
structure parente, puis celui de la structure grand-parente, et ainsi de
suite jusqu'au niveau principal du programme.

À la ligne 2 de notre exemple, c'est donc la variable d'instance qui
sera utilisée. À la ligne 5, par contre, c'est seulement au niveau de la
classe grand-parente qu'une variable répondant au nom **caract2** peut
être trouvée. C'est donc celle-là qui est affichée.

