## 18-B - Ébauche d'un logiciel client pour PostgreSQL

Pour terminer ce chapitre, nous allons vous proposer dans les pages qui
suivent un exemple de réalisation concrète. Il ne s'agira pas d'un
véritable logiciel (le sujet exigerait qu'on lui consacre un ouvrage
spécifique), mais plutôt d'une ébauche d'analyse, destinée à vous
montrer comment vous pouvez « penser comme un programmeur » lorsque vous
abordez un problème complexe.

Les techniques que nous allons mettre en œuvre ici sont de simples
suggestions, dans lesquelles nous essayerons d'utiliser au mieux les
outils que vous avez découverts au cours de votre apprentissage dans les
chapitres précédents, à savoir : les structures de données de haut
niveau (listes et dictionnaires), et la programmation par objets. Il va
de soi que les options retenues dans cet exercice restent largement
critiquables : vous pouvez bien évidemment traiter les mêmes problèmes
en utilisant des approches différentes.

Notre objectif concret est d'arriver à réaliser rapidement un client
rudimentaire, capable de dialoguer avec un « vrai » serveur de bases de
données Nous voudrions que notre client reste un petit utilitaire très
généraliste : il devra être capable de mettre en place une petite base
de données comportant plusieurs tables, de produire des enregistrements
pour chacune d'elles, et nous permettre de tester le résultat de
requêtes SQL basiques.

Dans les lignes qui suivent, nous supposerons que vous avez déjà accès à
un serveur *PostgreSQL*, sur lequel une base de données « discotheque »
aura été créée pour l'utilisateur « jules », lequel s'identifie à l'aide
du mot de passe « abcde ». Ce serveur peut être situé sur une machine
distante accessible via un réseau, ou localement sur votre ordinateur
personnel.

La configuration complète d'un serveur *PostgreSQL* sort du cadre de cet
ouvrage, mais une installation basique n'est pas bien compliquée sur un
système Linux récent, installé depuis une distribution « classique »
telle que *Debian*, *Ubuntu*, *RedHat*, *SuSE*...

Il vous suffit d'installer le paquetage contenant le serveur (soit par
exemple le paquetage **Postgresql-8.4** dans la version actuelle de
Ubuntu-Linux au moment où nous écrivons ces lignes), puis d'accomplir
les quelques opérations ci-après :

En tant qu'administrateur (*root*) du système Linux, vous éditez le
fichier de configuration **pg\_hba.conf** qui devrait se trouver soit
dans un sous-répertoire de **/etc/postgresql**, soit dans un
sous-répertoire de **/var/lib/postgresql**. Dans ce fichier, toutes les
lignes doivent rester des commentaires (c'est-à-dire commencer par le
caractère \#), à l'exception des suivantes :

**local all postgres
ident**\
**local all all
md5**\
**host all all
0.0.0.0 0.0.0.0 reject**

À l'aide de la commande système **sudo
passwd**, vous choisissez un mot de passe pour l'utilisateur
*postgres.* (Il s'agit d'un utilisateur système créé automatiquement
lors de l'installation du paquetage, et qui sera le grand patron (ou
*postmaster*) de votre serveur PostgreSQL.

Vous redémarrez le service PostgreSQL, à l'aide d'une commande telle que
:

**sudo /etc/init.d/postgresql-8.4
restart**

Il vous faut ensuite ouvrir une session sur le système Linux en tant
qu'utilisateur *postgres*, (au départ, celui-ci est le seul à pouvoir
créer de nouveaux utilisateurs du SGBDR), et lancer la commande
**createuser** :

`createuser jules -d -P `\
**Saisir le mot de passe pour le nouveau
rôle : \*\*\*\*\***\
**Le saisir de nouveau
: \*\*\*\*\***\
**Le nouveau rôle est-il super-utilisateur
? (o/n) n **\
**Le nouveau rôle est-il autorisé à créer
de nouveaux rôles ? (o/n) n**

Ces commandes définissent un nouvel utilisateur « jules » pour le
système *PostgreSQL*, et cet utilisateur devra se connecter grâce au mot
de passe fourni (« abcde », dans notre exercice). Le nom d'utilisateur
est quelconque : il ne doit pas nécessairement correspondre à un
utilisateur déjà répertorié dans le système Linux.

Vous pouvez désormais reprendre votre identité habituelle, et créer une
ou plusieurs bases de données au nom de « jules », à l'aide de la
commande **createdb** :



```python
createdb -U jules	  discotheque 
Mot de passe :	  abcde
```



C'est suffisant. À ce stade, le serveur *PostgreSQL* est prêt à
dialoguer avec le client Python décrit dans les pages qui suivent.

### 18-B-1 - Décrire la base de données dans un dictionnaire d'application {#article.xml#Ld0e76655 .TitreSection2}

