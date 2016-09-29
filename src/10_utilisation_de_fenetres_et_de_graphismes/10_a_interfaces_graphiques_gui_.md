## 10-A - Interfaces graphiques (GUI)

Si vous ne le saviez pas encore, apprenez dès à présent que le domaine
des interfaces graphiques (ou *GUI : Graphical User Interfaces*) est
extrêmement complexe. Chaque système d'exploitation peut en effet
proposer plusieurs « bibliothèques » de fonctions graphiques de base,
auxquelles viennent fréquemment s'ajouter de nombreux compléments, plus
ou moins spécifiques de langages de programmation particuliers. Tous ces
composants sont généralement présentés comme des *classes d'objets*,
dont il vous faudra étudier les *attributs* et les *méthodes*.

Avec Python, la bibliothèque graphique la plus utilisée jusqu'à présent
est la bibliothèque *tkinter*, qui est une adaptation de la bibliothèque
*Tk* développée à l'origine pour le langage *Tcl*. Plusieurs autres
bibliothèques graphiques fort intéressantes ont été proposées pour
Python : *wxPython*, *pyQT*, *pyGTK*, etc. Il existe également des
possibilités d'utiliser les bibliothèques de *widgetsJava* et les *MFC*
de *Windows*. Dans le cadre de ces notes, nous nous limiterons cependant
à *tkinter*, dont il existe fort heureusement des versions similaires
(et gratuites) pour les plates-formes *Linux*, *Windows* et *Mac OS*.

