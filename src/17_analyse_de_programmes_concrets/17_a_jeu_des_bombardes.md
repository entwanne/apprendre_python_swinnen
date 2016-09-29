## 17-A - Jeu des bombardes

Ce projet de jeu[^note_86]
s'inspire d'un travail similaire réalisé par des élèves de Terminale.

Il est vivement recommandé de commencer l'ébauche d'un tel projet par
une série de petits dessins et de schémas, dans lesquels seront décrits
les différents éléments graphiques à construire, ainsi qu'un maximum de
cas d'utilisations. Si vous rechignez à utiliser pour cela la bonne
vieille technologie papier/crayon (laquelle a pourtant bien fait ses
preuves), vous pouvez tirer profit d'un logiciel de dessin technique,
tel l'utilitaire *Draw* de la suite bureautique *OpenOffice.org*[^note_87]
qui nous a servi pour réaliser le schéma de la page suivante.

L'idée de départ est simple : deux joueurs s'affrontent au canon. Chacun
doit ajuster son angle de tir pour tâcher d'atteindre son adversaire,
les obus décrivant des trajectoires balistiques.

L'emplacement des canons est défini au début du jeu de manière aléatoire
(tout au moins en hauteur). Après chaque tir, les canons se déplacent
(afin d'accroître l'intérêt du jeu, l'ajustement des tirs étant ainsi
rendu plus difficile). Les coups au but sont comptabilisés.

Le dessin préliminaire que nous avons reproduit ci-dessus est l'une des
formes que peut prendre votre *travaild'analyse*. Avant de commencer le
développement d'un projet de programmation, il vous faut en effet
toujours vous efforcer d'établir un *cahierdescharges* détaillé. Cette
étude préalable est très importante. La plupart des débutants commencent
bien trop vite à écrire de nombreuses lignes de code au départ d'une
vague idée, en négligeant de rechercher la structure d'ensemble. Leur
programmation risque alors de devenir chaotique, parce qu'ils devront de
toute façon mettre en place cette structure tôt ou tard. Il
s'apercevront alors bien souvent qu'il leur faut supprimer et ré-écrire
des pans entiers d'un projet qu'ils ont conçu d'une manière
*tropmonolithique* et/ou *malparamétrée*.

-   *Tropmonolithique* : cela signifie que l'on a négligé de décomposer
    un problème complexe en plusieurs sous-problèmes plus simples. Par
    exemple, on a imbriqué plusieurs niveaux successifs d'instructions
    composées, au lieu de faire appel à des fonctions ou à des classes.
-   *Malparamétrée* : cela signifie que l'on a traité seulement un cas
    particulier, au lieu d'envisager le cas général. Par exemple, on a
    donné à un objet graphique des dimensions fixes, au lieu de prévoir
    des variables pour permettre son redimensionnement.

Vous devez donc toujours commencer le développement d'un projet par une
phase d'analyse aussi fouillée que possible, et concrétiser le résultat
de cette analyse dans un ensemble de documents (schémas, plans,
descriptions...) qui constitueront le cahier des charges. Pour les
projets de grande envergure, il existe d'ailleurs des méthodes d'analyse
très élaborées (*UML*, *Merise*...) que nous ne pouvons nous permettre
de décrire ici car elles font l'objet de livres entiers.

Cela étant dit, il faut malheureusement admettre qu'il est très
difficile (et même probablement impossible) de réaliser dès le départ
l'analyse tout à fait complète d'un projet de programmation. C'est
seulement lorsqu'il commence à fonctionner véritablement qu'un programme
révèle ses faiblesses. On constate alors qu'il reste des cas
d'utilisation ou des contraintes qui n'avaient pas été prévues au
départ. D'autre part, un projet logiciel est pratiquement toujours
destiné à évoluer : il vous arrivera fréquemment de devoir modifier le
cahier des charges au cours du développement lui-même, pas
nécessairement parce que l'analyse initiale a été mal faite, mais tout
simplement parce que l'on souhaite ajouter des fonctionnalités
supplémentaires.

En conclusion, tâchez de toujours aborder un nouveau projet de
programmation en respectant les deux consignes suivantes :

-   Décrivez votre projet en profondeur avant de commencer la rédaction
    des premières lignes de code, en vous efforçant de mettre en
    évidence les composants principaux et les relations qui les lient
    (pensez notamment à décrire les différents cas d'utilisation de
    votre programme).
-   Lorsque vous commencerez sa réalisation effective, évitez de vous
    laisser entraîner à rédiger de trop grands blocs d'instructions.
    Veillez au contraire à découper votre application en un certain
    nombre de composants *paramétrables* bien *encapsulés*, de telle
    manière que vous puissiez aisément modifier l'un ou l'autre d'entre
    eux sans compromettre le fonctionnement des autres, et peut-être
    même les réutiliser dans différents contextes si le besoin s'en fait
    sentir.

*C'est pour satisfaire cette exigence que la programmation orientée
objets est a été inventée.*

Considérons par exemple l'ébauche dessinée à la page précédente.

L'apprenti programmeur sera peut-être tenté de commencer la réalisation
de ce jeu en n'utilisant que la seule programmation procédurale
(c'est-à-dire en omettant de définir de nouvelles classes). C'est
d'ailleurs ainsi que nous avons procédé nous-même lors de notre première
approche des interfaces graphiques, tout au long du chapitre 8. Cette
façon de procéder ne se justifie cependant que pour de tout petits
programmes (des exercices ou des tests préliminaires). Lorsque l'on
s'attaque à un projet d'une certaine importance, la complexité des
problèmes qui se présentent se révèle rapidement trop importante, et il
devient alors indispensable de fragmenter et de compartimenter.

L'outil logiciel qui va permettre cette fragmentation est la *classe*.

Nous pouvons peut-être mieux comprendre son utilité en nous aidant d'une
analogie.

Tous les appareils électroniques sont constitués d'un petit nombre de
composants de base, à savoir des transistors, des diodes, des
résistances, des condensateurs, etc. Les premiers ordinateurs ont été
construits directement à partir de ces composants. Ils étaient
volumineux, très chers, et pourtant ils n'avaient que très peu de
fonctionnalités et tombaient fréquemment en panne.

On a alors développé différentes techniques pour encapsuler dans un même
boîtier un certain nombre de composants électroniques de base. Pour
utiliser ces nouveaux *circuits intégrés*, il n'était plus nécessaire de
connaître leur contenu exact : seule importait leur fonction globale.
Les premières fonctions intégrées étaient encore relativement simples :
c'étaient par exemple des portes logiques, des bascules, etc. En
combinant ces circuits entre eux, on obtenait des caractéristiques plus
élaborées, telles que des registres ou des décodeurs, qui purent à leur
tour être intégrés, et ainsi de suite, jusqu'aux microprocesseurs
actuels. Ceux-ci contiennent dorénavant plusieurs millions de
composants, et pourtant leur fiabilité reste extrêmement élevée.

En conséquence, pour l'électronicien moderne qui veut construire par
exemple un compteur binaire (circuit qui nécessite un certain nombre de
bascules), il est évidemment bien plus simple, plus rapide et plus sûr
de se servir de bascules intégrées, plutôt que de s'échiner à combiner
sans erreur plusieurs centaines de transistors et de résistances.

D'une manière analogue, le programmeur moderne que vous êtes peut
bénéficier du travail accumulé par ses prédécesseurs en utilisant la
fonctionnalité intégrée dans les nombreuses bibliothèques de classes
déjà disponibles pour Python. Mieux encore, il peut aisément créer
lui-même de nouvelles classes pour encapsuler les principaux composants
de son application, particulièrement ceux qui y apparaissent en
plusieurs exemplaires. Procéder ainsi est plus simple, plus rapide et
plus sûr que de multiplier les blocs d'instructions similaires dans un
corps de programme monolithique, de plus en plus volumineux et de moins
en moins compréhensible.

Examinons à présent notre ébauche dessinée. Les composants les plus
importants de ce jeu sont bien évidemment les petits canons, qu'il
faudra pouvoir dessiner à différents emplacements et dans différentes
orientations, et dont il nous faudra au moins deux exemplaires.

Plutôt que de les dessiner morceau par morceau dans le canevas au fur et
à mesure du déroulement du jeu, nous avons intérêt à les considérer
comme des objets logiciels à part entière, dotés de plusieurs propriétés
ainsi que d'un certain comportement (ce que nous voulons exprimer par là
est le fait qu'il devront être dotés de divers mécanismes, que nous
pourrons activer par programme à l'aide de *méthodes* particulières). Il
est donc certainement judicieux de leur consacrer une classe spécifique.

### 17-A-1 - Prototypage d'une classe Canon {#article.xml#Ld0e62922 .TitreSection2}

En définissant une telle classe, nous gagnons sur plusieurs tableaux.
Non seulement nous rassemblons ainsi tout le code correspondant au
dessin et au fonctionnement du canon dans une même « capsule », bien à
l'écart du reste du programme, mais de surcroît nous nous donnons la
possibilité d'instancier aisément un nombre quelconque de ces canons
dans le jeu, ce qui nous ouvre des perspectives de développements
ultérieurs.

Lorsqu'une première implémentation de la classe **Canon()** aura été
construite et testée, il sera également possible de la perfectionner en
la dotant de caractéristiques supplémentaires, sans modifier (ou très
peu) son interface, c'est-à-dire en quelque sorte son « mode d'emploi »
: à savoir les instructions nécessaires pour l'instancier et l'utiliser
dans des applications diverses.

Entrons à présent dans le vif du sujet.



![Canon](images/canon.png)



Le dessin de notre canon peut être simplifié à l'extrême. Nous avons
estimé qu'il pouvait se résumer à un cercle combiné avec un rectangle,
celui-ci pouvant d'ailleurs être lui-même considéré comme un simple
segment de ligne droite particulièrement épais.

Si l'ensemble est rempli d'une couleur uniforme (en noir, par exemple),
nous obtiendrons ainsi une sorte de petite bombarde suffisamment
crédible.

Dans la suite du raisonnement, nous admettrons que la position du canon
est en fait la position du centre du cercle (coordonnées x et y dans le
dessin ci-contre). Ce point clé indique également l'axe de rotation de
la buse du canon, ainsi que l'une des extrémités de la ligne épaisse qui
représentera cette buse.

Pour terminer notre dessin, il nous restera alors à déterminer les
coordonnées de l'autre extrémité de cette ligne. Ces coordonnées peuvent
être calculées sans grande difficulté, à la condition de nous remémorer
deux concepts fondamentaux de la trigonométrie (le sinus et le cosinus)
que vous devez certainement bien connaître :



*Dans un triangle rectangle, le rapport entre le coté opposé à un angle
et l'hypoténuse du triangle est une propriété spécifique de cet angle
qu'on appelle sinus de l'angle. Le cosinus du même angle est le rapport
entre le côté adjacent à l'angle et l'hypoténuse.*

Ainsi, dans le schéma ci-contre : ![](images/latex-sinus.png) et
![](images/latex-cosinus.png).







Pour représenter la buse de notre canon, en supposant que nous
connaissions sa longueur l et l'angle de tir α , il nous faut donc
tracer un segment de ligne droite épaisse, à partir des coordonnées du
centre du cercle (x et y), jusqu'à un autre point situé plus à droite et
plus haut, l'écart horizontal Δx étant égal à l.cos α , et l'écart
vertical Δy étant égal à l.sin α .

En résumant tout ce qui précède, dessiner un canon au point x, y
consistera simplement à :

-   tracer un cercle noir centré sur x, y ;
-   tracer une ligne noire épaisse depuis le point x, y jusqu'au point
    x + l.cos α, y + l.sin α.

Nous pouvons à présent commencer à envisager une ébauche de
programmation correspondant à une classe « Canon ». Il n'est pas encore
question ici de programmer le jeu proprement dit. Nous voulons seulement
vérifier si l'analyse que nous avons faite jusqu'à présent « tient la
route », en réalisant un premier *prototype* fonctionnel.

Un prototype est un petit programme destiné à expérimenter une idée, que
l'on se propose d'intégrer ensuite dans une application plus vaste. Du
fait de sa simplicité et de sa concision, Python se prête fort bien à
l'élaboration de prototypes, et de nombreux programmeurs l'utilisent
pour mettre au point divers composants logiciels qu'ils reprogrammeront
éventuellement ensuite dans d'autres langages plus « lourds », tels que
le C par exemple.

Dans notre premier prototype, la classe **Canon()** ne comporte que deux
méthodes : un constructeur qui crée les éléments de base du dessin, et
une méthode permettant de modifier celui-ci à volonté pour ajuster
l'angle de tir (l'inclinaison de la buse). Comme nous l'avons souvent
fait dans d'autres exemples, nous inclurons quelques lignes de code à la
fin du script afin de pouvoir tester la classe tout de suite :\



