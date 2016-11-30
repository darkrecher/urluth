# Urluth

## Objectif (urluthilité)

Il s'agit d'un site permettant de monétiser des urls avec de la publicité.

Lorsqu'on veut indiquer un lien (dans un blog, un site, un commentaire, un mail, une documentation, ...), on ne met pas directement l'adresse du lien final. On enregistre le lien dans urluth, avec un identifiant. Ensuite, on met un lien vers le site urluth, avec ce même identifiant.

Par exemple :
http://recher.pythonanywhere.com/urluth/?u=ad

Cette adresse mène vers le site urluth qui sert d'intermédiaire. La page affiché contient le lien final, ainsi que de la publicité. L'utilisateur peut regarder et cliquer sur cet pubs (bref, on lui prend un petit morceau de son cerveau). Ensuite il peut aller vers le lien final, soit en cliquant dessus, soit en attendant quelques secondes (redirection automatique).


RECTODO : écrire un vrai readme : ça fait quoi. lien avec mon article de blog. mélange des deux apps. lien vers l'autre repo (qu'existe pas encore).

RECTODO : mettre des try except lors du chargement des deux apps (urluth et expressionontron).

RECTODO : exporter/écrire/screenshotter la config de pythonanywhere

RECTODO : utiliser les templates. Voir `appurluth.py`

RECTODO : mettre la secret key dans le .profile. Vérifier qu'on peut bien la récupérer.

RECTODO : virer le main de `build_dict_urls.py`. De toutes façons c'est pas comme ça qu'on fait. Il faut qu'un seul point d'entrée. Et vu que ce main ne contient pas de vrais tests. Autant le virer complètement.

RECTODO : doc d'installation dans pythonanywhere, et éventuellement de test en local.

RECTODO : doc de conception, mais très rapide.

RECTODO : voir si y'a pas de la doc que j'ai laissé et qu'il faudrait mettre dans ce repo.

