## 15-D - Curseurs : un widget composite

Dans l'exercice précédent, vous avez construit un nouveau type de widget
que vous avez sauvegardé dans le module **oscillo.py**. Conservez
soigneusement ce module, car vous l'intégrerez bientôt dans un projet
plus complexe.

Pour l'instant, vous allez construire un autre widget, plus interactif
cette fois. Il s'agira d'une sorte de panneau de contrôle comportant
trois curseurs de réglage et une case à cocher. Comme le précédent, ce
widget est destiné à être réutilisé dans une application de synthèse.

### 15-D-1 - Présentation du widget Scale {#article.xml#Ld0e46668 .TitreSection2}



![](images/image42.png)



Commençons d'abord par découvrir un widget de base, que nous n'avions
pas encore utilisé jusqu'ici : le widget Scale se présente comme un
curseur qui coulisse devant une échelle. Il permet à l'utilisateur de
choisir rapidement la valeur d'un paramètre quelconque, d'une manière
très attrayante.

Le petit script ci-dessous vous montre comment le paramétrer et
l'utiliser dans une fenêtre :



```python
from tkinter import *
 
def updateLabel(x):
  lab.configure(text='Valeur actuelle = ' + str(x))
 
root = Tk()
Scale(root, length=250, orient=HORIZONTAL, label ='Réglage :',
    troughcolor ='dark grey', sliderlength =20,
    showvalue =0, from_=-25, to=125, tickinterval =25,
    command=updateLabel).pack()
lab = Label(root)
lab.pack()
 
root.mainloop()
```



Ces lignes ne nécessitent guère de commentaires.

Vous pouvez créer des widgets **Scale** de n'importe quelle taille
(option **length**), en orientation horizontale (comme dans notre
exemple) ou verticale (option **orient = VERTICAL**).\
 Les options **from\_** (attention : n'oubliez pas le caractère
'souligné', lequel est nécessaire afin d'éviter la confusion avec le mot
réservé **from** !) et **to** définissent la plage de réglage.
L'intervalle entre les repères numériques est défini dans l'option
**tickinterval**, etc.

La fonction désignée dans l'option **command** est appelée
automatiquement chaque fois que le curseur est déplacé, et la position
actuelle du curseur par rapport à l'échelle lui est transmise en
argument. Il est donc très facile d'utiliser cette valeur pour effectuer
un traitement quelconque. Considérez par exemple le paramètre **x** de
la fonction **updateLabel()**, dans notre exemple.

Le widget **Scale** constitue une interface très intuitive et attrayante
pour proposer différents réglages aux utilisateurs de vos programmes.
Nous allons à présent l'incorporer en plusieurs exemplaires dans une
nouvelle classe de widget : un panneau de contrôle destiné à choisir la
fréquence, la phase et l'amplitude pour un mouvement vibratoire, dont
nous afficherons ensuite le graphique élongation/temps à l'aide du
widget **oscilloGraphe** construit dans les pages précédentes.

### 15-D-2 - Construction d'un panneau de contrôle à trois curseurs {#article.xml#Ld0e46872 .TitreSection2}

Comme le précédent, le script que nous décrivons ci-dessous est destiné
à être sauvegardé dans un module, que vous nommerez cette fois
**curseurs.py**. Les classes que vous sauvegardez ainsi seront
réutilisées (par importation) dans une application de synthèse que nous
décrirons un peu plus loin[^note_77].
Nous attirons votre attention sur le fait que le code ci-dessous peut
être raccourci de différentes manières (nous y reviendrons). Nous ne
l'avons pas optimisé d'emblée, parce que cela nécessiterait d'y
incorporer un concept supplémentaire (les *expressions lambda*), ce que
nous préférons éviter pour l'instant.



![](images/image43.png)



Vous savez déjà que les lignes de code placées à la fin du script
permettent de tester son fonctionnement. Vous devriez obtenir une
fenêtre semblable à celle-ci :



