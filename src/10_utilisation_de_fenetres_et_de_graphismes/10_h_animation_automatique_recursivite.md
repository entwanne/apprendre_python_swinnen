## 10-H - Animation automatique - Récursivité

Pour conclure cette première prise de
contact avec l'interface graphique tkinter, voici un dernier
exemple d'animation, qui fonctionne cette fois de manière
autonome dès qu'on l'a mise en
marche.



```python
from tkinter import *
 
# définition des gestionnaires
# d'événements :
 
def move():
  "déplacement de la balle"
  global x1, y1, dx, dy, flag
  x1, y1 = x1 +dx, y1 + dy
  if x1 >210:
      x1, dx, dy = 210, 0, 15
  if y1 >210:
      y1, dx, dy = 210, -15, 0
  if x1 <10:
      x1, dx, dy = 10, 0, -15
  if y1 <10:
      y1, dx, dy = 10, 15, 0
  can1.coords(oval1,x1,y1,x1+30,y1+30)
  if flag >0: 
      fen1.after(50,move)      # => boucler, après 50 millisecondes
 
def stop_it():
  "arrêt de l'animation"
  global flag	  
  flag =0
 
def start_it():
  "démarrage de l'animation"
  global flag
  if flag ==0:	     # pour ne lancer qu'une seule boucle
     flag =1
     move()
 
#========== Programme principal =============
 
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10        # coordonnées initiales
dx, dy = 15, 0		 # 'pas' du déplacement
flag =0 	   # commutateur
 
# Création du widget principal ("parent") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# création des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=250, width=250)
can1.pack(side=LEFT, padx =5, pady =5)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
bou1 = Button(fen1,text='Quitter', width =8, command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Démarrer', width =8, command=start_it)
bou2.pack()
bou3 = Button(fen1, text='Arrêter', width =8, command=stop_it)
bou3.pack()
# démarrage du réceptionnaire d'événements (boucle principale) :
fen1.mainloop()
```



La seule nouveauté mise en œuvre dans ce script se trouve tout à la fin
de la définition de la fonction **move()** : vous y noterez
l'utilisation de la méthode **after()**. Cette méthode peut s'appliquer
à un widget quelconque. Elle déclenche l'appel d'une fonction *après
qu'un certain laps de temps se soit écoulé*. Ainsi par exemple, `window.after(200,qqc)` déclenche pour le
widget **window** un appel de la fonction **qqc()** après une pause de
200 millisecondes.

Dans notre script, la fonction qui est appelée par la méthode
**after()** est la fonction **move()** elle-même. Nous utilisons donc
ici pour la première fois une technique de programmation très puissante,
que l'on appelle *récursivité*. Pour faire simple, nous dirons que la
récursivité est ce qui se passe lorsqu'une fonction s'appelle elle-même.
On obtient bien évidemment ainsi un bouclage, qui peut se perpétuer
indéfiniment si l'on ne prévoit pas aussi un moyen pour l'interrompre.

Voyons comment cela fonctionne dans notre exemple.

