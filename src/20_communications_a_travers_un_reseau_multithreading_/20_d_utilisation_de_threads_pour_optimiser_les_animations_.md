## 20-D - Utilisation de threads pour optimiser les animations.

Le dernier exercice proposé à la fin de la section précédente nous
suggère une méthodologie de développements d'applications qui peut se
révéler particulièrement intéressante dans le cas de jeux vidéo
impliquant plusieurs animations simultanées.

En effet, si vous programmez les différents éléments animés d'un jeu
comme des objets indépendants fonctionnant chacun sur son propre thread,
alors non seulement vous vous simplifiez la tâche et vous améliorez la
lisibilité de votre script, mais encore vous augmentez la vitesse
d'exécution et donc la fluidité de ces animations. Pour arriver à ce
résultat, vous devrez abandonner la technique de temporisation que vous
avez exploitée jusqu'ici, mais celle que vous allez utiliser à sa place
est finalement plus simple !

### 20-D-1 - Temporisation des animations à l'aide de after() {#article.xml#Ld0e105948 .TitreSection2}

Dans toutes les animations que nous avons décrites jusqu'à présent, le «
moteur » était constitué à chaque fois par une fonction contenant la
méthode **after()**, laquelle est associée d'office à tous les widgets
tkinter. Vous savez que cette méthode permet d'introduire une
temporisation dans le déroulement de votre programme : un chronomètre
interne est activé, de telle sorte qu'après un intervalle de temps
convenu, le système invoque automatiquement une fonction quelconque. En
général, c'est la fonction contenant **after()** qui est elle-même
invoquée : on réalise ainsi une boucle récursive, dans laquelle il reste
à programmer les déplacements des divers objets graphiques.

Vous devez bien comprendre que pendant l'écoulement de l'intervalle de
temps programmé à l'aide de la méthode **after()**, votre application
n'est pas du tout « figée ». Vous pouvez par exemple, pendant ce temps,
cliquer sur un bouton, redimensionner la fenêtre, effectuer une entrée
clavier, etc. Comment cela est-il rendu possible ?

Nous avons mentionné déjà à plusieurs reprises le fait que les
applications graphiques modernes comportent toujours une sorte de moteur
qui « tourne » continuellement en tâche de fond : ce dispositif se met
en route lorsque vous activez la méthode **mainloop()** de votre fenêtre
principale. Comme son nom l'indique fort bien, cette méthode met en
œuvre une boucle répétitive perpétuelle, du même type que les boucles
**while** que vous connaissez bien. De nombreux mécanismes sont intégrés
à ce « moteur ». L'un d'entre eux consiste à réceptionner tous les
événements qui se produisent, et à les signaler ensuite à l'aide de
messages appropriés aux programmes qui en font la demande (voir :
*programmes pilotés par des événements*, page ), d'autres contrôlent les
actions à effectuer au niveau de l'affichage, etc. Lorsque vous faites
appel à la méthode **after()** d'un widget, vous utilisez en fait un
mécanisme de chronométrage qui est intégré lui aussi à **mainloop()**,
et c'est donc ce gestionnaire central qui déclenche l'appel de fonction
que vous souhaitez, après un certain intervalle de temps.

La technique d'animation utilisant la méthode **after()** est la seule
possible pour une application fonctionnant toute entière sur un seul
thread, parce que c'est la boucle **mainloop()** qui dirige l'ensemble
du comportement d'une telle application de manière absolue. C'est
notamment elle qui se charge de redessiner tout ou partie de la fenêtre
chaque fois que cela s'avère nécessaire. Pour cette raison, vous ne
pouvez pas imaginer de construire un moteur d'animation qui redéfinirait
les coordonnées d'un objet graphique à l'intérieur d'une simple boucle
**while**, par exemple, parce que pendant tout ce temps l'exécution de
**mainloop()** resterait suspendue, ce qui aurait pour conséquence que
durant cet intervalle de temps aucun objet graphique ne serait redessiné
(en particulier celui que vous souhaitez mettre en mouvement !). En
fait, toute l'application apparaîtrait figée, aussi longtemps que la
boucle **while** ne serait pas interrompue.

Puisqu'elle est la seule possible, c'est donc cette technique que nous
avons utilisée jusqu'à présent dans tous nos exemples d'applications
*mono-thread*. Elle comporte cependant un inconvénient gênant : du fait
du grand nombre d'opérations prises en charge à chaque itération de la
boucle **mainloop()**, la temporisation que l'on peut programmer à
l'aide de **after()** ne peut pas être très courte. Par exemple, elle ne
peut guère descendre en dessous de 15 ms sur un PC typique (année 2004,
processeur de type Pentium IV, f = 1,5 GHz). Vous devez tenir compte de
cette limitation si vous souhaitez développer des animations rapides.