1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
    from math import pi, sin, cos 
    ```

3.  ``` {.LignePreCode}
      
    ```

4.  ``` {.LignePreCode}
    class Canon(object): 
    ```

5.  ``` {.LignePreCode}
      """Petit canon graphique""" 
    ```

6.  ``` {.LignePreCode}
      def __init__(self, boss, x, y): 
    ```

7.  ``` {.LignePreCode}
          self.boss = boss	     # référence du canevas 
    ```

8.  ``` {.LignePreCode}
          self.x1, self.y1 = x, y	   # axe de rotation du canon 
    ```

9.  ``` {.LignePreCode}
          # dessiner la buse du canon, à l'horizontale pour commencer : 
    ```

10. ``` {.LignePreCode}
          self.lbu = 50	     # longueur de la buse 
    ```

11. ``` {.LignePreCode}
          self.x2, self.y2 = x + self.lbu, y 
    ```

12. ``` {.LignePreCode}
          self.buse = boss.create_line(self.x1, self.y1, self.x2, self.y2, 
    ```

13. ``` {.LignePreCode}
    		   width =10) 
    ```

14. ``` {.LignePreCode}
          # dessiner ensuite le corps du canon par-dessus : 
    ```

15. ``` {.LignePreCode}
          r = 15		  # rayon du cercle  
    ```

16. ``` {.LignePreCode}
          boss.create_oval(x-r, y-r, x+r, y+r, fill='blue', width =3) 
    ```

17. ``` {.LignePreCode}
      
    ```

18. ``` {.LignePreCode}
      def orienter(self, angle): 
    ```

19. ``` {.LignePreCode}
          "choisir l'angle de tir du canon" 
    ```

20. ``` {.LignePreCode}
          # rem : le paramètre  est reçu en tant que chaîne de car. 
    ```

21. ``` {.LignePreCode}
          # il faut le traduire en nombre réel, puis convertir en radians : 
    ```

22. ``` {.LignePreCode}
          self.angle = float(angle)*2*pi/360       
    ```

23. ``` {.LignePreCode}
          self.x2 = self.x1 + self.lbu*cos(self.angle) 
    ```

24. ``` {.LignePreCode}
          self.y2 = self.y1 - self.lbu*sin(self.angle) 
    ```

25. ``` {.LignePreCode}
          self.boss.coords(self.buse, self.x1, self.y1, self.x2, self.y2) 
    ```

26. ``` {.LignePreCode}
      
    ```

27. ``` {.LignePreCode}
    if __name__ == '__main__': 
    ```

28. ``` {.LignePreCode}
      # Code pour tester sommairement la classe Canon : 
    ```

29. ``` {.LignePreCode}
      f = Tk() 
    ```

30. ``` {.LignePreCode}
      can = Canvas(f,width =250, height =250, bg ='ivory') 
    ```

31. ``` {.LignePreCode}
      can.pack(padx =10, pady =10) 
    ```

32. ``` {.LignePreCode}
      c1 = Canon(can, 50, 200) 
    ```

33. ``` {.LignePreCode}
      
    ```

34. ``` {.LignePreCode}
      s1 =Scale(f, label='hausse', from_=90, to=0, command=c1.orienter) 
    ```

35. ``` {.LignePreCode}
      s1.pack(side=LEFT, pady =5, padx =20) 
    ```

36. ``` {.LignePreCode}
      s1.set(25)		      # angle de tir initial 
    ```

37. ``` {.LignePreCode}
      
    ```

38. ``` {.LignePreCode}
      f.mainloop() 
    ```



#### 17-A-1-A - Commentaires {#article.xml#Ld0e63731 .TitreSection3}

-   Ligne 6 : Dans la liste des paramètres qui devront être transmis au
    constructeur lors de l'instanciation, nous prévoyons les coordonnées
    **x** et **y**, qui indiqueront l'emplacement du canon dans le
    canevas, mais également une référence au canevas lui-même (la
    variable **boss**). Cette référence est indispensable : elle sera
    utilisée pour invoquer les méthodes du canevas.\
     Nous pourrions inclure aussi un paramètre pour choisir un angle de
    tir initial, mais puisque nous avons l'intention d'implémenter une
    méthode spécifique pour régler cette orientation, il sera plus
    judicieux de faire appel à celle-ci au moment voulu.
-   Lignes 7-8 : Ces références seront utilisées un peu partout dans les
    différentes méthodes que nous allons développer dans la classe. Il
    faut donc en faire des attributs d'instance.
-   Lignes 9 à 16 : Nous dessinons la buse d'abord, et le corps du canon
    ensuite. Ainsi une partie de la buse reste cachée. Cela nous permet
    de colorer éventuellement le corps du canon.
-   Lignes 18 à 25 : Cette méthode sera invoquée avec un argument
    **angle**, lequel sera fourni en degrés (comptés à partir de
    l'horizontale). S'il est produit à l'aide d'un widget tel que
    **Entry** ou **Scale**, il sera transmis sous la forme d'une chaîne
    de caractères, et nous devrons donc le convertir d'abord en nombre
    réel avant de l'utiliser dans nos calculs (ceux-ci ont été décrits à
    la page précédente).
-   Lignes 27 à 38 : Pour tester notre nouvelle classe, nous ferons
    usage d'un widget **Scale**. Pour définir la position initiale de
    son curseur, et donc fixer l'angle de hausse initial du canon, nous
    devons faire appel à sa méthode **set()** (ligne 36).

### 17-A-2 - Ajout de méthodes au prototype {#article.xml#Ld0e63771 .TitreSection2}



![](images/100000000000011B0000019D3E1D0558.png)



Notre prototype est fonctionnel, mais beaucoup trop rudimentaire. Nous
devons à présent le perfectionner pour lui ajouter la capacité de tirer
des obus.

Ceux-ci seront traités plutôt comme des « boulets » : ce seront de
simples petits cercles que nous ferons partir de la bouche du canon avec
une vitesse initiale d'orientation identique à celle de sa buse. Pour
leur faire suivre une trajectoire réaliste, nous devons à présent nous
rappeler quelques éléments de physique.

*Comment un objet lancé et laissé à lui-même évolue-t-il dans l'espace,
si l'on néglige les phénomènes secondaires tels que la résistance de
l'air ?*

Ce problème peut vous paraître complexe, mais en réalité sa résolution
est très simple : il vous suffit d'admettre que le boulet se déplace à
la fois horizontalement et verticalement, et que ces deux mouvements,
quoique simultanés, sont tout à fait indépendants l'un de l'autre.

Vous allez donc établir une boucle d'animation, dans laquelle vous
recalculez les nouvelles coordonnées **x** et **y** du boulet à
intervalles de temps réguliers, en sachant que :

-   Le mouvement horizontal est *uniforme*. À chaque itération, il vous
    suffit d'augmenter graduellement la coordonnée **x** du boulet, en
    lui ajoutant toujours un même déplacement Δx.
-   Le mouvement vertical est *uniformément accéléré*. Cela signifie
    simplement qu'à chaque itération, vous devez ajouter à la coordonnée
    **y** un déplacement Δy qui augmente lui-même graduellement,
    toujours de la même quantité.

Voyons cela dans le script :

Pour commencer, il faut ajouter les lignes suivantes à la fin de la
méthode constructeur. Elles vont servir à créer l'objet « obus », et à
préparer une variable d'instance qui servira d'interrupteur de
l'animation. L'obus est créé au départ avec des dimensions minimales (un
cercle d'un seul pixel) afin de rester presque invisible :



```python
     # dessiner un obus (réduit à un simple point, avant animation) :
     self.obus =boss.create_oval(x, y, x, y, fill='red')
     self.anim =False		  # interrupteur d'animation
     # retrouver la largeur et la hauteur du canevas :
     self.xMax =int(boss.cget('width'))
     self.yMax =int(boss.cget('height'))
