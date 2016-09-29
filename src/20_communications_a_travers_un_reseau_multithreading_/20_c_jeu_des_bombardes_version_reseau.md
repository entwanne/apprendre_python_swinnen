## 20-C - Jeu des bombardes, version réseau



![](images/100000000000034D0000028226D7135A.png)



Au chapitre 15, nous avons commenté le développement d'un petit jeu de
combat dans lequel des joueurs s'affrontaient à l'aide de bombardes.
L'intérêt de ce jeu reste toutefois fort limité, tant qu'il se pratique
sur un seul et même ordinateur. Nous allons donc le perfectionner, en y
intégrant les techniques que nous venons d'apprendre. Comme le système
de « chat » décrit dans les pages précédentes, l'application complète se
composera désormais de deux programmes distincts : un logiciel serveur
qui ne sera mis en fonctionnement que sur une seule machine, et un
logiciel client qui pourra être lancé sur toute une série d'autres.

Du fait du caractère portable de Python, il vous sera même possible
d'organiser des combats de bombardes entre ordinateurs gérés par des
systèmes d'exploitation différents (*Linux ↔ Windows ↔ MacOS !*).

### 20-C-1 - Programme serveur : vue d' ensemble {#article.xml#Ld0e97229 .TitreSection2}

Les programmes serveur et client exploitent la même base logicielle,
elle-même largement récupérée de ce qui avait déjà été mis au point tout
au long du chapitre 15. Nous admettrons donc pour la suite de cet exposé
que les deux versions précédentes du jeu ont été sauvegardées dans les
fichiers-modules **canon03.py** et **canon04.py**, installés dans le
répertoire courant. Nous pouvons en effet réutiliser une bonne partie du
code qu'ils contiennent, en nous servant judicieusement de l'importation
et de l'héritage de classes.

Du module **canon04**, nous allons réutiliser la classe **Canon()**
telle quelle, aussi bien pour le logiciel serveur que pour le logiciel
client. De ce même module, nous importerons également la classe
**AppBombardes()**, dont nous ferons dériver la classe maîtresse de
notre application serveur : **AppServeur()**. Vous constaterez plus loin
que celle-ci produira elle-même la sous-classe **AppClient()**, toujours
par héritage.

Du module **canon03**, nous récupérerons la classe **Pupitre()** dont
nous tirerons une version plus adaptée au « contrôle à distance ».

Enfin, deux nouvelles classes viendront s'ajouter aux précédentes,
chacune spécialisée dans la création d'un objet thread : la classe
**ThreadClients()**, dont une instance surveillera en permanence le
socket destiné à réceptionner les demandes de connexion de nouveaux
clients, et la classe **ThreadConnexion()**, qui servira à créer autant
d'objets sockets que nécessaire pour assurer le dialogue avec chacun des
clients déjà connectés.

Ces nouvelles classes seront inspirées de celles que nous avions
développées pour notre serveur de *chat* dans les pages précédentes. La
principale différence par rapport à celui-ci est que nous devrons
activer un thread spécifique pour le code qui gère l'attente et la prise
en charge des connexions clientes, afin que l'application principale
puisse faire autre chose pendant ce temps.

À partir de là, notre plus gros travail consistera à *développer un
protocole de communication* pour le dialogue entre le serveur et ses
clients. De quoi est-il question ? Tout simplement de définir la teneur
des messages que vont s'échanger les machines connectées. Rassurez-vous
: la mise au point de ce « langage » peut être progressive. On commence
par établir un dialogue de base, puis on y ajoute petit à petit un «
vocabulaire » plus étendu.

L'essentiel de ce travail peut être accompli en s'aidant du logiciel
client développé précédemment pour le système de *chat*. On se sert de
celui-ci pour envoyer des « ordres » au serveur en cours de
développement, et on corrige celui-ci jusqu'à ce qu'il « obéisse » : en
clair, les procédures que l'on met en place progressivement sur le
serveur sont testées au fur et à mesure, en réponse aux messages
correspondants émis « à la main » à partir du client.

### 20-C-2 - Protocole de communication {#article.xml#Ld0e97288 .TitreSection2}

Il va de soi que le protocole décrit ci-après est tout à fait
*arbitraire*. Il serait parfaitement possible de choisir d'autres
conventions complètement différentes. Vous pouvez bien évidemment
critiquer les choix effectués, et vous souhaiterez peut-être même les
remplacer par d'autres, plus efficaces ou plus simples.

Vous savez déjà que les messages échangés sont de simples chaînes
d'octets. Prévoyant que certains de ces messages devront transmettre
plusieurs informations à la fois, nous avons décidé que chacun d'eux
pourrait comporter plusieurs champs, que nous séparerons à l'aide de
virgules. Lors de la réception de l'un quelconque de ces messages, nous
pourrons alors aisément récupérer tous ses composants dans une liste, à
l'aide de la méthode intégrée **split()**.

Voici un exemple de dialogue type, tel qu'il peut être suivi du côté
d'un client. Les messages entre astérisques sont ceux qui sont reçus du
serveur ; les autres sont ceux qui sont émis par le client lui-même :



1.  ``` {.LignePreCode}
    *serveur OK* 
    ```

2.  ``` {.LignePreCode}
    client OK 
    ```

3.  ``` {.LignePreCode}
    *canons,Thread-3;104;228;1;dark red,Thread-2;454;166;-1;dark blue,* 
    ```

4.  ``` {.LignePreCode}
    OK 
    ```

5.  ``` {.LignePreCode}
    *nouveau_canon,Thread-4,481,245,-1,dark green,le_vôtre* 
    ```

6.  ``` {.LignePreCode}
    orienter,25, 
    ```

7.  ``` {.LignePreCode}
    feu 
    ```

8.  ``` {.LignePreCode}
    *mouvement_de,Thread-4,549,280,* 
    ```

9.  ``` {.LignePreCode}
    feu 
    ```

10. ``` {.LignePreCode}
    *mouvement_de,Thread-4,504,278,* 
    ```

11. ``` {.LignePreCode}
    *scores,Thread-4;1,Thread-3;-1,Thread-2;0,* 
    ```

12. ``` {.LignePreCode}
    *angle,Thread-2,23,* 
    ```

13. ``` {.LignePreCode}
    *angle,Thread-2,20,* 
    ```

14. ``` {.LignePreCode}
    *tir_de,Thread-2,* 
    ```

15. ``` {.LignePreCode}
    *mouvement_de,Thread-2,407,191,* 
    ```

16. ``` {.LignePreCode}
    *départ_de,Thread-2* 
    ```

17. ``` {.LignePreCode}
    *nouveau_canon,Thread-5,502,276,-1,dark green* 
    ```



-   Lorsqu'un nouveau client démarre, il envoie une requête de connexion
    au serveur, lequel lui expédie en retour le message : « serveur OK
    ». À la réception de ce dernier, le client répond alors en envoyant
    lui-même : « client OK ». Ce premier échange de politesses n'est pas
    absolument indispensable, mais il permet de vérifier que la
    communication passe bien dans les deux sens. Étant donc averti que
    le client est prêt à travailler, le serveur lui expédie alors une
    description des canons déjà présents dans le jeu (éventuellement
    aucun) : identifiant, emplacement sur le canevas, orientation et
    couleur (ligne 3).
