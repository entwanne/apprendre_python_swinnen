## 15-A - Code des couleurs : un petit projet bien encapsulé

Nous allons commencer par un petit projet qui nous a été inspiré par le
cours d'initiation à l'électronique. L'application que nous décrivons
ci-après permet de retrouver rapidement le code de trois couleurs qui
correspond à une résistance électrique de valeur bien déterminée.

Pour rappel, la fonction des résistances électriques consiste à
s'opposer (à résister) plus ou moins bien au passage du courant. Les
résistances se présentent concrètement sous la forme de petites pièces
tubulaires cerclées de bandes de couleur (en général 3). Ces bandes de
couleur indiquent la valeur numérique de la résistance, en fonction du
code suivant :

Chaque couleur correspond conventionnellement à l'un des chiffres de
zéro à neuf :

Noir = 0 ; Brun = 1 ; Rouge = 2 ; Orange = 3 ; Jaune = 4 ;\
 Vert = 5 ; Bleu = 6 ; Violet = 7 ; Gris = 8 ; Blanc = 9.

On oriente la résistance de manière telle que les bandes colorées soient
placées à gauche. La valeur de la résistance - exprimée en ohms
(**Ω**) - s'obtient en lisant ces bandes colorées également à partir de
la gauche : les deux premières bandes indiquent les deux premiers
chiffres de la valeur numérique ; il faut ensuite accoler à ces deux
chiffres un nombre de zéros égal à l'indication fournie par la troisième
bande.

Exemple concret : supposons qu'à partir de la gauche, les bandes
colorées soient jaune, violette et verte.\
 La valeur de cette résistance est 4700000 **Ω** , ou 4700 **kΩ** , ou
encore 4,7 **MΩ** .

Ce système ne permet évidemment de préciser une valeur numérique qu'avec
deux chiffres significatifs seulement. Il est toutefois considéré comme
largement suffisant pour la plupart des applications électroniques «
ordinaires » (radio, TV, etc.).

### 15-A-1 - Cahier des charges de notre programme {#article.xml#Ld0e42436 .TitreSection2}



![](images/image36.png)



Notre application doit faire apparaître une fenêtre comportant un dessin
de la résistance, ainsi qu'un champ d'entrée dans lequel l'utilisateur
peut encoder une valeur numérique. Un bouton « Montrer » déclenche la
modification du dessin de la résistance, de telle façon que les trois
bandes de couleur se mettent en accord avec la valeur numérique
introduite.

Contrainte : Le programme doit accepter toute entrée numérique fournie
sous forme entière ou réelle, dans les limites de 10 à 10^11^**Ω**. Par
exemple, une valeur telle que 4.78e6 doit être acceptée et arrondie
correctement, c'est-à-dire convertie en 4800000 **Ω**.\

### 15-A-2 - Mise en œuvre concrète {#article.xml#Ld0e42453 .TitreSection2}

Nous construisons le corps de cette application simple sous la forme
d'une classe. Nous voulons vous montrer ainsi comment une classe peut
servir d'*espace de noms commun*, dans lequel vous pouvez *encapsuler*
vos variables et nos fonctions. Le principal intérêt de procéder ainsi
est que cela vous permet de vous passer de variables globales. En effet
:

-   Mettre en route l'application se résumera à instancier un objet de
    cette classe.
-   Les fonctions que l'on voudra y mettre en œuvre seront les
    *méthodes* de cet objet-application.
-   À l'intérieur de ces méthodes, il suffira de rattacher un nom de
    variable au paramètre **self** pour que cette variable soit
    accessible de partout à l'intérieur de l'objet. Une telle *variable
    d'instance* est donc tout à fait l'équivalent d'une variable globale
    (mais seulement à l'intérieur de l'objet), puisque toutes les autres
    méthodes de cet objet peuvent y accéder par l'intermédiaire de
    **self**.\



