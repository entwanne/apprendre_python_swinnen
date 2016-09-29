## 19-A - Pages web interactives

Le protocole HTTP qui gère la transmission des pages web autorise
l'échange de données dans les deux sens. Mais dans le cas de la simple
consultation de sites, le transfert d'informations a surtout lieu dans
l'un des deux, à savoir du serveur vers le navigateur : des textes, des
images, des fichiers divers lui sont expédiés en grand nombre (ce sont
les pages consultées) ; en revanche, le navigateur n'envoie guère au
serveur que de toutes petites quantités d'information : essentiellement
les adresses URL des pages que l'internaute désire consulter.

Vous savez cependant qu'il existe des sites web où vous êtes invité à
fournir vous-même des quantités d'information plus importantes : vos
références personnelles pour l'inscription à un club ou la réservation
d'une chambre d'hôtel, votre numéro de carte de crédit pour la commande
d'un article sur un site de commerce électronique, votre avis ou vos
suggestions, etc.

Dans ces cas là, vous vous doutez bien que l'information transmise doit
être prise en charge, du côté du serveur, par un *programme* spécifique.
Il faudra donc associer étroitement un tel programme au serveur web.
Quant aux pages web destinées à accueillir cette information (on les
appelle des formulaires), il faudra les doter de divers widgets
d'encodage (champs d'entrée, cases à cocher, boîtes de listes, etc.),
afin que le navigateur puisse soumettre au serveur une *requête*
accompagnée d'arguments. Le serveur pourra alors confier ces arguments
au programme de traitement spécifique, et en fonction du résultat de ce
traitement, renvoyer une *réponse* adéquate à l'internaute, sous la
forme d'une nouvelle page web.

Il existe différentes manières de réaliser de tels programmes
spécifiques, que nous appellerons désormais ***applications web***.

L'une des plus répandues à l'heure actuelle consiste à utiliser des
pages HTML « enrichies » à l'aide de scripts écrits à l'aide d'un
langage spécifique tel que PHP. Ces scripts sont directement insérés
dans le code HTML, entre des balises particulières, et ils seront
exécutés par le serveur web (Apache, par exemple) à la condition que
celui-ci soit doté du module interpréteur adéquat. Il est possible de
procéder de cette façon avec Python via une forme légèrement modifiée du
langage nommée **PSP** (*Python Server Pages*).

Cette approche présente toutefois l'inconvénient de mêler trop
intimement le code de présentation de l'information (le HTML) et le code
de manipulation de celle-ci (les fragments de script PHP ou PSP insérés
entre balises), ce qui compromet gravement la lisibilité de l'ensemble.
Une meilleure approche consiste à écrire des scripts distincts, qui
génèrent du code HTML « classique » sous la forme de chaînes de
caractères, et de doter le serveur web d'un module approprié pour
interpréter ces scripts et renvoyer le code HTML en réponse aux requêtes
du navigateur (par exemple **mod\_python**, dans le cas de Apache).

Mais avec Python, nous pouvons pousser ce type de démarche encore plus
loin, en développant nous-même un véritable serveur web spécialisé, tout
à fait autonome, qui contiendra en un seul logiciel la fonctionnalité
particulière souhaitée pour notre application. Il est en effet
parfaitement possible de réaliser cela à l'aide de Python, car toutes
les bibliothèques nécessaires à la gestion du protocole HTTP sont
intégrées au langage. Partant de cette base, de nombreux programmeurs
indépendants ont d'ailleurs réalisé et mis à la disposition de la
communauté toute une série d'outils de développement pour faciliter la
mise au point de telles applications web spécifiques. Pour la suite de
notre étude, nous utiliserons donc l'un d'entre eux. Nous avons choisi
*Cherrypy*, car celui-ci nous semble particulièrement bien adapté aux
objectifs de cet ouvrage.

