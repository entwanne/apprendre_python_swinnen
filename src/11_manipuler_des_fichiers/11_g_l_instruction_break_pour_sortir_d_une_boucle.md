## 11-G - L'instruction break pour sortir d'une boucle

Il va de soi que les boucles de programmation s'imposent lorsque l'on
doit traiter un fichier dont on ne connaît pas nécessairement le contenu
à l'avance. L'idée de base consistera à lire ce fichier morceau par
morceau, jusqu'à ce que l'on ait atteint la fin du fichier.

La fonction ci-dessous illustre cette idée.
Elle copie l'intégralité d'un fichier,
quelle que soit sa taille, en transférant des portions de 50 caractères
à la fois :



```python
def copieFichier(source, destination):
  "copie intégrale d'un fichier" 
 fs = open(source, 'r')
 fd = open(destination, 'w')
 while 1:
     txt = fs.read(50)
     if txt =="":
     break
     fd.write(txt)
 fs.close()
 fd.close()
 return
```



Si vous voulez tester cette fonction, vous
devez lui fournir deux arguments : le premier est le nom du fichier
original, le second est le nom à donner au fichier qui accueillera la
copie. Exemple :



```python
copieFichier('Monfichier','Tonfichier') 
```



Vous aurez remarqué que la boucle **while** utilisée dans cette fonction
est construite d'une manière différente de ce que vous avez rencontré
précédemment. Vous savez en effet que l'instruction **while** doit
toujours être suivie d'une condition à évaluer ; le bloc d'instructions
qui suit est alors exécuté en boucle, aussi longtemps que cette
condition reste vraie. Or nous avons remplacé ici la condition à évaluer
par une simple constante, et vous savez également[^note_54]
que l'interpréteur Python considère comme vraie toute valeur numérique
différente de zéro.

Une boucle **while**construite comme nous l'avons fait
ci-dessus devrait donc boucler indéfiniment, puisque la condition de
continuation reste toujours vraie. Nous pouvons cependant interrompre ce
bouclage en faisant appel à l'instruction
**break**, laquelle permet
éventuellement de mettre en place plusieurs mécanismes de sortie
différents pour une même boucle :



```python
while <condition 1> :
 --- instructions diverses ---
 if <condition 2> :
     break
 --- instructions diverses ---
 if <condition 3>:
      break
 etc.
```



Dans notre fonction **copieFichier()**, il est facile de voir que
l'instruction **break** s'exécutera seulement lorsque la fin du fichier
aura été atteinte.


[^note_54]: Voir page : Véracité/fausseté d'une expression