Une application dialoguant avec une base de données est presque toujours
une application complexe. Elle comporte donc nécessairement de
nombreuses lignes de code, qu'il s'agit de structurer le mieux possible
en les regroupant dans des classes (ou au moins des fonctions) bien
encapsulées.

En de nombreux endroits du code, souvent fort éloignés les uns des
autres, des blocs d'instructions doivent prendre en compte la structure
de la base de données, c'est-à-dire son découpage en un certain nombre
de tables et de champs, ainsi que les relations qui établissent une
hiérarchie dans les enregistrements.

Or, l'expérience montre que la structure d'une base de données est
rarement définitive. Au cours d'un développement, on réalise souvent
qu'il est nécessaire de lui ajouter ou de lui retirer des champs,
parfois même de remplacer une table mal conçue par deux autres, etc. Il
n'est donc pas prudent de programmer des portions de code trop
spécifiques d'une structure particulière, « en dur ».

Au contraire, il est hautement recommandable *de décrire plutôt la
structure complète de la base de données en un seul endroit du
programme*, et d'utiliser ensuite cette description comme référence pour
la génération semi-automatique des instructions particulières concernant
telle table ou tel champ. On évite ainsi, dans une large mesure, le
cauchemar de devoir traquer et modifier un grand nombre d'instructions
un peu partout dans le code, chaque fois que la structure de la base de
données change un tant soit peu. Au lieu de cela, il suffit de changer
seulement la description de référence, et la plus grosse partie du code
reste correcte sans nécessiter de modification.

> Nous tenons là une idée maîtresse pour réaliser des applications
> robustes : un logiciel destiné au traitement de données devrait
> toujours être construit sur la base d*'*un dictionnaire
> d*'*application.

Ce que nous entendons ici par « dictionnaire d'application » ne doit pas
nécessairement revêtir la forme d'un dictionnaire Python. N'importe
quelle structure de données peut convenir, l'essentiel étant de se
construire *une référence centrale décrivant les données* que l'on se
propose de manipuler, avec peut-être aussi un certain nombre
d'informations concernant leur mise en forme.

Du fait de leur capacité à rassembler en une même entité des données de
n'importe quel type, les listes, tuples et dictionnaires de Python
conviennent parfaitement pour ce travail. Dans l'exemple des pages
suivantes, nous avons utilisé nous-mêmes un dictionnaire, dont les
valeurs sont des listes de tuples, mais vous pourriez tout aussi bien
opter pour une organisation différente des mêmes informations.

Tout cela étant bien établi, il nous reste encore à régler une question
d'importance : où allons-nous installer concrètement ce dictionnaire
d'application ?

Ses informations devront pouvoir être consultées depuis n'importe quel
endroit du programme. Il semble donc obligatoire de l'installer dans une
variable globale, de même d'ailleurs que d'autres données nécessaires au
fonctionnement de l'ensemble de notre logiciel. Or vous savez que
l'utilisation de variables globales n'est pas recommandée : elle
comporte des risques, qui augmentent avec la taille du programme. De
toute façon, les variables dites globales ne sont en fait globales qu'à
l'intérieur d'un même module. Si nous souhaitons organiser notre
logiciel comme un ensemble de modules (ce qui constitue par ailleurs une
excellente pratique), nous n'aurons accès à nos variables globales que
dans un seul d'entre eux.

Pour résoudre ce petit problème, il existe cependant une solution simple
et élégante : *regrouper dans une classe particulière toutes les
variables qui nécessitent un statut global* pour l'ensemble de
l'application. Ainsi encapsulées dans l'espace de noms d'une classe, ces
variables peuvent être utilisées sans problème dans n'importe quel
module : il suffit en effet que celui-ci importe la classe en question.
De plus, l'utilisation de cette technique entraîne une conséquence
intéressante : le caractère « global » des variables définies de cette
manière apparaît très clairement dans leur nom qualifié, puisque ce nom
commence par celui de la classe contenante.

Si vous choisissez, par exemple, un nom explicite tel que **Glob** pour
la classe destinée à accueillir vos variables « globales », vous vous
assurez de devoir faire référence à ces variables partout dans votre
code avec des noms tout aussi explicites tels que **Glob**.**ceci** ,
**Glob**.**cela** , etc[^note_96].

C'est cette technique que vous allez découvrir à présent dans les
premières lignes de notre script. Nous y définissons effectivement une
classe **Glob()**, qui n'est donc rien d'autre qu'un simple conteneur.
Aucun objet ne sera instancié à partir de cette classe, laquelle ne
comporte d'ailleurs aucune méthode. Nos variables « globales » y sont
définies comme de simples variables de classe, et nous pourrons donc y
faire référence dans tout le reste du programme en tant qu'attributs de
**Glob()**. Le nom de la base de données, par exemple, pourra être
retrouvé partout dans la variable **Glob**.**dbName** ; le nom ou
l'adresse IP du serveur dans la variable **Glob**.**host**, etc. :



