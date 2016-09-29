## 8-B - Interaction avec l'utilisateur : la fonction input()

La plupart des scripts élaborés nécessitent à un moment ou l'autre une
intervention de l'utilisateur (entrée d'un paramètre, clic de souris sur
un bouton, etc.). Dans un script en mode texte (comme ceux que nous
avons créés jusqu'à présent), la méthode la plus simple consiste à
employer la fonction intégrée **input()**. Cette fonction provoque une
interruption dans le programme courant. L'utilisateur est invité à
entrer des caractères au clavier et à terminer avec \<*Enter*\>. Lorsque
cette touche est enfoncée, l'exécution du programme se poursuit, et la
fonction fournit en retour une chaîne de caractères correspondant à ce
que l'utilisateur a entré. Cette chaîne peut alors être assignée à une
variable quelconque, convertie, etc.

On peut invoquer la fonction **input()** en laissant les parenthèses
vides. On peut aussi y placer en argument un message explicatif destiné
à l'utilisateur. Exemple :



```python
prenom = input("Entrez votre prénom : ")
print("Bonjour,", prenom)
```



ou encore :



```python
print("Veuillez entrer un nombre positif quelconque : ", end=" ")
ch = input()
nn = int(ch)	     # conversion de la chaîne en un nombre entier
print("Le carré de", nn, "vaut", nn**2)
```



### 8-B-1 - Remarque importante {#article.xml#Ld0e8122 .TitreSection2}

-   La fonction **input()** renvoie toujours une chaîne de
    caractères[^note_25].
    Si vous souhaitez que l'utilisateur entre une valeur numérique, vous
    devrez donc convertir la valeur entrée (qui sera donc de toute façon
    de type string) en une valeur numérique du type qui vous convient,
    par l'intermédiaire des fonctions intégrées **int()** (si vous
    attendez un entier) ou **float()** (si vous attendez un réel).
    Exemple :



```python
>>> a = input("Entrez une donnée numérique : ")
Entrez une donnée numérique : 52.37
>>> type(a)
<class 'str'>
>>> b = float(a)     # conversion de la chaîne en un nombre réel
>>> type(b)
<class 'float'>
```




[^note_25]: Dans les versions de Python antérieures à la version 3.0, la valeur renvoyée par input() était de type variable, suivant ce que l'utilisateur avait entré. Le comportement actuel est en fait celui de l'ancienne fonction raw\_input(), que lui préféraient la plupart des programmeurs.