-   En réponse à l'accusé de réception du client (ligne 4), le serveur
    installe un nouveau canon dans l'espace de jeu, puis il signale les
    caractéristiques de cette installation, non seulement au client qui
    l'a provoquée, mais également à tous les autres clients connectés.
    Le message expédié au nouveau client comporte cependant une
    différence (car c'est lui le propriétaire de ce nouveau canon) : en
    plus des caractéristiques du canon, qui sont fournies à tout le
    monde, il comporte un champ supplémentaire contenant simplement «
    le\_vôtre » (comparez par exemple la ligne 5 avec la ligne 17,
    laquelle signale la connexion d'un autre joueur). Cette indication
    supplémentaire permet au client propriétaire du canon de distinguer,
    parmi plusieurs messages similaires éventuels, celui qui contient
    l'identifiant unique que lui a attribué le serveur.
-   Les messages des lignes 6 et 7 sont des commandes envoyées par le
    client (réglage de la hausse et commande de tir). Dans la version
    précédente du jeu, nous avions déjà convenu que les canons se
    déplaceraient quelque peu (et au hasard) après chaque tir. Le
    serveur effectue donc cette opération, et s'empresse ensuite d'en
    faire connaître le résultat à tous les clients connectés. Le message
    reçu du serveur à la ligne 8 est donc l'indication d'un tel
    déplacement (les coordonnées fournies sont les coordonnées
    résultantes pour le canon concerné).
-   La ligne 11 reproduit le type de message expédié par le serveur
    lorsqu'une cible a été touchée. Les nouveaux scores de tous les
    joueurs sont ainsi communiqués à tous les clients.
-   Les messages serveur des lignes 12, 13 et 14 indiquent les actions
    entreprises par un autre joueur (réglage de hausse suivi d'un tir).
    Cette fois encore, le canon concerné est déplacé au hasard après
    qu'il ait tiré (ligne 15).
-   Lignes 16 et 17 : lorsque l'un des clients coupe sa connexion, le
    serveur en avertit tous les autres, afin que le canon correspondant
    disparaisse de l'espace de jeu sur tous les postes. À l'inverse, de
    nouveaux clients peuvent se connecter à tout moment pour participer
    au jeu.

#### 20-C-2-A - Remarques complémentaires {#article.xml#Ld0e97564 .TitreSection3}

Le premier champ de chaque message indique sa teneur. Les messages
envoyés par le client sont très simples : ils correspondent aux
différentes actions entreprises par le joueur (modifications de l'angle
de tir et commandes de feu). Ceux qui sont envoyés par le serveur sont
un peu plus complexes. La plupart d'entre eux sont expédiés à tous les
clients connectés, afin de les tenir informés du déroulement du jeu. En
conséquence, ces messages doivent mentionner l'identifiant du joueur qui
a commandé une action ou qui est concerné par un changement quelconque.
Nous avons vu plus haut que ces identifiants sont des noms générés
automatiquement par le gestionnaire de threads du serveur, chaque fois
qu'un nouveau client se connecte.

Certains messages concernant l'ensemble du jeu contiennent plusieurs
informations par champ. Dans ce cas, les différents « sous-champs » sont
séparés par des points-virgules (lignes 3 et 11).

### 20-C-3 - Programme serveur : première partie {#article.xml#Ld0e97571 .TitreSection2}

Vous trouverez dans les pages qui suivent le script complet du programme
serveur. Nous vous le présentons en trois morceaux successifs afin de
rapprocher les commentaires du code correspondant, mais la numérotation
de ses lignes est continue. Bien qu'il soit déjà relativement long et
complexe, vous estimerez probablement qu'il mérite d'être encore
perfectionné, notamment au niveau de la présentation générale. Nous vous
laisserons le soin d'y ajouter vous-même tous les compléments qui vous
sembleront utiles (par exemple, une proposition de choisir les
coordonnées de la machine hôte au démarrage, une barre de menus, etc.) :



1.  ``` {.LignePreCode}
    ####################################################### 
    ```

2.  ``` {.LignePreCode}
    # Jeu des bombardes - partie serveur		 # 
    ```

3.  ``` {.LignePreCode}
    # (C) Gérard Swinnen, Verviers (Belgique) - July 2004 # 
    ```

4.  ``` {.LignePreCode}
    # Licence : GPL 	       rév. 2010 # 
    ```

5.  ``` {.LignePreCode}
    # Avant d'exécuter ce script, vérifiez que l'adresse  # 
    ```

6.  ``` {.LignePreCode}
    # IP ci-dessous soit bien celle de la machine hôte.   # 
    ```

7.  ``` {.LignePreCode}
    # Vous pouvez choisir un numéro de port différent, ou # 
    ```

8.  ``` {.LignePreCode}
    # changer les dimensions de l'espace de jeu.	     # 
    ```

9.  ``` {.LignePreCode}
    # Dans tous les cas, vérifiez que les mêmes choix ont # 
    ```

10. ``` {.LignePreCode}
    # été effectués pour chacun des scripts clients.      # 
    ```

11. ``` {.LignePreCode}
    ####################################################### 
    ```

12. ``` {.LignePreCode}
      
    ```

13. ``` {.LignePreCode}
    host, port = '192.168.1.168', 36000 
    ```

14. ``` {.LignePreCode}
    largeur, hauteur = 700, 400	   # dimensions de l'espace de jeu 
    ```

15. ``` {.LignePreCode}
      
    ```

16. ``` {.LignePreCode}
    from tkinter import * 
    ```

17. ``` {.LignePreCode}
    import socket, sys, threading, time 
    ```

18. ``` {.LignePreCode}
    import canon03 
    ```

19. ``` {.LignePreCode}
    from canon04 import Canon, AppBombardes 
    ```

20. ``` {.LignePreCode}
      
    ```

21. ``` {.LignePreCode}
    class Pupitre(canon03.Pupitre): 
    ```

22. ``` {.LignePreCode}
      """Pupitre de pointage amélioré""" 
    ```

23. ``` {.LignePreCode}
      def __init__(self, boss, canon): 
    ```

24. ``` {.LignePreCode}
          canon03.Pupitre.__init__(self, boss, canon) 
    ```

25. ``` {.LignePreCode}
      
    ```

26. ``` {.LignePreCode}
      def tirer(self): 
    ```

27. ``` {.LignePreCode}
          "déclencher le tir du canon associé" 
    ```

28. ``` {.LignePreCode}
          self.appli.tir_canon(self.canon.id) 
    ```

29. ``` {.LignePreCode}
      
    ```

30. ``` {.LignePreCode}
      def orienter(self, angle): 
    ```

31. ``` {.LignePreCode}
          "ajuster la hausse du canon associé" 
    ```

32. ``` {.LignePreCode}
          self.appli.orienter_canon(self.canon.id, angle) 
    ```

33. ``` {.LignePreCode}
      
    ```

34. ``` {.LignePreCode}
      def valeur_score(self, sc =None): 
    ```

35. ``` {.LignePreCode}
          "imposer un nouveau score , ou lire le score existant" 
    ```

36. ``` {.LignePreCode}
          if sc == None: 
    ```

37. ``` {.LignePreCode}
          return self.score 
    ```

38. ``` {.LignePreCode}
          else: 
    ```

39. ``` {.LignePreCode}
          self.score =sc 
    ```

40. ``` {.LignePreCode}
          self.points.config(text = ' %s ' % self.score) 
    ```

41. ``` {.LignePreCode}
      
    ```

42. ``` {.LignePreCode}
      def inactiver(self): 
    ```

43. ``` {.LignePreCode}
          "désactiver le bouton de tir et le système de réglage d'angle" 
    ```

44. ``` {.LignePreCode}
          self.bTir.config(state =DISABLED) 
    ```

45. ``` {.LignePreCode}
          self.regl.config(state =DISABLED) 
    ```

46. ``` {.LignePreCode}
      
    ```

47. ``` {.LignePreCode}
      def activer(self): 
    ```

48. ``` {.LignePreCode}
          "activer le bouton de tir et le système de réglage d'angle" 
    ```

49. ``` {.LignePreCode}
          self.bTir.config(state =NORMAL) 
    ```

50. ``` {.LignePreCode}
          self.regl.config(state =NORMAL) 
    ```

51. ``` {.LignePreCode}
      
    ```

52. ``` {.LignePreCode}
      def reglage(self, angle): 
    ```

53. ``` {.LignePreCode}
          "changer la position du curseur de réglage" 
    ```

54. ``` {.LignePreCode}
          self.regl.config(state =NORMAL) 
    ```

55. ``` {.LignePreCode}
          self.regl.set(angle) 
    ```

56. ``` {.LignePreCode}
          self.regl.config(state =DISABLED) 
    ```



-   La classe **Pupitre()** est construite par dérivation de la classe
    de même nom importée du module **canon03**. Elle hérite donc toutes
    les caractéristiques de celle-ci, mais nous devons surcharger[^note_108]
    ses méthodes **tirer()** et **orienter().**
-   Dans la version monoposte du logiciel, en effet, chacun des pupitres
    pouvait commander directement l'objet canon correspondant. Dans
    cette version réseau, par contre, ce sont les clients qui contrôlent
    à distance le fonctionnement des canons. Par conséquent, les
    pupitres qui apparaissent dans la fenêtre du serveur ne peuvent être
    que de simples répétiteurs des manœuvres effectuées par les joueurs
    sur chaque client. Le bouton de tir et le curseur de réglage de la
    hausse sont donc désactivés, mais les indications fournies obéissent
    aux injonctions qui leur sont adressées par l'application
    principale.
-   Cette nouvelle classe **Pupitre()** sera également utilisée telle
    quelle dans chaque exemplaire du programme client. Dans la fenêtre
    de celui-ci comme dans celle du serveur, tous les pupitres seront
    affichés comme des répétiteurs, mais l'un d'entre eux cependant sera
    complètement fonctionnel : celui qui correspond au canon du joueur.
-   Toutes ces raisons expliquent également l'apparition des nouvelles
    méthodes **activer()**, **desactiver()**, **reglage()** et
    **valeur\_score()**, qui seront elles aussi invoquées par
    l'application principale, en réponse aux messages-instructions
    échangés entre le serveur et ses clients.
-   La classe **ThreadConnexion()** ci-dessous sert à instancier la
    série d'objets threads qui s'occuperont en parallèle de toutes les
    connexions lancées par les clients. Sa méthode **run()** contient la
    fonctionnalité centrale du serveur, à savoir la boucle
    d'instructions qui gère la réception des messages provenant d'un
    client particulier, lesquels entraînent chacun toute une cascade de
    réactions. Vous y trouverez la mise en œuvre concrète du protocole
    de communication décrit dans les pages précédentes (certains
    messages étant cependant générés par les méthodes
    **depl\_aleat\_canon()** et **goal()** de la classe **AppServeur()**
    décrite plus loin).\



1.  ``` {.LignePreCode}
    class ThreadConnexion(threading.Thread): 
    ```

2.  ``` {.LignePreCode}
      """objet thread gestionnaire d'une connexion client""" 
    ```

3.  ``` {.LignePreCode}
      def __init__(self, boss, conn): 
    ```

4.  ``` {.LignePreCode}
          threading.Thread.__init__(self) 
    ```

5.  ``` {.LignePreCode}
          self.connexion = conn	     # réf. du socket de connexion 
    ```

6.  ``` {.LignePreCode}
          self.app = boss		   # réf. de la fenêtre application 
    ```

7.  ``` {.LignePreCode}
      
    ```

8.  ``` {.LignePreCode}
      def run(self): 
    ```

9.  ``` {.LignePreCode}
          "actions entreprises en réponse aux messages reçus du client" 
    ```

10. ``` {.LignePreCode}
          nom = self.getName()	    # id. du client = nom du thread 
    ```

11. ``` {.LignePreCode}
          while 1: 
    ```

12. ``` {.LignePreCode}
          msgClient = self.connexion.recv(1024).decode("Utf8") 
    ```

13. ``` {.LignePreCode}
          print("**{}** de {}".format(msgClient, nom)) 
    ```

14. ``` {.LignePreCode}
          deb = msgClient.split(',')[0] 
    ```

15. ``` {.LignePreCode}
          if deb == "fin" or deb =="": 
    ```

16. ``` {.LignePreCode}
    	  self.app.enlever_canon(nom) 
    ```

17. ``` {.LignePreCode}
    	  # signaler le départ de ce canon aux autres clients : 
    ```

18. ``` {.LignePreCode}
    	  self.app.verrou.acquire() 
    ```

19. ``` {.LignePreCode}
    	  for cli in self.app.conn_client: 
    ```

20. ``` {.LignePreCode}
    	  if cli != nom: 
    ```

21. ``` {.LignePreCode}
    	      message = "départ_de,{}".format(nom) 
    ```

22. ``` {.LignePreCode}
    	      self.app.conn_client[cli].send(message.encode("Utf8")) 
    ```

23. ``` {.LignePreCode}
    	  self.app.verrou.release() 
    ```

24. ``` {.LignePreCode}
    	  # fermer le présent thread : 
    ```

25. ``` {.LignePreCode}
    	  break 
    ```

26. ``` {.LignePreCode}
          elif deb =="client OK": 
    ```

27. ``` {.LignePreCode}
    	  # signaler au nouveau client les canons déjà enregistrés : 
    ```

28. ``` {.LignePreCode}
    	  msg ="canons," 
    ```

29. ``` {.LignePreCode}
    	  for g in self.app.guns: 
    ```

30. ``` {.LignePreCode}
    	  gun = self.app.guns[g] 
    ```

31. ``` {.LignePreCode}
    	  msg =msg +"{};{};{};{};{},".\ 
    ```

32. ``` {.LignePreCode}
    	      format(gun.id, gun.x1, gun.y1, gun.sens, gun.coul) 
    ```

33. ``` {.LignePreCode}
    	  self.app.verrou.acquire() 
    ```

34. ``` {.LignePreCode}
    	  self.connexion.send(msg.encode("Utf8")) 
    ```

35. ``` {.LignePreCode}
    	  # attendre un accusé de réception ('OK') : 
    ```

36. ``` {.LignePreCode}
    	  self.connexion.recv(100).decode("Utf8") 
    ```

37. ``` {.LignePreCode}
    	  self.app.verrou.release() 
    ```

38. ``` {.LignePreCode}
    	  # ajouter un canon dans l'espace de jeu serveur. 
    ```

39. ``` {.LignePreCode}
    	  # la méthode invoquée renvoie les caract. du canon créé : 
    ```

40. ``` {.LignePreCode}
    	  x, y, sens, coul = self.app.ajouter_canon(nom) 
    ```

41. ``` {.LignePreCode}
    	  # signaler les caract. de ce nouveau canon à tous les 
    ```

42. ``` {.LignePreCode}
    	  # clients déjà connectés : 
    ```

43. ``` {.LignePreCode}
    	  self.app.verrou.acquire() 
    ```

44. ``` {.LignePreCode}
    	  for cli in self.app.conn_client: 
    ```

45. ``` {.LignePreCode}
    	  msg ="nouveau_canon,{},{},{},{},{}".\ 
    ```

46. ``` {.LignePreCode}
    	      format(nom, x, y, sens, coul) 
    ```

47. ``` {.LignePreCode}
    	  # pour le nouveau client, ajouter un champ indiquant 
    ```

48. ``` {.LignePreCode}
    	  # que le message concerne son propre canon : 
    ```

49. ``` {.LignePreCode}
    	  if cli == nom: 
    ```

50. ``` {.LignePreCode}
    	      msg =msg +",le_vôtre" 
    ```

51. ``` {.LignePreCode}
    	  self.app.conn_client[cli].send(msg.encode("Utf8")) 
    ```

52. ``` {.LignePreCode}
    	  self.app.verrou.release() 
    ```

53. ``` {.LignePreCode}
          elif deb =='feu': 
    ```

54. ``` {.LignePreCode}
    	  self.app.tir_canon(nom) 
    ```

55. ``` {.LignePreCode}
    	  # Signaler ce tir à tous les autres clients : 
    ```

56. ``` {.LignePreCode}
    	  self.app.verrou.acquire() 
    ```

57. ``` {.LignePreCode}
    	  for cli in self.app.conn_client: 
    ```

58. ``` {.LignePreCode}
    	  if cli != nom: 
    ```

59. ``` {.LignePreCode}
    	      message = "tir_de,{},".format(nom) 
    ```

60. ``` {.LignePreCode}
    	      self.app.conn_client[cli].send(message.encode("Utf8")) 
    ```

61. ``` {.LignePreCode}
    	  self.app.verrou.release() 
    ```

62. ``` {.LignePreCode}
          elif deb =="orienter": 
    ```

63. ``` {.LignePreCode}
    	  t =msgClient.split(',') 
    ```

64. ``` {.LignePreCode}
    	  # on peut avoir reçu plusieurs angles. utiliser le dernier : 
    ```

65. ``` {.LignePreCode}
    	  self.app.orienter_canon(nom, t[-1]) 
    ```

66. ``` {.LignePreCode}
    	  # Signaler ce changement à tous les autres clients : 
    ```

67. ``` {.LignePreCode}
    	  self.app.verrou.acquire() 
    ```

68. ``` {.LignePreCode}
    	  for cli in self.app.conn_client: 
    ```

69. ``` {.LignePreCode}
    	  if cli != nom: 
    ```

70. ``` {.LignePreCode}
    	      # virgule terminale, car messages parfois groupés : 
    ```

71. ``` {.LignePreCode}
    	      message = "angle,{},{},".format(nom, t[-1]) 
    ```

72. ``` {.LignePreCode}
    	      self.app.conn_client[cli].send(message.encode("Utf8")) 
    ```

73. ``` {.LignePreCode}
    	  self.app.verrou.release() 
    ```

74. ``` {.LignePreCode}
      
    ```

75. ``` {.LignePreCode}
          # Fermeture de la connexion : 
    ```

76. ``` {.LignePreCode}
          self.connexion.close()	      # couper la connexion 
    ```

77. ``` {.LignePreCode}
          del self.app.conn_client[nom]   # suppr. sa réf. dans le dictionnaire 
    ```

78. ``` {.LignePreCode}
          self.app.afficher("Client %s déconnecté.\n" % nom) 
    ```

79. ``` {.LignePreCode}
          # Le thread se termine ici 
    ```



### 20-C-4 - Synchronisation de threads concurrents à l'aide de verrous (thread locks) {#article.xml#Ld0e100304 .TitreSection2}

Au cours de votre examen du code ci-dessus, vous aurez certainement
remarqué la structure particulière des blocs d'instructions par
lesquelles le serveur expédie un même message à tous ses clients.
Considérez par exemple les lignes 74 à 80.

La ligne 75 active la méthode **acquire()** d'un objet « verrou » qui a
été créé par le constructeur de l'application principale (voir plus
loin). Cet objet est une instance de la classe **Lock()**, laquelle fait
partie du module **threading** que nous avons importé en début de
script. Les lignes suivantes (76 à 79) provoquent l'envoi d'un message à
tous les clients connectés (sauf un). Ensuite, l'objet-verrou est à
nouveau sollicité, cette fois pour sa méthode **release()**.

À quoi cet objet-verrou peut-il donc bien servir ? Puisqu'il est produit
par une classe du module **threading**, vous pouvez deviner que son
utilité concerne les threads. En fait, de tels objets-verrous servent à
synchroniser les *threads concurrents*. De quoi s'agit-il ?

Vous savez que le serveur démarre un thread différent pour chacun des
clients qui se connecte. Ensuite, tous ces threads fonctionnent en
parallèle. Il existe donc un risque que, de temps à autre, deux ou
plusieurs de ces threads essaient d'utiliser une ressource commune en
même temps.

Dans les lignes de code que nous venons de discuter, par exemple, nous
avons affaire à un thread qui souhaite exploiter quasiment toutes les
connexions présentes pour poster un message. Il est donc parfaitement
possible que, pendant ce temps, un autre thread tente d'exploiter lui
aussi l'une ou l'autre de ces connexions, ce qui risque de provoquer un
dysfonctionnement (en l'occurrence, la superposition chaotique de
plusieurs messages).

Un tel problème de *concurrence entre threads* peut être résolu par
l'utilisation d'un objet-verrou (*thread lock*). Un tel objet n'est créé
qu'en un seul exemplaire, dans un espace de noms accessible à tous les
threads concurrents. Il se caractérise essentiellement par le fait qu'il
se trouve toujours dans l'un ou l'autre de deux états : soit
*verrouillé*, soit *déverrouillé*. Son état initial est l'état
déverrouillé.

#### 20-C-4-A - Utilisation {#article.xml#Ld0e100349 .TitreSection3}

Lorsqu'un thread quelconque s'apprête à accéder à une ressource commune,
il active d'abord la méthode **acquire()** du verrou. Si celui-ci était
dans l'état déverrouillé, il se verrouille, et le thread demandeur peut
alors utiliser la ressource commune, en toute tranquillité. Lorsqu'il
aura fini d'utiliser la ressource, il s'empressera cependant d'activer
la méthode **release()** du verrou, ce qui le fera repasser dans l'état
déverrouillé.

En effet, si un autre thread concurrent essaie d'activer lui aussi la
méthode **acquire()** du verrou, alors que celui-ci est dans l'état
verrouillé, la méthode « ne rend pas la main », provoquant le blocage de
ce thread, lequel suspend donc son activité jusqu'à ce que le verrou
repasse dans l'état déverrouillé. Ceci l'empêche donc d'accéder à la
ressource commune durant tout le temps où un autre thread s'en sert.
Lorsque le verrou est déverrouillé, l'un des threads en attente (il peut
en effet y en avoir plusieurs) reprend alors son activité tout en
refermant le verrou, et ainsi de suite.

L'objet-verrou mémorise les références des threads bloqués, de manière à
n'en débloquer qu'un seul à la fois lorsque sa méthode **release()** est
invoquée. Il faut donc toujours veiller à ce que chaque thread qui
active la méthode **acquire()** du verrou avant d'accéder à une
ressource, active également sa méthode **release()** peu après.

Pour autant que tous les threads concurrents respectent la même
procédure, cette technique simple empêche donc qu'une ressource commune
soit exploitée en même temps par plusieurs d'entre eux. On dira dans ce
cas que les threads ont été *synchronisés*.

### 20-C-5 - Programme serveur : suite et fin {#article.xml#Ld0e100381 .TitreSection2}

Les deux classes ci-dessous complètent le script serveur. Le code
implémenté dans la classe **ThreadClients()** est assez similaire à
celui que nous avions développé précédemment pour le corps d'application
du logiciel de *Chat*. Dans le cas présent, toutefois, nous le plaçons
dans une classe dérivée de **Thread()**, parce que devons faire
fonctionner ce code dans un thread indépendant de celui de l'application
principale. Celui-ci est en effet déjà complètement accaparé par la
boucle **mainloop()** de l'interface graphique[^note_109].

La classe **AppServeur()** dérive de la classe **AppBombardes()** du
module **canon04**. Nous lui avons ajouté un ensemble de méthodes
complémentaires destinées à exécuter toutes les opérations qui
résulteront du dialogue entamé avec les clients. Nous avons déjà signalé
plus haut que les clients instancieront chacun une version dérivée de
cette classe (afin de profiter des mêmes définitions de base pour la
fenêtre, le canevas, etc.).



1.  ``` {.LignePreCode}
    class ThreadClients(threading.Thread): 
    ```

2.  ``` {.LignePreCode}
      """objet thread gérant la connexion de nouveaux clients""" 
    ```

3.  ``` {.LignePreCode}
      def __init__(self, boss, connex): 
    ```

4.  ``` {.LignePreCode}
          threading.Thread.__init__(self) 
    ```

5.  ``` {.LignePreCode}
          self.boss = boss		 # réf. de la fenêtre application 
    ```

6.  ``` {.LignePreCode}
          self.connex = connex	    # réf. du socket initial 
    ```

7.  ``` {.LignePreCode}
      
    ```

8.  ``` {.LignePreCode}
      def run(self): 
    ```

9.  ``` {.LignePreCode}
          "attente et prise en charge de nouvelles connexions clientes" 
    ```

10. ``` {.LignePreCode}
          txt ="Serveur prêt, en attente de requêtes ...\n" 
    ```

11. ``` {.LignePreCode}
          self.boss.afficher(txt) 
    ```

12. ``` {.LignePreCode}
          self.connex.listen(5) 
    ```

13. ``` {.LignePreCode}
          # Gestion des connexions demandées par les clients : 
    ```

14. ``` {.LignePreCode}
          while 1: 
    ```

15. ``` {.LignePreCode}
          nouv_conn, adresse = self.connex.accept() 
    ```

16. ``` {.LignePreCode}
          # Créer un nouvel objet thread pour gérer la connexion : 
    ```

17. ``` {.LignePreCode}
          th = ThreadConnexion(self.boss, nouv_conn) 
    ```

18. ``` {.LignePreCode}
          th.start() 
    ```

19. ``` {.LignePreCode}
          it = th.getName()       # identifiant unique du thread 
    ```

20. ``` {.LignePreCode}
          # Mémoriser la connexion dans le dictionnaire : 
    ```

21. ``` {.LignePreCode}
          self.boss.enregistrer_connexion(nouv_conn, it) 
    ```

22. ``` {.LignePreCode}
          # Afficher : 
    ```

23. ``` {.LignePreCode}
          txt = "Client %s connecté, adresse IP %s, port %s.\n" %\ 
    ```

24. ``` {.LignePreCode}
    	 (it, adresse[0], adresse[1]) 
    ```

25. ``` {.LignePreCode}
          self.boss.afficher(txt) 
    ```

26. ``` {.LignePreCode}
          # Commencer le dialogue avec le client : 
    ```

27. ``` {.LignePreCode}
          nouv_conn.send("serveur OK".encode("Utf8")) 
    ```

28. ``` {.LignePreCode}
      
    ```

29. ``` {.LignePreCode}
    class AppServeur(AppBombardes): 
    ```

30. ``` {.LignePreCode}
      """fenêtre principale de l'application (serveur ou client)""" 
    ```

31. ``` {.LignePreCode}
      def __init__(self, host, port, larg_c, haut_c): 
    ```

32. ``` {.LignePreCode}
          self.host, self.port = host, port 
    ```

33. ``` {.LignePreCode}
          AppBombardes.__init__(self, larg_c, haut_c) 
    ```

34. ``` {.LignePreCode}
          self.active =1	      # témoin d'activité 
    ```

35. ``` {.LignePreCode}
          # veiller à quitter proprement si l'on referme la fenêtre : 
    ```

36. ``` {.LignePreCode}
          self.bind('<Destroy>',self.fermer_threads) 
    ```

37. ``` {.LignePreCode}
      
    ```

38. ``` {.LignePreCode}
      def specificites(self): 
    ```

39. ``` {.LignePreCode}
          "préparer les objets spécifiques de la partie serveur" 
    ```

40. ``` {.LignePreCode}
          self.master.title('<<< Serveur pour le jeu des bombardes >>>') 
    ```

41. ``` {.LignePreCode}
      
    ```

42. ``` {.LignePreCode}
          # widget Text, associé à une barre de défilement : 
    ```

43. ``` {.LignePreCode}
          st =Frame(self) 
    ```

44. ``` {.LignePreCode}
          self.avis =Text(st, width =65, height =5) 
    ```

45. ``` {.LignePreCode}
          self.avis.pack(side =LEFT) 
    ```

46. ``` {.LignePreCode}
          scroll =Scrollbar(st, command =self.avis.yview) 
    ```

47. ``` {.LignePreCode}
          self.avis.configure(yscrollcommand =scroll.set) 
    ```

48. ``` {.LignePreCode}
          scroll.pack(side =RIGHT, fill =Y) 
    ```

49. ``` {.LignePreCode}
          st.pack() 
    ```

50. ``` {.LignePreCode}
      
    ```

51. ``` {.LignePreCode}
          # partie serveur réseau : 
    ```

52. ``` {.LignePreCode}
          self.conn_client = {}	     # dictionn. des connexions clients 
    ```

53. ``` {.LignePreCode}
          self.verrou =threading.Lock()   # verrou pour synchroniser threads 
    ```

54. ``` {.LignePreCode}
          # Initialisation du serveur - Mise en place du socket : 
    ```

55. ``` {.LignePreCode}
          connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    ```

56. ``` {.LignePreCode}
          try: 
    ```

57. ``` {.LignePreCode}
          connexion.bind((self.host, self.port)) 
    ```

58. ``` {.LignePreCode}
          except socket.error: 
    ```

59. ``` {.LignePreCode}
          txt ="La liaison du socket à l'hôte %s, port %s a échoué.\n" %\ 
    ```

60. ``` {.LignePreCode}
    	 (self.host, self.port) 
    ```

61. ``` {.LignePreCode}
          self.avis.insert(END, txt) 
    ```

62. ``` {.LignePreCode}
          self.accueil =None 
    ```

63. ``` {.LignePreCode}
          else: 
    ```

64. ``` {.LignePreCode}
          # démarrage du thread guettant la connexion des clients : 
    ```

65. ``` {.LignePreCode}
          self.accueil = ThreadClients(self, connexion) 
    ```

66. ``` {.LignePreCode}
          self.accueil.start() 
    ```

67. ``` {.LignePreCode}
      
    ```

68. ``` {.LignePreCode}
      def depl_aleat_canon(self, id): 
    ```

69. ``` {.LignePreCode}
          "déplacer aléatoirement le canon " 
    ```

70. ``` {.LignePreCode}
          x, y = AppBombardes.depl_aleat_canon(self, id) 
    ```

71. ``` {.LignePreCode}
          # signaler ces nouvelles coord. à tous les clients : 
    ```

72. ``` {.LignePreCode}
          self.verrou.acquire() 
    ```

73. ``` {.LignePreCode}
          for cli in self.conn_client: 
    ```

74. ``` {.LignePreCode}
          message = "mouvement_de,%s,%s,%s," % (id, x, y) 
    ```

75. ``` {.LignePreCode}
          self.conn_client[cli].send(message.encode("Utf8")) 
    ```

76. ``` {.LignePreCode}
          self.verrou.release() 
    ```

77. ``` {.LignePreCode}
      
    ```

78. ``` {.LignePreCode}
      def goal(self, i, j): 
    ```

79. ``` {.LignePreCode}
          "le canon  signale qu'il a atteint l'adversaire " 
    ```

80. ``` {.LignePreCode}
          AppBombardes.goal(self, i, j) 
    ```

81. ``` {.LignePreCode}
          # Signaler les nouveaux scores à tous les clients : 
    ```

82. ``` {.LignePreCode}
          self.verrou.acquire() 
    ```

83. ``` {.LignePreCode}
          for cli in self.conn_client: 
    ```

84. ``` {.LignePreCode}
          msg ='scores,' 
    ```

85. ``` {.LignePreCode}
          for id in self.pupi: 
    ```

86. ``` {.LignePreCode}
    	  sc = self.pupi[id].valeur_score() 
    ```

87. ``` {.LignePreCode}
    	  msg = msg +"%s;%s," % (id, sc) 
    ```

88. ``` {.LignePreCode}
          self.conn_client[cli].send(msg.encode("Utf8")) 
    ```

89. ``` {.LignePreCode}
          time.sleep(.5)	       # pour mieux séparer les messages 
    ```

90. ``` {.LignePreCode}
          self.verrou.release() 
    ```

91. ``` {.LignePreCode}
      
    ```

92. ``` {.LignePreCode}
      def ajouter_canon(self, id): 
    ```

93. ``` {.LignePreCode}
          "instancier un canon et un pupitre de nom  dans 2 dictionnaires" 
    ```

94. ``` {.LignePreCode}
          # on alternera ceux des 2 camps : 
    ```

95. ``` {.LignePreCode}
          n = len(self.guns) 
    ```

96. ``` {.LignePreCode}
          if n %2 ==0: 
    ```

97. ``` {.LignePreCode}
          sens = -1 
    ```

98. ``` {.LignePreCode}
          else: 
    ```

99. ``` {.LignePreCode}
          sens = 1 
    ```

100. ``` {.LignePreCode}
          x, y = self.coord_aleat(sens) 
    ```

101. ``` {.LignePreCode}
          coul =('dark blue', 'dark red', 'dark green', 'purple', 
    ```

102. ``` {.LignePreCode}
    	 'dark cyan', 'red', 'cyan', 'orange', 'blue', 'violet')[n] 
    ```

103. ``` {.LignePreCode}
          self.guns[id] = Canon(self.jeu, id, x, y, sens, coul) 
    ```

104. ``` {.LignePreCode}
          self.pupi[id] = Pupitre(self, self.guns[id]) 
    ```

105. ``` {.LignePreCode}
          self.pupi[id].inactiver() 
    ```

106. ``` {.LignePreCode}
          return (x, y, sens, coul) 
    ```

107. ``` {.LignePreCode}
      
    ```

108. ``` {.LignePreCode}
      def enlever_canon(self, id): 
    ```

109. ``` {.LignePreCode}
          "retirer le canon et le pupitre dont l'identifiant est " 
    ```

110. ``` {.LignePreCode}
          if self.active == 0:	# la fenêtre a été refermée 
    ```

111. ``` {.LignePreCode}
          return 
    ```

112. ``` {.LignePreCode}
          self.guns[id].effacer() 
    ```

113. ``` {.LignePreCode}
          del self.guns[id] 
    ```

114. ``` {.LignePreCode}
          self.pupi[id].destroy() 
    ```

115. ``` {.LignePreCode}
          del self.pupi[id] 
    ```

116. ``` {.LignePreCode}
      
    ```

117. ``` {.LignePreCode}
      def orienter_canon(self, id, angle): 
    ```

118. ``` {.LignePreCode}
          "régler la hausse du canon  à la valeur " 
    ```

119. ``` {.LignePreCode}
          self.guns[id].orienter(angle) 
    ```

120. ``` {.LignePreCode}
          self.pupi[id].reglage(angle) 
    ```

121. ``` {.LignePreCode}
      
    ```

122. ``` {.LignePreCode}
      def tir_canon(self, id): 
    ```

123. ``` {.LignePreCode}
          "déclencher le tir du canon " 
    ```

124. ``` {.LignePreCode}
          self.guns[id].feu() 
    ```

125. ``` {.LignePreCode}
      
    ```

126. ``` {.LignePreCode}
      def enregistrer_connexion(self, conn, it): 
    ```

127. ``` {.LignePreCode}
          "Mémoriser la connexion dans un dictionnaire" 
    ```

128. ``` {.LignePreCode}
          self.conn_client[it] = conn 
    ```

129. ``` {.LignePreCode}
      
    ```

130. ``` {.LignePreCode}
      def afficher(self, txt): 
    ```

131. ``` {.LignePreCode}
          "afficher un message dans la zone de texte" 
    ```

132. ``` {.LignePreCode}
          self.avis.insert(END, txt) 
    ```

133. ``` {.LignePreCode}
      
    ```

134. ``` {.LignePreCode}
      def fermer_threads(self, evt): 
    ```

135. ``` {.LignePreCode}
          "couper les connexions existantes et fermer les threads" 
    ```

136. ``` {.LignePreCode}
          # couper les connexions établies avec tous les clients : 
    ```

137. ``` {.LignePreCode}
          for id in self.conn_client: 
    ```

138. ``` {.LignePreCode}
          self.conn_client[id].send('fin'.encode("Utf8")) 
    ```

139. ``` {.LignePreCode}
          # forcer la terminaison du thread serveur qui attend les requêtes : 
    ```

140. ``` {.LignePreCode}
          if self.accueil != None: 
    ```

141. ``` {.LignePreCode}
          self.accueil._stop() 
    ```

142. ``` {.LignePreCode}
          self.active =0		  # empêcher accès ultérieurs à Tk 
    ```

143. ``` {.LignePreCode}
      
    ```

144. ``` {.LignePreCode}
    if __name__ =='__main__': 
    ```

145. ``` {.LignePreCode}
      AppServeur(host, port, largeur, hauteur).mainloop() 
    ```



#### 20-C-5-A - Commentaires {#article.xml#Ld0e103141 .TitreSection3}

-   Ligne 173 : Il vous arrivera de temps à autre de vouloir «
    intercepter » l'ordre de fermeture de l'application que
    l'utilisateur déclenche en quittant votre programme, par exemple
    parce que vous voulez forcer la sauvegarde de données importantes
    dans un fichier, ou fermer aussi d'autres fenêtres, etc. Il suffit
    pour ce faire de détecter l'événement `<Destroy>`, comme nous le faisons
    ici pour forcer la terminaison de tous les threads actifs.
-   Lignes 179 à 186 : Au passage, vous revoyez ici la technique
    d'association d'une barre de défilement à un widget **Text** (Voir
    aussi page ).
-   Ligne 190 : Instanciation de l'objet-verrou permettant de
    synchroniser les threads.
-   Lignes 202-203 : Instanciation de l'objet thread qui attendra en
    permanence les demandes de connexion des clients potentiels.
-   Lignes 205 à 213, 215 à 227 : Ces méthodes *surchargent* les
    méthodes de même nom héritées de leur classe parente. Elles
    commencent par invoquer celles-ci pour effectuer le même travail
    (lignes 207, 217), puis ajoutent leur fonctionnalité propre,
    laquelle consiste à signaler à tout le monde ce qui vient de se
    passer.
-   Lignes 229 à 243 : Cette méthode instancie un nouveau poste de tir
    chaque fois qu'un nouveau client se connecte. Les canons sont placés
    alternativement dans le camp de droite et dans celui de gauche,
    procédure qui pourrait bien évidemment être améliorée. La liste des
    couleurs prévues limite le nombre de clients à 10, ce qui devrait
    suffire.

### 20-C-6 - Programme client {#article.xml#Ld0e103167 .TitreSection2}

Le script correspondant au logiciel client est reproduit ci-après. Comme
celui qui correspond au serveur, il est relativement court, parce qu'il
utilise lui aussi l'importation de modules et l'héritage de classes. Le
script serveur doit avoir été sauvegardé dans un fichier-module nommé
**canon\_serveur.py**. Ce fichier doit être placé dans le répertoire
courant, de même que les fichiers-modules **canon03.py** et
**canon04.py** qu'il utilise lui-même.

De ces modules ainsi importés, le présent script utilise les classes
**Canon()** et **Pupitre()** à l'identique, ainsi qu'une forme dérivée
de la classe **AppServeur()**. Dans cette dernière, de nombreuses
méthodes ont été surchargées, afin d'adapter leur fonctionnalité.
Considérez par exemple les méthodes **goal()** et
**depl\_aleat\_canon()**, dont la variante surchargée ne fait plus rien
du tout (instruction **pass**), parce que le calcul des scores et le
repositionnement des canons après chaque tir ne peuvent être effectués
que sur le serveur seulement.

C'est dans la méthode **run()** de la classe **ThreadSocket()** (lignes
86 à 126) que se trouve le code traitant les messages échangés avec le
serveur. Nous y avons d'ailleurs laissé une instruction **print** (à la
ligne 88) afin que les messages reçus du serveur apparaissent sur la
sortie standard. Si vous réalisez vous-même une forme plus définitive de
ce jeu, vous pourrez bien évidemment supprimer cette instruction.



