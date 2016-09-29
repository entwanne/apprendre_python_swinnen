## 19-B - Réalisation concrète d'un site web interactif

Avec tout ce que vous avez appris jusqu'ici, vous devriez désormais
pouvoir envisager la réalisation d'un projet d'une certaine importance.
C'est ce que nous vous proposons ci-après en vous détaillant la mise en
place d'une ébauche d'un site web quelque peu élaborée, utilisable pour
la réservation en ligne de places de spectacle[^note_101]
:



![](images/100000000000027A000002218D36C75F.png)



Les « administrateurs » du site peuvent ajouter de nouveaux spectacles à
la liste et visionner les réservations déjà effectuées. Les « clients »
peuvent s'enregistrer, réserver des places pour l'un ou l'autre des
spectacles annoncés, et lister les places qu'ils ont déjà achetées.

Du fait qu'il ne s'agit toujours que d'un exercice, les fonctionnalités
de cette petite application sont forcément très incomplètes. Il y manque
notamment un dispositif de contrôle d'accès pour les administrateurs
(via un système de *login/mot de passe* par exemple), la possibilité de
supprimer ou modifier des spectacles existants, une gestion correcte des
dates, des adresses courriel et des numéros de téléphone (ce sont ici de
simples chaînes de caractères), etc., etc.

L'application intègre cependant une petite base de données relationnelle
comportant trois tables, liées par deux relations de type « un à
plusieurs ». Les pages web produites possèdent une mise en page commune,
et leur décoration utilise une feuille de style CSS. Le code python de
l'application et le code HTML « patron » sont bien séparés dans des
fichiers distincts.

Nous avons donc intégré dans cet exemple un maximum de concepts utiles,
mais délibérément laissé de côté tout le code de contrôle qui serait
indispensable dans une véritable application pour vérifier les entrées
de l'utilisateur, détecter les erreurs de communication avec la base de
données, etc., afin de ne pas encombrer la démonstration.



![](images/100000000000027A000001F91CF61590.png)



-   *Le traitement des données* est assuré par le script Python que nous
    décrivons ci-après. Il est entièrement inclus dans un seul fichier
    (*spectacles.py*), mais nous vous le présenterons en plusieurs
    morceaux afin de faciliter les explications et d'aérer quelque peu
    le texte.\
     Ce script fait appel au mécanisme des sessions pour garder en
    mémoire les coordonnées de l'utilisateur pendant tout le temps que
    dure sa visite du site.
-   *La présentation des données* est assurée par un ensemble de pages
    web, dont le code HTML est rassemblé pour sa plus grande partie dans
    un fichier texte distinct (*spectacles.htm*). Par programme, on
    extraira de ce fichier des chaînes de caractères qui seront
    formatées par insertion de valeurs issues de variables, suivant la
    technique décrite au chapitre 10. Ainsi le contenu statique des
    pages n'encombrera pas le script lui-même. Nous reproduisons le
    contenu de ce fichier à la page .
-   ![](images/100000000000027A000002A77EC42057.png)

### 19-B-1 - Le script {#article.xml#Ld0e84868 .TitreSection2}

Le script **spectacles.py** commence par définir une classe **Glob()**
qui servira uniquement de conteneur pour des variables que nous voulons
traiter comme globales. On y trouve notamment la description des tables
de la base de données dans un dictionnaire, suivant une technique
similaire à celle que nous avons expliquée au chapitre précédent :



1.  ``` {.LignePreCode}
    import os, cherrypy, sqlite3 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    class Glob(object): 
    ```

4.  ``` {.LignePreCode}
      "Données à caractère global pour l'application" 
    ```

5.  ``` {.LignePreCode}
      patronsHTML ="spectacles.htm"    # Fichier contenant les "patrons" HTML 
    ```

6.  ``` {.LignePreCode}
      html ={}	  # Les patrons seront chargés dans ce dictionnaire 
    ```

7.  ``` {.LignePreCode}
      # Structure de la base de données.  Dictionnaire des tables & champs : 
    ```

8.  ``` {.LignePreCode}
      dbName = "spectacles.sq3"	   # nom de la base de données 
    ```

9.  ``` {.LignePreCode}
      tables ={"spectacles":(("ref_spt","k"), ("titre","s"), ("date","t"), 
    ```

10. ``` {.LignePreCode}
    	     ("prix_pl","r"), ("vendues","i")), 
    ```

11. ``` {.LignePreCode}
           "reservations":(("ref_res","k"), ("ref_spt","i"), ("ref_cli","i"), 
    ```

12. ``` {.LignePreCode}
    	       ("place","i")), 
    ```

13. ``` {.LignePreCode}
           "clients":(("ref_cli","k"), ("nom","s"), ("e_mail","s"), 
    ```

14. ``` {.LignePreCode}
    	      ("tel", "i")) } 
    ```



Viennent ensuite les définitions de deux fonctions. La première (lignes
16 à 32) ne sera utilisée qu'une seule fois au démarrage. Son rôle
consiste à lire l'intégralité du fichier texte **spectacles.htm** afin
d'en extraire les « patrons » HTML qui seront utilisés pour formater les
pages web. Si vous examinez la structure de ce fichier (nous avons
reproduit son contenu à la page ), vous constaterez qu'il contient une
série de sections, clairement délimitées chacune par deux repères : une
balise d'ouverture (elle-même formée d'un libellé inclus entre deux
astérisques et des crochets), et une ligne terminale constituée d'au
moins 5 caractères \#. Chaque section peut donc ainsi être extraite
séparément, et mémorisée dans un dictionnaire global (**glob.html**).
Les clés de ce dictionnaire seront les libellés trouvés, et les valeurs
les sections correspondantes, chacune d'elles contenant donc une « page
» de code HTML, avec des balises de conversion `{}` qui pourront être remplacées par les
valeurs de variables.



