## 11-I - Enregistrement et restitution de variables diverses

L'argument de
la méthode **write()**utilisée avec
un fichier texte doit être une chaîne de caractères. Avec ce que nous
avons appris jusqu'à présent, nous ne pouvons donc enregistrer
d'autres types de valeurs qu'en les
transformant d'abord en chaînes de caractères
(*string*). Nous pouvons réaliser
cela à l'aide de la fonction intégrée
**str()** :



```python
>>> x = 52
>>> f.write(str(x))
```



Nous verrons plus loin qu'il existe
d'autres possibilités pour convertir des valeurs
numériques en chaînes de caractères (voir à ce sujet : *Formatage
des chaînes de caractères*). Mais la
question n'est pas vraiment là. Si nous enregistrons les
valeurs numériques en les transformant d'abord en
chaînes de caractères, nous risquons de ne plus pouvoir les
re-transformer correctement en valeurs numériques lorsque nous allons
relire le fichier. Exemple :



```python
>>> a = 5
>>> b = 2.83
>>> c = 67
>>> f = open('Monfichier', 'w')
>>> f.write(str(a))
>>> f.write(str(b))
>>> f.write(str(c))
>>> f.close()
>>> f = open('Monfichier', 'r')
>>> print(f.read())
52.8367
>>> f.close()
```



Nous avons enregistré trois valeurs numériques. Mais comment
pouvons-nous les distinguer dans la chaîne de caractères résultante,
lorsque nous effectuons la lecture du fichier ? C'est impossible ! Rien
ne nous indique d'ailleurs qu'il y a là trois valeurs plutôt qu'une
seule, ou 2, ou 4…

Il existe plusieurs solutions à ce genre de
problèmes. L'une des meilleures consiste à importer un module
Python spécialisé : le module **pickle**[^note_56]. Voici comment il s'utilise
:



```python
>>> import pickle 
>>> a, b, c = 27, 12.96, [5, 4.83, "René"] 
>>> f =open('donnees_test', 'wb') 
>>> pickle.dump(a, f) 
>>> pickle.dump(b, f) 
>>> pickle.dump(c, f) 
>>> f.close()
>>> f = open('donnes_test', 'rb') 
>>> j = pickle.load(f) 
>>> k = pickle.load(f) 
>>> l = pickle.load(f) 
>>> print(j, type(j))
27 <class 'int'> 
>>> print(k, type(k))
12.96 <class 'float'> 
>>> print(l, type(l)) 
[5, 4.83, 'René'] <class 'list'>
>>> f.close()
```



Comme vous pouvez le constater dans ce court exemple, le module *pickle*
permet d'enregistrer des données avec conservation de leur type. Les
contenus des trois variables **a**, **b** et **c** sont enregistrés dans
le fichier ***donnees\_test***, et ensuite fidèlement restitués, avec
leur type, dans les variables **j**, **k** et **l**. Vous pouvez donc
mémorisera ainsi des entiers, des réels, des chaînes de caractères, des
listes, et d'autres types de données encore que nous étudierons plus
loin.

***Attention :*** les fichiers traités à l'aide des fonctions du module
*pickle* ne seront pas des des fichiers texte, mais bien des *fichiers
binaires*[^note_57].
Pour cette raison, ils doivent obligatoirement être ouverts comme tels à
l'aide de la fonction **open()**. Vous utiliserez l'argument 'wb' pour
ouvrir un fichier binaire en écriture (comme à la 3^e^ ligne de notre
exemple), et l'argument 'rb' pour ouvrir un fichier binaire en lecture
(comme à la 8^e^ ligne de notre exemple).

La fonction **dump()** du module **pickle** attend deux arguments : le
premier est la variable à enregistrer, le second est l'objet fichier
dans lequel on travaille. La fonction **pickle.load()** effectue le
travail inverse, c'est-à-dire la restitution de chaque variable avec son
type.


[^note_56]: En anglais, le terme *pickle* signifie « conserver ». Le module a été nommé ainsi parce qu'il sert effectivement à enregistrer des données en conservant leur type.

[^note_57]: Dans les versions de Python antérieures à la version 3.0, le module *pickle* s'utilisait avec des fichiers texte (mais les chaînes de caractères étaient traitées en interne avec des conventions différentes). Les fichiers de données créés avec ces différentes versions de Python ne sont donc pas directement compatibles. Des convertisseurs existent.