1.  ``` {.LignePreCode}
    ####################################################### 
    ```

2.  ``` {.LignePreCode}
    # Jeu des bombardes - partie cliente		 # 
    ```

3.  ``` {.LignePreCode}
    # (C) Gérard Swinnen, Liège (Belgique) - Juillet 2004 # 
    ```

4.  ``` {.LignePreCode}
    # Licence : GPL 	     Révis.  2010 # 
    ```

5.  ``` {.LignePreCode}
    # Avant d'exécuter ce script, vérifiez que l'adresse, # 
    ```

6.  ``` {.LignePreCode}
    # le numéro de port et les dimensions de l'espace de  # 
    ```

7.  ``` {.LignePreCode}
    # jeu indiquées ci-dessous correspondent exactement   # 
    ```

8.  ``` {.LignePreCode}
    # à ce qui a été défini pour le serveur.	 # 
    ```

9.  ``` {.LignePreCode}
    ####################################################### 
    ```

10. ``` {.LignePreCode}
      
    ```

11. ``` {.LignePreCode}
    from tkinter import * 
    ```

12. ``` {.LignePreCode}
    import socket, sys, threading, time 
    ```

13. ``` {.LignePreCode}
    from canon_serveur import Canon, Pupitre, AppServeur 
    ```

14. ``` {.LignePreCode}
      
    ```

