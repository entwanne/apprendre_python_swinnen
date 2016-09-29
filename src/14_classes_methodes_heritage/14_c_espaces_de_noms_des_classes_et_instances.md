## 14-C - Espaces de noms des classes et instances

Vous avez appris précédemment (voir page ) que les variables définies à
l'intérieur d'une fonction sont des variables locales, inaccessibles aux
instructions qui se trouvent à l'extérieur de la fonction. Cela vous
permet d'utiliser les mêmes noms de variables dans différentes parties
d'un programme, sans risque d'interférence.

Pour décrire la même chose en d'autres termes, nous pouvons dire que
chaque fonction possède son propre *espace de noms*, indépendant de
l'espace de noms principal.

Vous avez appris également que les instructions se trouvant à
l'intérieur d'une fonction peuvent accéder aux variables définies au
niveau principal, mais *en consultation seulement* : elles peuvent
utiliser les valeurs de ces variables, mais pas les modifier (à moins de
faire appel à l'instruction **global**).

Il existe donc une sorte de hiérarchie entre les espaces de noms. Nous
allons constater la même chose à propos des classes et des objets. En
effet :

-   Chaque classe possède son propre espace de noms. Les variables qui
    en font partie sont appelées *variables de classe* ou *attributs de
    classe*.
-   Chaque objet instance (créé à partir d'une classe) obtient son
    propre espace de noms. Les variables qui en font partie sont
    appelées *variables d'instance* ou *attributs d'instance*.
-   Les classes peuvent utiliser (mais pas modifier) les variables
    définies au niveau principal.
-   Les instances peuvent utiliser (mais pas modifier) les variables
    définies au niveau de la classe et les variables définies au niveau
    principal.

Considérons par exemple la classe **Time()** définie précédemment. À la
page , nous avons instancié trois objets de cette classe :
**recreation**, **rentree** et **rendezVous**. Chacun a été initialisé
avec des valeurs différentes, indépendantes. Nous pouvons modifier et
réafficher ces valeurs à volonté dans chacun de ces trois objets, sans
que l'autre n'en soit affecté :



```python
>>> recreation.heure = 12
>>> rentree.affiche_heure()
10:30:0
>>> recreation.affiche_heure()
12:15:18
```



Veuillez à présent encoder et tester l'exemple ci-dessous :



```python
>>> class Espaces(object):		# 1
...    aa = 33			 # 2
...    def affiche(self):	      # 3
...	  print(aa, Espaces.aa, self.aa)     # 4
...
>>> aa = 12			 # 5
>>> essai = Espaces()		       # 6
>>> essai.aa = 67		   # 7
>>> essai.affiche()		     # 8
12 33 67
>>> print(aa, Espaces.aa, essai.aa)	     # 9
12 33 67
```



Dans cet exemple, le même nom **aa** est utilisé pour définir trois
variables différentes : une dans l'espace de noms de la classe (à la
ligne 2), une autre dans l'espace de noms principal (à la ligne 5), et
enfin une dernière dans l'espace de nom de l'instance (à la ligne 7).\
 La ligne 4 et la ligne 9 montrent comment vous pouvez accéder à ces
trois espaces de noms (de l'intérieur d'une classe, ou au niveau
principal), en utilisant la qualification par points. Notez encore une
fois l'utilisation de **self** pour désigner l'instance à l'intérieur de
la définition d'une classe.

