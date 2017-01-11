# Document de conception

Bon c'est assez simple, au départ il n'y a qu'une seule page web : la page de présentation contenant les liens vers les applications (en Flask, ça s'appelle des [Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/)).

Le Blueprint urluth contient une seule page, générée dynamiquement. Selon la valeur indiquée en paramètre, la page affiche un lien vers un autre site. Elle contient également des publicités, c'est le but principal.

L'autre application (expressionotron) contient une page et une tâche planifiée. Elles ne sont pas décrites dans cette documentation.

Tous les fichiers mentionnés dans cette documentation se trouve dans `repo_git/urluth/server/mysite`, ce chemin de base n'est donc pas mentionné à chaque fichier.

## flask_app.py

Fichier principal du site.

### Démarrage du serveur

Lors de l'exécution de ce fichier, les actions suivantes sont effectuées :

 - Tentative d'importation du Blueprint "expressionotron". Cette tentative est exécutée dans un bloc try-except. Si le Blueprint n'est pas présent (impossible de trouver et d'importer les fichiers python), l'exécution ne se bloque pas. La variable `app_expressionotron` contient le Blueprint chargé, ou None si ça a échoué.

 - Si le chargement a réussi, enregistrement du Blueprint dans le site, avec le préfixe d'url `expressionotron`. Ce qui veut dire que toutes les requêtes HTTP commençant par ce préfixe seront redirigées vers ce Blueprint (le préfixe est préalablement enlevé de l'url de la requête avant d'être envoyée au Blueprint).

 - Même principe avec le Blueprint "urluth". La variable `app_urluth` contient ce Blueprint, ou None si l'import a échoué.

 - Enregistrement du Blueprint `app_urluth`, si celui-ci est défini, avec le préfixe d'url `urluth`.

 - Lancement de l'application pour démarrer le serveur.

L'application doit avoir une "secret key" pour fonctionner. C'est une chaîne de caractère qui peut contenir un peu ce qu'on veut. Je ne sais pas exactement à quoi ça sert, je suppose que c'est pour la sécurité, le HTTPS ou quelque chose comme ça. Cette secret key est importée depuis le fichier `secret_key.py`. Il y a une version de ce fichier dans ce repository, mais la secret key qu'il contient n'est bien évidemment pas celle qui est réellement utilisée sur pythonanywhere. La vraie version de ce fichier n'est pas disponible publiquement.


### Construction et renvoi de la page de présentation du site

D'autre part, ce fichier contient la fonction `generate_main_page`, qui est appelée lorsqu'il faut répondre à une requête HTTP sur l'url racine du site (juste un slash, sans préfixe). Cette fonction effectue les actions suivantes :

 - Début de la génération d'une page html toute simple.

 - Si le Blueprint `app_expressionotron` existe, ajout d'un lien dans la page html, permettant d'aller à la page principale de l'expressionotron. L'url du lien est construite de façon à pointer vers la page unique de l'expressionotron.

 - Si le Blueprint `app_urluth` existe, ajout d'un lien dans la page html, permettant d'aller à la page unique d'urluth.

 - Renvoi de la page html simple, sous forme d'une chaîne de caractères.

Exemple de code HTML renvoyé (lorsque les deux Blueprints sont présents) :

    Il n'y a pas grand-chose ici. Vous pouvez juste :<br/>
     - <a href="/expressionotron/">cliquez ici pour aller &agrave; l'expressionotron</a><br/>
     - <a href="/urluth/">cliquez ici pour consulter urluth</a><br/>

Pas de balise `html`, `body`, `head`, etc. C'est vraiment au plus simple.


## urluth/appurluth.py

Fichier principal de l'application urluth. Il crée le Blueprint `app_urluth`.

Ce fichier contient une seule fonction censée répondre à une requête HTTP : `urluthGet`. L'url de routage est l'url racine (juste un slash), mais concrètement, avec le préfixe défini dans `flask_app.py`, la fonction est appelé sur l'url "/urluth".

La page web renvoyée est générée avec le moteur de template "jinja2", intégré à Flask. Le fichier de template utilisé est `urluth/templates/template.html`.

La fonction `urluthGet` vérifie le paramètre `u` de la requête HTTP. Il doit exister et sa valeur doit correspondre à une clé du dictionnaire `final_urls_from_key_urls`. Dans tous les cas, c'est le même template HTML qui est utilisé. Mais en fonction de la clé existante ou pas, les textes envoyés au moteur de template pour générer la page web sont différents.

Si le paramètre est une clé, les textes dans le template indiquent qu'on a bien trouvé le lien correspondant. Ils sont dans le dictionnaire de constantes `DICT_PARAMS_URL_OK`. Le lien se trouve dans la valeur dans le dictionnaire `final_urls_from_key_urls` correspondant à la clé. Ce lien est également utilisé dans le template.

Si le paramètre est inexistant ou n'est pas à une clé, les textes dans le template indiquent que le lientn'a pas été trouvé. Ils sont dans le dictionnaire de constantes `DICT_PARAMS_URL_NOT_FOUND`. Le lien utilisé dans le template est un lien par défaut : "http://recher.wordpress.com".


## urluth/build\_dict\_urls.py

## urluth/templates/template.html

## urluth/js/urluth\_index.js