15. ``` {.LignePreCode}
    host, port = '192.168.1.168', 36000 
    ```

16. ``` {.LignePreCode}
    largeur, hauteur = 700, 400	   # dimensions de l'espace de jeu 
    ```

17. ``` {.LignePreCode}
      
    ```

18. ``` {.LignePreCode}
    class AppClient(AppServeur): 
    ```

19. ``` {.LignePreCode}
      def __init__(self, host, port, larg_c, haut_c): 
    ```

20. ``` {.LignePreCode}
          AppServeur.__init__(self, host, port, larg_c, haut_c) 
    ```

21. ``` {.LignePreCode}
      
    ```

22. ``` {.LignePreCode}
      def specificites(self): 
    ```

23. ``` {.LignePreCode}
          "préparer les objets spécifiques de la partie client" 
    ```

24. ``` {.LignePreCode}
          self.master.title('<<< Jeu des bombardes >>>') 
    ```

25. ``` {.LignePreCode}
          self.connex =ThreadSocket(self, self.host, self.port) 
    ```

26. ``` {.LignePreCode}
          self.connex.start() 
    ```

27. ``` {.LignePreCode}
          self.id =None 
    ```

28. ``` {.LignePreCode}
      
    ```

29. ``` {.LignePreCode}
      def ajouter_canon(self, id, x, y, sens, coul): 
    ```

