## 21-E - Installation de pg8000

***pg8000*** est l'un des nombreux modules d'interface permettant
d'accéder à un serveur *PostgreSQL* depuis Python. Ce n'est pas le plus
performant, mais il a le mérite d'être déjà disponible pour Python 3 à
l'heure ou nous écrivons ces lignes, ce qui n'est pas encore le cas de
tous les autres. De plus, ce module est lui-même entièrement écrit en
Python et ne nécessite la présence d'aucune bibliothèque complémentaire,
ce qui fait que les applications Python qui l'utilisent restent
parfaitement portables.

Lorsque vous lirez ces lignes, des modules plus performants seront
certainement disponibles, tels l'excellent *psycopg2*. Veuillez donc
consulter les sites web traitant de l'interfaçage Python-PostgreSQL pour
en savoir davantage si vous souhaitez développer une application d'une
certaine importance.

Pour installer *pg8000* sur votre système, visitez le site web :
*http://pybrary.net/pg8000/* , et téléchargez le fichier correspondant à
la dernière version disponible, qui soit spécifique de Python 3 (par
exemple *pg8000-py3-1.07.zip* au moment où nous écrivons ces lignes). Il
vous suffit ensuite de copier le fichier archive téléchargé dans un
répertoire temporaire quelconque, de le décomprimer à l'aide du logiciel
approprié (unzip), puis de lancer la commande :\
`python3 setup.py install `(en
tant qu'administrateur) à partir du répertoire temporaire utilisé.