```python
class Glob(object):
  """Espace de noms pour les variables et fonctions <pseudo-globales>"""
 
  dbName = "discotheque"      # nom de la base de données
  user = "jules"	  # propriétaire ou utilisateur
  passwd = "abcde"	    # mot de passe d'accès
  host = "127.0.0.1"	      # nom ou adresse IP du serveur
  port =5432
 
  # Structure de la base de données.  Dictionnaire des tables & champs :
  dicoT ={"compositeurs":[('id_comp', "k", "clé primaire"),
	      ('nom', 25, "nom"),
	      ('prenom', 25, "prénom"),
	      ('a_naiss', "i", "année de naissance"),
	      ('a_mort', "i", "année de mort")],
      "oeuvres":[('id_oeuv', "k", "clé primaire"),
	     ('id_comp', "i", "clé compositeur"),
	     ('titre', 50, "titre de l'oeuvre"),
	     ('duree', "i", "durée (en minutes)"),
	     ('interpr', 30, "interprète principal")]}
```



Le dictionnaire d'application décrivant la structure de la base de
données est contenu dans la variable **Glob.dicoT**.

Il s'agit d'un dictionnaire Python, dont les clés sont les noms des
tables. Quant aux valeurs, chacune d'elles est une liste contenant la
description de tous les champs de la table, sous la forme d'autant de
tuples.

Chaque tuple décrit donc un champ particulier de la table. Pour ne pas
encombrer notre exercice, nous avons limité cette description à trois
informations seulement : le nom du champ, son type et un bref
commentaire. Dans une véritable application, il serait judicieux
d'ajouter encore d'autres informations ici, concernant par exemple des
valeurs limites éventuelles pour les données de ce champ, le formatage à
leur appliquer lorsqu'il s'agit de les afficher à l'écran ou de les
imprimer, le texte qu'il faut placer en haut de colonne lorsque l'on
veut les présenter dans un tableau, etc.

Il peut vous paraître assez fastidieux de décrire ainsi très en détail
la structure de vos données, alors que vous voudriez probablement
commencer tout de suite une réflexion sur les divers algorithmes à
mettre en œuvre afin de les traiter. Sachez cependant que si elle est
bien faite, une telle description structurée vous fera certainement
gagner beaucoup de temps par la suite, parce qu'elle vous permettra
d'automatiser pas mal de choses. Vous en verrez une démonstration un peu
plus loin. En outre, vous devez vous convaincre que cette tâche un peu
ingrate vous prépare à bien structurer aussi le reste de votre travail :
organisation des formulaires, tests à effectuer, etc.

### 18-B-2 - Définir une classe d'objets-interfaces {#article.xml#Ld0e77293 .TitreSection2}

La classe **Glob()** décrite à la rubrique précédente sera donc
installée en début de script, ou bien dans un module séparé importé en
début de script. Pour la suite de l'exposé, nous supposerons que c'est
cette dernière formule qui est retenue : nous avons sauvegardé la classe
**Glob()** dans un module nommé **dict\_app**.**py**, d'où nous pouvons
à présent l'importer dans le script suivant.

Ce nouveau script définit une classe d'objets-interfaces. Nous voulons
en effet essayer de mettre à profit ce que nous avons appris dans les
chapitres précédents, et donc privilégier la programmation par objets,
afin de créer des portions de code bien encapsulées et largement
réutilisables.

Les objets-interfaces que nous voulons construire seront similaires aux
objets-fichiers que nous avons abondamment utilisés pour la gestion des
fichiers au chapitre 9. Vous vous rappelez par exemple que nous ouvrons
un fichier en créant un objet-fichier, à l'aide de la fonction-fabrique
**open()**. D'une manière similaire, nous ouvrirons la communication
avec la base de données en commençant par créer un objet-interface à
l'aide de la classe **GestionBD()**, ce qui établira la connexion. Pour
lire ou écrire dans un fichier ouvert, nous utilisons diverses méthodes
de l'objet-fichier. D'une manière analogue, nous effectuerons nos
opérations sur la base de données par l'intermédiaire des diverses
méthodes de l'objet-interface.



1.  ``` {.LignePreCode}
    import sys 
    ```

2.  ``` {.LignePreCode}
    from pg8000 import DBAPI 
    ```

3.  ``` {.LignePreCode}
    from dict_app import * 
    ```

4.  ``` {.LignePreCode}
      
    ```

5.  ``` {.LignePreCode}
    class GestionBD(object): 
    ```

6.  ``` {.LignePreCode}
      """Mise en place et interfaçage d'une base de données PostgreSQL""" 
    ```

