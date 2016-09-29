# 22 - Solutions des exercices

*Pour quelques exercices, nous ne fournissons pas de solution.
Efforcez-vous de les trouver sans aide, même si cela vous semble
difficile. C'est en effet en vous acharnant sur de tels problèmes que
vous apprendrez le mieux.*

Exercice 4.2 :



```python
>>> c = 0
>>> while c < 20:
...    c = c +1
...    print(c, "x 7 =", c*7)
```



ou encore :



```python
>>> c = 1
>>> while c <= 20:
...    print(c, "x 7 =", c*7)
...    c = c +1
```



Exercice 4.3 :



```python
>>> s = 1
>>> while s <= 16384:
...    print(s, "euro(s) =", s *1.65, "dollar(s)")
...    s = s *2
```



Exercice 4.4 :



```python
>>> a, c = 1, 1
>>> while c < 13:
...    print(a, end =' ?)
...    a, c = a *3, c+1
```



Exercice 4.6 :



```python
# Le nombre de secondes est fourni au départ : 
# (un grand nombre s'impose !) 
nsd = 12345678912 
 
# Nombre de secondes dans une journée : 
nspj = 3600 * 24 
# Nombre de secondes dans un an (soit 365 jours - 
# on ne tiendra pas compte des années bissextiles) : 
nspa = nspj * 365 
# Nombre de secondes dans un mois (en admettant 
# pour chaque mois une durée identique de 30 jours) : 
nspm = nspj * 30 
# Nombre d'années contenues dans la durée fournie : 
na = nsd // nspa    # division <entière> 
nsr = nsd % nspa    # n. de sec. restantes 
# Nombre de mois restants : 
nmo = nsr // nspm    # division <entière> 
nsr = nsr % nspm    # n. de sec. restantes 
# Nombre de jours restants : 
nj = nsr // nspj    # division <entière> 
nsr = nsr % nspj    # n. de sec. restantes 
# Nombre d'heures restantes : 
nh = nsr // 3600    # division <entière> 
nsr = nsr % 3600    # n. de sec. restantes 
# Nombre de minutes restantes : 
nmi = nsr // 60     # division <entière> 
nsr = nsr % 60	      # n. de sec. restantes 
 
print("Nombre de secondes à convertir :", nsd) 
print("Cette durée correspond à", na, "années de 365 jours, plus") 
print(nmo, "mois de 30 jours,", end=' ') 
print(nj, "jours,", end=' ') 
print(nh, "heures,", end=' ') 
print(nmi, "minutes et", end=' ') 
print(nsr, "secondes.")
```



Exercice 4.7 :



```python
# affichage des 20 premiers termes de la table par 7,
# avec signalement des multiples de 3 :
 
i = 1		# compteur : prendra successivement les valeurs de 1 à 20
while i < 21:
  # calcul du terme à afficher :
  t = i * 7
  # affichage sans saut à la ligne (utilisation de la virgule) :
  print(t, end =' ?)
  # ce terme est-il un multiple de 3 ? (utilisation de l'opérateur modulo) :
  if t % 3 == 0:
      print("*", end =' ?)   # affichage d'une astérisque dans ce cas
  i = i + 1		# incrémentation du compteur dans tous les cas
```



Exercice 5.1 :



```python
# Conversion degrés -> radians
# Rappel : un angle de 1 radian est un angle qui correspond à une portion
# de circonférence de longueur égale à celle du rayon.
# Puisque la circonférence vaut 2 pi R, un angle de 1 radian correspond
# à 360° / 2 pi , ou encore à 180° / pi
 
# Angle fourni au départ en degrés, minutes, secondes :
deg, min, sec  = 32, 13, 49
 
# Conversion des secondes en une fraction de minute : 
fm = sec/60 
# Conversion des minutes en une fraction de degré : 
fd = (min + fm)/60 
# Valeur de l'angle en degrés "décimalisés" : 
ang = deg + fd 
# Valeur de pi : 
pi = 3.14159265359 
# Valeur d'un radian en degrés : 
rad = 180 / pi 
# Conversion de l'angle en radians : 
arad = ang / rad 
# Affichage : 
print(deg, "°", min, "'", sec, '" =', arad, "radian(s)")
```



Exercice 5.3 :



```python
# Conversion °Fahrenheit <-> °Celsius
 
# A) Température fournie en °C :
tempC = 25
# Conversion en °Fahrenheit :
tempF = tempC * 1.8 + 32
# Affichage :
print(tempC, "°C =", tempF, "°F")
 
# B) Température fournie en °F :
tempF = 25
# Conversion en °Celsius :
tempC = (tempF - 32) / 1.8
# Affichage :
print(tempF, "°F =", tempC, "°C")
```



Exercice 5.5 :



```python
n = 1	# numéro de la case 
g = 1	    # nombre de grains à y déposer 
# Pour la variante, il suffit de définir g comme <float> 
# en remplaçant la ligne ci-dessus par :  g = 1. 
 
while n < 65 : 
  print(n, g) 
  n, g = n+1, g*2
```



Exercice 5.6 :



```python
# Recherche d'un caractère particulier dans une chaîne
 
# Chaîne fournie au départ :
ch = "Monty python flying circus"
# Caractère à rechercher :
cr = "e"
# Recherche proprement dite :
lc = len(ch)	# nombre de caractères à tester
i = 0	     # indice du caractère en cours d'examen
t = 0	     # "drapeau" à lever si le caractère recherché est présent 
while i < lc:
  if ch[i] == cr:
      t = 1
  i = i + 1
# Affichage :
print("Le caractère", cr, end =' ?)	 
if t == 1:
  print("est présent", end =' ?)
else:
  print("est inrouvable", end =' ?)
print("dans la chaîne", ch)
```



Exercice 5.8 :



```python
# Insertion d'un caractère d'espacement dans une chaîne
 
# Chaîne fournie au départ :
ch = "Véronique"
# Caractère à insérer :
cr = "*"
# Le nombre de caractères à insérer est inférieur d'une unité au
# nombre de caractères de la chaîne. On traitera donc celle-ci à
# partir de son second caractère (en omettant le premier).
lc = len(ch)	# nombre de caractères total
i = 1	     # indice du premier caractère à examiner (le second, en fait)
nch = ch[0]    # nouvelle chaîne à construire (contient déjà le premier car.)
while i < lc:
  nch = nch + cr + ch[i]
  i = i + 1
# Affichage :
print(nch)
```



Exercice 5.9 :



```python
# Inversion d'une chaîne de caractères
 
# Chaîne fournie au départ :
ch = "zorglub"
lc = len(ch)	 # nombre de caractères total
i = lc - 1     # le traitement commencera à partir du dernier caractère
nch = ""     # nouvelle chaîne à construire (vide au départ)
while i >= 0:
  nch = nch + ch[i]
  i = i - 1
# Affichage :
print(nch)
```



Exercice 5.11 :



```python
# Combinaison de deux listes en une seule
 
# Listes fournies au départ :
t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin',
    'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
# Nouvelle liste à construire (vide au départ) :
t3 = []
# Boucle de traitement :
i = 0
while i < len(t1):
  t3.append(t2[i])
  t3.append(t1[i])
  i = i + 1
 
# Affichage :
print(t3)
```



Exercice 5.12 :



```python
# Affichage des éléments d'une liste
 
# Liste fournie au départ :
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin',
    'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
# Affichage :
i = 0
while i < len(t2):
  print(t2[i], end =' ?)    
  i = i + 1
```



Exercice 5.13 :



```python
# Recherche du plus grand élément d'une liste
 
# Liste fournie au départ :
tt = [32, 5, 12, 8, 3, 75, 2, 15]
# Au fur et à mesure du traitement de la liste, on mémorisera dans
# la variable ci-dessous la valeur du plus grand élément déjà trouvé :
max = 0
# Examen de tous les éléments :
i = 0
while i < len(tt):
  if tt[i] > max:
      max = tt[i]      # mémorisation d'un nouveau maximum     
  i = i + 1
# Affichage :
print("Le plus grand élément de cette liste a la valeur", max)
```



Exercice 5.14 :



```python
# Séparation des nombres pairs et impairs
 
# Liste fournie au départ :
tt = [32, 5, 12, 8, 3, 75, 2, 15]
pairs = []
impairs = []
# Examen de tous les éléments :
i = 0
while i < len(tt):
  if tt[i] % 2 == 0:
      pairs.append(tt[i])
  else:
      impairs.append(tt[i])
  i = i + 1
# Affichage :
print("Nombres pairs :", pairs)
print("Nombres impairs :", impairs)
```



Exercice 6.1 :



```python
# Conversion de miles/heure en km/h et m/s
 
print("Veuillez entrer le nombre de miles parcourus en une heure : ", end =' ?)
ch = input()
mph = float(ch)        # conversion de la chaîne entrée en nombre réel
mps = mph * 1609 / 3600     # conversion en mètres par seconde
kmph = mph * 1.609	 # conversion en km/h
# affichage :
print(mph, "miles/heure =", kmph, "km/h, ou encore", mps, "m/s")
```



Exercice 6.2 :



```python
# Périmètre et Aire d'un triangle quelconque
 
from math import sqrt 
 
print("Veuillez entrer le côté a : ") 
a = float(input()) 
print("Veuillez entrer le côté b : ") 
b = float(input()) 
print("Veuillez entrer le côté c : ") 
c = float(input()) 
d = (a + b + c)/2	  # demi-périmètre 
s = sqrt(d*(d-a)*(d-b)*(d-c))	  # aire (suivant formule) 
 
print("Longueur des côtés =", a, b, c) 
print("Périmètre =", d*2, "Aire =", s)
```



Exercice 6.4 :



```python
# Entrée d'éléments dans une liste
 
tt = []        # Liste à compléter (vide au départ)
ch = "start"	   # valeur quelconque (mais non nulle) 
while ch != "":
  print("Veuillez entrer une valeur : ")
  ch = input()
  if ch != "":
      tt.append(float(ch))	# variante : tt.append(ch)    
 
# affichage de la liste :
print(tt)
```



Exercice 6.8 :



```python
# Traitement de nombres entiers compris entre deux limites
 
print("Veuillez entrer la limite inférieure :", end=' ') 
a = eval(input()) 
print("Veuillez entrer la limite supérieure :", end=' ') 
b = eval(input()) 
s = 0		 # somme recherchée (nulle au départ) 
# Parcours de la série des nombres compris entre a et b : 
n = a		 # nombre en cours de traitement 
while n <= b: 
  if n % 3 ==0 and n % 5 ==0:	    # variante : 'or' au lieu de 'and' 
      s = s + n 
  n = n + 1 
 
print("La somme recherchée vaut", s)
```



Exercice 6.9 :



```python
# Années bissextiles
 
print("Veuillez entrer l'année à tester :", end=' ') 
a = eval(input()) 
 
if a % 4 != 0: 
  # a n'est pas divisible par 4 -> année non bissextile 
  bs = 0      
else: 
  if a % 400 ==0: 
      # a divisible par 400 -> année bissextile 
      bs = 1 
  elif a % 100 ==0: 
      # a divisible par 100 -> année non bissextile 
      bs = 0 
  else: 
      # autres cas ou a est divisible par 4 -> année bissextile 
      bs = 1 
if bs ==1: 
  ch = "est" 
else: 
  ch = "n'est pas" 
print("L'année", a, ch, "bissextile.") 
 
########### Variante (proposée par Alex Misbah ) : ##### 
 
a = eval(input('Veuillez entrer une année :')) 
 
if (a%4==0) and ((a+0!=0) or (a@0==0)): 
  print(a,"est une année bissextile") 
else: 
  print(a,"n'est pas une année bissextile")
```



Exercice 6.11 : Calculs de triangles



```python
from sys import exit    # module contenant des fonctions système
 
print(""" 
Veuillez entrer les longueurs des 3 côtés 
(en séparant ces valeurs à l'aide de virgules) :""") 
a, b, c = eval(input()) 
# Il n'est possible de construire un triangle que si chaque côté 
# a une longueur inférieure à la somme des deux autres : 
if a < (b+c) and b < (a+c) and c < (a+b) : 
  print("Ces trois longueurs déterminent bien un triangle.") 
else: 
  print("Il est impossible de construire un tel triangle !") 
  exit()      # ainsi l'on n'ira pas plus loin. 
 
f = 0 
if a == b and b == c : 
  print("Ce triangle est équilatéral.") 
  f = 1 
elif a == b or b == c or c == a : 
  print("Ce triangle est isocèle.") 
  f = 1 
if a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b : 
  print("Ce triangle est rectangle.") 
  f = 1 
if f == 0 : 
  print("Ce triangle est quelconque.") 
```



Exercice 6.15 :



```python
# Notes de travaux scolaires
 
notes = []	  # liste à construire	
n = 2		 # valeur positive quelconque pour initier la boucle
while n >= 0 : 
  print("Entrez la note suivante, s.v.p. : ", end=' ') 
  n = float(input())	      # conversion de l'entrée en un nombre réel 
  if n < 0 : 
      print("OK. Terminé.") 
  else:    
      notes.append(n)	       # ajout d'une note à la liste 
      # Calculs divers sur les notes déjà entrées : 
      # valeurs minimale et maximale + total de toutes les notes. 
      min = 500 	 # valeur supérieure à toute note
      max, tot, i = 0, 0, 0	  
      nn = len(notes)	       # nombre de notes déjà entrées 
      while i < nn: 
      if notes[i] > max: 
	  max = notes[i] 
      if notes[i] < min: 
	  min = notes[i] 
      tot = tot + notes[i] 
      moy = tot/nn 
      i = i + 1 
      print(nn, "notes entrées. Max =", max, "Min =", min, "Moy =", moy)
```



Exercice 7.3 :



```python
from math import pi
 
def surfCercle(r):
  "Surface d'un cercle de rayon r"
  return pi * r**2
 
# test :
print(surfCercle(2.5))
```



Exercice 7.4 :



```python
def volBoite(x1, x2, x3):
  "Volume d'une boîte parallélipipédique"
  return x1 * x2 * x3
 
# test :
print(volBoite(5.2, 7.7, 3.3))
```



Exercice 7.5 :



```python
def maximum(n1, n2, n3): 
  "Renvoie le plus grand de trois nombres" 
  if n1 >= n2 and n1 >= n3: 
      return n1 
  elif n2 >= n1 and n2 >= n3: 
      return n2 
  else: 
      return n3 
 
# test : 
print(maximum(4.5, 5.7, 3.9)) 
print(maximum(8.2, 2.1, 6.7)) 
print(maximum(1.3, 4.8, 7.6))
```



Exercice 7.9 :



```python
def compteCar(ca, ch):
  "Renvoie le nombre de caractères ca trouvés dans la chaîne ch"
  i, tot = 0, 0
  while i < len(ch):
      if ch[i] == ca:
      tot = tot + 1
      i = i + 1
  return tot	
 
# test :
print(compteCar("e","Cette chaîne est un exemple"))
```



Exercice 7.10 :



```python
def indexMax(tt):
  "renvoie l'indice du plus grand élément de la liste tt"
  i, max = 0, 0
  while i < len(tt):
      if tt[i] > max :
      max, imax = tt[i], i
      i = i + 1    
  return imax
 
# test :
serie = [5, 8, 2, 1, 9, 3, 6, 4]
print(indexMax(serie))
```



