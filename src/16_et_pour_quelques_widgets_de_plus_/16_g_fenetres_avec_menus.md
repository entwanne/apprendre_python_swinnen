## 16-G - Fenêtres avec menus



![](images/image55.png)



Pour terminer notre petite visite guidée des widgets *tkinter*, nous
allons décrire à présent la construction d'une fenêtre d'application
dotée de différents types de menus « déroulants », chacun de ces menus
pouvant être « détaché » de l'application principale pour devenir
lui-même une petite fenêtre indépendante, comme dans l'illustration
ci-contre.

Cet exercice un peu plus long nous servira également de révision, et
nous le réaliserons par étapes, en appliquant une stratégie de
programmation que l'on appelle *développement incrémental*.

Comme nous l'avons déjà expliqué précédemment[^note_82],
cette méthode consiste à commencer l'écriture d'un programme par une
ébauche, qui ne comporte que quelques lignes seulement mais qui est déjà
fonctionnelle. On teste alors cette ébauche soigneusement afin d'en
éliminer les *bugs* éventuels. Lorsque l'ébauche fonctionne
correctement, on y ajoute une fonctionnalité supplémentaire. On teste ce
complément jusqu'à ce qu'il donne entière satisfaction, puis on en
ajoute un autre, et ainsi de suite...

*Cela ne signifie pas que vous pouvez commencer directement à
programmer* sans avoir au préalable effectué une analyse sérieuse du
projet, dont au moins les grandes lignes devront être convenablement
décrites dans un *cahier des charges* clairement rédigé.