30. ``` {.LignePreCode}
          "instancier un canon et un pupitre de nom  dans 2 dictionnaires" 
    ```

31. ``` {.LignePreCode}
          self.guns[id] = Canon(self.jeu, id, int(x), int(y), int(sens), coul) 
    ```

32. ``` {.LignePreCode}
          self.pupi[id] = Pupitre(self, self.guns[id]) 
    ```

33. ``` {.LignePreCode}
          self.pupi[id].inactiver() 
    ```

34. ``` {.LignePreCode}
      
    ```

35. ``` {.LignePreCode}
      def activer_pupitre_personnel(self, id): 
    ```

36. ``` {.LignePreCode}
          self.id =id	       # identifiant reçu du serveur 
    ```

37. ``` {.LignePreCode}
          self.pupi[id].activer() 
    ```

38. ``` {.LignePreCode}
      
    ```

39. ``` {.LignePreCode}
      def tir_canon(self, id): 
    ```

40. ``` {.LignePreCode}
          r = self.guns[id].feu()	       # renvoie False si enrayé 
    ```

41. ``` {.LignePreCode}
          if r and id == self.id: 
    ```

42. ``` {.LignePreCode}
          self.connex.signaler_tir() 
    ```

43. ``` {.LignePreCode}
      
    ```

