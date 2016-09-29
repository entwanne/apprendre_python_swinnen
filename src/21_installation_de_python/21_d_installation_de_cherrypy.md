## 21-D - Installation de Cherrypy

Cherrypy est un produit indépendant qui dispose de son propre site web
officiel :

http://cherrypy.org. Visitez plus précisément la section download :

http://cherrypy.org/wiki/CherryPyDownload

À l'heure où nous écrivons ces lignes (13/01/2010), la seule version de
Cherrypy qui fonctionne avec Python3 est encore en cours de test, et
donc toujours considérée comme « instable ». Il faut donc la chercher
dans la section :

*Non-stable releases: http://download.cherrypy.org/cherrypy/3.2.0rc1*

et sélectionner l'un des fichiers *CherryPy-3.2.0rc1-py3.zip* ou
*CherryPy-3.2.0rc1-py3.tar.gz* (pour tous systèmes), ou encore
*CherryPy-3.2.0rc1-py3.win32.exe* (pour Windows uniquement).

-   Si vous travaillez sous Windows, il suffira de lancer l'exécutable
    téléchargé (installeur automatique).
-   Si vous travaillez sous Linux ou un autre système d'exploitation, il
    vous suffit de copier le fichier archive téléchargé (.zip ou
    .tar.gz) dans un répertoire temporaire quelconque, de le décomprimer
    à l'aide du logiciel approprié (unzip ou tar), puis de lancer la
    commande :\
    `python3 setup.py install `(en
    tant que *root*) à partir du répertoire temporaire utilisé.

Lorsque vous lirez ces lignes, vous pourrez vraisemblablement disposer
d'une version plus récente tout à fait stable. Si ce n'est pas encore le
cas et que vous devez utiliser la même que nous, vous devrez
probablement remplacer un fichier bogué (erreur « invalid buffer size »
au démarrage). Nous fournissons une version corrigée de ce fichier sur
notre site, avec les autres fichiers téléchargeables concernant ce livre
(Voir : *http://inforef.be/swi/python.htm*).

