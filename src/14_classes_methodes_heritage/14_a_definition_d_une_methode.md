## 14-A - Définition d'une méthode

Pour illustrer notre propos, nous allons définir une nouvelle classe
**Time()**, laquelle devrait nous permettre d'effectuer toute une série
d'opérations sur des instants, des durées, etc. :



```python
>>> class Time(object): 
...    "définition d'objets temporels" 
```



Créons à présent un objet de ce type, et ajoutons-lui des variables
d'instance pour mémoriser les heures, minutes et secondes :



```python
>>> instant = Time()
>>> instant.heure = 11
>>> instant.minute = 34
>>> instant.seconde = 25
```



À titre d'exercice, écrivez maintenant vous-même une fonction
**affiche\_heure()** , qui serve à visualiser le contenu d'un objet de
classe **Time()** sous la forme conventionnelle «
heures:minutes:secondes ». Appliquée à l'objet instant créé ci-dessus,
cette fonction devrait donc afficher `11:34:25 ` :



```python
>>> affiche_heure(instant)
11:34:25
```



Votre fonction ressemblera probablement à ceci :



```python
>>> def affiche_heure(t): 
...    print(str(t.heure) +":" +str(t.minute) +":" +str(t.seconde)) 
```



... ou mieux encore, à ceci :



```python
>>> def affiche_heure(t): 
...    print("{}:{}:{}".format(t.heure, t.minute, t.seconde)) 
```



en application de la technique de formatage des chaînes décrite à la
page .

Si par la suite vous deviez utiliser fréquemment des objets de la classe
**Time()**, cette fonction d'affichage vous serait probablement fort
utile.

Il serait donc judicieux d'arriver à *encapsuler* cette fonction
**affiche\_heure()** dans la classe **Time()** elle-même, de manière à
s'assurer qu'elle soit toujours automatiquement disponible, chaque fois
que l'on aura à manipuler des objets de la classe **Time()**.

Une fonction que l'on aura ainsi encapsulée dans une classe s'appelle
préférentiellement une *méthode*.

Vous avez évidemment déjà rencontré des méthodes à de nombreuses
reprises dans les chapitres précédents de cet ouvrage, et vous savez
donc déjà qu'une méthode est bien une fonction associée à une classe
particulière d'objets. Il vous reste seulement à apprendre comment
construire une telle fonction.

### 14-A-1 - Définition concrète d'une méthode dans un script {#article.xml#Ld0e38631 .TitreSection2}

On définit une méthode comme on définit une fonction, c'est-à-dire en
écrivant un bloc d'instructions à la suite du mot réservé **def**, mais
cependant avec deux différences :

-   la définition d'une méthode est toujours placée *à l'intérieur de la
    définition d'une classe*, de manière à ce que la relation qui lie la
    méthode à la classe soit clairement établie ;
-   la définition d'une méthode doit toujours comporter au moins un
    paramètre, lequel doit être *une référence d'instance*, et ce
    paramètre particulier doit toujours être listé en premier.

Vous pourriez en principe utiliser un nom de variable quelconque pour ce
premier paramètre, mais il est vivement conseillé de respecter la
convention qui consiste à toujours lui donner le nom : **self**.

Ce paramètre **self** est nécessaire, parce qu'il faut pouvoir désigner
*l'instance à laquelle la méthode sera associée*, dans les instructions
faisant partie de sa définition. Vous comprendrez cela plus facilement
avec les exemples ci-après.

> Remarquons que la définition d*'*une méthode comporte toujours au
> moins un paramètre : self, alors que la définition d*'*une fonction
> peut n*'*en comporter aucun.

Voyons comment cela se passe en pratique :

Pour faire en sorte que la fonction **affiche\_heure()** devienne une
méthode de la classe **Time()**, il nous suffit de déplacer sa
définition à l'intérieur de celle de la classe :



```python
>>> class Time(object):
...    "Nouvelle classe temporelle"
...    def affiche_heure(t):
...	  print("{}:{}:{}".format(t.heure, t.minute, t.seconde))
```



Techniquement, c'est tout à fait suffisant, car le paramètre **t** peut
parfaitement désigner l'instance à laquelle seront attachés les
attributs **heure**, **minute** et **seconde**. Étant donné son rôle
particulier, il est cependant fortement recommandé de changer son nom en
**self** :



```python
>>> class Time(object): 
...    "Nouvelle classe temporelle" 
...    def affiche_heure(self): 
...	  print("{}:{}:{}".format(self.heure, self.minute, self.seconde)) 
```



La définition de la méthode **affiche\_heure()** fait maintenant partie
du bloc d'instructions indentées suivant l'instruction **class** (et
dont fait partie aussi la chaîne documentaire « Nouvelle classe
temporelle »).

### 14-A-2 - Essai de la méthode, dans une instance quelconque {#article.xml#Ld0e38851 .TitreSection2}

Nous disposons donc dès à présent d'une classe **Time()**, dotée d'une
méthode **affiche\_heure()**. En principe, nous devons maintenant
pouvoir créer des objets de cette classe, et leur appliquer cette
méthode. Voyons si cela fonctionne. Pour ce faire, commençons par
instancier un objet :



```python
>>> maintenant = Time()
```



Si nous essayons un peu trop vite de tester notre nouvelle méthode sur
cet objet, cela ne marche pas :



```python
>>> maintenant.affiche_heure()
AttributeError: 'Time' object has no attribute 'heure'
```



C'est normal : nous n'avons pas encore créé les attributs d'instance. Il
faudrait faire par exemple :



```python
>>> maintenant.heure = 13
>>> maintenant.minute = 34
>>> maintenant.seconde = 21
```



... et réessayer. À présent, ça marche :



```python
>>> maintenant.affiche_heure()
13:34:21
```



À plusieurs reprises, nous avons cependant déjà signalé qu'il n'est pas
recommandable de créer ainsi des attributs d'instance par assignation
directe en dehors de l'objet lui-même. Entre autres désagréments, cela
conduirait fréquemment à des erreurs comme celle que nous venons de
rencontrer. Voyons donc à présent comment nous pouvons mieux faire.

