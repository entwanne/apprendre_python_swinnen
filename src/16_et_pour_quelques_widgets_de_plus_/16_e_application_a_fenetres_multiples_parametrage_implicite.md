## 16-E - Application à fenêtres multiples - paramétrage implicite

La classe **Toplevel()** de *tkinter* permet de créer des fenêtres «
satellites » de votre application principale. Ces fenêtres sont
autonomes, mais elles se refermeront automatiquement lorsque vous
fermerez la fenêtre principale. Cette restriction mise à part, elles se
traitent de la manière habituelle : vous pouvez y placer n'importe
quelle combinaison de widgets, à volonté.

La petite application ci-après vous montre quelques-unes de leurs
possibilités. Elle est constituée d'une fenêtre principale très
ordinaire, contenant simplement trois boutons. Ces boutons sont créés à
partir d'une classe dérivée de la classe **Button()** de base, ceci afin
de vous montrer encore une fois combien il est facile d'adapter les
classes d'objets existantes à vos besoins. Vous pourrez noter au passage
quelques options « décoratives » intéressantes.

Le bouton « Top1 » fait apparaître une première fenêtre satellite
contenant un canevas avec une image. Nous avons doté cette fenêtre de
propriétés particulières : elle ne possède ni bandeau-titre, ni bordure,
et il est impossible de la redimensionner à l'aide de la souris. De
plus, cette fenêtre est ***modale*** : on qualifie ainsi une fenêtre qui
reste toujours au premier plan, devant toutes les autres fenêtres
d'application éventuellement présentes à l'écran.



![](images/image53.png)





