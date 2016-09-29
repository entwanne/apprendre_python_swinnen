## 18-A - Les bases de données

Il existe de nombreux types de bases de données. On peut par exemple
déjà considérer comme une base de données élémentaire un fichier qui
contient une liste de noms et d'adresses.

Si la liste n'est pas trop longue, et si l'on ne souhaite pas pouvoir y
effectuer des recherches en fonction de critères complexes, il va de soi
que l'on peut accéder à ce type de données en utilisant des instructions
simples, telles celles que nous avons abordées .

La situation se complique cependant très vite si l'on souhaite pouvoir
effectuer des sélections et des tris parmi les données, surtout si
celles-ci deviennent très nombreuses. La difficulté augmente encore si
les données sont répertoriées dans différents ensembles reliés par un
certain nombre de relations hiérarchiques, et si plusieurs utilisateurs
doivent pouvoir y accéder en parallèle.

Imaginez par exemple que la direction de votre école vous confie la
charge de mettre au point un système de bulletins informatisé. En y
réfléchissant quelque peu, vous vous rendrez compte rapidement que cela
suppose la mise en œuvre de toute une série de tables différentes : une
table des noms d'élèves (laquelle pourra bien entendu contenir aussi
d'autres informations spécifiques à ces élèves : adresse, date de
naissance, etc.) ; une table contenant la liste des cours (avec le nom
du professeur titulaire, le nombre d'heures enseignées par semaine,
etc.) ; une table mémorisant les travaux pris en compte pour
l'évaluation (avec leur importance, leur date, leur contenu, etc.) ; une
table décrivant la manière dont les élèves sont groupés par classes ou
par options, les cours suivis par chacun, etc.

Vous comprenez bien que ces différentes tables ne sont pas
indépendantes. Les travaux effectués par un même élève sont liés à des
cours différents. Pour établir le bulletin de cet élève, il faut donc
extraire des données de la table des travaux, bien sûr, mais en relation
avec des informations trouvées dans d'autres tables (celles des cours,
des classes, des options, etc.).

Nous verrons plus loin comment représenter des tables de données et les
relations qui les lient.

### 18-A-1 - SGBDR - Le modèle client/serveur {#article.xml#Ld0e74370 .TitreSection2}

Les programmes informatiques capables de gérer efficacement de tels
ensembles de données complexes sont forcément complexes, eux aussi. On
appelle ces programmes des *SGBDR* (Systèmes de gestion de bases de
données relationnelles). Il s'agit d'applications informatiques de
première importance pour les entreprises. Certaines sont les fleurons de
sociétés spécialisées (*IBM*, *Oracle*, *Microsoft*, *Informix*,
*Sybase.*..) et sont en général vendues à des prix fort élevés. D'autres
ont été développées dans des centres de recherche et d'enseignement
universitaires (*PostgreSQL, SQLite, MySQL* ...) ; elles sont alors en
général tout à fait gratuites.

Ces systèmes ont chacun leurs spécificités et leurs performances, mais
la plupart fonctionnant sur *le modèle client/serveur* : cela signifie
que la plus grosse partie de l'application (ainsi que la base de données
prise en charge) est installée en un seul endroit, en principe sur une
machine puissante (cet ensemble constituant donc le *serveur*), alors
que l'autre partie, beaucoup plus simple, est installée sur un nombre
indéterminé de postes de travail, appelés des *clients*.