```python
from tkinter import *
from math import pi
 
class ChoixVibra(Frame):
  """Curseurs pour choisir fréquence, phase & amplitude d'une vibration"""
  def __init__(self, boss =None, coul ='red'):
      Frame.__init__(self)	# constructeur de la classe parente
      # Initialisation de quelques attributs d'instance :
      self.freq, self.phase, self.ampl, self.coul = 0, 0, 0, coul
      # Variable d'état de la case à cocher :
      self.chk = IntVar()	   # 'objet-variable' tkinter	     
      Checkbutton(self, text='Afficher', variable=self.chk,
	  fg = self.coul, command = self.setCurve).pack(side=LEFT)
      # Définition des 3 widgets curseurs :
      Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,
	label ='Fréquence (Hz) :', from_=1., to=9., tickinterval =2,
	resolution =0.25,
	showvalue =0, command = self.setFrequency).pack(side=LEFT)
      Scale(self, length=150, orient=HORIZONTAL, sliderlength =15,
	label ='Phase (degrés) :', from_=-180, to=180, tickinterval =90,
	showvalue =0, command = self.setPhase).pack(side=LEFT)
      Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,
	label ='Amplitude :', from_=1, to=9, tickinterval =2,
	showvalue =0, command = self.setAmplitude).pack(side=LEFT)
 
  def setCurve(self):
      self.event_generate('<Control-Z>')
 
  def setFrequency(self, f):
      self.freq = float(f)
      self.event_generate('<Control-Z>')
 
  def setPhase(self, p):
      pp =float(p)
      self.phase = pp*2*pi/360	      # conversion degrés -> radians
      self.event_generate('<Control-Z>')
 
  def setAmplitude(self, a):
      self.ampl = float(a)
      self.event_generate('<Control-Z>')
 
#### Code pour tester la classe : ###
 
if __name__ == '__main__':
  def afficherTout(event=None):
      lab.configure(text = '%s - %s - %s - %s' %
	    (fra.chk.get(), fra.freq, fra.phase, fra.ampl))	      
  root = Tk()
  fra = ChoixVibra(root,'navy')
  fra.pack(side =TOP)
  lab = Label(root, text ='test')
  lab.pack()
  root.bind('<Control-Z>', afficherTout)
  root.mainloop()
```



Ce panneau de contrôle permettra à vos utilisateurs de régler aisément
la valeur des paramètres indiqués (fréquence, phase et amplitude),
lesquels pourront alors servir à commander l'affichage de graphiques
élongation/temps dans un widget de la classe **OscilloGraphe()**
construite précédemment, comme nous le montrerons dans l'application de
synthèse.

#### 15-D-2-A - Commentaires {#article.xml#Ld0e47744 .TitreSection3}

-   Ligne 6 : La méthode « constructeur » utilise un paramètre optionnel
    **coul**. Ce paramètre permettra de choisir une couleur pour le
    graphique soumis au contrôle du widget. Le paramètre **boss** sert à
    réceptionner la référence d'une fenêtre maîtresse éventuelle (voir
    plus loin).
-   Ligne 7 : Activation du constructeur de la classe parente (pour
    hériter sa fonctionnalité).
-   Ligne 9 : Déclaration de quelques variables d'instance. Leurs vraies
    valeurs seront déterminées par les méthodes des lignes 29 à 40
    (gestionnaires d'événements).
-   Ligne 11 : Cette instruction instancie un objet de la classe
    **IntVar()**, laquelle fait partie du module tkinter au même titre
    que les classes similaires **DoubleVar()**, **StringVar()** et
    **BooleanVar()**. Toutes ces classes permettent de définir des
    *variables tkinter*, lesquels sont en fait des objets, mais qui se
    comportent comme des variables à l'intérieur des widgets tkinter
    (voir ci-après).\
     Ainsi l'objet référencé dans **self.chk** contient l'équivalent
    d'une variable de type entier, dans un format utilisable par
    tkinter. Pour accéder à sa valeur depuis Python, il faut utiliser
    des méthodes spécifiques de cette classe d'objets : la méthode
    **set()** permet de lui assigner une valeur, et la méthode **get()**
    permet de la récupérer (ce que l'on mettra en pratique à la ligne
    47).
-   Ligne 12 : L'option **variable** de l'objet **checkbutton** est
    associée à la *variable tkinter* définie à la ligne précédente. Nous
    ne pouvons pas référencer directement une variable ordinaire dans la
    définition d'un widget tkinter, parce que tkinter lui-même est écrit
    dans un langage qui n'utilise pas les mêmes conventions que Python
    pour formater ses variables. Les objets construits à partir des
    classes de *variables tkinter* sont donc nécessaires pour assurer
    l'interface.
-   Ligne 13 : L'option **command** désigne la méthode que le système
    doit invoquer lorsque l'utilisateur effectue un clic de souris dans
    la case à cocher.
-   Lignes 14 à 24 : Ces lignes définissent les trois widgets curseurs,
    en trois instructions similaires. Il serait plus élégant de
    programmer tout ceci en une seule instruction, répétée trois fois à
    l'aide d'une boucle. Cela nécessiterait cependant de faire appel à
    un concept que nous n'avons pas encore expliqué (les *fonctions ou
    expressionslamdba*), et la définition du gestionnaire d'événements
    associé à ces widgets deviendrait elle aussi plus complexe.
    Conservons donc pour cette fois des instructions séparées : nous
    nous efforcerons d'améliorer tout cela plus tard.