Exercice 7.11 :



```python
def nomMois(n):
  "renvoie le nom du n-ième mois de l'année"
  mois = ['Janvier,', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
      'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
  return mois[n -1]	 # les indices sont numérotés à partir de zéro
 
# test :
print(nomMois(4))
```



Exercice 7.14 :



```python
def volBoite(x1 =10, x2 =10, x3 =10):
  "Volume d'une boîte parallélipipédique"
  return x1 * x2 * x3
 
# test :
print(volBoite())
print(volBoite(5.2))
print(volBoite(5.2, 3))
```



Exercice 7.15 :



```python
def volBoite(x1 =-1, x2 =-1, x3 =-1):
  "Volume d'une boîte parallélipipédique"
  if x1 == -1 :
      return x1      # aucun argument n'a été fourni
  elif x2 == -1 :
      return x1**3	# un seul argument -> boîte cubique
  elif x3 == -1 :
      return x1*x1*x2	   # deux arguments -> boîte prismatique
  else :
      return x1*x2*x3
 
# test :
print(volBoite()) 
print(volBoite(5.2)) 
print(volBoite(5.2, 3)) 
print(volBoite(5.2, 3, 7.4))
```



Exercice 7.16 :



```python
def changeCar(ch, ca1, ca2, debut =0, fin =-1):
  "Remplace tous les caractères ca1 par des ca2 dans la chaîne ch"
  if fin == -1:
      fin = len(ch)
  nch, i = "", 0	# nch : nouvelle chaîne à construire
  while i < len(ch) :
      if i >= debut and i <= fin and ch[i] == ca1:
      nch = nch + ca2
      else :
      nch = nch + ch[i]
      i = i + 1
  return nch
 
# test :
print((changeCar("Ceci est une toute petite phrase", " ", "*"))) 
print((changeCar("Ceci est une toute petite phrase", " ", "*", 8, 12))) 
print((changeCar("Ceci est une toute petite phrase", " ", "*", 12))) 
print((changeCar("Ceci est une toute petite phrase", " ", "*", fin =12))) 
```



Exercice 7.17 :



```python
def eleMax(lst, debut =0, fin =-1): 
  "renvoie le plus grand élément de la liste lst" 
  if fin == -1: 
      fin = len(lst) 
  max, i = 0, 0 
  while i < len(lst): 
      if i >= debut and i <= fin and lst[i] > max: 
      max = lst[i] 
      i = i + 1 
  return max 
 
# test : 
serie = [9, 3, 6, 1, 7, 5, 4, 8, 2] 
print(eleMax(serie)) 
print(eleMax(serie, 2, 5)) 
print(eleMax(serie, 2)) 
print(eleMax(serie, fin =3, debut =1)) 
```



Exercice 8.7 :



```python
from tkinter import *
 
# Coordonnées X,Y des 5 anneaux :
coord = [[20,30], [120,30], [220, 30], [70,80], [170,80]]
# Couleurs des 5 anneaux :
coul = ["red", "yellow", "blue", "green", "black"]
 
base = Tk()
can = Canvas(base, width =335, height =200, bg ="white")
can.pack()
bou = Button(base, text ="Quitter", command =base.quit)
bou.pack(side = RIGHT)
# Dessin des 5 anneaux :
i = 0
while i < 5:
  x1, y1 = coord[i][0], coord[i][1]
  can.create_oval(x1, y1, x1+100, y1 +100, width =2, outline =coul[i])
  i = i +1
```





![](images/olympe.gif)



Variante :



```python
from tkinter import *
 
# Dessin des 5 anneaux :
def dessineCercle(i):
  x1, y1 = coord[i][0], coord[i][1]
  can.create_oval(x1, y1, x1+100, y1 +100, width =2, outline =coul[i])
 
def a1():
  dessineCercle(0)
 
def a2():
  dessineCercle(1)
 
def a3():
  dessineCercle(2)
 
def a4():
  dessineCercle(3)
 
def a5():
  dessineCercle(4)
 
# Coordonnées X,Y des 5 anneaux :
coord = [[20,30], [120,30], [220, 30], [70,80], [170,80]]
# Couleurs des 5 anneaux :
coul = ["red", "yellow", "blue", "green", "black"]
 
base = Tk()
can = Canvas(base, width =335, height =200, bg ="white")
can.pack()
bou = Button(base, text ="Quitter", command =base.quit)
bou.pack(side = RIGHT)
 
# Installation des 5 boutons :	  
Button(base, text='1', command = a1).pack(side =LEFT)	 
Button(base, text='2', command = a2).pack(side =LEFT)	 
Button(base, text='3', command = a3).pack(side =LEFT)	 
Button(base, text='4', command = a4).pack(side =LEFT)	 
Button(base, text='5', command = a5).pack(side =LEFT)	 
base.mainloop()
```



Exercices 8.9 et 8.10 :



```python
# Dessin d'un damier, avec placement de pions au hasard
 
from tkinter import *
from random import randrange	   # générateur de nombres aléatoires
 
def damier():
  "dessiner dix lignes de carrés avec décalage alterné"
  y = 0
  while y < 10:
      if y % 2 == 0:	      # une fois sur deux, on
      x = 0	     # commencera la ligne de
      else:		 # carrés avec un décalage
      x = 1	     # de la taille d'un carré
      ligne_de_carres(x*c, y*c)
      y += 1
 
def ligne_de_carres(x, y):
  "dessiner une ligne de carrés, en partant de x, y" 
  i = 0
  while i < 10:
      can.create_rectangle(x, y, x+c, y+c, fill='navy')
      i += 1
      x += c*2		 # espacer les carrés
 
def cercle(x, y, r, coul):
  "dessiner un cercle de centre x,y et de rayon r"
  can.create_oval(x-r, y-r, x+r, y+r, fill=coul)
 
def ajouter_pion():
  "dessiner un pion au hasard sur le damier"
  # tirer au hasard les coordonnées du pion :
  x = c/2 + randrange(10) * c
  y = c/2 + randrange(10) * c
  cercle(x, y, c/3, 'red')
 
##### Programme principal : ############
 
# Tâchez de bien "paramétrer" vos programmes, comme nous l'avons
# fait dans ce script. Celui-ci peut en effet tracer des damiers
# de n'importe quelle taille en changeant seulement la valeur
# d'une seule variable, à savoir la dimension des carrés :
 
c = 30		  # taille des carrés
 
fen = Tk()
can = Canvas(fen, width =c*10, height =c*10, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(fen, text ='damier', command =damier)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(fen, text ='pions', command =ajouter_pion)
b2.pack(side =RIGHT, padx =3, pady =3)
fen.mainloop()#
```



Exercice 8.12 :



```python
# Simulation du phénomène de gravitation universelle
 
from tkinter import *
from math import sqrt
 
def distance(x1, y1, x2, y2):
  "distance séparant les points x1,y1 et x2,y2"
  d = sqrt((x2-x1)**2 + (y2-y1)**2)	 # théorème de Pythagore
  return  d
 
def forceG(m1, m2, di):
  "force de gravitation s'exerçant entre m1 et m2 pour une distance di"
  return m1*m2*6.67e-11/di**2	       # loi de Newton
 
def avance(n, gd, hb):
  "déplacement de l'astre n, de gauche à droite ou de haut en bas"
  global x, y, step
  # nouvelles coordonnées :
  x[n], y[n] = x[n] +gd, y[n] +hb
  # déplacement du dessin dans le canevas :
  can.coords(astre[n], x[n]-10, y[n]-10, x[n]+10, y[n]+10)
  # calcul de la nouvelle interdistance :
  di = distance(x[0], y[0], x[1], y[1])
  # conversion de la distance "écran" en distance "astronomique" :
  diA = di*1e9	     # (1 pixel => 1 million de km) 
  # calcul de la force de gravitation correspondante :
  f = forceG(m1, m2, diA)
  # affichage des nouvelles valeurs de distance et force :
  valDis.configure(text="Distance = " +str(diA) +" m")
  valFor.configure(text="Force = " +str(f) +" N")
  # adaptation du "pas" de déplacement en fonction de la distance :
  step = di/10
 
def gauche1():
  avance(0, -step, 0)
 
def droite1():
  avance(0, step, 0)
 
def haut1():
  avance(0, 0, -step)
 
def bas1():
  avance(0, 0, step)
 
def gauche2():
  avance(1, -step, 0)
 
def droite2():
  avance (1, step, 0)
 
def haut2():
  avance(1, 0, -step)
 
def bas2():
  avance(1, 0, step)
 
# Masses des deux astres :
m1 = 6e24      # (valeur de la masse de la terre, en kg)
m2 = 6e24      # 
astre = [0]*2	   # liste servant à mémoriser les références des dessins
x =[50., 350.]	    # liste des coord. X de chaque astre (à l'écran)
y =[100., 100.]    # liste des coord. Y de chaque astre
step =10      # "pas" de déplacement initial
 
# Construction de la fenêtre :
fen = Tk()
fen.title(' Gravitation universelle suivant Newton')
# Libellés :
valM1 = Label(fen, text="M1 = " +str(m1) +" kg")
valM1.grid(row =1, column =0)
valM2 = Label(fen, text="M2 = " +str(m2) +" kg")
valM2.grid(row =1, column =1)
valDis = Label(fen, text="Distance")
valDis.grid(row =3, column =0)
valFor = Label(fen, text="Force")
valFor.grid(row =3, column =1)
# Canevas avec le dessin des 2 astres:
can = Canvas(fen, bg ="light yellow", width =400, height =200)
can.grid(row =2, column =0, columnspan =2)
astre[0] = can.create_oval(x[0]-10, y[0]-10, x[0]+10, y[0]+10,
	     fill ="red", width =1)
astre[1] = can.create_oval(x[1]-10, y[1]-10, x[1]+10, y[1]+10,
	     fill ="blue", width =1)
# 2 groupes de 4 boutons, chacun installé dans un cadre (frame) :
fra1 = Frame(fen)
fra1.grid(row =4, column =0, sticky =W, padx =10)
Button(fra1, text="<-", fg ='red',command =gauche1).pack(side =LEFT)
Button(fra1, text="->", fg ='red', command =droite1).pack(side =LEFT)
Button(fra1, text="^", fg ='red', command =haut1).pack(side =LEFT)
Button(fra1, text="v", fg ='red', command =bas1).pack(side =LEFT)
fra2 = Frame(fen)
fra2.grid(row =4, column =1, sticky =E, padx =10)
Button(fra2, text="<-", fg ='blue', command =gauche2).pack(side =LEFT)
Button(fra2, text="->", fg ='blue', command =droite2).pack(side =LEFT)
Button(fra2, text="^", fg ='blue', command =haut2).pack(side =LEFT)
Button(fra2, text="v", fg ='blue', command =bas2).pack(side =LEFT)
 
fen.mainloop()
```





![](images/100000000000019C00000129BA738C0C.gif)



Exercice 8.16 :



```python
# Conversions de températures Fahrenheit <=> Celsius
 
from tkinter import *
 
def convFar(event):
  "valeur de cette température, exprimée en degrés Fahrenheit" 
  tF = eval(champTC.get())
  varTF.set(str(tF*1.8 +32))
 
def convCel(event):
  "valeur de cette température, exprimée en degrés Celsius" 
  tC = eval(champTF.get())
  varTC.set(str((tC-32)/1.8))
 
fen = Tk()
fen.title('Fahrenheit/Celsius')
 
Label(fen, text='Temp. Celsius :').grid(row =0, column =0)
# "variable tkinter" associée au champ d'entrée. Cet "objet-variable"
# assure l'interface entre TCL et Python (voir notes, page 165) :
varTC =StringVar()	 
champTC = Entry(fen, textvariable =varTC)
champTC.bind("<Return>", convFar)
champTC.grid(row =0, column =1)
# Initialisation du contenu de la variable tkinter :
varTC.set("100.0")
 
Label(fen, text='Temp. Fahrenheit :').grid(row =1, column =0) 
varTF =StringVar()
champTF = Entry(fen, textvariable =varTF)
champTF.bind("<Return>", convCel)
champTF.grid(row =1, column =1)
varTF.set("212.0")
 
fen.mainloop()
```





![](images/10000000000000E500000040EDF63C0B.gif)



Exercice 8.18 à 8.20 :



```python
# Cercles et courbes de Lissajous
 
from tkinter import *
from math import sin, cos
 
def move():    
  global ang, x, y
  # on mémorise les coordonnées précédentes avant de calculer les nouvelles :
  xp, yp = x, y
  # rotation d'un angle de 0.1 radian :
  ang = ang +.1 
  # sinus et cosinus de cet angle => coord. d'un point du cercle trigono.
  x, y = sin(ang), cos(ang)
  # Variante déterminant une courbe de Lissajous avec f1/f2 = 2/3 :
  # x, y = sin(2*ang), cos(3*ang)
  # mise à l'échelle (120 = rayon du cercle, (150,150) = centre du canevas)
  x, y = x*120 + 150, y*120 + 150
  can.coords(balle, x-10, y-10, x+10, y+10)
  can.create_line(xp, yp, x, y, fill ="blue")	  # trace la trajectoire
 
ang, x, y = 0., 150., 270.
fen = Tk()
fen.title('Courbes de Lissajous')
can = Canvas(fen, width =300, height=300, bg="white")
can.pack()
balle = can.create_oval(x-10, y-10, x+10, y+10, fill='red')
Button(fen, text='Go', command =move).pack()
fen.mainloop()
```





![](images/1000000000000138000001672D795CF3.gif)



Exercice 8.27 :



```python
# Chutes et rebonds
 
from tkinter import *
 
def move():
  global x, y, v, dx, dv, flag
  xp, yp = x, y       # mémorisation des coord. précédentes
  # déplacement horizontal :
  if x > 385 or x < 15 :   # rebond sur les parois latérales :
      dx = -dx	      # on inverse le déplacement
  x = x + dx
  # variation de la vitesse verticale (toujours vers le bas):
  v = v + dv
  # déplacement vertical (proportionnel à la vitesse)
  y = y + v	 
  if y > 240:		# niveau du sol à 240 pixels : 
      y = 240		#  défense d'aller + loin !
      v = -v	       # rebond : la vitesse s'inverse
  # on repositionne la balle :	 
  can.coords(balle, x-10, y-10, x+10, y+10)
  # on trace un bout de trajectoire :
  can.create_line(xp, yp, x, y, fill ='light grey')
  # ... et on remet ça jusqu'à plus soif :
  if flag > 0:
      fen.after(50,move)
 
def start():
  global flag
  flag = flag +1
  if flag == 1:
      move()
 
def stop():
  global flag
  flag =0
 
 
 
 
 
 
 
# initialisation des coordonnées, des vitesses et du témoin d'animation :   
x, y, v, dx, dv, flag  = 15, 15, 0, 6, 5, 0
 
fen = Tk()
fen.title(' Chutes et rebonds')
can = Canvas(fen, width =400, height=250, bg="white")
can.pack()
balle = can.create_oval(x-10, y-10, x+10, y+10, fill='red')
Button(fen, text='Start', command =start).pack(side =LEFT, padx =10)
Button(fen, text='Stop', command =stop).pack(side =LEFT)
Button(fen, text='Quitter', command =fen.quit).pack(side =RIGHT, padx =10)
fen.mainloop()
```





