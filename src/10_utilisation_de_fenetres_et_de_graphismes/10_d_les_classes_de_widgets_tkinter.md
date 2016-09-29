## 10-D - Les classes de widgets tkinter

> Tout au long de cet ouvrage, nous vous
> présenterons petit à petit le mode d*'*utilisation d*'*un certain nombre de **widgets**.
> Comprenez bien cependant qu*'*il
> n'entre pas dans nos intentions de fournir ici un manuel de référence
> complet sur **tkinter**.
> Nous limiterons nos explications aux widgets qui nous semblent les
> plus intéressants d*'*un point de
> vue didactique, c*'*est-à-dire
> ceux qui pourront nous aider à mettre en évidence des concepts de
> programmation importants, tels ceux de classe et d'objet. Veuillez
> donc consulter la littérature (voir page ) si vous souhaitez davantage
> de précisions.

Il existe 15 classes de base pour les widgets tkinter :



  ------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Widget        Description
  Button        Un bouton classique, à utiliser pour provoquer l'exécution d'une commande quelconque.
  Canvas        Un espace pour disposer divers éléments graphiques. Ce widget peut être utilisé pour dessiner, créer des éditeurs graphiques, et aussi pour implémenter des widgets personnalisés.
  Checkbutton   Une case à cocher qui peut prendre deux états distincts (la case est cochée ou non). Un clic sur ce widget provoque le changement d'état.
  Entry         Un champ d'entrée, dans lequel l'utilisateur du programme pourra insérer un texte quelconque à partir du clavier.
  Frame         Une surface rectangulaire dans la fenêtre, où l'on peut disposer d'autres widgets. Cette surface peut être colorée. Elle peut aussi être décorée d'une bordure.
  Label         Un texte (ou libellé) quelconque (éventuellement une image).
  Listbox       Une liste de choix proposés à l'utilisateur, généralement présentés dans une sorte de boîte. On peut également configurer la Listbox de telle manière qu'elle se comporte comme une série de « boutons radio » ou de cases à cocher.
  Menu          Un menu. Ce peut être un menu déroulant attaché à la barre de titre, ou bien un menu « *pop up* » apparaissant n'importe où à la suite d'un clic.
  Menubutton    Un bouton-menu, à utiliser pour implémenter des menus déroulants.
  Message       Permet d'afficher un texte. Ce widget est une variante du widget Label, qui permet d'adapter automatiquement le texte affiché à une certaine taille ou à un certain rapport largeur/hauteur.
  Radiobutton   Représente (par un point noir dans un petit cercle) une des valeurs d'une variable qui peut en posséder plusieurs. Cliquer sur un bouton radio donne la valeur correspondante à la variable, et « vide » tous les autres boutons radio associés à la même variable.
  Scale         Vous permet de faire varier de manière très visuelle la valeur d'une variable, en déplaçant un curseur le long d'une règle.
  Scrollbar     Ascenseur ou barre de défilement que vous pouvez utiliser en association avec les autres widgets : Canvas, Entry, Listbox, Text.
  Text          Affichage de texte formaté. Permet aussi à l'utilisateur d'éditer le texte affiché. Des images peuvent également être insérées.
  Toplevel      Une fenêtre affichée séparément, au premier plan.
  ------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Ces classes de widgets intègrent chacune un grand nombre de méthodes. On
peut aussi leur associer (lier) des événements, comme nous venons de le
voir dans les pages précédentes. Vous allez apprendre en outre que tous
ces widgets peuvent être positionnés dans les fenêtres à l'aide de trois
méthodes différentes : la méthode **grid()**, la méthode **pack()** et
la méthode **place()**.

L'utilité de ces méthodes apparaît clairement lorsque l'on s'efforce de
réaliser des programmes portables (c'est-à-dire susceptibles de
fonctionner de manière identique sur des systèmes d'exploitation aussi
différents que *Unix*, *Mac OS* ou *Windows*), et dont les fenêtres
soient *redimensionnables.*