15. ``` {.LignePreCode}
     
    ```

16. ``` {.LignePreCode}
    def chargerPatronsHTML(): 
    ```

17. ``` {.LignePreCode}
      # Chargement de tous les "patrons" de pages HTML dans un dictionnaire : 
    ```

18. ``` {.LignePreCode}
      fi =open(Glob.patronsHTML,"r") 
    ```

19. ``` {.LignePreCode}
      try:	       # pour s'assurer que le fichier sera toujours refermé 
    ```

20. ``` {.LignePreCode}
          for ligne in fi: 
    ```

21. ``` {.LignePreCode}
          if ligne[:2] =="[*":	    # étiquette trouvée ==> 
    ```

22. ``` {.LignePreCode}
    	  label =ligne[2:]	    # suppression [* 
    ```

23. ``` {.LignePreCode}
    	  label =label[:-1].strip()	 # suppression LF et esp évent. 
    ```

24. ``` {.LignePreCode}
    	  label =label[:-2]	    # suppression *] 
    ```

25. ``` {.LignePreCode}
    	  txt ="" 
    ```

26. ``` {.LignePreCode}
          else: 
    ```

27. ``` {.LignePreCode}
    	  if ligne[:5] =="#####": 
    ```

28. ``` {.LignePreCode}
    	  Glob.html[label] =txt 
    ```

29. ``` {.LignePreCode}
    	  else: 
    ```

30. ``` {.LignePreCode}
    	  txt += ligne 
    ```

31. ``` {.LignePreCode}
      finally: 
    ```

32. ``` {.LignePreCode}
          fi.close()       # fichier refermé dans tous les cas 
    ```



La seconde fonction, quoique toute simple, effectue un travail
remarquable : c'est elle en effet qui va nous permettre de donner à
toutes nos pages un aspect similaire, en les insérant dans un patron
commun. Ce patron, comme tous les autres, provient à l'origine du
fichier *spectacles.htm*, mais la fonction précédente l'aura déjà mis à
notre disposition dans le dictionnaire **Glob.html**, sous le libellé
"miseEnPage" :



34. ``` {.LignePreCode}
    def mep(page): 
    ```

35. ``` {.LignePreCode}
      # Fonction de "mise en page" du code HTML généré : renvoie la  
    ```

36. ``` {.LignePreCode}
      # transmise, agrémentée d'un en-tête et d'un bas de page adéquats. 
    ```

37. ``` {.LignePreCode}
      return Glob.html["miseEnPage"].format(page) 
    ```



Vient ensuite la définition d'une classe d'objets-interfaces pour
l'accès à la base de données. Cette classe est certainement très
perfectible[^note_102].
Vous y retrouverez l'application de quelques principes décrits au
chapitre précédent. Si vous effacez le fichier *spectacles.sq3* qui
contient la base de données, celle-ci sera recréée automatiquement par
la méthode **creaTables()** :



39. ``` {.LignePreCode}
    class GestionBD(object): 
    ```

40. ``` {.LignePreCode}
      "Mise en place et interfaçage d'une base de données SQLite" 
    ```

41. ``` {.LignePreCode}
      
    ```

42. ``` {.LignePreCode}
      def __init__(self, dbName): 
    ```

43. ``` {.LignePreCode}
          "Établissement de la connexion - Création du curseur" 
    ```

44. ``` {.LignePreCode}
          self.dbName =dbName 
    ```

45. ``` {.LignePreCode}
      
    ```

46. ``` {.LignePreCode}
      def executerReq(self, req, param =()): 
    ```

47. ``` {.LignePreCode}
          "Exécution de la requête , avec détection d'erreur éventuelle" 
    ```

48. ``` {.LignePreCode}
          connex =sqlite3.connect(self.dbName) 
    ```

49. ``` {.LignePreCode}
          cursor =connex.cursor() 
    ```

50. ``` {.LignePreCode}
          try: 
    ```

51. ``` {.LignePreCode}
          cursor.execute(req, param) 
    ```

52. ``` {.LignePreCode}
          except Exception as err: 
    ```

53. ``` {.LignePreCode}
          # renvoyer la requête et le message d'erreur système : 
    ```

54. ``` {.LignePreCode}
          msg ="Requête SQL incorrecte :\n{}\nErreur détectée :".format(req) 
    ```

55. ``` {.LignePreCode}
          return msg +str(err) 
    ```

56. ``` {.LignePreCode}
          if "SELECT" in req.upper(): 
    ```

57. ``` {.LignePreCode}
          return cursor.fetchall()	 # renvoyer une liste de tuples 
    ```

58. ``` {.LignePreCode}
          else: 
    ```

59. ``` {.LignePreCode}
          connex.commit()	      # On enregistre systématiquement 
    ```

60. ``` {.LignePreCode}
          cursor.close() 
    ```

61. ``` {.LignePreCode}
          connex.close() 
    ```

62. ``` {.LignePreCode}
      
    ```

63. ``` {.LignePreCode}
      def creaTables(self, dicTables): 
    ```

64. ``` {.LignePreCode}
          "Création des tables de la base de données si elles n'existent pas déjà" 
    ```

65. ``` {.LignePreCode}
          for table in dicTables:	      # parcours des clés du dictionnaire 
    ```

66. ``` {.LignePreCode}
          req = "CREATE TABLE {} (".format(table) 
    ```

67. ``` {.LignePreCode}
          pk ="" 
    ```

