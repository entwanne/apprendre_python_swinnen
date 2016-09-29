## 4-C - Noms de variables et mots réservés

Les noms de variables sont des noms que vous choisissez vous-même assez
librement. Efforcez-vous cependant de bien les choisir : de préférence
assez courts, mais aussi explicites que possible, de manière à exprimer
clairement ce que la variable est censée contenir. Par exemple, des noms
de variables tels que *altitude*, *altit* ou *alt* conviennent mieux que
x pour exprimer une altitude.

> ***Un bon programmeur doit veiller à ce que ses lignes d'instructions
> soient faciles à lire.***

Sous Python, les noms de variables doivent en outre obéir à quelques
règles simples :

-   Un nom de variable est une séquence de lettres (a → z , A → Z) et de
    chiffres (0 → 9), qui doit toujours commencer par une lettre.
-   Seules les lettres ordinaires sont autorisées. Les lettres
    accentuées, les cédilles, les espaces, les caractères spéciaux tels
    que \$, \#, @, etc. sont interdits, à l'exception du caractère \_
    (souligné).
-   La casse est significative (les caractères majuscules et minuscules
    sont distingués).\
    *Attention : Joseph, joseph, JOSEPH sont donc des variables
    différentes. Soyez attentifs !*

Prenez l'habitude d'écrire l'essentiel des noms de variables en
caractères minuscules (y compris la première lettre[^note_7]).
Il s'agit d'une simple convention, mais elle est largement respectée.
N'utilisez les majuscules qu'à l'intérieur même du nom, pour en
augmenter éventuellement la lisibilité, comme dans *tableDesMatieres*.

En plus de ces règles, il faut encore ajouter que vous ne pouvez pas
utiliser comme nom de variables les 33 « mots réservés » ci-dessous (ils
sont utilisés par le langage lui-même) :



  ---------- ---------- ---------- ---------- ---------- ---------- ----------
  and        as         assert     break      class      continue   def
  del        elif       else       except     False      finally    for
  from       global     if         import     in         is         lambda
  None       nonlocal   not        or         pass       raise      return
  True       try        while      with       yield                 
  ---------- ---------- ---------- ---------- ---------- ---------- ----------




[^note_7]: Les noms commençant par une majuscule ne sont pas interdits, mais l'usage veut qu'on le réserve plutôt aux variables qui désignent des *classes* (le concept de classe sera abordé plus loin dans cet ouvrage). Il arrive aussi que l'on écrive entièrement en majuscules certaines variables que l'on souhaite traiter comme des pseudo-constantes (c'est-à-dire des variables que l'on évite de modifier au cours du programme).
