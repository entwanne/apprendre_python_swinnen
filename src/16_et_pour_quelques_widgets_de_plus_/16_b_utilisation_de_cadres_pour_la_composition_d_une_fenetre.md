## 16-B - Utilisation de cadres pour la composition d'une fenêtre



![](images/image48.png)



Vous avez déjà abondamment utilisé la classe de widgets **Frame()** («
cadre », en français), notamment pour créer de nouveaux widgets
complexes par dérivation.

Le petit script ci-dessous vous montre l'utilité de cette même classe
pour regrouper des ensembles de widgets et les disposer d'une manière
déterminée dans une fenêtre. Il vous démontre également l'utilisation de
certaines options décoratives (bordures, relief, etc.).

Pour composer la fenêtre ci-contre, nous avons utilisé deux cadres
**f1** et **f2**, de manière à réaliser deux groupes de widgets bien
distincts, l'un à gauche et l'autre à droite. Nous avons coloré ces deux
cadres pour bien les mettre en évidence, mais ce n'est évidemment pas
indispensable.

Le cadre **f1** contient lui-même 6 autres cadres, qui contiennent
chacun un widget de la classe **Label()**. Le cadre **f2** contient un
widget **Canvas()** et un widget **Button()**. Les couleurs et
garnitures sont de simples options.



1.  ``` {.LignePreCode}
    from tkinter import * 
    ```

2.  ``` {.LignePreCode}
      
    ```

3.  ``` {.LignePreCode}
    fen = Tk() 
    ```

4.  ``` {.LignePreCode}
    fen.title("Fenêtre composée à l'aide de frames") 
    ```

5.  ``` {.LignePreCode}
    fen.geometry("300x300") 
    ```

6.  ``` {.LignePreCode}
      
    ```

7.  ``` {.LignePreCode}
    f1 = Frame(fen, bg = '#80c0c0') 
    ```

8.  ``` {.LignePreCode}
    f1.pack(side =LEFT, padx =5)   
    ```

9.  ``` {.LignePreCode}
      
    ```

10. ``` {.LignePreCode}
    fint = [0]*6 
    ```

11. ``` {.LignePreCode}
    for (n, col, rel, txt) in [(0, 'grey50', RAISED, 'Relief sortant'), 
    ```

12. ``` {.LignePreCode}
    	     (1, 'grey60', SUNKEN, 'Relief rentrant'), 
    ```

13. ``` {.LignePreCode}
    	     (2, 'grey70', FLAT, 'Pas de relief'), 
    ```

14. ``` {.LignePreCode}
    	     (3, 'grey80', RIDGE, 'Crête'), 
    ```

15. ``` {.LignePreCode}
    	     (4, 'grey90', GROOVE, 'Sillon'), 
    ```

16. ``` {.LignePreCode}
    	     (5, 'grey100', SOLID, 'Bordure')]: 
    ```

17. ``` {.LignePreCode}
      fint[n] = Frame(f1, bd =2, relief =rel) 
    ```

18. ``` {.LignePreCode}
      e = Label(fint[n], text =txt, width =15, bg =col) 
    ```

19. ``` {.LignePreCode}
      e.pack(side =LEFT, padx =5, pady =5) 
    ```

20. ``` {.LignePreCode}
      fint[n].pack(side =TOP, padx =10, pady =5) 
    ```

21. ``` {.LignePreCode}
      
    ```

22. ``` {.LignePreCode}
    f2 = Frame(fen, bg ='#d0d0b0', bd =2, relief =GROOVE) 
    ```

23. ``` {.LignePreCode}
    f2.pack(side =RIGHT, padx =5) 
    ```

24. ``` {.LignePreCode}
      
    ```

25. ``` {.LignePreCode}
    can = Canvas(f2, width =80, height =80, bg ='white', bd =2, relief =SOLID) 
    ```

26. ``` {.LignePreCode}
    can.pack(padx =15, pady =15) 
    ```

27. ``` {.LignePreCode}
    bou =Button(f2, text='Bouton') 
    ```

28. ``` {.LignePreCode}
    bou.pack() 
    ```

29. ``` {.LignePreCode}
      
    ```

30. ``` {.LignePreCode}
    fen.mainloop() 
    ```



### 16-B-1 - Commentaires {#article.xml#Ld0e50764 .TitreSection2}

-   Lignes 3 à 5 : Afin de simplifier au maximum la démonstration, nous
    ne programmons pas cet exemple comme une nouvelle classe. Remarquez
    à la ligne 5 l'utilité de la méthode **geometry()** pour fixer les
    dimensions de la fenêtre principale.
