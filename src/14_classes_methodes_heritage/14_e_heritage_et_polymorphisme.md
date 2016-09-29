## 14-E - Héritage et polymorphisme

Analysez soigneusement le script de la page suivante. Il met en œuvre
plusieurs concepts décrits précédemment, en particulier le concept
d'héritage.

Pour bien comprendre ce script, il faut cependant d'abord vous rappeler
quelques notions élémentaires de *chimie*. Dans votre cours de chimie,
vous avez certainement dû apprendre que les *atomes* sont des entités,
constitués d'un certain nombre de *protons* (particules chargées
d'électricité positive), *d'électrons* (chargés négativement) et de
*neutrons* (neutres).

Le type d'atome (ou élément) est déterminé par le nombre de protons, que
l'on appelle également *numéroatomique*. Dans son état fondamental, un
atome contient autant d'électrons que de protons, et par conséquent il
est électriquement neutre. Il possède également un nombre variable de
neutrons, mais ceux-ci n'influencent en aucune manière la charge
électrique globale.

Dans certaines circonstances, un atome peut gagner ou perdre des
électrons. Il acquiert de ce fait une charge électrique globale, et
devient alors un *ion* (il s'agit d'un *ionnégatif* si l'atome a gagné
un ou plusieurs électrons, et d'un *ionpositif* s'il en a perdu). La
charge électrique d'un ion est égale à la différence entre le nombre de
protons et le nombre d'électrons qu'il contient.

Le script reproduit à la page suivante génère des objets **Atome()** et
des objets **Ion()**. Nous avons rappelé ci-dessus qu'un ion est
simplement un atome modifié. Dans notre programmation, la classe qui
définit les objets **Ion()** sera donc une *classe dérivée* de la classe
**Atome()** : elle héritera d'elle tous ses attributs et toutes ses
méthodes, en y ajoutant les siennes propres.

L'une de ces méthodes ajoutées (la méthode **affiche()**) remplace une
méthode de même nom héritée de la classe **Atome()**. Les classes
**Atome()** et **Ion()** possèdent donc chacune une méthode de même nom,
mais qui effectuent un travail différent. On parle dans ce cas de
*polymorphisme*. On pourra dire également que la méthode **affiche()**
de la classe **Atome()** a été *surchargée*.

Il sera évidemment possible d'instancier un nombre quelconque d'atomes
et d'ions à partir de ces deux classes. Or l'une d'entre elles, la
classe **Atome()**, doit contenir une version simplifiée du tableau
périodique des éléments (tableau de Mendeleïev), de façon à pouvoir
attribuer un nom d'élément chimique, ainsi qu'un nombre de neutrons, à
chaque objet généré. Comme il n'est pas souhaitable de recopier tout ce
tableau dans chacune des instances, nous le placerons dans un *attribut
de classe*. Ainsi ce tableau n'existera qu'en un seul endroit en
mémoire, tout en restant accessible à tous les objets qui seront
produits à partir de cette classe.

Voyons concrètement comment toutes ces idées s'articulent :



```python
class Atome: 
  """atomes simplifiés, choisis parmi les 10 premiers éléments du TP""" 
  table =[None, ('hydrogène',0),('hélium',2),('lithium',4), 
      ('béryllium',5),('bore',6),('carbone',6),('azote',7), 
      ('oxygène',8),('fluor',10),('néon',10)] 
 
  def __init__(self, nat): 
      "le n° atomique détermine le n. de protons, d'électrons et de neutrons"
      self.np, self.ne = nat, nat	 # nat = numéro atomique 
      self.nn = Atome.table[nat][1] 
 
  def affiche(self): 
      print() 
      print("Nom de l'élément :", Atome.table[self.np][0]) 
      print("%s protons, %s électrons, %s neutrons" % \ 
	 (self.np, self.ne, self.nn)) 
 
class Ion(Atome): 
  """les ions sont des atomes qui ont gagné ou perdu des électrons""" 
 
  def __init__(self, nat, charge): 
      "le n° atomique et la charge électrique déterminent l'ion" 
      Atome.__init__(self, nat) 
      self.ne = self.ne - charge 
      self.charge = charge 
 
  def affiche(self): 
      Atome.affiche(self) 
      print("Particule électrisée. Charge =", self.charge)	
 
### Programme principal : ###	 
 
a1 = Atome(5) 
a2 = Ion(3, 1) 
a3 = Ion(8, -2) 
a1.affiche() 
a2.affiche() 
a3.affiche()
```



L'exécution de ce script provoque l'affichage suivant :



```python
Nom de l'élément : bore
5 protons, 5 électrons, 6 neutrons
 
Nom de l'élément : lithium
3 protons, 2 électrons, 4 neutrons
Particule électrisée. Charge = 1
 
Nom de l'élément : oxygène
8 protons, 10 électrons, 8 neutrons
Particule électrisée. Charge = -2
```