```python
class Application(object): 
  def __init__(self): 
      """Constructeur de la fenêtre principale""" 
      self.root =Tk() 
      self.root.title('Code des couleurs') 
      self.dessineResistance() 
      Label(self.root, text ="Entrez la valeur de la résistance, en ohms :").\ 
	  grid(row =2, column =1, columnspan =3) 
      Button(self.root, text ='Montrer', command =self.changeCouleurs).\ 
	  grid(row =3, column =1) 
      Button(self.root, text ='Quitter', command =self.root.quit).\ 
	  grid(row =3, column =3) 
      self.entree = Entry(self.root, width =14) 
      self.entree.grid(row =3, column =2) 
      # Code des couleurs pour les valeurs de zéro à neuf :
      self.cc = ['black','brown','red','orange','yellow', 
	 'green','blue','purple','grey','white'] 
      self.root.mainloop() 
 
  def dessineResistance(self): 
      """Canevas avec un modèle de résistance à trois lignes colorées""" 
      self.can = Canvas(self.root, width=250, height =100, bg ='ivory') 
      self.can.grid(row =1, column =1, columnspan =3, pady =5, padx =5) 
      self.can.create_line(10, 50, 240, 50, width =5)	       # fils
      self.can.create_rectangle(65, 30, 185, 70, fill ='light grey', width =2) 
      # Dessin des trois lignes colorées (noires au départ) :
      self.ligne =[]	     # on mémorisera les trois lignes dans 1 liste
      for x in range(85,150,24): 
      self.ligne.append(self.can.create_rectangle(x,30,x+12,70, 
			      fill='black',width=0)) 
 
  def changeCouleurs(self): 
      """Affichage des couleurs correspondant à la valeur entrée""" 
      self.v1ch = self.entree.get()	 # cette méthode renvoie une chaîne
      try: 
      v = float(self.v1ch)	 #conversion en valeur numérique
      except: 
      err =1		  # erreur : entrée non numérique
      else: 
      err =0 
      if err ==1 or v < 10 or v > 1e11 : 
      self.signaleErreur()	 # entrée incorrecte ou hors limites
      else: 
      li =[0]*3 	     # liste des 3 codes à afficher 
      logv = int(log10(v))	 # partie entière du logarithme 
      ordgr = 10**logv		# ordre de grandeur 
      # extraction du premier chiffre significatif : 
      li[0] = int(v/ordgr)	 # partie entière
      decim = v/ordgr - li[0]	   # partie décimale 
      # extraction du second chiffre significatif :
      li[1] = int(decim*10 +.5)      # +.5 pour arrondir correctement 
      # nombre de zéros à accoler aux 2 chiffres significatifs :
      li[2] = logv -1 
      # Coloration des 3 lignes :
      for n in range(3): 
	  self.can.itemconfigure(self.ligne[n], fill =self.cc[li[n]]) 
 
  def signaleErreur(self): 
      self.entree.configure(bg ='red')	     # colorer le fond du champ
      self.root.after(1000, self.videEntree)	  # après 1 seconde, effacer 
 
  def videEntree(self): 
      self.entree.configure(bg ='white')      # rétablir le fond blanc
      self.entree.delete(0, len(self.v1ch))	 # enlever les car. présents
 
# Programme principal :
if __name__ == '__main__': 
  from tkinter import * 
  from math import log10	# logarithmes en base 10
  f = Application()	       # instanciation de l'objet application
```



### 15-A-3 - Commentaires {#article.xml#Ld0e43925 .TitreSection2}

-   Ligne 1 : La classe est définie comme une nouvelle classe
    indépendante (elle ne dérive d'aucune classe parente préexistante,
    mais seulement de **object**, « ancêtre » de toutes les classes).
-   Lignes 2 à 14 : Le constructeur de la classe instancie les widgets
    nécessaires : espace graphique, libellés et boutons. Afin
    d'améliorer la lisibilité du programme, cependant, nous avons placé
    l'instanciation du canevas (avec le dessin de la résistance) dans
    une méthode distincte : **dessineResistance()**. Veuillez remarquer
    aussi que pour obtenir un code plus compact, nous ne mémorisons pas
    les boutons et le libellé dans des variables (comme cela a été
    expliqué à la page ), parce que nous ne souhaitons pas y faire
    référence ailleurs dans le programme. Le positionnement des widgets
    dans la fenêtre utilise la méthode **grid()** décrite à la page .
-   Lignes 15-17 : Le code des couleurs est mémorisé dans une simple
    liste.
-   Ligne 18 : La dernière instruction du constructeur démarre
    l'application. Si vous préférez démarrer l'application
    indépendamment de sa création, vous devez supprimer cette ligne, et
    reporter l'appel à **mainloop()** au niveau principal du programme,
    en ajoutant une instruction : `f.root.mainloop()` à la ligne 71.
-   Lignes 20 à 30 : Le dessin de la résistance se compose d'une ligne
    et d'un premier rectangle gris clair, pour le corps de la résistance
    et ses deux fils. Trois autres rectangles figureront les bandes
    colorées que le programme devra modifier en fonction des entrées de
    l'utilisateur. Ces bandes sont noires au départ ; elles sont
    référencées dans la liste **self.ligne**.