68. ``` {.LignePreCode}
          for descr in dicTables[table]: 
    ```

69. ``` {.LignePreCode}
    	  nomChamp = descr[0]	  # libellé du champ à créer 
    ```

70. ``` {.LignePreCode}
    	  tch = descr[1]	 # type de champ à créer 
    ```

71. ``` {.LignePreCode}
    	  if tch =="i": 
    ```

72. ``` {.LignePreCode}
    	  typeChamp ="INTEGER" 
    ```

73. ``` {.LignePreCode}
    	  elif tch =="k": 
    ```

74. ``` {.LignePreCode}
    	  # champ 'clé primaire' (entier incrémenté automatiquement) 
    ```

75. ``` {.LignePreCode}
    	  typeChamp ="INTEGER PRIMARY KEY AUTOINCREMENT" 
    ```

76. ``` {.LignePreCode}
    	  pk = nomChamp 
    ```

77. ``` {.LignePreCode}
    	  elif tch =="r": 
    ```

78. ``` {.LignePreCode}
    	  typeChamp ="REAL" 
    ```

79. ``` {.LignePreCode}
    	  else: 	    # pour simplifier, nous considérons 
    ```

80. ``` {.LignePreCode}
    	  typeChamp ="TEXT"	# comme textes tous les autres types 
    ```

81. ``` {.LignePreCode}
    	  req += "{} {}, ".format(nomChamp, typeChamp) 
    ```

82. ``` {.LignePreCode}
          req = req[:-2] + ")" 
    ```

83. ``` {.LignePreCode}
          try: 
    ```

84. ``` {.LignePreCode}
    	  self.executerReq(req) 
    ```

85. ``` {.LignePreCode}
          except: 
    ```

86. ``` {.LignePreCode}
    	  pass		   # La table existe probablement déjà 
    ```



Le script se poursuit avec la définition de la classe qui assure la
fonctionnalité du site web. Comme nous l'avons expliqué dans les pages
précédentes, *Cherrypy* convertit chacune des *url* demandées par le
navigateur web en un appel de méthode de cette classe.



88. ``` {.LignePreCode}
    class WebSpectacles(object): 
    ```

89. ``` {.LignePreCode}
      "Classe générant les objets gestionnaires de requêtes HTTP" 
    ```

90. ``` {.LignePreCode}
      
    ```

91. ``` {.LignePreCode}
      def index(self): 
    ```

92. ``` {.LignePreCode}
          # Page d'entrée du site web - renvoi d'une page HTML statique : 
    ```

93. ``` {.LignePreCode}
          return mep(Glob.html["pageAccueil"]) 
    ```

94. ``` {.LignePreCode}
      index.exposed =True 
    ```



La page d'entrée du site est une page statique, dont le texte a donc été
chargé dans le dictionnaire **Glob.html** (sous le libellé `"pageAccueil"`) pendant la phase
d'initialisation du programme. La méthode **index()** doit donc
simplement renvoyer ce texte, préalablement « habillé » à l'aide de la
fonction **mep()** pour lui donner l'aspect commun à toutes les pages.

La méthode suivante est un peu plus complexe. Pour bien comprendre son
fonctionnement, il est préférable d'examiner d'abord le contenu la page
web qui aura été renvoyée à l'utilisateur par la méthode **index()**
(cf. ligne 93). Cette page contient un *formulaire HTML*, que nous
reproduisons ci-après. Un tel formulaire est délimité par les balises
`` et `` :



```python
<form action="/identification" method=GET> 
<h4>Veuillez SVP entrer vos coordonnées dans les champs ci-après :</h4> 
<table> 
<tr><td>Votre nom :</td><td><input name="nom"></td></tr> 
<tr><td>Votre adresse courriel :</td><td><input name="mail"></td></tr> 
<tr><td>Votre numéro de téléphone :</td><td><input name="tel"></td></tr> 
</table> 
<input type=submit class="button" name="acces" value="Accès client"> 
<input type=submit class="button" name="acces" value="Accès administrateur"> 
</form> 
```



L'attribut `action` utilisé dans
la balise `` indique
indique *l'url* qui sera invoquée lorsque le visiteur du site aura
cliqué sur l'un des boutons de type `submit`. Cette *url* sera convertie par
*Cherrypy* en un appel de la méthode de même nom, à la racine du site
puisque le nom est précédé d'un simple /. C'est donc la méthode
**identification()** de notre classe principale qui sera appelée. Les
balises de type **\** définissent les champs d'entrée, chacun avec son
libellé spécifique signalé par l'attribut `name`. Ce sont ces libellés qui
permettront à *Cherrypy* de transmettre les valeurs encodées dans ces
champs, aux paramètres de mêmes noms de la méthode **identification()**.
Examinons à présent celle-ci :



95. ``` {.LignePreCode}
     
    ```

96. ``` {.LignePreCode}
      def identification(self, acces="", nom="", mail="", tel=""): 
    ```

97. ``` {.LignePreCode}
          # On mémorise les coord. de l'utilisat. dans des variables de session : 
    ```

98. ``` {.LignePreCode}
          cherrypy.session["nom"] =nom 
    ```

99. ``` {.LignePreCode}
          cherrypy.session["mail"] =mail 
    ```

100. ``` {.LignePreCode}
          cherrypy.session["tel"] =tel 
    ```

101. ``` {.LignePreCode}
          if acces=="Accès administrateur": 
    ```

102. ``` {.LignePreCode}
          return mep(Glob.html["accesAdmin"])     # renvoi d'une page HTML 
    ```

103. ``` {.LignePreCode}
          else: 
    ```