Au niveau du programme principal, vous pouvez constater que l'on
instancie les objets **Atome()** en fournissant leur numéro atomique
(lequel doit être compris entre 1 et 10). Pour instancier des objets
**Ion()**, par contre, on doit fournir un numéro atomique et une charge
électrique globale (positive ou négative). La même méthode **affiche()**
fait apparaître les propriétés de ces objets, qu'il s'agisse d'atomes ou
d'ions, avec dans le cas de l'ion une ligne supplémentaire
(*polymorphisme*).

### 14-E-1 - Commentaires {#article.xml#Ld0e41362 .TitreSection2}

La définition de la classe **Atome()** commence par l'assignation de la
variable **table**. Une variable définie à cet endroit fait partie de
l'espace de noms de la classe. C'est donc un *attribut de classe*, dans
lequel nous plaçons une liste d'informations concernant les 10 premiers
éléments du tableau périodique de *Mendeleïev.*

Pour chacun de ces éléments, la liste contient un tuple : (nom de
l'élément, nombre de neutrons), à l'indice qui correspond au numéro
atomique. Comme il n'existe pas d'élément de numéro atomique zéro, nous
avons placé à l'indice zéro dans la liste, l'objet spécial *None*. Nous
aurions pu placer à cet endroit n'importe quelle autre valeur, puisque
cet indice ne sera pas utilisé. L'objet *None* de Python nous semble
cependant particulièrement explicite.

Viennent ensuite les définitions de deux méthodes :

-   Le constructeur **\_\_init\_\_()** sert essentiellement ici à
    générer trois *attributs d'instance*, destinés à mémoriser
    respectivement les nombres de protons, d'électrons et de neutrons
    pour chaque objet atome construit à partir de cette classe
    (rappelez-vous que les attributs d'instance sont des variables liées
    au paramètre **self**).\
     Notez au passage la technique utilisée pour obtenir le nombre de
    neutrons à partir de l'attribut de classe, en mentionnant le nom de
    la classe elle-même dans une qualification par points, comme dans
    l'instruction : **self.nn =
    Atome.table[nat][1]**.
-   La méthode **affiche()** utilise à la fois les attributs d'instance,
    pour retrouver les nombres de protons, d'électrons et de neutrons de
    l'objet courant, et l'attribut de classe (lequel est commun à tous
    les objets) pour en extraire le nom d'élément correspondant.

La définition de la classe **Ion()** inclut dans ses parenthèses le nom
de la classe **Atome()** qui précède.

Les méthodes de cette classe sont des variantes de celles de la classe
**Atome()**. Elles devront donc vraisemblablement faire appel à
celles-ci. Cette remarque est importante : comment peut-on, à
l'intérieur de la définition d'une classe, faire appel à une méthode
définie dans une autre classe ?

Il ne faut pas perdre de vue, en effet, qu'une méthode se rattache
toujours à l'instance qui sera générée à partir de la classe (instance
représentée par **self** dans la définition). Si une méthode doit faire
appel à une autre méthode définie dans une autre classe, il faut pouvoir
lui transmettre la référence de l'instance à laquelle elle doit
s'associer. Comment faire ? C'est très simple :

> Lorsque dans la définition d*'*une classe, on souhaite faire appel à
> une méthode définie dans une autre classe, il suffit de l*'*invoquer
> directement, via cette autre classe, en lui transmettant la référence
> de l*'*instance comme premier argument.

C'est ainsi que dans notre script, par exemple, la méthode **affiche()**
de la classe **Ion()** peut faire appel à la méthode **affiche()** de la
classe **Atome()** : les informations affichées seront bien celles de
l'objet-ion courant, puisque sa référence a été transmise dans
l'instruction d'appel :



```python
     Atome.affiche(self)
```



Dans cette instruction, **self** est bien entendu la référence de
l'instance courante.

De la même manière (vous en verrez de nombreux autres exemples plus
loin), la méthode constructeur de la classe **Ion()** fait appel à la
méthode constructeur de sa classe parente, dans :



```python
     Atome.__init__(self, nat)
```



Cet appel est nécessaire, afin que les objets de la classe **Ion()**
soient initialisés de la même manière que les objets de la classe
**Atome()**. Si nous n'effectuons pas cet appel, les objets-ions
n'hériteront pas automatiquement les attributs **ne**, **np** et **nn**,
car ceux ci sont des *attributs d'instance* créés par la méthode
constructeur de la classe **Atome()**, et celle-ci *n'est pas invoquée
automatiquement* lorsqu'on instancie des objets d'une classe dérivée.

Comprenez donc bien que l'héritage ne concerne que les classes, et non
les instances de ces classes. Lorsque nous disons qu'une classe dérivée
hérite toutes les propriétés de sa classe parente, cela ne signifie pas
que les propriétés des instances de la classe parente sont
automatiquement transmises aux instances de la classe fille. En
conséquence, retenez bien que :

> Dans la méthode constructeur d*'*une classe dérivée, il faut presque
> toujours prévoir un appel à la méthode constructeur de sa classe
> parente.



![](images/image35.png)



