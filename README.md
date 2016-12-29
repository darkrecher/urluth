# Urluth


## Objectif (urluthilité de ce projet)

Il s'agit d'un site permettant de monétiser des urls avec de la publicité.

Lorsqu'on veut indiquer un lien (dans un blog, un site, un commentaire, un mail, une documentation, ...), on ne met pas directement l'adresse du lien final. On enregistre le lien dans urluth, avec un identifiant. Ensuite, on met un lien vers le site urluth, avec ce même identifiant.

Par exemple :
http://recher.pythonanywhere.com/urluth/?u=ad

Cette adresse mène vers le site urluth qui sert d'intermédiaire. La page affiché contient le lien final, ainsi que de la publicité. L'utilisateur peut regarder et cliquer sur cet pubs (bref, on lui prend un petit morceau de son cerveau). Ensuite il peut aller vers le lien final, soit en cliquant dessus, soit en attendant quelques secondes (redirection automatique).

Dans la version actuelle du projet, toutes les publicités affichées permettent de me faire gagner des bitcoins, il n'y a pas d'autres monnaies utilisée. Rien ne vous empêche, bien entendu, de forker le projet et de mettre vos publicités à vous, gérées par n'importe quelle site, avec n'importe quelle monnaie.

Ce site effectue la même tâche (en moins bien) que coinUrl. J'ai souhaité me faire une alternative à coinUrl car ils sont lent à envoyer les bitcoins que je gagne chez eux, qu'ils n'ont jamais répondu à ma demande de support, et qu'ils m'avaient accidentellement banni. Pour plus de détails, : https://recher.wordpress.com/2016/01/27/coinurl-mmmppfffeeeuaarrgh/


## Installation

Le site fonctionne sur un serveur Flask.

Il est actuellement installé sur la plate-forme d'hébergement pythonanywhere, à l'adresse : http://recher.pythonanywhere.com/

Le code dans ce repository n'est pas le même que celui dans pythonanywhere.

Il y a deux applications différentes dans pythonanywhere : urluth, et expressionotron (https://github.com/darkrecher/expressionotron).

Ces deux applications sont chacune dans un "Blueprints". Le code du fichier d'entrée `repo_git/urluth/server/mysite/flask_app.py` peut être lancé même si l'une des deux applications est manquante. Il devrait donc être possible d'exécuter le code de ce repository tel quel, dans un environnement autre que pythonanywhere. (Ça a été plus ou moins testé, mais pas en détail).


## Configuration dans l'hébergeur PythonAnywhere

RECTODO : à compléter.


## Document de conception

RECTODO : à compléter


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


## Restant à faire

RECTODO : exporter/écrire/screenshotter la config de pythonanywhere

RECTODO : doc d'installation dans pythonanywhere, et éventuellement de test en local.

RECTODO : doc de conception, mais très rapide. (expliquer le coup de la secret key)

RECTODO : remplacer le signe "+oo"

RECTODO : changer les guillemets double en simple, partout où il faut.

RECTODO : revérifier les TODO restants dans le code. Mais normalement y'a plus.
