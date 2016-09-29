## 11-F - Lecture séquentielle d'un fichier

Vous allez maintenant rouvrir le fichier,
mais cette fois en lecture, de manière à pouvoir y relire les
informations que vous avez enregistrées dans l'étape précédente :



```python
>>> ofi = open('Monfichier', 'r')
>>> t = ofi.read()
>>> print(t)
Bonjour, fichier !Quel beau temps, aujourd'hui !
>>> ofi.close()
```



Comme on pouvait s'y attendre, la méthode **read()** lit les données
présentes dans le fichier et les transfère dans une variable de type
chaîne de caractères (*string*) . Si on utilise cette méthode sans
argument, la totalité du fichier est transférée.

### 11-F-1 - Notes {#article.xml#Ld0e22359 .TitreSection2}

-   Le fichier que nous voulons lire s'appelle **Monfichier**.
    L'instruction d'ouverture de fichier devra donc nécessairement faire
    référence à ce nom là. Si le fichier n'existe pas, nous obtenons un
    message d'erreur. Exemple :\
    **\>\>\> ofi = open('Monficier','r')**\
    **IOError: [Errno 2] No such file or
    directory: 'Monficier'**
-   Par contre, nous ne sommes tenus à aucune obligation concernant le
    nom à choisir pour *l'objet-fichier*. C'est un nom de variable
    quelconque. Ainsi donc, dans notre première instruction, nous avons
    choisi de créer un objet-fichier **ofi**, faisant référence au
    fichier réel **Monfichier**, lequel est ouvert en lecture (argument
    **'r'**).
-   Les deux chaînes de caractères que nous avions entrées dans le
    fichier sont à présent accolées en une seule. C'est normal, puisque
    nous n'avons fourni aucun caractère de séparation lorsque nous les
    avons enregistrées. Nous verrons un peu plus loin comment
    enregistrer des lignes de texte distinctes.
-   La méthode **read()** peut également être utilisée avec un argument.
    Celui-ci indiquera combien de caractères doivent être lus, à partir
    de la position déjà atteinte dans le fichier :\
    **\>\>\> ofi = open('Monfichier',
    'r')**\
    `>>> t = ofi.read(7)`\
    `>>> print(t)`\
    `Bonjour`\
    `>>> t = ofi.read(15)`\
    `>>> print(t)`\
    `, fichier !Quel`\
    \
     S'il ne reste pas assez de caractères au fichier pour satisfaire la
    demande, la lecture s'arrête tout simplement à la fin du fichier :\
    `>>> t = ofi.read(1000)`\
    `>>> print(t)`\
    ** beau temps, aujourd'hui
    !**\
    \
     Si la fin du fichier est déjà atteinte, **read()** renvoie une
    chaîne vide :\
    `>>> t = ofi.read()`\
    `>>> print(t)`
-   N'oubliez pas de refermer le fichier après
    usage :\
    `>>> ofi.close()`

> Dans tout ce qui précède, nous avons
> admis sans explication que les chaînes de caractères étaient échangées
> telles quelles entre l'interpréteur Python et le fichier. En réalité,
> ceci est inexact, parce que les séquences de caractères doivent être
> converties en séquences d'octets pour pouvoir être mémorisées dans les
> fichiers, et il existe malheureusement différentes normes pour cela.
> En toute rigueur, il faudrait donc préciser à Python la norme
> d'encodage que vous souhaitez utiliser dans vos fichiers : nous
> verrons comment faire au chapitre suivant. En attendant, vous pouvez
> tabler sur le fait que Python utilise par défaut la norme en vigueur
> sur votre système d'exploitation, ce qui devrait vous éviter tout
> problème pour ces premiers exercices. Si vous obtenez tout de même un
> rendu bizarre de vos caractères accentués, veuillez l'ignorer
> provisoirement.