![](images/100000000000019B0000013539E38851.gif)



Exercice 8.33 (Jeu du serpent)

Nous ne fournissons ici qu'une première ébauche du script : le principe
d'animation du « serpent ». Si le cœur vous en dit, vous pouvez
continuer le développement pour en faire un véritable jeu, mais c'est du
travail ! :



```python
from tkinter import * 
 
# === Définition de quelques gestionnaires d'événements :
 
def start_it(): 
  "Démarrage de l'animation" 
  global flag 
  if flag ==0: 
      flag =1 
      move() 
 
def stop_it(): 
  "Arrêt de l'animation" 
  global flag 
  flag =0 
 
def go_left(event =None): 
  "délacement vers la gauche" 
  global dx, dy 
  dx, dy = -1, 0 
 
def go_right(event =None): 
  global dx, dy 
  dx, dy = 1, 0 
 
def go_up(event =None): 
  "déplacement vers le haut" 
  global dx, dy 
  dx, dy = 0, -1 
 
def go_down(event =None): 
  global dx, dy 
  dx, dy = 0, 1 
 
def move(): 
  "Animation du serpent par récursivité" 
  global flag 
  # Principe du mouvement opéré : on déplace le carré de queue, dont les 
  # caractéristiques sont mémorisées dans le premier élément de la liste 
  # <serp>, de manière à l'amener en avant du carré de tête, dont les 
  # caractéristiques sont mémorisées dans le dernier élément de la liste. 
  # On définit ainsi un nouveau carré de tête pour le serpent, dont on 
  # mémorise les caractéristiques en les ajoutant à la liste. 
  # Il ne reste plus qu'à effacer alors le premier élément de la liste, 
  # et ainsi de suite ... : 
  c = serp[0]	       # extraction des infos concernant le carré de queue 
  cq = c[0]	     # réf. de ce carré (coordonnées inutiles ici) 
  l =len(serp)	     # longueur actuelle du serpent (= n. de carrés) 
  c = serp[l-1]      # extraction des infos concernant le carré de tête 
  xt, yt = c[1], c[2]	   # coordonnées de ce carré 
  # Préparation du déplacement proprement dit. 
  # (cc est la taille du carré. dx & dy indiquent le sens du déplacement) : 
  xq, yq = xt+dx*cc, yt+dy*cc	       # coord. du nouveau carré de tête 
  # Vérification : a-t-on atteint les limites du canevas ? : 
  if xq<0 or xq>canX-cc or yq<0 or yq>canY-cc: 
      flag =0	       # => arrêt de l'animation 
      can.create_text(canX/2, 20, anchor =CENTER, text ="Perdu !!!", 
	      fill ="red", font="Arial 14 bold") 
  can.coords(cq, xq, yq, xq+cc, yq+cc)	  # déplacement effectif 
  serp.append([cq, xq, yq])	# mémorisation du nouveau carré de tête 
  del(serp[0])		# effacement (retrait de la liste) 
  # Appel récursif de la fonction par elle-même (=> boucle d'animation) : 
  if flag >0: 
      fen.after(50, move)    
 
# === Programme principal : ======== 
 
# Variables globales modifiables par certaines fonctions : 
flag =0 	# commutateur pour l'animation 
dx, dy = 1, 0	     # indicateurs pour le sens du déplacement 
 
# Autres variables globales :
canX, canY = 500, 500	 # dimensions du canevas 
x, y, cc = 100, 100, 15     # coordonnées et coté du premier carré 
 
# Création de l'espace de jeu (fenêtre, canevas, boutons ...) : 
fen =Tk() 
can =Canvas(fen, bg ='dark gray', height =canX, width =canY) 
can.pack(padx =10, pady =10) 
bou1 =Button(fen, text="Start", width =10, command =start_it) 
bou1.pack(side =LEFT) 
bou2 =Button(fen, text="Stop", width =10, command =stop_it) 
bou2.pack(side =LEFT) 
 
# Association de gestionnaires d'événements aux touches fléchées du clavier :
fen.bind("<Left>", go_left)	  # Attention : les événements clavier 
fen.bind("<Right>", go_right)	    # doivent toujours être associés à la 
fen.bind("<Up>", go_up)        # fenêtre principale, et non au canevas 
fen.bind("<Down>", go_down)	  # ou à un autre widget. 
 
# Création du serpent initial (= ligne de 5 carrés). 
# On mémorisera les infos concernant les carrés créés dans une liste de listes :
serp =[]	       # liste vide 
# Création et mémorisation des 5 carrés : le dernier (à droite) est la tête.
i =0 
while i <5: 
  carre =can.create_rectangle(x, y, x+cc, y+cc, fill="green") 
  # Pour chaque carré, on mémorise une petite sous-liste contenant
  # 3 éléments : la référence du carré et ses coordonnées de base :
  serp.append([carre, x, y]) 
  x =x+cc	   # le carré suivant sera un peu plus à droite 
  i =i+1 
 
fen.mainloop() 
```



Exercice 9.1 (éditeur simple, pour lire et écrire dans un fichier
**'**texte**'**) :



```python
def sansDC(ch): 
  "cette fonction renvoie la chaîne ch amputée de son dernier caractère" 
  nouv = "" 
  i, j = 0, len(ch) -1 
  while i < j: 
      nouv = nouv + ch[i] 
      i = i + 1 
  return nouv 
 
def ecrireDansFichier(): 
  of = open(nomF, 'a') 
  while 1: 
      ligne = input("entrez une ligne de texte (ou <Enter>) : ") 
      if ligne == '': 
      break 
      else: 
      of.write(ligne + '\n') 
  of.close() 
 
def lireDansFichier(): 
  of = open(nomF, 'r') 
  while 1: 
      ligne = of.readline() 
      if ligne == "": 
      break 
      # afficher en omettant le dernier caractère (= fin de ligne) : 
      print(sansDC(ligne)) 
  of.close() 
 
nomF = input('Nom du fichier à traiter : ') 
choix = input('Entrez "e" pour écrire, "c" pour consulter les données : ') 
 
if choix =='e': 
  ecrireDansFichier() 
else: 
  lireDansFichier()
```



Exercice 9.3 (génération des tables de multiplication de 2 à 30) :



```python
def tableMulti(n):
  # Fonction générant la table de multiplication par n (20 termes)
  # La table sera renvoyée sous forme d'une chaîne de caractères :
  i, ch = 0, ""
  while i < 20:
      i = i + 1
      ch = ch + str(i * n) + " "
  return ch
 
NomF = input("Nom du fichier à créer : ")
fichier = open(NomF, 'w')
 
# Génération des tables de 2 à 30 :
table = 2
while table < 31:
  fichier.write(tableMulti(table) + '\n')
  table = table + 1
fichier.close()
```



Exercice 9.4 :



```python
# Triplement des espaces dans un fichier texte.
# Ce script montre également comment modifier le contenu d'un fichier
# en le transférant d'abord tout entier dans une liste, puis en
# ré-enregistrant celle-ci après modifications
 
def triplerEspaces(ch):
  "fonction qui triple les espaces entre mots dans la chaîne ch"
  i, nouv = 0, ""
  while i < len(ch):
      if ch[i] == " ":
      nouv = nouv + "	"
      else:
      nouv = nouv + ch[i]
      i = i +1	  
  return nouv
 
NomF = input("Nom du fichier : ")
fichier = open(NomF, 'r+')	  # 'r+' = mode read/write
lignes = fichier.readlines()	    # lire toutes les lignes
 
n=0
while n < len(lignes):
  lignes[n] = triplerEspaces(lignes[n])
  n =n+1
 
fichier.seek(0) 	    # retour au début du fichier
fichier.writelines(lignes)	  # réenregistrement
fichier.close()
```



Exercice 9.5 :



```python
# Mise en forme de données numériques.
# Le fichier traité est un fichier texte dont chaque ligne contient un nombre
# réel (sans exposants et encodé sous la forme d'une chaîne de caractères)    
 
def valArrondie(ch):
  "représentation arrondie du nombre présenté dans la chaîne ch"
  f = float(ch)       # conversion de la chaîne en un nombre réel
  e = int(f + .5)     # conversion en entier (On ajoute d'abord
	      # 0.5 au réel pour l'arrondir correctement)
  return str(e)       # reconversion en chaîne de caractères
 
fiSource = input("Nom du fichier à traiter : ")
fiDest = input("Nom du fichier destinataire : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')
 
while 1:
  ligne = fs.readline()       # lecture d'une ligne du fichier
  if ligne == "" or ligne == "\n":
      break
  ligne = valArrondie(ligne)
  fd.write(ligne +"\n")
 
fd.close()
fs.close()
```



Exercice 9.6 :



```python
# Comparaison de deux fichiers, caractère par caractère :
 
fich1 = input("Nom du premier fichier : ")
fich2 = input("Nom du second fichier : ")
fi1 = open(fich1, 'r')
fi2 = open(fich2, 'r')
 
c, f = 0, 0	      # compteur de caractères et "drapeau" 
while 1:
  c = c + 1
  car1 = fi1.read(1)	  # lecture d'un caractère dans chacun
  car2 = fi2.read(1)	  # des deux fichiers
  if car1 =="" or car2 =="":
      break
  if car1 != car2 :
      f = 1
      break	     # différence trouvée
 
fi1.close()
fi2.close()
 
print("Ces 2 fichiers", end=' ') 
if f ==1: 
  print("diffèrent à partir du caractère n°", c) 
else: 
  print("sont identiques.")
```



Exercice 9.7 :



```python
# Combinaison de deux fichiers texte pour en faire un nouveau
 
fichA = input("Nom du premier fichier : ")
fichB = input("Nom du second fichier : ")
fichC = input("Nom du fichier destinataire : ")
fiA = open(fichA, 'r')
fiB = open(fichB, 'r')
fiC = open(fichC, 'w')
 
while 1:
  ligneA = fiA.readline()    
  ligneB = fiB.readline()
  if ligneA =="" and ligneB =="":
      break	     # On est arrivé à la fin des 2 fichiers
  if ligneA != "":
      fiC.write(ligneA)
  if ligneB != "":    
      fiC.write(ligneB)
 
fiA.close()
fiB.close()
fiC.close()
```



Exercice 9.8 :



```python
# Enregistrer les coordonnées des membres d'un club
 
def encodage():
  "renvoie la liste des valeurs entrées, ou une liste vide"
  print("*** Veuillez entrer les données (ou <Enter> pour terminer) :")
  while 1:
      nom = input("Nom : ")
      if nom == "":
      return []
      prenom = input("Prénom : ")
      rueNum = input("Adresse (N° et rue) : ")
      cPost = input("Code postal : ")
      local = input("Localité : ")
      tel = input("N° de téléphone : ")
      print(nom, prenom, rueNum, cPost, local, tel)
      ver = input("Entrez <Enter> si c'est correct, sinon <n> ")
      if ver == "":
      break
  return [nom, prenom, rueNum, cPost, local, tel]
 
def enregistrer(liste):
  "enregistre les données de la liste en les séparant par des <#>"
  i = 0
  while i < len(liste):
      of.write(liste[i] + "#")
      i = i + 1
  of.write("\n")	  # caractère de fin de ligne	 
 
nomF = input('Nom du fichier destinataire : ')
of = open(nomF, 'a')
while 1:
  tt = encodage()
  if tt == []:
      break
  enregistrer(tt)
 
of.close()
```



Exercice 9.9 :



```python
# Ajouter des informations dans le fichier du club
 
def traduire(ch):
  "convertir une ligne du fichier source en liste de données"
  dn = ""	   # chaîne temporaire pour extraire les données  
  tt = []	   # la liste à produire
  i = 0
  while i < len(ch):
      if ch[i] == "#":
      tt.append(dn)   # on ajoute la donnée à la liste, et   
      dn =""	  # on réinitialise la chaine temporaire
      else:
      dn = dn + ch[i]
      i = i + 1
  return tt
 
def encodage(tt):
  "renvoyer la liste tt, complétée avec la date de naissance et le sexe"
  print "*** Veuillez entrer les données (ou <Enter> pour terminer) :"
  # Affichage des données déjà présentes dans la liste :
  i = 0
  while i < len(tt):
      print(tt[i], end =' ?)
      i = i +1
  print()
  while 1:
      daNai = input("Date de naissance : ")
      sexe = input("Sexe (m ou f) : ")
      print(daNai, sexe)
      ver = input("Entrez <Enter> si c'est correct, sinon <n> ")
      if ver == "":
      break
  tt.append(daNai)
  tt.append(sexe)
  return tt
 
def enregistrer(tt):
  "enregistrer les données de la liste tt en les séparant par des <#>"
  i = 0
  while i < len(tt):
      fd.write(tt[i] + "#")
      i = i + 1
  fd.write("\n")      # caractère de fin de ligne
 
fSource = input('Nom du fichier source : ')
fDest = input('Nom du fichier destinataire : ')
fs = open(fSource, 'r')
fd = open(fDest, 'w')
while 1:
  ligne = fs.readline()      # lire une ligne du fichier source
  if ligne =="" or ligne =="\n":
      break
  liste = traduire(ligne)      # la convertir en une liste
  liste = encodage(liste)      # y ajouter les données supplémentaires
  enregistrer(liste)	      # sauvegarder dans fichier dest.
 
fd.close()
fs.close()
```



Exercice 9.10 :



```python
# Recherche de lignes particulières dans un fichier texte :
 
def chercheCP(ch):
  "recherche dans ch la portion de chaîne contenant le code postal"
  i, f, ns = 0, 0, 0	      # ns est un compteur de codes #
  cc = ""	       # chaîne à construire 
  while i < len(ch):
      if ch[i] =="#":
      ns = ns +1
      if ns ==3:	  # le CP se trouve après le 3e code #
	  f = 1 	 # variable "drapeau" (flag)
      elif ns ==4:	  # inutile de lire après le 4e code #
	  break
      elif f ==1:	   # le caractère lu fait partie du
      cc = cc + ch[i]	  # CP recherché -> on mémorise
      i = i +1
  return cc
 
nomF = input("Nom du fichier à traiter : ")
codeP = input("Code postal à rechercher : ")
fi = open(nomF, 'r')
while 1:
  ligne = fi.readline()
  if ligne =="":
      break
  if chercheCP(ligne) == codeP:
      print(ligne)
fi.close()
```