```



Les deux dernières lignes utilisent la méthode **cget()** du widget «
maître » (le canevas, ici), afin de retrouver certaines de ses
caractéristiques. Nous voulons en effet que notre classe **Canon** soit
généraliste, c'est-à-dire réutilisable dans n'importe quel contexte, et
nous ne pouvons donc pas tabler à l'avance sur des dimensions
particulières pour le canevas dans lequel ce canon sera utilisé.

> tkinter renvoie ces valeurs sous la forme de chaînes de caractères. Il
> faut donc les convertir dans un type numérique si nous voulons pouvoir
> les utiliser dans un calcul.

Ensuite, nous devons ajouter deux nouvelles méthodes : l'une pour
déclencher le tir, et l'autre pour gérer l'animation du boulet une fois
que celui-ci aura été lancé :\



1.  ``` {.LignePreCode}
    	   def feu(self): 
    ```

2.  ``` {.LignePreCode}
          "déclencher le tir d'un obus" 
    ```

3.  ``` {.LignePreCode}
          if not self.anim: 
    ```

4.  ``` {.LignePreCode}
          self.anim =True 
    ```

5.  ``` {.LignePreCode}
          # position de départ de l'obus (c'est la bouche du canon) : 
    ```

6.  ``` {.LignePreCode}
          self.boss.coords(self.obus, self.x2 -3, self.y2 -3, 
    ```

7.  ``` {.LignePreCode}
    		      self.x2 +3, self.y2 +3) 
    ```

8.  ``` {.LignePreCode}
          v =15	    # vitesse initiale 
    ```

9.  ``` {.LignePreCode}
          # composantes verticale et horizontale de cette vitesse : 
    ```

10. ``` {.LignePreCode}
          self.vy = -v *sin(self.angle) 
    ```

11. ``` {.LignePreCode}
          self.vx = v *cos(self.angle) 
    ```

12. ``` {.LignePreCode}
          self.animer_obus() 
    ```

13. ``` {.LignePreCode}
      
    ```

14. ``` {.LignePreCode}
      def animer_obus(self): 
    ```

15. ``` {.LignePreCode}
          "animation de l'obus (trajectoire balistique)" 
    ```

16. ``` {.LignePreCode}
          if self.anim: 
    ```

17. ``` {.LignePreCode}
          self.boss.move(self.obus, int(self.vx), int(self.vy)) 
    ```

18. ``` {.LignePreCode}
          c = tuple(self.boss.coords(self.obus))   # coord. résultantes 
    ```

19. ``` {.LignePreCode}
          xo, yo = c[0] +3, c[1] +3 	  # coord. du centre de l'obus 
    ```

20. ``` {.LignePreCode}
          if yo > self.yMax or xo > self.xMax: 
    ```

21. ``` {.LignePreCode}
    	  self.anim =False	      # arrêter l'animation 
    ```

22. ``` {.LignePreCode}
          self.vy += .5 
    ```

23. ``` {.LignePreCode}
          self.boss.after(30, self.animer_obus) 
    ```



#### 17-A-2-A - Commentaires {#article.xml#Ld0e64405 .TitreSection3}

-   Lignes 1 à 4 : Cette méthode sera invoquée par appui sur un bouton.
    Elle déclenche le mouvement de l'obus, et attribue une valeur «
    vraie » à notre « interrupteur d'animation » (la variable
    **self.anim** : voir ci-après). Il faut cependant nous assurer que
    pendant toute la durée de cette animation, un nouvel appui sur le
    bouton ne puisse pas activer d'autres boucles d'animation parasites.
    C'est le rôle du test effectué à la ligne 3 : le bloc d'instruction
    qui suit ne peut s'exécuter que si la variable **self.anim** possède
    la valeur « faux », ce qui signifie que l'animation n'a pas encore
    commencé.
-   Lignes 5 à 7 : Le canevas tkinter dispose de deux méthodes pour
    déplacer les objets graphiques :
    -   La méthode **coords()** (utilisée à la ligne 6) effectue un
        positionnement absolu ; il faut cependant lui fournir toutes les
        coordonnées de l'objet (comme si on le redessinait).
    -   La méthode **move()** (utilisée plus loin, à la ligne 17),
        provoque un déplacement relatif ; elle s'utilise avec deux
        arguments seulement, à savoir les composantes horizontale et
        verticale du déplacement souhaité.
-   Lignes 8 à 12 : La vitesse initiale de l'obus est choisie à la ligne
    8. Comme nous l'avons expliqué à la page précédente, le mouvement du
    boulet est la résultante d'un mouvement horizontal et d'un mouvement
    vertical. Nous connaissons la valeur de la vitesse initiale ainsi
    que son inclinaison (c'est-à-dire l'angle de tir). Pour déterminer
    les composantes horizontale et verticale de cette vitesse, il nous
    suffit d'utiliser des relations trigonométriques tout à fait
    similaires à celles que nous avons déjà exploitées pour dessiner la
    buse du canon. Le signe **-** utilisé à la ligne 10 provient du fait
    que les coordonnées verticales se comptent de haut en bas.\
     La ligne 12 active l'animation proprement dite.
-   Lignes 14 à 23 : Cette procédure se ré-appelle elle-même toutes les
    30 millisecondes par l'intermédiaire de la méthode **after()**
    invoquée à la ligne 23. Cela continue aussi longtemps que la
    variable **self**.**anim** (notre « interrupteur d'animation »)
    reste « vraie », condition qui changera lorsque les coordonnées de
    l'obus sortiront des limites imposées (test de la ligne 20).
-   Lignes 18-19 : Pour retrouver ces coordonnées après chaque
    déplacement, on fait appel encore une fois à la méthode **coords()**
    du canevas : utilisée cette fois avec la référence d'un objet
    graphique comme unique argument, elle renvoie ses quatre coordonnées
    dans un objet itérable que l'on peut convertir en une liste ou un
    tuple à l'aide des fonctions intégrées **list()** et **tuple()**.
-   Lignes 17-22 : La coordonnée horizontale de l'obus augmente toujours
    de la même quantité (mouvement uniforme), tandis que la coordonnée
    verticale augmente d'une quantité qui est elle-même augmentée à
    chaque fois à la ligne 24 (mouvement uniformément accéléré). Le
    résultat est une trajectoire parabolique.

> L*'*opérateur `+=` permet
> d*'*incrémenter une variable :\
>  ainsi `a += 3 `équivaut à
> `a = a + 3`. Veuillez noter au
> passage que l*'*utilisation de cet opérateur spécifique est plus
> efficace que la ré-affectation utilisée jusqu*'*ici.

> À partir de la version 2.3, Python initialise automatiquement deux
> variables nommées `True` et
> `False` pour représenter la
> véracité et la fausseté d*'*une expression (notez bien que ces noms
> commencent tous deux par une majuscule). Comme nous l*'*avons fait
> dans le script ci-dessus, vous pouvez utiliser ces variables dans les
> expressions conditionnelles afin d*'*augmenter la lisibilité de votre
> code. Si vous préférez, vous pouvez cependant continuer à utiliser
> aussi des valeurs numériques, comme nous l*'*avons fait précédemment.
> (cf. « Véracité/Fausseté d*'*une expression », page ).

Il reste enfin à ajouter un bouton déclencheur dans la fenêtre
principale. Une ligne telle que la suivante (à insérer dans le code de
test) fera parfaitement l'affaire :



```python
	Button(f, text='Feu !', command =c1.feu).pack(side=LEFT)
