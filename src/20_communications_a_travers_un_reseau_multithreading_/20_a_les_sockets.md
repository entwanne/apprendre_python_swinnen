## 20-A - Les sockets

Le premier exercice qui va vous être proposé consistera à établir une
communication entre deux machines seulement. L'une et l'autre pourront
s'échanger des messages à tour de rôle, mais vous constaterez cependant
que leurs configurations ne sont pas symétriques. Le script installé sur
l'une de ces machines jouera en effet le rôle d'un logiciel *serveur*,
alors que l'autre se comportera comme un logiciel *client*.

Le logiciel serveur fonctionne en continu, sur une machine dont
l'identité est bien définie sur le réseau grâce à une *adresseIP*
spécifique[^note_103].
Il guette en permanence l'arrivée de requêtes expédiées par les clients
potentiels en direction de cette adresse, par l'intermédiaire d'un *port
de communication* bien déterminé. Pour ce faire, le script correspondant
doit mettre en œuvre un objet logiciel associé à ce port, que l'on
appelle un *socket*.

Depuis une autre machine, le logiciel client tente d'établir la
connexion en émettant une *requête* appropriée. Cette requête est un
message qui est confié au réseau, un peu comme on confie une lettre à la
Poste. Le réseau pourrait en effet acheminer la requête vers n'importe
quelle autre machine, mais une seule est visée : pour que la destination
visée puisse être atteinte, la requête contient dans son en-tête
l'indication de l'adresse IP et du port de communication destinataires.

Lorsque la connexion est établie avec le serveur, le client lui assigne
lui-même l'un de ses propres ports de communication. À partir de ce
moment, on peut considérer qu'*un canal privilégié relie les deux
machines*, comme si on les avait connectées l'une à l'autre par
l'intermédiaire d'un fil (les deux ports de communication respectifs
jouant le rôle des deux extrémités de ce fil). L'échange d'informations
proprement dit peut commencer.