44. ``` {.LignePreCode}
      def imposer_score(self, id, sc): 
    ```

45. ``` {.LignePreCode}
          self.pupi[id].valeur_score(int(sc)) 
    ```

46. ``` {.LignePreCode}
      
    ```

47. ``` {.LignePreCode}
      def deplacer_canon(self, id, x, y): 
    ```

48. ``` {.LignePreCode}
          "note: les valeurs de x et y sont reçues en tant que chaînes" 
    ```

49. ``` {.LignePreCode}
          self.guns[id].deplacer(int(x), int(y)) 
    ```

50. ``` {.LignePreCode}
      
    ```

51. ``` {.LignePreCode}
      def orienter_canon(self, id, angle): 
    ```

52. ``` {.LignePreCode}
          "régler la hausse du canon  à la valeur " 
    ```

53. ``` {.LignePreCode}
          self.guns[id].orienter(angle) 
    ```

54. ``` {.LignePreCode}
          if id == self.id: 
    ```

55. ``` {.LignePreCode}
          self.connex.signaler_angle(angle) 
    ```

56. ``` {.LignePreCode}
          else: 
    ```

57. ``` {.LignePreCode}
          self.pupi[id].reglage(angle) 
    ```

58. ``` {.LignePreCode}
      
    ```

59. ``` {.LignePreCode}
      def fermer_threads(self, evt): 
    ```