-   Lignes 26 à 40 : Les 4 widgets définis dans les lignes précédentes
    possèdent chacun une option **command**. Pour chacun d'eux, la
    méthode invoquée dans cette option **command** est différente : la
    case à cocher active la méthode **setCurve()**, le premier curseur
    active la méthode **setFrequency()**, le second curseur active la
    méthode **setPhase()**, et le troisième curseur active la méthode
    **setAmplitude()**. Remarquez bien au passage que l'option
    **command** des widgets **Scale** transmet un argument à la méthode
    associée (la position actuelle du curseur), alors que la même option
    **command** ne transmet rien dans le cas du widget **Checkbutton.**\
    \
     Ces 4 méthodes (qui sont donc les gestionnaires des événements
    produits par la case à cocher et les trois curseurs) provoquent
    elles-mêmes chacune l'émission d'un nouvel *événement*[^note_78],
    en faisant appel à la méthode **event\_generate()**.\
    \
     Lorsque cette méthode est invoquée, Python envoie au système
    d'exploitation exactement le même message-événement que celui qui se
    produirait si l'utilisateur enfonçait simultanément les touches
    \<Ctrl\>, \<Maj\> et \<Z\> de son clavier.\
     Nous produisons ainsi un message-événement bien particulier, qui
    peut être détecté et traité par un gestionnaire d'événement associé
    à un autre widget (voir page suivante). De cette manière, nous
    mettons en place un véritable système de communication entre widgets
    : chaque fois que l'utilisateur exerce une action sur notre panneau
    de contrôle, celui-ci génère un événement spécifique, qui signale
    cette action à l'attention des autres widgets présents.\
    \
     Note : nous aurions pu choisir une autre combinaison de touches (ou
    même carrément un autre type d'événement). Notre choix s'est porté
    sur celle-ci parce qu'il y a vraiment très peu de chances que
    l'utilisateur s'en serve alors qu'il examine notre programme. Nous
    pourrons cependant produire nous-mêmes un tel événement au clavier à
    titre de test, lorsque le moment sera venu de vérifier le
    gestionnaire de cet événement, que nous mettrons en place par
    ailleurs.\
-   Lignes 42 à 54 : Comme nous l'avions déjà fait pour **oscillo.py**,
    nous complétons ce nouveau module par quelques lignes de code au
    niveau principal. Ces lignes permettent de tester le bon
    fonctionnement de la classe : elles ne s'exécutent que si on lance
    le module directement, comme une application à part entière. Veillez
    à utiliser vous-même cette technique dans vos propres modules, car
    elle constitue une bonne pratique de programmation : l'utilisateur
    de modules construits ainsi peut en effet (re)découvrir très
    aisément leur fonctionnalité (en les exécutant) et la manière de
    s'en servir (en analysant ces quelques lignes de code).\
    \
     Dans ces lignes de test, nous construisons une fenêtre principale
    **root** qui contient deux widgets : un widget de la nouvelle classe
    **ChoixVibra()** et un widget de la classe **Label()**.\
    \
     À la ligne 53, nous associons à la fenêtre principale un
    gestionnaire d'événement : tout événement du type spécifié déclenche
    désormais un appel de la fonction **afficherTout()**.\
     Cette fonction est donc notre gestionnaire d'événement spécialisé,
    qui est sollicité chaque fois qu'un événement de type \<Maj-Ctrl-Z\>
    est détecté par le système d'exploitation.\
    \
     Comme nous l'avons déjà expliqué plus haut, nous avons fait en
    sorte que de tels événements soient produits par les objets de la
    classe **ChoixVibra()**, chaque fois que l'utilisateur modifie
    l'état de l'un ou l'autre des trois curseurs, ou celui de la case à
    cocher.
