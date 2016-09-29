## 16-C - Comment déplacer des dessins à l'aide de la souris

Le widget canevas est l'un des points forts de la bibliothèque graphique
*tkinter*. Il intègre en effet un grand nombre de dispositifs très
efficaces pour manipuler des dessins. Le script ci-après est destiné à
vous montrer quelques techniques de base. Si vous voulez en savoir plus,
notamment en ce qui concerne la manipulation de dessins composés de
plusieurs parties, veuillez consulter l'un ou l'autre ouvrage de
référence traitant de *tkinter*.

Au démarrage de notre petite application, une série de dessins sont
tracés au hasard dans un canevas (il s'agit en l'occurrence de simples
ellipses colorées). Vous pouvez déplacer n'importe lequel de ces dessins
en le « saisissant » à l'aide de votre souris.



![](images/image49.png)



Lorsqu'un dessin est déplacé, il passe à l'avant-plan par rapport aux
autres, et sa bordure apparaît plus épaisse pendant toute la durée de sa
manipulation.

Pour bien comprendre la technique utilisée, vous devez vous rappeler
qu'un logiciel utilisant une interface graphique est un logiciel «
piloté par les événements » (revoyez au besoin les explications de la
page ). Dans cette application, nous allons mettre en place un mécanisme
qui réagit aux événements : « enfoncement du bouton gauche de la souris
», « déplacement de la souris, le bouton gauche restant enfoncé », «
relâchement du bouton gauche ».

Ces événements sont générés par le système d'exploitation et pris en
charge par l'interface *tkinter*. Notre travail de programmation
consistera donc simplement à les associer à des gestionnaires différents
(fonctions ou méthodes).

Pour développer cette petite application en suivant la « philosophie
objet », nous préférerons créer une nouvelle classe **Bac\_a\_sable**,
dérivée du canevas de base, et y insérer la fonctionnalité souhaitée,
plutôt que de programmer cette fonctionnalité au niveau du corps
principal du programme, en agissant sur un canevas ordinaire. Ainsi nous
produisons du code réutilisable.



