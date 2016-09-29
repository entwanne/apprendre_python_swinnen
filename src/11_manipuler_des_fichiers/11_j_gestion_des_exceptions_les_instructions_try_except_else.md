## 11-J - Gestion des exceptions : les instructions try - except - else

Les *exceptions*sont les opérations qu'effectue un
interpréteur ou un compilateur lorsqu'une erreur
est détectée au cours de l'exécution
d'un programme. En règle générale, l'exécution du
programme est alors interrompue, et un message d'erreur plus
ou moins explicite est affiché. Exemple :



```python
>>> print(55/0)
ZeroDivisionError: int division or modulo by zero
```



> D*'*autres
> informations complémentaires sont affichées, lesquelles indiquent
> notamment à quel endroit du script l*'*erreur a
> été détectée, mais nous ne les reproduisons pas ici.

Le message d'erreur proprement dit comporte deux parties séparées par un
double point : d'abord le type d'erreur, et ensuite une information
spécifique de cette erreur.

Dans de nombreux cas, il est possible de prévoir à l'avance certaines
des erreurs qui risquent de se produire à tel ou tel endroit du
programme et d'inclure à cet endroit des instructions particulières, qui
seront activées seulement si ces erreurs se produisent. Dans les
langages de niveau élevé comme Python, il est également possible
d'associer un mécanisme de surveillance à *tout un ensemble
d'instructions*, et donc de simplifier le traitement des erreurs qui
peuvent se produire dans n'importe laquelle de ces instructions.

Un mécanisme de ce type s'appelle en général *mécanisme de traitement
des exceptions*. Celui de Python utilise l'ensemble d'instructions
**try** - **except** - **else**, qui permettent d'intercepter une erreur
et d'exécuter une portion de script spécifique de cette erreur. Il
fonctionne comme suit.

Le bloc d'instructions qui suit directement une instruction **try** est
exécuté par Python *sousréserve*. Si une erreur survient pendant
l'exécution de l'une de ces instructions, alors Python annule cette
instruction fautive et exécute à sa place le code inclus dans le bloc
qui suit l'instruction **except.** Si aucune erreur ne s'est produite
dans les instructions qui suivent **try**, alors c'est le bloc qui suit
l'instruction **else** qui est exécuté (si cette instruction est
présente). Dans tous les cas, l'exécution du programme peut se
poursuivre ensuite avec les instructions ultérieures.

Considérons par exemple un script qui
demande à l'utilisateur d'entrer un
nom de fichier, lequel fichier étant destiné à être ouvert en lecture.
Si le fichier n'existe pas, nous ne voulons pas que le programme
se « plante ». Nous voulons qu'un
avertissement soit affiché, et éventuellement que l'utilisateur
puisse essayer d'entrer un autre nom.



```python
filename = input("Veuillez entrer un nom de fichier : ")
try:
 f = open(filename, "r")
except:
 print("Le fichier", filename, "est introuvable")
```



Si nous estimons que ce genre de test est
susceptible de rendre service à plusieurs endroits d'un
programme, nous pouvons aussi l'inclure dans
une fonction :



```python
def existe(fname):
 try:
     f = open(fname,'r')
     f.close()
     return 1
 except:
     return 0
 
filename = input("Veuillez entrer le nom du fichier : ")
if existe(filename):
 print("Ce fichier existe bel et bien.")
else:
 print("Le fichier", filename, "est introuvable.")
```



Il est également possible de faire suivre l'instruction **try** de
plusieurs blocs **except**, chacun d'entre eux traitant un type d'erreur
spécifique, mais nous ne développerons pas ces compléments ici. Veuillez
consulter un ouvrage de référence sur Python si nécessaire.

Exercices

.Écrivez un script qui permette de créer et de relire aisément un
fichier texte. Votre programme demandera d'abord à l'utilisateur
d'entrer le nom du fichier. Ensuite il lui proposera le choix, soit
d'enregistrer de nouvelles lignes de texte, soit d'afficher le contenu
du fichier.\
 L'utilisateur devra pouvoir entrer ses lignes de texte successives en
utilisant simplement la touche \<Enter\> pour les séparer les unes des
autres. Pour terminer les entrées, il lui suffira d'entrer une ligne
vide (c'est-à-dire utiliser la touche \<Enter\> seule).\
 L'affichage du contenu devra montrer les lignes du fichier séparées les
unes des autres de la manière la plus naturelle (les codes de fin de
ligne ne doivent pas apparaître).

.Considérons que vous avez à votre disposition un fichier texte
contenant des phrases de différentes longueurs. Écrivez un script qui
recherche et affiche la phrase la plus longue.

.Écrivez un script qui génère automatiquement un fichier texte contenant
les tables de multiplication de 2 à 30 (chacune d'entre elles incluant
20 termes seulement).

.Écrivez un script qui recopie un fichier texte en triplant tous les
espaces entre les mots.

.Vous avez à votre disposition un fichier texte dont chaque ligne est la
représentation d'une valeur numérique de type réel (mais sans
exposants). Par exemple :

`14.896`\
`7894.6`\
`123.278`\
`etc.`

Écrivez un script qui recopie ces valeurs dans un autre fichier en les
arrondissant en nombres entiers (l'arrondi doit être correct).

.Écrivez un script qui compare les contenus de deux fichiers et signale
la première différence rencontrée.

.À partir de deux fichiers préexistants A et B, construisez un fichier C
qui contienne alternativement un élément de A, un élément de B, un
élément de A... et ainsi de suite jusqu'à atteindre la fin de l'un des
deux fichiers originaux. Complétez ensuite C avec les éléments restant
sur l'autre.

.Écrivez un script qui permette d'encoder un fichier texte dont les
lignes contiendront chacune les noms, prénom, adresse, code postal et
n^o^ de téléphone de différentes personnes (considérez par exemple qu'il
s'agit des membres d'un club).

.Écrivez un script qui recopie le fichier utilisé dans l'exercice
précédent, en y ajoutant la date de naissance et le sexe des personnes
(l'ordinateur devra afficher les lignes une par une et demander à
l'utilisateur d'entrer pour chacune les données complémentaires).

.Considérons que vous avez fait les exercices précédents et que vous
disposez à présent d'un fichier contenant les coordonnées d'un certain
nombre de personnes. Écrivez un script qui permette d'extraire de ce
fichier les lignes qui correspondent à un code postal bien déterminé.

.Modifiez le script de l'exercice précédent, de manière à retrouver les
lignes correspondant à des prénoms dont la première lettre est située
entre F et M (inclus) dans l'alphabet.

.Écrivez des fonctions qui effectuent le
même travail que celles du module **pickle**. Ces fonctions doivent permettre
l'enregistrement de variables diverses dans un fichier texte, en les
accompagnant systématiquement d'informations concernant leur format
exact.