7.  ``` {.LignePreCode}
      def __init__(self, dbName, user, passwd, host, port =5432): 
    ```

8.  ``` {.LignePreCode}
          "Établissement de la connexion - Création du curseur" 
    ```

9.  ``` {.LignePreCode}
          try: 
    ```

10. ``` {.LignePreCode}
          self.baseDonn = DBAPI.connect(host =host, port =port, 
    ```

11. ``` {.LignePreCode}
    		     database =dbName, 
    ```

12. ``` {.LignePreCode}
    		     user=user, password=passwd) 
    ```

13. ``` {.LignePreCode}
          except Exception as err: 
    ```

14. ``` {.LignePreCode}
          print('La connexion avec la base de données a échoué :\n'\ 
    ```

15. ``` {.LignePreCode}
    	 'Erreur détectée :\n%s' % err) 
    ```

16. ``` {.LignePreCode}
          self.echec =1 
    ```

17. ``` {.LignePreCode}
          else: 
    ```

18. ``` {.LignePreCode}
          self.cursor = self.baseDonn.cursor()   # création du curseur 
    ```

19. ``` {.LignePreCode}
          self.echec =0 
    ```

20. ``` {.LignePreCode}
      
    ```

21. ``` {.LignePreCode}
      def creerTables(self, dicTables): 
    ```

22. ``` {.LignePreCode}
          "Création des tables décrites dans le dictionnaire <dicTables>." 
    ```

23. ``` {.LignePreCode}
          for table in dicTables:	      # parcours des clés du dictionnaire 
    ```

24. ``` {.LignePreCode}
          req = "CREATE TABLE %s (" % table 
    ```

25. ``` {.LignePreCode}
          pk ='' 
    ```

26. ``` {.LignePreCode}
          for descr in dicTables[table]: 
    ```

27. ``` {.LignePreCode}
    	  nomChamp = descr[0]	  # libellé du champ à créer 
    ```

28. ``` {.LignePreCode}
    	  tch = descr[1]	 # type de champ à créer 
    ```

29. ``` {.LignePreCode}
    	  if tch =='i': 
    ```

30. ``` {.LignePreCode}
    	  typeChamp ='INTEGER' 
    ```

31. ``` {.LignePreCode}
    	  elif tch =='k': 
    ```

32. ``` {.LignePreCode}
    	  # champ 'clé primaire' (entier incrémenté automatiquement) 
    ```

33. ``` {.LignePreCode}
    	  typeChamp ='SERIAL' 
    ```

34. ``` {.LignePreCode}
    	  pk = nomChamp 
    ```

35. ``` {.LignePreCode}
    	  else: 
    ```

36. ``` {.LignePreCode}
    	  typeChamp ='VARCHAR(%s)' % tch 
    ```

37. ``` {.LignePreCode}
    	  req = req + "%s %s, " % (nomChamp, typeChamp) 
    ```

38. ``` {.LignePreCode}
          if pk == '': 
    ```

39. ``` {.LignePreCode}
    	  req = req[:-2] + ")" 
    ```

40. ``` {.LignePreCode}
          else: 
    ```

41. ``` {.LignePreCode}
    	  req = req + "CONSTRAINT %s_pk PRIMARY KEY(%s))" % (pk, pk) 
    ```

42. ``` {.LignePreCode}
          self.executerReq(req) 
    ```

43. ``` {.LignePreCode}
      
    ```

44. ``` {.LignePreCode}
      def supprimerTables(self, dicTables): 
    ```

45. ``` {.LignePreCode}
          "Suppression de toutes les tables décrites dans <dicTables>" 
    ```

46. ``` {.LignePreCode}
          for table in list(dicTables.keys()): 
    ```

47. ``` {.LignePreCode}
          req ="DROP TABLE %s" % table 
    ```

48. ``` {.LignePreCode}
          self.executerReq(req) 
    ```

49. ``` {.LignePreCode}
          self.commit()		 # transfert -> disque 
    ```

50. ``` {.LignePreCode}
      
    ```

51. ``` {.LignePreCode}
      def executerReq(self, req, param =None): 
    ```

52. ``` {.LignePreCode}
          "Exécution de la requête , avec détection d'erreur éventuelle" 
    ```

53. ``` {.LignePreCode}
          try: 
    ```

54. ``` {.LignePreCode}
          self.cursor.execute(req, param) 
    ```

55. ``` {.LignePreCode}
          except Exception as err: 
    ```

56. ``` {.LignePreCode}
          # afficher la requête et le message d'erreur système : 
    ```

57. ``` {.LignePreCode}
          print("Requête SQL incorrecte :\n{}\nErreur détectée :".format(req)) 
    ```

58. ``` {.LignePreCode}
          print(err) 
    ```

59. ``` {.LignePreCode}
          return 0 
    ```