La fonction **move()** est invoquée une première fois lorsque l'on
clique sur le bouton « Démarrer ». Elle effectue son travail
(c'est-à-dire positionner la balle). Ensuite, par l'intermédiaire de la
méthode **after()**, elle s'invoque elle-même après une petite pause.
Elle repart donc pour un second tour, puis s'invoque elle-même à
nouveau, et ainsi de suite indéfiniment...

C'est du moins ce qui se passerait si nous n'avions pas pris la
précaution de placer quelque part dans la boucle une instruction de
sortie. En l'occurrence, il s'agit d'un simple test conditionnel : à
chaque itération de la boucle, nous examinons le contenu de la variable
**flag** à l'aide d'une instruction **if**. Si le contenu de la variable
**flag** est zéro, alors le bouclage ne s'effectue plus et l'animation
s'arrête. Remarquez que nous avons pris la précaution de définir
**flag** comme une variable globale. Ainsi nous pouvons aisément changer
sa valeur à l'aide d'autres fonctions, en l'occurrence celles que nous
avons associées aux boutons « Démarrer » et « Arrêter ».

Nous obtenons ainsi un mécanisme simple pour lancer ou arrêter notre
animation : un premier clic sur le bouton « Démarrer » assigne une
valeur non-nulle à la variable **flag**, puis provoque immédiatement un
premier appel de la fonction **move()**. Celle-ci s'exécute, puis
continue ensuite à s'appeler elle-même toutes les 50 millisecondes, tant
que **flag** ne revient pas à zéro. Si l'on continue à cliquer sur le
bouton « Démarrer », la fonction **move()** ne peut plus être appelée,
parce que la valeur de **flag** vaut désormais 1. On évite ainsi le
démarrage de plusieurs boucles concurrentes.

Le bouton « Arrêter » remet **flag** à zéro, et la boucle s'interrompt.

Exercices

.Dans la fonction **start\_it()**, supprimez l'instruction `if flag == 0: `(et l'indentation des deux
lignes suivantes). Que se passe-t-il ? (Cliquez plusieurs fois sur le
bouton « Démarrer ».)\
 Tâchez d'exprimer le plus clairement possible votre explication des
faits observés.

.Modifiez le programme de telle façon que la balle change de couleur à
chaque « virage ».

.Modifiez le programme de telle façon que la balle effectue des
mouvements obliques comme une bille de billard qui rebondit sur les
bandes (« en zig-zag »).

.Modifiez le programme de manière à obtenir d'autres mouvements. Tâchez
par exemple d'obtenir un mouvement circulaire (comme dans les exercices
de la page ).

.Modifiez ce programme, ou bien écrivez-en un autre similaire, de
manière à simuler le mouvement d'une balle qui tombe (sous l'effet de la
pesanteur), et rebondit sur le sol. Attention : il s'agit cette fois de
mouvements accélérés !

.À partir des scripts précédents, vous pouvez à présent écrire un
programme de jeu fonctionnant de la manière suivante : une balle se
déplace au hasard sur un canevas, à vitesse faible. Le joueur doit
essayer de cliquer sur cette balle à l'aide de la souris. S'il y arrive,
il gagne un point, mais la balle se déplace désormais un peu plus vite,
et ainsi de suite. Arrêter le jeu après un certain nombre de clics et
afficher le score atteint.

.Variante du jeu précédent : chaque fois que le joueur parvient à «
l'attraper », la balle devient plus petite (elle peut également changer
de couleur).

.Écrivez un programme dans lequel évoluent plusieurs balles de couleurs
différentes, qui rebondissent les unes sur les autres ainsi que sur les
parois.

.Perfectionnez le jeu des précédents exercices en y intégrant
l'algorithme ci-dessus. Il s'agit à présent pour le joueur de cliquer
seulement sur la balle rouge. Un clic erroné (sur une balle d'une autre
couleur) lui fait perdre des points.

.Écrivez un programme qui simule le mouvement de deux planètes tournant
autour du soleil sur des orbites circulaires différentes (ou deux
électrons tournant autour d'un noyau d'atome...).

.Écrivez un programme pour le jeu du serpent : un « serpent » (constitué
en fait d'une courte ligne de carrés) se déplace sur le canevas dans
l'une des 4 directions : droite, gauche, haut, bas. Le joueur peut à
tout moment changer la direction suivie par le serpent à l'aide des
touches fléchées du clavier. Sur le canevas se trouvent également des «
proies » (des petits cercles fixes disposés au hasard). Il faut diriger
le serpent de manière à ce qu'il « mange » les proies sans arriver en
contact avec les bords du canevas. À chaque fois qu'une proie est
mangée, le serpent s'allonge d'un carré, le joueur gagne un point, et
une nouvelle proie apparaît ailleurs. La partie s'arrête lorsque le
serpent touche l'une des parois, ou lorsqu'il a atteint une certaine
taille.

.Perfectionnement du jeu précédent : la
partie s'arrête également si le serpent « se recoupe
».