104. ``` {.LignePreCode}
          # Une variable de session servira de "caddy" pour les réservations : 
    ```

105. ``` {.LignePreCode}
          cherrypy.session["caddy"] =[]	# (liste vide, au départ) 
    ```

106. ``` {.LignePreCode}
          # Renvoi d'une page HTML, formatée avec le nom de l'utilisateur : 
    ```

107. ``` {.LignePreCode}
          return mep(Glob.html["accesClients"].format(nom)) 
    ```

108. ``` {.LignePreCode}
      identification.exposed =True 
    ```



Les arguments reçus sont donc réceptionnés dans les variables locales
**acces**, **nom**, **mail** et **tel**. Si nous souhaitons que ces
valeurs restent mémorisées spécifiquement pour chaque utilisateur durant
sa visite de notre site, il nous suffit de les confier aux bons soins de
l'objet **cherrypy.session**, qui se présente à nous sous l'apparence
d'un simple dictionnaire (Lignes 98-100).

Ligne 101 : Le paramètre **acces** aura reçu la valeur correspondant au
bouton `submit` qui aura été
utilisé par le visiteur, à savoir la chaîne « Accès administrateurs » ou
« Accès client ». Cela nous permet donc d'aiguiller ce visiteur vers
d'autres pages.

Ligne 104 : Nous allons mémoriser les réservations envisagées par le
visiteur dans une liste de tuples, qu'il pourra remplir à sa guise. Par
analogie avec ce qui se pratique sur les sites de commerce électronique
en ligne, nous appellerons cette liste son « panier » ou « caddy ».
L'enregistrement de ces réservations dans la base de données aura lieu
plus tard, dans une étape distincte, et seulement lorsqu'il en exprimera
le souhait. Nous devrons donc conserver cette liste tout au long de la
visite, dans une *variable de session* libellée `"caddy"` (Nous appellerons désormais
*variables de session* les valeurs mémorisées dans l'objet
**cherrypy.session**).