Les clients sont reliés au serveur, en permanence ou non, par divers
procédés et protocoles (éventuellement par l'intermédiaire de
l'internet). Chacun d'entre eux peut accéder à une partie plus ou moins
importante des données, avec autorisation ou non de modifier certaines
d'entre elles, d'en ajouter ou d'en supprimer, en fonction de règles
d'accès bien déterminées, définies par un administrateur de la base de
données.

Le serveur et ses clients sont en fait des applications distinctes qui
s'échangent des informations. Imaginez par exemple que vous êtes l'un
des utilisateurs du système.

Pour accéder aux données, vous devez lancer l'exécution d'une
application cliente sur un poste de travail quelconque. Dans son
processus de démarrage, l'application cliente commence par établir la
connexion avec le serveur et la base de données[^note_88].
Lorsque la connexion est établie, l'application cliente peut interroger
le serveur en lui envoyant une *requête* sous une forme convenue. Il
s'agit par exemple de retrouver une information précise. Le serveur
exécute alors la requête en recherchant les données correspondantes dans
la base, puis il expédie en retour une certaine *réponse* au client.

Cette réponse peut être l'information demandée, ou encore un message
d'erreur en cas d'insuccès.

La communication entre le client et le serveur est donc faite de
*requêtes* et de *réponses*. Les requêtes sont de véritables
instructions expédiées du client au serveur, non seulement pour extraire
des données de la base, mais aussi pour en ajouter, en supprimer, en
modifier, etc.

### 18-A-2 - Le langage SQL {#article.xml#Ld0e74432 .TitreSection2}

À la lecture de ce qui précède, vous aurez bien compris qu'il ne peut
être question de vous expliquer dans ces pages comment vous pourriez
réaliser vous-même un logiciel serveur. C'est vraiment là une affaire de
spécialistes (au même titre que le développement d'un nouveau langage de
programmation, par exemple). L'élaboration d'un logiciel client, par
contre, est tout à fait à votre portée et peut vous apporter un immense
bénéfice. Il faut savoir en effet que la plupart des applications «
sérieuses » de l'informatique s'articulent autour d'une base de données
plus ou moins complexe : même les logiciels de jeu doivent mémoriser une
foule de données, et maintenir entre elles des relations.

En fonction des besoins de votre application, vous devrez donc choisir,
soit de vous connecter à un gros serveur distant géré par d'autres
personnes, soit de mettre en place un serveur local plus ou moins
performant. Dans le cas particulier d'une application monoposte, vous
pourrez utiliser un logiciel serveur installé sur la même machine que
votre application, ou plus simplement encore exploiter une
bibliothèque-serveur compatible avec votre langage de programmation.
Vous verrez cependant que dans tous les cas de figure, les mécanismes à
mettre en œuvre restent fondamentalement les mêmes.

On aurait pu craindre, en effet, qu'étant donnée la grande diversité des
systèmes serveurs existants, il soit nécessaire de faire usage de
protocoles et de langages différents pour adresser des requêtes à chacun
d'eux. Mais fort heureusement, de grands efforts de standardisation ont
été accomplis pour la mise au point d'un langage de requêtes commun, qui
porte le nom de **SQL** (*Structured Query Language*, ou langage de
requêtes structuré)[^note_89].
En ce qui concerne Python, un effort supplémentaire a été accompli pour
standardiser les procédures d'accès aux serveurs eux-mêmes, sous la
forme d'une interface commune (*DBAPI*[^note_90]).

Vous allez donc devoir apprendre quelques rudiments de ce langage pour
pouvoir continuer, mais cela ne doit pas vous effrayer. Vous aurez
d'ailleurs certainement l'occasion de rencontrer SQL dans d'autres
domaines (bureautique, par exemple). Dans le cadre restreint de ce
cours, il vous suffira de connaître quelques instructions SQL très
simples pour comprendre les mécanismes de base et peut-être déjà
réaliser quelques projets intéressants.

### 18-A-3 - SQLite {#article.xml#Ld0e74460 .TitreSection2}



![](images/10000201000001440000005F4970656E.png)



Cela signifie donc que vous pouvez écrire en Python une application
contenant son propre SGBDR intégré, sans qu'il soit nécessaire
d'installer quoi que ce soit d'autre, et que les performances seront au
rendez-vous.

Nous verrons en fin de chapitre comment les choses se présentent si
votre application doit utiliser plutôt un serveur de bases de données
hébergé par une autre machine, mais les principes resteront les mêmes.
Tout ce que vous aurez appris à faire avec **SQLite** sera transposable
sans modification si vous devez plus tard travailler avec un SGDBR plus
« imposant » tel que *PostgreSQL*, *MySQL* ou *Oracle*.

Commençons donc tout de suite à explorer les bases de ce système, à la
ligne de commande. Nous écrirons ensuite un petit script pour gérer une
base de données simple à deux tables.

### 18-A-4 - Création de la base de données. Objets « connexion » et « curseur ». {#article.xml#Ld0e74482 .TitreSection2}

Comme vous vous y attendez certainement, il suffit d'importer un module
pour accéder aux fonctionnalités attendues :

`>>> import sqlite3`

(Le chiffre à la fin du nom est le numéro de la version actuelle du
module d'interface au moment où nous écrivons ces lignes. Il est
possible que ce soit modifié dans des versions futures de Python).

Il faut ensuite décider le nom de fichier que vous voulez attribuer à la
base de données. **SQLite** mémorise toutes les tables d'une base de
données dans un seul fichier multi-plateformes que vous pouvez
sauvegarder où vous voulez (cela devrait grandement vous faciliter la
vie pour les archivages !) :



```python
>>> fichierDonnees ="E:/python3/essais/bd_test.sq3" 
```



Le nom de fichier peut comporter un chemin et une extension quelconques.
Il est également possible d'utiliser le nom spécial « `:memory:` », ce qui indiquera au système
de traiter la base de données en mémoire vive seulement. Ainsi les temps
d'accès aux données seront raccourcis, et l'application pourra être
ultra-rapide, ce qui peut vous intéresser dans le contexte d'un logiciel
de jeu, par exemple, à la condition de prévoir un mécanisme distinct
pour les sauvegardes sur disque.

Vous créez alors un ***objet-connexion***, à l'aide de la
fonction-fabrique **connect()**. Cet objet assurera l'interface entre
votre programme et la base de données. L'opération est tout à fait
comparable à l'ouverture d'un simple fichier texte, l'instanciation de
l'objet créant le fichier de mémorisation au passage (s'il n'existe pas
déjà) :



