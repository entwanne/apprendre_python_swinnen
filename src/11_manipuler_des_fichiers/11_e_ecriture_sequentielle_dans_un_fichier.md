## 11-E - Écriture séquentielle dans un fichier

Sous Python, l'accès aux fichiers est assuré par l'intermédiaire d'un objet-interface particulier, que
l'on appelle
*objet-fichier*. On crée cet objet à
l'aide de la fonction intégrée
**open()**[^note_53]. Celle-ci renvoie un objet doté de méthodes
spécifiques, qui vous permettront de lire et écrire dans le
fichier.

L'exemple ci-après vous montre comment ouvrir un
fichier en écriture, y enregistrer deux chaînes de caractères, puis le
refermer. Notez bien que si le fichier n'existe pas encore, il sera créé automatiquement.
Par contre, si le nom utilisé concerne un fichier préexistant qui
contient déjà des données, les caractères que vous y enregistrerez
viendront s'ajouter à la suite de
ceux qui s'y trouvent déjà. Vous
pouvez faire tout cet exercice directement à la ligne de commande
:



```python
>>> obFichier = open('Monfichier','a')
>>> obFichier.write('Bonjour, fichier !')
>>> obFichier.write("Quel beau temps, aujourd'hui !")
>>> obFichier.close()
>>>
```



### 11-E-1 - Notes {#article.xml#Ld0e22196 .TitreSection2}

-   La première ligne crée l'*objet-fichier***obFichier**, lequel fait
    référence à un fichier véritable (sur disque ou disquette) dont le
    nom sera **Monfichier**. Attention : *ne confondez pas le nom de
    fichier avec le nom de l'objet-fichier* qui y donne accès ! À la
    suite de cet exercice, vous pouvez vérifier qu'il s'est bien créé
    sur votre système (dans le répertoire courant) un fichier dont le
    nom est **Monfichier** (et dont vous pouvez visualiser le contenu à
    l'aide d'un éditeur quelconque).
-   La fonction **open()** attend deux arguments, qui doivent tous deux
    être des chaînes de caractères. Le premier argument est le nom du
    fichier à ouvrir, et le second est le mode d'ouverture. **'a'** indique qu'il faut ouvrir ce
    fichier en mode « ajout » (*append*), ce qui signifie que les
    données à enregistrer doivent être ajoutées à la fin du fichier, à
    la suite de celles qui s'y trouvent éventuellement déjà. Nous
    aurions pu utiliser aussi le mode **'w'** (pour *write*), mais lorsqu'on
    utilise ce mode, Python crée toujours un nouveau fichier (vide), et
    l'écriture des données commence à partir du début de ce nouveau
    fichier. S'il existe déjà un fichier de même nom, celui-ci est
    effacé au préalable.
-   La méthode **write()** réalise l'écriture proprement dite. Les
    données à écrire doivent être fournies en argument. Ces données sont
    enregistrées dans le fichier les unes à la suite des autres (c'est
    la raison pour laquelle on parle de fichier à accès séquentiel).
    Chaque nouvel appel de **write()** continue l'écriture à la suite de
    ce qui est déjà enregistré.
-   La méthode **close()** referme le fichier. Celui-ci est désormais
    disponible pour tout usage.


[^note_53]: Une telle fonction, dont la valeur de retour est un objet particulier, est souvent appelée *fonction-fabrique*.
