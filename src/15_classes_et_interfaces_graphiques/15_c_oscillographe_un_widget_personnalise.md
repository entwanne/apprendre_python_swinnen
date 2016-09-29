## 15-C - OscilloGraphe : un widget personnalisé

Le projet qui suit va nous entraîner encore un petit peu plus loin. Nous
allons y construire *une nouvelle classe de widget*, qu'il sera possible
d'intégrer dans nos projets futurs comme n'importe quel widget standard.
Comme la classe principale de l'exercice précédent, cette nouvelle
classe sera construite par dérivation d'une classe tkinter préexistante.

Le sujet concret de cette application nous est inspiré par le cours de
physique.

Pour rappel, un mouvement vibratoire harmonique se définit comme étant
la projection d'un mouvement circulaire uniforme sur une droite. Les
positions successives d'un mobile qui effectue ce type de mouvement sont
traditionnellement repérées par rapport à une position centrale : on les
appelle alors des *élongations*. L'équation qui décrit l'évolution de
l'élongation d'un tel mobile au cours du temps est toujours de la forme
![](images/formule09.png), dans laquelle ***e*** représente l'élongation
du mobile à tout instant ***t*** . Les constantes ***A, f*** et *φ*
désignent respectivement l'*amplitude*, la *fréquence* et la *phase* du
mouvement vibratoire.



![](images/image38.png)



Le widget que nous allons construire d'abord s'occupera de l'affichage
proprement dit. Nous construirons ensuite d'autres widgets pour
faciliter l'entrée des paramètres ***A, f*** et *φ*.

Veuillez donc encoder le script ci-dessous et le sauvegarder dans un
fichier, auquel vous donnerez le nom **oscillo.py**. Vous réaliserez
ainsi *un véritable module contenant une classe* (vous pourrez par la
suite ajouter d'autres classes dans ce même module, si le cœur vous en
dit).\



```python
from tkinter import *
from math import sin, pi
 
class OscilloGraphe(Canvas):
  "Canevas spécialisé, pour dessiner des courbes élongation/temps"
  def __init__(self, boss =None, larg=200, haut=150):
      "Constructeur du graphique : axes et échelle horiz."
      # construction du widget parent :
      Canvas.__init__(self)		    # appel au constructeur
      self.configure(width=larg, height=haut)	      # de la classe parente
      self.larg, self.haut = larg, haut 	     # mémorisation
      # tracé des axes de référence :
      self.create_line(10, haut/2, larg, haut/2, arrow=LAST)  # axe X
      self.create_line(10, haut-5, 10, 5, arrow=LAST)	       # axe Y
      # tracé d'une échelle avec 8 graduations :
      pas = (larg-25)/8.      # intervalles de l'échelle horizontale
      for t in range(1, 9):
      stx = 10 + t*pas	    # +10 pour partir de l'origine
      self.create_line(stx, haut/2-4, stx, haut/2+4)
 
  def traceCourbe(self, freq=1, phase=0, ampl=10, coul='red'):
      "tracé d'un graphique élongation/temps sur 1 seconde"
      curve =[] 	     # liste des coordonnées
      pas = (self.larg-25)/1000.      # l'échelle X correspond à 1 seconde
      for t in range(0,1001,5):       # que l'on divise en 1000 ms.
      e = ampl*sin(2*pi*freq*t/1000 - phase)
      x = 10 + t*pas
      y = self.haut/2 - e*self.haut/25
      curve.append((x,y))
      n = self.create_line(curve, fill=coul, smooth=1)
      return n		     # n = numéro d'ordre du tracé
 
#### Code pour tester la classe : ####
 
if __name__ == '__main__':
  root = Tk()
  gra = OscilloGraphe(root, 250, 180)
  gra.pack()
  gra.configure(bg ='ivory', bd =2, relief=SUNKEN)
  gra.traceCourbe(2, 1.2, 10, 'purple')
  root.mainloop()    
```



Le niveau principal du script est constitué par les lignes 35 à 41.\
 Comme nous l'avons déjà expliqué à la page , les lignes de code situées
après l'instruction **if \_\_name\_\_ ==
'\_\_main\_\_': **ne sont pas exécutées si le script est importé
en tant que module dans une autre application. Si on lance le script
comme application principale, par contre, ces instructions s'exécutent.
Nous disposons ainsi d'un mécanisme intéressant, qui nous permet
d'intégrer des instructions de test à l'intérieur des modules, même si
ceux-ci sont destinés à être importés dans d'autres scripts.

Lancez donc l'exécution du script de la manière habituelle. Vous devriez
obtenir un affichage similaire à celui qui est reproduit à la page
précédente.