```



### 17-A-3 - Développement de l'application {#article.xml#Ld0e64547 .TitreSection2}

Disposant désormais d'une classe d'objets « canon » assez bien
dégrossie, nous pouvons envisager l'élaboration de l'application
proprement dite. Et puisque nous sommes décidés à exploiter la
méthodologie de la programmation orientée objet, nous devons concevoir
cette application comme *un ensemble d'objets qui interagissent par
l'intermédiaire de leurs méthodes*.



![](images/10000000000001B3000001ABB44494B2.png)



Plusieurs de ces objets proviendront de classes préexistantes, bien
entendu : ainsi le canevas, les boutons, etc. Mais nous avons vu dans
les pages précédentes que nous avons intérêt à regrouper des ensembles
bien délimités de ces objets basiques dans de nouvelles classes, chaque
fois que nous pouvons identifier pour ces ensembles une fonctionnalité
particulière. C'était le cas par exemple pour cet ensemble de cercles et
de lignes mobiles que nous avons décidé d'appeler « canon ».

Pouvons-nous encore distinguer dans notre projet initial d'autres
composants qui mériteraient d'être encapsulés dans des nouvelles classes
? Certainement. Il y a par exemple le pupitre de contrôle que nous
voulons associer à chaque canon : nous pouvons y rassembler le
dispositif de réglage de la hausse (l'angle de tir), le bouton de mise à
feu, le score réalisé, et peut-être d'autres indications encore, comme
le nom du joueur. Il est d'autant plus intéressant de lui consacrer une
classe particulière, que nous savons d'emblée qu'il nous en faudra deux
instances.

Il y a aussi l'application elle-même, bien sûr. En l'encapsulant dans
une classe, nous en ferons notre objet principal, celui qui dirigera
tous les autres.

Veuillez à présent analyser le script ci-dessous. Vous y retrouverez la
classe **Canon()** encore davantage développée : nous y avons ajouté
quelques attributs et trois méthodes supplémentaires, afin de pouvoir
gérer les déplacements du canon lui-même, ainsi que les coups au but.

La classe **Application()** remplace désormais le code de test des
prototypes précédents. Nous y instancions deux objets **Canon()**, et
deux objets de la nouvelle classe **Pupitre()**, que nous plaçons dans
des dictionnaires en prévision de développements ultérieurs (nous
pouvons en effet imaginer d'augmenter le nombre de canons et donc de
pupitres). Le jeu est à présent fonctionnel : les canons se déplacent
après chaque tir, et les coups au but sont comptabilisés.



1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
    from math import sin, cos, pi 
    ```

3.  ``` {.LignePreCode}
    from random import randrange 
    ```

4.  ``` {.LignePreCode}
      
    ```

5.  ``` {.LignePreCode}
    class Canon(object): 
    ```

6.  ``` {.LignePreCode}
      """Petit canon graphique""" 
    ```

7.  ``` {.LignePreCode}
      def __init__(self, boss, id, x, y, sens, coul): 
    ```

8.  ``` {.LignePreCode}
          self.boss = boss	     # réf. du canevas 
    ```

9.  ``` {.LignePreCode}
          self.appli = boss.master	  # réf. de la fenêtre d'application 
    ```

10. ``` {.LignePreCode}
          self.id = id	    # identifiant du canon (chaîne) 
    ```

11. ``` {.LignePreCode}
          self.coul = coul	     # couleur associée au canon 
    ```

12. ``` {.LignePreCode}
          self.x1, self.y1 = x, y	   # axe de rotation du canon 
    ```

13. ``` {.LignePreCode}
          self.sens = sens	     # sens de tir (-1:gauche, +1:droite) 
    ```

14. ``` {.LignePreCode}
          self.lbu = 30	     # longueur de la buse 
    ```

15. ``` {.LignePreCode}
          self.angle = 0	      # hausse par défaut (angle de tir) 
    ```

16. ``` {.LignePreCode}
          # retrouver la largeur et la hauteur du canevas : 
    ```

17. ``` {.LignePreCode}
          self.xMax = int(boss.cget('width')) 
    ```

18. ``` {.LignePreCode}
          self.yMax = int(boss.cget('height')) 
    ```

19. ``` {.LignePreCode}
          # dessiner la buse du canon (horizontale) : 
    ```

20. ``` {.LignePreCode}
          self.x2, self.y2 = x + self.lbu * sens, y 
    ```

21. ``` {.LignePreCode}
          self.buse = boss.create_line(self.x1, self.y1, 
    ```

22. ``` {.LignePreCode}
    		   self.x2, self.y2, width =10) 
    ```

23. ``` {.LignePreCode}
          # dessiner le corps du canon (cercle de couleur) : 
    ```

24. ``` {.LignePreCode}
          self.rc = 15	    # rayon du cercle  
    ```

25. ``` {.LignePreCode}
          self.corps = boss.create_oval(x -self.rc, y -self.rc, x +self.rc, 
    ```

26. ``` {.LignePreCode}
    		    y +self.rc, fill =coul) 
    ```

27. ``` {.LignePreCode}
          # pré-dessiner un obus caché (point en dehors du canevas) : 
    ```

28. ``` {.LignePreCode}
          self.obus = boss.create_oval(-10, -10, -10, -10, fill='red') 
    ```

29. ``` {.LignePreCode}
          self.anim = False      # indicateurs d'animation  
    ```

30. ``` {.LignePreCode}
          self.explo = False      #    et d'explosion 
    ```

31. ``` {.LignePreCode}
      
    ```

32. ``` {.LignePreCode}
      def orienter(self, angle): 
    ```

33. ``` {.LignePreCode}
          "régler la hausse du canon" 
    ```

34. ``` {.LignePreCode}
          # rem: le paramètre  est reçu en tant que chaîne. 
    ```

35. ``` {.LignePreCode}
          # Il faut donc le traduire en réel, puis le convertir en radians : 
    ```

36. ``` {.LignePreCode}
          self.angle = float(angle)*pi/180 
    ```

37. ``` {.LignePreCode}
          # rem: utiliser la méthode coords de préférence avec des entiers :       
    ```

38. ``` {.LignePreCode}
          self.x2 = int(self.x1 + self.lbu * cos(self.angle) * self.sens) 
    ```

39. ``` {.LignePreCode}
          self.y2 = int(self.y1 - self.lbu * sin(self.angle)) 
    ```

40. ``` {.LignePreCode}
          self.boss.coords(self.buse, self.x1, self.y1, self.x2, self.y2) 
    ```

41. ``` {.LignePreCode}
      
    ```

42. ``` {.LignePreCode}
      def deplacer(self, x, y): 
    ```

43. ``` {.LignePreCode}
          "amener le canon dans une nouvelle position x, y" 
    ```

44. ``` {.LignePreCode}
          dx, dy = x -self.x1, y -self.y1	   # valeur du déplacement 
    ```

45. ``` {.LignePreCode}
          self.boss.move(self.buse, dx, dy)  
    ```

46. ``` {.LignePreCode}
          self.boss.move(self.corps, dx, dy) 
    ```

47. ``` {.LignePreCode}
          self.x1 += dx 
    ```

48. ``` {.LignePreCode}
          self.y1 += dy 
    ```

49. ``` {.LignePreCode}
          self.x2 += dx 
    ```

50. ``` {.LignePreCode}
          self.y2 += dy 
    ```

51. ``` {.LignePreCode}
      
    ```

52. ``` {.LignePreCode}
      def feu(self): 
    ```

53. ``` {.LignePreCode}
          "tir d'un obus - seulement si le précédent a fini son vol" 
    ```

54. ``` {.LignePreCode}
          if not (self.anim or self.explo): 
    ```

55. ``` {.LignePreCode}
          self.anim =True 
    ```

56. ``` {.LignePreCode}
          # récupérer la description de tous les canons présents : 
    ```

57. ``` {.LignePreCode}
          self.guns = self.appli.dictionnaireCanons() 
    ```

