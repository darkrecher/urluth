# Urluth


## Objectif (urluthilité) de ce projet

Il s'agit d'un site permettant de monétiser des urls avec de la publicité.

Lorsqu'on veut mettre un lien (dans un blog, un site, un commentaire, un mail, une documentation, ...), on ne l'indique pas directement. Au lieu de ça, on l'enregistre dans urluth en lui associant un identifiant, puis on indique un lien vers urluth.

Par exemple :
http://recher.pythonanywhere.com/urluth/?u=ad

Cette adresse mène vers le site urluth qui sert d'intermédiaire. La page affichée contient l'url finale (retrouvée grâce à l'identifiant spécifié en paramètre), ainsi que de la publicité. Le cerveau de l'utilisateur est monétisé grâce à ces pubs, ensuite il peut suivre le lien, soit en cliquant dessus, soit en attendant quelques secondes (redirection automatique).

Dans la version actuelle du projet, toutes les publicités affichées me font gagner des bitcoins, il n'y a pas d'autre monnaie utilisée. Rien ne vous empêche de forker le projet et de mettre vos publicités à vous, gérées par n'importe quelle site, avec n'importe quelle monnaie.

Ce site effectue la même tâche (en moins bien) que coinUrl. J'ai souhaité avoir cette alternative car coinUrl est lent à envoyer les bitcoins que je gagne chez eux, qu'ils n'ont jamais répondu à ma demande de support et qu'ils m'avaient accidentellement banni. Pour plus de détails : https://recher.wordpress.com/2016/01/27/coinurl-mmmppfffeeeuaarrgh/


## Installation actuelle en production

Le site fonctionne sur un serveur Flask.

Il est actuellement en production sur la plate-forme d'hébergement pythonanywhere, à l'adresse : [http://recher.pythonanywhere.com/](http://recher.pythonanywhere.com/), mais le code n'est pas exactement le même.

Pythonanywhere héberge deux applications différente, chacune dans un "Blueprint" :

 - urluth
 - expressionotron (https://github.com/darkrecher/expressionotron).

Ce repository contient uniquement le code de l'application urluth, ainsi que le fichier python principal `repo_git/urluth/server/mysite/flask_app.py`.


## Exécution en local

Voir : [doc/exec_en_local.md](doc/exec_en_local.md)


## Configuration dans l'hébergeur PythonAnywhere

Voir : [doc/mise_en_prod_pythonanywhere.md](doc/mise_en_prod_pythonanywhere.md)


## Document de conception

Voir : [doc/doc_conception.md](doc/doc_conception.md)


## Crédits

Créé par Réchèr.

Le code et cette doc sont sous une double licence : Art Libre ou Creative Commons CC-BY (au choix). N'hésitez pas à en faire ce que vous voulez.

Repository : https://github.com/darkrecher/urluth

Mon blog : http://recher.wordpress.com

J'accepte les dons en diverses crypto-monnaies.

 - Bitcoin (BTC) : 12wF4PWLeVAoaU1ozD1cnQprSiKr6dYW1G
 - Litecoin (LTC) : LQfceQahHPwXS9ByKF8NtdT4TJeQoDWTaF
 - Dogecoin (Ð) : DKQUVP7on5K6stnLffKp3mHJor3nzYTLnS
 - Next (NXT) : 12693681966999686910

