## 4-G - Affectations multiples

Sous Python, on peut assigner une valeur à plusieurs variables
simultanément. Exemple :



```python
>>> x = y = 7
>>> x
7
>>> y
7
```



On peut aussi effectuer des *affectations parallèles* à l'aide d'un seul
opérateur :



```python
>>> a, b = 4, 8.33
>>> a
4
>>> b
8.33
```



Dans cet exemple, les variables **a** et **b** prennent simultanément
les nouvelles valeurs **4** et **8,33**.

> Les francophones que nous sommes avons pour habitude d*'*utiliser la
> virgule comme séparateur ***décimal, alors que les langages de
> programmation utilisent toujours la convention en vigueur dans les
> pays de langue anglaise, c**'*est-à-dire le point décimal. La virgule,
> quant à elle, est très généralement utilisée pour séparer différents
> éléments (arguments, etc.) comme on le voit dans notre exemple, pour
> les variables elles-mêmes ainsi que pour les valeurs qu*'*on leur
> attribue.

Exercices

.Décrivez le plus clairement et le
plus complètement possible ce qui se passe à chacune des trois lignes de
l'exemple ci-dessous :\



```python
>>> largeur = 20
>>> hauteur = 5 * 9.3
>>> largeur * hauteur
930
```



.Assignez les valeurs respectives 3, 5, 7 à trois variables a, b, c.\
 Effectuez l'opération *a - b//c*. Interprétez le résultat obtenu.