```python
>>> conn =sqlite3.connect(fichierDonnees) 
```



L'objet ***connexion*** est désormais en place, et vous allez pouvoir
dialoguer avec lui à l'aide du langage SQL. Il serait possible de le
faire directement à l'aide de certaines méthodes de cet objet[^note_91]
, mais il est préférable de mettre en place pour ce dialogue, encore un
autre objet-interface que l'on appelle un ***curseur**.* Il s'agit d'une
sorte de tampon mémoire intermédiaire, destiné à mémoriser
temporairement les données en cours de traitement, ainsi que les
opérations que vous effectuez sur elles, avant leur transfert définitif
dans la base de données. Cette technique permet donc d'annuler si
nécessaire une ou plusieurs opérations qui se seraient révélées
inadéquates, et de revenir en arrière dans le traitement, sans que la
base de données n'en soit affectée (vous pouvez en apprendre davantage
sur ce concept en consultant l'un des nombreux manuels qui traitent du
langage SQL).



```python
>>> cur =conn.cursor()
```



Une base de données se compose toujours d'une ou plusieurs ***tables***,
qui contiendront les ***enregistrements*** (ou *records*), ceux-ci
comportant eux-mêmes un certain nombre de ***champs*** de différents
types. Ces concepts vous sont probablement familiers si vous avez déjà
travaillé avec un logiciel tableur quelconque : les enregistrements sont
les lignes du tableau, et les champs les cellules d'une ligne. Nous
allons donc rédiger une première requête SQL pour demander la création
d'une nouvelle table :



```python
>>> cur.execute("CREATE TABLE membres (age INTEGER, nom TEXT, taille REAL)") 
```



La requête est exprimée dans une chaîne de caractères classique, que
nous transmettons au curseur par l'intermédiaire de sa méthode
**execute()**. Notez bien que *le langage SQL ne tient aucun compte de
la casse des caractères* : vous pouvez donc encoder vos requêtes SQL
indifféremment en majuscules ou en minuscules. Nous avons
personnellement choisi d'écrire en majuscules les instructions de ce
langage, afin de bien marquer la différence avec les instructions Python
environnantes, mais vous pouvez bien évidemment adopter d'autres
habitudes.

Veuillez également remarquer au passage que les types de données ne
portent pas les mêmes noms en Python et en SQL. La traduction ne devrait
cependant pas vous tracasser outre mesure. Signalons simplement que les
chaînes de caractères seront encodées par défaut en *Utf-8*, suivant en
cela la même convention que celle déjà mentionnée précédemment pour les
fichiers texte (voir page ).

Nous pouvons maintenant entrer des enregistrements :



```python
>>> cur.execute("INSERT INTO membres(age,nom,taille) VALUES(21,'Dupont',1.83)")
>>> cur.execute("INSERT INTO membres(age,nom,taille) VALUES(15,'Blumâr',1.57)")
>>> cur.execute("INSERT Into membres(age,nom,taille) VALUES(18,'Özémir',1.69)")
```