60. ``` {.LignePreCode}
          "couper les connexions existantes et refermer les threads" 
    ```

61. ``` {.LignePreCode}
          self.connex.terminer() 
    ```

62. ``` {.LignePreCode}
          self.active =0		  # empêcher accès ultérieurs à Tk 
    ```

63. ``` {.LignePreCode}
      
    ```

64. ``` {.LignePreCode}
      def depl_aleat_canon(self, id): 
    ```

65. ``` {.LignePreCode}
          pass		    # => méthode inopérante 
    ```

66. ``` {.LignePreCode}
      
    ```

67. ``` {.LignePreCode}
      def goal(self, a, b): 
    ```

68. ``` {.LignePreCode}
          pass		    # => méthode inopérante 
    ```

69. ``` {.LignePreCode}
      
    ```

70. ``` {.LignePreCode}
      
    ```

71. ``` {.LignePreCode}
    class ThreadSocket(threading.Thread): 
    ```

72. ``` {.LignePreCode}
      """objet thread gérant l'échange de messages avec le serveur""" 
    ```

73. ``` {.LignePreCode}
      def __init__(self, boss, host, port): 
    ```

74. ``` {.LignePreCode}
          threading.Thread.__init__(self) 
    ```

75. ``` {.LignePreCode}
          self.app = boss	      # réf. de la fenêtre application 
    ```

76. ``` {.LignePreCode}
          # Mise en place du socket - connexion avec le serveur : 
    ```

77. ``` {.LignePreCode}
          self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    ```

78. ``` {.LignePreCode}
          try: 
    ```

79. ``` {.LignePreCode}
          self.connexion.connect((host, port)) 
    ```

80. ``` {.LignePreCode}
          except socket.error: 
    ```

81. ``` {.LignePreCode}
          print("La connexion a échoué.") 
    ```

82. ``` {.LignePreCode}
          sys.exit() 
    ```

83. ``` {.LignePreCode}
          print("Connexion établie avec le serveur.") 
    ```

84. ``` {.LignePreCode}
      
    ```

85. ``` {.LignePreCode}
      def run(self): 
    ```

86. ``` {.LignePreCode}
          while 1: 
    ```

87. ``` {.LignePreCode}
          msg_recu = self.connexion.recv(1024).decode("Utf8") 
    ```

88. ``` {.LignePreCode}
          print("*%s*" % msg_recu) 
    ```

89. ``` {.LignePreCode}
          # le message reçu est d'abord converti en une liste : 
    ```

90. ``` {.LignePreCode}
          t =msg_recu.split(',') 
    ```

91. ``` {.LignePreCode}
          if t[0] =="" or t[0] =="fin": 
    ```

92. ``` {.LignePreCode}
    	  # fermer le présent thread : 
    ```

93. ``` {.LignePreCode}
    	  break 
    ```

94. ``` {.LignePreCode}
          elif t[0] =="serveur OK": 
    ```

95. ``` {.LignePreCode}
    	  self.connexion.send("client OK".encode("Utf8")) 
    ```

96. ``` {.LignePreCode}
          elif t[0] =="canons": 
    ```

97. ``` {.LignePreCode}
    	  self.connexion.send("OK".encode("Utf8"))   # accusé de réception 
    ```

98. ``` {.LignePreCode}
    	  # éliminons le 1er et le dernier élément de la liste. 
    ```

