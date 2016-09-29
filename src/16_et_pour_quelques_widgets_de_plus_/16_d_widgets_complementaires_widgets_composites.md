## 16-D - Widgets complémentaires, widgets composites

Si vous explorez la volumineuse documentation que l'on peut trouver sur
l'internet concernant *tkinter*, vous vous rendrez compte qu'il en
existe différentes extensions, sous la forme de bibliothèques annexes.
Ces extensions vous proposent des classes de widgets supplémentaires qui
peuvent se révéler très précieuses pour le développement rapide
d'applications complexes. Nous ne pouvons évidemment pas nous permettre
de présenter tous ces ces widgets dans le cadre restreint de ce cours
d'initiation. Si vous êtes intéressés, veuillez consulter les sites web
traitant des bibliothèques **Tix** et **Ttk** (entre entres). La
bibliothèque **Tix** propose plus de 40 widgets complémentaires. La
bibliothèque **Ttk** est plutôt destinée à « habiller » les widgets avec
différents thèmes (styles de boutons, de fenêtres, etc.). Certaines de
ces bibliothèques sont écrites entièrement en Python, comme par exemple
**Pmw** (*Python Mega Widgets*).

Vous pouvez cependant faire une multitude de choses sans chercher
d'autres ressources que la bibliothèque standard *tkinter*. Vous pouvez
en effet assez aisément construire vous-même de nouvelles classes de
widgets composites adaptées à vos besoins. Cela peut vous demander un
certain travail au départ, mais en procédant ainsi, vous contrôlez très
précisément ce que contiennent vos applications, et vous garantissez la
portabilité de celles-ci sur tous les systèmes qui acceptent Python,
puisque *tkinter* fait partie de la distribution standard du langage.
Lorsque vous utilisez des bibliothèques tierces, en effet, vous devez
toujours vérifier la disponibilité et la compatibilité de celles-ci pour
les machines cibles de vos programmes, et prévoir leur installation si
nécessaire.

Les pages qui suivent vous expliquent les principes généraux à mettre en
œuvre pour réaliser vous-même des classes de widgets composites, avec
quelques exemples parmi les plus utiles.

### 16-D-1 - Combo box simplifié {#article.xml#Ld0e52258 .TitreSection2}