-   Lignes 32 à 53 : Ces lignes contiennent l'essentiel de la
    fonctionnalité du programme. L'entrée brute fournie par
    l'utilisateur est acceptée sous la forme d'une chaîne de
    caractères.\
     À la ligne 36, on essaie de convertir cette chaîne en une valeur
    numérique de type *float*. Si la conversion échoue, on mémorise
    l'erreur. Si l'on dispose bien d'une valeur numérique, on vérifie
    ensuite qu'elle se situe effectivement dans l'intervalle autorisé
    (de 10 Ω à 10^11^ Ω). Si une erreur est détectée, on signale à
    l'utilisateur que son entrée est incorrecte en colorant de rouge le
    fond du champ d'entrée, qui est ensuite vidé de son contenu (lignes
    55 à 61).
-   Lignes 45-46 : Les mathématiques viennent à notre secours pour
    extraire de la valeur numérique son ordre de grandeur (c'est-à-dire
    l'exposant de 10 le plus proche). Veuillez consulter un ouvrage de
    mathématiques pour de plus amples explications concernant les
    logarithmes.
-   Lignes 47-48 : Une fois connu l'ordre de grandeur, il devient
    relativement facile d'extraire du nombre traité ses deux premiers
    chiffres significatifs. Exemple : supposons que la valeur entrée
    soit 31687. Le logarithme de ce nombre est 4,50088... dont la partie
    entière (4) nous donne l'ordre de grandeur de la valeur entrée (soit
    10^4^). Pour extraire de celle-ci son premier chiffre significatif,
    il suffit de la diviser par 10^4^, soit 10000, et de conserver
    seulement la partie entière du résultat (3).
-   Lignes 49 à 51 : Le résultat de la division effectuée dans le
    paragraphe précédent est 3,1687. Nous récupérons la partie décimale
    de ce nombre à la ligne 49, soit 0,1687 dans notre exemple. Si nous
    le multiplions par dix, ce nouveau résultat comporte une partie
    entière qui n'est rien d'autre que notre second chiffre significatif
    (1 dans notre exemple).\
     Nous pourrions facilement extraire ce dernier chiffre, mais puisque
    c'est le dernier, nous souhaitons encore qu'il soit correctement
    arrondi. Pour ce faire, il suffit d'ajouter une demi unité au
    produit de la multiplication par dix, avant d'en extraire la valeur
    entière. Dans notre exemple, en effet, ce calcul donnera donc
    1,687 + 0,5 = 2,187 , dont la partie entière (2) est bien la valeur
    arrondie recherchée.
-   Ligne 53 : Le nombre de zéros à accoler aux deux chiffres
    significatifs correspond au calcul de l'ordre de grandeur. Il suffit
    de retirer une unité au logarithme.
-   Ligne 56 : Pour attribuer une nouvelle couleur à un objet déjà
    dessiné dans un canevas, on utilise la méthode **itemconfigure()**.
    Nous utilisons donc cette méthode pour modifier l'option **fill** de
    chacune des bandes colorées, en utilisant les noms de couleur
    extraits de la liste **self.cc** grâce à aux trois indices
    **li[1]**, **li[2]** et **li[3]** qui contiennent les 3 chiffres
    correspondants.

Exercices

.Modifiez le script ci-dessus de telle manière que le fond d'image
devienne bleu clair (*light blue*), que le corps de la résistance
devienne beige (*beige*), que le fil de cette résistance soit plus fin,
et que les bandes colorées indiquant la valeur soient plus larges.

.Modifiez le script ci-dessus de telle manière que l'image dessinée soit
deux fois plus grande.

.Modifiez le script ci-dessus de
telle manière qu'il devienne possible d'entrer aussi des valeurs de
résistances comprises entre 1 et 10 **Ω**. Pour ces valeurs, le premier
anneau coloré devra rester noir, les deux autres indiqueront la valeur
en **Ω** et dixièmes d'**Ω**.

.Modifiez le script ci-dessus de telle façon que le bouton « Montrer »
ne soit plus nécessaire. Dans votre script modifié, il suffira de
frapper \<*Enter*\> après avoir entré la valeur de la résistance, pour
que l'affichage s'active.

.Modifiez le script ci-dessus de telle manière que les trois bandes
colorées redeviennent noires dans les cas où l'utilisateur fournit une
entrée inacceptable.

