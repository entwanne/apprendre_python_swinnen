## 16-F - Barres d'outils - expressions lambda

De nombreux programmes comportent une ou plusieurs « barres d'outils »
(*toolbar*) constituées de petits boutons sur lesquels sont représentés
des pictogrammes (icônes). Cette façon de faire permet de proposer à
l'utilisateur un grand nombre de commandes spécialisées, sans que
celles-ci n'occupent une place excessive à l'écran (un petit dessin vaut
mieux qu'un long discours, dit-on).



![](images/image54.png)



L'application décrite ci-après comporte une barre d'outils et un
canevas. Lorsque l'utilisateur clique sur l'un des 8 premiers boutons de
la barre, le pictogramme qu'il porte est recopié dans le canevas, à un
emplacement choisi au hasard. Lorsqu'il clique sur le dernier bouton, le
contenu du canevas est effacé.



1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
    from random import randrange 
    ```

3.  ``` {.LignePreCode}
      
    ```

4.  ``` {.LignePreCode}
    class ToolBar(Frame): 
    ```

5.  ``` {.LignePreCode}
      "Barre d'outils (petits boutons avec icônes)" 
    ```

6.  ``` {.LignePreCode}
      def __init__(self, boss, images =[], command =None, **Arguments): 
    ```

7.  ``` {.LignePreCode}
          Frame.__init__(self, boss, bd =1, **Arguments) 
    ```

8.  ``` {.LignePreCode}
          #  = liste des noms d'icônes à placer sur les boutons 
    ```

9.  ``` {.LignePreCode}
          self.command =command	     # commande à exécuter lors du clic 
    ```

10. ``` {.LignePreCode}
          nBou =len(images) 	 # Nombre de boutons à construire 
    ```

11. ``` {.LignePreCode}
          # Les icônes des boutons doivent être placées dans des variables 
    ```

12. ``` {.LignePreCode}
          # persistantes. Une liste fera l'affaire : 
    ```

13. ``` {.LignePreCode}
          self.photoI =[None]*nBou 
    ```

14. ``` {.LignePreCode}
          for b in range(nBou): 
    ```

15. ``` {.LignePreCode}
          # Création de l'icône (objet PhotoImage Tkinter) : 
    ```

16. ``` {.LignePreCode}
          self.photoI[b] =PhotoImage(file = images[b] +'.gif') 
    ```

17. ``` {.LignePreCode}
          # Création du bouton. On fait appel à une fonction lambda 
    ```

18. ``` {.LignePreCode}
          # pour pouvoir transmettre un argument à la méthode  : 
    ```

19. ``` {.LignePreCode}
          bou = Button(self, image =self.photoI[b], bd =2, relief =GROOVE, 
    ```

20. ``` {.LignePreCode}
    	    command = lambda arg =b: self.action(arg)) 
    ```

21. ``` {.LignePreCode}
          bou.pack(side =LEFT) 
    ```

22. ``` {.LignePreCode}
      
    ```

23. ``` {.LignePreCode}
      def action(self, index): 
    ```

24. ``` {.LignePreCode}
          # Exécuter  avec l'indice du bouton comme argument : 
    ```

25. ``` {.LignePreCode}
          self.command(index) 
    ```

26. ``` {.LignePreCode}
      
    ```

27. ``` {.LignePreCode}
    class Application(Frame): 
    ```

28. ``` {.LignePreCode}
      def __init__(self): 
    ```

29. ``` {.LignePreCode}
          Frame.__init__(self) 
    ```

30. ``` {.LignePreCode}
          # noms des fichiers contenant les icones (format GIF): 
    ```

31. ``` {.LignePreCode}
          icones =('floppy_2', 'coleo', 'papi2', 'pion_1', 'pion_2', 'pion_3', 
    ```

32. ``` {.LignePreCode}
    	'pion_4', 'help_4', 'clear') 
    ```

33. ``` {.LignePreCode}
          # Création de la barre d'outils : 
    ```

34. ``` {.LignePreCode}
          self.barOut =ToolBar(self, images =icones, command =self.transfert) 
    ```

35. ``` {.LignePreCode}
          self.barOut.pack(expand =YES, fill =X) 
    ```

36. ``` {.LignePreCode}
          # Création du canevas destiné à recevoir les images : 
    ```

37. ``` {.LignePreCode}
          self.ca = Canvas(self, width =400, height =200, bg ='orange') 
    ```

38. ``` {.LignePreCode}
          self.ca.pack() 
    ```

39. ``` {.LignePreCode}
          self.pack() 
    ```

40. ``` {.LignePreCode}
      
    ```

41. ``` {.LignePreCode}
      def transfert(self, b): 
    ```

42. ``` {.LignePreCode}
          if b ==8: 
    ```

43. ``` {.LignePreCode}
          self.ca.delete(ALL)	 # Effacer tout dans le canevas 
    ```

44. ``` {.LignePreCode}
          else: 
    ```

45. ``` {.LignePreCode}
          # Recopier l'icône du bouton b (extraite de la barre) => canevas : 
    ```

46. ``` {.LignePreCode}
          x, y = randrange(25,375), randrange(25,175) 
    ```

47. ``` {.LignePreCode}
          self.ca.create_image(x, y, image =self.barOut.photoI[b]) 
    ```

48. ``` {.LignePreCode}
      
    ```

49. ``` {.LignePreCode}
    Application().mainloop() 
    ```



### 16-F-1 - Métaprogrammation - expressions lambda {#article.xml#Ld0e59834 .TitreSection2}

Vous savez qu'en règle générale, on associe à chaque bouton une
*commande*, laquelle est la référence d'une méthode ou d'une fonction
particulière qui se charge d'effectuer le travail lorsque le bouton est
activé. Or, dans l'application présente, tous les boutons doivent faire
à peu près la même chose (recopier un dessin dans le canevas), la seule
différence entre eux étant le dessin concerné.

Pour simplifier notre code, nous voudrions donc pouvoir associer
l'option **command** de tous nos boutons *avec une seule et même
méthode* (ce sera la méthode **action()** ), mais en lui transmettant à
chaque fois la référence du bouton particulier utilisé, de manière à ce
que l'action accomplie puisse être différente pour chacun d'eux.

Une difficulté se présente, cependant, parce que l'option **command** du
widget Button accepte seulement une *valeur* ou une *expression*, et non
une *instruction*. Il s'agit en fait de lui indiquer la référence d'une
fonction, mais certainement pas d'invoquer la fonction à cet endroit
avec des arguments (l'invocation ne pourra avoir lieu en effet que
lorsque l'utilisateur cliquera sur le bouton : c'est alors le
réceptionnaire d'événements de *tkinter* qui devra la provoquer). C'est
la raison pour laquelle on indique seulement le nom de la fonction,
*sans parenthèses*.

On peut résoudre cette difficulté de deux manières :

-   Du fait de son caractère *dynamique*, Python accepte qu'un programme
    puisse *se modifier lui-même*, par exemple en définissant de
    nouvelles fonctions au cours de son exécution (c'est le concept de
    *métaprogrammation*).\
     Il est donc possible *de définir à la volée* une fonction avec des
    paramètres, *en indiquant pour chacun de ceux-ci une valeur par
    défaut*, et de fournir ensuite la référence de cette fonction à
    l'option **command**. Puisque la fonction est définie *en cours
    d'exécution*, ces valeurs par défaut peuvent être les contenus de
    variables. Lorsque l'événement « clic sur le bouton » provoquera
    l'appel de la fonction, celle-ci utilisera donc les valeurs par
    défaut de ses paramètres, comme s'il s'agissait d'arguments. Le
    résultat de l'opération équivaut par conséquent à un transfert
    d'arguments classique.

Pour illustrer cette technique, remplacez les lignes 17 à 20 du script
par les suivantes :

**\# Création du bouton. On définit à la
volée une fonction avec un**\
**\# paramètre dont la valeur par défaut
est l'argument à transmettre.**\
**\# Cette fonction appelle la méthode qui
nécessite un argument :**\
`def agir(arg = b):`\
`self.action(arg)`\
**\# La commande associée au bouton appelle
la fonction ci-dessus :**\
**bou = Button(self, image =
self.photoI[b], relief = GROOVE,**\
`command = agir)`

-   Voilà pour le principe. Mais tout ce qui précède peut être
    simplifié, en faisant appel à une expression **lambda**. Ce mot
    réservé Python désigne une *expression* qui renvoie un
    *objetfonction*, similaire à ceux que vous créez avec l'instruction
    **def**, mais avec la différence que **lambda** étant une expression
    et non une instruction, on peut l'utiliser comme interface afin
    d'invoquer une fonction (avec passage d'arguments) là où ce n'est
    normalement pas possible. Notez au passage qu'une telle fonction est
    *anonyme* (elle ne possède pas de nom).

Par exemple, l'expression :

**lambda ar1=b, ar2=c :
bidule(ar1,ar2)**

renvoie la référence d'une fonction anonyme créée à la volée, qui pourra
elle-même invoquer la fonction **bidule()** en lui transmettant les
arguments **b** et **c** , ceux-ci étant utilisés comme valeurs par
défaut dans la définition des paramètres **ar1** et **ar2** de la
fonction.

Cette technique utilise finalement le même principe que la précédente,
mais elle présente l'avantage d'être plus concise, raison pour laquelle
nous l'avons utilisée dans notre script. En revanche, elle est un peu
plus difficile à comprendre :

**command = lambda arg =b:
self.action(arg)**

Dans cette portion d'instruction, la commande associée au bouton se
réfère à une fonction anonyme dont le paramètre **arg** possède une
valeur par défaut : la valeur de l'argument **b**.\
 Invoquée sans argument par la commande, cette fonction anonyme peut
tout de même utiliser son paramètre **arg** (avec la valeur par défaut)
pour faire appel à la méthode cible **self.action()**, et l'on obtient
ainsi un véritable transfert d'argument vers cette méthode .

Nous ne détaillerons pas davantage ici la question des expressions
lambda, car elle déborde du cadre que nous nous sommes fixés pour cet
ouvrage d'initiation. Si vous souhaitez en savoir plus, veuillez donc
consulter l'un ou l'autre des ouvrages de référence cités dans la
bibliographie.

### 16-F-2 - Passage d'une fonction (ou d'une méthode) comme argument {#article.xml#Ld0e60003 .TitreSection2}

Vous avez déjà rencontré de nombreux widgets comportant une telle option
**command**, à laquelle il faut à chaque fois associer le nom d'une
fonction (ou d'une méthode). En termes plus généraux, cela signifie donc
qu'une fonction avec paramètres peut recevoir la référence d'une autre
fonction comme argument, et l'utilité de la chose apparaît clairement
ici.

Nous avons d'ailleurs programmé nous-même une fonctionnalité de ce genre
dans notre nouvelle classe **ToolBar()**. Vous pouvez constater que nous
avons inclus le nom **command** dans la liste de paramètres de son
constructeur, à la ligne 6. Ce paramètre attend la référence d'une
fonction ou d'une méthode comme argument. La dite référence est alors
mémorisée dans une variable d'instance (à la ligne 9), de manière à être
accessible depuis les autres méthodes de la classe. Celles-ci peuvent
dès lors invoquer la fonction ou la méthode (au besoin en lui
transmettant des arguments si nécessaire, suivant la technique expliquée
à la rubrique précédente). C'est ce que fait donc notre méthode
**action()**, à la ligne 25. En l'occurrence, la méthode ainsi transmise
est la méthode **transfert()** de la classe **Application** (cf. ligne
34).

Nous sommes parvenus ainsi à développer une classe d'objets **ToolBar**
parfaitement réutilisables dans d'autres contextes. Comme le montre
notre petite application, il suffit en effet d'instancier ces objets en
indiquant la référence d'une fonction quelconque en argument de l'option
**command**. Cette fonction sera alors automatiquement appelée elle-même
avec le numéro d'ordre du bouton cliqué par l'utilisateur.

Libre à vous d'imaginer à présent ce que la fonction devra effectuer !

Pour en terminer avec cet exemple, remarquons encore un petit détail :
chacun de nos boutons apparaît entouré d'un sillon (option `relief =GROOVE`). Vous pouvez aisément
obtenir d'autres aspects en choisissant judicieusement les options
**relief** et **bd** (*bordure*) dans l'instruction d'instanciation de
ces boutons. En particulier, vous pouvez choisir `relief =FLAT` et `bd =0` pour obtenir des petits boutons «
plats », sans aucun relief.

