## 14-B - La méthode constructeur

L'erreur que nous avons rencontrée au paragraphe précédent est-elle
évitable ?

Elle ne se produirait effectivement pas, si nous nous étions arrangés
pour que la méthode **affiche\_heure()** puisse toujours afficher
quelque chose, sans qu'il ne soit nécessaire d'effectuer au préalable
une manipulation sur l'objet nouvellement créé. En d'autres termes, il
serait judicieux que *les variables d'instance soient prédéfinies* elles
aussi à l'intérieur de la classe, avec pour chacune d'elles une valeur «
par défaut ».

Pour obtenir cela, nous allons faire appel à une méthode particulière,
que l'on désignera par la suite sous le nom de *constructeur*. Une
méthode constructeur a ceci de particulier qu'*elle est exécutée
automatiquement* lorsque l'on instancie un nouvel objet à partir de la
classe. On peut donc y placer tout ce qui semble nécessaire pour
initialiser automatiquement l'objet que l'on crée.

Afin qu'elle soit reconnue comme telle par Python, la méthode
constructeur devra obligatoirement s'appeler **\_\_init\_\_** (deux
caractères « souligné », le mot **init**, puis encore deux caractères «
souligné »).

### 14-B-1 - Exemple {#article.xml#Ld0e39007 .TitreSection2}



```python
>>> class Time(object): 
...    "Encore une nouvelle classe temporelle" 
...    def __init__(self): 
...	  self.heure =12 
...	  self.minute =0 
...	  self.seconde =0
...    def affiche_heure(self): 
...	  print("{}:{}:{}".format(self.heure, self.minute, self.seconde)) 
```



Comme précédemment, créons un objet de cette classe et testons-en la
méthode **affiche\_heure()** :



```python
>>> tstart = Time()
>>> tstart.affiche_heure()
12:0:0
```



Nous n'obtenons plus aucune erreur, cette fois. En effet : lors de son
instanciation, l'objet **tstart** s'est vu attribuer automatiquement les
trois attributs **heure**, **minute** et **seconde** par la méthode
constructeur, avec 12 et zéro comme valeurs par défaut. Dès lors qu'un
objet de cette classe existe, on peut donc tout de suite demander
l'affichage de ces attributs.

L'intérêt de cette technique apparaîtra plus clairement si nous ajoutons
encore quelque chose.

Comme toute méthode qui se respecte, la méthode **\_\_init\_\_()** peut
être dotée de paramètres. Et dans le cas de cette méthode particulière
qu'est le constructeur, les paramètres peuvent jouer un rôle très
intéressant, parce qu'ils vont permettre d'initialiser certaines de ses
variables d'instance au moment même de l'instanciation de l'objet.

Veuillez donc reprendre l'exemple précédent, en modifiant la définition
de la méthode **\_\_init\_\_()** comme suit :



```python
...	  def __init__(self, hh =12, mm =0, ss =0): 
...	  self.heure =hh 
...	  self.minute =mm 
...	  self.seconde =ss 
```



Notre nouvelle méthode **\_\_init\_\_()** comporte à présent 3
paramètres, avec pour chacun une valeur par défaut. Nous obtenons ainsi
une classe encore plus perfectionnée. Lorsque nous instancions un objet
de cette classe, nous pouvons maintenant initialiser ses principaux
attributs à l'aide d'arguments, au sein même de l'instruction
d'instanciation. Et si nous omettons tout ou partie d'entre eux, les
attributs reçoivent de toute manière des valeurs par défaut.

Lorsque l'on écrit l'instruction d'instanciation d'un nouvel objet, et
que l'on veut lui transmettre des arguments, il suffit de placer ceux-ci
dans les parenthèses qui accompagnent le nom de la classe. On procède
donc exactement de la même manière que lorsque l'on invoque une fonction
quelconque.

Voici par exemple la création et l'initialisation simultanées d'un
nouvel objet **Time()** :



```python
>>> recreation = Time(10, 15, 18)
>>> recreation.affiche_heure()
10:15:18
```



Puisque les variables d'instance possèdent maintenant des valeurs par
défaut, nous pouvons aussi bien créer de tels objets **Time()** en
omettant un ou plusieurs arguments :



```python
>>> rentree = Time(10, 30)
>>> rentree.affiche_heure()
10:30:0
```



ou encore :



```python
>>> rendezVous = Time(hh =18)
>>> rendezVous.affiche_heure()
18:0:0
```



Exercices

.Définissez une classe **Domino()** qui permette d'instancier des objets
simulant les pièces d'un jeu de dominos. Le constructeur de cette classe
initialisera les valeurs des points présents sur les deux faces A et B
du domino (valeurs par défaut = 0).\
 Deux autres méthodes seront définies :

-   une méthode **affiche\_points()** qui affiche les points présents
    sur les deux faces ;
-   une méthode **valeur()** qui renvoie la somme des points présents
    sur les 2 faces.

Exemples d'utilisation de cette classe :

`>>> d1 = Domino(2,6)`\
`>>> d2 = Domino(4,3)`\
`>>> d1.affiche_points()`\
**face A : 2 face B : 6**\
`>>> d2.affiche_points()`\
**face A : 4 face B : 3**\
**\>\>\> print("total des points :",
d1.valeur() + d2.valeur())**\
`15`\
`>>> liste_dominos = []`\
`>>> for i in range(7):`\
**... liste\_dominos.append(Domino(6, i))**\
`>>> print(liste_dominos[3])`\
**\<\_\_main\_\_.Domino object at
0xb758b92c\>**

