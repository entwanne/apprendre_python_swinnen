## 13-H - Modification des objets

Nous pouvons changer les propriétés d'un objet en assignant de nouvelles
valeurs à ses attributs. Par exemple, nous pouvons modifier la taille
d'un rectangle (sans modifier sa position), en réassignant ses attributs
hauteur et largeur :



```python
>>> boite.hauteur = boite.hauteur + 20
>>> boite.largeur = boite.largeur ? 5
```



Nous pouvons faire cela sous Python, parce que dans ce langage les
propriétés des objets sont toujours *publiques* (du moins jusqu'à la
version actuelle 3.1). D'autres langages établissent une distinction
nette entre attributs publics (accessibles de l'extérieur de l'objet) et
attributs privés (qui sont accessibles seulement aux algorithmes inclus
dans l'objet lui-même).

Cependant, comme nous l'avons déjà signalé plus haut (à propos de la
définition des attributs par assignation simple, depuis l'extérieur de
l'objet), modifier de cette façon les attributs d'une instance ***n'est
pas une pratique recommandable***, parce qu'elle contredit l'un des
objectifs fondamentaux de la programmation orientée objet, qui vise à
établir une séparation stricte entre la fonctionnalité d'un objet (telle
qu'elle a été déclarée au monde extérieur) et la manière dont cette
fonctionnalité est réellement implémentée dans l'objet (et que le monde
extérieur n'a pas à connaître).

Concrètement, cela signifie que nous devons maintenant étudier comment
faire fonctionner les objets à l'aide d'outils vraiment appropriés, que
nous appellerons des *méthodes*.

Ensuite, lorsque nous aurons bien compris le maniement de celles-ci,
*nous nous fixerons pour règle de ne plus modifier les attributs d'un
objet par assignation directe depuis le monde extérieur*, comme nous
l'avons fait jusqu'à présent. Nous veillerons au contraire à toujours
utiliser pour cela des méthodes mises en place spécifiquement dans ce
but, comme nous allons l'expliquer dans le chapitre suivant. L'ensemble
de ces méthodes constituera ce que nous appellerons désormais
l'*interface* de l'objet.