Exercice 10.2 (découpage d**'**une chaîne en fragments) :



```python
def decoupe(ch, n): 
  "découpage de la chaîne ch en une liste de fragments de n caractères" 
  d, f = 0, n	       # indices de début et de fin de fragment 
  tt = []	   # liste à construire 
  while d < len(ch): 
      if f > len(ch):	   # on ne peut pas découper au-delà de la fin 
      f = len(ch) 
      fr = ch[d:f]	# découpage d'un fragment 
      tt.append(fr)	 # ajout du fragment à la liste 
      d, f = f, f +n	  # indices suivants
  return tt 
 
def inverse(tt): 
  "rassemble les éléments de la liste tt dans l'ordre inverse" 
  ch = ""	   # chaîne à construire 
  i = len(tt)	       # on commence par la fin de la liste 
  while i > 0 : 
      i = i - 1      # le dernier élément possède l'indice n -1 
      ch = ch + tt[i] 
  return ch 
 
# Test : 
if __name__ == '__main__': 
  ch ="abcdefghijklmnopqrstuvwxyz123456789âêîôûàèìòùáéíóú" 
  liste = decoupe(ch, 5) 
  print("chaîne initiale :") 
  print(ch) 
  print("liste de fragments de 5 caractères :") 
  print(liste) 
  print("fragments rassemblés après inversion de la liste :") 
  print(inverse(liste))
```



Exercices 10.3 & 10.4 :



```python
# Rechercher l'indice d'un caractère donné dans une chaîne
 
def trouve(ch, car, deb=0): 
  "trouve l'indice du caractère car dans la chaîne ch" 
  i = deb 
  while i < len(ch): 
      if ch[i] == car: 
      return i	    # le caractère est trouvé -> on termine 
      i = i + 1 
  return -1	     # toute la chaîne a été scannée sans succès 
 
# Test : 
if __name__ == '__main__': 
  print(trouve("Coucou c'est moi", "z")) 
  print(trouve("Juliette & Roméo", "&")) 
  print(trouve("César & Cléopâtre", "r", 5))
```



Exercice 10.5 :



```python
# Comptage des occurrences d'un caractère donné dans une chaîne 
 
def compteCar(ch, car): 
  "trouve l'indice du caractère car dans la chaîne ch" 
  i, nc = 0, 0	      # initialisations 
  while i < len(ch): 
      if ch[i] == car: 
      nc = nc + 1	# caractère est trouvé -> on incrémente le compteur
      i = i + 1 
  return nc 
 
# Test : 
if __name__ == '__main__': 
  print(compteCar("ananas au jus", "a")) 
  print(compteCar("Gédéon est déjà là", "é")) 
  print(compteCar("Gédéon est déjà là", "à")) 
```



Exercice 10.6 :



```python
prefixes, suffixe = "JKLMNOP", "ack"
 
for p in prefixes:
  print(p + suffixe )
```



Exercice 10.7 :



```python
def compteMots(ch):
  "comptage du nombre de mots dans la chaîne ch"
  if len(ch) ==0:
      return 0
  nm = 1	  # la chaîne comporte au moins un mot	   
  for c in ch:
      if c == " ":	# il suffit de compter les espaces
      nm = nm + 1
  return nm
 
# Test :
if __name__ == '__main__': 
  print(compteMots("Les petits ruisseaux font les grandes rivières"))
```



Exercice 10.8 :



```python
def compteCar(ch, car): 
  "comptage du nombre de caractères <car> la chaîne <ch>" 
  if len(ch) ==0: 
      return 0 
  n =0 
  for c in ch: 
      if c == car: 
      n = n + 1 
  return n 
 
# Programme principal : 
 
def compteCarDeListe(chaine, serie): 
  "dans la chaine <ch>, comptage du nombre de caractères listés dans <serie>" 
  for cLi in serie: 
      nc =compteCar(chaine, cLi) 
      print("Caractère", cLi, ":", nc) 
 
 
# Test : 
if __name__ == '__main__': 
  txt ="René et Célimène étaient eux-mêmes nés à Noël de l'année dernière" 
  print(txt) 
  compteCarDeListe(txt, "eéèêë")
```



Exercice 10.9 :



```python
def estUnChiffre(car): 
  "renvoie <vrai> si le caractère 'car' est un chiffre" 
  if car in "0123456789": 
      return "vrai" 
  else: 
      return "faux" 
 
# Test : 
if __name__ == '__main__': 
  caracteres ="d75è8b0â1" 
  print("Caractères à tester :", caracteres) 
  for car in caracteres: 
      print(car, estUnChiffre(car)) 
```



Exercice 10.10 :



```python
def estUneMaj(car): 
  "renvoie <vrai> si le caractère 'car' est une majuscule" 
  if car in "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÉÈÊËÇÎÏÙÜÛÔÖ": 
      return True 
  else: 
      return False 
 
# Test : 
if __name__ == '__main__': 
  caracteres ="eÀçMöSÖÛmÇéùT" 
  print("Caractères à tester :", caracteres) 
  for car in caracteres: 
      print(car, estUneMaj(car)) 
```



Exercice 10.11 :



```python
def chaineListe(ch): 
  "convertit la chaîne ch en une liste de mots" 
  liste, ct = [], ""	      # ct est une chaîne temporaire 
  for c in ch:		 # examiner tous les caractères de ch 
      if c == " ":	    # lorsqu'on rencontre un espace,
      liste.append(ct)	  # on ajoute la chaîne temporaire à la liste 
      ct = ""	       # ... et on ré-initialise la chaîne temporaire 
      else: 
      # les autres caractères examinés sont ajoutés à la chaîne temp. : 
      ct = ct + c 
  # Ne pas oublier le mot restant après le dernier espace ! :	    
  if ct:	      # vérifier si ct n'est pas une chaîne vide 
      liste.append(ct) 
  return liste		 # renvoyer la liste ainsi construite 
 
# Tests : 
if __name__ == '__main__': 
  li = chaineListe("René est un garçon au caractère héroïque") 
  print(li) 
  for mot in li: 
      print(mot, "-", end=' ') 
  print(chaineListe(""))	  # doit renvoyer une liste vide 
```



Exercice 10.12 (utilise les deux fonctions définies dans les exercices
précédents) :



```python
from exercice_10_10 import estUneMaj 
from exercice_10_11 import chaineListe 
 
txt = "Le prénom de cette Dame est Élise" 
print("Phrase à tester :", txt) 
 
lst = chaineListe(txt)	      # convertir la phrase en une liste de mots 
 
for mot in lst: 	# analyser chacun des mots de la liste 
  prem = mot[0] 	 # extraction du premier caractère 
  if estUneMaj(prem):	       # test de majuscule 
      print(mot) 
 
# Variante plus compacte, utilisant la composition :
print("Variante :") 
for mot in lst: 
  if estUneMaj(mot[0]): 
      print(mot)
```



Exercice 10.13 (utilise les deux fonctions définies dans les exercices
précédents) :



```python
from exercice_10_10 import estUneMaj 
from exercice_10_11 import chaineListe 
 
def compteMaj(ch): 
  "comptage des mots débutant par une majuscule dans la chaîne ch" 
  c = 0 
  lst = chaineListe(ch)       # convertir la phrase en une liste de mots 
  for mot in lst:	   # analyser chacun des mots de la liste 
      if estUneMaj(mot[0]): 
      c = c +1 
  return c 
 
# Test : 
if __name__ == '__main__': 
  phrase = "Les filles Tidgoutt se nomment Joséphine, Justine et Corinne" 
  print("Phrase à tester : ", phrase) 
  print("Cette phrase contient", compteMaj(phrase), "majuscules.")
```



Exercice 10.14 (table des caractères ASCII) :



```python
# Table des codes ASCII
 
c = 32		 # premier code ASCII <imprimable> 
 
while c < 128 :     # dernier code strictement ASCII = 127 
  print("Code", c, ":", chr(c), end =" - ")
  c = c + 1
```



Exercice 10.16 (échange des majuscules et des minuscules) :



```python
def convMajMin(ch): 
  "échange les majuscules et les minuscules dans la chaîne ch" 
  nouvC = ""		       # chaîne à construire 
  for car in ch: 
      code = ord(car) 
      # les codes numériques des caractères majuscules et minuscules 
      # correspondants sont séparés de 32 unités : 
      if code >= 65 and code <= 91:	  # majuscules ordinaires 
      code = code + 32 
      elif code >= 192 and code <= 222:    # majuscules accentuées
      code = code + 32 
      elif code >= 97 and code <= 122:	   # minuscules ordinaires 
      code = code - 32 
      elif code >= 224 and code <= 254:    # minuscules accentuées 
      code = code - 32 
      nouvC = nouvC + chr(code) 
  # renvoi de la chaîne construite : 
  return nouvC 
 
# test : 
if __name__ == '__main__': 
  txt ="Émile Noël épouse Irène Müller" 
  print(txt) 
  print(convMajMin(txt)) 
```



Exercice 10.17 (convertir un fichier Latin-1 en Utf-8) :



```python
# Traitement et conversion de lignes dans un fichier texte 
 
def traiteLigne(ligne): 
  "remplacement des espaces de la ligne de texte par '-*-' " 
  newLine =""		    # nouvelle chaîne à construire 
  c, m = 0, 0		    # initialisations 
  while c < len(ligne):       # lire tous les caractères de la ligne 
      if ligne[c] == " ":	
      # Le caractère lu est un espace. 
      # On ajoute une 'tranche' à la chaîne en cours de construction : 
      newLine = newLine + ligne[m:c] + "-*-" 
      # On mémorise dans m la position atteinte dans la ligne lue : 
      m = c + 1 	  # ajouter 1 pour "oublier" l'espace 
      c = c + 1 
  # Ne pas oublier d'ajouter la 'tranche' suivant le dernier espace : 
  newLine = newLine + ligne[m:] 
  # Renvoyer la chaîne construite : 
  return newLine 
 
# --- Programme principal : --- 
nomFS = input("Nom du fichier source (Latin-1) : ") 
nomFD = input("Nom du fichier destinataire (Utf-8) : ") 
fs = open(nomFS, 'r', encoding ="Latin1")    # ouverture des 2 fichiers 
fd = open(nomFD, 'w', encoding ="Utf8")      # dans les encodages spécifiés 
while 1:	       # boucle de traitement 
  li = fs.readline()	      # lecture d'une ligne
  if li == "":		 # détection de la fin du fichier : 
      break		 # readline() renvoie une chaîne vide 
  fd.write(traiteLigne(li))	 # traitement + écriture  
fd.close() 
fs.close() 
```



Exercice 10.18 (tester si un caractère donné est une voyelle) :



```python
def voyelle(car): 
  "teste si le caractère <car> est une voyelle" 
  if car in "AEIOUYÀÉÈÊËÎÏÔÛÙaeiouyàéèêëîïôûù": 
      return True 
  else: 
      return False 
 
# Test : 
if __name__ == '__main__': 
  ch ="gOàÉsùïÇ"	# lettres à tester 
  for c in ch: 
      print(c, ":", voyelle(c))
```



Exercice 10.19 (utilise la fonction définie dans le script précédent) :



```python
from exercice_10_18 import voyelle 
 
def compteVoyelles(phrase): 
  "compte les voyelles présentes dans la chaîne de caractères <phrase>" 
  n = 0 
  for c in phrase: 
      if voyelle(c): 
      n = n + 1 
  return n 
 
# Test : 
if __name__ == '__main__': 
  texte ="Maître corbeau sur un arbre perché" 
  nv = compteVoyelles(texte) 
  print("La phrase <", texte, "> compte ", nv, " voyelles.", sep="")
```



Exercice 10.20 :



```python
c = 1040		      # code du premier caractère (majuscule) 
maju =""	      # chaîne destinée aux majuscules 
minu =""	      # chaîne destinée aux minuscules 
while c <1072:		    # on se limitera à cette gamme 
  maju = maju + chr(c) 
  minu = minu + chr(c +32)   # voir exercices précédents 
  c = c+1 
print(maju) 
print(minu)
```



Exercice 10.21 :



```python
# Conversion en majuscule du premier caractère de chaque mot dans un texte.
 
fiSource = input("Nom du fichier à traiter (Latin-1) : ") 
fiDest = input("Nom du fichier destinataire (Utf-8) : ") 
fs = open(fiSource, 'r', encoding ="Latin1") 
fd = open(fiDest, 'w', encoding ="Utf8") 
 
while 1: 
  ch = fs.readline()		# lecture d'une ligne 
  if ch == "": 
      break		   # fin du fichier 
  ch = ch.title()	     # conversion des initiales en maj. 
  fd.write(ch)		   # transcription 
 
fd.close()    
fs.close() 
```



Exercice 10.22 :



```python
# Conversion Latin-1 => Utf8 (variante utilisant une variable <bytes> 
 
fiSource = input("Nom du fichier à traiter (Latin-1) : ") 
fiDest = input("Nom du fichier destinataire (Utf-8) : ") 
fs = open(fiSource, 'rb')	 # mode de lecture <binaire> 
fd = open(fiDest, 'wb') 	# mode d'écriture <binaire> 
 
while 1: 
  so = fs.readline()	       # la ligne lue est une séquence d'octets 
  # Remarque : la variable so étant du type <bytes>, on doit la comparer 
  # avec une chaîne littérale (vide) du même type dans les tests :  
  if so == b"": 
      break		  # fin du fichier 
  ch = so.decode("Latin-1")	  # conversion en chaîne de caractères 
  ch = ch.replace(" ","-*-")	   # remplacement des espaces par -*- 
  so = ch.encode("Utf-8")	# Ré-encodage en une séquence d'octets 
  fd.write(so)		  # transcription 
 
fd.close()    
fs.close() 
```



Exercice 10.23 :



```python
# Comptage du nombre de mots dans un texte
 
fiSource = input("Nom du fichier à traiter : ")
fs = open(fiSource, 'r')
 
n = 0		       # variable compteur
while 1:
  ch = fs.readline()
  if ch == "":		# fin du fichier
      break
  # conversion de la chaîne lue en une liste de mots :
  li = ch.split()
  # totalisation des mots :
  n = n + len(li)    
fs.close()
 
print("Ce fichier texte contient un total de %s mots" % (n))
```



Exercice 10.24 :



```python
# Fusion de lignes pour former des phrases 
 
fiSource = input("Nom du fichier à traiter (Latin-1) : ") 
fiDest = input("Nom du fichier destinataire (Utf-8) : ") 
fs = open(fiSource, 'r', encoding ="Latin1") 
fd = open(fiDest, 'w', encoding ="Utf8") 
 
# On lit d'abord la première ligne : 
ch1 = fs.readline() 
# On lit ensuite les suivantes, en les fusionnant si nécessaire : 
while 1: 
  ch2 = fs.readline() 
  if not ch2:	      # Rappel : une chaîne vide est considérée
      break	    # comme "fausse" dans les tests 
  # Si la chaîne lue commence par une majuscule, on transcrit
  # la précédente dans le fichier destinataire, et on la 
  # remplace par celle que l'on vient de lire :
  if ch2[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÉÈÊËÎÏÔÙÛÇ": 
      fd.write(ch1) 
      ch1 = ch2 
  # Sinon, on la fusionne avec la précédente, en veillant à en
  # enlever au préalable le ou les caractère(s) de fin de ligne. 
  else: 
      ch1 = ch1[:-1] + " " + ch2 
 
# Attention : ne pas oublier de transcrire la dernière ligne :
fd.write(ch1) 
fd.close()    
fs.close()
```



Exercice 10.25 (caractéristiques de sphères) :



```python
# Le fichier de départ est un fichier <texte> dont chaque ligne contient
# un nombre réel (encodé sous la forme d'une chaîne de caractères)    
 
from math import pi 
 
def caractSphere(d): 
  "renvoie les caractéristiques d'une sphère de diamètre d" 
  d = float(d)	      # conversion de l'argument (=chaîne) en réel 
  r = d/2	   # rayon 
  ss = pi*r**2	      # surface de section 
  se = 4*pi*r**2      # surface extérieure 
  v = 4/3*pi*r**3     # volume 
  # La balise {:8.2f} utilisé ci-dessous formate le nombre 
  # affiché de manière à occuper 8 caractères au total, en arrondissant 
  # de manière à conserver deux chiffres après la virgule : 
  ch = "Diam. {:6.2f} cm Section = {:8.2f} cm&#178; ".format(d, ss) 
  ch = ch +"Surf. = {:8.2f} cm&#178;. Vol. = {:9.2f} cm&#179;".format(se, v) 
  return ch 
 
fiSource = input("Nom du fichier à traiter : ") 
fiDest = input("Nom du fichier destinataire : ") 
fs = open(fiSource, 'r') 
fd = open(fiDest, 'w') 
while 1: 
  diam = fs.readline() 
  if diam == "" or diam == "\n": 
      break 
  fd.write(caractSphere(diam) + "\n")	       # enregistrement 
fd.close() 
fs.close()
```



Exercice 10.26 :



```python
# Mise en forme de données numériques
# Le fichier traité est un fichier <texte> dont chaque ligne contient un nombre
# réel (sans exposants et encodé sous la forme d'une chaîne de caractères)    
 
def arrondir(reel):
  "représentation arrondie à .0 ou .5 d'un nombre réel"
  ent = int(reel)	   # partie entière du nombre
  fra = reel - ent	    # partie fractionnaire
  if fra < .25 :
      fra = 0
  elif fra < .75 :
      fra = .5
  else:
      fra = 1
  return ent + fra    
 
fiSource = input("Nom du fichier à traiter : ")
fiDest = input("Nom du fichier destinataire : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')
while 1:
  ligne = fs.readline()
  if ligne == "" or ligne == "\n":
      break
  n = arrondir(float(ligne))	  # conversion en <float>, puis arrondi
  fd.write(str(n) + "\n")      # enregistrement
 
fd.close()
fs.close()
```



Exercice 10.29 :



```python
# Affichage de tables de multiplication
 
nt = [2, 3, 5, 7, 9, 11, 13, 17, 19]
 
def tableMulti(m, n):
   "renvoie n termes de la table de multiplication par m"
   ch =""
   for i in range(n):
     v = m * (i+1)	      # calcul d'un des termes
     ch = ch + "M" % (v)	  # formatage à 4 caractères
   return ch
 
for a in nt:
   print(tableMulti(a, 15))	   # 15 premiers termes seulement
```



Exercice 10.30 (simple parcours d**'**une liste) :



```python
# -*- coding:Utf-8 -*- 
 
lst = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 
     'Maximilien', 'Alexandre-Benoît', 'Louise'] 
 
for e in lst: 
   print("%s : %s caractères" % (e, len(e)))
```



Exercice 10.31 :



```python
# Élimination de doublons
 
lst = [9, 12, 40, 5, 12, 3, 27, 5, 9, 3, 8, 22, 40, 3, 2, 4, 6, 25]
lst2 = []
 
for el in lst:
   if el not in lst2:
     lst2.append(el)
lst2.sort()
 
print("Liste initiale :", lst) 
print("Liste traitée  :", lst2)
```



**Exercice 10.33 (afficher tous les jours d'une année) :**



```python
## Cette variante utilise une liste de listes ##
## (que l'on pourrait aisément remplacer par deux listes distinctes)
 
# La liste ci-dessous contient deux éléments qui sont eux-mêmes des listes.
# l'élément 0 contient les nombres de jours de chaque mois, tandis que
# l'élément 1 contient les noms des douze mois :
mois = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
     ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
    'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']]
 
jour = ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi']
 
ja, jm, js, m = 0, 0, 0, 0
 
while ja <365:
 ja, jm = ja +1, jm +1	  # ja = jour dans l'année, jm = jour dans le mois
 js = (ja +3) % 7      # js = jour de la semaine. Le décalage ajouté 
	      #     permet de choisir le jour de départ
 
 if jm > mois[0][m]:	       # élément m de l'élément 0 de la liste
     jm, m = 1, m+1
 
 print(jour[js], jm, mois[1][m])   # élément m de l'élément 1 de la liste
```



Exercice 10.36 :



```python
# Insertion de nouveaux éléments dans une liste existante
 
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin',
   'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
 
c, d = 1, 0
while d < 12 :
  t2[c:c] = [t1[d]]	 # ! l'élément inséré doit être une liste
  c, d = c+2, d+1
 
print(t2)
```



Exercice 10.40 :



```python
# Crible d'Eratosthène pour rechercher les nombres premiers de 1 à 999
 
# Créer une liste de 1000 éléments 1 (leurs indices vont de 0 à 999) :
lst = [1]*1000	      
# Parcourir la liste à partir de l'élément d'indice 2:
for i in range(2,1000):
  # Mettre à zéro les éléments suivants dans la liste,
  # dont les indices sont des multiples de i :
  for j in range(i*2, 1000, i):
      lst[j] = 0
 
# Afficher les indices des éléments restés à 1 (on ignore l'élément 0) :
for i in range(1,1000):
  if lst[i]:
      print(i, end =' ?)
```



Exercice 10.43 (Test du générateur de nombres aléatoires, page ) :



```python
from random import random      # tire au hasard un réel entre 0 et 1
 
n = input("Nombre de valeurs à tirer au hasard (défaut = 1000) : ")
if n == "":
  nVal =1000
else:
  nVal = int(n)
n = input("Nombre de fractions dans l'intervalle 0-1 (entre 2 et {}, "\ 
     "défaut =5) : ".format(nVal//10)) 
if n == "":
  nFra =5
else:
  nFra = int(n)
if nFra < 2:
  nFra =2
elif nFra > nVal/10:
  nFra = nVal/10
 
print("Tirage au sort des", nVal, "valeurs ...")
listVal = [0]*nVal	      # créer une liste de zéros
for i in range(nVal):		 # puis modifier chaque élément
  listVal[i] = random()
print("Comptage des valeurs dans chacune des", nFra, "fractions ...")
listCompt = [0]*nFra		# créer une liste de compteurs
 
# parcourir la liste des valeurs :
for valeur in listVal:
  # trouver l'index de la fraction qui contient la valeur :
  index = int(valeur*nFra)
  # incrémenter le compteur correspondant :
  listCompt[index] = listCompt[index] +1
 
# afficher l'état des compteurs :
for compt in listCompt:
  print(compt, end =' ?)
print()
```



Exercice 10.44 : tirage de cartes



```python
from random import randrange
 
couleurs = ['Pique', 'Trèfle', 'Carreau', 'Cœur']
valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as']
 
# Construction de la liste des 52 cartes :
carte =[]
for coul in couleurs:
   for val in valeurs:
     carte.append("{} de {}".format(val, coul)) 
 
# Tirage au hasard :
while 1:
   k = input("Frappez <c> pour tirer une carte, <Enter> pour terminer ") 
   if k =="":
     break
   r = randrange(52)	  # tirage au hasard d'un entier entre 0 et 51
   print(carte[r])
```



Exercice 10.45 : Création et consultation d**'**un dictionnaire



```python
# Mini système de bases de données 
 
def consultation(): 
  while 1: 
      nom = input("Entrez le nom (ou <enter> pour terminer) : ") 
      if nom == "": 
      break 
      if nom in dico:		   # le nom est-il répertorié ? 
      item = dico[nom]		# consultaion proprement dite 
      age, taille = item[0], item[1] 
      print("Nom : {} - âge : {} ans - taille : {} m.".\ 
	 format(nom, age, taille))
      else: 
      print("*** nom inconnu ! ***") 
 
def remplissage(): 
  while 1: 
      nom = input("Entrez le nom (ou <enter> pour terminer) : ") 
      if nom == "": 
      break 
      age = int(input("Entrez l'âge (nombre entier !) : ")) 
      taille = float(input("Entrez la taille (en mètres) : ")) 
      dico[nom] = (age, taille) 
 
dico ={} 
while 1: 
  choix = input("Choisissez : (R)emplir - (C)onsulter - (T)erminer : ") 
  if choix.upper() == 'T': 
      break 
  elif choix.upper() == 'R': 
      remplissage() 
  elif choix.upper() == 'C': 
      consultation()
```



Exercice 10.46 : échange des clés et des valeurs dans un dictionnaire



```python
def inverse(dico):
  "Construction d'un nouveau dico, pas à pas"
  dic_inv ={} 
  for cle in dico:
      item = dico[cle]	
      dic_inv[item] = cle
 
  return dic_inv
 
# programme test :
 
dico = {'Computer':'Ordinateur',
      'Mouse':'Souris',
      'Keyboard':'Clavier',
      'Hard disk':'Disque dur',
      'Screen':'Écran'}
 
print(dico)
print(inverse(dico))
```



Exercice 10.47 : histogramme



```python
# Histogramme des fréquences de chaque lettre dans un texte 
 
nFich = input('Nom du fichier (Latin-1) : ') 
fi = open(nFich, 'r', encoding ="Latin1") 
texte = fi.read() 
fi.close() 
 
print(texte) 
dico ={} 
for c in texte: 	  # afin de les regrouper, on convertit 
  c = c.upper() 	    # toutes les lettres en majuscules 
  dico[c] = dico.get(c, 0) +1 
 
liste = list(dico.items()) 
liste.sort() 
for car, freq in liste: 
  print("Caractère {} : {} occurrence(s).".format(car, freq))
```



Exercice 10.48 :



```python
# Histogramme des fréquences de chaque mot dans un texte 
# Suivant l'encodage du fichier source, activer l'une ou l'autre ligne : 
encodage ="Latin-1" 
# encodage ="Utf-8" 
 
nFich = input('Nom du fichier à traiter ({}) : '.format(encodage)) 
# Conversion du fichier en une chaîne de caractères : 
fi = open(nFich, 'r', encoding =encodage) 
texte = fi.read() 
fi.close() 
 
# afin de pouvoir aisément séparer les mots du texte, on commence 
# par convertir tous les caractères non-alphabétiques en espaces  : 
alpha = "abcdefghijklmnopqrstuvwxyzéèàùçâêîôûäëïöü" 
lettres = ""	    # nouvelle chaîne à construire 
for c in texte: 
  c = c.lower()       # conversion de chaque caractère en minuscule 
  if c in alpha: 
      lettres = lettres + c 
  else: 
      lettres = lettres + ' ' 
 
# conversion de la chaîne résultante en une liste de mots : 
mots = lettres.split() 
 
# construction de l'histogramme : 
dico ={} 
for m in mots: 
  dico[m] = dico.get(m, 0) +1 
liste = list(dico.items()) 
 
# tri de la liste résultante : 
liste.sort() 
# affichage en clair : 
for item in liste: 
  print("{} : {}".format(item[0], item[1])) 
```



Exercice 10.49 :



```python
# Encodage d'un texte dans un dictionnaire 
# Suivant l'encodage du fichier source, activer l'une ou l'autre ligne : 
encodage ="Latin-1" 
# encodage ="Utf-8" 
 
nFich = input('Nom du fichier à traiter ({}) : '.format(encodage)) 
# Conversion du fichier en une chaîne de caractères : 
fi = open(nFich, 'r', encoding =encodage) 
texte = fi.read() 
fi.close() 
 
# On considère que les mots sont des suites de caractères faisant partie 
# de la chaîne ci-dessous. Tous les autres sont des séparateurs : 
alpha = "abcdefghijklmnopqrstuvwxyzéèàùçâêîôûäëïöü" 
 
# Construction du dictionnaire : 
dico ={} 
# Parcours de tous les caractères du texte : 
i =0		 # indice du caractère en cours de lecture 
im =-1		   # indice du premier caractère du mot 
mot = ""	 # variable de travail : mot en cours de lecture 
for c in texte: 
  c = c.lower()    # conversion de chaque caractère en minuscule
 
  if c in alpha:    # car. alphabétique => on est à l'intérieur d'un mot
      mot = mot + c 
      if im < 0:    # mémoriser l'indice du premier caractère du mot 
      im =i   
  else:        # car. non-alphabétique => fin de mot 
      if mot != "":    # afin d'ignorer les car. non-alphab. successifs 
      # pour chaque mot, on construit une liste d'indices : 
      if mot in dico:	       # mot déjà répertorié :
	  dico[mot].append(im)	  # ajout d'un indice à la liste 
      else:		 # mot rencontré pour la 1e fois : 
	  dico[mot] =[im]	   # création de la liste d'indices 
      mot =""	 # préparer la lecture du mot suivant 
      im =-1 
  i += 1	# indice du caractère suivant 
 
# Affichage du dictionnaire, en clair : 
listeMots =list(dico.items())	  # Conversion du dico en une liste de tuples 
listeMots.sort()	 # tri alphabétique de la liste 
for clef, valeur in listeMots: 
  print(clef, ":", valeur)
```



Exercice 10.50 : Sauvegarde d**'**un dictionnaire (complément
de l**'**ex. 10.45).



```python
# Mini-système de base de données 
 
def consultation(): 
  while 1: 
      nom = input("Entrez le nom (ou <enter> pour terminer) : ") 
      if nom == "": 
      break 
      if nom in dico:		   # le nom est-il répertorié ? 
      item = dico[nom]		# consultaion proprement dite 
      age, taille = item[0], item[1] 
      print("Nom : {} - âge : {} ans - taille : {} m.".\ 
	 format(nom, age, taille))	 
      else: 
      print("*** nom inconnu ! ***") 
 
def remplissage(): 
  while 1: 
      nom = input("Entrez le nom (ou <enter> pour terminer) : ") 
      if nom == "": 
      break 
      age = int(input("Entrez l'âge (nombre entier !) : ")) 
      taille = float(input("Entrez la taille (en mètres) : ")) 
      dico[nom] = (age, taille) 
 
def enregistrement(): 
  fich = input("Entrez le nom du fichier de sauvegarde : ") 
  ofi = open(fich, "w") 
  # écriture d'une ligne-repère pour identifier le type de fichier : 
  ofi.write("DicoExercice10.50\n") 
  # parcours du dictionnaire entier, converti au préalable en une liste : 
  for cle, valeur in list(dico.items()): 
      # utilisation du formatage des chaînes pour créer l'enregistrement : 
      ofi.write("{}@{}#{}\n".format(cle, valeur[0], valeur[1])) 
  ofi.close() 
 
def lectureFichier(): 
  fich = input("Entrez le nom du fichier de sauvegarde : ") 
  try: 
      ofi = open(fich, "r") 
  except: 
      print("*** fichier inexistant ***") 
      return 
  # Vérification : le fichier est-il bien de notre type spécifique ? : 
  repere =ofi.readline() 
  if repere != "DicoExercice10.50\n": 
      print("*** type de fichier incorrect ***") 
      return 
  # Lecture des lignes restantes du fichier : 
  while 1: 
      ligne = ofi.readline() 
      if ligne =='':	      # détection de la fin de fichier 
      break 
      enreg = ligne.split("@")	  # restitution d'une liste [clé,valeur] 
      cle = enreg[0] 
      valeur = enreg[1][:-1]	  # élimination du caractère de fin de ligne 
      data = valeur.split("#")	  # restitution d'une liste [âge, taille] 
      age, taille = int(data[0]), float(data[1]) 
      dico[cle] = (age, taille)   # reconstitution du dictionnaire 
  ofi.close() 
 
########### Programme principal : ########### 
dico ={} 
lectureFichier()
while 1: 
  choix = input("Choisissez : (R)emplir - (C)onsulter - (T)erminer : ") 
  if choix.upper() == 'T': 
      break 
  elif choix.upper() == 'R': 
      remplissage() 
  elif choix.upper() == 'C': 
      consultation() 
enregistrement()
```



Exercice 10.51 : Contrôle du flux d**'**exécution à l**'**aide d**'**un dictionnaire

Cet exercice complète le précédent. On ajoute encore deux petites
fonctions, et on réécrit le corps principal du programme pour diriger le
flux d'exécution en se servant d'un dictionnaire :



```python
def sortie(): 
  print("*** Job terminé ***") 
  return 1		# afin de provoquer la sortie de la boucle 
 
def autre(): 
  print("Veuillez frapper R, A, C, S ou T, svp.") 
 
######## * Programme principal * ######### 
 
dico ={} 
fonc ={"R":lectureFichier, "A":remplissage, "C":consultation, 
     "S":enregistrement, "T":sortie} 
while 1: 
  choix = input("Choisissez :\n" +\ 
  "(R)écupérer un dictionnaire préexistant sauvegardé dans un fichier\n" +\ 
  "(A)jouter des données au dictionnaire courant\n" +\ 
  "(C)onsulter le dictionnaire courant\n" +\ 
  "(S)auvegarder le dictionnaire courant dans un fichier\n" +\ 
  "(T)erminer : ").upper() 
  # l'instruction ci-dessous appelle une fonction différente pour chaque 
  # choix, par l'intermédiaire du dictionnaire <fonc> : 
  if fonc.get(choix, autre)(): 
      break 
  # note : toutes les fonctions appelées ici renvoient <None> par défaut 
  #	  sauf la fonction sortie() qui renvoie 1 => sortie de la boucle
```



Exercice 11.1 :



```python
from math import sqrt	     # fonction racine carrée 
 
def distance(p1, p2): 
  # On applique le théorème de Pythagore : 
  dx =abs(p1.x - p2.x)	      # abs() => valeur absolue 
  dy =abs(p1.y - p2.y) 
  return sqrt(dx*dx + dy*dy) 
 
def affiche_point(p): 
  print("Coord. horiz.", p.x, "Coord. vert.", p.y) 
 
class Point(object): 
  "Classe de points géométriques" 
 
# Définition des 2 points : 
p8, p9 = Point(), Point() 
p8.x, p8.y, p9.x, p9.y = 12.3, 5.7, 6.2, 9.1 
 
affiche_point(p8) 
affiche_point(p9) 
print("Distance =", distance(p8,p9)) 
```



Exercice 12.1 :



```python
class Domino(object):
  def __init__(self, pa, pb):
      self.pa, self.pb = pa, pb
 
  def affiche_points(self):
      print "face A :", self.pa,
      print "face B :", self.pb
 
  def valeur(self):
      return self.pa + self.pb
 
# Programme de test :
 
d1 = Domino(2,6)
d2 = Domino(4,3)
 
d1.affiche_points()
d2.affiche_points()
 
print("total des points :", d1.valeur() + d2.valeur())
 
liste_dominos = []
for i in range(7):
  liste_dominos.append(Domino(6, i))
 
vt =0
for i in range(7):
  liste_dominos[i].affiche_points()
  vt = vt + liste_dominos[i].valeur()
 
print("valeur totale des points", vt) 
print(liste_dominos[3], liste_dominos[4])
```



Exercice 12.2 :



```python
class CompteBancaire(object): 
  def __init__(self, nom ='Dupont', solde =1000): 
      self.nom, self.solde = nom, solde 
 
  def depot(self, somme): 
      self.solde = self.solde + somme 
 
  def retrait(self, somme): 
      self.solde = self.solde - somme 
 
  def affiche(self): 
      print("Le solde du compte bancaire de {} est de {} euros.".\ 
	format(self.nom, self.solde)) 
 
# Programme de test : 
 
if __name__ == '__main__': 
  c1 = CompteBancaire('Duchmol', 800) 
  c1.depot(350) 
  c1.retrait(200) 
  c1.affiche() 
```



Exercice 12.3 :



```python
class Voiture(object): 
  def __init__(self, marque = 'Ford', couleur = 'rouge'): 
      self.couleur = couleur 
      self.marque = marque 
      self.pilote = 'personne' 
      self.vitesse = 0 
 
  def accelerer(self, taux, duree): 
      if self.pilote =='personne': 
      print("Cette voiture n'a pas de conducteur !") 
      else:
      self.vitesse = self.vitesse + taux * duree 
 
  def choix_conducteur(self, nom): 
      self.pilote = nom    
 
  def affiche_tout(self): 
      print("{} {} pilotée par {}, vitesse = {} m/s".\ 
      format(self.marque, self.couleur, self.pilote, self.vitesse))	
 
a1 = Voiture('Peugeot', 'bleue') 
a2 = Voiture(couleur = 'verte') 
a3 = Voiture('Mercedes') 
a1.choix_conducteur('Roméo') 
a2.choix_conducteur('Juliette') 
a2.accelerer(1.8, 12) 
a3.accelerer(1.9, 11) 
a2.affiche_tout() 
a3.affiche_tout()
```



Exercice 12.4 :



```python
class Satellite(object): 
  def __init__(self, nom, masse =100, vitesse =0): 
      self.nom, self.masse, self.vitesse = nom, masse, vitesse 
 
  def impulsion(self, force, duree): 
      self.vitesse = self.vitesse + force * duree / self.masse 
 
  def energie(self): 
      return self.masse * self.vitesse**2 / 2	  
 
  def affiche_vitesse(self): 
      print("Vitesse du satellite {} = {} m/s".\ 
	format(self.nom, self.vitesse)) 
 
# Programme de test : 
 
s1 = Satellite('Zoé', masse =250, vitesse =10) 
 
s1.impulsion(500, 15) 
s1.affiche_vitesse() 
print("énergie =", s1.energie()) 
s1.impulsion(500, 15) 
s1.affiche_vitesse() 
print("nouvelle énergie =", s1.energie())
```



Exercices 12.5-12.6 (classes de cylindres et de cônes) :



```python
# Classes dérivées - Polymorphisme
 
class Cercle(object):
  def __init__(self, rayon):
      self.rayon = rayon
 
  def surface(self):
      return 3.1416 * self.rayon**2
 
class Cylindre(Cercle):
  def __init__(self, rayon, hauteur):
      Cercle.__init__(self, rayon)
      self.hauteur = hauteur
 
  def volume(self):
      return self.surface()*self.hauteur
 
  # la méthode surface() est héritée de la classe parente
 
class Cone(Cylindre):
  def __init__(self, rayon, hauteur):
      Cylindre.__init__(self, rayon, hauteur)
 
  def volume(self):
      return Cylindre.volume(self)/3	    
      # cette nouvelle méthode volume() remplace celle que
      # l'on a héritée de la classe parente (exemple de polymorphisme)
 
# Programme test :
 
cyl = Cylindre(5, 7) 
print("Surf. de section du cylindre =", cyl.surface()) 
print("Volume du cylindre =", cyl.volume()) 
 
co = Cone(5,7) 
print("Surf. de base du cône =", co.surface()) 
print("Volume du cône =", co.volume())
```



Exercice 12.7 :



```python
# Tirage de cartes 
 
from random import randrange 
 
class JeuDeCartes(object): 
  """Jeu de cartes""" 
  # attributs de classe (communs à toutes les instances) : 
  couleur = ('Pique', 'Trèfle', 'Carreau', 'Cœur') 
  valeur = (0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as') 
 
  def __init__(self): 
      "Construction de la liste des 52 cartes" 
      self.carte =[] 
      for coul in range(4): 
      for val in range(13): 
	  self.carte.append((val +2, coul))    # la valeur commence à 2 
 
  def nom_carte(self, c): 
      "Renvoi du nom de la carte c, en clair" 
      return "{} de {}".format(self.valeur[c[0]], self.couleur[c[1]]) 
 
  def battre(self): 
      "Mélange des cartes" 
      t = len(self.carte)	   # nombre de cartes restantes 
      # pour mélanger, on procède à un nombre d'échanges équivalent : 
      for i in range(t): 
      # tirage au hasard de 2 emplacements dans la liste : 
      h1, h2 = randrange(t), randrange(t) 
      # échange des cartes situées à ces emplacements : 
      self.carte[h1], self.carte[h2] = self.carte[h2], self.carte[h1] 
 
  def tirer(self): 
      "Tirage de la première carte de la pile" 
      t = len(self.carte)	   # vérifier qu'il reste des cartes
      if t >0:		     
      carte = self.carte[0]	  # choisir la première carte du jeu 
      del(self.carte[0])	  # la retirer du jeu
      return carte	     # en renvoyer copie au prog. appelant 
      else: 
      return None	       # facultatif
 
### Programme test : 
 
if __name__ == '__main__': 
  jeu = JeuDeCartes()		   # instanciation d'un objet 
  jeu.battre()		     # mélange des cartes 
  for n in range(53):		   # tirage des 52 cartes : 
      c = jeu.tirer() 
      if c == None:		 # il ne reste aucune carte 
      print('Terminé !')	  # dans la liste 
      else: 
      print(jeu.nom_carte(c))	  # valeur et couleur de la carte
```



Exercice 12.8 :

( *On supposera que l'exercice précédent a été sauvegardé sous le nom
**cartes.py**.* )



```python
# Bataille de de cartes
 
from cartes import JeuDeCartes
 
jeuA = JeuDeCartes()	   # instanciation du premier jeu
jeuB = JeuDeCartes()	   # instanciation du second jeu      
jeuA.battre()		# mélange de chacun
jeuB.battre()
pA, pB = 0, 0		# compteurs de points des joueurs A et B
 
# tirer 52 fois une carte de chaque jeu :
for n in range(52):	  
  cA, cB = jeuA.tirer(), jeuB.tirer()
  vA, vB = cA[0], cB[0]   # valeurs de ces cartes
  if vA > vB:
      pA += 1
  elif vB > vA:
      pB += 1	       # (rien ne se passe si vA = vB)
  # affichage des points successifs et des cartes tirées :
  print("{} * {} ==> {} * {}".format(jeuA.nom_carte(cA), 
		     jeuB.nom_carte(cB), pA, pB)) 
 
print("le joueur A obtient {} pts, le joueur B en obtient {}.".format(pA, pB))
```



Exercice 12.9 :



```python
from exercice_12_02 import CompteBancaire 
 
class CompteEpargne(CompteBancaire): 
  def __init__(self, nom ='Durand', solde =500): 
      CompteBancaire.__init__(self, nom, solde) 
      self.taux =.3	    # taux d'intérêt mensuel par défaut 
 
  def changeTaux(self, taux): 
      self.taux =taux 
 
  def capitalisation(self, nombreMois =6): 
      print("Capitalisation sur {} mois au taux mensuel de {} %.".\ 
	format(nombreMois, self.taux)) 
      for m in range(nombreMois): 
      self.solde = self.solde * (100 +self.taux)/100
 
# Programme de test : 
 
if __name__ == '__main__': 
  c1 = CompteEpargne('Duvivier', 600) 
  c1.depot(350) 
  c1.affiche() 
  c1.capitalisation(12) 
  c1.affiche() 
  c1.changeTaux(.5) 
  c1.capitalisation(12) 
  c1.affiche() 
```



Exercice 13.6 :



```python
from tkinter import *
 
def cercle(can, x, y, r, coul ='white'):
  "dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
  can.create_oval(x-r, y-r, x+r, y+r, fill =coul)
 
class Application(Tk):
  def __init__(self):
      Tk.__init__(self)    # constructeur de la classe parente
      self.can =Canvas(self, width =475, height =130, bg ="white")
      self.can.pack(side =TOP, padx =5, pady =5)
      Button(self, text ="Train", command =self.dessine).pack(side =LEFT)
      Button(self, text ="Hello", command =self.coucou).pack(side =LEFT)
      Button(self, text ="Ecl34", command =self.eclai34).pack(side =LEFT)
 
  def dessine(self):
      "instanciation de 4 wagons dans le canevas"
      self.w1 = Wagon(self.can, 10, 30)
      self.w2 = Wagon(self.can, 130, 30, 'dark green')
      self.w3 = Wagon(self.can, 250, 30, 'maroon')
      self.w4 = Wagon(self.can, 370, 30, 'purple')
 
  def coucou(self):
      "apparition de personnages dans certaines fenêtres"
      self.w1.perso(3)	      # 1er wagon, 3e fenêtre
      self.w3.perso(1)	      # 3e wagon, 1e fenêtre
      self.w3.perso(2)	      # 3e wagon, 2e fenêtre
      self.w4.perso(1)	      # 4e wagon, 1e fenêtre
 
  def eclai34(self):
      "allumage de l'éclairage dans les wagons 3 & 4"
      self.w3.allumer()
      self.w4.allumer()
 
class Wagon(object):
  def __init__(self, canev, x, y, coul ='navy'):
      "dessin d'un petit wagon en <x,y> dans le canevas <canev>"
      # mémorisation des paramètres dans des variables d'instance :
      self.canev, self.x, self.y = canev, x, y
      # rectangle de base : 95x60 pixels :
      canev.create_rectangle(x, y, x+95, y+60, fill =coul)
      # 3 fenêtres de 25x40 pixels, écartées de 5 pixels :
      self.fen =[]    # pour mémoriser les réf. des fenêtres 
      for xf in range(x +5, x +90, 30):
      self.fen.append(canev.create_rectangle(xf, y+5,
		  xf+25, y+40, fill ='black'))
      # 2 roues, de rayon égal à 12 pixels  :
      cercle(canev, x+18, y+73, 12, 'gray')
      cercle(canev, x+77, y+73, 12, 'gray')
 
  def perso(self, fen):
      "apparition d'un petit personnage à la fenêtre <fen>"
      # calcul des coordonnées du centre de chaque fenêtre :
      xf = self.x + fen*30 -12
      yf = self.y + 25
      cercle(self.canev, xf, yf, 10, "pink")	  # visage
      cercle(self.canev, xf-5, yf-3, 2)      # œil gauche	 
      cercle(self.canev, xf+5, yf-3, 2)      # œil droit
      cercle(self.canev, xf, yf+5, 3)	       # bouche
 
  def allumer(self):
      "déclencher l'éclairage interne du wagon"
      for f in self.fen:
      self.canev.itemconfigure(f, fill ='yellow')
 
app = Application()
app.mainloop()
```



Exercice 13.10 :



```python
#  Widget dérivé de <Canvas>, spécialisé pour
#  dessiner des graphiques élongation/temps
 
from tkinter import * 
from math import sin, pi 
 
class OscilloGraphe(Canvas): 
  "Canevas spécialisé, pour dessiner des courbes élongation/temps" 
  def __init__(self, master=None, larg=200, haut=150): 
      "Constructeur de la base du graphique : quadrillage et axes" 
      Canvas.__init__(self)		     # appel au constructeur 
      self.configure(width=larg, height=haut)	       # de la classe parente 
      self.larg, self.haut = larg, haut 	 # mémorisation 
      # tracé d'une échelle horizontale avec 8 graduations : 
      pas = (larg-25)/8.	# intervalles de l'échelle horizontale
      for t in range(0, 9): 
      stx = 10 + t*pas	      # +10 pour partir de l'origine 
      self.create_line(stx, haut/10, stx, haut*9/10, fill='grey') 
      # tracé d'une échelle verticale avec 5 graduations :
      pas = haut*2/25.	       # intervalles de l'échelle verticale 
      for t in range(-5, 6): 
      sty = haut/2 -t*pas	 # haut/2 pour partir de l'origine 
      self.create_line(10, sty, larg-15, sty, fill='grey') 
      self.traceAxes()	       # tracé des axes de référence X et Y
 
  def traceAxes(self): 
      "Méthode traçant les axes de référence (pourra être surchargée)." 
      # axes horizontal (X) et vertical (Y) : 
      self.create_line(10, self.haut/2, self.larg, self.haut/2, arrow=LAST) 
      self.create_line(10, self.haut-5, 10, 5, arrow=LAST) 
      # indication des grandeurs physiques aux extrémités des axes : 
      self.create_text(20, 10, anchor =CENTER, text = "e") 
      self.create_text(self.larg-10, self.haut/2-12, anchor=CENTER, text="t") 
 
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
  racine = Tk() 
  gra = OscilloGraphe(racine, 250, 180) 
  gra.pack() 
  gra.configure(bg ='ivory', bd =2, relief=SUNKEN) 
  gra.traceCourbe(2, 1.2, 10, 'purple') 
  racine.mainloop() 
```



Exercice 13.16 :



```python
#  Tracé de graphiques élongation/temps pour 3
#  mouvements vibratoires harmoniques
 
from tkinter import * 
from math import sin, pi 
from exercice_13_10 import OscilloGraphe 
 
class OscilloGrapheBis(OscilloGraphe): 
  """Classe dérivée du widget Oscillographe (cf. exercice 13.10)""" 
  def __init__(self, master =None, larg =200, haut =150): 
      # Appel du constructeur de la classe parente : 
      OscilloGraphe.__init__(self, master, larg, haut) 
 
  def traceAxes(self): 
      "Surchage de la méthode de même nom dans la classe parente" 
      # tracé de l'axe de référence Y : 
      pas = (self.larg-25)/8.	     # intervalles de l'échelle horizontale 
      self.create_line(10+4*pas, self.haut-5, 10+4*pas, 5, fill ='grey90', 
	    arrow=LAST) 
      # tracé de l'axe de référence X : 
      self.create_line(10, self.haut/2, self.larg, self.haut/2, 
	    fill= 'grey90', arrow=LAST) 
      # indication des grandeurs physiques aux extrémités des axes : 
      self.create_text(20+4*pas, 15, anchor=CENTER, text="e", fill='red') 
      self.create_text(self.larg-5, self.haut/2-12, anchor=CENTER, text ="t", 
	    fill='red') 
 
class ChoixVibra(Frame): 
  """Curseurs pour choisir fréquence, phase & amplitude d'une vibration""" 
  def __init__(self, master=None, coul='red'): 
      Frame.__init__(self)	# constructeur de la classe parente 
      # Définition de quelques attributs d'instance : 
      self.freq, self.phase, self.ampl, self.coul = 0, 0, 0, coul 
      # Variable d'état de la case à cocher : 
      self.chk = IntVar()	   # 'objet-variable' Tkinter 
      Checkbutton(self, text='Afficher', variable=self.chk, 
	  fg = self.coul, command=self.setCurve).pack(side=LEFT) 
      # Définition des 3 widgets curseurs : 
      Scale(self, length=150, orient=HORIZONTAL, sliderlength =25, 
	label ='Fréquence (Hz) :', from_=1., to=9., tickinterval =2, 
	resolution =0.25, showvalue =0, 
	command = self.setFrequency).pack(side=LEFT, pady =5) 
      Scale(self, length=150, orient=HORIZONTAL, sliderlength =15, 
	label ='Phase (degrés) :', from_=-180, to=180, tickinterval =90, 
	showvalue =0, command = self.setPhase).pack(side=LEFT, pady =5) 
      Scale(self, length=150, orient=HORIZONTAL, sliderlength =25, 
	label ='Amplitude :', from_=2, to=10, tickinterval =2, 
	showvalue =0, 
	command = self.setAmplitude).pack(side=LEFT, pady =5) 
 
  def setCurve(self): 
      self.master.event_generate('<Control-Z>') 
 
  def setFrequency(self, f): 
      self.freq = float(f) 
      self.master.event_generate('<Control-Z>') 
 
  def setPhase(self, p): 
      pp =float(p) 
      self.phase = pp*2*pi/360	      # conversion degrés -> radians 
      self.master.event_generate('<Control-Z>') 
 
  def setAmplitude(self, a): 
      self.ampl = float(a) 
      self.master.event_generate('<Control-Z>') 
 
## Classe principale ##
 
class ShowVibra(Frame): 
  """Démonstration de mouvements vibratoires harmoniques""" 
  def __init__(self, master=None): 
      Frame.__init__(self)	  # constructeur de la classe parente 
      self.couleur = ['green', 'yellow', 'orange'] 
      self.trace = [0]*3	# liste des tracés (courbes à dessiner) 
      self.controle = [0]*3	   # liste des panneaux de contrôle 
      # Instanciation du canevas avec axes X et Y : 
      self.gra = OscilloGrapheBis(self, larg =400, haut=300) 
      self.gra.configure(bg ='grey40', bd=3, relief=SUNKEN) 
      self.gra.pack(side =TOP, pady=3) 
      # Instanciation de 3 panneaux de contrôle (curseurs) : 
      for i in range(3): 
      self.controle[i] = ChoixVibra(self, self.couleur[i]) 
      self.controle[i].configure(bd =3, relief = GROOVE) 
      self.controle[i].pack(padx =10, pady =3) 
      # Désignation de l'événement qui déclenche l'affichage des tracés : 
      self.master.bind('<Control-Z>', self.montreCourbes) 
      self.master.title('Mouvements vibratoires harmoniques') 
      self.pack() 
 
  def montreCourbes(self, event): 
      """(Ré)Affichage des trois graphiques élongation/temps""" 
      for i in range(3): 
      # D'abord, effacer le tracé précédent (éventuel) : 
      self.gra.delete(self.trace[i]) 
      # Ensuite, dessiner le nouveau tracé : 
      if self.controle[i].chk.get(): 
	  self.trace[i] = self.gra.traceCourbe( 
		  coul=self.couleur[i], 
		  freq=self.controle[i].freq, 
		  phase=self.controle[i].phase, 
		  ampl=self.controle[i].ampl) 
 
#### Code de test : ### 
 
if __name__ == '__main__': 
  ShowVibra().mainloop() 
```



Exercice 13.22 : Dictionnaire de couleurs



```python
from tkinter import * 
# Module donnant accès aux boîtes de dialogue standard pour 
# la recherche de fichiers sur disque : 
from tkinter.filedialog import asksaveasfile, askopenfile 
 
class Application(Frame): 
  '''Fenêtre d'application''' 
  def __init__(self): 
      Frame.__init__(self) 
      self.master.title("Création d'un dictionnaire de couleurs") 
      self.dico ={}	     # création du dictionnaire 
 
      # Les widgets sont regroupés dans deux cadres (Frames) : 
      frSup =Frame(self)      # cadre supérieur contenant 6 widgets
      Label(frSup, text ="Nom de la couleur :", 
	width =20).grid(row =1, column =1) 
      self.enNom =Entry(frSup, width =25)      # champ d'entrée pour 
      self.enNom.grid(row =1, column =2)      # le nom de la couleur 
      Button(frSup, text ="Existe déjà ?", width =12, 
	 command =self.chercheCoul).grid(row =1, column =3) 
      Label(frSup, text ="Code hexa. corresp. :", 
	width =20).grid(row =2, column =1) 
      self.enCode =Entry(frSup, width =25)	# champ d'entrée pour
      self.enCode.grid(row =2, column =2)      # le code hexa. 
      Button(frSup, text ="Test", width =12, 
	 command =self.testeCoul).grid(row =2, column =3) 
      frSup.pack(padx =5, pady =5) 
 
      frInf =Frame(self)      # cadre inférieur contenant le reste 
      self.test = Label(frInf, bg ="white", width =45,	  # zone de test
	     height =7, relief = SUNKEN) 
      self.test.pack(pady =5)	 
      Button(frInf, text ="Ajouter la couleur au dictionnaire", 
	 command =self.ajouteCoul).pack() 
      Button(frInf, text ="Enregistrer le dictionnaire", width =25, 
	 command =self.enregistre).pack(side = LEFT, pady =5) 
      Button(frInf, text ="Restaurer le dictionnaire", width =25, 
	 command =self.restaure).pack(side =RIGHT, pady =5) 
      frInf.pack(padx =5, pady =5) 
      self.pack()     
 
  def ajouteCoul(self): 
      "ajouter la couleur présente au dictionnaire" 
      if self.testeCoul() ==0:	      # une couleur a-t-elle été définie ?
      return
      nom = self.enNom.get() 
      if len(nom) >1:		   # refuser les noms trop petits 
      self.dico[nom] =self.cHexa 
      else: 
      self.test.config(text ="%s : nom incorrect" % nom, bg='white') 
 
  def chercheCoul(self): 
      "rechercher une couleur déjà inscrite au dictionnaire" 
      nom = self.enNom.get() 
      if nom in self.dico: 
      self.test.config(bg =self.dico[nom], text ="") 
      else: 
      self.test.config(text ="%s : couleur inconnue" % nom, bg='white') 
 
  def testeCoul(self): 
      "vérifier la validité d'un code hexa. - afficher la couleur corresp." 
      try: 
      self.cHexa =self.enCode.get() 
      self.test.config(bg =self.cHexa, text ="") 
      return 1 
      except: 
      self.test.config(text ="Codage de couleur incorrect", bg ='white') 
      return 0 
 
  def enregistre(self): 
      "enregistrer le dictionnaire dans un fichier texte" 
      # Cette méthode utilise une boîte de dialogue standard pour la 
      # sélection d'un fichier sur disque. Tkinter fournit toute une série 
      # de fonctions associées à ces boîtes, dans le module filedialog.
      # La fonction ci-dessous renvoie un objet-fichier ouvert en écriture :
      ofi =asksaveasfile(filetypes=[("Texte",".txt"),("Tous","*")]) 
      for clef, valeur in list(self.dico.items()): 
      ofi.write("{} {}\n".format(clef, valeur)) 
      ofi.close() 
 
  def restaure(self): 
      "restaurer le dictionnaire à partir d'un fichier de mémorisation" 
      # La fonction ci-dessous renvoie un objet-fichier ouvert en lecture : 
      ofi =askopenfile(filetypes=[("Texte",".txt"),("Tous","*")]) 
      lignes = ofi.readlines() 
      for li in lignes: 
      cv = li.split()	  # extraction de la clé et la valeur corresp.
      self.dico[cv[0]] = cv[1] 
      ofi.close() 
 
if __name__ == '__main__': 
  Application().mainloop() 
```





![](images/10000000000001D60000012916439269.jpg)



Exercice 13.23 (variante 3) :



```python
from tkinter import *
from random import randrange
from math import sin, cos, pi
class FaceDom(object):
  def __init__(self, can, val, pos, taille =70):
      self.can =can	  
      x, y, c = pos[0], pos[1], taille/2
      self. carre = can.create_rectangle(x -c, y-c, x+c, y+c,
		     fill ='ivory', width =2)
      d = taille/3	 
      # disposition des points sur la face, pour chacun des 6 cas :
      self.pDispo = [((0,0),),
	     ((-d,d),(d,-d)),
	     ((-d,-d), (0,0), (d,d)),
	     ((-d,-d),(-d,d),(d,-d),(d,d)),
	     ((-d,-d),(-d,d),(d,-d),(d,d),(0,0)),
	     ((-d,-d),(-d,d),(d,-d),(d,d),(d,0),(-d,0))]
 
      self.x, self.y, self.dim = x, y, taille/15
      self.pList =[]	  # liste contenant les points de cette face
      self.tracer_points(val)
 
  def tracer_points(self, val):
      # créer les dessins de points correspondant à la valeur val :
      disp = self.pDispo[val -1]
      for p in disp:
      self.cercle(self.x +p[0], self.y +p[1], self.dim, 'red')
      self.val = val
 
  def cercle(self, x, y, r, coul):
      self.pList.append(self.can.create_oval(x-r, y-r, x+r, y+r, fill=coul))
 
  def effacer(self, flag =0):
      for p in self.pList:
      self.can.delete(p)
      if flag:
      self.can.delete(self.carre)
 
class Projet(Frame):
  def __init__(self, larg, haut):
      Frame.__init__(self)
      self.larg, self.haut = larg, haut
      self.can = Canvas(self, bg='dark green', width =larg, height =haut)
      self.can.pack(padx =5, pady =5)
      # liste des boutons à installer, avec leur gestionnaire :
      bList = [("A", self.boutA), ("B", self.boutB),
	("C", self.boutC), ("Quitter", self.boutQuit)]
      bList.reverse()	       # inverser l'ordre de la liste
      for b in bList:
      Button(self, text =b[0], command =b[1]).pack(side =RIGHT, padx=3)
      self.pack()
      self.des =[]	    # liste qui contiendra les faces de dés
      self.actu =0	    # réf. du dé actuellement sélectionné
 
  def boutA(self):
      if len(self.des):
      return	      # car les dessins existent déjà !
      a, da = 0, 2*pi/13
      for i in range(13):
      cx, cy = self.larg/2, self.haut/2
      x = cx + cx*0.75*sin(a)	       # pour disposer en cercle,
      y = cy + cy*0.75*cos(a)	       # on utilise la trigono !
      self.des.append(FaceDom(self.can, randrange(1,7) , (x,y), 65))
      a += da
 
  def boutB(self):
      # incrémenter la valeur du dé sélectionné. Passer au suivant :
      v = self.des[self.actu].val
      v = v % 6
      v += 1	    
      self.des[self.actu].effacer()
      self.des[self.actu].tracer_points(v)
      self.actu += 1
      self.actu = self.actu % 13
 
  def boutC(self):
      for i in range(len(self.des)):
      self.des[i].effacer(1)
      self.des =[]
      self.actu =0
 
  def boutQuit(self):
      self.master.destroy()
 
Projet(600, 600).mainloop()
```





![](images/100000000000026F000002A26994F415.png)



Exercice 14.1 (Widget combo box complet) :



```python
class ComboFull(Frame):
  "Widget composite 'Combo box' (champ d'entrée + liste 'déroulante')"
  def __init__(self, boss, item='', items=[], command ='', width =10,
	listSize =5):
      Frame.__init__(self, boss)  # constructeur de la classe parente
      self.boss =boss	       # référence du widget 'maître'
      self.items =items      # items à placer dans la boîte de liste
      self.command =command	 # fonction à invoquer après clic ou <enter>
      self.item =item	       # item entré ou sélectionné
      self.listSize =listSize	   # nombre d'items visibles dans la liste
      self.width =width      # largeur du champ d'entrée (en caract.)
 
      # Champ d'entrée :
      self.entree =Entry(self, width =width)	     # largeur en caractères
      self.entree.insert(END, item)
      self.entree.bind("<Return>", self.sortieE)
      self.entree.pack(side =LEFT)
 
      # Bouton pour faire apparaître la liste associée :
      self.gif1 = PhotoImage(file ="down.gif")	     # ! variable persistante
      Button(self, image =self.gif1, width =15, height=15,
	 command =self.popup).pack()
 
  def sortieL(self, event =None):
      # Extraire de la liste l'item qui a été sélectionné :
      index =self.bListe.curselection()      # renvoie un tuple d'index
      ind0 =int(index[0])	      # on ne garde que le premier
      self.item =self.items[ind0]
      # Actualiser le champ d'entrée avec l'item choisi :
      self.entree.delete(0, END)
      self.entree.insert(END, self.item)
      # Exécuter la commande indiquée, avec l'item choisi comme argument :
      self.command(self.item)
      self.pop.destroy()	     # supprimer la fenêtre satellite
 
  def sortieE(self, event =None):
      # Exécuter la commande indiquée, avec l'argument-item encodé tel quel :
      self.command(self.entree.get())
 
  def get(self):
      # Renvoyer le dernier item sélectionné dans la boîte de liste
      return self.item
 
  def popup(self):
      # Faire apparaître la petite fenêtre satellite contenant la liste.
      # On commence par récupérer les coordonnées du coin supérieur gauche
      # du présent widget dans la fenêtre principale :
      xW, yW =self.winfo_x(), self.winfo_y()
      # ... et les coordonnées de la fenêtre principale sur l'écran, grâce à
      # la méthode geometry() qui renvoie une chaîne avec taille et coordo. :
      geo =self.boss.geometry().split("+")
      xF, yF =int(geo[1]), int(geo[2])	   # coord. coin supérieur gauche
      # On peut alors positionner une petite fenêtre, modale et sans bordure,
      # exactement sous le champ d'entrée :
      xP, yP = xF +xW +10, yF +yW +45	   # +45 : compenser haut champ Entry
      self.pop =Toplevel(self)	     # fenêtre secondaire ("pop up")
      self.pop.geometry("+{}+{}".format(xP, yP))    # positionnement / écran
      self.pop.overrideredirect(1)	# => fen. sans bordure ni bandeau
      self.pop.transient(self.master)	   # => fen. 'modale'
 
      # Boîte de liste, munie d'un 'ascenseur' (scroll bar) :
      cadreLB =Frame(self.pop)	     # cadre pour l'ensemble des 2
      self.bListe =Listbox(cadreLB, height=self.listSize, width=self.width-1)
      scrol =Scrollbar(cadreLB, command =self.bListe.yview)
      self.bListe.config(yscrollcommand =scrol.set)
      self.bListe.bind("<ButtonRelease-1>", self.sortieL)
      self.bListe.pack(side =LEFT)
      scrol.pack(expand =YES, fill =Y)
      cadreLB.pack()
      # Remplissage de la boîte de liste avec les items fournis :
      for it in self.items:
      self.bListe.insert(END, it)
 
if __name__ =="__main__":	   # --- Programme de test ---
  def changeCoul(col):
      fen.configure(background = col)
 
  def changeLabel():
      lab.configure(text = combo.get())
 
  couleurs = ('navy', 'royal blue', 'steelblue1', 'cadet blue',
	  'lawn green', 'forest green', 'yellow', 'dark red',
	  'grey80','grey60', 'grey40', 'grey20', 'pink')
  fen =Tk()
  combo =ComboFull(fen, item ="néant", items =couleurs, command =changeCoul,
	  width =15, listSize =6)
  combo.grid(row =1, columnspan =2, padx =10, pady =10)
  bou = Button(fen, text ="Test", command =changeLabel)
  bou.grid(row =3, column =0, padx =8, pady =8)
  lab = Label(fen, text ="Bonjour", bg ="ivory", width =15)
  lab.grid(row =3, column =1, padx =8)
  fen.mainloop()
```





![](images/10000000000000EA000000771F15F883.png)



Exercice 16.1 (Création de la base de données « musique ») :



```python
# Création et Alimentation d'une petite base de données SQLite 
 
import sqlite3 
 
# Établissement de la connexion - Création du curseur : 
connex = sqlite3.connect("musique.sq3") 
cur = connex.cursor() 
# Création des tables. L'utilisation de try/except permet de ré-utiliser le 
# script indéfiniment, même si la base de données existe déjà. 
try: 
  req ="CREATE TABLE compositeurs(comp TEXT, a_naiss INTEGER, "\ 
    "a_mort INTEGER)" 
  cur.execute(req) 
  req ="CREATE TABLE oeuvres(comp TEXT, titre TEXT, duree INTEGER, "\ 
    "interpr TEXT)" 
  cur.execute(req) 
except: 
  pass		 # Les tables existent certainement déjà => on continue.
 
print("Entrée des enregistrements, table des compositeurs :") 
while 1: 
  nom = input("Nom du compositeur (<Enter> pour terminer) : ") 
  if nom =='': 
      break 
  aNais = input("Année de naissance : ") 
  aMort = input("Année de mort : ") 
  req ="INSERT INTO compositeurs (comp, a_naiss, a_mort) VALUES (?, ?, ?)" 
  cur.execute(req, (nom, aNais, aMort)) 
 
print("Rappel des infos introduites :") 
cur.execute("select * from compositeurs") 
for enreg in cur: 
  print(enreg) 
 
print("Entrée des enregistrements, table des oeuvres musicales :") 
while 1: 
  nom = input("Nom du compositeur (<Enter> pour terminer) : ") 
  if nom =='': 
      break 
  titre = input("Titre de l'oeuvre : ") 
  duree = input("durée (minutes) : ") 
  inter = input("interprète principal : ") 
 req ="INSERT INTO oeuvres (comp, titre, duree, interpr) "\ 
    "VALUES (?, ?, ?, ?)" 
  cur.execute(req, (nom, titre, duree, inter)) 
 
print("Rappel des infos introduites :") 
cur.execute("select * from oeuvres") 
for enreg in cur: 
  print(enreg) 
 
# Transfert effectif des enregistrements dans la BD : 
connex.commit()
```



Exercice 18.2 :



```python
#####################################
# Bombardement d'une cible mobile   #
# (C) G. Swinnen - Avril 2004 - GPL #
#####################################
 
from tkinter import *
from math import sin, cos, pi
from random import randrange
from threading import Thread
import time		  # seulement pour le variante avec sleep()
 
class Canon:
  """Petit canon graphique"""
  def __init__(self, boss, num, x, y, sens):
      self.boss = boss	     # référence du canevas
      self.num = num	      # n° du canon dans la liste
      self.x1, self.y1 = x, y	   # axe de rotation du canon
      self.sens = sens	     # sens de tir (-1:gauche, +1:droite)
      self.lbu = 30	     # longueur de la buse
      # dessiner la buse du canon (horizontale) :
      self.x2, self.y2 = x + self.lbu * sens, y
      self.buse = boss.create_line(self.x1, self.y1,
		   self.x2, self.y2, width =10)
      # dessiner le corps du canon (cercle de couleur) :
      self.rc = 15	    # rayon du cercle 
      self.corps = boss.create_oval(x -self.rc, y -self.rc, x +self.rc,
		    y +self.rc, fill ='black')
      # pré-dessiner un obus (au départ c'est un simple point) :
      self.obus = boss.create_oval(x, y, x, y, fill='red')
      self.anim = 0
      # retrouver la largeur et la hauteur du canevas :
      self.xMax = int(boss.cget('width'))
      self.yMax = int(boss.cget('height'))
 
  def orienter(self, angle):
      "régler la hausse du canon"
      # rem : le paramètre <angle> est reçu en tant que chaîne.
      # il faut donc le traduire en réel, puis le convertir en radians :
      self.angle = float(angle)*2*pi/360      
      self.x2 = self.x1 + self.lbu * cos(self.angle) * self.sens
      self.y2 = self.y1 - self.lbu * sin(self.angle)
      self.boss.coords(self.buse, self.x1, self.y1, self.x2, self.y2)
 
  def feu(self):
      "déclencher le tir d'un obus"
      # référence de l'objet cible :
      self.cible = self.boss.master.cible
      if self.anim ==0:
      self.anim =1
      # position de départ de l'obus (c'est la bouche du canon) :
      self.xo, self.yo = self.x2, self.y2
      v = 20	      # vitesse initiale
      # composantes verticale et horizontale de cette vitesse :
      self.vy = -v *sin(self.angle)
      self.vx = v *cos(self.angle) *self.sens
      self.animer_obus()
 
  def animer_obus(self):
      "animer l'obus (trajectoire balistique)"
      # positionner l'obus, en re-définissant ses coordonnées :
      self.boss.coords(self.obus, self.xo -3, self.yo -3,
		  self.xo +3, self.yo +3)
      if self.anim >0:
      # calculer la position suivante :
      self.xo += self.vx
      self.yo += self.vy
      self.vy += .5
      self.test_obstacle()	  # a-t-on atteint un obstacle ?
      self.boss.after(15, self.animer_obus)
      else:
      # fin de l'animation :
      self.boss.coords(self.obus, self.x1, self.y1, self.x1, self.y1) 
 
  def test_obstacle(self):
      "évaluer si l'obus a atteint une cible ou les limites du jeu"
      if self.yo >self.yMax or self.xo <0 or self.xo >self.xMax:
      self.anim =0
      return
      if self.yo > self.cible.y -3 and self.yo < self.cible.y +18 \
      and self.xo > self.cible.x -3 and self.xo < self.cible.x +43:
      # dessiner l'explosion de l'obus (cercle orange) :
      self.explo = self.boss.create_oval(self.xo -10,
	    self.yo -10, self.xo +10, self.yo +10,
	    fill ='orange', width =0)
      self.boss.after(150, self.fin_explosion)
      self.anim =0
 
  def fin_explosion(self):
      "effacer le cercle d'explosion - gérer le score"
      self.boss.delete(self.explo)
      # signaler le succès à la fenêtre maîtresse :
      self.boss.master.goal()	      
 
class Pupitre(Frame):
  """Pupitre de pointage associé à un canon""" 
  def __init__(self, boss, canon):
      Frame.__init__(self, bd =3, relief =GROOVE)
      self.score =0
      s =Scale(self, from_ =88, to =65,
	troughcolor ='dark grey',
	command =canon.orienter)
      s.set(45) 	     # angle initial de tir
      s.pack(side =LEFT)
      Label(self, text ='Hausse').pack(side =TOP, anchor =W, pady =5)	      
      Button(self, text ='Feu !', command =canon.feu).\
		  pack(side =BOTTOM, padx =5, pady =5)
      Label(self, text ="points").pack()
      self.points =Label(self, text=' 0 ', bg ='white')
      self.points.pack()
      # positionner à gauche ou à droite suivant le sens du canon :
      gd =(LEFT, RIGHT)[canon.sens == -1]
      self.pack(padx =3, pady =5, side =gd)
 
  def attribuerPoint(self, p):
      "incrémenter ou décrémenter le score"
      self.score += p
      self.points.config(text = ' %s ' % self.score)
 
class Cible:
  """objet graphique servant de cible"""
  def __init__(self, can, x, y):
      self.can = can	     # référence du canevas
      self.x, self.y = x, y
      self.cible = can.create_oval(x, y, x+40, y+15, fill ='purple')
 
  def deplacer(self, dx, dy):
      "effectuer avec la cible un déplacement dx,dy" 
      self.can.move(self.cible, dx, dy)
      self.x += dx
      self.y += dy
      return self.x, self.y
 
class Thread_cible(Thread):
  """objet thread gérant l'animation de la cible"""
  def __init__(self, app, cible):
      Thread.__init__(self)
      self.cible = cible      # objet à déplacer
      self.app = app	      # réf. de la fenêtre d'application
      self.sx, self.sy = 6, 3	   # incréments d'espace et de
      self.dt =300	    # temps pour l'animation (ms)
 
  def run(self):
      "animation, tant que la fenêtre d'application existe" 
      x, y = self.cible.deplacer(self.sx, self.sy)
      if x > self.app.xm -50 or x < self.app.xm /5:
	  self.sx = -self.sx
      if y < self.app.ym /2 or y > self.app.ym -20:
	  self.sy = -self.sy
      if self.app != None:
      self.app.after(int(self.dt), self.run)
 
  def stop(self):
      "fermer le thread si la fenêtre d'application est refermée"
      self.app =None
 
  def accelere(self):
      "accélérer le mouvement"
      self.dt /= 1.5
      self.app.bell()	       # beep sonore
 
class Application(Frame):
  def __init__(self):
      Frame.__init__(self)
      self.master.title('<<< Tir sur cible mobile >>>')
      self.pack()
      self.xm, self.ym = 600, 500
      self.jeu = Canvas(self, width =self.xm, height =self.ym,
	     bg ='ivory', bd =3, relief =SUNKEN)
      self.jeu.pack(padx =4, pady =4, side =TOP)
 
      # Instanciation d'un canon et d'un pupitre de pointage :
      x, y = 30, self.ym -20
      self.gun =Canon(self.jeu, 1, x, y, 1)
      self.pup =Pupitre(self, self.gun)
 
      # instanciation de la cible mobile :
      self.cible = Cible(self.jeu, self.xm/2, self.ym -25)
      # animation de la cible mobile, sur son propre thread :
      self.tc = Thread_cible(self, self.cible)
      self.tc.start()
      # arrêter tous les threads lorsque l'on ferme la fenêtre :
      self.bind('<Destroy>',self.fermer_threads)
 
  def goal(self):
      "la cible a été touchée"
      self.pup.attribuerPoint(1)
      self.tc.accelere()
 
  def fermer_threads(self, evt):
      "arrêter le thread d'animation de la cible"
      self.tc.stop()
 
if __name__ =='__main__':
  Application().mainloop()
```



Variante, utilisant une temporisation de la cible à l'aide de
Time.sleep() :



```python
class Thread_cible(Thread): 
  """objet thread gérant l'animation de la cible""" 
  def __init__(self, app, cible): 
      Thread.__init__(self) 
      self.cible = cible      # objet à déplacer 
      self.app = app	      # réf. de la fenêtre d'application 
      self.sx, self.sy = 6, 3	   # incréments d'espace et de 
----->	  self.dt =.3		# temps pour l'animation 
 
  def run(self): 
      "animation, tant que la fenêtre d'application existe" 
----->	  while self.app != None: 
      x, y = self.cible.deplacer(self.sx, self.sy) 
      if x > self.app.xm -50 or x < self.app.xm /5: 
	  self.sx = -self.sx 
      if y < self.app.ym /2 or y > self.app.ym -20: 
	  self.sy = -self.sy 
--------->  time.sleep(self.dt) 
```





![](images/image56.png)