60. ``` {.LignePreCode}
          else: 
    ```

61. ``` {.LignePreCode}
          return 1 
    ```

62. ``` {.LignePreCode}
      
    ```

63. ``` {.LignePreCode}
      def resultatReq(self): 
    ```

64. ``` {.LignePreCode}
          "renvoie le résultat de la requête précédente (une liste de tuples)" 
    ```

65. ``` {.LignePreCode}
          return self.cursor.fetchall() 
    ```

66. ``` {.LignePreCode}
      
    ```

67. ``` {.LignePreCode}
      def commit(self): 
    ```

68. ``` {.LignePreCode}
          if self.baseDonn: 
    ```

69. ``` {.LignePreCode}
          self.baseDonn.commit()	 # transfert curseur -> disque 
    ```

70. ``` {.LignePreCode}
      
    ```

71. ``` {.LignePreCode}
      def close(self): 
    ```

72. ``` {.LignePreCode}
          if self.baseDonn: 
    ```

73. ``` {.LignePreCode}
          self.baseDonn.close() 
    ```



#### 18-B-2-A - Commentaires {#article.xml#Ld0e78565 .TitreSection3}

-   Lignes 1-3 : Outre notre propre module **dict\_app** qui contient
    les variables « globales », nous importons le module **sys** qui
    englobe quelques fonctions système, et surtout le module **pg8000**
    qui rassemble tout ce qui est nécessaire pour communiquer avec
    *PostgreSQL*. Ce module ne fait pas partie de la distribution
    standard de Python. Il s'agit d'un des modules d'interface
    Python-PostgreSQL déjà disponibles pour Python 3. Plusieurs autres
    bibliothèques plus performantes, disponibles depuis longtemps pour
    les versions précédentes de Python, seront très certainement adaptés
    sous peu (l'excellent pilote **psycopg2** devrait être bientôt
    prêt). Pour l'installation de pg8000, voyez page .
-   Ligne 7 : Lors de la création des objets-interfaces, nous devrons
    fournir les paramètres de la connexion : nom de la base de données,
    nom de son utilisateur, nom ou adresse IP de la machine où est situé
    le serveur. Le numéro du port de communication est habituellement
    celui que nous avons prévu par défaut. Toutes ces informations sont
    supposées être en votre possession.
-   Lignes 9 à 19 : Il est hautement recommandable de placer le code
    servant à établir la connexion à l'intérieur d'un gestionnaire
    d'exceptions **try**-**except**-**else** (voir page ), car nous ne
    pouvons pas présumer que le serveur sera nécessairement accessible.
    Remarquons au passage que la méthode **\_\_init\_\_()** ne peut pas
    renvoyer de valeur (à l'aide de l'instruction **return**), du fait
    qu'elle est invoquée automatiquement par Python lors de
    l'instanciation d'un objet. En effet : ce qui est renvoyé dans ce
    cas au programme appelant est l'objet nouvellement construit. Nous
    ne pouvons donc pas signaler la réussite ou l'échec de la connexion
    au programme appelant à l'aide d'une valeur de retour. Une solution
    simple à ce petit problème consiste à mémoriser le résultat de la
    tentative de connexion dans un attribut d'instance (variable
    **self.echec**), que le programme appelant peut ensuite tester quand
    bon lui semble.
-   Lignes 21 à 42 : Cette méthode automatise la création de toutes les
    tables de la base de données, en tirant profit de la description du
    dictionnaire d'application, lequel doit lui être transmis en
    argument. Une telle automatisation sera évidemment d'autant plus
    appréciable, que la structure de la base de données sera plus
    complexe (imaginez par exemple une base de données contenant 35
    tables !). Afin de ne pas alourdir la démonstration, nous avons
    restreint les capacités de cette méthode à la création de champs des
    types *integer* et *varchar*. Libre à vous d'ajouter les
    instructions nécessaires pour créer des champs d'autres types.\
    \
     Si vous détaillez le code, vous constaterez qu'il consiste
    simplement à construire une requête SQL pour chaque table, morceau
    par morceau, dans la chaîne de caractères **req**. Celle-ci est
    ensuite transmise à la méthode **executerReq()** pour exécution. Si
    vous souhaitez visualiser la requête ainsi construite, vous pouvez
    évidemment ajouter une instruction `print(req)` juste après la ligne 42.\
    \
     Vous pouvez également ajouter à cette méthode la capacité de mettre
    en place les *contraintes d'intégrité référentielle*, sur la base
    d'un complément au dictionnaire d'application qui décrirait ces
    contraintes. Nous ne développons pas cette question ici, mais cela
    ne devrait pas vous poser de problème si vous savez de quoi il
    retourne.