-   Ligne 7 : Instanciation du cadre de gauche. La couleur de fond (une
    variété de bleu cyan) est déterminée par l'argument **bg**
    (*background*). Cette chaîne de caractères contient en notation
    hexadécimale la description des trois composantes rouge, verte et
    bleue de la teinte que l'on souhaite obtenir : après le caractère
    **\#** signalant que ce qui suit est une valeur numérique
    hexadécimale, on trouve trois groupes de deux symboles
    alphanumériques. Chacun de ces groupes représente un nombre compris
    entre 1 et 255. Ainsi, 80 correspond à 128, et c0 correspond à 192
    en notation décimale. Dans notre exemple, les composantes rouge,
    verte et bleue de la teinte à représenter valent donc respectivement
    128, 192 et 192.\
     En application de cette technique descriptive, le noir serait
    obtenu avec `#000000`, le
    blanc avec `#ffffff`, le
    rouge pur avec `#ff0000`, un
    bleu sombre avec `#000050`,
    etc.
-   Ligne 8 : Puisque nous lui appliquons la méthode **pack()**, le
    cadre sera automatiquement dimensionné par son contenu. L'option
    `side =LEFT` le positionnera à
    gauche dans sa fenêtre maîtresse. L'option `padx =5` ménagera un espace de 5
    pixels à sa gauche et à sa droite (nous pouvons traduire « padx »
    par « espacement horizontal »).
-   Ligne 10 : Dans le cadre **f1** que nous venons de préparer, nous
    avons l'intention de regrouper 6 autres cadres similaires contenant
    chacun une étiquette. Le code correspondant sera plus simple et plus
    efficace si nous instancions ces widgets dans une liste plutôt que
    dans des variables indépendantes. Nous préparons donc cette liste
    avec 6 éléments que nous remplacerons plus loin.
-   Lignes 11 à 16 : Pour construire nos 6 cadres similaires, nous
    allons parcourir une liste de 6 tuples contenant les
    caractéristiques particulières de chaque cadre. Chacun de ces tuples
    est constitué de 4 éléments : un indice, une constante tkinter
    définissant un type de relief, et deux chaînes de caractères
    décrivant respectivement la couleur et le texte de l'étiquette.\
     La boucle **for** effectue 6 itérations pour parcourir les 6
    éléments de la liste. À chaque itération, le contenu d'un des tuples
    est affecté aux variables **n**, **col**, **rel** et **txt** (et
    ensuite les instructions des lignes 17 à 20 sont exécutées).

> Le parcours d*'*une liste de tuples à l*'*aide d*'*une boucle for
> constitue une construction particulièrement compacte, qui permet de
> réaliser de nombreuses affectations avec un très petit nombre
> d*'*instructions.

-   Ligne 17 : Les 6 cadres sont instanciés comme des éléments de la
    liste **fint**. Chacun d'entre eux est agrémenté d'une bordure
    décorative de 2 pixels de large, avec un certain effet de relief.
-   Lignes 18-20 : Les étiquettes ont toutes la même taille, mais leurs
    textes et leurs couleurs de fond diffèrent. Du fait de l'utilisation
    de la méthode **pack()**, c'est la dimension des étiquettes qui
    détermine la taille des petits cadres. Ceux-ci à leur tour
    déterminent la taille du cadre qui les regroupe (le cadre f1). Les
    options **padx** et **pady** permettent de réserver un petit espace
    autour de chaque étiquette, et un autre autour de chaque petit
    cadre. L'option `side =TOP`
    positionne les 6 petits cadres les uns en dessous des autres dans le
    cadre conteneur f1.
-   Lignes 22-23 : Préparation du cadre **f2** (cadre de droite). Sa
    couleur sera une variété de jaune, et nous l'entourerons d'une
    bordure décorative ayant l'aspect d'un sillon.
-   Lignes 25 à 28 : Le cadre **f2** contiendra un canevas et un bouton.
    Notez encore une fois l'utilisation des options **padx** et **pady**
    pour ménager des espaces autour des widgets (considérez par exemple
    le cas du bouton, pour lequel cette option n'a pas été utilisée : de
    ce fait, il entre en contact avec la bordure du cadre qui
    l'entoure). Comme nous l'avons fait pour les cadres, nous avons
    placé une bordure autour du canevas. Sachez que d'autres widgets
    acceptent également ce genre de décoration : boutons, champs
    d'entrée, etc.