1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    class FunnyButton(Button): 
    ```

4.  ``` {.LignePreCode}
      "Bouton de fantaisie : vert virant au rouge quand on l'actionne" 
    ```

5.  ``` {.LignePreCode}
      def __init__(self, boss, **Arguments): 
    ```

6.  ``` {.LignePreCode}
          Button.__init__(self, boss,  bg ="dark green", fg ="white", bd =5, 
    ```

7.  ``` {.LignePreCode}
    	      activebackground ="red", activeforeground ="yellow", 
    ```

8.  ``` {.LignePreCode}
    	      font =('Helvetica', 12, 'bold'), **Arguments) 
    ```

9.  ``` {.LignePreCode}
      
    ```

10. ``` {.LignePreCode}
    class SpinBox(Frame): 
    ```

11. ``` {.LignePreCode}
      "widget composite comportant un Label et 2 boutons 'up' & 'down'" 
    ```

12. ``` {.LignePreCode}
      def __init__(self, boss, largC=5, largB =2, vList=[0], liInd=0, orient =Y): 
    ```

13. ``` {.LignePreCode}
          Frame.__init__(self, boss) 
    ```

14. ``` {.LignePreCode}
          self.vList =vList      # liste des valeurs à présenter 
    ```

15. ``` {.LignePreCode}
          self.liInd =liInd      # index de la valeur à montrer par défaut 
    ```

16. ``` {.LignePreCode}
          if orient ==Y: 
    ```

17. ``` {.LignePreCode}
          s, augm, dimi = TOP, "^", "v"	 # Orientation 'verticale' 
    ```

18. ``` {.LignePreCode}
          else: 
    ```

19. ``` {.LignePreCode}
          s, augm, dimi = RIGHT, ">", "<"	 # Orientation 'horizontale' 
    ```

20. ``` {.LignePreCode}
          Button(self, text =augm, width =largB, command =self.up).pack(side =s) 
    ```

21. ``` {.LignePreCode}
          self.champ = Label(self, bg ='white', width =largC, 
    ```

22. ``` {.LignePreCode}
    	     text =str(vList[liInd]), relief =SUNKEN) 
    ```

23. ``` {.LignePreCode}
          self.champ.pack(pady =3, side =s) 
    ```

24. ``` {.LignePreCode}
          Button(self, text=dimi, width=largB, command =self.down).pack(side =s) 
    ```

25. ``` {.LignePreCode}
      
    ```

26. ``` {.LignePreCode}
      def up(self): 
    ```

27. ``` {.LignePreCode}
          if self.liInd < len(self.vList) -1: 
    ```

28. ``` {.LignePreCode}
          self.liInd += 1 
    ```

29. ``` {.LignePreCode}
          else: 
    ```

30. ``` {.LignePreCode}
          self.bell()	 # émission d'un bip 
    ```

31. ``` {.LignePreCode}
          self.champ.configure(text =str(self.vList[self.liInd])) 
    ```

32. ``` {.LignePreCode}
      
    ```

33. ``` {.LignePreCode}
      def down(self): 
    ```

34. ``` {.LignePreCode}
          if self.liInd > 0: 
    ```

35. ``` {.LignePreCode}
          self.liInd -= 1 
    ```

36. ``` {.LignePreCode}
          else: 
    ```

37. ``` {.LignePreCode}
          self.bell()	 # émission d'un bip 
    ```

38. ``` {.LignePreCode}
          self.champ.configure(text =str(self.vList[self.liInd])) 
    ```

39. ``` {.LignePreCode}
      
    ```

40. ``` {.LignePreCode}
      def get(self): 
    ```

41. ``` {.LignePreCode}
          return self.vList[self.liInd] 
    ```

42. ``` {.LignePreCode}
      
    ```

43. ``` {.LignePreCode}
    class FenDessin(Toplevel): 
    ```

44. ``` {.LignePreCode}
      "Fenêtre satellite (modale) contenant un simple canevas" 
    ```

45. ``` {.LignePreCode}
      def __init__(self, **Arguments): 
    ```

46. ``` {.LignePreCode}
          Toplevel.__init__(self, **Arguments) 
    ```

47. ``` {.LignePreCode}
          self.geometry("250x200+100+240") 
    ```

48. ``` {.LignePreCode}
          self.overrideredirect(1)	     # => fenêtre sans bordure ni bandeau 
    ```

49. ``` {.LignePreCode}
          self.transient(self.master)      # => fenêtre 'modale' 
    ```

50. ``` {.LignePreCode}
          self.can =Canvas(self, bg="ivory", width =200, height =150) 
    ```

51. ``` {.LignePreCode}
          self.img = PhotoImage(file ="papillon2.gif") 
    ```

52. ``` {.LignePreCode}
          self.can.create_image(90, 80, image =self.img) 
    ```

53. ``` {.LignePreCode}
          self.can.pack(padx =20, pady =20) 
    ```

54. ``` {.LignePreCode}
      
    ```

55. ``` {.LignePreCode}
    class FenControle(Toplevel): 
    ```

56. ``` {.LignePreCode}
      "Fenêtre satellite contenant des contrôles de redimensionnement" 
    ```

57. ``` {.LignePreCode}
      def __init__(self, boss, **Arguments): 
    ```

58. ``` {.LignePreCode}
          Toplevel.__init__(self, boss, **Arguments) 
    ```

59. ``` {.LignePreCode}
          self.geometry("250x200+400+230") 
    ```

60. ``` {.LignePreCode}
          self.resizable(width =0, height =0)    # => empêche le redimensionnement 
    ```

61. ``` {.LignePreCode}
          p =(10, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300) 
    ```

62. ``` {.LignePreCode}
          self.spX =SpinBox(self, largC=5,largB =1,vList =p,liInd=5,orient =X) 
    ```

63. ``` {.LignePreCode}
          self.spX.pack(pady =5) 
    ```

64. ``` {.LignePreCode}
          self.spY =SpinBox(self, largC=5,largB =1,vList =p,liInd=5,orient =Y) 
    ```

65. ``` {.LignePreCode}
          self.spY.pack(pady =5) 
    ```

66. ``` {.LignePreCode}
          FunnyButton(self, text ="Dimensionner le canevas", 
    ```

67. ``` {.LignePreCode}
    	  command =boss.redimF1).pack(pady =5) 
    ```

68. ``` {.LignePreCode}
      
    ```

69. ``` {.LignePreCode}
    class Demo(Frame): 
    ```

70. ``` {.LignePreCode}
      "Démo. de quelques caractéristiques du widget Toplevel" 
    ```

71. ``` {.LignePreCode}
      def __init__(self): 
    ```

72. ``` {.LignePreCode}
          Frame.__init__(self) 
    ```

73. ``` {.LignePreCode}
          self.master.geometry("400x300+200+200") 
    ```

74. ``` {.LignePreCode}
          self.master.config(bg ="cadet blue") 
    ```

75. ``` {.LignePreCode}
          FunnyButton(self, text ="Top 1", command =self.top1).pack(side =LEFT) 
    ```

76. ``` {.LignePreCode}
          FunnyButton(self, text ="Top 2", command =self.top2).pack(side =LEFT) 
    ```

77. ``` {.LignePreCode}
          FunnyButton(self, text ="Quitter", command =self.quit).pack() 
    ```

78. ``` {.LignePreCode}
          self.pack(side =BOTTOM, padx =10, pady =10) 
    ```

79. ``` {.LignePreCode}
      
    ```

80. ``` {.LignePreCode}
      def top1(self): 
    ```

81. ``` {.LignePreCode}
          self.fen1 =FenDessin(bg ="grey") 
    ```

82. ``` {.LignePreCode}
      
    ```

83. ``` {.LignePreCode}
      def top2(self): 
    ```

84. ``` {.LignePreCode}
          self.fen2 =FenControle(self, bg ="khaki") 
    ```

85. ``` {.LignePreCode}
      
    ```

86. ``` {.LignePreCode}
      def redimF1(self): 
    ```

87. ``` {.LignePreCode}
          dimX, dimY = self.fen2.spX.get(), self.fen2.spY.get() 
    ```

88. ``` {.LignePreCode}
          self.fen1.can.config(width =dimX, height =dimY) 
    ```

89. ``` {.LignePreCode}
      
    ```

90. ``` {.LignePreCode}
    if __name__ =="__main__":	   # --- Programme de test --- 
    ```

91. ``` {.LignePreCode}
      Demo().mainloop() 
    ```



### 16-E-1 - Commentaires {#article.xml#Ld0e58686 .TitreSection2}

-   Lignes 3 à 8 : Si vous souhaitez pouvoir disposer du même style de
    boutons à différents endroits de votre projet, n'hésitez pas à créer
    une classe dérivée, comme nous l'avons fait ici. Cela vous évitera
    d'avoir à reprogrammer partout les mêmes options spécifiques.\
     Notez bien les deux astérisques qui préfixent le nom du dernier
    paramètre du constructeur : **\*\*Arguments**. Elles signifient que
    la variable correspondante sera en fait un *dictionnaire*, capable
    de réceptionner automatiquement n'importe quel ensemble d'arguments
    « avec étiquettes ». Ces arguments pourront alors être transmis tels
    quels au constructeur de la classe parente (à la ligne 8). Cela nous
    évite d'avoir à reproduire dans notre liste de paramètres toutes les
    options de paramétrage du bouton de base, qui sont fort nombreuses.
    Ainsi vous pourrez instancier ces boutons de fantaisie avec
    n'importe quelle combinaison d'options, du moment que celles-ci
    soient disponibles pour les boutons de base. On appelle ce qui
    précède un ***paramétrage implicite***. Vous pouvez utiliser cette
    forme de paramétrage avec n'importe quelle fonction ou méthode.
-   Lignes 10 à 24 : Le constructeur de notre widget **SpinBox** ne
    nécessite guère de commentaires. En fonction de l'orientation
    souhaitée, la méthode **pack()** disposera les boutons et le libellé
    de haut en bas ou de gauche à droite (arguments **TOP** ou **RIGHT**
    pour son option **side**).
-   Lignes 26 à 38 : Ces deux méthodes ne font rien d'autre que de
    modifier la valeur affichée dans le libellé. Notez au passage que la
    classe **Frame()** dispose d'une méthode **bell()** pour provoquer
    l'émission d'un « bip » sonore.
-   Lignes 43 à 53 : La première fenêtre satellite est définie ici.
    Remarquez à nouveau l'utilisation du *paramétrage implicite* du
    constructeur, à l'aide de la variable **\*\*Arguments**. C'est lui
    qui nous permet d'instancier cette fenêtre (à la ligne 81) en
    spécifiant une couleur de fond. (Nous pourrions aussi demander une
    bordure, etc.). Les méthodes invoquées aux lignes 47 à 49
    définissent quelques propriétés particulières (elles qui sont
    applicables à n'importe quelle fenêtre). La méthode **geometry()**
    permet de fixer à la fois les dimensions de la fenêtre et son
    emplacement à l'écran (l'indication `+100+240` signifie que son coin
    supérieur gauche doit être décalé de 100 pixels vers la droite, et
    de 240 pixels vers le bas, par rapport au coin supérieur gauche de
    l'écran).
-   Lignes 45 et 57 : Veuillez remarquer la petite différence entre les
    listes de paramètres de ces lignes. Dans le constructeur de
    **FenDessin**, nous avons omis le paramètre **boss**, qui est bien
    présent dans le constructeur de **FenControle**. Vous savez que ce
    paramètre sert à transmettre la référence du widget « maître » à son
    « esclave ». Il est très généralement nécessaire (à la ligne 67, par
    exemple, nous nous en servons pour référencer une méthode de
    l'application principale), mais il n'est pas absolument
    indispensable : dans **FenDessin** nous n'en avons aucune utilité.
    Vous retrouverez bien évidemment la différence correspondante dans
    les instructions d'instanciation de ces fenêtres, aux lignes 82 et
    84.
-   Lignes 55 à 67 : À l'exception de la différence mentionnée
    ci-dessus, la construction du widget **FenControle** est très
    similaire à celle de **FenDessin**. Remarquez à la ligne 60 la
    méthode permettant d'empêcher le redimensionnement d'une fenêtre
    (dans le cas d' une fenêtre sans bordure ni bandeau-titre, comme
    **FenDessin**, cette méthode est inutile).
-   Lignes 73-74 (et 49) : Toutes les classes dérivées des widgets
    *tkinter* sont dotées automatiquement d'un attribut **master**, qui
    contient la référence de la classe parente. C'est ce qui nous permet
    ici d'accéder aux dimensions et à la couleur de fond de la fenêtre
    maîtresse.
-   Lignes 86 à 88 : Cette méthode récupère les valeurs numériques
    affichées dans la fenêtre de contrôle (méthode **get()** de ce
    widget), pour redimensionner le canevas de la fenêtre de dessin. Cet
    exemple simple vous montre une fois de plus comment peuvent
    s'établir les communications entre divers composants de votre
    programme.