Un autre inconvénient lié à l'utilisation de la méthode **after()**
réside dans la structure de la boucle d'animation (à savoir une fonction
ou une méthode « récursive », c'est-à-dire qui s'appelle elle-même) : il
n'est pas toujours simple en effet de bien maîtriser ce genre de
construction logique, en particulier si l'on souhaite programmer
l'animation de plusieurs objets graphiques indépendants, dont le nombre
ou les mouvements doivent varier au cours du temps.

### 20-D-2 - Temporisation des animations à l'aide de time.sleep() {#article.xml#Ld0e106014 .TitreSection2}

Vous pouvez ignorer les limitations de la méthode **after()** évoquées
ci-dessus, si vous confiez l'animation de vos objets graphiques à des
threads indépendants. En procédant ainsi, vous vous libérez de la
tutelle de **mainloop()**, et il vous est permis alors de construire des
procédures d'animation sur la base de structures de boucles plus «
classiques », utilisant l'instruction **while** ou l'instruction **for**
par exemple.

Au cœur de chacune de ces boucles, vous devez cependant toujours veiller
à insérer une temporisation pendant laquelle vous « rendez la main » au
système d'exploitation (afin qu'il puisse s'occuper des autres threads).
Pour ce faire, vous ferez appel à la fonction **sleep()** du module
**time**. Cette fonction permet de suspendre l'exécution du thread
courant pendant un certain intervalle de temps, pendant lequel les
autres threads et applications continuent à fonctionner. La
temporisation ainsi produite ne dépend pas de **mainloop()**, et par
conséquent, elle peut être beaucoup plus courte que celle que vous
autorise la méthode **after()**.

Attention : cela ne signifie pas que le rafraîchissement de l'écran sera
lui-même plus rapide, car ce rafraîchissement continue à être assuré par
**mainloop()**. Vous pourrez cependant accélérer fortement les
différents mécanismes que vous installez vous-même dans vos procédures
d'animation. Dans un logiciel de jeu, par exemple, il est fréquent
d'avoir à comparer périodiquement les positions de deux mobiles (tels
qu'un projectile et une cible), afin de pouvoir entreprendre une action
lorsqu'ils se rejoignent (explosion, ajout de points à un score, etc.).
Avec la technique d'animation décrite ici, vous pouvez effectuer
beaucoup plus souvent ces comparaisons et donc espérer un résultat plus
précis. De même, vous pouvez augmenter le nombre de points pris en
considération pour le calcul d'une trajectoire en temps réel, et donc
affiner celle-ci.

> **- Attention :** Lorsque vous utilisez la méthode after(), vous devez
> lui indiquer la temporisation souhaitée en millisecondes, sous la
> forme d'un argument entier. Lorsque vous faites appel à la fonction
> sleep(), par contre, l'argument que vous transmettez doit être exprimé
> en secondes, sous la forme d'un réel (float). Vous pouvez cependant
> utiliser des très petites valeurs (0.0003 par ex.).

### 20-D-3 - Exemple concret {#article.xml#Ld0e106054 .TitreSection2}

Le petit script reproduit ci-dessous illustre la mise en œuvre de cette
technique, dans un exemple volontairement minimaliste. Il s'agit d'une
petite application graphique dans laquelle une figure se déplace en
cercle à l'intérieur d'un canevas. Son « moteur » **mainloop()** est
lancé comme d'habitude sur le thread principal. Le constructeur de
l'application instancie un canevas contenant le dessin d'un cercle, un
bouton et un objet thread. C'est cet objet thread qui assure l'animation
du dessin, mais sans faire appel à la méthode **after()** d'un widget.
Il utilise plutôt une simple boucle **while** très classique, installée
dans sa méthode **run()**.



![](images/10000000000001AD000001DBE1C86696.png)





