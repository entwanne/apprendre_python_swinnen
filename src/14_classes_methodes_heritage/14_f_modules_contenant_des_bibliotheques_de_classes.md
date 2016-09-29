## 14-F - Modules contenant des bibliothèques de classes

Vous connaissez déjà depuis longtemps l'utilité des modules Python (cf.
pages et ). Vous savez qu'ils servent à regrouper des bibliothèques de
classes et de fonctions. À titre d'exercice de révision, vous allez
créer vous-même un nouveau module de classes, en encodant les lignes
d'instruction ci-dessous dans un fichier-module que vous nommerez
**formes.py** :



```python
class Rectangle(object): 
  "Classe de rectangles" 
  def __init__(self, longueur =0, largeur =0): 
      self.L = longueur 
      self.l = largeur 
      self.nom ="rectangle" 
 
  def perimetre(self): 
      return "(%d + %d) * 2 = %d" % (self.L, self.l, 
		       (self.L + self.l)*2) 
  def surface(self): 
      return "%d * %d = %d" % (self.L, self.l, self.L*self.l) 
 
  def mesures(self): 
      print("Un %s de %d sur %d" % (self.nom, self.L, self.l)) 
      print("a une surface de %s" % (self.surface(),)) 
      print("et un périmètre de %s\n" % (self.perimetre(),)) 
 
class Carre(Rectangle): 
  "Classe de carrés" 
  def __init__(self, cote): 
      Rectangle.__init__(self, cote, cote) 
      self.nom ="carré" 
 
if __name__ == "__main__": 
  r1 = Rectangle(15, 30) 
  r1.mesures()	  
  c1 = Carre(13) 
  c1.mesures() 
```



Une fois ce module enregistré, vous pouvez l'utiliser de deux manières :
soit vous en lancez l'exécution comme celle d'un programme ordinaire,
soit vous l'importez dans un script quelconque ou depuis la ligne de
commande, pour en utiliser les classes. Exemple :



```python
>>> import formes
>>> f1 = formes.Rectangle(27, 12)
>>> f1.mesures()
Un rectangle de 27 sur 12
a une surface de 27 * 12 = 324
et un périmètre de (27 + 12) * 2 = 78
 
>>> f2 = formes.Carre(13)
>>> f2.mesures()
Un carré de 13 sur 13
a une surface de 13 * 13 = 169
et un périmètre de (13 + 13) * 2 = 52
```



On voit dans ce script que la classe **Carre()** est construite par
dérivation à partir de la classe **Rectangle()** dont elle hérite toutes
les caractéristiques. En d'autres termes, la classe **Carre()** est une
classe fille de la classe **Rectangle()**.

Vous pouvez remarquer encore une fois que le constructeur de la classe
**Carre()** doit faire appel au constructeur de sa classe parente (
**Rectangle.\_\_init\_\_(self,
...)** ), en lui transmettant la référence de l'instance
(**self**) comme premier argument.

Quant à l'instruction :



```python
if __name__ == "__main__":
```



placée à la fin du module, elle sert à déterminer si le module est «
lancé » en tant que programme autonome (auquel cas les instructions qui
suivent doivent être exécutées), ou au contraire utilisé comme une
bibliothèque de classes importée ailleurs. Dans ce cas cette partie du
code est sans effet.

Exercices

.Définissez une classe **Cercle()**. Les objets construits à partir de
cette classe seront des cercles de tailles variées. En plus de la
méthode constructeur (qui utilisera donc un paramètre **rayon**), vous
définirez une méthode **surface()**, qui devra renvoyer la surface du
cercle.

Définissez ensuite une classe **Cylindre()** dérivée de la précédente.
Le constructeur de cette nouvelle classe comportera les deux paramètres
**rayon** et **hauteur**. Vous y ajouterez une méthode **volume()** qui
devra renvoyer le volume du cylindre (rappel : volume d'un cylindre =
surface de section × hauteur).

Exemple d'utilisation de cette classe :\
`>>> cyl = Cylindre(5, 7)`\
`>>> print(cyl.surface())`\
`78.54`\
`>>> print(cyl.volume())`\
`549.78`

