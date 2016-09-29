## 16-A - Les boutons radio

Les widgets « boutons radio » permettent de proposer à l'utilisateur un
ensemble de choix mutuellement exclusifs. On les appelle ainsi par
analogie avec les boutons de sélection que l'on trouvait jadis sur les
postes de radio. Ces boutons étaient conçus de telle manière qu'un seul
à la fois pouvait être enfoncé : tous les autres ressortaient
automatiquement.



![](images/image45.png)





```python
from tkinter import *
 
class RadioDemo(Frame):
  """Démo : utilisation de widgets 'boutons radio'"""
  def __init__(self, boss =None):
      """Création d'un champ d'entrée avec 4 boutons radio"""
      Frame.__init__(self)
      self.pack()
      # Champ d'entrée contenant un petit texte :
      self.texte = Entry(self, width =30, font ="Arial 14")
      self.texte.insert(END, "La programmation, c'est génial")
      self.texte.pack(padx =8, pady =8)
      # Nom français et nom technique des quatre styles de police :	       
      stylePoliceFr =["Normal", "Gras", "Italique", "Gras/Italique"]
      stylePoliceTk =["normal", "bold", "italic"  , "bold italic"]
      # Le style actuel est mémorisé dans un 'objet-variable' tkinter ;
      self.choixPolice = StringVar()
      self.choixPolice.set(stylePoliceTk[0])
      # Création des quatre 'boutons radio' :
      for n in range(4):
      bout = Radiobutton(self,
		 text = stylePoliceFr[n],
		 variable = self.choixPolice,
		 value = stylePoliceTk[n],
		 command = self.changePolice)
      bout.pack(side =LEFT, padx =5)
 
  def changePolice(self):
      """Remplacement du style de la police actuelle"""
      police = "Arial 15 " + self.choixPolice.get() 
      self.texte.configure(font =police)
 
if __name__ == '__main__':
  RadioDemo().mainloop()
```



### 16-A-1 - Commentaires {#article.xml#Ld0e50074 .TitreSection2}

-   Ligne 3 : Cette fois encore, nous préférons construire notre petite
    application comme une classe dérivée de la classe **Frame()**, ce
    qui nous permettrait éventuellement de l'intégrer sans difficulté
    dans une application plus importante.
-   Ligne 8 : En général, on applique les méthodes de positionnement des
    widgets (**pack()**, **grid()**, ou **place()**) après instanciation
    de ceux-ci, ce qui permet de choisir librement leur disposition à
    l'intérieur des fenêtres maîtresses. Comme nous le montrons ici, il
    est cependant tout à fait possible de déjà prévoir ce positionnement
    dans le constructeur du widget.
-   Ligne 11 : Les widgets de la classe **Entry** disposent de plusieurs
    méthodes pour accéder à la chaîne de caractères affichée. La méthode
    **get()** permet de récupérer la chaîne entière. La méthode
    **insert()** permet d'insérer de nouveaux caractères à un
    emplacement quelconque (c'est-à-dire au début, à la fin, ou même à
    l'intérieur d'une chaîne préexistante éventuelle). Cette méthode
    s'utilise donc avec deux arguments, le premier indiquant
    l'emplacement de l'insertion (utilisez **0** pour insérer au début,
    **END** pour insérer à la fin, ou encore un indice numérique
    quelconque pour désigner un caractère dans la chaîne). La méthode
    **delete()** permet d'effacer tout ou partie de la chaîne. Elle
    s'utilise avec les mêmes arguments que la précédente (cf. projet «
    Code des couleurs », page ).
-   Lignes 14-15 : Plutôt que de les instancier dans des instructions
    séparées, nous préférons créer nos quatre boutons à l'aide d'une
    boucle. Les options spécifiques à chacun d'eux sont d'abord
    préparées dans les deux listes **stylePoliceFr** et
    **stylePoliceTk** : la première contient les petits textes qui
    devront s'afficher en regard de chaque bouton, et la seconde les
    valeurs qui devront leur être associées.
-   Lignes 17-18 : Comme expliqué à la page précédente, les quatre
    boutons forment un groupe autour d'une variable commune. Cette
    variable prendra la valeur associée au bouton radio que
    l'utilisateur décidera de choisir. Nous ne pouvons cependant pas
    utiliser une variable ordinaire pour remplir ce rôle, parce que les
    attributs internes des objets tkinter ne sont accessibles qu'au
    travers de méthodes spécifiques. Une fois de plus, nous utilisons
    donc ici un *objet-variable* tkinter, de type chaîne de caractères,
    que nous instancions à partir de la classe **StringVar()**, et
    auquel nous donnons une valeur par défaut à la ligne 18.
-   Lignes 20 à 26 : Instanciation des quatre boutons radio. Chacun
    d'entre eux se voit attribuer une étiquette et une valeur
    différentes, mais tous sont associés à la même variable tkinter
    commune (**self.choixPolice**). Tous invoquent également la même
    méthode **self.changePolice()**, chaque fois que l'utilisateur
    effectue un clic de souris sur l'un ou l'autre.
-   Lignes 28 à 31 : Le changement de police s'obtient par
    re-configuration de l'option **font** du widget **Entry**. Cette
    option attend un tuple contenant le nom de la police, sa taille, et
    éventuellement son style. Si le nom de la police ne contient pas
    d'espaces, le tuple peut aussi être remplacé par une chaîne de
    caractères. Exemples :\
    **('Arial', 12,
    'italic')**\
    **('Helvetica',
    10)**\
    **('Times
    New Roman', 12, 'bold
    italic')**\
    `"Verdana 14 bold"`\
    **"President 18 italic" (**Voyez également les exemples de la
    page ).