Attention : à ce stade des opérations, les enregistrement sont dans le
tampon du curseur, mais ils n'ont pas encore été transférés
véritablement dans la base de données. Vous pourriez donc annuler tout,
si nécessaire, comme nous le verrons un peu plus loin. Le transfert dans
la basse de données sera déclenché par la méthode **commit()** de
l'objet connexion :



```python
>>> conn.commit() 
```



Le curseur peut alors être refermé, de même que la connexion, si le
travail est terminé[^note_92]
:



```python
>>> cur.close() 
>>> conn.close() 
```



### 18-A-5 - Connexion à une base de données existante {#article.xml#Ld0e74935 .TitreSection2}

À la suite des opérations ci-dessus, un fichier nommé` bd_test.sq3 `aura été crée à
l'emplacement indiqué dans votre machine. Vous pourriez dès lors quitter
Python, et même éventuellement même éteindre votre ordinateur : les
données sont enregistrées. Maintenant, comment faut-il procéder pour y
accéder à nouveau ? C'est très simple : il suffit d'utiliser exactement
les mêmes instructions :



```python
>>> import sqlite3
>>> conn =sqlite3.connect("E:/python3/essais/bd_test.sq3") 
>>> cur =conn.cursor() 
```



L'interrogation de la base s'effectue bien évidemment à l'aide de
requêtes SQL, que l'on confie à la méthode **execute()** du curseur,
toujours sous la forme de chaînes de caractères :



```python
>>> cur.execute("SELECT * FROM membres")
```



Cette requête demande la *sélection* d'un ensemble particulier
d'enregistrements, qui devront être transférés de la base de données au
curseur. Dans le cas présent, la sélection n'en n'est pas tout à fait
une, car nous y demandons en effet d'extraire *tous* les enregistrements
de la table membres (rappelons que le symbole **\*** est fréquemment
utilisé en informatique comme un « joker » ayant la signification « tout
» ou « tous »).

Les enregistrement sélectionnés sont donc à présent dans le curseur. Si
nous voulons les voir, nous devons les en extraire. Cela peut être
réalisé de deux façons, qui peuvent paraître différentes à première vue,
mais qui en réalité tirent parti toutes les deux du fait que
l'objet-curseur produit par Python est un *itérateur*, c'est-à-dire un
dispositif générateur de séquences[^note_93].

Vous pouvez parcourir directement la séquence qu'il produit, à l'aide
d'une boucle **for** classique. Vous obtenez une série de tuples :



```python
>>> for l in cur:
...    print(l) 
... 
(21, 'Dupont', 1.83)
(15, 'Blumâr', 1.57)
(18, 'Özémir', 1.69) 
```



... ou bien la recueillir dans une liste ou un tuple en vue d'un
traitement ultérieur (à l'aide des fonctions intégrées **list()** et
**tuple()**) :



```python
>>> cur.execute("SELECT * FROM membres") 
>>> list(cur) 
[(21, 'Dupont', 1.83), (15, 'Blumâr', 1.57), (18, 'Özémir', 1.69)] 
```



Vous pouvez également, d'une manière plus classique, faire appel à la
méthode **fetchall()** du curseur, laquelle renvoie elle aussi une liste
de tuples :



```python
>>> cur.execute("SELECT * FROM membres") 
>>> cur.fetchall() 
[(21, 'Dupont', 1.83), (15, 'Blumâr', 1.57), (18, 'Özémir', 1.69)]
```



Tant que le curseur reste ouvert, vous pouvez bien entendu ajouter des
enregistrements supplémentaires :



```python
>>> cur.execute("INSERT INTO membres(age,nom,taille) VALUES(19,'Ricard',1.75)")
```



Dans un programme concret, les données à enregistrer se présenteront la
plupart du temps dans des variables Python. Vous devrez donc construire
la chaîne de caractères contenant la requête SQL, en y incluant les
valeurs tirées de ces variables. Il est cependant fortement déconseillé
de faire appel dans ce but aux techniques ordinaires de formatage des
chaînes, car cela peut ouvrir une faille de sécurité dans vos
programmes, en y autorisant les intrusions par la méthode de piratage
connue sous le nom de *SQL injection*[^note_94].
Il faut donc plutôt confier le formatage de vos requêtes au module
d'interface lui-même. La bonne technique est illustrée ci-après : la
chaîne « patron » utilise le point d'interrogation comme balise de
conversion, et le formatage proprement dit est pris en charge par la
méthode **execute()** du curseur :