> **Note :** Ce que nous allons expliquer dans les paragraphes qui
> suivent sera directement fonctionnel sur l'intranet de votre
> établissement scolaire ou de votre entreprise. En ce qui concerne
> l'internet, par contre, les choses sont un peu plus compliquées. Il va
> de soi que l'installation de logiciels sur un ordinateur serveur relié
> à l'internet ne peut se faire qu'avec l'accord de son propriétaire. Si
> un fournisseur d'accès à l'internet a mis a votre disposition un
> certain espace où vous êtes autorisé à installer des pages web «
> statiques » (c'est-à-dire de simples documents à consulter), cela ne
> signifie pas pour autant que vous pourrez y faire fonctionner des
> programmes ! Pour que cela puisse marcher, il faudra donc que vous
> demandiez une autorisation et un certain nombre de renseignements à
> votre fournisseur d'accès. La plupart d'entre eux refuseront cependant
> de vous laisser installer des applications tout à fait autonomes du
> type que nous décrivons ci-après, mais vous pourrez assez facilement
> convertir celles-ci afin qu'elles soient également utilisables avec le
> module mod\_python de Apache, lequel est généralement disponible[^note_97].

### 19-A-1 - Un serveur web en pur Python ! {#article.xml#Ld0e80586 .TitreSection2}

L'intérêt pour le développement web est devenu très important à notre
époque, et il existe donc une forte demande pour des interfaces et des
environnements de programmation bien adaptés à cette tâche. Or, même
s'il ne peut pas prétendre à l'universalité de langages tels que C/C++,
Python est déjà largement utilisé un peu partout dans le monde pour
écrire des programmes très ambitieux, y compris dans le domaine des
serveurs d'applications web. La robustesse et la facilité de mise en
œuvre du langage ont séduit de nombreux développeurs de talent, qui ont
réalisé des outils de développement web de très haut niveau. Plusieurs
de ces applications peuvent vous intéresser si vous souhaitez réaliser
vous-même des sites web interactifs de différents types.

Les produits existants sont pour la plupart des logiciels libres. Ils
permettent de couvrir une large gamme de besoins, depuis le petit site
personnel de quelques pages, jusqu'au gros site commercial collaboratif,
capable de répondre à des milliers de requêtes journalières, et dont les
différents secteurs sont gérés sans interférence par des personnes de
compétences variées (infographistes, programmeurs, spécialistes de bases
de données, etc.).

Le plus célèbre de ces produits est le logiciel *Zope*, déjà adopté par
de grands organismes privés et publics pour le développement d'intranets
et d'extranets collaboratifs. Il s'agit en fait d'un système serveur
d'applications, très performant, sécurisé, presqu'entièrement écrit en
Python, et que l'on peut administrer à distance à l'aide d'une simple
interface web. Il ne nous est pas possible de décrire l'utilisation de
*Zope* dans ces pages : le sujet est trop vaste, et un livre entier n'y
suffirait pas. Sachez cependant que ce produit est parfaitement capable
de gérer de très gros sites d'entreprise en offrant d'énormes avantages
par rapport à des solutions plus connues telles que PHP ou Java.

D'autres outils moins ambitieux mais tout aussi intéressants sont
disponibles. Tout comme *Zope*, la plupart d'entre eux peuvent être
téléchargés librement depuis Internet. Le fait qu'ils soient écrits en
Python assure en outre leur portabilité : vous pourrez donc les employer
aussi bien sous *Windows* que sous *Linux* ou *MacOs*. Chacun d'eux peut
être utilisé en conjonction avec un serveur web « classique » tel que
*Apache* ou *Xitami* (c'est d'ailleurs préférable si le site à réaliser
est destiné à supporter une charge de connexions importante sur
l'internet), mais la plupart d'entre eux intègrent leur propre serveur,
ce qui leur permet de fonctionner également de manière tout à fait
autonome. Cette possibilité se révèle particulièrement intéressante au
cours de la mise au point d'un site, car elle facilite la recherche des
erreurs.

Une totale autonomie, alliée à une grande facilité de mise en œuvre,
font de ces produits de fort bonnes solutions pour la réalisation de
sites web d'intranet spécialisés, notamment dans des petites et moyennes
entreprises, des administrations, ou dans des écoles. Si vous souhaitez
développer une application Python qui soit accessible à distance, par
l'intermédiaire d'un simple navigateur web, ces outils sont faits pour
vous. Il en existe une grande variété : *Django*, *Turbogears*, *Spyce*,
*Karrigell*, *Webware*, *Cherrypy*, *Quixote*, *Twisted*, *Pylons*,
etc[^note_98].
Choisissez en fonction de vos besoins : vous n'aurez que l'embarras du
choix.

Dans les lignes qui suivent, nous allons décrire pas à pas le
développement d'une application web fonctionnant à l'aide de
***Cherrypy***. Vous pouvez trouver ce système à l'adresse :
*http://www.cherrypy.org.* Il s'agit d'une solution de développement web
très conviviale pour un programmeur Python, car elle lui permet de le
développer un site web comme une application Python classique, sur la
base d'un ensemble d'objets. Ceux-ci génèrent du code HTML en réponse
aux requêtes HTTP qu'on leur adresse via leurs méthodes, et ces méthodes
sont elles-mêmes perçues comme des adresses URL ordinaires par les
navigateurs.

> Pour la suite de ce texte, nous allons supposer que vous possédez
> quelques rudiments du langage HTML, et nous admettrons également que
> la bibliothèque Cherrypy a déjà été installée sur votre poste de
> travail. (Cette installation est décrite à la page ).

### 19-A-2 - Première ébauche : mise en ligne d'une page web minimaliste {#article.xml#Ld0e80664 .TitreSection2}

Dans votre répertoire de travail, préparez un petit fichier texte que
vous nommerez `tutoriel.conf`, et
qui contiendra les lignes suivantes :



```python
[global] 
server.socket_host = "127.0.0.1" 
server.socket_port = 8080 
server.thread_pool = 5 
tools.sessions.on = True 
tools.encode.encoding = "Utf-8" 
[/annexes] 
tools.staticdir.on = True 
tools.staticdir.dir = "annexes" 
```



Il s'agit d'un simple fichier de configuration que notre serveur web
consultera au démarrage. Notez surtout le n° de port utilisé (8080 dans
notre exemple). Vous savez peut-être que les logiciels navigateurs
s'attendent à trouver les services web sur le n° de port 80 par défaut.
Si vous êtes le propriétaire de votre machine, et que vous n'y avez
encore installé aucun autre logiciel serveur web, vous avez donc
probablement intérêt à remplacer 8080 par 80 dans ce fichier de
configuration : ainsi les navigateurs qui se connecteront à votre
serveur ne devront pas spécifier un n° de port dans l'adresse.
Cependant, si vous faites ces exercices sur une machine dont vous n'êtes
pas l'administrateur, vous n'avez pas le droit d'utiliser les numéros de
port inférieurs à 1024 (pour des raisons de sécurité). Dans ce cas, vous
devez donc utiliser un numéro de port plus élevé que 80, tel celui que
nous vous proposons. Il en va de même si un autre serveur web (*Apache*,
par exemple) est déjà en fonction sur votre machine, car ce logiciel
utilise très certainement déjà le port 80, par défaut.

Remarquez également la ligne concernant l'encodage. Il s'agit de
l'encodage que *Cherrypy* devra utiliser dans les pages web produites.
Il est possible que certains navigateurs web attendent une autre norme
que Utf-8 comme encodage par défaut. Si vous obtenez des caractères
accentués incorrects dans votre navigateur lorsque vous expérimenterez
les exercices décrits ci-après, refaites vos essais en spécifiant un
autre encodage dans cette ligne.

Les 3 dernières lignes du fichier indiquent le chemin d'un répertoire où
vous placerez les documents « statiques » dont votre site peut avoir
besoin (images, feuilles de style, etc.).

Veuillez à présent encoder le petit script ci-dessous :



1.  ``` {.LignePreCode}
    import cherrypy 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    class MonSiteWeb(object):      # Classe maîtresse de l'application 
    ```

4.  ``` {.LignePreCode}
      def index(self):	   # Méthode invoquée comme URL racine (/) 
    ```

5.  ``` {.LignePreCode}
          return "<h1>Bonjour à tous !</h1>" 
    ```

6.  ``` {.LignePreCode}
      index.exposed = True	    # la méthode doit être ?publiée' 
    ```

7.  ``` {.LignePreCode}
      
    ```

8.  ``` {.LignePreCode}
    ###### Programme principal : ############# 
    ```

9.  ``` {.LignePreCode}
    cherrypy.quickstart(MonSiteWeb(), config ="tutoriel.conf") 
    ```



Lancez l'exécution du script. Si tout est en ordre, vous obtenez
quelques lignes d'information similaires aux suivantes dans votre
terminal. Elles vous confirment que « quelque chose » a démarré, et
reste en attente d'événements :



```python
[07/Jan/2010:18:00:34] ENGINE Listening for SIGHUP. 
[07/Jan/2010:18:00:34] ENGINE Listening for SIGTERM. 
[07/Jan/2010:18:00:34] ENGINE Listening for SIGUSR1. 
[07/Jan/2010:18:00:34] ENGINE Bus STARTING 
[07/Jan/2010:18:00:34] ENGINE Started monitor thread '_TimeoutMonitor'. 
[07/Jan/2010:18:00:34] ENGINE Started monitor thread 'Autoreloader'. 
[07/Jan/2010:18:00:34] ENGINE Serving on 127.0.0.1:8080 
[07/Jan/2010:18:00:34] ENGINE Bus STARTED 
```



***Vous venez effectivement de mettre en route un serveur web !***

Il ne vous reste plus qu'à vérifier qu'il fonctionne bel et bien, à
l'aide de votre navigateur préféré. Si vous utilisez ce navigateur sur
la même machine que le serveur, dirigez-le vers une adresse telle que :
*http://localhost:8080*, « localhost » étant une expression consacrée
pour désigner la machine locale (vous pouvez également spécifier
celle-ci à l'aide de l'adresse IP conventionnelle : 127.0.0.1), et «
8080 » le numéro de port choisi dans le fichier de configuration[^note_99].
Vous devriez obtenir la page d'accueil suivante :



![](images/100000000000027F000000FE20EAD0ED.png)



Examinons à présent notre script d'un peu plus près.\
 Sa concision est remarquable : seulement 6 lignes effectives !

Après importation du module **cherrypy**, on y définit une nouvelle
classe **MonSiteWeb()**. Les objets produits à l'aide de cette classe
seront des gestionnaires de requêtes. Leurs méthodes seront invoquées
par un dispositif interne à *Cherrypy*, qui convertira l'adresse *url*
demandée par le navigateur, en un appel de méthode avec un nom
équivalent (nous illustrerons mieux ce mécanisme avec l'exemple
suivant). Si l'*url* reçue ne comporte aucun nom de page, comme c'est le
cas ici, c'est le nom **index** qui sera recherché par défaut, suivant
une convention bien établie sur le web. C'est pour cette raison que nous
avons nommé ainsi notre unique méthode, qui attend donc les requêtes
s'adressant à la racine du site.

-   Ligne 5 : Les méthodes de cette classe vont donc traiter les
    requêtes provenant du navigateur, et lui renvoyer en réponse des
    chaînes de caractères contenant du texte rédigé en HTML. Pour ce
    premier exercice, nous avons simplifié au maximum le code HTML
    produit, le résumant à un petit message inséré entre deux balises de
    titre (\<*h1*\> et \</*h1*\>). En toute rigueur, nous aurions dû
    insérer le tout entre balises \<*html*\>\</*html*\> et
    \<*body*\>\</*body*\> afin de réaliser une mise en page correcte.
    Mais puisque cela peut déjà fonctionner ainsi, nous attendrons
    encore un peu avant de montrer nos bonnes manières.
-   Ligne 6 : Les méthodes destinées à traiter une requête HTTP et à
    renvoyer en retour une page web, doivent être « publiées » à l'aide
    d'un attribut **exposed** contenant une valeur « vraie ». Il s'agit
    là d'un dispositif de sécurité mis en place par *Cherrypy*, qui fait
    que par défaut, toutes les méthodes que vous écrivez sont protégées
    vis-à-vis des tentatives d'accès extérieurs indésirables. Les seules
    méthodes « accessibles » seront donc celles qui auront été
    délibérément rendues « publiques » à l'aide de cet attribut.
-   Ligne 9 : La fonction **quickstart()** du module *cherrypy* démarre
    le serveur proprement dit. Il faut lui fournir en argument la
    référence de l'objet gestionnaire de requêtes qui sera la racine du
    site, ainsi que la référence d'un fichier de configuration générale.

### 19-A-3 - Ajout d'une deuxième page {#article.xml#Ld0e80967 .TitreSection2}

Le même objet gestionnaire peut bien entendu prendre en charge plusieurs
pages :



1.  ``` {.LignePreCode}
    import cherrypy 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    class MonSiteWeb(object): 
    ```

4.  ``` {.LignePreCode}
      
    ```

5.  ``` {.LignePreCode}
      def index(self): 
    ```

6.  ``` {.LignePreCode}
          # Renvoi d'une page HTML contenant un lien vers une autre page 
    ```

7.  ``` {.LignePreCode}
          # (laquelle sera produite par une autre méthode du même objet) : 
    ```

8.  ``` {.LignePreCode}
          return ''' 
    ```

9.  ``` {.LignePreCode}
          <h2>Veuillez cliquer ici 
    ```

10. ``` {.LignePreCode}
          pour accéder à une information d'importance cruciale.</h2> 
    ```

11. ``` {.LignePreCode}
          ''' 
    ```

12. ``` {.LignePreCode}
      index.exposed = True 
    ```

13. ``` {.LignePreCode}
      
    ```

14. ``` {.LignePreCode}
      def unMessage(self): 
    ```

15. ``` {.LignePreCode}
          return "<h1>La programmation, c'est génial !</h1>" 
    ```

16. ``` {.LignePreCode}
      unMessage.exposed = True 
    ```

17. ``` {.LignePreCode}
      
    ```

18. ``` {.LignePreCode}
    cherrypy.quickstart(MonSiteWeb(), config ="tutoriel.conf") 
    ```



Ce script dérive directement du précédent. La page renvoyée par la
méthode **index()** contient cette fois une balise-lien :`  `dont l'argument
est *l'url* d'une autre page. Si cette *url* est un simple nom, la page
correspondante est supposée se trouver dans le répertoire racine du
site. Dans la logique de conversion des *url* utilisée par *Cherrypy*,
cela revient à invoquer une méthode de l'objet racine possédant un nom
équivalent. Dans notre exemple, la page référencée sera donc produite
par la méthode **unMessage()**.

### 19-A-4 - Présentation et traitement d'un formulaire {#article.xml#Ld0e81368 .TitreSection2}

Les choses vont vraiment commencer à devenir intéressantes avec le
script suivant :



1.  ``` {.LignePreCode}
    import cherrypy 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    class Bienvenue(object): 
    ```

4.  ``` {.LignePreCode}
      def index(self): 
    ```

5.  ``` {.LignePreCode}
          # Formulaire demandant son nom à l'utilisateur : 
    ```

6.  ``` {.LignePreCode}
          return ''' 
    ```

7.  ``` {.LignePreCode}
           
    ```

8.  ``` {.LignePreCode}
          Bonjour. Quel est votre nom ? 
    ```

9.  ``` {.LignePreCode}
           
    ```

10. ``` {.LignePreCode}
           
    ```

11. ``` {.LignePreCode}
           
    ```

12. ``` {.LignePreCode}
          ''' 
    ```

13. ``` {.LignePreCode}
      index.exposed = True 
    ```

14. ``` {.LignePreCode}
      
    ```

15. ``` {.LignePreCode}
      def salutations(self, nom =None): 
    ```

16. ``` {.LignePreCode}
          if nom:	      # Accueil de l'utilisateur : 
    ```

17. ``` {.LignePreCode}
          return "Bonjour, {}, comment allez-vous ?".format(nom) 
    ```

18. ``` {.LignePreCode}
          else:	    # Aucun nom n'a été fourni : 
    ```

19. ``` {.LignePreCode}
          return 'Veuillez svp fournir votre nom ici.' 
    ```

20. ``` {.LignePreCode}
      salutations.exposed = True 
    ```

21. ``` {.LignePreCode}
      
    ```

22. ``` {.LignePreCode}
    cherrypy.quickstart(Bienvenue(), config ="tutoriel.conf") 
    ```



La méthode **index()** de notre objet racine présente cette fois à
l'utilisateur une page web contenant *un formulaire* : le code HTML
inclus entre les balises `` et `` peut en effet contenir un
ensemble de widgets divers, à l'aide desquels l'internaute pourra
encoder des informations et exercer une certaine activité : champs
d'entrée, cases à cocher, boutons radio, boîtes de listes, etc. Pour ce
premier exemple, un champ d'entrée et un bouton suffiront :



![](images/1000000000000253000000DA5799D7BC.png)



-   La ligne 9 contient la balise HTML qui définit un champ d'entrée
    (balise **\**). Son attribut `name` permet d'associer une étiquette
    à la chaîne de caractères qui sera encodée par l'utilisateur.
    Lorsque le navigateur transmettra au serveur la requête HTTP
    correspondante, celle-ci contiendra donc cet argument bien étiqueté.
    Comme nous l'avons déjà expliqué plus haut, *Cherrypy* convertira
    alors cette requête en un appel de méthode classique, dans lequel
    l'étiquette sera associée à son argument, de la manière habituelle
    sous Python.
-   La ligne 10 définit un widget de type « bouton d'envoi » (balise
    ``). Le
    texte qui doit apparaître sur le bouton est précisé par l'attribut
    `value`.
-   Les lignes 15 à 20 définissent la méthode qui réceptionnera la
    requête, lorsque le formulaire aura été expédié au serveur. Son
    paramètre `nom` recevra
    l'argument correspondant, reconnu grâce à son étiquette homonyme.
    Comme d'habitude sous Python, vous pouvez définir des valeurs par
    défaut pour chaque paramètre (si un champ du formulaire est laissé
    vide par l'utilisateur, l'argument correspondant n'est pas
    transmis). Dans notre exemple, le paramètre `nom` contient par défaut un objet
    vide : il sera donc très facile de vérifier par programme, si
    l'utilisateur a effectivement entré un nom ou pas.

Le fonctionnement de tous ces mécanismes est finalement très naturel et
très simple : les *url* invoquées dans les pages web sont converties par
*Cherrypy* en appels de méthodes possédant les mêmes noms, auxquelles
les arguments sont transmis de manière tout à fait classique.

### 19-A-5 - Analyse de la communication et des erreurs {#article.xml#Ld0e81943 .TitreSection2}

En expérimentant les scripts décrits jusqu'ici, vous aurez remarqué que
divers messages apparaissent dans la fenêtre de terminal où vous avez
lancé leur exécution. Ces messages vous renseignent (en partie) sur le
dialogue qui s'est instauré entre le serveur et ses clients. Vous
pourrez ainsi y suivre la connexion éventuellement établie avec votre
serveur par d'autres machines (si votre serveur est relié à un réseau,
bien entendu) :.



```python
[12/Jan/2010:14:43:27] ENGINE Started monitor thread '_TimeoutMonitor'. 
[12/Jan/2010:14:43:27] ENGINE Started monitor thread 'Autoreloader'. 
[12/Jan/2010:14:43:27] ENGINE Serving on 127.0.0.1:8080 
[12/Jan/2010:14:43:27] ENGINE Bus STARTED 
127.0.0.1 - - [12/Jan/2010:14:43:31] "GET / HTTP/1.1" 200 215 "" "Mozilla/5.0
(X11; U; Linux i686; fr; rv:1.9.1.6) Gecko/20091215 Ubuntu/9.10 (karmic)
 Firefox/3.5.6" 
127.0.0.1 - - [12/Jan/2010:14:44:07] "GET /salutations?nom=Juliette HTTP/1.1"
 200 39 "http://localhost:8080/" "Mozilla/5.0 (X11; U; Linux i686; fr;
 rv:1.9.1.6) Gecko/20091215 Ubuntu/9.10 (karmic) Firefox/3.5.6" 
```



C'est dans cette fenêtre de terminal que vous trouverez également les
messages d'erreur (fautes de syntaxe, par exemple) qui se rapportent à
tout ce que votre programme met éventuellement en place *avant le
démarrage du serveur*. Si une erreur est détectée en cours de
fonctionnement, par contre (erreur dans une méthode gestionnaire de
requêtes), le message d'erreur correspondant apparaît dans la fenêtre du
navigateur, ***et le serveur continue de fonctionner***. Voici par
exemple le message que nous avons obtenu en ajoutant un ‘e' erroné au
nom de la méthode **format()**, à la ligne 17 de notre script (`formate(nom)` au lieu de `format(nom)`) :



![](images/1000000000000344000001BA05E93E34.png)



Vous pouvez vérifier que le serveur fonctionne toujours, en revenant à
la page précédente et en entrant cette fois un nom vide. Cette faculté
de ne pas se bloquer complètement lorsqu'une erreur est détectée est
extrêmement importante pour un serveur web, car cela lui permet de
continuer à répondre à la majorité des requêtes qu'il reçoit, même si
certaines d'entre elles doivent être rejetées parce qu'il subsiste
quelques petits défauts dans le programme. Ce comportement robuste est
rendu possible par l'utilisation de threads (voir page ).

### 19-A-6 - Structuration d'un site à pages multiples {#article.xml#Ld0e82057 .TitreSection2}

Voyons à présent comment nous pouvons organiser notre site web de
manière bien structurée, en établissant une hiérarchie entre les classes
d'une manière analogue à celle qui lie les répertoires et
sous-répertoires dans un système de fichiers.



![](images/100000000000025D00000126083BE4D8.png)





1.  ``` {.LignePreCode}
    import cherrypy 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    class HomePage(object): 
    ```

4.  ``` {.LignePreCode}
      def __init__(self): 
    ```

5.  ``` {.LignePreCode}
          # Les objets gestionnaires de requêtes peuvent instancier eux-mêmes 
    ```

6.  ``` {.LignePreCode}
          # d'autres gestionnaires "esclaves", et ainsi de suite : 
    ```

7.  ``` {.LignePreCode}
          self.maxime = MaximeDuJour() 
    ```

8.  ``` {.LignePreCode}
          self.liens = PageDeLiens() 
    ```

9.  ``` {.LignePreCode}
          # L'instanciation d'objets gestionnaires de requêtes peut bien entendu 
    ```

10. ``` {.LignePreCode}
          # être effectuée à n'importe quel niveau du programme. 
    ```

11. ``` {.LignePreCode}
      
    ```

12. ``` {.LignePreCode}
      def index(self): 
    ```

13. ``` {.LignePreCode}
          return ''' 
    ```

14. ``` {.LignePreCode}
          <h3>Site des adorateurs du Python royal - Page d'accueil.</h3> 
    ```

15. ``` {.LignePreCode}
          Veuillez visiter nos rubriques géniales : 
    ```

16. ``` {.LignePreCode}
           
    ```

17. ``` {.LignePreCode}
    	  Restons entre nous 
    ```

18. ``` {.LignePreCode}
    	  Une maxime subtile 
    ```

19. ``` {.LignePreCode}
    	  Des liens utiles 
    ```

20. ``` {.LignePreCode}
           
    ```

21. ``` {.LignePreCode}
          ''' 
    ```

22. ``` {.LignePreCode}
      index.exposed = True 
    ```

23. ``` {.LignePreCode}
      
    ```

24. ``` {.LignePreCode}
      def entreNous(self): 
    ```

25. ``` {.LignePreCode}
          return ''' 
    ```

26. ``` {.LignePreCode}
          Cette page est produite à la racine du site. 
    ```

27. ``` {.LignePreCode}
          [Retour] 
    ```

28. ``` {.LignePreCode}
          ''' 
    ```

29. ``` {.LignePreCode}
      entreNous.exposed =True 
    ```

30. ``` {.LignePreCode}
      
    ```

31. ``` {.LignePreCode}
    class MaximeDuJour(object): 
    ```

32. ``` {.LignePreCode}
      def index(self): 
    ```

33. ``` {.LignePreCode}
          return ''' 
    ```

34. ``` {.LignePreCode}
          <h3>Il existe 10 sortes de gens : ceux qui comprennent 
    ```

35. ``` {.LignePreCode}
          le binaire, et les autres !</h3> 
    ```

36. ``` {.LignePreCode}
          [Retour] 
    ```

37. ``` {.LignePreCode}
          ''' 
    ```

38. ``` {.LignePreCode}
      index.exposed = True 
    ```

39. ``` {.LignePreCode}
      
    ```

40. ``` {.LignePreCode}
    class PageDeLiens(object): 
    ```

41. ``` {.LignePreCode}
      def __init__(self): 
    ```

42. ``` {.LignePreCode}
          self.extra = LiensSupplementaires() 
    ```

43. ``` {.LignePreCode}
      
    ```

44. ``` {.LignePreCode}
      def index(self): 
    ```

45. ``` {.LignePreCode}
          return ''' 
    ```

46. ``` {.LignePreCode}
          Page racine des liens (sans utilité réelle). 
    ```

47. ``` {.LignePreCode}
          En fait, les liens sont plutôt ici 
    ```

48. ``` {.LignePreCode}
          ''' 
    ```

49. ``` {.LignePreCode}
      index.exposed = True 
    ```

50. ``` {.LignePreCode}
      
    ```

51. ``` {.LignePreCode}
      def utiles(self): 
    ```

52. ``` {.LignePreCode}
          # Veuillez noter comment le lien vers les autres pages est défini : 
    ```

53. ``` {.LignePreCode}
          # on peut procéder de manière ABSOLUE ou RELATIVE. 
    ```

54. ``` {.LignePreCode}
          return ''' 
    ```

55. ``` {.LignePreCode}
          Quelques liens utiles : 
    ```

56. ``` {.LignePreCode}
           
    ```

57. ``` {.LignePreCode}
    	  Site de CherryPy 
    ```

58. ``` {.LignePreCode}
    	  Site de Python 
    ```

59. ``` {.LignePreCode}
           
    ```

60. ``` {.LignePreCode}
          D'autres liens utiles vous sont proposés 
    ```

61. ``` {.LignePreCode}
           ici . 
    ```

62. ``` {.LignePreCode}
          [Retour] 
    ```

63. ``` {.LignePreCode}
          ''' 
    ```

64. ``` {.LignePreCode}
      utiles.exposed = True 
    ```

65. ``` {.LignePreCode}
      
    ```

66. ``` {.LignePreCode}
    class LiensSupplementaires(object): 
    ```

67. ``` {.LignePreCode}
      def index(self): 
    ```

68. ``` {.LignePreCode}
          # Notez le lien relatif pour retourner à la page maîtresse : 
    ```

69. ``` {.LignePreCode}
          return ''' 
    ```

70. ``` {.LignePreCode}
          Encore quelques autres liens utiles : 
    ```

71. ``` {.LignePreCode}
           
    ```

72. ``` {.LignePreCode}
    	  Le site de l'auteur 
    ```

73. ``` {.LignePreCode}
    	  Ubuntu : le must 
    ```

74. ``` {.LignePreCode}
           
    ```

75. ``` {.LignePreCode}
          [Retour à la page racine des liens] 
    ```

76. ``` {.LignePreCode}
          ''' 
    ```

77. ``` {.LignePreCode}
      index.exposed = True 
    ```

78. ``` {.LignePreCode}
      
    ```

79. ``` {.LignePreCode}
    racine = HomePage() 
    ```

80. ``` {.LignePreCode}
    cherrypy.quickstart(racine, config ="tutoriel.conf") 
    ```



Lignes 4 à 10 : La méthode constructeur des objets racine est l'endroit
idéal pour instancier d'autres objets « esclaves ». On accédera aux
méthodes gestionnaires de requêtes de ceux-ci exactement comme on accède
aux sous-répertoires d'un répertoire racine (voir ci-après).

Lignes 12 à 22 : La page d'accueil propose des liens vers les autres
pages du site. Remarquez la syntaxe utilisée dans les balises-liens,
utilisée ici de manière à définir un ***chemin absolu*** :

-   les méthodes de l'objet racine sont référencées par un caractère /
    suivi de leur nom seul. Le caractère / indique que le « chemin »
    part de la racine du site. Exemple : `/entreNous`.
-   les méthodes racines des objets esclaves sont référencées à l'aide
    d'un simple / suivant le nom de ces autres objets. Exemple : `/maxime/`
-   les autres méthodes des objets esclaves sont référencées à l'aide de
    leur nom inclus dans un chemin complet : Exemple : `/liens/utiles`

Lignes 36, 62 et 75 : Pour retourner à la racine du niveau précédent, on
utilise cette fois un ***chemin relatif***, avec la même syntaxe que
celle utilisée pour remonter au répertoire précédent dans une
arborescence de fichiers (deux points).

Lignes 41-42 : Vous aurez compris qu'on installe ainsi une hiérarchie en
forme d'arborescence de fichiers, en instanciant des objets « esclaves »
les uns à partir des autres. En suivant cette logique, le chemin absolu
complet menant à la méthode **index()** de cette classe devrait être par
conséquent `/liens/extra/index`.

### 19-A-7 - Prise en charge des sessions {#article.xml#Ld0e84316 .TitreSection2}

Lorsqu'on élabore un site web interactif, on souhaite fréquemment que la
personne visitant le site puisse s'identifier et fournir un certain
nombre de renseignements tout au long de sa visite dans différentes
pages (l'exemple type est le remplissage d'un *caddie* au cours de la
consultation d'un site commercial), toutes ces informations étant
conservées quelque part jusqu'à la fin de sa visite. *Et il faut bien
entendu réaliser cela indépendamment pour chaque client connecté*, car
nous ne pouvons pas oublier qu'un site web est destiné à être utilisé en
parallèle par toute une série de personnes.

Il serait possible de transmettre ces informations de page en page, à
l'aide de champs de formulaires cachés (balises `<INPUT TYPE="hidden">`), mais ce serait
compliqué et très contraignant. Il est donc préférable que le serveur
soit doté d'un mécanisme spécifique, qui attribue à chaque client une
*session* particulière, dans laquelle seront mémorisées toutes les
informations particulières à ce client. *Cherrypy* réalise cet objectif
par l'intermédiaire de *cookies*.

Lorsqu'un nouveau visiteur du site se présente, le serveur génère un
*cookie* (c'est-à-dire un petit paquet d'informations contenant un
*identifiant de session* unique sous la forme d'une chaîne aléatoire
d'octets) et l'envoie au navigateur web, qui l'enregistre. En relation
avec le cookie généré, le serveur va alors conserver durant un certain
temps un *objet-session* dans lequel seront mémorisées toutes les
informations spécifiques du visiteur. Lorsque celui-ci parcourt les
autres pages du site, son navigateur renvoie à chaque fois le contenu du
cookie au serveur, ce qui permet à celui-ci de l'identifier et de
retrouver l'objet-session qui lui correspond. L'objet-session reste donc
disponible tout au long de la visite de l'internaute : il s'agit d'un
objet Python ordinaire, dans lequel on mémorise un nombre quelconque
d'informations sous forme d'attributs.

Au niveau de la programmation, voici comment cela se passe :



1.  ``` {.LignePreCode}
    import cherrypy 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    class CompteurAcces(object): 
    ```

4.  ``` {.LignePreCode}
      def index(self): 
    ```

5.  ``` {.LignePreCode}
          # Exemple simplissime : incrémentation d'un compteur d'accès. 
    ```

6.  ``` {.LignePreCode}
          # On commence par récupérer le total actuel du comptage : 
    ```

7.  ``` {.LignePreCode}
          count = cherrypy.session.get('count', 0) 
    ```

8.  ``` {.LignePreCode}
          # ... on l'incrémente : 
    ```

9.  ``` {.LignePreCode}
          count += 1 
    ```

10. ``` {.LignePreCode}
          # ... on mémorise sa nouvelle valeur dans le dictionnaire de session : 
    ```

11. ``` {.LignePreCode}
          cherrypy.session['count'] = count 
    ```

12. ``` {.LignePreCode}
          # ... et on affiche le compte actuel : 
    ```

13. ``` {.LignePreCode}
          return ''' 
    ```

14. ``` {.LignePreCode}
          Durant la présente session, vous avez déjà visité 
    ```

15. ``` {.LignePreCode}
          cette page {} fois ! Votre vie est bien excitante ! 
    ```

16. ``` {.LignePreCode}
          '''.format(count) 
    ```

17. ``` {.LignePreCode}
      index.exposed = True 
    ```

18. ``` {.LignePreCode}
      
    ```

19. ``` {.LignePreCode}
    cherrypy.quickstart(CompteurAcces(), config='tutoriel.conf') 
    ```





![](images/1000000000000263000000D743AA5748.png)



Il vous suffit de redemander la page produite par ce script à plusieurs
reprises. Vous constaterez qu'à chaque fois le compteur de visites est
bien incrémenté :

Le script lui-même devrait être assez explicite. On y remarquera que le
module **cherrypy** est doté d'un objet **session** qui se comporte
(apparemment) comme un dictionnaire classique. Nous pouvons lui ajouter
des clefs à volonté, et associer à ces clefs des valeurs quelconques.

À la ligne 7 de notre exemple, nous utilisons la méthode **get()** des
dictionnaires, pour retrouver la valeur associée à la clef **count** (ou
zéro, si la clef n'existe pas encore). À la ligne 11 nous
ré-enregistrons ensuite cette valeur, incrémentée, dans le même
dictionnaire. Ainsi nous pouvons constater une fois de plus que
*Cherrypy* met à notre disposition un environnement de programmation
tout à fait familier pour un habitué de Python.

Remarquons toutefois que l'objet **session**, qui se comporte pour nous
comme un simple dictionnaire, est en réalité l'interface d'une
machinerie interne complexe, puisqu'il nous « sert » automatiquement les
informations qui correspondent à un client particulier de notre site,
identifié par l'intermédiaire de son cookie de session.

Pour bien visualiser cela, faites donc l'expérience d'accéder à votre
serveur depuis deux navigateurs différents[^note_100]
(Firefox et Opera, par exemple) : vous constaterez que le décompte des
visites est bel et bien différent pour chacun d'eux.


[^note_97]: Veuillez pour cela consulter des ouvrages plus spécialisés, comme par exemple *Cherrypy Essentials*, par Sylvain Hellegouarch - Packt Publishing, Birmingham, 2007. (Un ouvrage de référence concernant Cherrypy).

[^note_98]: Cherrypy vient tout juste d'être rendu disponible pour la version 3 de Python au moment où nous écrivons ces lignes. Parmi les autres outils mentionnés ici, plusieurs sont encore en cours d'adaptation, mais ils restent de toute façon parfaitement utilisables avec les versions antérieures de Python.

[^note_99]: Si vous avez choisi le n^o^ de port par défaut (80) dans le fichier de configuration, il est inutile de le rappeler dans les adresses, puisque c'est ce numéro de port qui est utilisé par défaut par la plupart des navigateurs. Vous pouvez donc dans ce cas vous connecter à votre nouveau site en entrant simplement : *http://localhost* .

[^note_100]: Attention : les sessions ne pourront être distinguées qu'au départ de machines différentes (utilisant des navigateurs quelconques), ou bien de navigateurs différents fonctionnant sur la même machine. Si vous lancez deux instances du même navigateur sur la même machine, elles vont utiliser des cookies communs, ce qui signifie que le serveur ne pourra pas différencier les requêtes émanant de l'une ou de l'autre. En d'autres termes, ces deux instances du même navigateur partageront la même session.
