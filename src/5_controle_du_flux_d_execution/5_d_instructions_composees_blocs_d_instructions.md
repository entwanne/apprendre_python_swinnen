## 5-D - Instructions composées - blocs d'instructions

La construction que vous avez utilisée avec l'instruction **if**est
votre premier exemple d'**instruction composée**. Vous en rencontrerez
bientôt d'autres. Sous Python, les instructions composées ont toujours
la même structure : une ligne d'en-tête terminée par un double point,
suivie d'une ou de plusieurs instructions indentées sous cette ligne
d'en-tête. Exemple :



```python
Ligne d'en-tête:
 première instruction du bloc
 ... ...
 ... ...
 dernière instruction du bloc
```



S'il y a plusieurs instructions indentées sous la ligne d'en-tête, elles
doivent l'être exactement au même niveau (comptez un décalage de 4
caractères, par exemple). Ces instructions indentées constituent ce que
nous appellerons désormais un bloc d'instructions. Un bloc
d'instructions est une suite d'instructions formant un ensemble logique,
qui n'est exécuté que dans certaines conditions définies dans la ligne
d'en-tête. Dans l'exemple du paragraphe précédent, les deux lignes
d'instructions indentées sous la ligne contenant l'instruction
**if**constituent un même bloc logique : ces deux lignes ne sont
exécutées - toutes les deux - que si la condition testée avec
l'instruction **if**se révèle vraie, c'est-à-dire si le reste de la
division de **a**par 2 est nul.