```python
>>> data =[(17,"Durand",1.74),(22,"Berger",1.71),(20,"Weber",1.65)] 
>>> for tu in data:
...    cur.execute("INSERT INTO membres(age,nom,taille) VALUES(?,?,?)", tu)
...
>>> conn.commit() 
```



Dans cet exemple, la chaîne de requête comporte 3 points
d'interrogation, qui sont nos balises. Elles seront remplacées par les 3
éléments du tuple **tu** à chaque itération de la boucle, le module
d'interface avec SQLite se chargeant de traiter chaque variable
correctement en fonction de son type.

À ce stade des opérations, vous pourriez penser que tout ce que nous
venons de voir est bien compliqué pour écrire et relire ensuite des
informations dans un fichier. Ne serait-il pas plus simple de faire
appel aux procédés de traitement des fichiers texte que nous connaissons
déjà ? Oui et Non. Cela reste vrai pour de petites quantités
d'informations ne nécessitant guère de changements au fil du temps qui
passe, mais n'est plus défendable si l'on considère déjà le simple
problème de la modification ou de la suppression d'un enregistrement
quelconque au sein du fichier. Dans une base de données, c'est très
simple :

Pour modifier un ou plusieurs enregistrements, exécutez une requête du
type :



```python
>>> cur.execute("UPDATE membres SET nom ='Gerart' WHERE nom='Ricard'")
```



Pour supprimer un ou plusieurs enregistrements, utilisez une requête
telle que :



```python
>>> cur.execute("DELETE FROM membres WHERE nom='Gerart'")
```



Avec ce que nous connaissons des fichiers texte, nous devrions
certainement déjà écrire pas mal de lignes de code pour arriver faire la
même chose ! Mais il y a encore beaucoup plus.

> Attention : n'oubliez pas que toutes les modifications apportées au
> curseur se passent en mémoire vive, et de ce fait rien n'est
> enregistré définitivement tant que vous n'exécutez pas l'instruction
> `conn.commit()`. Vous pouvez
> donc annuler toutes les modifications apportées depuis le **commit()** précédent, en refermant la
> connexion à l'aide de l'instruction : **conn.close()**

### 18-A-6 - Recherches sélectives dans une base de données {#article.xml#Ld0e75695 .TitreSection2}

Exercice

.Avant d'aller plus loin, et à titre d'exercice de synthèse, nous allons
vous demander de créer entièrement vous-même une base de données «
Musique » qui contiendra les deux tables suivantes (cela représente un
certain travail, mais il faut que vous puissiez disposer d'un certain
nombre de données pour pouvoir expérimenter valablement les fonctions de
recherche et de tri prises en charge par le SGBDR) :



  ------------------------ ------------------------ ------------------------
  Oeuvres                                           Compositeurs
  comp (chaîne)                                     comp (chaîne)
  titre (chaîne)                                    a\_naiss (entier)
  duree (entier)                                    a\_mort (entier)
  interpr (chaîne)                                  
  ------------------------ ------------------------ ------------------------



Commencez à remplir la table **Compositeurs** avec les données qui
suivent (et profitez de cette occasion pour faire la preuve des
compétences que vous maîtrisez déjà, en écrivant un petit script pour
vous faciliter l'entrée des informations : une boucle s'impose !)



```python
comp	     a_naiss	  a_mort
 
Mozart		1756	   1791
Beethoven      1770	  1827
Haendel        1685	  1759
Schubert       1797	  1828
Vivaldi        1678	  1741
Monteverdi     1567	  1643
Chopin		1810	   1849
Bach	      1685	 1750
Shostakovich   1906	  1975
```



Dans la table **oeuvres**, entrez les données suivantes :