-   Lignes 44 à 49 : Beaucoup plus simple que la précédente, cette
    méthode utilise le même principe pour supprimer toutes les tables
    décrites dans le dictionnaire d'application.
-   Lignes 51 à 61 : Cette méthode transmet simplement la requête à
    l'objet curseur. Son utilité est de simplifier l'accès à celui-ci et
    de produire un message d'erreur si nécessaire.
-   Lignes 63 à 73 : Ces méthodes ne sont que de simples relais vers les
    objets produits par le module **pg8000** : l'objet-connecteur
    produit par la fonction-fabrique **DBAPI.connect()**, et l'objet
    curseur correspondant. Elles permettent de simplifier légèrement le
    code du programme appelant.

### 18-B-3 - Construire un générateur de formulaires {#article.xml#Ld0e78647 .TitreSection2}

Nous avons ajouté cette classe à notre exercice pour vous expliquer
comment vous pouvez utiliser le même dictionnaire d'application afin
d'élaborer du code généraliste. L'idée développée ici est de réaliser
une classe d'objets-formulaires capables de prendre en charge l'encodage
des enregistrements de n'importe quelle table, en construisant
automatiquement les instructions d'entrée adéquates grâce aux
informations tirées du dictionnaire d'application.

Dans une application véritable, ce formulaire trop simpliste devrait
certainement être fortement remanié, et il prendrait vraisemblablement
la forme d'une fenêtre spécialisée, dans laquelle les champs d'entrée et
leurs libellés pourraient encore une fois être générés de manière
automatique. Nous ne prétendons donc pas qu'il constitue un bon exemple,
mais nous voulons simplement vous montrer comment vous pouvez
automatiser sa construction dans une large mesure. Tâchez de réaliser
vos propres formulaires en vous servant de principes semblables.



1.  ``` {.LignePreCode}
    class Enregistreur(object): 
    ```

2.  ``` {.LignePreCode}
      """classe pour gérer l'entrée d'enregistrements divers""" 
    ```

3.  ``` {.LignePreCode}
      def __init__(self, bd, table): 
    ```

4.  ``` {.LignePreCode}
          self.bd =bd 
    ```

5.  ``` {.LignePreCode}
          self.table =table 
    ```

6.  ``` {.LignePreCode}
          self.descriptif =Glob.dicoT[table]   # descriptif des champs 
    ```

7.  ``` {.LignePreCode}
      
    ```

8.  ``` {.LignePreCode}
      def entrer(self): 
    ```

9.  ``` {.LignePreCode}
          "procédure d'entrée d'un enregistrement entier" 
    ```

10. ``` {.LignePreCode}
          champs ="("	 # ébauche de chaîne pour les noms de champs 
    ```

11. ``` {.LignePreCode}
          valeurs =[]	 # liste pour les valeurs correspondantes 
    ```

12. ``` {.LignePreCode}
          # Demander successivement une valeur pour chaque champ : 
    ```

13. ``` {.LignePreCode}
          for cha, type, nom in self.descriptif: 
    ```

14. ``` {.LignePreCode}
          if type =="k":	# on ne demandera pas le n° d'enregistrement 
    ```

15. ``` {.LignePreCode}
    	  continue	# à l'utilisateur (numérotation auto.) 
    ```

16. ``` {.LignePreCode}
          champs = champs + cha + "," 
    ```

17. ``` {.LignePreCode}
          val = input("Entrez le champ %s :" % nom) 
    ```

18. ``` {.LignePreCode}
          if type =="i": 
    ```

19. ``` {.LignePreCode}
    	  val =int(val) 
    ```

20. ``` {.LignePreCode}
          valeurs.append(val) 
    ```

21. ``` {.LignePreCode}
      
    ```

22. ``` {.LignePreCode}
          balises ="(" + "%s," * len(valeurs)     # balises de conversion 
    ```

23. ``` {.LignePreCode}
          champs = champs[:-1] + ")"    # supprimer la dernière virgule, 
    ```

24. ``` {.LignePreCode}
          balises = balises[:-1] + ")"  # et ajouter une parenthèse 
    ```

25. ``` {.LignePreCode}
          req ="INSERT INTO %s %s VALUES %s" % (self.table, champs, balises) 
    ```

26. ``` {.LignePreCode}
          self.bd.executerReq(req, valeurs) 
    ```

27. ``` {.LignePreCode}
      
    ```

28. ``` {.LignePreCode}
          ch =input("Continuer (O/N) ? ") 
    ```

29. ``` {.LignePreCode}
          if ch.upper() == "O": 
    ```

30. ``` {.LignePreCode}
          return 0 
    ```

31. ``` {.LignePreCode}
          else: 
    ```

32. ``` {.LignePreCode}
          return 1 
    ```



#### 18-B-3-A - Commentaires {#article.xml#Ld0e79337 .TitreSection3}