58. ``` {.LignePreCode}
          # position de départ de l'obus (c'est la bouche du canon) : 
    ```

59. ``` {.LignePreCode}
          self.boss.coords(self.obus, self.x2 -3, self.y2 -3, 
    ```

60. ``` {.LignePreCode}
    		      self.x2 +3, self.y2 +3) 
    ```

61. ``` {.LignePreCode}
          v = 17	      # vitesse initiale 
    ```

62. ``` {.LignePreCode}
          # composantes verticale et horizontale de cette vitesse : 
    ```

63. ``` {.LignePreCode}
          self.vy = -v *sin(self.angle) 
    ```

64. ``` {.LignePreCode}
          self.vx = v *cos(self.angle) *self.sens 
    ```

65. ``` {.LignePreCode}
          self.animer_obus() 
    ```

66. ``` {.LignePreCode}
          return True      # => signaler que le coup est parti 
    ```

67. ``` {.LignePreCode}
          else: 
    ```

68. ``` {.LignePreCode}
          return False    # => le coup n'a pas pu être tiré 
    ```

69. ``` {.LignePreCode}
      
    ```

70. ``` {.LignePreCode}
      def animer_obus(self): 
    ```

71. ``` {.LignePreCode}
          "animer l'obus (trajectoire balistique)" 
    ```

72. ``` {.LignePreCode}
          if self.anim: 
    ```

73. ``` {.LignePreCode}
          self.boss.move(self.obus, int(self.vx), int(self.vy)) 
    ```

74. ``` {.LignePreCode}
          c = tuple(self.boss.coords(self.obus))	 # coord. résultantes 
    ```

75. ``` {.LignePreCode}
          xo, yo = c[0] +3, c[1] +3     # coord. du centre de l'obus 
    ```

76. ``` {.LignePreCode}
          self.test_obstacle(xo, yo)     # a-t-on atteint un obstacle ? 
    ```

77. ``` {.LignePreCode}
          self.vy += .4	    # accélération verticale 
    ```

78. ``` {.LignePreCode}
          self.boss.after(20, self.animer_obus) 
    ```

79. ``` {.LignePreCode}
          else: 
    ```

80. ``` {.LignePreCode}
          # animation terminée - cacher l'obus et déplacer les canons : 
    ```

81. ``` {.LignePreCode}
          self.fin_animation() 
    ```

82. ``` {.LignePreCode}
      
    ```

83. ``` {.LignePreCode}
      def test_obstacle(self, xo, yo): 
    ```

84. ``` {.LignePreCode}
          "évaluer si l'obus a atteint une cible ou les limites du jeu" 
    ```

85. ``` {.LignePreCode}
          if yo >self.yMax or xo <0 or xo >self.xMax: 
    ```

86. ``` {.LignePreCode}
          self.anim =False 
    ```

87. ``` {.LignePreCode}
          return 
    ```

88. ``` {.LignePreCode}
          # analyser le dictionnaire des canons pour voir si les coord. 
    ```

89. ``` {.LignePreCode}
          # de l'un d'entre eux sont proches de celles de l'obus : 
    ```

90. ``` {.LignePreCode}
          for id in self.guns:	   # id = clef dans dictionn. 
    ```

91. ``` {.LignePreCode}
          gun = self.guns[id]	  # valeur correspondante 
    ```

92. ``` {.LignePreCode}
          if xo < gun.x1 +self.rc and xo > gun.x1 -self.rc \ 
    ```

93. ``` {.LignePreCode}
          and yo < gun.y1 +self.rc and yo > gun.y1 -self.rc : 
    ```

94. ``` {.LignePreCode}
    	  self.anim =False 
    ```

95. ``` {.LignePreCode}
    	  # dessiner l'explosion de l'obus (cercle jaune) : 
    ```

96. ``` {.LignePreCode}
    	  self.explo = self.boss.create_oval(xo -12, yo -12, 
    ```

97. ``` {.LignePreCode}
    	       xo +12, yo +12, fill ='yellow', width =0) 
    ```

98. ``` {.LignePreCode}
    	  self.hit =id	   # référence de la cible touchée 
    ```

99. ``` {.LignePreCode}
    	  self.boss.after(150, self.fin_explosion) 
    ```

100. ``` {.LignePreCode}
    	  break         
    ```

101. ``` {.LignePreCode}
      
    ```

102. ``` {.LignePreCode}
      def fin_explosion(self): 
    ```

103. ``` {.LignePreCode}
          "effacer l'explosion ; ré-initaliser l'obus ; gérer le score" 
    ```

104. ``` {.LignePreCode}
          self.boss.delete(self.explo)    # effacer l'explosion 
    ```

105. ``` {.LignePreCode}
          self.explo =False 	 # autoriser un nouveau tir 
    ```

106. ``` {.LignePreCode}
          # signaler le succès à la fenêtre maîtresse : 
    ```

107. ``` {.LignePreCode}
          self.appli.goal(self.id, self.hit) 
    ```

108. ``` {.LignePreCode}
      
    ```

109. ``` {.LignePreCode}
      def fin_animation(self): 
    ```

110. ``` {.LignePreCode}
          "actions à accomplir lorsque l'obus a terminé sa trajectoire" 
    ```

111. ``` {.LignePreCode}
          self.appli.disperser()	      # déplacer les canons 
    ```

112. ``` {.LignePreCode}
          # cacher l'obus (en l'expédiant hors du canevas) : 
    ```

113. ``` {.LignePreCode}
          self.boss.coords(self.obus, -10, -10, -10, -10) 
    ```

114. ``` {.LignePreCode}
      
    ```

115. ``` {.LignePreCode}
    class Pupitre(Frame): 
    ```

116. ``` {.LignePreCode}
      """Pupitre de pointage associé à un canon"""  
    ```

117. ``` {.LignePreCode}
      def __init__(self, boss, canon): 
    ```

118. ``` {.LignePreCode}
          Frame.__init__(self, bd =3, relief =GROOVE) 
    ```

119. ``` {.LignePreCode}
          self.score =0 
    ```

120. ``` {.LignePreCode}
          self.appli =boss		 # réf. de l'application 
    ```

121. ``` {.LignePreCode}
          self.canon =canon 	 # réf. du canon associé 
    ```

122. ``` {.LignePreCode}
          # Système de réglage de l'angle de tir : 
    ```

123. ``` {.LignePreCode}
          self.regl =Scale(self, from_ =85, to =-15, troughcolor=canon.coul, 
    ```

124. ``` {.LignePreCode}
    	    command =self.orienter) 
    ```

125. ``` {.LignePreCode}
          self.regl.set(45) 	 # angle initial de tir 
    ```

126. ``` {.LignePreCode}
          self.regl.pack(side =LEFT) 
    ```

127. ``` {.LignePreCode}
          # Étiquette d'identification du canon : 
    ```

128. ``` {.LignePreCode}
          Label(self, text =canon.id).pack(side =TOP, anchor =W, pady =5) 
    ```

129. ``` {.LignePreCode}
          # Bouton de tir : 
    ```

130. ``` {.LignePreCode}
          self.bTir =Button(self, text ='Feu !', command =self.tirer) 
    ```

131. ``` {.LignePreCode}
          self.bTir.pack(side =BOTTOM, padx =5, pady =5) 
    ```

132. ``` {.LignePreCode}
          Label(self, text ="points").pack() 
    ```

133. ``` {.LignePreCode}
          self.points =Label(self, text=' 0 ', bg ='white') 
    ```

134. ``` {.LignePreCode}
          self.points.pack() 
    ```

135. ``` {.LignePreCode}
          # positionner à gauche ou à droite suivant le sens du canon : 
    ```

136. ``` {.LignePreCode}
          if canon.sens == -1: 
    ```

137. ``` {.LignePreCode}
          self.pack(padx =5, pady =5, side =RIGHT) 
    ```

138. ``` {.LignePreCode}
          else: 
    ```

139. ``` {.LignePreCode}
          self.pack(padx =5, pady =5, side =LEFT) 
    ```

140. ``` {.LignePreCode}
      
    ```

141. ``` {.LignePreCode}
      def tirer(self): 
    ```

142. ``` {.LignePreCode}
          "déclencher le tir du canon associé" 
    ```

143. ``` {.LignePreCode}
          self.canon.feu() 
    ```

144. ``` {.LignePreCode}
      
    ```

145. ``` {.LignePreCode}
      def orienter(self, angle): 
    ```

146. ``` {.LignePreCode}
          "ajuster la hausse du canon associé" 
    ```

147. ``` {.LignePreCode}
          self.canon.orienter(angle) 
    ```

148. ``` {.LignePreCode}
      
    ```

149. ``` {.LignePreCode}
      def attribuerPoint(self, p): 
    ```

150. ``` {.LignePreCode}
          "incrémenter ou décrémenter le score, de  points" 
    ```

151. ``` {.LignePreCode}
          self.score += p 
    ```

152. ``` {.LignePreCode}
          self.points.config(text = ' %s ' % self.score) 
    ```

153. ``` {.LignePreCode}
      
    ```