![](images/image39.png)



### 15-C-1 - Expérimentation {#article.xml#Ld0e46194 .TitreSection2}

Nous commenterons les lignes importantes du script un peu plus loin dans
ce texte. Mais commençons d'abord par expérimenter quelque peu la classe
que nous venons de construire.

Ouvrez donc votre terminal, et entrez les instructions ci-dessous
directement à la ligne de commande :



```python
>>> from oscillo import *
>>> g1 = OscilloGraphe()
>>> g1.pack()
```



Après importation des classes du module **oscillo**, nous instancions un
premier objet **g1**, de la classe **OscilloGraphe()**.

Puisque nous ne fournissons aucun argument, l'objet possède les
dimensions par défaut, définies dans le constructeur de la classe.
Remarquons au passage que nous n'avons même pas pris la peine de définir
d'abord une fenêtre maître pour y placer ensuite notre widget. tkinter
nous pardonne cet oubli et nous en fournit une automatiquement !



```python
>>> g2 = OscilloGraphe(haut=200, larg=250)
>>> g2.pack()
>>> g2.traceCourbe()
```



Par ces instructions, nous créons un second widget de la même classe, en
précisant cette fois ses dimensions (hauteur et largeur, dans n'importe
quel ordre).

Ensuite, nous activons la méthode **traceCourbe()** associée à ce
widget. Étant donné que nous ne lui fournissons aucun argument, la
sinusoïde qui apparaît correspond aux valeurs prévues par défaut pour
les paramètres *A, f* et *φ*.



```python
>>> g3 = OscilloGraphe(larg=220)
>>> g3.configure(bg='white', bd=3, relief=SUNKEN)
>>> g3.pack(padx=5,pady=5)
>>> g3.traceCourbe(phase=1.57, coul='purple')
>>> g3.traceCourbe(phase=3.14, coul='dark green')
```



Pour comprendre la configuration de ce troisième widget, il faut nous
rappeler que la classe **OscilloGraphe()** a été construite par
dérivation de la classe **Canvas()**. Elle hérite donc toutes les
propriétés de celle-ci, ce qui nous permet de choisir la couleur de
fond, la bordure, etc., en utilisant les mêmes arguments que ceux qui
sont à notre disposition lorsque nous configurons un canevas.

Nous faisons ensuite apparaître deux tracés successifs, en faisant appel
deux fois à la méthode **traceCourbe()**, à laquelle nous fournissons
des arguments pour la phase et la couleur.

Exercice

.Créez un quatrième widget, de
taille : 400 × 300, couleur de fond : jaune, et faites-y apparaître
plusieurs courbes correspondant à des fréquences et des amplitudes
différentes.

Il est temps à présent que nous analysions la structure de la classe qui
nous a permis d'instancier tous ces widgets. Nous avons donc enregistré
cette classe dans le module **oscillo.py** (voir page ).

### 15-C-2 - Cahier des charges {#article.xml#Ld0e46479 .TitreSection2}

Nous souhaitons définir une nouvelle classe de widget, capable
d'afficher automatiquement les graphiques élongation/temps correspondant
à divers mouvements vibratoires harmoniques.

Ce widget doit pouvoir être dimensionné à volonté au moment de son
instanciation. Il doit faire apparaître deux axes cartésiens X et Y
munis de flèches. L'axe X représentera l'écoulement du temps pendant une
seconde au total, et il sera muni d'une échelle comportant 8
intervalles.

Une méthode **traceCourbe()** sera associée à ce widget. Elle provoquera
le tracé du graphique élongation/temps pour un mouvement vibratoire,
dont on aura fourni la *fréquence* (entre 0.25 et 10 Hz), la *phase*
(entre 0 et 2**π** radians) et *l'amplitude* (entre 1 et 10 ; échelle
arbitraire).

### 15-C-3 - Implémentation {#article.xml#Ld0e46503 .TitreSection2}

-   Ligne 4 : La classe **OscilloGraphe()** est créée par dérivation de
    la classe **Canvas()**. Elle hérite donc toutes les propriétés de
    celle-ci : on pourra configurer les objets de cette nouvelle classe
    en utilisant les nombreuses options déjà disponibles pour la classe
    **Canvas()**.
-   Ligne 6 : La méthode constructeur utilise 3 paramètres, qui sont
    tous optionnels puisque chacun d'entre eux possède une valeur par
    défaut. Le paramètre **boss** ne sert qu'à réceptionner la référence
    d'une fenêtre maîtresse éventuelle (voir exemples suivants). Les
    paramètres **larg** et **haut** (largeur et hauteur) servent à
    assigner des valeurs aux options **width** et **height** du canevas
    parent, au moment de l'instanciation.