1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
    from random import randrange 
    ```

3.  ``` {.LignePreCode}
      
    ```

4.  ``` {.LignePreCode}
    class Bac_a_sable(Canvas): 
    ```

5.  ``` {.LignePreCode}
      "Canevas modifié pour prendre en compte quelques actions de la souris" 
    ```

6.  ``` {.LignePreCode}
      def __init__(self, boss, width=80, height=80, bg="white"): 
    ```

7.  ``` {.LignePreCode}
          # invocation du constructeur de la classe parente : 
    ```

8.  ``` {.LignePreCode}
          Canvas.__init__(self, boss, width=width, height=height, bg=bg) 
    ```

9.  ``` {.LignePreCode}
          # association-liaison d'événements  au présent widget : 
    ```

10. ``` {.LignePreCode}
          self.bind("<Button-1>", self.mouseDown) 
    ```

11. ``` {.LignePreCode}
          self.bind("<Button1-Motion>", self.mouseMove) 
    ```

12. ``` {.LignePreCode}
          self.bind("<Button1-ButtonRelease>", self.mouseUp) 
    ```

13. ``` {.LignePreCode}
      
    ```

14. ``` {.LignePreCode}
      def mouseDown(self, event): 
    ```

15. ``` {.LignePreCode}
          "Opération à effectuer quand le bouton gauche de la souris est enfoncé" 
    ```

16. ``` {.LignePreCode}
          self.currObject =None 
    ```

17. ``` {.LignePreCode}
          # event.x et event.y contiennent les coordonnées du clic effectué : 
    ```

18. ``` {.LignePreCode}
          self.x1, self.y1 = event.x, event.y 
    ```

19. ``` {.LignePreCode}
          # <find_closest> renvoie la référence du dessin le plus proche : 
    ```

20. ``` {.LignePreCode}
          self.selObject = self.find_closest(self.x1, self.y1) 
    ```

21. ``` {.LignePreCode}
          # modification de l'épaisseur du contour du dessin : 
    ```

22. ``` {.LignePreCode}
          self.itemconfig(self.selObject, width =3) 
    ```

23. ``` {.LignePreCode}
          #  fait passer le dessin à l'avant-plan : 
    ```

24. ``` {.LignePreCode}
          self.lift(self.selObject) 
    ```

25. ``` {.LignePreCode}
      
    ```

26. ``` {.LignePreCode}
      def mouseMove(self, event): 
    ```

27. ``` {.LignePreCode}
          "Op. à effectuer quand la souris se déplace, bouton gauche enfoncé" 
    ```

28. ``` {.LignePreCode}
          x2, y2 = event.x, event.y 
    ```

29. ``` {.LignePreCode}
          dx, dy = x2 -self.x1, y2 -self.y1 
    ```

30. ``` {.LignePreCode}
          if self.selObject: 
    ```

31. ``` {.LignePreCode}
          self.move(self.selObject, dx, dy) 
    ```

32. ``` {.LignePreCode}
          self.x1, self.y1 = x2, y2 
    ```

33. ``` {.LignePreCode}
      
    ```

34. ``` {.LignePreCode}
      def mouseUp(self, event): 
    ```

35. ``` {.LignePreCode}
          "Op. à effectuer quand le bouton gauche de la souris est relâché" 
    ```

36. ``` {.LignePreCode}
          if self.selObject: 
    ```

37. ``` {.LignePreCode}
          self.itemconfig(self.selObject, width =1) 
    ```

38. ``` {.LignePreCode}
          self.selObject =None 
    ```

39. ``` {.LignePreCode}
      
    ```

40. ``` {.LignePreCode}
    if __name__ == '__main__':    # ---- Programme de test ---- 
    ```

41. ``` {.LignePreCode}
      couleurs =('red','orange','yellow','green','cyan','blue','violet','purple') 
    ```

42. ``` {.LignePreCode}
      fen =Tk() 
    ```

43. ``` {.LignePreCode}
      # mise en place du canevas - dessin de 15 ellipses colorés : 
    ```

44. ``` {.LignePreCode}
      bac =Bac_a_sable(fen, width =400, height =300, bg ='ivory') 
    ```

45. ``` {.LignePreCode}
      bac.pack(padx =5, pady =3) 
    ```

46. ``` {.LignePreCode}
      # bouton de sortie : 
    ```

47. ``` {.LignePreCode}
      b_fin = Button(fen, text ='Terminer', bg ='royal blue', fg ='white', 
    ```

48. ``` {.LignePreCode}
    	 font =('Helvetica', 10, 'bold'), command =fen.quit) 
    ```

49. ``` {.LignePreCode}
      b_fin.pack(pady =2) 
    ```

50. ``` {.LignePreCode}
      # tracé de 15 ellipses avec couleur et coordonnées aléatoires : 
    ```

51. ``` {.LignePreCode}
      for i in range(15): 
    ```

52. ``` {.LignePreCode}
          coul =couleurs[randrange(8)] 
    ```

53. ``` {.LignePreCode}
          x1, y1 = randrange(300), randrange(200) 
    ```

54. ``` {.LignePreCode}
          x2, y2 = x1 + randrange(10, 150), y1 + randrange(10, 150) 
    ```

55. ``` {.LignePreCode}
          bac.create_oval(x1, y1, x2, y2, fill =coul) 
    ```

56. ``` {.LignePreCode}
      fen.mainloop() 
    ```



### 16-C-1 - Commentaires {#article.xml#Ld0e52123 .TitreSection2}

Le script contient essentiellement la définition d'une classe graphique
dérivée de **Canvas()**.

Cette nouvelle classe étant susceptible d'être réutilisée dans d'autres
projets, nous plaçons l'ensemble du programme de test de cette classe
dans la structure désormais classique : `if __name__ ="__main__": `Ainsi
le script peut être utilisé tel quel en tant que module à importer, pour
d'autres applications à votre gré..

Le constructeur de notre nouveau widget **Bac\_a\_sable()** attend la
référence du widget maître (*boss*) comme premier paramètre, suivant la
convention habituelle. Il fait appel au constructeur de la classe
parente, puis met en place des mécanismes locaux.

En l'occurrence, il s'agit d'associer les trois identificateurs
d'événements **\<Button-1\>,
\<Button1-Motion\>** et `<Button1-ButtonRelease>` aux noms des
trois méthodes choisies comme gestionnaires de cesévénements[^note_80].

Lorsque l'utilisateur enfonce le bouton gauche de sa souris, la méthode
**mouseDown()** est donc activée, et le système d'exploitation lui
transmet en argument un objet **event**, dont les attributs **x** et
**y** contiennent les coordonnées du curseur souris dans le canevas,
déterminées au moment du clic.

Nous mémorisons directement ces coordonnées dans les variables
d'instance **self.x1** et **self.x2**, car nous en aurons besoin par
ailleurs. Ensuite, nous utilisons la méthode **find\_closest()** du
widget canevas, qui nous renvoie la référence du dessin le plus proche.
Cette méthode bien pratique renvoie toujours une référence, même si le
clic de souris n'a pas été effectué à l'intérieur du dessin.

Le reste est facile à comprendre : la référence du dessin sélectionné
est mémorisée dans une variable d'instance, et nous pouvons faire appel
à d'autres méthodes du canevas de base pour modifier ses
caractéristiques. En l'occurrence, nous utilisons les méthodes
**itemconfig()** et **lift()** pour épaissir son contour et le faire
passer à l'avant-plan.

Le « transport » du dessin est assuré par la méthode **mouseMove()**,
invoquée à chaque fois que la souris se déplace alors que son bouton
gauche est resté enfoncé. L'objet **event** contient cette fois encore
les coordonnées du curseur souris, au terme de ce déplacement. Nous nous
en servons pour calculer les différences entre ces nouvelles coordonnées
et les précédentes, afin de pouvoir les transmettre à la méthode
**move()** du widget canevas, qui effectuera le transport proprement
dit.

Nous ne pouvons cependant faire appel à cette méthode que s'il existe
effectivement un objet sélectionné (c'est le rôle de la variable
d'instance **selObject**), et il nous faut veiller également à mémoriser
les nouvelles coordonnées acquises.

La méthode **mouseUp()** termine le travail. Lorsque le dessin
transporté est arrivé à destination, il reste à annuler la sélection et
rendre au contour son épaisseur initiale. Ceci ne peut être envisagé que
s'il existe effectivement une sélection, bien entendu.

Dans le corps du programme de test, nous instancions 15 dessins sans
nous préoccuper de conserver leurs références dans des variables. Nous
pouvons procéder ainsi parce que tkinter conserve lui-même une référence
interne pour chacun de ces objets (cf. page ; si vous travaillez avec
d'autres bibliothèques graphiques, vous devrez probablement prévoir une
mémorisation de ces références).

Les dessins sont de simples ellipses colorées. Leur couleur est choisie
au hasard dans une liste de 8 possibilités, l'indice de la couleur
choisie étant déterminé par la fonction **randrange()** importée du
module **random**.


[^note_80]: Rappel : le gestionnaire d'événements ne transmettra les messages correspondants, que si les événements indiqués sont produits dans le canevas. Des clics de souris effectués en dehors ne produiront aucun effet.