La ligne 107 combine deux formatages successifs, le premier pour
fusionner le code HTML produit localement (le nom entré par
l'utilisateur) avec celui d'un patron extrait du dictionnaire
**glob.html**, et le second pour « envelopper » l'ensemble dans un autre
patron, commun à toutes les pages celui-là, par l'intermédiaire de la
fonction **mep()**.

La page web ainsi renvoyée est une simple page statique, qui fournit les
liens menant à d'autres pages. La suite du script contient les méthodes
correspondantes :



110. ``` {.LignePreCode}
         def reserver(self): 
    ```

111. ``` {.LignePreCode}
          # Retouver le nom utilisateur dans les variables de session : 
    ```

112. ``` {.LignePreCode}
          nom =cherrypy.session["nom"] 
    ```

113. ``` {.LignePreCode}
          # Retrouver la liste des spectacles proposés : 
    ```

114. ``` {.LignePreCode}
          req ="SELECT ref_spt, titre, date, prix_pl, vendues FROM spectacles" 
    ```

115. ``` {.LignePreCode}
          res =BD.executerReq(req)	      # On obtient une liste de tuples 
    ```

116. ``` {.LignePreCode}
          # Construire un tableau html pour lister les infos trouvées : 
    ```

117. ``` {.LignePreCode}
          tabl ='\n' 
    ```

118. ``` {.LignePreCode}
          ligneTableau ="" +"{}"*5 +"\n" 
    ```

119. ``` {.LignePreCode}
          # Ajouter une ligne en haut du tableau avec les en-têtes de colonnes : 
    ```

120. ``` {.LignePreCode}
          tabl += ligneTableau.\ 
    ```

121. ``` {.LignePreCode}
          format("Réf.", "Titre", "Date", "Prix des places", "Vendues") 
    ```

122. ``` {.LignePreCode}
          for ref, tit, dat, pri, ven in res: 
    ```

123. ``` {.LignePreCode}
          tabl +=ligneTableau.format(ref, tit, dat, pri, ven) 
    ```

124. ``` {.LignePreCode}
          tabl +="" 
    ```

125. ``` {.LignePreCode}
          # Renvoyer une page HTML (assemblage d'un "patron" et de valeurs) : 
    ```

126. ``` {.LignePreCode}
          return mep(Glob.html["reserver"].format(tabl, nom)) 
    ```

127. ``` {.LignePreCode}
      reserver.exposed =True 
    ```

128. ``` {.LignePreCode}
      
    ```

129. ``` {.LignePreCode}
      def reservations(self, tel="", spect="", places=""): 
    ```

130. ``` {.LignePreCode}
          # Mémoriser les réservations demandées, dans une variable de session : 
    ```

131. ``` {.LignePreCode}
          spect, places = int(spect), int(places)	      # conversion en nombres 
    ```

132. ``` {.LignePreCode}
          caddy =cherrypy.session["caddy"]	  # récupération état actuel 
    ```

133. ``` {.LignePreCode}
          caddy.append((spect, places))	 # ajout d'un tuple à la liste 
    ```

134. ``` {.LignePreCode}
          cherrypy.session["caddy"] =caddy	  # mémorisation de la liste 
    ```

135. ``` {.LignePreCode}
          nSp, nPl = len(caddy), 0 
    ```

136. ``` {.LignePreCode}
          for c in caddy:		   # totaliser les réservations 
    ```

137. ``` {.LignePreCode}
          nPl += c[1] 
    ```

138. ``` {.LignePreCode}
          return mep(Glob.html["reservations"].format(nPl, nSp)) 
    ```

139. ``` {.LignePreCode}
      reservations.exposed =True 
    ```



Lignes 110-127 : Cette méthode fait appel à la base de données pour
pouvoir afficher la liste des spectacles déjà encodés. Examinez
particulièrement les lignes 116 à 124, qui vous montrent comment vous
pouvez très efficacement construire par programme tout le code HTML
décrivant un tableau, en vous servant des techniques de création et de
formatage des chaînes de caractères que nous avons vues au chapitre 10.
À la ligne 126, on se sert à nouveau de la même technique pour fusionner
le code produit localement avec un patron HTML.

Lignes 129-139 : La page web produite ainsi est à nouveau un formulaire.
L'examen de son code HTML (voir page ) nous indique que c'est cette fois
la méthode **reservations()** qui sera invoquée lorsque l'utilisateur
actionnera le bouton « Enregistrer ». Cette méthode réceptionne les
valeurs entrées dans le formulaire et les rassemble dans un tuple, puis
ajoute celui-ci à la liste contenue dans la variable de session `"caddy"`. Elle renvoie ensuite à
l'utilisateur une petite page qui l'informe sur l'évolution de ses
demandes.

Ligne 131 : Tous les arguments transmis par un formulaire HTML sont des
chaînes de caractères. Si ces arguments représentent des valeurs
numériques, il faut donc les convertir dans le type adéquat avant de les
utiliser comme telles.



![](images/100000000000027A000001D2570FABE6.png)



Le reste du script est reproduit ci-après. Vous y trouverez les méthodes
qui permettent à l'utilisateur « client » de clôturer sa visite du site
en demandant l'enregistrement de ses réservations, ou de revoir des
réservations qu'il aurait effectuées précédemment. Les méthodes
concernant les fonctions réservées aux « administrateurs » viennent
ensuite. Elles sont construites sur les mêmes principes et ne
nécessitent guère de commentaires.

Les requêtes SQL figurant dans les lignes suivantes devraient être assez
explicites. Leur description détaillée sort du cadre de cet ouvrage, et
nous ne nous y attarderons donc pas. Si elles vous paraissent quelque
peu complexes, ne vous découragez pas : l'apprentissage de ce langage
peut être très progressif. Sachez cependant qu'il s'agit d'un passage
obligé si vous souhaitez acquérir une vraie compétence de développeur.



141. ``` {.LignePreCode}
         def finaliser(self): 
    ```

142. ``` {.LignePreCode}
          # Finaliser l'enregistrement du caddy. 
    ```

143. ``` {.LignePreCode}
          nom =cherrypy.session["nom"] 
    ```

144. ``` {.LignePreCode}
          mail =cherrypy.session["mail"] 
    ```

145. ``` {.LignePreCode}
          tel =cherrypy.session["tel"] 
    ```

146. ``` {.LignePreCode}
          caddy =cherrypy.session["caddy"] 
    ```

147. ``` {.LignePreCode}
          # Enregistrer les références du client dans la table ad hoc : 
    ```

148. ``` {.LignePreCode}
          req ="INSERT INTO clients(nom, e_mail, tel) VALUES(?,?,?)" 
    ```

149. ``` {.LignePreCode}
          res =BD.executerReq(req, (nom, mail, tel)) 
    ```

150. ``` {.LignePreCode}
          # Récupérer la réf. qui lui a été attribuée automatiquement : 
    ```

151. ``` {.LignePreCode}
          req ="SELECT ref_cli FROM clients WHERE nom=?" 
    ```

152. ``` {.LignePreCode}
          res =BD.executerReq(req, (nom,)) 
    ```

153. ``` {.LignePreCode}
          client =res[0][0]      # extraire le 1er élément du 1er tuple 
    ```

154. ``` {.LignePreCode}
          # Parcours du caddy - enregistrement des places pour chaque spectacle : 
    ```

155. ``` {.LignePreCode}
          for (spect, places) in caddy: 
    ```

156. ``` {.LignePreCode}
          # Rechercher le dernier N° de place déjà réservée pour ce spect. : 
    ```

157. ``` {.LignePreCode}
          req ="SELECT MAX(place) FROM reservations WHERE ref_spt =?" 
    ```

158. ``` {.LignePreCode}
          res =BD.executerReq(req, (int(spect),)) 
    ```

159. ``` {.LignePreCode}
          numP =res[0][0] 
    ```

160. ``` {.LignePreCode}
          if numP is None: 
    ```

161. ``` {.LignePreCode}
    	  numP =0 
    ```

162. ``` {.LignePreCode}
          # Générer les numéros de places suivants, les enregistrer : 
    ```

163. ``` {.LignePreCode}
          req ="INSERT INTO reservations(ref_spt,ref_cli,place) VALUES(?,?,?)" 
    ```

164. ``` {.LignePreCode}
          for i in range(places): 
    ```

165. ``` {.LignePreCode}
    	  numP +=1 
    ```

166. ``` {.LignePreCode}
    	  res =BD.executerReq(req, (spect, client, numP)) 
    ```

167. ``` {.LignePreCode}
          # Enregistrer le nombre de places vendues pour ce spectacle : 
    ```

168. ``` {.LignePreCode}
          req ="UPDATE spectacles SET vendues=? WHERE ref_spt=?" 
    ```

169. ``` {.LignePreCode}
          res =BD.executerReq(req, (numP, spect)) 
    ```

170. ``` {.LignePreCode}
          cherrypy.session["caddy"] =[]	# vider le caddy 
    ```

171. ``` {.LignePreCode}
          return self.accesClients()     # Retour à la page d'accueil 
    ```

172. ``` {.LignePreCode}
      finaliser.exposed =True 
    ```

173. ``` {.LignePreCode}
      
    ```

174. ``` {.LignePreCode}
      def revoir(self): 
    ```

175. ``` {.LignePreCode}
          # Retrouver les infos concernant un client particulier. 
    ```

176. ``` {.LignePreCode}
          # On retrouvera sa référence à l'aide de son adresse courriel : 
    ```

177. ``` {.LignePreCode}
          mail =cherrypy.session["mail"] 
    ```

178. ``` {.LignePreCode}
          req ="SELECT ref_cli, nom, tel FROM clients WHERE e_mail =?" 
    ```

179. ``` {.LignePreCode}
          res =BD.executerReq(req, (mail,)) 
    ```

180. ``` {.LignePreCode}
          client, nom, tel =res[0] 
    ```

181. ``` {.LignePreCode}
          # Spectacles pour lesquels il a acheté des places : 
    ```

182. ``` {.LignePreCode}
          req ="SELECT titre, date, place, prix_pl "\ 
    ```

183. ``` {.LignePreCode}
           "FROM reservations JOIN spectacles USING (ref_spt) "\ 
    ```

184. ``` {.LignePreCode}
           "WHERE ref_cli =? ORDER BY titre, place" 
    ```

185. ``` {.LignePreCode}
          res =BD.executerReq(req, (client,)) 
    ```

186. ``` {.LignePreCode}
          # Construction d'un tableau html pour lister les infos trouvées : 
    ```

187. ``` {.LignePreCode}
          tabl ='\n' 
    ```

188. ``` {.LignePreCode}
          ligneTableau ="" +"{}"*4 +"\n" 
    ```

189. ``` {.LignePreCode}
          # Ajouter une ligne en haut du tableau avec les en-têtes de colonnes : 
    ```

190. ``` {.LignePreCode}
          tabl += ligneTableau.format("Titre", "Date", "N° place", "Prix") 
    ```

191. ``` {.LignePreCode}
          tot =0		     # compteur pour prix total 
    ```

192. ``` {.LignePreCode}
          for titre, date, place, prix in res: 
    ```

193. ``` {.LignePreCode}
          tabl += ligneTableau.format(titre, date, place, prix) 
    ```

194. ``` {.LignePreCode}
          tot += prix 
    ```

195. ``` {.LignePreCode}
          # Ajouter une ligne en bas du tableau avec le total en bonne place : 
    ```

196. ``` {.LignePreCode}
          tabl += ligneTableau.format("", "", "Total", str(tot)) 
    ```

197. ``` {.LignePreCode}
          tabl += "" 
    ```

198. ``` {.LignePreCode}
          return mep(Glob.html["revoir"].format(nom, mail, tel, tabl)) 
    ```

199. ``` {.LignePreCode}
      revoir.exposed =True 
    ```

200. ``` {.LignePreCode}
      
    ```

201. ``` {.LignePreCode}
      def accesClients(self): 
    ```

202. ``` {.LignePreCode}
          nom =cherrypy.session["nom"] 
    ```

203. ``` {.LignePreCode}
          return mep(Glob.html["accesClients"].format(nom)) 
    ```

204. ``` {.LignePreCode}
      accesClients.exposed =True 
    ```

205. ``` {.LignePreCode}
      
    ```

206. ``` {.LignePreCode}
      def entrerSpectacles(self): 
    ```

207. ``` {.LignePreCode}
          return mep(Glob.html["entrerSpectacles"]) 
    ```

208. ``` {.LignePreCode}
      entrerSpectacles.exposed =True 
    ```

209. ``` {.LignePreCode}
      
    ```

210. ``` {.LignePreCode}
      def memoSpectacles(self, titre ="", date ="", prixPl =""): 
    ```

211. ``` {.LignePreCode}
          # Mémoriser un nouveau spectacle 
    ```

212. ``` {.LignePreCode}
          if not titre or not date or not prixPl: 
    ```

213. ``` {.LignePreCode}
          return '<h4>Complétez les champs ! [Retour]</h4>' 
    ```

214. ``` {.LignePreCode}
          req ="INSERT INTO spectacles (titre, date, prix_pl, vendues) "\ 
    ```

215. ``` {.LignePreCode}
           "VALUES (?, ?, ?, ?)" 
    ```

216. ``` {.LignePreCode}
          msg =BD.executerReq(req, (titre, date, float(prixPl), 0)) 
    ```

217. ``` {.LignePreCode}
          return self.index()      # Retour à la page d'accueil 
    ```

218. ``` {.LignePreCode}
      memoSpectacles.exposed =True 
    ```

219. ``` {.LignePreCode}
      
    ```

220. ``` {.LignePreCode}
      def toutesReservations(self): 
    ```

221. ``` {.LignePreCode}
          # Lister les réservations effectuées par chaque client 
    ```

222. ``` {.LignePreCode}
          req ="SELECT titre, nom, e_mail, COUNT(place) FROM spectacles "\ 
    ```

223. ``` {.LignePreCode}
           "LEFT JOIN reservations USING(ref_spt) "\ 
    ```

224. ``` {.LignePreCode}
           "LEFT JOIN clients USING (ref_cli) "\ 
    ```

225. ``` {.LignePreCode}
           "GROUP BY nom, titre "\ 
    ```

226. ``` {.LignePreCode}
           "ORDER BY titre, nom" 
    ```

227. ``` {.LignePreCode}
          res =BD.executerReq(req) 
    ```

228. ``` {.LignePreCode}
          # Construction d'un tableau html pour lister les infos trouvées : 
    ```

229. ``` {.LignePreCode}
          tabl ='\n' 
    ```

230. ``` {.LignePreCode}
          ligneTableau ="" +"{}"*4 +"\n" 
    ```

231. ``` {.LignePreCode}
          # Ajouter une ligne en haut du tableau avec les en-têtes de colonnes : 
    ```

232. ``` {.LignePreCode}
          tabl += ligneTableau.\ 
    ```

233. ``` {.LignePreCode}
          format("Titre", "Nom du client", "Courriel", "Places réservées") 
    ```

234. ``` {.LignePreCode}
          for tit, nom, mail, pla in res: 
    ```

235. ``` {.LignePreCode}
          tabl += ligneTableau.format(tit, nom, mail, pla) 
    ```

236. ``` {.LignePreCode}
          tabl +="" 
    ```

237. ``` {.LignePreCode}
          return mep(Glob.html["toutesReservations"].format(tabl)) 
    ```

238. ``` {.LignePreCode}
      toutesReservations.exposed =True 
    ```

239. ``` {.LignePreCode}
      
    ```

240. ``` {.LignePreCode}
    # === PROGRAMME PRINCIPAL === 
    ```

241. ``` {.LignePreCode}
    # Ouverture de la base de données - création de celle-ci si elle n'existe pas : 
    ```

242. ``` {.LignePreCode}
    BD =GestionBD(Glob.dbName) 
    ```

243. ``` {.LignePreCode}
    BD.creaTables(Glob.tables) 
    ```

244. ``` {.LignePreCode}
    # Chargement des "patrons" de pages web dans un dictionnaire global : 
    ```

245. ``` {.LignePreCode}
    chargerPatronsHTML() 
    ```

246. ``` {.LignePreCode}
    # Reconfiguration et démarrage du serveur web : 
    ```

247. ``` {.LignePreCode}
    cherrypy.config.update({"tools.staticdir.root":os.getcwd()}) 
    ```

248. ``` {.LignePreCode}
    cherrypy.quickstart(WebSpectacles(), config ="tutoriel.conf") 
    ```



### 19-B-2 - Les « patrons » HTML {#article.xml#Ld0e91508 .TitreSection2}

Les « patrons » HTML utilisés par le script (en tant que chaînes de
caractères à formater) sont tous contenus dans un seul fichier texte,
que nous reproduisons intégralement ci-après :



1.  ``` {.LignePreCode}
    [*miseEnPage*]  
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
      
    ```

4.  ``` {.LignePreCode}
      
    ```

5.  ``` {.LignePreCode}
      
    ```

6.  ``` {.LignePreCode}
      
    ```

7.  ``` {.LignePreCode}
      
    ```

8.  ``` {.LignePreCode}
    <h1>Grand Théâtre de Python City</h1>  
    ```

9.  ``` {.LignePreCode}
    {}  
    ```

10. ``` {.LignePreCode}
    <h3>[Retour à la page d'accueil]</h3>  
    ```

11. ``` {.LignePreCode}
      
    ```

12. ``` {.LignePreCode}
      
    ```

13. ``` {.LignePreCode}
    ##########  
    ```

14. ``` {.LignePreCode}
    [*pageAccueil*]  
    ```

15. ``` {.LignePreCode}
      
    ```

16. ``` {.LignePreCode}
    <h4>Veuillez SVP entrer vos coordonnées dans les champs ci-après :</h4>  
    ```

17. ``` {.LignePreCode}
      
    ```

18. ``` {.LignePreCode}
    Votre nom :  
    ```

19. ``` {.LignePreCode}
    Votre adresse courriel :  
    ```

20. ``` {.LignePreCode}
    Votre numéro de téléphone :  
    ```

21. ``` {.LignePreCode}
      
    ```

22. ``` {.LignePreCode}
      
    ```

23. ``` {.LignePreCode}
      
    ```

24. ``` {.LignePreCode}
      
    ```

25. ``` {.LignePreCode}
    ##########  
    ```

26. ``` {.LignePreCode}
    [*accesAdmin*]  
    ```

27. ``` {.LignePreCode}
    <h3>  
    ```

28. ``` {.LignePreCode}
    Ajouter de nouveaux spectacles<Li>  
    ```

29. ``` {.LignePreCode}
    Lister les réservations  
    ```

30. ``` {.LignePreCode}
    </h3>  
    ```

31. ``` {.LignePreCode}
    ##########  
    ```

32. ``` {.LignePreCode}
    [*accesClients*]  
    ```

33. ``` {.LignePreCode}
    <h3>Bonjour, Monsieur {}.</h3>  
    ```

34. ``` {.LignePreCode}
    <h4>Veuillez choisir l'action souhaitée :  
    ```

35. ``` {.LignePreCode}
    Réserver des places pour un spectacle  
    ```

36. ``` {.LignePreCode}
    Finaliser l'enregistrement des réservations  
    ```

37. ``` {.LignePreCode}
    Revoir toutes les réservations effectuées  
    ```

38. ``` {.LignePreCode}
    </h4>  
    ```

39. ``` {.LignePreCode}
    ##########  
    ```

40. ``` {.LignePreCode}
    [*reserver*]  
    ```

41. ``` {.LignePreCode}
    <h3>Les spectacles actuellement programmés sont les suivants : </h3>  
    ```

42. ``` {.LignePreCode}
    {}  
    ```

43. ``` {.LignePreCode}
    Les réservations seront faites au nom de : {}.  
    ```

44. ``` {.LignePreCode}
      
    ```

45. ``` {.LignePreCode}
      
    ```

46. ``` {.LignePreCode}
    La réf. du spectacle choisi :  
    ```

47. ``` {.LignePreCode}
    Le nombre de places souhaitées :  
    ```

48. ``` {.LignePreCode}
      
    ```

49. ``` {.LignePreCode}
      
    ```

50. ``` {.LignePreCode}
      
    ```

51. ``` {.LignePreCode}
    ##########  
    ```

52. ``` {.LignePreCode}
    [*reservations*]  
    ```

53. ``` {.LignePreCode}
    <h3>Réservations mémorisées.</h3>  
    ```

54. ``` {.LignePreCode}
    <h4>Vous avez déjà réservé {} place(s) pour {} spectacle(s).</h4>  
    ```

55. ``` {.LignePreCode}
    <h3>Réserver encore d'autres places</h3>  
    ```

56. ``` {.LignePreCode}
    ##########  
    ```

57. ``` {.LignePreCode}
    [*entrerSpectacles*]  
    ```

58. ``` {.LignePreCode}
      
    ```

59. ``` {.LignePreCode}
      
    ```

60. ``` {.LignePreCode}
    Titre du spectacle :  
    ```

61. ``` {.LignePreCode}
    Date :  
    ```

62. ``` {.LignePreCode}
    Prix des places :  
    ```

63. ``` {.LignePreCode}
      
    ```

64. ``` {.LignePreCode}
      
    ```

65. ``` {.LignePreCode}
      
    ```

66. ``` {.LignePreCode}
    ##########  
    ```

67. ``` {.LignePreCode}
    [*toutesReservations*]  
    ```

68. ``` {.LignePreCode}
    <h4>Les réservations ci-après ont déjà été effectuées :</h4>  
    ```

69. ``` {.LignePreCode}
    {}  
    ```

70. ``` {.LignePreCode}
    ##########  
    ```

71. ``` {.LignePreCode}
    [*revoir*]  
    ```

72. ``` {.LignePreCode}
    <h4>Réservations effectuées par :</h4>  
    ```

73. ``` {.LignePreCode}
    <h3>{}</h3><h4>Adresse courriel : {} - Tél : {}</h4>  
    ```

74. ``` {.LignePreCode}
    {}  
    ```

75. ``` {.LignePreCode}
    ##########  
    ```



Avec cet exemple un peu élaboré, nous espérons que vous aurez bien
compris l'intérêt de séparer le code Python et le code HTML dans des
fichiers distincts, comme nous l'avons fait, afin que l'ensemble de
votre production conserve une lisibilité maximale. Une application web
est en effet souvent destinée à grandir et à devenir de plus en plus
complexe au fil du temps. Vous devez donc mettre toutes les chances de
votre côté pour qu'elle reste toujours bien structurée et facilement
compréhensible. En utilisant des techniques modernes comme la
programmation par objets, vous êtes certainement sur la bonne voie pour
progresser rapidement et acquérir une maîtrise très productive.



![](images/1000000000000272000002DC84922D7E.png)



Exercices

*Le script précédent peut vous servir de banc d'essai pour exercer vos
compétences dans un grand nombre de domaines.*

.Comme expliqué précédemment, on peut structurer un site web en le
fractionnant en plusieurs classes. Il serait judicieux de séparer les
méthodes concernant les « clients » et les « administrateurs » de ce
site dans des classes différentes.

.Le script tel qu'il est ne fonctionne à peu près correctement que si
l'utilisateur remplit correctement tous les champs qui lui sont
proposés. Il serait donc fort utile de lui ajouter une série
d'instructions de contrôle des valeurs encodées, avec renvoi de messages
d'erreur à l'utilisateur lorsque c'est nécessaire.

.L'accès « administrateurs » permet seulement d'ajouter de nouveaux
spectacles, mais non de modifier ou de supprimer ceux qui sont déjà
encodés. Ajoutez donc des méthodes pour implémenter ces fonctions.

.L'accès administrateur est libre. Il serait judicieux d'ajouter au
script un mécanisme d'authentification par mot de passe, afin que cet
accès soit réservé aux seules personnes possédant le sésame.

.L'utilisateur « client » qui se connecte plusieurs fois de suite, est à
chaque fois mémorisé comme un nouveau client, alors qu'il devrait
pouvoir ajouter d'autres réservations à son compte existant,
éventuellement modifier ses données personnelles, etc. Toutes ces
fonctionnalités pourraient être ajoutées.

.Vous aurez probablement remarqué que les ***tableaux*** HTML générés
dans le script sont produits à partir d'algorithmes très semblables. Il
serait donc intéressant d'écrire une fonction généraliste capable de
produire un tel tableau, dont on recevrait la description dans un
dictionnaire ou une liste.

.La décoration des pages web générées par le script est définie dans une
feuille de style annexe (le fichier *spectacles.css*). Libre à vous
d'examiner ce qui se passe si vous enlevez le lien activant cette
feuille de style (5^e^ ligne du fichier *spectacles.htm*), ou si vous
modifiez son contenu, lequel décrit le style à appliquer à chaque
balise.


[^note_101]: Le dessin du serpent est le logo du logiciel libre ***WebCamSpy*** (ce logiciel est écrit en Python). Voir : *http://webcamspy.sourceforge.net/*

[^note_102]: Vous y verrez notamment que nous y recréons un nouvel objet connexion à chaque requête, ce qui n'est guère heureux mais résulte du fait que SQLite ne permet pas d'utiliser au sein d'un *thread* un objet connexion créé dans un autre *thread*. Il faudrait donc : soit faire en sorte que l'application n'utilise en tout et pour tout qu'un seul *thread*, soit qu'on lui ajoute la fonctionnalité nécessaire pour identifier les *threads* courants, soit utiliser un autre SGBDR que SQLite … Tout cela est réalisable, mais demanderait son lot d'explications et nous ferait sortir du cadre de cet ouvrage. Vous trouverez une introduction aux *threads* à la page .