-   Lignes 9-10 : Comme nous l'avons déjà dit à plusieurs reprises, le
    constructeur d'une classe dérivée doit presque toujours commencer
    par activer le constructeur de sa classe parente. Nous ne pouvons en
    effet hériter toute la fonctionnalité de la classe parente, que si
    cette fonctionnalité a été effectivement mise en place et
    initialisée.\
     Nous activons donc le constructeur de la classe **Canvas()** à la
    ligne 9, et nous ajustons deux de ses options à la ligne 10. Notez
    au passage que nous pourrions condenser ces deux lignes en une
    seule, qui deviendrait en l'occurrence :\
    **Canvas.\_\_init\_\_(self, width=larg,
    height=haut)**.\
     Et comme cela a également déjà été expliqué (cf. page ), nous
    devons transmettre à ce constructeur la référence de l'instance
    présente (**self**) comme premier argument.
-   Ligne 11 : Il est nécessaire de mémoriser les paramètres **larg** et
    **haut** dans des variables d'instance, parce que nous devrons
    pouvoir y accéder aussi dans la méthode **traceCourbe()**.
-   Lignes 13-14 : Pour tracer les axes X et Y, nous utilisons les
    paramètres **larg** et **haut**, ainsi ces axes sont automatiquement
    mis à dimension. L'option `arrow=LAST` permet de faire
    apparaître une petite flèche à l'extrémité de chaque ligne.
-   Lignes 16 à 19 : Pour tracer l'échelle horizontale, on commence par
    réduire de 25 pixels la largeur disponible, de manière à ménager des
    espaces aux deux extrémités. On divise ensuite en 8 intervalles, que
    l'on visualise sous la forme de 8 petits traits verticaux.
-   Ligne 21 : La méthode **traceCourbe()** pourra être invoquée avec
    quatre arguments. Chacun d'entre eux pourra éventuellement être
    omis, puisque chacun des paramètres correspondants possède une
    valeur par défaut. Il sera également possible de fournir les
    arguments dans n'importe quel ordre, comme nous l'avons déjà
    expliqué à la page .
-   Lignes 23 à 31 : Pour le tracé de la courbe, la variable **t** prend
    successivement toutes les valeurs de 0 à 1000, et on calcule à
    chaque fois l'élongation **e** correspondante, à l'aide de la
    formule théorique (ligne 26). Les couples de valeurs **t** et **e**
    ainsi trouvées sont mises à l'échelle et transformées en coordonnées
    **x, y** aux lignes 27 et 28, puis accumulées dans la liste
    **curve**.
-   Lignes 30-31 : La méthode **create\_line()** trace alors la courbe
    correspondante en une seule opération, et elle renvoie le numéro
    d'ordre du nouvel objet ainsi instancié dans le canevas (ce numéro
    d'ordre nous permettra d'y accéder encore par après : pour
    l'effacer, par exemple). L'option `smooth =1`améliore l'aspect final,
    par lissage.

Exercices

.Modifiez le script de manière à ce que l'axe de référence vertical
comporte lui aussi une échelle, avec 5 tirets de part et d'autre de
l'origine.

.Comme les widgets de la classe **Canvas()** dont il dérive, votre
widget peut intégrer des indications textuelles. Il suffit pour cela
d'utiliser la méthode **create\_text()**. Cette méthode attend au moins
trois arguments : les coordonnées **x** et **y** de l'emplacement où
vous voulez faire apparaître votre texte et puis le texte lui-même, bien
entendu. D'autres arguments peuvent être transmis sous forme d'options,
pour préciser par exemple la police de caractères et sa taille. Afin de
voir comment cela fonctionne, ajoutez provisoirement la ligne suivante
dans le constructeur de la classe **OscilloGraphe()**, puis relancez le
script :

**self.create\_text(130, 30, text =
"Essai", anchor =CENTER)**

Utilisez cette méthode pour ajouter au widget les indications suivantes
aux extrémités des axes de référence : **e** (pour « élongation ») le
long de l'axe vertical, et **t** (pour « temps ») le long de l'axe
horizontal. Le résultat pourrait ressembler à la figure de gauche page .

.Vous pouvez compléter encore votre widget en y faisant apparaître une
grille de référence plutôt que de simples tirets le long des axes. Pour
éviter que cette grille ne soit trop visible, vous pouvez colorer ses
traits en gris (option **fill =
'grey'**), comme dans la figure de droite de la
page .

.Complétez encore votre widget en y faisant apparaître des repères
numériques.