154. ``` {.LignePreCode}
    class Application(Frame): 
    ```

155. ``` {.LignePreCode}
      '''Fenêtre principale de l'application''' 
    ```

156. ``` {.LignePreCode}
      def __init__(self): 
    ```

157. ``` {.LignePreCode}
          Frame.__init__(self) 
    ```

158. ``` {.LignePreCode}
          self.master.title('>>>>> Boum ! Boum ! <<<<<') 
    ```

159. ``` {.LignePreCode}
          self.pack() 
    ```

160. ``` {.LignePreCode}
          self.jeu = Canvas(self, width =400, height =250, bg ='ivory', 
    ```

161. ``` {.LignePreCode}
    	     bd =3, relief =SUNKEN) 
    ```

162. ``` {.LignePreCode}
          self.jeu.pack(padx =8, pady =8, side =TOP) 
    ```

163. ``` {.LignePreCode}
      
    ```

164. ``` {.LignePreCode}
          self.guns ={}	     # dictionnaire des canons présents 
    ```

165. ``` {.LignePreCode}
          self.pupi ={}	     # dictionnaire des pupitres présents 
    ```

166. ``` {.LignePreCode}
          # Instanciation de 2 objets canons (+1, -1 = sens opposés) : 
    ```

167. ``` {.LignePreCode}
          self.guns["Billy"] = Canon(self.jeu, "Billy", 30, 200, 1, "red") 
    ```

168. ``` {.LignePreCode}
          self.guns["Linus"] = Canon(self.jeu, "Linus", 370,200,-1, "blue") 
    ```

169. ``` {.LignePreCode}
          # Instanciation de 2 pupitres de pointage associés à ces canons : 
    ```

170. ``` {.LignePreCode}
          self.pupi["Billy"] = Pupitre(self, self.guns["Billy"]) 
    ```

171. ``` {.LignePreCode}
          self.pupi["Linus"] = Pupitre(self, self.guns["Linus"]) 
    ```

172. ``` {.LignePreCode}
      
    ```

173. ``` {.LignePreCode}
      def disperser(self): 
    ```

174. ``` {.LignePreCode}
          "déplacer aléatoirement les canons" 
    ```

175. ``` {.LignePreCode}
          for id in self.guns: 
    ```

176. ``` {.LignePreCode}
          gun =self.guns[id] 
    ```

177. ``` {.LignePreCode}
          # positionner à gauche ou à droite, suivant sens du canon : 
    ```

178. ``` {.LignePreCode}
          if gun.sens == -1 : 
    ```

179. ``` {.LignePreCode}
    	  x = randrange(320,380) 
    ```

180. ``` {.LignePreCode}
          else: 
    ```

181. ``` {.LignePreCode}
    	  x = randrange(20,80) 
    ```

182. ``` {.LignePreCode}
          # déplacement proprement dit : 
    ```

183. ``` {.LignePreCode}
          gun.deplacer(x, randrange(150,240)) 
    ```

184. ``` {.LignePreCode}
      
    ```

185. ``` {.LignePreCode}
      def goal(self, i, j): 
    ```

186. ``` {.LignePreCode}
          "le canon  signale qu'il a atteint l'adversaire " 
    ```

187. ``` {.LignePreCode}
          if i != j: 
    ```

188. ``` {.LignePreCode}
          self.pupi[i].attribuerPoint(1)	 
    ```

189. ``` {.LignePreCode}
          else: 
    ```

190. ``` {.LignePreCode}
          self.pupi[i].attribuerPoint(-1) 
    ```

191. ``` {.LignePreCode}
      
    ```

192. ``` {.LignePreCode}
      def dictionnaireCanons(self): 
    ```

193. ``` {.LignePreCode}
          "renvoyer le dictionnaire décrivant les canons présents"  
    ```

194. ``` {.LignePreCode}
          return self.guns 
    ```

195. ``` {.LignePreCode}
      
    ```

196. ``` {.LignePreCode}
    if __name__ =='__main__': 
    ```

197. ``` {.LignePreCode}
      Application().mainloop() 
    ```



#### 17-A-3-A - Commentaires {#article.xml#Ld0e68633 .TitreSection3}

-   Ligne 7 : Par rapport au prototype, trois paramètres ont été ajoutés
    à la méthode constructeur. Le paramètre **id** nous permet
    d'identifier chaque instance de la classe **Canon()** à l'aide d'un
    nom quelconque. Le paramètre **sens** indique s'il s'agit d'un canon
    qui tire vers la droite (sens = 1) ou vers la gauche (sens = -1). Le
    paramètre **coul** spécifie la couleur associée au canon.
-   Ligne 9 : Tous les widgets *tkinter* possèdent un attribut
    **master** qui contient la référence leur widget maître éventuel
    (leur « contenant »). Cette référence est donc pour nous celle de
    l'application principale. Nous avons implémenté nous-mêmes une
    technique similaire pour référencer le canevas, à l'aide de
    l'attribut **boss**.
-   Lignes 42 à 50 : Cette méthode permet d'amener le canon dans un
    nouvel emplacement. Elle servira à repositionner les canons au
    hasard après chaque tir, ce qui augmente l'intérêt du jeu.
-   Lignes 56-57 : Nous essayons de construire notre classe canon de
    telle manière qu'elle puisse être réutilisée dans des projets plus
    vastes, impliquant un nombre quelconque d'objets canons qui pourront
    apparaître et disparaître au fil des combats. Dans cette
    perspective, il faut que nous puissions disposer d'une description
    de tous les canons présents, avant chaque tir, de manière à pouvoir
    déterminer si une cible a été touchée ou non. Cette description est
    gérée par l'application principale, dans un dictionnaire, dont on
    peut demander une copie par l'intermédiaire de sa méthode
    **dictionnaireCanons()**.
-   Lignes 66 à 68 : Dans cette même perspective généraliste, il peut
    être utile d'informer éventuellement le programme appelant que le
    coup a effectivement été tiré ou non.
-   Ligne 76 : L'animation de l'obus est désormais traitée par deux
    méthodes complémentaires. Afin de clarifier le code, nous avons
    placé dans une méthode distincte les instructions servant à
    déterminer si une cible a été atteinte (méthode
    **test\_obstacle()**).
-   Lignes 79 à 81 : Nous avons vu précédemment que l'on interrompt
    l'animation de l'obus en attribuant une valeur « fausse » à la
    variable **self**.**anim**. La méthode **animer\_obus()** cesse
    alors de boucler et exécute le code de la ligne 81.
-   Lignes 83 à 100 : Cette méthode évalue si les coordonnées actuelles
    de l'obus sortent des limites de la fenêtre, ou encore si elles
    s'approchent de celles d'un autre canon. Dans les deux cas,
    l'interrupteur d'animation est actionné, mais dans le second, on
    dessine une « explosion » jaune, et la référence du canon touché est
    mémorisée. La méthode annexe **fin\_explosion**() est invoquée après
    un court laps de temps pour terminer le travail, c'est-à-dire
    effacer le cercle d'explosion et envoyer un message à la fenêtre
    maîtresse pour signaler le coup au but.
-   Lignes 115 à 152 : La classe **Pupitre()** définit un nouveau widget
    par dérivation de la classe **Frame()**, selon une technique qui
    doit désormais vous être devenue familière. Ce nouveau widget
    regroupe les commandes de hausse et de tir, ainsi que l'afficheur de
    points associés à un canon bien déterminé. La correspondance
    visuelle entre les deux est assurée par l'adoption d'une couleur
    commune. Les méthodes **tirer()** et **orienter()** communiquent
    avec l'objet **Canon()** associé, par l'intermédiaire des méthodes
    de celui-ci.
-   Lignes 154 à 171 : La fenêtre d'application est elle aussi un widget
    dérivé de **Frame()**. Son constructeur instancie les deux canons et
    leurs pupitres de pointage, en plaçant ces objets dans les deux
    dictionnaires **self**.**guns** et **self**.**pupi**. Cela permet
    d'effectuer ensuite divers traitements systématiques sur chacun
    d'eux (comme par exemple à la méthode suivante). En procédant ainsi,
    on se réserve en outre la possibilité d'augmenter sans effort le
    nombre de ces canons si nécessaire, dans les développements
    ultérieurs du programme.
-   Lignes 173 à 183 : Cette méthode est invoquée après chaque tir pour
    déplacer aléatoirement les deux canons, ce qui augmente la
    difficulté du jeu.

### 17-A-4 - Développements complémentaires {#article.xml#Ld0e68728 .TitreSection2}

Tel qu'il vient d'être décrit, notre programme correspond déjà plus ou
moins au cahier des charges initial, mais il est évident que nous
pouvons continuer à le perfectionner.

