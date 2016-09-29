## 11-H - Fichiers texte

Un *fichier texte* est un fichier qui contient des caractères
imprimables et des espaces organisés en lignes successives, ces lignes
étant séparées les unes des autres par un caractère spécial
non-imprimable appelé « marqueur de fin de ligne »[^note_55].

Les fichiers texte sont donc des fichiers que nous pouvons lire et
comprendre à l'aide d'un simple éditeur de texte, par opposition aux
*fichiers binaires* dont le contenu est - au moins en partie -
inintelligible pour un lecteur humain, et qui ne prend son sens que
lorsqu'il est décodé par un logiciel spécifique. Par exemple, les
fichiers contenant des images, des sons, des vidéos, etc. sont presque
toujours des fichiers binaires. Nous donnons un petit exemple de
traitement de fichier binaire un peu plus loin, mais dans le cadre de ce
cours, nous nous intéresserons presqu'exclusivement aux fichiers texte.

Il est très facile de traiter des fichiers
texte avec Python. Par exemple, les instructions suivantes suffisent
pour créer un fichier texte de quatre lignes :



```python
>>> f = open("Fichiertexte", "w")
>>> f.write("Ceci est la ligne un\nVoici la ligne deux\n")
>>> f.write("Voici la ligne trois\nVoici la ligne quatre\n")
>>> f.close() 
```



Notez bien le marqueur de fin de ligne **\\n** inséré dans les chaînes
de caractères, aux endroits où l'on souhaite séparer les lignes de texte
dans l'enregistrement. Sans ce marqueur, les caractères seraient
enregistrés les uns à la suite des autres, comme dans les exemples
précédents.

Lors des opérations de lecture, les lignes
d'un fichier texte peuvent être extraites
séparément les unes des autres. La méthode **readline()**, par exemple, ne lit qu'une seule
ligne à la fois (en incluant le caractère de fin de ligne) :



```python
>>> f = open('Fichiertexte','r')
>>> t = f.readline()
>>> print(t)
Ceci est la ligne un
>>> print(f.readline())
Voici la ligne deux
```



La méthode **readlines()**transfère toutes les lignes restantes dans une
liste de chaînes :



```python
>>> t = f.readlines()
>>> print(t)
['Voici la ligne trois\n', 'Voici la ligne quatre\n']
>>> f.close()
```



### 11-H-1 - Remarques {#article.xml#Ld0e23110 .TitreSection2}

-   La liste apparaît ci-dessus en format brut, avec des apostrophes
    pour délimiter les chaînes, et les caractères spéciaux sous leur
    forme conventionnelle. Vous pourrez bien évidemment parcourir cette
    liste (à l'aide d'une boucle **while**, par exemple) pour en
    extraire les chaînes individuelles.
-   La méthode **readlines()** permet donc de lire l'intégralité d'un
    fichier en une instruction seulement. Cela n'est possible toutefois
    que si le fichier à lire n'est pas trop gros : puisqu'il est copié
    intégralement dans une variable, c'est-à-dire dans la mémoire vive
    de l'ordinateur, il faut que la taille de celle-ci soit suffisante.
    Si vous devez traiter de gros fichiers, utilisez plutôt la méthode
    **readline()** dans une boucle, comme le montrera l'exemple suivant.
-   Notez bien que **readline()** est une méthode qui renvoie une
    *chaîne de caractères*, alors que la méthode **readlines()** renvoie
    une *liste*. À la fin du fichier, **readline()** renvoie une chaîne
    vide, tandis que **readlines()** renvoie une liste vide.

Le script qui suit vous montre comment
créer une fonction destinée à effectuer un certain traitement sur un
fichier texte. En l'occurrence, il s'agit ici de
recopier un fichier texte, en omettant toutes les lignes qui commencent
par un caractère **'\#'** :



```python
def filtre(source,destination):
  "recopier un fichier en éliminant les lignes de remarques"
 fs = open(source, 'r')
 fd = open(destination, 'w')
 while 1:
     txt = fs.readline()
     if txt =='':
     break
     if txt[0] != '#':
     fd.write(txt)
 fs.close()
 fd.close()
 return
```



Pour appeler cette fonction, vous devez
utiliser deux arguments : le nom du fichier original, et le nom du
fichier destiné à recevoir la copie filtrée. Exemple :



```python
filtre('test.txt', 'test_f.txt')
```




[^note_55]: Suivant le système d'exploitation utilisé, le codage correspondant au marqueur de fin de ligne peut être différent. Sous Windows, par exemple, il s'agit d'une séquence de deux caractères (retour chariot et saut de ligne), alors que dans les systèmes de type Unix (comme Linux) il s'agit d'un seul saut de ligne, MacOS pour sa part utilisant un seul retour chariot. En principe, vous n'avez pas à vous préoccuper de ces différences. Lors des opérations d'écriture, Python utilise la convention en vigueur sur votre système d'exploitation. Pour la lecture, Python interprète correctement chacune des trois conventions (qui sont donc considérées comme équivalentes).