-   Lignes 1 à 6 : Au moment de leur instanciation, les objets de cette
    classe reçoivent la référence de l'une des tables du dictionnaire.
    C'est ce qui leur donne accès au descriptif des champs.
-   Ligne 8 : Cette méthode **entrer()** génère le formulaire proprement
    dit. Elle prend en charge l'entrée des enregistrements dans la
    table, en s'adaptant à leur structure propre grâce au descriptif
    trouvé dans le dictionnaire. Sa fonctionnalité concrète consiste
    encore une fois à construire morceau par morceau une chaîne de
    caractères qui deviendra une requête SQL, comme dans la méthode
    **creerTables()** de la classe **GestionBD()** décrite à la rubrique
    précédente.\
     Vous pourriez bien entendu ajouter à la présente classe encore
    d'autres méthodes, pour gérer par exemple la suppression et/ou la
    modification d'enregistrements.
-   Lignes 12 à 20 : L'attribut d'instance **self**.**descriptif**
    contient une liste de tuples, et chacun de ceux-ci est fait de trois
    éléments, à savoir le nom d'un champ, le type de données qu'il est
    censé recevoir, et sa description « en clair ». La boucle **for** de
    la ligne 13 parcourt cette liste et affiche pour chaque champ un
    message d'invite construit sur la base de la description qui
    accompagne ce champ. Lorsque l'utilisateur a entré la valeur
    demandée, celle-ci et mémorisée dans une liste en construction,
    tandis que le nom du champ s'ajoute à une chaîne en cours de
    formatage.
-   Lignes 22 à 26 : Lorsque tous les champs ont été parcourus, la
    requête proprement dite est assemblée et exécutée. Comme nous
    l'avons expliqué page , les valeurs ne doivent pas être intégrés
    dans la chaîne de requête elle-même, mais plutôt transmises comme
    arguments à la méthode **execute()**.

### 18-B-4 - Le corps de l'application {#article.xml#Ld0e79372 .TitreSection2}

Il ne nous paraît pas utile de développer davantage encore cet exercice
dans le cadre d'un manuel d'initiation. Si le sujet vous intéresse, vous
devriez maintenant en savoir assez pour commencer déjà quelques
expériences personnelles. Veuillez alors consulter les bons ouvrages de
référence, comme par exemple *Python : How to program* de Deitel &
coll., ou encore les sites web consacrés aux extensions de Python.

Le script qui suit est celui d'une petite application destinée à tester
les classes décrites dans les pages qui précèdent. Libre à vous de la
perfectionner, ou alors d'en écrire une autre tout à fait différente !



1.  ``` {.LignePreCode}
    ###### Programme principal : ######### 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    # Création de l'objet-interface avec la base de données : 
    ```

4.  ``` {.LignePreCode}
    bd = GestionBD(Glob.dbName, Glob.user, Glob.passwd, Glob.host, Glob.port) 
    ```

5.  ``` {.LignePreCode}
    if bd.echec: 
    ```

6.  ``` {.LignePreCode}
      sys.exit() 
    ```

7.  ``` {.LignePreCode}
      
    ```

8.  ``` {.LignePreCode}
    while 1: 
    ```

9.  ``` {.LignePreCode}
      print("\nQue voulez-vous faire :\n"\ 
    ```

10. ``` {.LignePreCode}
         "1) Créer les tables de la base de données\n"\ 
    ```

11. ``` {.LignePreCode}
         "2) Supprimer les tables de la base de données ?\n"\ 
    ```

12. ``` {.LignePreCode}
         "3) Entrer des compositeurs\n"\ 
    ```

13. ``` {.LignePreCode}
         "4) Entrer des oeuvres\n"\ 
    ```

14. ``` {.LignePreCode}
         "5) Lister les compositeurs\n"\ 
    ```

15. ``` {.LignePreCode}
         "6) Lister les oeuvres\n"\ 
    ```

16. ``` {.LignePreCode}
         "7) Exécuter une requête SQL quelconque\n"\ 
    ```

17. ``` {.LignePreCode}
         "9) terminer ?		Votre choix :", end=' ') 
    ```

18. ``` {.LignePreCode}
      ch = int(input()) 
    ```

19. ``` {.LignePreCode}
      if ch ==1: 
    ```

20. ``` {.LignePreCode}
          # création de toutes les tables décrites dans le dictionnaire : 
    ```

21. ``` {.LignePreCode}
          bd.creerTables(Glob.dicoT) 
    ```

22. ``` {.LignePreCode}
      elif ch ==2: 
    ```

23. ``` {.LignePreCode}
          # suppression de toutes les tables décrites dans le dic. : 
    ```

24. ``` {.LignePreCode}
          bd.supprimerTables(Glob.dicoT) 
    ```

25. ``` {.LignePreCode}
      elif ch ==3 or ch ==4: 
    ```