Pour pouvoir utiliser les ports de communication réseau, les programmes
font appel à un ensemble de procédures et de fonctions du système
d'exploitation, par l'intermédiaire d'objets interfaces que l'on appelle
donc des *sockets*. Ceux-ci peuvent mettre en œuvre deux techniques de
communication différentes et complémentaires : celle des *paquets* (que
l'on appelle aussi des *datagrammes*), très largement utilisée sur
l'internet, et celle de la *connexioncontinue*, ou *streamsocket*, qui
est un peu plus simple.

### 20-A-1 - Construction d'un serveur rudimentaire {#article.xml#Ld0e93385 .TitreSection2}

Pour nos premières expériences, nous allons utiliser la technique des
*streamsockets*.\
 Celle-ci est en effet parfaitement appropriée lorsqu'il s'agit de faire
communiquer des ordinateurs interconnectés par l'intermédiaire d'un
réseau local. C'est une technique particulièrement aisée à mettre en
œuvre, et elle permet un débit élevé pour l'échange de données.

L'autre technologie (celle des *paquets*) serait préférable pour les
communications expédiées *via* l'Internet, en raison de sa plus grande
fiabilité (les mêmes paquets peuvent atteindre leur destination par
différents chemins, être émis ou ré-émis en plusieurs exemplaires si
cela se révèle nécessaire pour corriger les erreurs de transmission),
mais sa mise en œuvre est un peu plus complexe. Nous ne l'étudierons pas
dans ce livre.

Le premier script ci-dessous met en place un serveur capable de
communiquer avec un seul client. Nous verrons un peu plus loin ce qu'il
faut lui ajouter afin qu'il puisse prendre en charge en parallèle les
connexions de plusieurs clients.



1.  ``` {.LignePreCode}
    # Définition d'un serveur réseau rudimentaire 
    ```

2.  ``` {.LignePreCode}
    # Ce serveur attend la connexion d'un client 
    ```

3.  ``` {.LignePreCode}
      
    ```

4.  ``` {.LignePreCode}
    import socket, sys 
    ```

5.  ``` {.LignePreCode}
      
    ```

6.  ``` {.LignePreCode}
    HOST = '192.168.1.168' 
    ```

7.  ``` {.LignePreCode}
    PORT = 50000 
    ```

8.  ``` {.LignePreCode}
    counter =0	 # compteur de connexions actives 
    ```

9.  ``` {.LignePreCode}
      
    ```

10. ``` {.LignePreCode}
    # 1) création du socket : 
    ```

11. ``` {.LignePreCode}
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    ```

12. ``` {.LignePreCode}
      
    ```

13. ``` {.LignePreCode}
    # 2) liaison du socket à une adresse précise : 
    ```

14. ``` {.LignePreCode}
    try: 
    ```

15. ``` {.LignePreCode}
      mySocket.bind((HOST, PORT)) 
    ```

16. ``` {.LignePreCode}
    except socket.error: 
    ```

17. ``` {.LignePreCode}
      print("La liaison du socket à l'adresse choisie a échoué.") 
    ```

18. ``` {.LignePreCode}
      sys.exit 
    ```

19. ``` {.LignePreCode}
      
    ```

20. ``` {.LignePreCode}
    while 1: 
    ```

21. ``` {.LignePreCode}
      # 3) Attente de la requête de connexion d'un client : 
    ```

22. ``` {.LignePreCode}
      print("Serveur prêt, en attente de requêtes ...") 
    ```

23. ``` {.LignePreCode}
      mySocket.listen(2) 
    ```

24. ``` {.LignePreCode}
      
    ```

25. ``` {.LignePreCode}
      # 4) Etablissement de la connexion : 
    ```

26. ``` {.LignePreCode}
      connexion, adresse = mySocket.accept() 
    ```

27. ``` {.LignePreCode}
      counter +=1 
    ```

28. ``` {.LignePreCode}
      print("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1])) 
    ```

29. ``` {.LignePreCode}
      
    ```

30. ``` {.LignePreCode}
      # 5) Dialogue avec le client : 
    ```

31. ``` {.LignePreCode}
      msgServeur ="Vous êtes connecté au serveur Marcel. Envoyez vos messages." 
    ```

32. ``` {.LignePreCode}
      connexion.send(msgServeur.encode("Utf8")) 
    ```

33. ``` {.LignePreCode}
      msgClient = connexion.recv(1024).decode("Utf8") 
    ```

34. ``` {.LignePreCode}
      while 1: 
    ```

35. ``` {.LignePreCode}
          print("C>", msgClient) 
    ```

36. ``` {.LignePreCode}
          if msgClient.upper() == "FIN" or msgClient =="": 
    ```

37. ``` {.LignePreCode}
          break 
    ```

38. ``` {.LignePreCode}
          msgServeur = input("S> ") 
    ```

39. ``` {.LignePreCode}
          connexion.send(msgServeur.encode("Utf8")) 
    ```

40. ``` {.LignePreCode}
          msgClient = connexion.recv(1024).decode("Utf8") 
    ```

41. ``` {.LignePreCode}
      
    ```

42. ``` {.LignePreCode}
      # 6) Fermeture de la connexion : 
    ```

43. ``` {.LignePreCode}
      connexion.send("fin".encode("Utf8")) 
    ```

44. ``` {.LignePreCode}
      print("Connexion interrompue.") 
    ```

45. ``` {.LignePreCode}
      connexion.close() 
    ```

46. ``` {.LignePreCode}
      
    ```

47. ``` {.LignePreCode}
      ch = input("<R>ecommencer <T>erminer ? ") 
    ```

48. ``` {.LignePreCode}
      if ch.upper() =='T': 
    ```

49. ``` {.LignePreCode}
          break 
    ```



#### 20-A-1-A - Commentaires {#article.xml#Ld0e94307 .TitreSection3}

-   Ligne 4 : Le module **socket** contient toutes les fonctions et les
    classes nécessaires pour construire des programmes communicants.
    Comme nous allons le voir dans les lignes suivantes, l'établissement
    de la communication comporte six étapes.
-   Lignes 6-7 : Ces deux variables définissent l'identité du serveur,
    telle qu'on l'intégrera au socket. **HOST** doit contenir une chaîne
    de caractères indiquant l'adresse IP du serveur sous la forme
    décimale habituelle, ou encore le nom DNS de ce même serveur (mais à
    la condition qu'un mécanisme de résolution des noms ait été mis en
    place sur le réseau). **PORT** doit contenir un entier, à savoir le
    numéro d'un port qui ne soit pas déjà utilisé pour un autre usage,
    et de préférence une valeur supérieure à 1024.
-   Lignes 10-11 : Première étape du mécanisme d'interconnexion. On
    instancie un objet de la classe **socket()**, en précisant deux
    options qui indiquent le type d'adresses choisi (nous utiliserons
    des adresses de type « Internet ») ainsi que la technologie de
    transmission (datagrammes ou connexion continue (*stream*) : nous
    avons décidé d'utiliser cette dernière).
-   Lignes 13 à 18 : Seconde étape. On tente d'établir la liaison entre
    le socket et le port de communication. Si cette liaison ne peut être
    établie (port de communication occupé, par exemple, ou nom de
    machine incorrect), le programme se termine sur un message d'erreur.
    *Remarque concernant la ligne 15* : la méthode **bind()** du socket
    attend un argument du type tuple, raison pour laquelle nous devons
    enfermer nos deux variables dans une double paire de parenthèses.
-   Ligne 20 : Notre programme serveur étant destiné à fonctionner en
    permanence dans l'attente des requêtes de clients potentiels, nous
    le lançons dans une boucle sans fin.
-   Lignes 21 à 23 : Troisième étape. Le socket étant relié à un port de
    communication, il peut à présent se préparer à recevoir les requêtes
    envoyées par les clients. C'est le rôle de la méthode **listen()**.
    L'argument qu'on lui transmet indique le nombre maximum de
    connexions à accepter en parallèle. Nous verrons plus loin comment
    gérer celles-ci.
-   Lignes 25 à 28 : Quatrième étape. Lorsqu'on fait appel à sa méthode
    **accept()**, le socket attend indéfiniment qu'une requête se
    présente. Le script est donc interrompu à cet endroit, un peu comme
    il le serait si nous faisions appel à une fonction **input()** pour
    attendre une entrée clavier. Si une requête est réceptionnée, la
    méthode **accept()** renvoie un tuple de deux éléments : le premier
    est la référence d'un nouvel objet de la classe **socket()**[^note_104],
    qui sera la véritable interface de communication entre le client et
    le serveur, et le second un autre tuple contenant les coordonnées de
    ce client (son adresse IP et le n^o^ de port qu'il utilise
    lui-même).
-   Lignes 30 à 33 : Cinquième étape. La communication proprement dite
    est établie. Les méthodes **send()** et **recv()** du socket servent
    évidemment à l'émission et à la réception des messages, *qui doivent
    impérativement être des chaînes d'octets.* À l'émission, il faut
    donc prévoir explicitement la conversion des chaînes de caractères
    en données de type ***bytes***, et faire l'inverse à la réception.\
    *Remarques :* la méthode **send()** renvoie le nombre d'octets
    expédiés. L'appel de la méthode **recv**() doit comporter un
    argument entier indiquant le nombre maximum d'octets à réceptionner
    en une fois. Les octets surnuméraires sont mis en attente dans un
    tampon, ils sont transmis lorsque la même méthode **recv()** est
    appelée à nouveau.
-   Lignes 34 à 40 : Cette nouvelle boucle sans fin maintient le
    dialogue jusqu'à ce que le client décide d'envoyer le mot « fin » ou
    une simple chaîne vide. Les écrans des deux machines afficheront
    chacune l'évolution de ce dialogue.
-   Lignes 42 à 45 : Sixième étape. Fermeture de la connexion.

### 20-A-2 - Construction d'un client rudimentaire {#article.xml#Ld0e94397 .TitreSection2}

Le script ci-dessous définit un logiciel client complémentaire du
serveur décrit dans les pages précédentes. On notera sa grande
simplicité.



1.  ``` {.LignePreCode}
    # Définition d'un client réseau rudimentaire 
    ```

2.  ``` {.LignePreCode}
    # Ce client dialogue avec un serveur ad hoc 
    ```

3.  ``` {.LignePreCode}
      
    ```

4.  ``` {.LignePreCode}
    import socket, sys 
    ```

5.  ``` {.LignePreCode}
      
    ```

6.  ``` {.LignePreCode}
    HOST = '192.168.1.168' 
    ```

7.  ``` {.LignePreCode}
    PORT = 50000 
    ```

8.  ``` {.LignePreCode}
      
    ```

9.  ``` {.LignePreCode}
    # 1) création du socket : 
    ```

10. ``` {.LignePreCode}
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    ```

11. ``` {.LignePreCode}
      
    ```

12. ``` {.LignePreCode}
    # 2) envoi d'une requête de connexion au serveur : 
    ```

13. ``` {.LignePreCode}
    try: 
    ```

14. ``` {.LignePreCode}
      mySocket.connect((HOST, PORT)) 
    ```

15. ``` {.LignePreCode}
    except socket.error: 
    ```

16. ``` {.LignePreCode}
      print("La connexion a échoué.") 
    ```

17. ``` {.LignePreCode}
      sys.exit() 
    ```

18. ``` {.LignePreCode}
    print("Connexion établie avec le serveur.") 
    ```

19. ``` {.LignePreCode}
      
    ```

20. ``` {.LignePreCode}
    # 3) Dialogue avec le serveur : 
    ```

21. ``` {.LignePreCode}
    msgServeur = mySocket.recv(1024).decode("Utf8") 
    ```

22. ``` {.LignePreCode}
      
    ```

23. ``` {.LignePreCode}
    while 1: 
    ```

24. ``` {.LignePreCode}
      if msgServeur.upper() == "FIN" or msgServeur =="": 
    ```

25. ``` {.LignePreCode}
          break 
    ```

26. ``` {.LignePreCode}
      print("S>", msgServeur) 
    ```

27. ``` {.LignePreCode}
      msgClient = input("C> ") 
    ```

28. ``` {.LignePreCode}
      mySocket.send(msgClient.encode("Utf8")) 
    ```

29. ``` {.LignePreCode}
      msgServeur = mySocket.recv(1024).decode("Utf8") 
    ```

30. ``` {.LignePreCode}
      
    ```

31. ``` {.LignePreCode}
    # 4) Fermeture de la connexion : 
    ```

32. ``` {.LignePreCode}
    print("Connexion interrompue.") 
    ```

33. ``` {.LignePreCode}
    mySocket.close() 
    ```



#### 20-A-2-A - Commentaires {#article.xml#Ld0e94917 .TitreSection3}

-   Le début du script est similaire à celui du serveur. L'adresse IP et
    le port de communication doivent être ceux du serveur.
-   Lignes 12 à 18 : On ne crée cette fois qu'un seul objet socket, dont
    on utilise la méthode **connect()** pour envoyer la requête de
    connexion.
-   Lignes 20 à 33 : Une fois la connexion établie, on peut dialoguer
    avec le serveur en utilisant les méthodes **send()** et **recv()**
    déjà décrites plus haut pour celui-ci.


[^note_103]: Une machine particulière peut également être désignée par un nom plus explicite, mais à la condition qu'un mécanisme ait été mis en place sur le réseau (DNS) pour traduire automatiquement ce nom en adresse IP. Veuillez consulter un ouvrage sur les réseaux pour en savoir davantage.

[^note_104]: 