etc.

.Définissez une classe **CompteBancaire()**, qui permette d'instancier
des objets tels que **compte1**, **compte2**, etc. Le constructeur de
cette classe initialisera deux attributs d'instance **nom** et
**solde**, avec les valeurs par défaut 'Dupont' et 1000.\
 Trois autres méthodes seront définies :

-   **depot(somme)**permettra d'ajouter une certaine somme au solde ;
-   **retrait(somme)**permettra de retirer une certaine somme du solde ;
-   **affiche()**permettra d'afficher le nom du titulaire et le solde de
    son compte.

Exemples d'utilisation de cette classe :

**\>\>\> compte1 =
CompteBancaire('Duchmol',
800)**\
`>>> compte1.depot(350)`\
`>>> compte1.retrait(200)`\
`>>> compte1.affiche()`\
**Le solde du compte bancaire de Duchmol
est de 950 euros.**\
**\>\>\> compte2 =
CompteBancaire()**\
`>>> compte2.depot(25)`\
`>>> compte2.affiche()`\
**Le solde du compte bancaire de Dupont est
de 1025 euros.**

.Définissez une classe **Voiture()** qui permette d'instancier des
objets reproduisant le comportement de voitures automobiles. Le
constructeur de cette classe initialisera les attributs d'instance
suivants, avec les valeurs par défaut indiquées :\
**marque = 'Ford',
couleur = 'rouge',
pilote = 'personne',
vitesse = 0**.

Lorsque l'on instanciera un nouvel objet **Voiture()**, on pourra
choisir sa marque et sa couleur, mais pas sa vitesse, ni le nom de son
conducteur.\
 Les méthodes suivantes seront définies :

-   **choix\_conducteur(nom)** permettra de désigner (ou changer) le nom
    du conducteur.
-   **accelerer(taux, duree)** permettra de faire varier la vitesse de
    la voiture. La variation de vitesse obtenue sera égale au produit :
    **taux** × **duree**. Par exemple, si la voiture accélère au taux de
    1,3 m/s pendant 20 secondes, son gain de vitesse doit être égal à 26
    m/s. Des taux négatifs seront acceptés (ce qui permettra de
    décélérer). La variation de vitesse ne sera pas autorisée si le
    conducteur est 'personne'.
-   **affiche\_tout()** permettra de faire apparaître les propriétés
    présentes de la voiture, c'est-à-dire sa marque, sa couleur, le nom
    de son conducteur, sa vitesse.

Exemples d'utilisation de cette classe :

**\>\>\> a1 = Voiture('Peugeot',
'bleue')**\
**\>\>\> a2 = Voiture(couleur =
'verte')**\
**\>\>\> a3 = Voiture('Mercedes')**\
**\>\>\> a1.choix\_conducteur('Roméo')**\
**\>\>\> a2.choix\_conducteur('Juliette')**\
`>>> a2.accelerer(1.8, 12)`\
`>>> a3.accelerer(1.9, 11)`\
**Cette voiture n'a pas de
conducteur !**\
`>>> a2.affiche_tout()`\
**Ford verte pilotée par Juliette, vitesse
= 21.6 m/s.**\
`>>> a3.affiche_tout()`\
**Mercedes rouge pilotée par personne,
vitesse = 0 m/s.**

.Définissez une classe **Satellite()** qui permette d'instancier des
objets simulant des satellites artificiels lancés dans l'espace, autour
de la terre. Le constructeur de cette classe initialisera les attributs
d'instance suivants, avec les valeurs par défaut indiquées :\
**masse = 100, vitesse = 0.**\
 Lorsque l'on instanciera un nouvel objet **Satellite()**, on pourra
choisir son nom, sa masse et sa vitesse.\
 Les méthodes suivantes seront définies :

-   **impulsion(force, duree)** permettra de faire varier la vitesse du
    satellite. Pour savoir comment, rappelez-vous votre cours de
    physique : la variation de vitesse **Δv**subie par un objet de masse
    **m** soumis à l'action d'une force **F** pendant un temps **t**
    vaut ![](images/formule07.png). Par exemple : un satellite de 300 kg
    qui subit une force de 600 Newtons pendant 10 secondes voit sa
    vitesse augmenter (ou diminuer) de 20 m/s.
-   **affiche\_vitesse()** affichera le nom du satellite et sa vitesse
    courante.
-   **energie()** renverra au programme appelant la valeur de l'énergie
    cinétique du satellite.\
     Rappel : l'énergie cinétique se calcule à l'aide de la formule
    ![](images/formule08.png)

Exemples d'utilisation de cette classe :

**\>\>\> s1 = Satellite('Zoé', masse
=250, vitesse =10)**\
`>>> s1.impulsion(500, 15)`\
`>>> s1.affiche_vitesse()`\
**vitesse du satellite Zoé = 40
m/s.**\
`>>> print(s1.energie())`\
`200000`\
`>>> s1.impulsion(500, 15)`\
`>>> s1.affiche_vitesse()`\
**vitesse du satellite Zoé = 70
m/s.**\
`>>> print(s1.energie())`\
`612500`