A\) Nous devrions par exemple *mieux le paramétrer*. Qu'est-ce à dire ?
Dans sa forme actuelle, notre jeu comporte un canevas de taille
prédéterminée (400 × 250 pixels, voir ligne 161). Si nous voulons
modifier ces valeurs, nous devons veiller à modifier aussi les autres
lignes du script où ces dimensions interviennent (comme par exemple aux
lignes 168-169, ou 179-184). De telles lignes interdépendantes risquent
de devenir nombreuses si nous ajoutons encore d'autres fonctionnalités.
Il serait donc plus judicieux de dimensionner le canevas *à l'aide de
variables*, dont la valeur serait définie en un seul endroit. Ces
variables seraient ensuite exploitées dans toutes les lignes
d'instructions où les dimensions du canevas interviennent.

Nous avons déjà effectué une partie de ce travail : dans la classe
**Canon()**, en effet, les dimensions du canevas sont récupérées à
l'aide d'une méthode prédéfinie (voir lignes 17-18), et placées dans des
attributs d'instance qui peuvent être utilisés partout dans la classe.

B\) Après chaque tir, nous provoquons un déplacement aléatoire des
canons, en redéfinissant leurs coordonnées au hasard. Il serait
probablement plus réaliste de provoquer de véritables *déplacements
relatifs*, plutôt que de redéfinir au hasard des positions absolues.
Pour ce faire, il suffit de retravailler la méthode **deplacer()** de la
classe **Canon()**. En fait, il serait encore plus intéressant de faire
en sorte que cette méthode puisse produire à volonté, aussi bien un
déplacement relatif qu'un positionnement absolu, en fonction d'une
valeur transmise en argument.

C\) Le système de commande des tirs devrait être amélioré : puisque nous
ne disposons que d'une seule souris, il faut demander aux joueurs de
tirer à tour de rôle, et nous n'avons mis en place aucun mécanisme pour
les forcer à le faire. Une meilleure approche consisterait à prévoir des
commandes de hausse et de tir utilisant certaines touches du clavier,
qui soient distinctes pour les deux joueurs.



![](images/10000000000002A5000001D57D0D1D80.png)



Ce type de développement suppose cependant que nous ayons appris à
maîtriser au préalable deux domaines de programmation qui débordent un
peu le cadre de ce cours :

-   la technique des *sockets*, qui permet d'établir une communication
    entre deux ordinateurs ;
-   la technique des *threads*, qui permet à un même programme
    d'effectuer plusieurs tâches simultanément (cela nous sera
    nécessaire, si nous voulons construire une application capable de
    communiquer en même temps avec plusieurs partenaires).

Ces matières ne font pas strictement partie des objectifs que nous nous
sommes fixés pour ce cours, et leur traitement nécessite à lui seul un
chapitre entier. Nous n'aborderons donc pas cette question ici. Que ceux
que le sujet intéresse se rassurent cependant : ce chapitre existe, mais
sous la forme d'un complément à la fin du livre (chapitre 18) : vous y
trouverez la version réseau de notre jeu de bombardes.

En attendant, voyons tout de même comment nous pouvons encore
progresser, en apportant à notre projet quelques améliorations qui en
feront un jeu pour 4 joueurs. Nous nous efforcerons aussi de mettre en
place une programmation bien compartimentée, de manière à ce que les
méthodes de nos classes soient réutilisables dans une large mesure. Nous
allons voir au passage comment cette évolution peut se faire sans
modifier le code existant, en utilisant *l'héritage* pour produire de
nouvelles classes à partir de celles qui sont déjà écrites.

Commençons par sauvegarder notre ouvrage précédent dans un fichier, dont
nous admettrons pour la suite de ce texte que le nom est :
**canon03.py**.

Nous disposons ainsi d'un véritable *module* Python, que nous pouvons
importer dans un nouveau script à l'aide d'une seule ligne
d'instruction. En exploitant cette technique, nous continuons à
perfectionner notre application, en ne conservant sous les yeux que les
nouveautés :