```python
comp	      titre		duree	 interpr
 
Vivaldi      Les quatre saisons      20     T. Pinnock
Mozart	      Concerto piano N°12     25     M. Perahia
Brahms	      Concerto violon N°2     40     A. Grumiaux
Beethoven    Sonate "au clair de lune"	   14	  W. Kempf
Beethoven    Sonate "pathétique"     17     W. Kempf
Schubert     Quintette "la truite"     39     SE of London
Haydn	     La création	 109	 H. Von Karajan
Chopin	      Concerto piano N°1      42     M.J. Pires
Bach	    Toccata & fugue	     9	   P. Burmester
Beethoven    Concerto piano N°4      33     M. Pollini
Mozart	      Symphonie N°40	     29     F. Bruggen
Mozart	      Concerto piano N°22     35     S. Richter
Beethoven    Concerto piano N°3      37     S. Richter
```



Les champs **a\_naiss** et **a\_mort** contiennent respectivement
l'année de naissance et l'année de la mort des compositeurs. La durée
des œuvres est fournie en minutes. Vous pouvez évidemment ajouter autant
d'enregistrements d'œuvres et de compositeurs que vous le voulez, mais
ceux qui précèdent devraient suffire pour la suite de la démonstration.

Pour ce qui va suivre, nous supposerons donc que vous avez effectivement
encodé les données des deux tables décrites ci-dessus. Si vous éprouvez
des difficultés à écrire le script nécessaire, veuillez consulter le
corrigé de l'exercice 16.1, à la page .

Le petit script ci-dessous est fourni à titre purement indicatif. Il
s'agit d'un client SQL rudimentaire, qui vous permet de vous connecter à
la base de données « musique » qui devrait à présent exister dans l'un
de vos répertoires, d'y ouvrir un curseur et d'utiliser celui-ci pour
effectuer des requêtes. Notez encore une fois que rien n'est transcrit
sur le disque tant que la méthode **commit()** n'a pas été invoquée.



```python
# Utilisation d'une petite base de données acceptant les requêtes SQL
 
import sqlite3
 
baseDonn = sqlite3.connect("musique.sq3")
cur = baseDonn.cursor()
while 1:
  print("Veuillez entrer votre requête SQL (ou <Enter> pour terminer) :")
  requete = input()
  if requete =="":
      break
  try:
      cur.execute(requete)	   # exécution de la requête SQL
  except:
      print('*** Requête SQL incorrecte ***')
  else:
      for enreg in cur: 	# Affichage du résultat
      print(enreg)
  print()
 
choix = input("Confirmez-vous l'enregistrement de l'état actuel (o/n) ? ")
if choix[0] == "o" or choix[0] == "O":
  baseDonn.commit()
else:
  baseDonn.close()
```



Cette application très simple n'est évidemment qu'un exemple. Il
faudrait y ajouter la possibilité de choisir la base de données ainsi
que le répertoire de travail. Pour éviter que le script ne se « plante »
lorsque l'utilisateur encode une requête incorrecte, nous avons utilisé
ici le traitement des *exceptions* déjà décrit à la page .

### 18-A-7 - La requête select {#article.xml#Ld0e76141 .TitreSection2}

L'une des instructions les plus puissantes du langage SQL est la requête
**select**, dont nous allons à présent explorer quelques
fonctionnalités. Rappelons encore une fois que nous n'abordons ici
qu'une très petite partie du sujet : la description détaillée de SQL
peut occuper plusieurs livres.

Lancez donc le script ci-dessus, et analysez attentivement ce qui se
passe lorsque vous proposez les requêtes suivantes :



```python
select * from oeuvres
select * from oeuvres where comp = 'Mozart'
select comp, titre, duree  from oeuvres order by comp
select titre, comp from oeuvres where comp='Beethoven' or comp='Mozart'
 order by comp
select count(*) from oeuvres 
select sum(duree) from oeuvres
select avg(duree) from oeuvres
select sum(duree) from oeuvres where comp='Beethoven'
select * from oeuvres where duree >35 order by duree desc
select * from compositeurs where a_mort <1800
select * from compositeurs where a_mort <1800 limit 3
```



Pour chacune de ces requêtes, tâchez d'exprimer le mieux possible ce qui
se passe. Fondamentalement, vous activez sur la base de données des
*filtres de sélection* et des *tris*.

Les requêtes suivantes sont plus élaborées, car elles concernent les
deux tables à la fois.