La petite application ci-après vous montre comment construire une
nouvelle classe de widget de type **Combo box**. On appelle ainsi un
widget qui associe un champ d'entrée à une boîte de liste :
l'utilisateur de ce widget peut entrer dans le système, soit un des
éléments de la liste proposée (en cliquant sur son nom), soit un élément
non répertorié (en entrant un nouveau nom dans le champ d'entrée). Nous
avons un peu simplifié le problème en laissant la liste visible en
permanence, mais il est parfaitement possible de perfectionner ce widget
pour qu'il prenne la forme classique d'un champ d'entrée assorti d'un
petit bouton provoquant l'apparition de la liste, celle-ci étant cachée
au départ. (*Voir exercice 14.1, page* ).

Tel que nous l'imaginons, notre widget combo va donc regrouper en une
seule entité trois widgets de base tkinter : un champ d'entrée, une
boîte de liste (*listbox*) et un « ascenseur » (barre de défilement
vertical ou *scrollbar*).

La boîte de liste et son ascenseur seront étroitement associés, puisque
l'ascenseur permet de faire défiler la liste dans sa boîte. Il faudra
d'ailleurs s'assurer que l'ascenseur ait toujours la même hauteur que la
boîte, quelle que soit la taille choisie pour celle-ci.



![](images/image50.png)



Pour tester celui-ci, nous l'incluons dans une petite application très
simple : lorsque l'utilisateur choisit une couleur dans la liste (il
peut aussi entrer un nom de couleur directement dans le champ d'entrée),
cette couleur devient automatiquement la couleur de fond pour la fenêtre
maîtresse.

Dans cette fenêtre maîtresse, nous avons ajouté un libellé et un bouton,
afin de vous montrer comment vous pouvez accéder à la sélection opérée
précédemment dans le **ComboBox** lui-même (le bouton provoque
l'affichage du nom de la dernière couleur choisie).



1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    class ComboBox(Frame): 
    ```

4.  ``` {.LignePreCode}
      "Widget composite associant un champ d'entrée avec une boîte de liste" 
    ```

5.  ``` {.LignePreCode}
      def __init__(self, boss, item='', items=[], command ='', width =10, 
    ```

6.  ``` {.LignePreCode}
    	listSize =5): 
    ```

7.  ``` {.LignePreCode}
          Frame.__init__(self, boss)   # constructeur de la classe parente 
    ```

8.  ``` {.LignePreCode}
    		   # ( est la réf. du widget 'maître') 
    ```

9.  ``` {.LignePreCode}
          self.items =items       # items à placer dans la boîte de liste 
    ```

10. ``` {.LignePreCode}
          self.command =command	  # fonction à invoquer après clic ou  
    ```

11. ``` {.LignePreCode}
          self.item =item		# item entré ou sélectionné 
    ```

12. ``` {.LignePreCode}
      
    ```

13. ``` {.LignePreCode}
          # Champ d'entrée : 
    ```

14. ``` {.LignePreCode}
          self.entree =Entry(self, width =width)	      # largeur en caractères 
    ```

15. ``` {.LignePreCode}
          self.entree.insert(END, item) 
    ```

16. ``` {.LignePreCode}
          self.entree.bind("<Return>", self.sortieE) 
    ```

17. ``` {.LignePreCode}
          self.entree.pack(side =TOP) 
    ```

18. ``` {.LignePreCode}
      
    ```

19. ``` {.LignePreCode}
          # Boîte de liste, munie d'un 'ascenseur' (scroll bar) : 
    ```

20. ``` {.LignePreCode}
          cadreLB =Frame(self)	     # cadre pour l'ensemble des 2 
    ```

21. ``` {.LignePreCode}
          self.bListe =Listbox(cadreLB, height =listSize, width =width-1) 
    ```

22. ``` {.LignePreCode}
          scrol =Scrollbar(cadreLB, command =self.bListe.yview) 
    ```

23. ``` {.LignePreCode}
          self.bListe.config(yscrollcommand =scrol.set) 
    ```

24. ``` {.LignePreCode}
          self.bListe.bind("<ButtonRelease-1>", self.sortieL) 
    ```

25. ``` {.LignePreCode}
          self.bListe.pack(side =LEFT) 
    ```

26. ``` {.LignePreCode}
          scrol.pack(expand =YES, fill =Y) 
    ```

27. ``` {.LignePreCode}
          cadreLB.pack() 
    ```

28. ``` {.LignePreCode}
      
    ```

29. ``` {.LignePreCode}
          # Remplissage de la boîte de liste avec les items fournis : 
    ```

30. ``` {.LignePreCode}
          for it in items: 
    ```

31. ``` {.LignePreCode}
          self.bListe.insert(END, it) 
    ```

32. ``` {.LignePreCode}
      
    ```

33. ``` {.LignePreCode}
      def sortieL(self, event =None): 
    ```

34. ``` {.LignePreCode}
          # Extraire de la liste l'item qui a été sélectionné : 
    ```

35. ``` {.LignePreCode}
          index =self.bListe.curselection()      # renvoie un tuple d'index 
    ```

36. ``` {.LignePreCode}
          ind0 =int(index[0])	      # on ne garde que le premier 
    ```

37. ``` {.LignePreCode}
          self.item =self.items[ind0] 
    ```

38. ``` {.LignePreCode}
          # Actualiser le champ d'entrée avec l'item choisi : 
    ```

39. ``` {.LignePreCode}
          self.entree.delete(0, END) 
    ```

40. ``` {.LignePreCode}
          self.entree.insert(END, self.item) 
    ```

41. ``` {.LignePreCode}
          # Exécuter la commande indiquée, avec l'item choisi comme argument : 
    ```

42. ``` {.LignePreCode}
          self.command(self.item) 
    ```

43. ``` {.LignePreCode}
      
    ```

44. ``` {.LignePreCode}
      def sortieE(self, event =None): 
    ```

45. ``` {.LignePreCode}
          # Exécuter la commande indiquée, avec l'argument-item encodé tel quel : 
    ```

46. ``` {.LignePreCode}
          self.command(self.entree.get()) 
    ```

47. ``` {.LignePreCode}
      
    ```

48. ``` {.LignePreCode}
      def get(self): 
    ```

49. ``` {.LignePreCode}
          # Renvoyer le dernier item sélectionné dans la boîte de liste 
    ```

50. ``` {.LignePreCode}
          return self.item 
    ```

51. ``` {.LignePreCode}
      
    ```

52. ``` {.LignePreCode}
    if __name__ =="__main__":	    # --- Programme de test --- 
    ```

53. ``` {.LignePreCode}
      def changeCoul(col): 
    ```

54. ``` {.LignePreCode}
          fen.configure(background = col) 
    ```

55. ``` {.LignePreCode}
      
    ```

56. ``` {.LignePreCode}
      def changeLabel(): 
    ```

57. ``` {.LignePreCode}
          lab.configure(text = combo.get()) 
    ```

58. ``` {.LignePreCode}
      
    ```

59. ``` {.LignePreCode}
      couleurs = ('navy', 'royal blue', 'steelblue1', 'cadet blue', 
    ```

60. ``` {.LignePreCode}
    	  'lawn green', 'forest green', 'yellow', 'dark red', 
    ```

61. ``` {.LignePreCode}
    	  'grey80','grey60', 'grey40', 'grey20', 'pink') 
    ```

62. ``` {.LignePreCode}
      fen =Tk() 
    ```

63. ``` {.LignePreCode}
      combo =ComboBox(fen, item ="néant", items =couleurs, command =changeCoul, 
    ```

64. ``` {.LignePreCode}
    	  width =15, listSize =6) 
    ```

65. ``` {.LignePreCode}
      combo.grid(row =1, columnspan =2, padx =10, pady =10) 
    ```

66. ``` {.LignePreCode}
      bou = Button(fen, text ="Test", command =changeLabel) 
    ```

67. ``` {.LignePreCode}
      bou.grid(row =2, column =0, padx =8, pady =8) 
    ```

68. ``` {.LignePreCode}
      lab = Label(fen, text ="Bonjour", bg ="ivory", width =15) 
    ```

69. ``` {.LignePreCode}
      lab.grid(row =2, column =1, padx =8) 
    ```

70. ``` {.LignePreCode}
      fen.mainloop() 
    ```



#### 16-D-1-A - Commentaires {#article.xml#Ld0e53703 .TitreSection3}

-   Lignes 5-8 : Le constructeur de notre widget attend la référence du
    widget maître (*boss*) comme premier paramètre, suivant la
    convention habituelle. Les autres paramètres permettent notamment de
    prévoir un texte par défaut dans le champ d'entrée (*item*), de
    fournir la liste des éléments à insérer dans la boîte (*items*), et
    de désigner la fonction à invoquer lorsque l'utilisateur effectuera
    un clic dans la liste, ou enfoncera la touche \<enter\> de son
    clavier (*command*). Nous avons conservé des noms anglais pour ces
    paramètres, afin que notre widget puisse être utilisé avec les mêmes
    conventions que les widgets de base dont il dérive.
-   Lignes 15, 39, 40 : Les méthodes du widget Entry ont déjà été
    décrites précédemment (cf. page ). Rappelons simplement que la
    méthode **insert()** permet d'insérer du texte dans le champ, sans
    faire disparaître un texte préexistant éventuel. Le premier argument
    permet de préciser à quel endroit du texte préexistant l'insertion
    doit avoir lieu. Ce peut être un entier, ou bien une valeur
    symbolique (en important l'ensemble du module tkinter à la ligne 1,
    on a importé une série de variables globales, dont END, qui
    contiennent ces valeurs symboliques, et END désigne bien entendu la
    fin du texte préexistant).
-   Lignes 16 et 24 : deux événements seront associés à des méthodes
    locales : le fait de relâcher le bouton droit de la souris alors que
    son pointeur se trouve dans la boîte de liste (événement `<ButtonRelease-1>`) et le fait
    d'enfoncer la touche \<enter\> (événement `<Return>`).
-   Ligne 21 : création de la boîte de liste (classe de base
    **Listbox**). Sa largeur s'exprime en nombre de caractères de la
    police courante. On en retranche un ou deux, afin de compenser
    approximativement la place qu'occupera l'ascenseur ci-après
    (l'ensemble des deux devant avoir à peu près la même largeur que le
    champ d'entrée).
-   Ligne 22 : création de la barre de défilement verticale (classe de
    base **Scrollbar**). La commande qu'on lui associe :` command =self.bListe.yview `indique
    la méthode du widget *Listbox* qui sera invoquée pour provoquer le
    défilement de la liste dans la boîte, lorsque l'on actionnera cet
    ascenseur.
-   Ligne 23 : symétriquement, on doit re-configurer la boîte de liste
    pour lui indiquer quelle méthode du widget *Scrollbar* elle devra
    invoquer afin que la position de l'ascenseur soit le reflet correct
    de la position relative de l'item couramment sélectionné dans la
    liste. Il n'était pas possible d'indiquer déjà cette commande dans
    la ligne d'instruction créant la boîte de liste, à la ligne 21, car
    à ce moment-là le widget *Scrollbar* n'existait pas encore. Y faire
    référence était donc exclu[^note_81].
-   Ligne 33 : cette méthode est invoquée chaque fois que l'utilisateur
    sélectionne un élément dans la liste. Elle fait appel à la méthode
    **curselection()** du widget *Listbox* de base, laquelle lui renvoie
    un tuple d'indices, car il a été prévu par les développeurs de
    *tkinter* que l'utilisateur puisse avoir sélectionné plusieurs items
    dans la liste (à l'aide de la touche \<ctrl\>). Nous supposerons
    cependant ici qu'un seul a été pointé, et récupérons donc seulement
    le premier élément de ce tuple. À la ligne 47, nous pouvons alors
    extraire l'item correspondant de la liste et l'utiliser, à la fois
    pour mettre à jour le champ d'entrée (lignes 39-40), ainsi que comme
    argument pour exécuter la commande (ligne 42) dont la référence
    avait été fournie lors de l'instanciation du widget (dans le cas de
    notre petite application, ce sera donc la fonction
    **changeCoul()**).
-   Lignes 44-46 : la même commande est invoquée lorsque l'utilisateur
    actionne la touche \<enter\> après avoir encodé une chaîne de
    caractères dans le champ d'entrée. Le paramètre **event**, non
    utilisé ici, permettrait de récupérer le ou les événements associés.
-   Lignes 48-49 : nous avons aussi inclus une méthode **get()**,
    suivant la convention suivie par d'autres widgets, afin de permettre
    la récupération libre du dernier item sélectionné.

### 16-D-2 - Le widget Text assorti d'un ascenseur {#article.xml#Ld0e53805 .TitreSection2}

En procédant de la même manière que dans l'exemple précédent, vous
pouvez associer les widgets standard *tkinter* de multiples façons.
Ainsi nous vous présentons ci-après un widget composite qui pourrait
vous servir à ébaucher un système de traitement de textes rudimentaire.
Son principal composant est le widget **Text** standard, lequel peut
afficher des textes formatés, c'est-à-dire des textes intégrant divers
attributs de style, comme par exemple le gras, l'italique, l'exposant
..., ainsi que des polices de caractères différentes, de la couleur, et
même des images. Nous l'avons simplement associé à une barre de
défilement verticale pour vous montrer une fois de plus les interactions
que vous pouvez créer entre ces composants.



![](images/image51.png)



Par exemple, dans l'application décrite ci-après, le fait de cliquer sur
le nom « Jean de la Fontaine », à l'aide du bouton droit de la souris,
provoque le défilement automatique du texte (*scrolling*), jusqu'à ce
qu'une rubrique décrivant cet auteur devienne visible dans le widget
(voir le script correspondant page suivante). D'autres fonctionnalités
sont présentes, telles la possibilité de sélectionner à l'aide de la
souris n'importe quelle portion du texte affiché pour lui faire subir un
traitement quelconque, mais nous ne présenterons ici que les plus
fondamentales. Veuillez donc consulter les ouvrages ou sites web
spécialisés pour en savoir davantage.

#### 16-D-2-A - Gestion du texte affiché {#article.xml#Ld0e53822 .TitreSection3}

Vous pouvez accéder à n'importe quelle portion du texte pris en charge
par un widget **Text** grâce à deux concepts complémentaires, les
***index*** et les ***balises*** :

-   Chaque caractère du texte affiché est référencé par un *index*,
    lequel doit être une chaîne de caractères contenant deux valeurs
    numériques reliées par un point (ex : `"5.2"`). Ces deux valeurs indiquent
    respectivement le numéro de ligne et le numéro de colonne où se
    situe le caractère.
-   N'importe quelle portion du texte peut être associée à une ou
    plusieurs *balise(s)*, dont vous choisissez librement le nom et les
    propriétés. Celles-ci vous permettent de définir la police, les
    couleurs d'avant- et d'arrière-plan, les événements associés, etc.

> Pour la bonne compréhension du script ci-dessous, veuillez considérer
> que le texte de la fable traitée doit être accessible, dans un fichier
> nommé **CorbRenard.txt**, encodé en latin-1.



1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    class ScrolledText(Frame): 
    ```

4.  ``` {.LignePreCode}
      """Widget composite, associant un widget Text et une barre de défilement""" 
    ```

5.  ``` {.LignePreCode}
      def __init__(self, boss, baseFont ="Times", width =50, height =25): 
    ```

6.  ``` {.LignePreCode}
          Frame.__init__(self, boss, bd =2, relief =SUNKEN) 
    ```

7.  ``` {.LignePreCode}
          self.text =Text(self, font =baseFont, bg ='ivory', bd =1, 
    ```

8.  ``` {.LignePreCode}
    	      width =width, height =height) 
    ```

9.  ``` {.LignePreCode}
          scroll =Scrollbar(self, bd =1, command =self.text.yview) 
    ```

10. ``` {.LignePreCode}
          self.text.configure(yscrollcommand =scroll.set) 
    ```

11. ``` {.LignePreCode}
          self.text.pack(side =LEFT, expand =YES, fill =BOTH, padx =2, pady =2) 
    ```

12. ``` {.LignePreCode}
          scroll.pack(side =RIGHT, expand =NO, fill =Y, padx =2, pady =2) 
    ```

13. ``` {.LignePreCode}
      
    ```

14. ``` {.LignePreCode}
      def importFichier(self, fichier, encodage ="Utf8"): 
    ```

15. ``` {.LignePreCode}
          "insertion d'un texte dans le widget, à partir d'un fichier" 
    ```

16. ``` {.LignePreCode}
          of =open(fichier, "r", encoding =encodage) 
    ```

17. ``` {.LignePreCode}
          lignes =of.readlines() 
    ```

18. ``` {.LignePreCode}
          of.close() 
    ```

19. ``` {.LignePreCode}
          for li in lignes: 
    ```

20. ``` {.LignePreCode}
          self.text.insert(END, li) 
    ```

21. ``` {.LignePreCode}
      
    ```

22. ``` {.LignePreCode}
    def chercheCible(event=None): 
    ```

23. ``` {.LignePreCode}
      "défilement du texte jusqu'à la balise , grâce à la méthode see()" 
    ```

24. ``` {.LignePreCode}
      index = st.text.tag_nextrange('cible', '0.0', END) 
    ```

25. ``` {.LignePreCode}
      st.text.see(index[0]) 
    ```

26. ``` {.LignePreCode}
      
    ```

27. ``` {.LignePreCode}
    ### Programme principal : fenêtre avec un libellé et un 'ScrolledText' ### 
    ```

28. ``` {.LignePreCode}
    fen =Tk() 
    ```

29. ``` {.LignePreCode}
    lib =Label(fen, text ="Widget composite : Text + Scrollbar", 
    ```

30. ``` {.LignePreCode}
         font ="Times 14 bold italic", fg ="navy") 
    ```

31. ``` {.LignePreCode}
    lib.pack(padx =10, pady =4) 
    ```

32. ``` {.LignePreCode}
    st =ScrolledText(fen, baseFont="Helvetica 12 normal", width =40, height =10) 
    ```

33. ``` {.LignePreCode}
    st.pack(expand =YES, fill =BOTH, padx =8, pady =8) 
    ```

34. ``` {.LignePreCode}
      
    ```

35. ``` {.LignePreCode}
    # Définition de balises, liaison d'un événement  : 
    ```

36. ``` {.LignePreCode}
    st.text.tag_configure("titre", foreground ="brown", 
    ```

37. ``` {.LignePreCode}
    	    font ="Helvetica 11 bold italic") 
    ```

38. ``` {.LignePreCode}
    st.text.tag_configure("lien", foreground ="blue", 
    ```

39. ``` {.LignePreCode}
    	    font ="Helvetica 11 bold") 
    ```

40. ``` {.LignePreCode}
    st.text.tag_configure("cible", foreground ="forest green", 
    ```

41. ``` {.LignePreCode}
    	    font ="Times 11 bold") 
    ```

42. ``` {.LignePreCode}
    st.text.tag_bind("lien", "<Button-3>", chercheCible) 
    ```

43. ``` {.LignePreCode}
      
    ```

44. ``` {.LignePreCode}
    titre ="""Le Corbeau et le Renard 
    ```

45. ``` {.LignePreCode}
    par Jean de la Fontaine, auteur français 
    ```

46. ``` {.LignePreCode}
    \n""" 
    ```

47. ``` {.LignePreCode}
    auteur =""" 
    ```

48. ``` {.LignePreCode}
    Jean de la Fontaine 
    ```

49. ``` {.LignePreCode}
    écrivain français (1621-1695) 
    ```

50. ``` {.LignePreCode}
    célèbre pour ses Contes en vers, 
    ```

51. ``` {.LignePreCode}
    et surtout ses Fables, publiées 
    ```

52. ``` {.LignePreCode}
    de 1668 à 1694.""" 
    ```

53. ``` {.LignePreCode}
      
    ```

54. ``` {.LignePreCode}
    # Remplissage du widget Text (2 techniques) : 
    ```

55. ``` {.LignePreCode}
    st.importFichier("CorbRenard.txt", encodage ="Latin1") 
    ```

56. ``` {.LignePreCode}
    st.text.insert("0.0", titre, "titre") 
    ```

57. ``` {.LignePreCode}
    st.text.insert(END, auteur, "cible") 
    ```

58. ``` {.LignePreCode}
    # Insertion d'une image : 
    ```

59. ``` {.LignePreCode}
    photo =PhotoImage(file= "penguin.gif") 
    ```

60. ``` {.LignePreCode}
    st.text.image_create("6.14", image =photo) 
    ```

61. ``` {.LignePreCode}
    # Ajout d'une balise supplémentaire : 
    ```

62. ``` {.LignePreCode}
    st.text.tag_add("lien", "2.4", "2.23") 
    ```

63. ``` {.LignePreCode}
      
    ```

64. ``` {.LignePreCode}
    fen.mainloop() 
    ```



#### 16-D-2-B - Commentaires {#article.xml#Ld0e55203 .TitreSection3}

-   Lignes 3 à 6 : le widget composite que nous définissons dans cette
    classe sera une fois de plus obtenu par dérivation de la classe
    **Frame()**. Son constructeur prévoit quelques paramètres
    d'instanciation à titre d'exemple (police utilisée, largeur et
    hauteur), avec des valeurs par défaut. Ces paramètres seront
    simplement transmis au widget *Text* « interne » (aux lignes 7 et
    8). Vous pourriez bien évidemment en ajouter beaucoup d'autres, pour
    déterminer par exemple l'apparence du curseur, la couleur du fond ou
    des caractères, la manière dont les lignes trop longues doivent être
    coupées ou non, etc. Vous pourriez aussi de la même façon
    transmettre divers paramètres à la barre de défilement.
-   ![](images/image52.png)
-   Lignes 11 et 12 : l'option **expand** de la méthode **pack()**
    n'accepte que les valeurs **YES** ou **NO**. Elle détermine si le
    widget doit s'étirer ou non lorsque la fenêtre est éventuellement
    redimensionnée. L'option complémentaire **fill** peut prendre les 3
    valeurs : **X**, **Y** ou **BOTH**. Elle indique si l'étirement peut
    s'effectuer horizontalement (*axe X*), verticalement (*axe Y*), ou
    dans les deux directions (*BOTH*). Lorsque vous développez une
    application, Il est important de prévoir ces redimensionnements
    éventuels, surtout si l'application est destinée à être utilisée
    dans des environnements variés (Windows, Linux, MacOS, …).
-   Lignes 22 à 25 : Cette fonction est un gestionnaire d'événement, qui
    est appelé lorsque l'utilisateur clique avec le bouton droit sur le
    nom de l'auteur (l'événement en question est associé à la balise
    correspondante, à la ligne 42).\
     À la ligne 24, on utilise la méthode **tag\_nextrange()** du widget
    *Text* pour trouver les index de la portion de texte associée à la
    balise « cible ». La recherche de ces index est limitée au domaine
    défini par les 2^e^ et 3^e^ arguments (dans notre exemple, on
    recherche du début à la fin du texte entier). La méthode
    **tag\_nextrange()** renvoie un tuple de deux index (ceux des
    premier et dernier caractères de la portion de texte associée à la
    balise « cible »). À la ligne 25, nous nous servons d'un seul de ces
    index (le premier) pour activer la méthode **see()**. Celle-ci
    provoque un défilement automatique du texte (*scrolling*), de telle
    manière que le caractère correspondant à l'index transmis devienne
    visible dans le widget (avec en général un certain nombre des
    caractères qui suivent).
-   Lignes 27 à 33 : Construction classique d'une fenêtre contenant deux
    widgets.
-   Lignes 35 à 42 : Ces lignes définissent les trois balises **titre**,
    **lien** et **cible** ainsi que le formatage du texte qui leur sera
    associé. La ligne 42 précise en outre que le texte associé à la
    balise **lien** sera « cliquable » (le bouton n°3 de la souris est
    le bouton droit), avec indication du gestionnaire d'événement
    correspondant.
-   Ligne 55 : Vous pouvez incorporer n'importe quelle fonctionnalité
    dans la définition d'une classe, comme nous l'avons fait ici en
    prévoyant une méthode d'importation de fichier texte dans le widget
    lui-même, avec le paramètre *ad hoc* pour un décodage éventuel. Avec
    cette méthode, le texte importé s'insère à la fin du texte déjà
    présent dans le widget, mais vous pourriez aisément l'améliorer en
    lui ajoutant un paramètre pour préciser l'endroit exact où doit se
    faire l'insertion.
-   Lignes 56-57 : Ces instructions insèrent des fragments de texte
    (respectivement au début et à la fin du texte préexistant), en
    associant une balise à chacun d'eux.
-   Ligne 62 : L'association des balises au texte est dynamique. À tout
    moment, vous pouvez activer une nouvelle association (comme nous le
    faisons ici en rattachant la balise « lien » à une portion de texte
    préexistante). Note : pour « détacher » une balise, utilisez la
    méthode **tag\_delete()**.

### 16-D-3 - Le widget Canvas assorti d'un ascenseur {#article.xml#Ld0e55305 .TitreSection2}

Nous avons déjà beaucoup exploité le widget Canvas, dont les
possibilités sont extrêmement étendues. Nous avons déjà vu aussi comment
nous pouvons encore enrichir cette classe par dérivation. C'est ce que
nous allons faire une fois de plus dans l'exemple ci-après, avec la
définition d'une nouvelle classe **ScrolledCanvas**, dans laquelle nous
associerons au canevas standard deux barres de défilement (une verticale
et une horizontale).

Afin de rendre l'exercice plus attrayant, nous nous servirons de notre
nouvelle classe de widget pour réaliser un petit jeu d'adresse, dans
lequel l'utilisateur devra réussir à cliquer sur un bouton qui s'esquive
sans cesse. (Note : Si vous éprouvez vraiment des difficultés pour
l'attraper, commencez d'abord par dilater la fenêtre !).

Le widget **Canvas** est très polyvalent : il vous permet de combiner à
volonté des dessins, des images bitmap, des fragments de texte, ***et
même d'autres widgets***, dans un espace parfaitement extensible. Si
vous souhaitez développer l'un ou l'autre jeu graphique, c'est
évidemment le widget qu'il vous faut apprendre à maîtriser en priorité.

Comprenez bien cependant que les indications que nous vous fournissons à
ce sujet dans les présentes notes sont forcément très incomplètes. Leur
objectif est seulement de vous aider à comprendre quelques concepts de
base, afin que vous puissiez ensuite consulter les ouvrages de référence
spécialisés dans de bonnes conditions.

Notre petite application se présente comme une nouvelle classe
**FenPrinc()**, obtenue par dérivation à partir de la classe de base
**Tk()**. Elle contient deux widgets : un simple libellé, et notre
nouveau widget composite **ScrolledCanvas**. Celui-ci est une « vue »
sur un espace de dessin beaucoup plus grand, dans lequel nous pourrons «
voyager » grâce aux barres de défilement.

Afin que l'espace disponible soit bien repérable, nous commençons par y
planter un décor simple, constitué de 80 ellipses de couleur dont
l'emplacement et les dimensions sont tirés au hasard. Nous y ajoutons
également un petit clin d'œil sous la forme d'une image bitmap, destinée
avant tout à vous rappeler comment vous pouvez gérer ce type de
ressource.

Pour terminer, nous y installons aussi un *véritable widget fonctionnel*
: en l'occurrence un simple bouton, mais la technique mise en œuvre
pourrait s'appliquer à n'importe quel autre type de widget, y compris un
gros widget composite comme ceux que nous avons développés précédemment.
Cette grande souplesse dans le développement d'applications complexes
est l'un des principaux bénéfices apportés par le mode de programmation
« orientée objet ».

Le bouton s'anime dès qu'on l'a enfoncé une première fois, et
l'animation s'arrête si on arrive à nouveau à cliquer dessus. Dans votre
analyse du script ci-après, soyez attentifs aux méthodes utilisées pour
modifier les propriétés d'un objet existant.



1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
    from random import randrange 
    ```

3.  ``` {.LignePreCode}
      
    ```

4.  ``` {.LignePreCode}
    class ScrolledCanvas(Frame): 
    ```

5.  ``` {.LignePreCode}
      """Canevas extensible avec barres de défilement""" 
    ```

6.  ``` {.LignePreCode}
      def __init__(self, boss, width =100, height =100, bg="white", bd=2, 
    ```

7.  ``` {.LignePreCode}
    	scrollregion =(0, 0, 300, 300), relief=SUNKEN): 
    ```

8.  ``` {.LignePreCode}
          Frame.__init__(self, boss, bd =bd, relief=relief) 
    ```

9.  ``` {.LignePreCode}
          self.can =Canvas(self, width=width-20, height=height-20, bg=bg, 
    ```

10. ``` {.LignePreCode}
    	    scrollregion =scrollregion, bd =1) 
    ```

11. ``` {.LignePreCode}
          self.can.grid(row =0, column =0) 
    ```

12. ``` {.LignePreCode}
          bdv =Scrollbar(self, orient =VERTICAL, command =self.can.yview, bd =1) 
    ```

13. ``` {.LignePreCode}
          bdh =Scrollbar(self, orient =HORIZONTAL, command =self.can.xview, bd =1) 
    ```

14. ``` {.LignePreCode}
          self.can.configure(xscrollcommand =bdh.set, yscrollcommand =bdv.set) 
    ```

15. ``` {.LignePreCode}
          bdv.grid(row =0, column =1, sticky = NS)	     # sticky => 
    ```

16. ``` {.LignePreCode}
          bdh.grid(row =1, column =0, sticky = EW)	     # étirer la barre 
    ```

17. ``` {.LignePreCode}
          # Lier l'événement  à un gestionnaire approprié : 
    ```

18. ``` {.LignePreCode}
          self.bind("<Configure>", self.redim) 
    ```

19. ``` {.LignePreCode}
          self.started =False 
    ```

20. ``` {.LignePreCode}
      
    ```

21. ``` {.LignePreCode}
      def redim(self, event): 
    ```

22. ``` {.LignePreCode}
          "opérations à effectuer à chaque redimensionnement du widget" 
    ```

23. ``` {.LignePreCode}
          if not self.started: 
    ```

24. ``` {.LignePreCode}
          self.started =True       # Ne pas redimensionner dès la création 
    ```

25. ``` {.LignePreCode}
          return	       # du widget (sinon => bouclage) 
    ```

26. ``` {.LignePreCode}
          # À partir des nouvelles dimensions du cadre, redimensionner le canevas 
    ```

27. ``` {.LignePreCode}
          # (la diff. de 20 pixels sert à compenser l'épaisseur des scrollbars) : 
    ```

28. ``` {.LignePreCode}
          larg, haut = self.winfo_width()-20, self.winfo_height()-20 
    ```

29. ``` {.LignePreCode}
          self.can.config(width =larg, height =haut) 
    ```

30. ``` {.LignePreCode}
      
    ```

31. ``` {.LignePreCode}
    class FenPrinc(Tk): 
    ```

32. ``` {.LignePreCode}
      def __init__(self): 
    ```

33. ``` {.LignePreCode}
          Tk.__init__(self) 
    ```

34. ``` {.LignePreCode}
          self.libelle =Label(text ="Scroll game", font="Helvetica 14 bold") 
    ```

35. ``` {.LignePreCode}
          self.libelle.pack(pady =3) 
    ```

36. ``` {.LignePreCode}
          terrainJeu =ScrolledCanvas(self, width =500, height =300, relief=SOLID, 
    ```

37. ``` {.LignePreCode}
    		 scrollregion =(-600,-600,600,600), bd =3) 
    ```

38. ``` {.LignePreCode}
          terrainJeu.pack(expand =YES, fill =BOTH, padx =6, pady =6) 
    ```

39. ``` {.LignePreCode}
          self.can =terrainJeu.can 
    ```

40. ``` {.LignePreCode}
          # Décor : tracé d'une série d'ellipses aléatoires : 
    ```

41. ``` {.LignePreCode}
          coul =('sienna','maroon','brown','pink','tan','wheat','gold','orange', 
    ```

42. ``` {.LignePreCode}
    	 'plum','red','khaki','indian red','thistle','firebrick', 
    ```

43. ``` {.LignePreCode}
    	 'salmon','coral','yellow','cyan','blue','green') 
    ```

44. ``` {.LignePreCode}
          for r in range(80): 
    ```

45. ``` {.LignePreCode}
          x1, y1 = randrange(-600,450), randrange(-600,450) 
    ```

46. ``` {.LignePreCode}
          x2, y2 = x1 +randrange(40,300), y1 +randrange(40,300) 
    ```

47. ``` {.LignePreCode}
          couleur = coul[randrange(20)] 
    ```

48. ``` {.LignePreCode}
          self.can.create_oval(x1, y1, x2, y2, fill=couleur, outline='black') 
    ```

49. ``` {.LignePreCode}
          # Ajout d'une petite image GIF : 
    ```

50. ``` {.LignePreCode}
          self.img = PhotoImage(file ='linux2.gif') 
    ```

51. ``` {.LignePreCode}
          self.can.create_image(50, 20, image =self.img) 
    ```

52. ``` {.LignePreCode}
          # Bouton à attraper : 
    ```

53. ``` {.LignePreCode}
          self.x, self.y = 50, 100 
    ```

54. ``` {.LignePreCode}
          self.bou = Button(self.can, text ="Start", command =self.start) 
    ```

55. ``` {.LignePreCode}
          self.fb = self.can.create_window(self.x, self.y, window =self.bou) 
    ```

56. ``` {.LignePreCode}
      
    ```

57. ``` {.LignePreCode}
      def anim(self): 
    ```

58. ``` {.LignePreCode}
          if self.run ==0: 
    ```

59. ``` {.LignePreCode}
          return 
    ```

60. ``` {.LignePreCode}
          self.x += randrange(-60, 61) 
    ```

61. ``` {.LignePreCode}
          self.y += randrange(-60, 61) 
    ```

62. ``` {.LignePreCode}
          self.can.coords(self.fb, self.x, self.y) 
    ```

63. ``` {.LignePreCode}
          self.libelle.config(text = 'Cherchez en %s %s' % (self.x, self.y)) 
    ```

64. ``` {.LignePreCode}
          self.after(250, self.anim) 
    ```

65. ``` {.LignePreCode}
      
    ```

66. ``` {.LignePreCode}
      def stop(self): 
    ```

67. ``` {.LignePreCode}
          self.run =0 
    ```

68. ``` {.LignePreCode}
          self.bou.configure(text ="Start", command =self.start) 
    ```

69. ``` {.LignePreCode}
      
    ```

70. ``` {.LignePreCode}
      def start(self): 
    ```

71. ``` {.LignePreCode}
          self.bou.configure(text ="Attrapez-moi !", command =self.stop) 
    ```

72. ``` {.LignePreCode}
          self.run =1 
    ```

73. ``` {.LignePreCode}
          self.anim() 
    ```

74. ``` {.LignePreCode}
      
    ```

75. ``` {.LignePreCode}
    if __name__ =="__main__":	   # --- Programme de test --- 
    ```

76. ``` {.LignePreCode}
      FenPrinc().mainloop() 
    ```



#### 16-D-3-A - Commentaires {#article.xml#Ld0e56874 .TitreSection3}

-   Lignes 6 à 10 : comme beaucoup d'autres, notre nouveau widget est
    dérivé de **Frame()**. Son constructeur accepte un certain nombre de
    paramètres. Remarquez bien que ces paramètres sont transmis pour
    partie au cadre (paramètres *bd, relief*), et pour partie au canevas
    (paramètres *width, height, bg, scrollregion*). Vous pouvez bien
    évidemment faire d'autres choix selon vos besoins. L'option `scrollregion` du widget Canvas sert à
    définir l'espace de dessin dans lequel la « vue » du canevas pourra
    se déplacer.
-   Lignes 11 à 16 : Nous utiliserons cette fois la méthode **grid()**
    pour mettre en place le canevas et ses barres de défilement (cette
    méthode vous a été présentée page ). La méthode **pack()** ne
    conviendrait guère pour mettre en place correctement les deux barres
    de défilement, car elle imposerait l'utilisation de plusieurs cadres
    (*frames*) imbriqués (essayez, à titre d'exercice !). Les
    interactions à mettre en place entre les barres de défilement et le
    widget qu'elles contrôlent (lignes 12, 13, 14) ont déjà été décrites
    en détail pour les deux widgets composites précédents. L'option
    `orient` des barres de
    défilement n'avait pas été utilisée jusqu'ici, parce que sa valeur
    par défaut (`VERTICAL`)
    convenait aux cas traités.\
     Aux lignes 15 et 16, les options `sticky =NS` et `sticky =EW` provoquent l'étirement
    des barres de défilement jusqu'à occuper toute la hauteur (`NS` = direction *Nord-Sud*) ou toute
    la largeur (`EW` = direction
    *Est-Ouest*)de la cellule dans la grille. Il n'y aura cependant pas
    de redimensionnement automatique comme c'est le cas avec la méthode
    **pack()** (les options `expand` et `fill` ne sont d'ailleurs pas
    disponibles : voir ci-après).
-   Ligne 18 : Du fait que la méthode **grid()** n'inclut pas le
    redimensionnement automatique, nous devons guetter l'événement qui
    est généré par le système lorsque l'utilisateur redimensionne le
    widget, et l'associer à une méthode appropriée pour effectuer
    nous-mêmes le redimensionnement des composants du widget.
-   Lignes 19 à 29 : La méthode de redimensionnement consistera
    simplement à redimensionner le canevas (les barres de défilement
    s'adapteront toutes seules, du fait de l'option *sticky* qui leur
    est appliquée). Notez au passage que les dimensions actualisées d'un
    widget peuvent être trouvées dans ses attributs `winfo_width()` et `winfo_height()`.\
     La variable d'instance `self.started` est un simple
    interrupteur, qui permet d'éviter que le redimensionnement soit déjà
    appelé prématurément, lors de l'instanciation du widget (ce qui
    produit un bouclage curieux : essayez sans !).
-   Lignes 31 à 55 : Cette classe définit notre petite application de
    jeu. Son constructeur instancie notre nouveau widget dans la
    variable `terrainJeu` (ligne
    36). Remarquez que le type de bordure et son épaisseur
    s'appliqueront au cadre du widget composite, alors que les autres
    arguments choisis s'appliqueront au canevas. Avec l'option
    *scrollregion*, nous définissons un espace de jeu nettement plus
    étendu que la surface du canevas lui-même, ce qui obligera le joueur
    à déplacer (ou redimensionner) celui-ci.
-   Lignes 54-55 : C'est la méthode **create\_window()** du widget
    **Canvas** qui permet d'y insérer n'importe quel autre widget (y
    compris un widget composite). Le widget à insérer doit cependant
    avoir été défini lui-même au préalable comme un esclave du canevas
    ou de sa fenêtre maîtresse. La méthode **create\_window()** attend
    trois arguments : les coordonnées **X** et **Y** du point où l'on
    souhaite insérer le widget, et la référence de ce widget.
-   Lignes 57 à 64 : Cette méthode est utilisée pour l'animation du
    bouton. Après avoir repositionné le bouton au hasard à une certaine
    distance de sa position précédente, elle se ré-appelle elle-même
    après une pause de 250 millisecondes. Ce bouclage s'effectue sans
    cesse, aussi longtemps que la variable **self.run** contient une
    valeur non-nulle.
-   Lignes 66 à 73 : Ces deux gestionnaires d'événement sont associés au
    bouton en alternance. Ils servent évidemment à démarrer et à arrêter
    l'animation.


[^note_81]: Nous aurions pu aussi faire exactement l'inverse, c'est-à-dire créer d'abord l'ascenseur sans indication de commande, puis créer la boîte de liste en indiquant la commande d'accès à l'ascenseur dans la ligne d'instanciation, et enfin reconfigurer l'ascenseur en lui indiquant la commande de défilement de la liste :  `scrol =Scrollbar(cadreLB)` **self.bListe =Listbox(cadreLB, height =listSize, width =width-1,** `yscrollcommand =scrol.set)` **scrol.config(command =self.bListe.yview) **