26. ``` {.LignePreCode}
          # création d'un  de compositeurs ou d'oeuvres : 
    ```

27. ``` {.LignePreCode}
          table ={3:'compositeurs', 4:'oeuvres'}[ch] 
    ```

28. ``` {.LignePreCode}
          enreg =Enregistreur(bd, table) 
    ```

29. ``` {.LignePreCode}
          while 1: 
    ```

30. ``` {.LignePreCode}
          if enreg.entrer(): 
    ```

31. ``` {.LignePreCode}
    	  break 
    ```

32. ``` {.LignePreCode}
      elif ch ==5 or ch ==6: 
    ```

33. ``` {.LignePreCode}
          # listage de tous les compositeurs, ou toutes les oeuvres : 
    ```

34. ``` {.LignePreCode}
          table ={5:'compositeurs', 6:'oeuvres'}[ch] 
    ```

35. ``` {.LignePreCode}
          if bd.executerReq("SELECT * FROM %s" % table): 
    ```

36. ``` {.LignePreCode}
          # analyser le résultat de la requête ci-dessus : 
    ```

37. ``` {.LignePreCode}
          records = bd.resultatReq()      # ce sera un tuple de tuples 
    ```

38. ``` {.LignePreCode}
          for rec in records:	   # => chaque enregistrement 
    ```

39. ``` {.LignePreCode}
    	  for item in rec:	 # => chaque champ dans l'enreg. 
    ```

40. ``` {.LignePreCode}
    	  print(item, end=' ') 
    ```

41. ``` {.LignePreCode}
    	  print() 
    ```

42. ``` {.LignePreCode}
      elif ch ==7: 
    ```

43. ``` {.LignePreCode}
          req =input("Entrez la requête SQL : ") 
    ```

44. ``` {.LignePreCode}
          if bd.executerReq(req): 
    ```

45. ``` {.LignePreCode}
          print(bd.resultatReq())	    # ce sera un tuple de tuples 
    ```

46. ``` {.LignePreCode}
      else: 
    ```

47. ``` {.LignePreCode}
          bd.commit() 
    ```

48. ``` {.LignePreCode}
          bd.close() 
    ```

49. ``` {.LignePreCode}
          break 
    ```



#### 18-B-4-A - Commentaires {#article.xml#Ld0e80464 .TitreSection3}

-   On supposera bien évidemment que les classes décrites plus haut
    soient présentes dans le même script, ou qu'elles aient été
    importées.
-   Lignes 3 à 6 : L'objet-interface est créé ici. Si la création
    échoue, l'attribut d'instance **bd.echec** contient la valeur 1. Le
    test des lignes 5 et 6 permet alors d'arrêter l'application
    immédiatement (la fonction **exit()** du module **sys** sert
    spécifiquement à cela).
-   Ligne 8 : Le reste de l'application consiste à proposer sans cesse
    le même menu, jusqu'à ce que l'utilisateur choisisse l'option n^o^
    9.
-   Lignes 27-28 : La classe **Enregistreur()** accepte de gérer les
    enregistrements de n'importe quelle table. Afin de déterminer
    laquelle doit être utilisée lors de l'instanciation, on utilise un
    petit dictionnaire qui indique quel nom retenir, en fonction du
    choix opéré par l'utilisateur (option n^o^ 3 ou n^o^ 4).
-   Lignes 29 à 31 : La méthode **entrer()** de l'objet-enregistreur
    renvoie une valeur 0 ou 1 suivant que l'utilisateur a choisi de
    continuer à entrer des enregistrements, ou bien d'arrêter. Le test
    de cette valeur permet d'interrompre la boucle de répétition en
    conséquence.
-   Lignes 35-44 : La méthode **executerReq()** renvoie une valeur 0 ou
    1 suivant que la requête a été acceptée ou non par le serveur. On
    peut donc tester cette valeur pour décider si le résultat doit être
    affiché ou non.

Exercices

.Modifiez le script décrit dans ces pages de manière à ajouter une table
supplémentaire à la base de données. Ce pourrait être par exemple une
table « orchestres », dont chaque enregistrement contiendrait le nom de
l'orchestre, le nom de son chef, et le nombre total d'instruments.

.Ajoutez d'autres types de champ à l'une des tables (par exemple un
champ de type *float* (réel) ou de type *date*), et modifiez le script
en conséquence.


[^note_96]: Vous pourriez également placer vos variables « globales » dans un module nommé **Glob.py**, puis importer celui-ci. Utiliser un module ou une classe comme espace de noms pour stocker des variables sont donc des techniques assez similaires. L'utilisation d'une classe est peut-être un peu plus souple et plus lisible, puisque la classe peut accompagner le reste du script, alors qu'un module est nécessairement un fichier distinct.