-   Conçue seulement pour effectuer un test, la fonction
    **afficherTout()** ne fait rien d'autre que provoquer l'affichage
    des valeurs des variables associées à chacun de nos quatre widgets,
    en (re)configurant l'option **text** d'un widget de classe
    **Label()**.
-   Ligne 47, expression `fra.chk.get()` : nous avons vu plus
    haut que la variable mémorisant l'état de la case à cocher est un
    objet-variable tkinter. Python ne peut pas lire directement le
    contenu d'une telle variable, qui est en réalité un objet-interface.
    Pour en extraire la valeur, il faut donc faire usage d'une méthode
    spécifique de cette classe d'objets : la méthode **get()**.

#### 15-D-2-B - Propagation des événements {#article.xml#Ld0e47918 .TitreSection3}

Le mécanisme de communication décrit ci-dessus respecte la hiérarchie de
classes des widgets. Vous aurez noté que la méthode qui déclenche
l'événement est associée au widget dont nous sommes en train de définir
la classe, par l'intermédiaire de self. En général, un message-événement
est en effet associé à un widget particulier (par exemple, un clic de
souris sur un bouton est associé à ce bouton), ce qui signifie que le
système d'exploitation va d'abord examiner s'il existe un gestionnaire
pour ce type d'événement, qui soit lui aussi associé à ce widget. S'il
en existe un, c'est celui-là qui est activé, et la propagation du
message s'arrête. Sinon, le message-événement est « présenté »
successivement aux widgets maîtres, dans l'ordre hiérarchique, jusqu'à
ce qu'un gestionnaire d'événement soit trouvé, ou bien jusqu'à ce que la
fenêtre principale soit atteinte.

Les événements correspondant à des frappes sur le clavier (telle la
combinaison de touches `<Maj-Ctrl-Z>` utilisée dans notre
exercice) sont cependant toujours expédiés directement à la fenêtre
principale de l'application. Dans notre exemple, le gestionnaire de cet
événement doit donc être associé à la fenêtre **root**.

Exercices

.Votre nouveau widget hérite des propriétés de la classe **Frame()**.
Vous pouvez donc modifier son aspect en modifiant les options par défaut
de cette classe, à l'aide de la méthode **configure()**. Essayez par
exemple de faire en sorte que le panneau de contrôle soit entouré d'une
bordure de 4 pixels ayant l'aspect d'un sillon (`bd = 4, relief = GROOVE`). Si vous ne
comprenez pas bien ce qu'il faut faire, inspirez-vous du script
**oscillo.py** (ligne 10).

.Si l'on assigne la valeur 1 à l'option **showvalue** des widgets
**Scale()**, la position précise du curseur par rapport à l'échelle est
affichée en permanence. Activez donc cette fonctionnalité pour le
curseur qui contrôle le paramètre « phase ».

.L'option **troughcolor** des widgets **Scale()** permet de définir la
couleur de leur glissière. Utilisez cette option pour faire en sorte que
la couleur des glissières des 3 curseurs soit celle qui est utilisée
comme paramètre lors de l'instanciation de votre nouveau widget.

.Modifiez le script de telle manière que les widgets curseurs soient
écartés davantage les uns des autres (options **padx** et **pady** de la
méthode **pack()**).


[^note_77]: Vous pourriez bien évidemment aussi enregistrer plusieurs classes dans un même module.

[^note_78]: En fait, on devrait plutôt appeler cela un message (qui est lui-même la notification d'un événement). Veuillez relire à ce sujet les explications de la page : ***Programmes pilotés par des événements***.