> Il reste également impératif de commenter convenablement le code
> produit, au fur et à mesure de son élaboration. S*'*efforcer de
> rédiger de bons commentaires est en effet nécessaire, non seulement
> pour que votre code soit facile à lire (et donc à maintenir plus tard,
> par d*'*autres ou par vous-même), mais aussi pour que vous soyez
> forcés d*'*exprimer ce que vous souhaitez vraiment que la machine
> fasse (Cf. erreurs sémantiques, page .)

### 16-G-1 - Cahier des charges de l'exercice {#article.xml#Ld0e60104 .TitreSection2}

Notre application comportera simplement une barre de menus et un
canevas. Les différentes rubriques et options des menus ne serviront
qu'à faire apparaître des fragments de texte dans le canevas ou à
modifier des détails de décoration, mais ce seront avant tout des
exemples variés, destinés à donner un aperçu des nombreuses possibilités
offertes par ce type de widget, accessoire indispensable de toute
application moderne d'une certaine importance.

Nous souhaitons également que le code produit dans cet exercice soit
bien structuré. Pour ce faire, nous ferons usage de deux classes : une
classe pour l'application principale, et une autre pour la barre de
menus. Nous voulons procéder ainsi afin de bien mettre en évidence la
construction d'une application type incorporant plusieurs classes
d'objets interactifs.

### 16-G-2 - Première ébauche du programme {#article.xml#Ld0e60111 .TitreSection2}

Lorsque l'on construit l'ébauche d'un programme, il faut tâcher d'y
faire apparaître le plus tôt possible la structure d'ensemble, avec les
relations entre les principaux blocs qui constitueront l'application
définitive. C'est ce que nous nous sommes efforcés de faire dans
l'exemple ci-dessous :



1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    class MenuBar(Frame): 
    ```

4.  ``` {.LignePreCode}
      """Barre de menus déroulants""" 
    ```

5.  ``` {.LignePreCode}
      def __init__(self, boss =None): 
    ```

6.  ``` {.LignePreCode}
          Frame.__init__(self, borderwidth =2) 
    ```

7.  ``` {.LignePreCode}
      
    ```

8.  ``` {.LignePreCode}
          ##### Menu <Fichier> ##### 
    ```

9.  ``` {.LignePreCode}
          fileMenu = Menubutton(self, text ='Fichier') 
    ```

10. ``` {.LignePreCode}
          fileMenu.pack(side =LEFT) 
    ```

11. ``` {.LignePreCode}
          # Partie "déroulante" : 
    ```

12. ``` {.LignePreCode}
          me1 = Menu(fileMenu) 
    ```

13. ``` {.LignePreCode}
          me1.add_command(label ='Effacer', underline =0, 
    ```

14. ``` {.LignePreCode}
    	      command = boss.effacer) 
    ```

15. ``` {.LignePreCode}
          me1.add_command(label ='Terminer', underline =0, 
    ```

16. ``` {.LignePreCode}
    	      command = boss.quit) 
    ```

17. ``` {.LignePreCode}
          # Intégration du menu : 
    ```

18. ``` {.LignePreCode}
          fileMenu.configure(menu = me1)	 
    ```

19. ``` {.LignePreCode}
      
    ```

20. ``` {.LignePreCode}
    class Application(Frame): 
    ```

21. ``` {.LignePreCode}
      """Application principale""" 
    ```

22. ``` {.LignePreCode}
      def __init__(self, boss =None): 
    ```

23. ``` {.LignePreCode}
          Frame.__init__(self) 
    ```

24. ``` {.LignePreCode}
          self.master.title('Fenêtre avec menus') 
    ```

25. ``` {.LignePreCode}
          mBar = MenuBar(self) 
    ```

26. ``` {.LignePreCode}
          mBar.pack() 
    ```

27. ``` {.LignePreCode}
          self.can = Canvas(self, bg='light grey', height=190, 
    ```

28. ``` {.LignePreCode}
    	     width=250, borderwidth =2) 
    ```

29. ``` {.LignePreCode}
          self.can.pack() 
    ```

30. ``` {.LignePreCode}
          self.pack() 
    ```

31. ``` {.LignePreCode}
      
    ```

32. ``` {.LignePreCode}
      def effacer(self): 
    ```

33. ``` {.LignePreCode}
          self.can.delete(ALL) 
    ```

34. ``` {.LignePreCode}
      
    ```

35. ``` {.LignePreCode}
    if __name__ == '__main__': 
    ```

36. ``` {.LignePreCode}
      app = Application() 
    ```

37. ``` {.LignePreCode}
      app.mainloop() 
    ```





![](images/image56.gif)



\
 Veuillez donc encoder ces lignes et en tester l'exécution. Vous devriez
obtenir une fenêtre avec un canevas gris clair surmonté d'une barre de
menus. À ce stade, la barre de menus ne comporte encore que la seule
rubrique « Fichier ».

Cliquez sur la rubrique « Fichier » pour faire apparaître le menu
correspondant : l'option « Effacer » n'est pas encore fonctionnelle
(elle servira plus loin à effacer le contenu du canevas), mais l'option
« Terminer » devrait déjà vous permettre de fermer proprement
l'application.

Comme tous les menus gérés par *tkinter*, le menu que vous avez créé
peut être converti en menu « flottant » : il suffit de cliquer sur la
ligne pointillée apparaissant en-tête de menu. Vous obtenez ainsi une
petite fenêtre satellite, que vous pouvez alors positionner où bon vous
semble sur le bureau.

#### 16-G-2-A - Analyse du script {#article.xml#Ld0e60582 .TitreSection3}

La structure de ce petit programme devrait vous apparaître familière :
afin que les classes définies dans ce script puissent éventuellement
être (ré)utilisées dans d'autres projets par importation, comme nous
l'avons déjà expliqué précédemment[^note_83],
le corps principal du programme (lignes 35 à 37) comporte l'instruction
désormais classique :\
** if \_\_name\_\_ == '\_\_main\_\_':**

Les deux instructions qui suivent consistent seulement à instancier un
objet **app** et à faire fonctionner sa méthode **mainloop()**. Comme
vous le savez certainement, nous aurions pu également condenser ces deux
instructions en une seule.

L'essentiel du programme se trouve cependant dans les définitions de
classes qui précèdent.

La classe **MenuBar()** contient la description de la barre de menus.
Dans l'état présent du script, elle se résume à une ébauche de
constructeur.

-   Ligne 5 : Le paramètre **boss** réceptionne la référence de la
    fenêtre maîtresse du widget au moment de son instanciation. Cette
    référence va nous permettre d'invoquer les méthodes associées à
    cette fenêtre maîtresse, aux lignes 14 et 16.
-   Ligne 6 : Activation obligatoire du constructeur de la classe
    parente.
-   Ligne 9 : Instanciation d'un widget de la classe **Menubutton()**,
    défini comme un « esclave » de **self** (c'est-à-dire l'objet
    composite « barre de menus » dont nous sommes occupés à définir la
    classe). Comme l'indique son nom, ce type de widget se comporte un
    peu comme un bouton : une action se produit lorsque l'on clique
    dessus.
-   Ligne 12 : Afin que cette action consiste en l'apparition véritable
    d'un menu, il reste encore à définir celui-ci : ce sera encore un
    nouveau widget, de la classe **Menu()** cette fois, défini lui-même
    comme un « esclave » du widget **Menubutton** instancié à la ligne
    9.
-   Lignes 13 à 16 : On peut appliquer aux widgets de la classe
    **Menu()** un certain nombre de méthodes spécifiques, chacune
    d'elles acceptant de nombreuses options. Nous utilisons ici la
    méthode **add\_command()** pour installer dans le menu les deux
    items « Effacer » et « Terminer ». Nous y intégrons tout de suite
    l'option **underline**, qui sert à définir un raccourci clavier :
    cette option indique en effet lequel des caractères de l'item doit
    apparaître souligné à l'écran. L'utilisateur sait alors qu'il lui
    suffit de frapper ce caractère au clavier pour que l'action
    correspondant à cet item soit activée (comme s'il avait cliqué
    dessus à l'aide de la souris).\
     L'action à déclencher lorsque l'utilisateur sélectionne l'item est
    désignée par l'option **command**. Dans notre script, les commandes
    invoquées sont toutes les deux des méthodes de la fenêtre maîtresse,
    dont la référence aura été transmise au présent widget au moment de
    son instanciation par l'intermédiaire du paramètre **boss**. La
    méthode **effacer()**, que nous définissons nous-même plus loin,
    servira à vider le canevas. La méthode prédéfinie **quit()**
    provoque la sortie de la boucle **mainloop()** et donc l'arrêt du
    réceptionnaire d'événements associé à la fenêtre d'application.
-   Ligne 18 : Lorsque les items du menu ont été définis, il reste
    encore à reconfigurer le widget maître **Menubutton** de manière à
    ce que son option « menu » désigne effectivement le **Menu** que
    nous venons de construire. En effet, nous ne pouvions pas déjà
    préciser cette option lors de la définition initiale du widget
    **Menubutton**, puisqu'à ce stade le **Menu** n'existait pas encore.
    Nous ne pouvions pas non plus définir le widget **Menu** en premier
    lieu, puisque celui-ci doit être défini comme un « esclave » du
    widget **Menubutton.** Il faut donc bien procéder en trois étapes
    comme nous l'avons fait, en faisant appel à la méthode
    **configure()**. Cette méthode peut être appliquée à n'importe quel
    widget préexistant pour en modifier l'une ou l'autre option.

La classe **Application()** contient la description de la fenêtre
principale du programme ainsi que les méthodes gestionnaires
d'événements qui lui sont associées.

-   Ligne 20 : Nous préférons faire dériver notre application de la
    classe **Frame()**, qui présente de nombreuses options, plutôt que
    de la classe primordiale **Tk()**. De cette manière, l'application
    toute entière est encapsulée dans un widget, lequel pourra
    éventuellement être intégré par la suite dans une application plus
    importante. Rappelons que, de toute manière, tkinter instanciera
    automatiquement une fenêtre maîtresse de type **Tk()** pour contenir
    cette **Frame**.
-   Lignes 23-24 : Après l'indispensable activation du constructeur de
    la classe parente, nous utilisons l'attribut **master** que tkinter
    associe automatiquement à chaque widget, pour référencer la classe
    parente (dans le cas présent, l'objet correspondant est la fenêtre
    principale de l'application) et en redéfinir le bandeau-titre.
-   Lignes 25 à 29 : Instanciation de deux widgets esclaves pour notre
    cadre (**Frame**) principal. La « barre de menus » est évidemment le
    widget défini dans l'autre classe.
-   Ligne 30 : Comme n'importe quel autre widget, notrecadre principal
    doit être confié à une méthode de mis en place afin d'apparaître
    véritablement.
-   Lignes 32-33 : La méthode servant à effacer le canevas est définie
    dans la classe présente (puisque l'objet canevas en fait partie),
    mais elle est invoquée par l'option **command** d'un widget esclave
    défini dans une autre classe.\
     Comme nous l'avons expliqué plus haut, ce widget esclave reçoit la
    référence de son widget maître par l'intermédiaire du paramètre
    **boss**. Toutes ces références sont hiérarchisées à l'aide de la
    qualification des noms par points.

### 16-G-3 - Ajout de la rubrique Musiciens {#article.xml#Ld0e60737 .TitreSection2}

Continuez le développement de ce petit programme, en ajoutant les lignes
suivantes dans le constructeur de la classe **MenuBar()** (après la
ligne 18) :



```python
##### Menu <Musiciens> #####	      
      self.musi = Menubutton(self, text ='Musiciens')
      self.musi.pack(side =LEFT, padx ='3')
      # Partie "déroulante" du menu <Musiciens> :
      me1 = Menu(self.musi)
      me1.add_command(label ='17e siècle', underline =1,
	      foreground ='red', background ='yellow',
	      font =('Comic Sans MS', 11),
	      command = boss.showMusi17)
      me1.add_command(label ='18e siècle', underline =1,
	      foreground='royal blue', background ='white',
	      font =('Comic Sans MS', 11, 'bold'),
	      command = boss.showMusi18)
      # Intégration du menu :
      self.musi.configure(menu = me1)
```



... ainsi que les définitions de méthodes suivantes à la classe
**Application()** (après la ligne 33) :



```python
    def showMusi17(self):
      self.can.create_text(10, 10, anchor =NW, text ='H. Purcell',
	  font=('Times', 20, 'bold'), fill ='yellow')
 
  def showMusi18(self):
      self.can.create_text(245, 40, anchor =NE, text ="W. A. Mozart",
	  font =('Times', 20, 'italic'), fill ='dark green')
```





![](images/100000000000010A000000FE2BD51DF4.gif)



Lorsque vous y aurez ajouté toutes ces lignes, sauvegardez le script et
exécutez-le.

Votre barre de menus comporte à présent une rubrique supplémentaire : la
rubrique « Musiciens ».

Le menu correspondant propose deux items qui sont affichés avec des
couleurs et des polices personnalisées. Vous pourrez vous inspirer de
ces techniques décoratives pour vos projets personnels. À utiliser avec
modération !

Les commandes que nous avons associées à ces items sont évidemment
simplifiées afin de ne pas alourdir l'exercice : elles provoquent
l'affichage de petits textes sur le canevas.

#### 16-G-3-A - Analyse du script {#article.xml#Ld0e61174 .TitreSection3}

Les seules nouveautés introduites dans ces lignes concernent
l'utilisation de polices de caractères bien déterminées (option
**font**), ainsi que de couleurs pour l'avant-plan (option
**foreground**) et le fond (option **background**) des textes affichés.

Veuillez noter encore une fois l'utilisation de l'option **underline**
pour désigner les caractères correspondant à des raccourcis claviers (en
n'oubliant pas que la numérotation des caractères d'une chaîne commence
à partir de zéro), et surtout que l'option **command** de ces widgets
accède aux méthodes de l'autre classe, par l'intermédiaire de la
référence mémorisée dans l'attribut **boss**.

La méthode **create\_text()** du canevas doit être utilisée avec deux
arguments numériques, qui sont les coordonnées X et Y d'un point dans le
canevas. Le texte transmis sera positionné par rapport à ce point, en
fonction de la valeur choisie pour l'option **anchor** : celle-ci
détermine comment le fragment de texte doit être « ancré » au point
choisi dans le canevas, par son centre, par son coin supérieur gauche,
etc., en fonction d'une syntaxe qui utilise l'analogie des points
cardinaux géographiques (**NW** = angle supérieur gauche, **SE** = angle
inférieur droit, **CENTER** = centre, etc.).

### 16-G-4 - Ajout de la rubrique Peintres {#article.xml#Ld0e61216 .TitreSection2}

Cette nouvelle rubrique est construite d'une manière assez semblable à
la précédente, mais nous lui avons ajouté une fonctionnalité
supplémentaire : des menus « en cascade ». Veuillez donc ajouter les
lignes suivantes dans le constructeur de la classe **MenuBar()** :



```python
     ##### Menu <Peintres> #####
      self.pein = Menubutton(self, text ='Peintres')
      self.pein.pack(side =LEFT, padx='3')
      # Partie "déroulante" :
      me1 = Menu(self.pein)
      me1.add_command(label ='classiques', state=DISABLED)
      me1.add_command(label ='romantiques', underline =0,
	      command = boss.showRomanti)
      # Sous-menu pour les peintres impressionistes :
      me2 = Menu(me1)
      me2.add_command(label ='Claude Monet', underline =7,
	      command = boss.tabMonet)
      me2.add_command(label ='Auguste Renoir', underline =8,
	      command = boss.tabRenoir)
      me2.add_command(label ='Edgar Degas', underline =6,
	      command = boss.tabDegas)
      # Intégration du sous-menu :
      me1.add_cascade(label ='impressionistes', underline=0, menu =me2)
      # Intégration du menu :
      self.pein.configure(menu =me1)
```



... et les définitions suivantes dans la classe **Application()** :



```python
    def showRomanti(self):
      self.can.create_text(245, 70, anchor =NE, text = "E. Delacroix",
	  font =('Times', 20, 'bold italic'), fill ='blue')
 
  def tabMonet(self):
      self.can.create_text(10, 100, anchor =NW, text = 'Nymphéas à Giverny',
	  font =('Technical', 20), fill ='red')
 
  def tabRenoir(self):
      self.can.create_text(10, 130, anchor =NW,
	  text = 'Le moulin de la galette',
	  font =('Dom Casual BT', 20), fill ='maroon')
 
  def tabDegas(self):
      self.can.create_text(10, 160, anchor =NW, text = 'Danseuses au repos',
	  font =('President', 20), fill ='purple')
```



#### 16-G-4-A - Analyse du script {#article.xml#Ld0e61800 .TitreSection3}

Vous pouvez réaliser aisément des menus en cascade, en enchaînant des
sous-menus les uns aux autres jusqu'à un niveau quelconque (il vous est
cependant déconseillé d'aller au-delà de 5 niveaux successifs : vos
utilisateurs s'y perdraient).

Un sous-menu est défini comme un menu « esclave » du menu de niveau
précédent (dans notre exemple, **me2** est défini comme un menu «
esclave » de **me1**). L'intégration est assurée ensuite à l'aide de la
méthode **add\_cascade()**.

L'un des items est désactivé (option **state = DISABLED**). L'exemple
suivant vous montrera comment vous pouvez activer ou désactiver à
volonté des items, par programme.

### 16-G-5 - Ajout de la rubrique Options {#article.xml#Ld0e61821 .TitreSection2}

La définition de cette rubrique est un peu plus compliquée, parce que
nous allons y intégrer l'utilisation de variables internes à *tkinter*.

Les fonctionnalités de ce menu sont cependant beaucoup plus élaborées :
les options ajoutées permettent en effet d'activer ou de désactiver à
volonté les rubriques « Musiciens » et « Peintres », et vous pouvez
également modifier à volonté l'aspect de la barre de menus elle-même.

Veuillez donc ajouter les lignes suivantes dans le constructeur de la
classe **MenuBar()** :



```python
     ##### Menu <Options> ##### 
      optMenu = Menubutton(self, text ='Options') 
      optMenu.pack(side =LEFT, padx ='3') 
      # Variables tkinter : 
      self.relief = IntVar() 
      self.actPein = IntVar() 
      self.actMusi = IntVar()	  
      # Partie "déroulante" du menu : 
      self.mo = Menu(optMenu) 
      self.mo.add_command(label = 'Activer :', foreground ='blue') 
      self.mo.add_checkbutton(label ='musiciens', 
	 command = self.choixActifs, variable =self.actMusi) 
      self.mo.add_checkbutton(label ='peintres', 
	 command = self.choixActifs, variable =self.actPein) 
      self.mo.add_separator() 
      self.mo.add_command(label = 'Relief :', foreground ='blue') 
      for (v, lab) in [(0,'aucun'), (1,'sorti'), (2,'rentré'), 
	    (3,'sillon'), (4,'crête'), (5,'bordure')]: 
      self.mo.add_radiobutton(label =lab, variable =self.relief, 
		  value =v, command =self.reliefBarre) 
      # Intégration du menu : 
      optMenu.configure(menu = self.mo) 
```



... ainsi que les définitions de méthodes suivantes (toujours dans la
classe **MenuBar()**) :



```python
    def reliefBarre(self):
      choix = self.relief.get()
      self.configure(relief =[FLAT,RAISED,SUNKEN,GROOVE,RIDGE,SOLID][choix])
 
  def choixActifs(self):
      p = self.actPein.get()
      m = self.actMusi.get()
      self.pein.configure(state =[DISABLED, NORMAL][p])
      self.musi.configure(state =[DISABLED, NORMAL][m])
```



### 16-G-6 - Menu avec cases à cocher {#article.xml#Ld0e62264 .TitreSection2}

Notre nouveau menu déroulant comporte deux parties. Afin de bien les
mettre en évidence, nous avons inséré une ligne de séparation ainsi que
deux « faux items » (« Activer : » et « Relief : ») qui servent
simplement de titres. Nous faisons apparaître ceux-ci en couleur pour
que l'utilisateur ne les confonde pas avec de véritables commandes.

Les items de la première partie sont dotées de « cases à cocher ».
Lorsque l'utilisateur effectue un clic de souris sur l'un ou l'autre de
ces items, les options correspondantes sont activées ou désactivées, et
ces états « actif / inactif » sont affichés sous la forme d'une encoche.
Les instructions qui servent à mettre en place ce type de rubrique sont
assez explicites. Elles présentent en effet ces items comme des widgets
de type **chekbutton** :



```python
    self.mo.add_checkbutton(label = 'musiciens', command = choixActifs,
	     variable = mbu.me1.music)
```



Il est important de comprendre ici que ce type de widget comporte
nécessairement une variable interne, destinée à mémoriser l'état « actif
/ inactif » du widget. Comme nous l'avons déjà expliqué plus haut, cette
variable ne peut pas être une variable Python ordinaire, parce que les
classes de la bibliothèque *tkinter* sont écrites dans un autre langage.
Et par conséquent, on ne pourra accéder à une telle variable interne
qu'à travers un objet-interface, que nous appellerons variable *tkinter*
pour simplifier[^note_84].

C'est ainsi que dans notre exemple, nous utilisons la classe
*tkinter***IntVar()** pour créer des objets équivalents à des variables
de type entier.

-   Nous instancions donc un de ces objets-variables, que nous
    mémorisons comme attribut d'instance : `self.actMusi =IntVar()`.\
     Après cette affectation, l'objet référencé dans **self.actMusi**
    contient désormais l'équivalent d'une variable de type entier, dans
    un format spécifique à *tkinter*.
-   Il faut ensuite associer l'option **variable** de l'objet
    **checkbutton** à la variable *tkinter* ainsi définie :\
    **self.mo.add\_checkbutton(label
    ='musiciens',
    variable =self.actMusi)**.
-   Il est nécessaire de procéder ainsi en deux étapes, parce que
    *tkinter* ne peut pas directement assigner des valeurs aux variables
    Python. Pour une raison similaire, il n'est pas possible à Python de
    lire directement le contenu d'une variable *tkinter*. Il faut
    utiliser pour cela les méthodes spécifiques de cette classe d'objets
    : la méthode **get()** pour lire, et la méthode **set()** pour
    écrire :\
    `m = self.actMusi.get()`.\
     Dans cette instruction, nous affectons à **m** (variable ordinaire
    de Python) le contenu de la variable tkinter **self.actMusi**
    (laquelle est elle-même associée à un widget bien déterminé).

Tout ce qui précède peut vous paraître un peu compliqué. Considérez
simplement qu'il s'agit de votre première rencontre avec les problèmes
d'interfaçage entre deux langages de programmation différents, utilisés
ensemble dans un projet composite.

### 16-G-7 - Menu avec choix exclusifs {#article.xml#Ld0e62383 .TitreSection2}

La deuxième partie du menu « Options » permet à l'utilisateur de choisir
l'aspect que prendra la barre de menus, parmi six possibilités. Il va de
soi que l'on ne peut activer qu'une seule de ces possibilités à la fois.
Pour mettre en place ce genre de fonctionnalité, on fait classiquement
appel appel à des widgets de type « boutons radio ». La caractéristique
essentielle de ces widgets est que plusieurs d'entre eux doivent être
associés à une seule et même variable *tkinter*. À chaque bouton radio
correspond alors une valeur particulière, et c'est cette valeur qui est
affectée à la variable lorsque l'utilisateur sélectionne le bouton.

Ainsi, l'instruction :



```python
    self.mo.add_radiobutton(label ='sillon', variable =self.relief,
	     value =3, command =self.reliefBarre)
```



configure un item du menu « Options » de telle manière qu'il se comporte
comme un bouton radio.

Lorsque l'utilisateur sélectionne cet item, la valeur 3 est affectée à
la variable *tkinter***self.relief** (celle-ci étant désignée à l'aide
de l'option **variable** du widget), et un appel est lancé en direction
de la méthode **reliefBarre()**. Celle-ci récupère alors la valeur
mémorisée dans la variable tkinter pour effectuer son travail.

Dans le contexte particulier de ce menu, nous souhaitons proposer 6
possibilités différentes à l'utilisateur. Il nous faut donc six «
boutons radio », pour lesquels nous pourrions encoder six instructions
similaires à celle que nous avons reproduite ci-dessus, chacune d'elles
ne différant des cinq autres que par ses options **value** et **label**.
Dans une situation de ce genre, la bonne pratique de programmation
consiste à placer les valeurs de ces options dans une liste, et à
parcourir ensuite cette liste à l'aide d'une boucle **for**, afin
d'instancier les widgets avec une instruction commune :



```python
    for (v, lab) in [(0,'aucun'), (1,'sorti'), (2,'rentré'),
	     (3,'sillon'), (4,'crête'), (5,'bordure')]:
     self.mo.add_radiobutton(label =lab, variable =self.relief,
		 value =v, command =self.reliefBarre)
```



La liste utilisée est une liste de 6 tuples (valeur, libellé). À chacune
des 6 itérations de la boucle, un nouvel item **radiobutton** est
instancié, dont les options **label** et **value** sont extraites de la
liste par l'intermédiaire des variables **lab** et **v**.

Dans vos projets personnels, il vous arrivera fréquemment de constater
que vous pouvez ainsi remplacer des suites d'instructions similaires par
une structure de programmation plus compacte (en général, la combinaison
d'une liste et d'une boucle, comme dans l'exemple ci-dessus).

Vous découvrirez petit à petit encore d'autres techniques pour alléger
votre code : nous en fournissons un exemple dans le paragraphe suivant.
Tâchez cependant de garder à l'esprit cette règle essentielle : un bon
programme doit avant tout rester *très lisible* et *bien commenté*.

### 16-G-8 - Contrôle du flux d'exécution à l'aide d'une liste {#article.xml#Ld0e62573 .TitreSection2}

Veuillez à présent considérer la définition de la méthode
**reliefBarre()**.

À la première ligne, la méthode **get()** nous permet de récupérer
l'état d'une variable tkinter qui contient le numéro du choix opéré par
l'utilisateur dans le sous-menu « Relief : ».

À la seconde ligne, nous utilisons le contenu de la variable **choix**
pour extraire d'une liste de six éléments celui qui nous intéresse. Par
exemple, si **choix** contient la valeur 2, c'est l'option **SUNKEN**
qui sera utilisée pour reconfigurer le widget.

La variable **choix** est donc utilisée ici comme un *index*, servant à
désigner un élément de la liste. En lieu et place de cette construction
compacte, nous aurions pu programmer une série de tests conditionnels,
comme :



```python
if choix ==0:
 self.configure(relief =FLAT)
elif choix ==1:
 self.configure(relief =RAISED)
elif choix ==2:
 self.configure(relief =SUNKEN)
...
etc.
```



D'un point de vue strictement fonctionnel, le résultat serait exactement
le même. Vous admettrez cependant que la construction que nous avons
choisie est d'autant plus efficace que le nombre de possibilités de
choix est élevé. Imaginez par exemple que l'un de vos programmes
personnels doive effectuer une sélection dans un très grand nombre
d'éléments : avec une construction du type ci-dessus, vous seriez
peut-être amené à encoder plusieurs pages de **elif** !

Nous utilisons encore la même technique dans la méthode
**choixActifs()**. Ainsi l'instruction :



```python
     self.pein.configure(state =[DISABLED, NORMAL][p])
```



utilise le contenu de la variable **p** comme index pour désigner lequel
des deux états **DISABLED**, **NORMAL** doit être sélectionné pour
reconfigurer le menu « Peintres ».

Lorsqu'elle est appelée, la méthode **choixActifs()** reconfigure donc
les deux rubriques « Peintres » et « Musiciens » de la barre de menus,
pour les faire apparaître « normales » ou « désactivées » en fonction de
l'état des variables **m** et **p**, lesquelles sont elles-mêmes le
reflet de variables *tkinter*.

Ces variables intermédiaires **m** et **p** ne servent en fait qu'à
clarifier le script. Il serait en effet parfaitement possible de les
éliminer, et de rendre le script encore plus compact, en utilisant la
composition d'instructions. On pourrait par exemple remplacer les deux
instructions :



```python
     m = self.actMusi.get()
  self.musi.configure(state =[DISABLED, NORMAL][m])
```



par une seule, telle que :



```python
     self.musi.configure(state =[DISABLED, NORMAL][self.actMusi.get()])
```



Notez cependant que ce que l'on gagne en compacité peut se payer d'une
certaine perte de lisibilité.

### 16-G-9 - Pré-sélection d'une rubrique {#article.xml#Ld0e62750 .TitreSection2}

Pour terminer cet exercice, voyons encore comment vous pouvez déterminer
à l'avance certaines sélections, ou bien les modifier par programme.

Veuillez donc ajouter l'instruction suivante dans le constructeur de la
classe **Application()** (juste avant l'instruction **self.pack()**, par
exemple) :



```python
    mBar.mo.invoke(2)
```



Lorsque vous exécutez le script ainsi modifié, vous constatez qu'au
départ la rubrique « Musiciens » de la barre de menus est active, alors
que la rubrique « Peintres » ne l'est pas. Programmées comme elles le
sont, ces deux rubriques devraient être actives toutes deux par défaut.
Et c'est effectivement ce qui se passe si nous supprimons l'instruction
`mBar.mo.invoke(2)`.

Nous vous avons suggéré d'ajouter cette instruction au script pour vous
montrer comment vous pouvez effectuer par programme la même opération
que celle que l'on obtient normalement avec un clic de souris.

L'instruction ci-dessus invoque le widget **mBar.mo** en actionnant la
commande associée au deuxième item de ce widget. En consultant le
listing, vous pouvez vérifier que ce deuxième item est bien l'objet de
type **checkbutton** qui active/désactive le menu « Peintres »
(rappelons encore une fois que l'on numérote toujours à partir de zéro).

Au démarrage du programme, tout se passe donc comme si l'utilisateur
effectuait tout de suite un premier clic sur la rubrique « Peintres » du
menu « Options », ce qui a pour effet de désactiver le menu
correspondant.

Exercice

.Perfectionnez le widget « combo box simplifié » décrit à la page , de
manière à ce que la liste soit cachée au départ, et qu'un petit bouton à
droite du champ d'entrée en provoque l'apparition. Vous devrez pour ce
faire placer la liste et son ascenseur dans une fenêtre satellite sans
bordure (Cf. widget Toplevel, page ), positionner celle-ci correctement
(il vous faudra probablement consulter les sites web traitant de Tkinter
pour trouver les informations nécessaires, mais cela fait partie de
votre apprentissage !), et vous assurer que cette fenêtre disparaisse
après que l'utilisateur ait sélectionné un item dans la liste.



![](images/10000000000000EA000000771F15F883.png)




[^note_82]: Voir page : *recherche des erreurs et expérimentation*.

[^note_83]: Voir page : *modules contenant des bibliothèques de classes*.

[^note_84]: Voir également page .
