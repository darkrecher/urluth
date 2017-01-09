# Document de conception

Bon c'est assez simple, au départ il n'y a qu'une seule page web : la page de présentation contenant les liens vers les applications (en Flask, ça s'appelle des [Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/)).

Le Blueprint urluth contient une seule page, générée dynamiquement. Selon la valeur indiquée en paramètre, la page affiche un lien vers un autre site. Elle contient également des publicités, c'est le but principal.

L'autre application (expressionotron) contient une page et une tâche planifiée. Elles ne sont pas décrites dans cette documentation.

## flask_app.py

Fichier principal du site. Il effectue les actions suivantes :

 - Tentative d'importation du Blueprint "expressionotron". Cette tentative est exécutée dans un bloc try-except. Si le Blueprint n'est pas présent (impossible de trouver et d'importer les fichiers python), l'exécution ne se bloque pas. La variable `app_expressionotron` contient le Blueprint chargé, ou None si ça a échoué.

 - Si le chargement a réussi, enregistrement du Blueprint dans le site, avec le préfixe d'url `expressionotron`. Ce qui veut dire que toutes les requêtes HTTP commençant par ce préfixe seront redirigées vers ce Blueprint (le préfixe est préalablement enlevé de l'url de la requête avant d'être envoyée au Blueprint).

 - Même principe avec le Blueprint "urluth". La variable `app_urluth` contient ce Blueprint, ou None si l'import a échoué.

 - Enregistrement du Blueprint `app_urluth`, si celui-ci est défini, avec le préfixe d'url `urluth`.

 - exécution de la fonction `generate_main_page`, qui effectue les actions suivantes :

     + Début de la génération d'une page html toute simple.

     + Si le Blueprint `app_expressionotron` existe, ajout d'un lien dans la page html, permettant d'aller à la page principale de l'expressionotron.

     + Si le Blueprint `app_urluth` existe, ajout d'un lien dans la page html, permettant d'aller à la page principale d'urluth.

     + Renvoi de la page html simple, sous forme d'une chaîne de caractères.

(TODO : exemple)


## appurluth.py

## build\_dict\_urls.py

## templates/template.html

## js/urluth\_index.js



