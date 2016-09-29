## 3-E - Édition du code source - Interprétation

Le programme tel que nous l'écrivons dans un langage de programmation
quelconque est à strictement parler un simple texte. Pour rédiger ce
texte, on peut faire appel à toutes sortes de logiciels plus ou moins
perfectionnés, à la condition qu'ils ne produisent que du texte brut,
c'est-à-dire sans mise en page particulière ni aucun attribut de style
(pas de spécification de police, donc, pas de gros titres, pas de gras,
ni de souligné, ni d'italique, etc.)[^note_3].

Le texte ainsi produit est ce que nous appellerons désormais un « code
source ».

Comme nous l'avons déjà évoqué plus haut, le code source doit être
traduit en une suite d'instructions binaires directement compréhensibles
par la machine : le « code objet ». Dans le cas de Python, cette
traduction est prise en charge par un *interpréteur* assisté d'un
*pré-compilateur*. Cette technique hybride (également utilisée par le
langage *Java*) vise à exploiter au maximum les avantages de
l'interprétation et de la compilation, tout en minimisant leurs
inconvénients respectifs.

Veuillez consulter un ouvrage d'informatique générale si vous voulez en
savoir davantage sur ces deux techniques. Sachez simplement à ce sujet
que vous pourrez réaliser des programmes extrêmement performants avec
Python, même s'il est indiscutable qu'un langage strictement compilé tel
que le C peut toujours faire mieux en termes de rapidité d'exécution.


[^note_3]: Ces logiciels sont appelés des *éditeurs de texte*. Même s'ils proposent divers automatismes, et sont souvent capables de mettre en évidence certains éléments du texte traité (coloration syntaxique, par ex.), ils ne produisent strictement que du texte non formaté. Ils sont donc assez différents des logiciels de *traitement de texte*, dont la fonction consiste justement à mettre en page et à ornementer un texte avec des attributs de toute sorte, de manière à le rendre aussi agréable à lire que possible.