```python
select o.titre, c.comp, c.a_naiss from oeuvres as o, compositeurs as c
 where o.comp =c.comp
select comp, titre, a_naiss from oeuvres join compositeurs using(comp)	    
select * from oeuvres join compositeurs using(comp) order by a_mort
select comp from oeuvres intersect select comp from compositeurs
select comp from oeuvres except select comp from compositeurs
select comp from compositeurs except select comp from oeuvres
select distinct comp from oeuvres union select comp from compositeurs
```



Il ne nous est pas possible de développer davantage le langage de
requêtes dans le cadre restreint de cet ouvrage. Nous allons cependant
examiner encore un exemple de réalisation Python faisant appel à un
système de bases de données, mais en supposant cette fois qu'il s'agisse
de dialoguer avec un système serveur indépendant (lequel pourrait être
par exemple un gros serveur de bases de données d'entreprise, un serveur
de documentation dans une école, etc.). Du fait qu'il existe
d'excellents logiciels libres et gratuits, vous pouvez aisément mettre
en service vous-même un serveur extrêmement performant tel que
*PostgreSQL*[^note_95].
L'exercice sera particulièrement intéressant si vous prenez la peine
d'installer le logiciel serveur sur une machine distincte de votre poste
de travail habituel, et de relier les deux par l'intermédiaire d'une
connexion réseau de type TCP/IP.


[^note_88]: Il vous faudra certainement entrer quelques informations pour obtenir l'accès : adresse du serveur sur le réseau, nom de la base de données, nom d'utilisateur, mot de passe...

[^note_89]: Quelques variantes subsistent entre différentes implémentations du SQL, pour des requêtes très spécifiques, mais la base reste cependant la même.

[^note_90]: La *Python DataBase Application Programming Interface Specification* définit un ensemble de règles de conduite pour les développeurs de modules d'accès aux divers SGBDR présents et à venir, afin que ces modules soient autant que possible interchangeables. Ainsi la même application Python devrait pouvoir indifféremment utiliser un SGBDR ou un bien un autre, au prix d'un simple échange de modules.

[^note_91]: Le module SQLite de Python propose en effet quelques méthodes-raccourcis pour accéder aux données sans faire usage d'un curseur (plus exactement, en utilisant un curseur implicite). Ces méthodes ne correspondent cependant pas aux techniques standard, et nous préférons donc les ignorer ici.

[^note_92]: Les applications gérant des grosses bases de données sont souvent des applications à utilisateurs multiples. Nous verrons plus loin (page ) que de telles applications mettent en œuvre plusieurs « fils » d'exécution simultanées du programme, que l'on appelle des *threads*, afin de pouvoir gérer en parallèle les requêtes émanant de plusieurs utilisateurs différents. Chacun d'eux disposera ainsi de ses propres objets connexion et curseur au sein du même programme, et il n'y aura pas de télescopages. Dans le cas de SQLite, qui est un système monoposte, la fermeture de la connexion provoque aussi la fermeture du fichier contenant la base de données, ce qui serait différent sur un gros système.

[^note_93]: Les itérateurs font partie des dispositifs de programmation avancée de Python. Nous ne les étudierons pas dans cet ouvrage, de même que bien d'autres instruments très intéressants comme la définition fonctionnelle des listes, les décorateurs, etc. Il vous restera donc encore bien des choses à découvrir, si vous continuez à explorer ce langage !

[^note_94]: Ce problème de sécurité ne se pose en fait que pour des applications web, l'attaquant se servant des champs d'un formulaire HTML pour « injecter » des instructions SQL malicieuses là où le programme n'attend que des chaînes de caractères inoffensives. Il est cependant recommandé d'utiliser de toute façon les techniques de programmation les plus sûres, même pour une simple application monoposte.

[^note_95]: PostgreSQL est un SGBDR libre, disponible selon les termes d'une licence de type BSD. Ce système très élaboré est concurrent d'autres systèmes de gestion de base de données, qu'ils soient libres (comme MySQL et Firebird), ou propriétaires (comme Oracle, Sybase, DB2 et Microsoft SQL Server). Comme les projets libres Apache et Linux, PostgreSQL n'est pas contrôlé par une seule entreprise, mais est fondé sur une communauté mondiale de développeurs et d'entreprises. Des millions d'exemplaires de PostgreSQL sont installés sur des serveurs Web et des serveurs d'application.