.Complétez l'exercice précédent en lui ajoutant encore une classe
**Cone()**, qui devra dériver cette fois de la classe **Cylindre()**, et
dont le constructeur comportera lui aussi les deux paramètres **rayon**
et **hauteur**. Cette nouvelle classe possédera sa propre méthode
**volume()**, laquelle devra renvoyer le volume du cône (rappel : volume
d'un cône = volume du cylindre correspondant divisé par 3).

Exemple d'utilisation de cette classe :\
`>>> co = Cone(5,7)`\
`>>> print(co.volume())`\
`183.26`

.Définissez une classe **JeuDeCartes()** permettant d'instancier des
objets dont le comportement soit similaire à celui d'un vrai jeu de
cartes. La classe devra comporter au moins les quatre méthodes suivantes
:

-   méthode constructeur : création et remplissage d'une liste de 52
    éléments, qui sont eux-mêmes des tuples de 2 entiers. Cette liste de
    tuples contiendra les caractéristiques de chacune des 52 cartes.
    Pour chacune d'elles, il faut en effet mémoriser séparément un
    entier indiquant la valeur (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, les 4 dernières valeurs étant celles des valet, dame, roi et
    as), et un autre entier indiquant la couleur de la carte
    (c'est-à-dire 3,2,1,0 pour Cœur, Carreau, Trèfle et Pique).\
     Dans une telle liste, l'élément (11,2) désigne donc le valet de
    Trèfle, et la liste terminée doit être du type :\
    **[(2, 0), (3,0), (3,0), (4,0), .....
    (12,3), (13,3), (14,3)]**
-   méthode **nom\_carte()** : cette méthode doit renvoyer, sous la
    forme d'une chaîne, l'identité d'une carte quelconque dont on lui a
    fourni le tuple descripteur en argument. Par exemple, l'instruction
    : **print(jeu.nom\_carte((14,
    3)))** doit provoquer l'affichage de :` As de pique`
-   méthode **battre()** : comme chacun sait, battre les cartes consiste
    à les mélanger.\
     Cette méthode sert donc à mélanger les éléments de la liste
    contenant les cartes, quel qu'en soit le nombre.
-   méthode **tirer()** : lorsque cette méthode est invoquée, une carte
    est retirée du jeu. Le tuple contenant sa valeur et sa couleur est
    renvoyé au programme appelant. On retire toujours la première carte
    de la liste. Si cette méthode est invoquée alors qu'il ne reste plus
    aucune carte dans la liste, il faut alors renvoyer l'objet spécial
    **None** au programme appelant. Exemple d'utilisation de la classe
    **JeuDeCartes()** :\
    \
    `jeu = JeuDeCartes() `*\# instanciation d***'***un
    objet*\
    `jeu.battre() `*\# mélange des cartes*\
    `for n in range(53): `*\# tirage des 52 cartes :*\
    `c = jeu.tirer() `\
    `if c == None: `*\# il ne reste plus aucune carte*\
    **print('Terminé
    !')***\# dans la liste*\
    `else:`\
    **print(jeu.nom\_carte(c))
    ***\# valeur et couleur de la
    carte*\

.Complément de l'exercice précédent
: définir deux joueurs A et B. Instancier deux jeux de cartes (un pour
chaque joueur) et les mélanger. Ensuite, à l'aide d'une boucle, tirer 52
fois une carte de chacun des deux jeux et comparer leurs valeurs. Si
c'est la première des deux qui a la valeur la plus élevée, on ajoute un
point au joueur A. Si la situation contraire se présente, on ajoute un
point au joueur B. Si les deux valeurs sont égales, on passe au tirage
suivant. Au terme de la boucle, comparer les comptes de A et B pour
déterminer le gagnant.

.Écrivez un nouveau script qui
récupère le code de l'exercice 12.2 (compte bancaire) en l'important
comme un module. Définissez-y une nouvelle classe **CompteEpargne()**,
dérivant de la classe **CompteBancaire()** importée, qui permette de
créer des comptes d'épargne rapportant un certain intérêt au cours du
temps. Pour simplifier, nous admettrons que ces intérêts sont calculés
tous les mois.\
 Le constructeur de votre nouvelle classe devra initialiser un taux
d'intérêt mensuel par défaut égal à **0,3 %**. Une méthode
**changeTaux(valeur)** devra permettre de modifier ce taux à volonté.\
 Une méthode **capitalisation(nombreMois)** devra :

-   afficher le nombre de mois et le taux d'intérêt pris en compte ;
-   calculer le solde atteint en capitalisant les intérêts composés,
    pour le taux et le nombre de mois qui auront été choisis.

Exemple d'utilisation de la nouvelle classe :\
\
**\>\>\> c1 = CompteEpargne('Duvivier', 600)
**\
`>>> c1.depot(350)`\
`>>> c1.affiche()`\
**Le solde du compte bancaire de Duvivier
est de 950 euros. **\
`>>> c1.capitalisation(12)`\
**Capitalisation sur 12 mois au taux
mensuel de 0.3 %.**\
`>>> c1.affiche()`\
**Le solde du compte bancaire de Duvivier
est de 984.769981274 euros. **\
`>>> c1.changeTaux(.5)`\
`>>> c1.capitalisation(12)`\
**Capitalisation sur 12 mois au taux
mensuel de 0.5 %. **\
`>>> c1.affiche()`\
**Le solde du compte bancaire de Duvivier
est de 1045.50843891 euros.**