1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
    from math import sin, cos 
    ```

3.  ``` {.LignePreCode}
    import time, threading 
    ```

4.  ``` {.LignePreCode}
      
    ```

5.  ``` {.LignePreCode}
    class App(Frame): 
    ```

6.  ``` {.LignePreCode}
      def __init__(self): 
    ```

7.  ``` {.LignePreCode}
          Frame.__init__(self) 
    ```

8.  ``` {.LignePreCode}
          self.pack() 
    ```

9.  ``` {.LignePreCode}
          can =Canvas(self, width =400, height =400, 
    ```

10. ``` {.LignePreCode}
    	  bg ='ivory', bd =3, relief =SUNKEN) 
    ```

11. ``` {.LignePreCode}
          can.pack(padx =5, pady =5) 
    ```

12. ``` {.LignePreCode}
          cercle = can.create_oval(185, 355, 215, 385, fill ='red') 
    ```

13. ``` {.LignePreCode}
          tb = Thread_balle(can, cercle) 
    ```

14. ``` {.LignePreCode}
          Button(self, text ='Marche', command =tb.start).pack(side =LEFT) 
    ```

15. ``` {.LignePreCode}
          # Button(self, text ='Arrêt', command =tb.stop).pack(side =RIGHT) 
    ```

16. ``` {.LignePreCode}
          # arrêter l'autre thread si l'on ferme la fenêtre : 
    ```

17. ``` {.LignePreCode}
          self.bind('<Destroy>', tb.stop) 
    ```

18. ``` {.LignePreCode}
      
    ```

19. ``` {.LignePreCode}
    class Thread_balle(threading.Thread): 
    ```

20. ``` {.LignePreCode}
      def __init__(self, canevas, dessin): 
    ```

21. ``` {.LignePreCode}
          threading.Thread.__init__(self) 
    ```

22. ``` {.LignePreCode}
          self.can, self.dessin = canevas, dessin 
    ```

23. ``` {.LignePreCode}
          self.anim =1 
    ```

24. ``` {.LignePreCode}
      
    ```

25. ``` {.LignePreCode}
      def run(self): 
    ```

26. ``` {.LignePreCode}
          a = 0.0 
    ```

27. ``` {.LignePreCode}
          while self.anim == 1: 
    ```

28. ``` {.LignePreCode}
          a += .01 
    ```

29. ``` {.LignePreCode}
          x, y = 200 + 170*sin(a), 200 +170*cos(a) 
    ```

30. ``` {.LignePreCode}
          self.can.coords(self.dessin, x-15, y-15, x+15, y+15) 
    ```

31. ``` {.LignePreCode}
          time.sleep(0.010) 
    ```

32. ``` {.LignePreCode}
      
    ```

33. ``` {.LignePreCode}
      def stop(self, evt =0): 
    ```

34. ``` {.LignePreCode}
          self.anim =0 
    ```

35. ``` {.LignePreCode}
      
    ```

36. ``` {.LignePreCode}
    App().mainloop() 
    ```



#### 20-D-3-A - Commentaires {#article.xml#Ld0e106562 .TitreSection3}

-   Lignes 13-14 : Afin de simplifier notre exemple au maximum, nous
    créons l'objet thread chargé de l'animation, directement dans le
    constructeur de l'application principale. Cet objet thread ne
    démarrera cependant que lorsque l'utilisateur aura cliqué sur le
    bouton « Marche », qui active sa méthode **start()** (rappelons ici
    que c'est cette méthode intégrée qui lancera elle-même la méthode
    **run()** où nous avons installé notre boucle d'animation).
-   Ligne 15 : Vous ne pouvez par redémarrer un thread qui s'est
    terminé. De ce fait, vous ne pouvez lancer cette animation qu'une
    seule fois (tout au moins sous la forme présentée ici). Pour vous en
    convaincre, activez la ligne n^o^ 15 en enlevant le caractère **\#**
    situé au début (et qui fait que Python considère qu'il s'agit d'un
    simple commentaire) : lorsque l'animation est lancée, un clic de
    souris sur le bouton ainsi mis en place provoque la sortie de la
    boucle **while** des lignes 27-31, ce qui termine la méthode
    **run()**. L'animation s'arrête, mais le thread qui la gérait s'est
    terminé lui aussi. Si vous essayez de le relancer à l'aide du bouton
    « Marche », vous n'obtenez rien d'autre qu'un message d'erreur.
-   Lignes 26 à 31 : Pour simuler un mouvement circulaire uniforme, il
    suffit de faire varier continuellement la valeur d'un angle **a**.
    Le sinus et le cosinus de cet angle permettent alors de calculer les
    coordonnées **x** et **y** du point de la circonférence qui
    correspond à cet angle[^note_110].\
     À chaque itération, l'angle ne varie que d'un centième de radian
    seulement (environ 0,6°), et il faudra donc 628 itérations pour que
    le mobile effectue un tour complet. La temporisation choisie pour
    ces itérations se trouve à la ligne 31 : 10 millisecondes. Vous
    pouvez accélérer le mouvement en diminuant cette valeur, mais vous
    ne pourrez guère descendre en dessous de 1 milliseconde (0.001 s),
    ce qui n'est déjà pas si mal.

> - Rappel Vous pouvez vous procurer le code source de tous nos exemples
> sur le site :\
>  http://inforef.be/swi/python.htm , ou bien :\
>  http://main.pythomium.net/download/cours\_python.zip\
>  Vous y trouverez notamment, dans un fichier nommé
> **cibles\_multiples.py**, un petit programme de jeu dans lequel
> l*'*utilisateur doit tirer au canon sur une série de cibles mobiles
> qui deviennent de plus en plus rapides et nombreuses au cours du
> temps. Ce jeu utilise les techniques d*'*animation expliquées
> ci-dessus.



![](images/100000000000033B0000029F814E7AF6.png)




[^note_110]: Vous pouvez trouver quelques explications complémentaires à ce sujet à la page .
