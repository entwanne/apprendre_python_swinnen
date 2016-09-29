## 13-G - Objets comme valeurs de retour d'une fonction

Nous avons vu plus haut que les fonctions peuvent utiliser des objets
comme paramètres. Elles peuvent également transmettre une instance comme
valeur de retour. Par exemple, la fonction **trouveCentre()**ci-dessous
doit être appelée avec un argument de type **Rectangle()** et elle
renvoie un objet de type **Point()**, lequel contiendra les coordonnées
du centre du rectangle.



```python
>>> def trouveCentre(box):
...    p = Point()
...    p.x = box.coin.x + box.largeur/2.0
...    p.y = box.coin.y + box.hauteur/2.0
...    return p
```



Vous pouvez par exemple appeler cette fonction, en utilisant comme
argument l'objet **boite** défini plus haut :



```python
>>> centre = trouveCentre(boite)
>>> print(centre.x, centre.y)
37.0  44.5
```