99. ``` {.LignePreCode}
    	  # ceux qui restent sont eux-mêmes des listes : 
    ```

100. ``` {.LignePreCode}
    	  lc = t[1:-1] 
    ```

101. ``` {.LignePreCode}
    	  # chacune est la description complète d'un canon : 
    ```

102. ``` {.LignePreCode}
    	  for g in lc: 
    ```

103. ``` {.LignePreCode}
    	  s = g.split(';') 
    ```

104. ``` {.LignePreCode}
    	  self.app.ajouter_canon(s[0], s[1], s[2], s[3], s[4]) 
    ```

105. ``` {.LignePreCode}
          elif t[0] =="nouveau_canon": 
    ```

106. ``` {.LignePreCode}
    	  self.app.ajouter_canon(t[1], t[2], t[3], t[4], t[5]) 
    ```

107. ``` {.LignePreCode}
    	  if len(t) >6: 
    ```

108. ``` {.LignePreCode}
    	  self.app.activer_pupitre_personnel(t[1]) 
    ```

109. ``` {.LignePreCode}
          elif t[0] =='angle': 
    ```

110. ``` {.LignePreCode}
    	  # il se peut que l'on ait reçu plusieurs infos regroupées. 
    ```

111. ``` {.LignePreCode}
    	  # on ne considère alors que la première : 
    ```

112. ``` {.LignePreCode}
    	  self.app.orienter_canon(t[1], t[2]) 
    ```

113. ``` {.LignePreCode}
          elif t[0] =="tir_de": 
    ```

114. ``` {.LignePreCode}
    	  self.app.tir_canon(t[1]) 
    ```

115. ``` {.LignePreCode}
          elif t[0] =="scores": 
    ```

116. ``` {.LignePreCode}
    	  # éliminons le 1er et le dernier élément de la liste. 
    ```

117. ``` {.LignePreCode}
    	  # ceux qui restent sont eux-mêmes des listes : 
    ```

118. ``` {.LignePreCode}
    	  lc = t[1:-1] 
    ```

119. ``` {.LignePreCode}
    	  # chaque élément est la description d'un score : 
    ```

120. ``` {.LignePreCode}
    	  for g in lc: 
    ```

121. ``` {.LignePreCode}
    	  s = g.split(';') 
    ```

122. ``` {.LignePreCode}
    	  self.app.imposer_score(s[0], s[1]) 
    ```

123. ``` {.LignePreCode}
          elif t[0] =="mouvement_de": 
    ```

124. ``` {.LignePreCode}
    	  self.app.deplacer_canon(t[1],t[2],t[3]) 
    ```

125. ``` {.LignePreCode}
          elif t[0] =="départ_de": 
    ```

126. ``` {.LignePreCode}
    	  self.app.enlever_canon(t[1]) 
    ```

127. ``` {.LignePreCode}
      
    ```

128. ``` {.LignePreCode}
          # Le thread <réception> se termine ici. 
    ```

129. ``` {.LignePreCode}
          print("Client arrêté. Connexion interrompue.") 
    ```

130. ``` {.LignePreCode}
          self.connexion.close() 
    ```

131. ``` {.LignePreCode}
      
    ```

132. ``` {.LignePreCode}
      def signaler_tir(self): 
    ```

133. ``` {.LignePreCode}
          self.connexion.send("feu".encode("Utf8")) 
    ```

134. ``` {.LignePreCode}
      
    ```

135. ``` {.LignePreCode}
      def signaler_angle(self, angle): 
    ```

136. ``` {.LignePreCode}
          msg ="orienter,{}".format(angle) 
    ```

137. ``` {.LignePreCode}
          self.connexion.send(msg.encode("Utf8")) 
    ```

138. ``` {.LignePreCode}
      
    ```

139. ``` {.LignePreCode}
      def terminer(self): 
    ```

140. ``` {.LignePreCode}
          self.connexion.send("fin".encode("Utf8")) 
    ```

141. ``` {.LignePreCode}
      
    ```

142. ``` {.LignePreCode}
    # Programme principal : 
    ```

143. ``` {.LignePreCode}
    if __name__ =='__main__': 
    ```

144. ``` {.LignePreCode}
      AppClient(host, port, largeur, hauteur).mainloop() 
    ```



#### 20-C-6-A - Commentaires {#article.xml#Ld0e105904 .TitreSection3}

-   Lignes 15-16 : Vous pouvez vous-même perfectionner ce script en lui
    ajoutant un formulaire qui demandera ces valeurs à l'utilisateur au
    cours du démarrage.
-   Lignes 19 à 27 : Le constructeur de la classe parente se termine en
    invoquant la méthode **specificites()**. On peut donc placer dans
    celle-ci ce qui doit être construit différemment dans le serveur et
    dans les clients. Le serveur instancie notamment un widget **text**
    qui n'est pas repris dans les clients ; l'un et l'autre démarrent
    des objets threads différents pour gérer les connexions.
-   Lignes 39 à 42 : Cette méthode est invoquée chaque fois que
    l'utilisateur enfonce le bouton de tir. Le canon ne peut cependant
    pas effectuer des tirs en rafale. Par conséquent, aucun nouveau tir
    ne peut être accepté tant que l'obus précédent n'a pas terminé sa
    trajectoire. C'est la valeur « vraie » ou « fausse » renvoyée par la
    méthode **feu()** de l'objet canon qui indique si le tir a été
    accepté ou non. On utilise cette valeur pour ne signaler au serveur
    (et donc aux autres clients) que les tirs qui ont effectivement eu
    lieu.
-   Lignes 105 à 108 : Un nouveau canon doit être ajouté dans l'espace
    de jeu de chacun (c'est-à-dire dans le canevas du serveur, et dans
    le canevas de tous les clients connectés), chaque fois qu'un nouveau
    client se connecte. Le serveur envoie donc à ce moment un même
    message à tous les clients pour les informer de la présence de ce
    nouveau partenaire. Mais le message envoyé à celui-ci en particulier
    comporte un champ supplémentaire (lequel contient simplement la
    chaîne « le\_vôtre »), afin que ce partenaire sache que ce message
    concerne son propre canon, et qu'il puisse donc activer le pupitre
    correspondant, tout en mémorisant l'identifiant qui lui a été
    attribué par le serveur (voir également les lignes 35 à 37).

#### 20-C-6-B - Conclusions et perspectives : {#article.xml#Ld0e105925 .TitreSection3}

Cette application vous a été présentée dans un but didactique. Nous y
avons délibérément simplifié un certain nombre de problèmes. Par
exemple, si vous testez vous-même ces logiciels, vous constaterez que
les messages échangés sont souvent rassemblés en « paquets », ce qui
nécessiterait d'affiner les algorithmes mis en place pour les
interpréter.

De même, nous avons à peine esquissé le mécanisme fondamental du jeu :
répartition des joueurs dans les deux camps, destruction des canons
touchés, obstacles divers, etc. Il vous reste bien des pistes à explorer
!

Exercices

.Simplifiez le script correspondant au client de *chat* décrit à la page
, en supprimant l'un des deux objets threads. Arrangez-vous par exemple
pour traiter l'émission de messages au niveau du thread principal.

.Modifiez le jeu des bombardes (version monoposte) du chapitre 15 (voir
pages et suivantes), en ne gardant qu'un seul canon et un seul pupitre
de pointage. Ajoutez-y une cible mobile, dont le mouvement sera géré par
un objet thread indépendant (de manière à bien séparer les portions de
code qui contrôlent l'animation de la cible et celle du boulet).


[^note_108]: Rappel : dans une classe dérivée, vous pouvez définir une nouvelle méthode avec le même nom qu'une méthode de la classe parente, afin de modifier sa fonctionnalité dans la classe dérivée. Cela s'appelle **surcharger** cette méthode (voir aussi page ).

[^note_109]: Nous détaillerons cette question quelques pages plus loin, car elle ouvre quelques perspectives intéressantes. Voir : *optimiser les animations à l'aide des threads*, page .