1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
    from math import sin, cos, pi 
    ```

3.  ``` {.LignePreCode}
    from random import randrange 
    ```

4.  ``` {.LignePreCode}
    import canon03 
    ```

5.  ``` {.LignePreCode}
      
    ```

6.  ``` {.LignePreCode}
    class Canon(canon03.Canon): 
    ```

7.  ``` {.LignePreCode}
      """Canon amélioré""" 
    ```

8.  ``` {.LignePreCode}
      def __init__(self, boss, id, x, y, sens, coul): 
    ```

9.  ``` {.LignePreCode}
          canon03.Canon.__init__(self, boss, id, x, y, sens, coul) 
    ```

10. ``` {.LignePreCode}
      
    ```

11. ``` {.LignePreCode}
      def deplacer(self, x, y, rel =False): 
    ```

12. ``` {.LignePreCode}
          "déplacement, relatif si  est vrai, absolu si  est faux" 
    ```

13. ``` {.LignePreCode}
          if rel: 
    ```

14. ``` {.LignePreCode}
          dx, dy = x, y 
    ```

15. ``` {.LignePreCode}
          else: 
    ```

16. ``` {.LignePreCode}
          dx, dy = x -self.x1, y -self.y1 
    ```

17. ``` {.LignePreCode}
          # limites horizontales : 
    ```

18. ``` {.LignePreCode}
          if self.sens ==1: 
    ```

19. ``` {.LignePreCode}
          xa, xb = 20, int(self.xMax *.33) 
    ```

20. ``` {.LignePreCode}
          else: 
    ```

21. ``` {.LignePreCode}
          xa, xb = int(self.xMax *.66), self.xMax -20 
    ```

22. ``` {.LignePreCode}
          # ne déplacer que dans ces limites : 
    ```

23. ``` {.LignePreCode}
          if self.x1 +dx < xa: 
    ```

24. ``` {.LignePreCode}
          dx = xa -self.x1 
    ```

25. ``` {.LignePreCode}
          elif self.x1 +dx > xb: 
    ```

26. ``` {.LignePreCode}
          dx = xb -self.x1 
    ```

27. ``` {.LignePreCode}
          # limites verticales : 
    ```

28. ``` {.LignePreCode}
          ya, yb = int(self.yMax *.4), self.yMax -20 
    ```

29. ``` {.LignePreCode}
          # ne déplacer que dans ces limites : 
    ```

30. ``` {.LignePreCode}
          if self.y1 +dy < ya: 
    ```

31. ``` {.LignePreCode}
          dy = ya -self.y1 
    ```

32. ``` {.LignePreCode}
          elif self.y1 +dy > yb: 
    ```

33. ``` {.LignePreCode}
          dy = yb -self.y1 
    ```

34. ``` {.LignePreCode}
          # déplacement de la buse et du corps du canon :	   
    ```

35. ``` {.LignePreCode}
          self.boss.move(self.buse, dx, dy)  
    ```

36. ``` {.LignePreCode}
          self.boss.move(self.corps, dx, dy)  
    ```

37. ``` {.LignePreCode}
          # renvoyer les nouvelles coord. au programme appelant : 
    ```

38. ``` {.LignePreCode}
          self.x1 += dx 
    ```

39. ``` {.LignePreCode}
          self.y1 += dy 
    ```

40. ``` {.LignePreCode}
          self.x2 += dx 
    ```

41. ``` {.LignePreCode}
          self.y2 += dy 
    ```

42. ``` {.LignePreCode}
          return self.x1, self.y1 
    ```

43. ``` {.LignePreCode}
      
    ```

44. ``` {.LignePreCode}
      def fin_animation(self): 
    ```

45. ``` {.LignePreCode}
          "actions à accomplir lorsque l'obus a terminé sa trajectoire" 
    ```

46. ``` {.LignePreCode}
          # déplacer le canon qui vient de tirer : 
    ```

47. ``` {.LignePreCode}
          self.appli.depl_aleat_canon(self.id) 
    ```

48. ``` {.LignePreCode}
          # cacher l'obus (en l'expédiant hors du canevas) : 
    ```

49. ``` {.LignePreCode}
          self.boss.coords(self.obus, -10, -10, -10, -10) 
    ```

50. ``` {.LignePreCode}
      
    ```

51. ``` {.LignePreCode}
      def effacer(self): 
    ```

52. ``` {.LignePreCode}
          "faire disparaître le canon du canevas" 
    ```

53. ``` {.LignePreCode}
          self.boss.delete(self.buse) 
    ```

54. ``` {.LignePreCode}
          self.boss.delete(self.corps) 
    ```

55. ``` {.LignePreCode}
          self.boss.delete(self.obus)      
    ```

56. ``` {.LignePreCode}
      
    ```

57. ``` {.LignePreCode}
    class AppBombardes(Frame): 
    ```

58. ``` {.LignePreCode}
      '''Fenêtre principale de l'application''' 
    ```

59. ``` {.LignePreCode}
      def __init__(self, larg_c, haut_c): 
    ```

60. ``` {.LignePreCode}
          Frame.__init__(self) 
    ```

61. ``` {.LignePreCode}
          self.pack() 
    ```

62. ``` {.LignePreCode}
          self.xm, self.ym = larg_c, haut_c 
    ```

63. ``` {.LignePreCode}
          self.jeu = Canvas(self, width =self.xm, height =self.ym, 
    ```

64. ``` {.LignePreCode}
    	     bg ='ivory', bd =3, relief =SUNKEN) 
    ```

65. ``` {.LignePreCode}
          self.jeu.pack(padx =4, pady =4, side =TOP) 
    ```

66. ``` {.LignePreCode}
      
    ```

67. ``` {.LignePreCode}
          self.guns ={}	     # dictionnaire des canons présents 
    ```

68. ``` {.LignePreCode}
          self.pupi ={}	     # dictionnaire des pupitres présents 
    ```

69. ``` {.LignePreCode}
          self.specificites()     # objets différents dans classes dérivées 
    ```

70. ``` {.LignePreCode}
      
    ```

71. ``` {.LignePreCode}
      def specificites(self): 
    ```

72. ``` {.LignePreCode}
          "instanciation des canons et des pupitres de pointage" 
    ```

73. ``` {.LignePreCode}
          self.master.title('<<< Jeu des bombardes >>>') 
    ```

74. ``` {.LignePreCode}
          id_list =[("Paul","red"),("Roméo","cyan"), 
    ```

75. ``` {.LignePreCode}
    	 ("Virginie","orange"),("Juliette","blue")] 
    ```

76. ``` {.LignePreCode}
          s = False 
    ```

77. ``` {.LignePreCode}
          for id, coul in id_list: 
    ```

78. ``` {.LignePreCode}
          if s: 
    ```

79. ``` {.LignePreCode}
    	  sens =1 
    ```

80. ``` {.LignePreCode}
          else: 
    ```

81. ``` {.LignePreCode}
    	  sens =-1 
    ```

82. ``` {.LignePreCode}
          x, y = self.coord_aleat(sens) 
    ```

83. ``` {.LignePreCode}
          self.guns[id] = Canon(self.jeu, id, x, y, sens, coul) 
    ```

84. ``` {.LignePreCode}
          self.pupi[id] = canon03.Pupitre(self, self.guns[id]) 
    ```

85. ``` {.LignePreCode}
          s = not s 	 # changer de côté à chaque itération 
    ```

86. ``` {.LignePreCode}
      
    ```

87. ``` {.LignePreCode}
      def depl_aleat_canon(self, id): 
    ```

88. ``` {.LignePreCode}
          "déplacer aléatoirement le canon " 
    ```

89. ``` {.LignePreCode}
          gun =self.guns[id] 
    ```

90. ``` {.LignePreCode}
          dx, dy = randrange(-60, 61), randrange(-60, 61) 
    ```

91. ``` {.LignePreCode}
          # déplacement (avec récupération des nouvelles coordonnées) : 
    ```

92. ``` {.LignePreCode}
          x, y = gun.deplacer(dx, dy, True) 
    ```

93. ``` {.LignePreCode}
          return x, y 
    ```

94. ``` {.LignePreCode}
      
    ```

95. ``` {.LignePreCode}
      def coord_aleat(self, s): 
    ```

96. ``` {.LignePreCode}
          "coordonnées aléatoires, à gauche (s =1) ou à droite (s =-1)"  
    ```

97. ``` {.LignePreCode}
          y =randrange(int(self.ym /2), self.ym -20) 
    ```

98. ``` {.LignePreCode}
          if s == -1: 
    ```

99. ``` {.LignePreCode}
          x =randrange(int(self.xm *.7), self.xm -20) 
    ```

100. ``` {.LignePreCode}
          else: 
    ```

101. ``` {.LignePreCode}
          x =randrange(20, int(self.xm *.3)) 
    ```

102. ``` {.LignePreCode}
          return x, y 
    ```

103. ``` {.LignePreCode}
      
    ```

104. ``` {.LignePreCode}
      def goal(self, i, j): 
    ```

105. ``` {.LignePreCode}
          "le canon n°i signale qu'il a atteint l'adversaire n°j" 
    ```

106. ``` {.LignePreCode}
          # de quel camp font-ils partie chacun ? 
    ```

107. ``` {.LignePreCode}
          ti, tj = self.guns[i].sens, self.guns[j].sens	   
    ```

108. ``` {.LignePreCode}
          if ti != tj :	     # ils sont de sens opposés : 
    ```

109. ``` {.LignePreCode}
          p = 1	     # on gagne 1 point 
    ```

110. ``` {.LignePreCode}
          else:		 # ils sont dans le même sens : 
    ```

111. ``` {.LignePreCode}
          p = -2	      # on a touché un allié !! 
    ```

112. ``` {.LignePreCode}
          self.pupi[i].attribuerPoint(p) 
    ```

113. ``` {.LignePreCode}
          # celui qui est touché perd de toute façon un point : 
    ```

114. ``` {.LignePreCode}
          self.pupi[j].attribuerPoint(-1) 
    ```

115. ``` {.LignePreCode}
      
    ```

116. ``` {.LignePreCode}
      def dictionnaireCanons(self): 
    ```

117. ``` {.LignePreCode}
          "renvoyer le dictionnaire décrivant les canons présents"  
    ```

118. ``` {.LignePreCode}
          return self.guns 
    ```

119. ``` {.LignePreCode}
      
    ```

120. ``` {.LignePreCode}
    if __name__ =='__main__': 
    ```

121. ``` {.LignePreCode}
      AppBombardes(650,300).mainloop() 
    ```



#### 17-A-4-A - Commentaires {#article.xml#Ld0e70856 .TitreSection3}



![](images/10000000000002980000012C7E1E8330.png)



-   Ligne 6 : La forme d'importation utilisée à la ligne 4 nous permet
    de redéfinir une nouvelle classe **Canon()** dérivée de la
    précédente, tout en lui conservant le même nom. De cette manière,
    les portions de code qui utilisent cette classe ne devront pas être
    modifiées (cela n'aurait pas été possible si nous avions utilisé par
    exemple « **from canon03
    import \*** ».)
-   Lignes 11 à 16 : La méthode définie ici porte le même nom qu'une
    méthode de la classe parente. *Elle va donc remplacer celle-ci dans
    la nouvelle classe* (on pourra dire également que la méthode
    **deplacer()** a été *sur chargée*). Lorsque l'on réalise ce genre
    de modification, on s'efforce en général de faire en sorte que la
    nouvelle méthode effectue le même travail que l'ancienne quand elle
    est invoquée de la même façon que l'était cette dernière. On
    s'assure ainsi que les applications qui utilisaient la classe
    parente pourront aussi utiliser la classe fille, sans devoir être
    elles-mêmes modifiées.\
     Nous obtenons ce résultat en ajoutant un ou plusieurs paramètres,
    dont les valeurs par défaut forceront l'ancien comportement. Ainsi,
    lorsque l'on ne fournit aucun argument pour le paramètre **rel**,
    les paramètres **x** et **y** sont utilisés comme des coordonnées
    absolues (ancien comportement de la méthode). Par contre, si l'on
    fournit pour **rel** un argument « vrai », alors les paramètres
    **x** et **y** sont traités comme des déplacements relatifs (nouveau
    comportement).
-   Lignes 17 à 33 : Les déplacements demandés seront produits
    aléatoirement. Il nous faut donc prévoir un système de barrières
    logicielles, afin d'éviter que l'objet ainsi déplacé ne sorte du
    canevas.
-   Ligne 42 : Nous renvoyons les coordonnées résultantes au programme
    appelant. Il se peut en effet que celui-ci commande un déplacement
    du canon sans connaître sa position initiale.
-   Lignes 44 à 49 : Il s'agit encore une fois de *surcharger* une
    méthode qui existait dans la classe parente, de manière à obtenir un
    comportement différent : après chaque tir, désormais on ne disperse
    plus tous les canons présents, mais seulement celui qui vient de
    tirer.
-   Lignes 51 à 55 : Méthode ajoutée en prévision d'applications qui
    souhaiteraient installer ou retirer des canons au fil du déroulement
    du jeu.
-   Lignes 57 et suivantes : Cette nouvelle classe est conçue dès le
    départ de telle manière qu'elle puisse aisément être dérivée. C'est
    la raison pour laquelle nous avons fragmenté son constructeur en
    deux parties : la méthode **\_\_init\_\_()** contient le code commun
    à tous les objets, aussi bien ceux qui seront instanciés à partir de
    cette classe que ceux qui seront instanciés à partir d'une classe
    dérivée éventuelle. La méthode **specificites()** contient des
    portions de code plus spécifiques : cette méthode est clairement
    destinée à être *surchargée* dans les classes dérivées éventuelles.


[^note_86]: Nous n'hésitons pas à discuter ici le développement d'un logiciel de jeu, parce qu'il s'agit d'un domaine directement accessible à tous, et dans lequel les objectifs concrets sont aisément identifiables. Il va de soi que les mêmes techniques de développement peuvent s'appliquer à d'autres applications plus « sérieuses ».

[^note_87]: Il s'agit d'une suite bureautique complète, libre et gratuite, largement compatible avec MS-Office, disponible pour *Linux, Windows, Mac OS, Solaris*... Le présent manuel a été entièrement rédigé avec son traitement de texte. Vous pouvez vous la procurer par téléchargement depuis le site web : [http://www.openoffice.org](www.openoffice.org "openoffice.org")
