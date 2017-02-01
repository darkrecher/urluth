# Document de conception

La page de présentation est toute simple, pas de JS ni de CSS. Elle contient les liens vers les applications qui ont pu être chargées (en Flask, ça s'appelle des [Blueprints](http://flask.pocoo.org/docs/0.12/blueprints/)).

Le Blueprint urluth contient une seule page, générée dynamiquement. Selon la valeur indiquée en paramètre, la page affiche un lien vers un autre site (dans la suite de ce document, ce lien est appelé "url finale", parce que c'est là où l'utilisateur veut se rendre). La page contient également des publicités, c'est le but principal.

L'autre Blueprint (expressionotron) contient une page et une tâche planifiée. Elles ne sont pas décrites dans cette documentation.

Tous les fichiers mentionnés dans cette documentation se trouve dans `repo_git/urluth/server/mysite`, ce chemin de base n'est donc pas mentionné à chaque fichier.


## flask_app.py

Fichier principal du site.

### Démarrage du serveur

Lors de l'exécution de ce fichier, les actions suivantes sont effectuées :

 - Tentative d'importation du Blueprint "expressionotron" et stockage dans la variable `app_expressionotron`. Cette tentative est exécutée dans un bloc try-except. Si le Blueprint n'est pas présent (impossible de trouver ou d'importer les fichiers python), l'exécution ne se bloque pas, mais `app_expressionotron` vaut None.

 - Si le chargement a réussi, enregistrement du Blueprint dans le site, avec le préfixe d'url `expressionotron`. Ce qui veut dire que toutes les requêtes HTTP commençant par ce préfixe seront redirigées vers ce Blueprint.

 - Même principe avec urluth. La variable `app_urluth` contient le Blueprint "urluth", ou None si l'import a échoué.

 - Si `app_urluth` ne vaut pas None, enregistrement du Blueprint dans le site, avec le préfixe d'url `urluth`.

 - Lancement de l'application pour démarrer le serveur.

L'application doit avoir une "secret key" pour fonctionner. C'est une chaîne de caractère contenant ce qu'on veut. Je ne sais pas exactement à quoi ça sert, je suppose que c'est pour la sécurité, le HTTPS ou quelque chose comme ça. Cette secret key est importée depuis le fichier `secret_key.py`. Il y a une version de ce fichier dans ce repository, qui n'est bien évidemment pas la même que celle qui est réellement utilisée sur pythonanywhere. La vraie secret key n'est pas disponible publiquement.

### Construction et renvoi de la page de présentation du site

D'autre part, le fichier `flask_app.py` contient la fonction `generate_main_page`, qui est appelée lorsqu'il faut répondre à une requête HTTP sur l'url racine du site (juste un slash, sans préfixe). Cette fonction effectue les actions suivantes :

 - Début de la génération d'une page HTML toute simple.

 - Si le Blueprint `app_expressionotron` existe, écriture d'un lien dans la page HTML. L'url de ce lien est construite de façon à pointer vers la page unique de l'expressionotron.

 - Si le Blueprint `app_urluth` existe, écriture d'un autre lien dans la page HTML, permettant d'aller à la page unique d'urluth.

 - Renvoi de la page, sous forme d'une chaîne de caractères.

Exemple de code HTML renvoyé (lorsque les deux Blueprints sont présents) :

    Il n'y a pas grand-chose ici. Vous pouvez juste :<br/>
     - <a href="/expressionotron/">cliquez ici pour aller &agrave; l'expressionotron</a><br/>
     - <a href="/urluth/">cliquez ici pour consulter urluth</a><br/>

Pas de balise `html`, `body`, `head`, etc. C'est vraiment au plus simple.


## urluth/appurluth.py

Fichier principal de l'application urluth. Il crée le Blueprint `app_urluth`.

Ce fichier contient une seule fonction `urluth_get`, censée répondre à une requête HTTP ayant l'url "/" (url racine). Dans les faits, l'url de départ est "/urluth". Le fichier `flask_app.py` l'intercepte et détecte la présence du préfixe. Ce préfixe est supprimé, puis la requête est transmise à `app_urluth`. L'url résultante est donc l'url racine, qui est interceptée par `urluthGet`.

La page HTML renvoyée est générée avec le moteur de template "jinja2", intégré à Flask. Le fichier de template utilisé est `urluth/templates/template_urluth.html`.

La fonction `urluth_get` vérifie le paramètre `u` de la requête HTTP. Il doit exister et sa valeur doit correspondre à une clé du dictionnaire `final_urls_from_key_urls`. Dans tous les cas, c'est le même template HTML qui est utilisé. Mais en fonction de la clé existante ou pas, les textes envoyés au moteur de template pour générer la page web sont différents.

Si le paramètre `u` est bien une clé, les textes envoyés au template sont ceux du dictionnaire de constantes `DICT_PARAMS_URL_OK`. Le lien (l'url finale) se trouve dans le dictionnaire `final_urls_from_key_urls`, il s'agit de la valeur dont la clé est le paramètre `u`. Cette url finale est également envoyée au template.

Si le paramètre `u` est inexistant ou n'est pas une clé, les textes envoyés au template sont ceux du dictionnaire de constantes `DICT_PARAMS_URL_NOT_FOUND`, ils indiquent que le lien n'a pas été trouvé. L'url finale envoyée au template est un lien par défaut : "http://recher.wordpress.com".


## urluth/build\_dict\_urls.py, urluth/data\_urls.py

`data_urls.py` contient une seule grande chaîne de caractère multi-ligne : `bigstring_urls`. Ce format de donnée a été choisi, car c'est ce qui est le plus simple à mettre à jour.

Chaque ligne de `bigstring_urls` est une correspondance entre une valeur possible du paramètre `u` de la requête HTTP, et une url finale affichée dans la page web. Les lignes vides ne sont pas prises en compte.

Le paramètre `u` et l'url doivent être séparés par un ou plusieurs espaces.

Le fichier `build_dict_urls.py` lit la donnée `bigstring_urls` pour créer le dictionnaire `final_urls_from_key_urls`. clé : paramètre `u`. valeur : url finale.

Il n'y a pas de contrôle sur l'unicité des clés. Si `bigstring_urls` contient plusieurs fois le même paramètre `u`, c'est le dernier de chaque qui sera pris en compte.


## urluth/templates/template_urluth.html

Il s'agit du fichier de template utilisé pour générer la page unique de urluth, avec les éléments suivants :

 - des publicités diverses.
 - l'url finale sur laquelle l'utilisateur est censé cliquer. S'il n'a pas cliqué au bout de 50 secondes, une redirection automatique est effectuée vers cette url. Le compteur peut être arrêté en cliquant sur le nombre indiquant le temps restant.
 - divers textes de blabla.
 - deux boutons permettant de changer le langage des textes (français ou anglais).

### Fichiers additionnels

En dehors de ce qui est imposé par les encarts publicitaires (voir chapitre suivant), le template contient une référence vers 3 fichiers :

 - `urluth/img/drapalfr.png` : image du drapeau français. Utilisé comme bouton pour mettre la page en français.
 - `urluth/img/drapalen.png` : pareil, mais drapeau anglais.
 - `urluth/js/urluth_index.js` : fichier javascript définissant les comportements interactifs de la page.

Le CSS est intégré dans le template HTML. C'est pas génial, mais c'est le plus simple, puisqu'il n'y a qu'une page.

### Éléments imposés par les encarts publicitaires

Les parties de HTML suivantes sont à insérer telle quelle dans la page, au bon endroit (voir documentation respectives des sites à publicité)

#### Adbit :

`<meta name="adbit-site-verification" content="8844b9f937c9c2d0a196f3d1e3775f524593b6f4ba886b4bddd4d353cd65af36" />`

`<script type="text/javascript" src="https://adbit.co/js/show_ads.js"></script>`

`<div class="adbit-display-ad" data-adspace-id="754F5AE8F1"></div>`

#### Anonymous ads :

`<iframe data-aa='273455' src='https://ad.a-ads.com/273455?size=468x60' scrolling='no' style='width:468px; height:60px; border:0px; padding:0;overflow:hidden' allowtransparency='true' frameborder='0'></iframe>`

`<iframe data-aa='143164' src='https://ad.a-ads.com/143164?size=300x250' scrolling='no' style='width:300px; height:250px; border:0px; padding:0;overflow:hidden' allowtransparency='true' frameborder='0'></iframe>`

#### Blockadz

    <center>
      <div>
        <iframe scrolling="no" src="//blockadz.com/ads/show/show.php?a=E1GPX7V6IJNOA&b=7WVAHMEV3AEJJ" style="overflow:hidden;width:468px;height:60px;" frameborder="0"></iframe>
      </div>
      <div style="text-align:center;">
        <a href="https://blockadz.com/?a=BuyAds&id=E1GPX7V6IJNOA" target="_blank">Advertise in this spot</a>
      </div>
    </center>

    <center>
      <div>
        <iframe scrolling="no" src="//blockadz.com/ads/show/show.php?a=E1GPX7V6IJNOA&b=HYXVT2VFEZD35" style="overflow:hidden;width:300px;height:250px;" frameborder="0"></iframe>
      </div>
      <div style="text-align:center;">
        <a href="https://blockadz.com/?a=BuyAds&id=E1GPX7V6IJNOA" target="_blank">Advertise in this spot</a>
      </div>
    </center>

#### Coinhits

`<iframe src="http://coinhits.com/ad/pbnr2.php?ref=563" marginwidth="0" marginheight="0" width="468" height="60" scrolling="no" border="0" frameborder="0"></iframe>`

#### Coinmedia

`<iframe src="http://coinmedia.co/new_code_site23973.js" scrolling="no" frameborder="0" width="468px" height="90px"></iframe>`

### Gestion du changement de langue

Il n'y a que deux langues et une seule page. Le changement de langue a donc été fait au plus simple.

Lorsque le fichier HTML est généré, il contient déjà tous les textes des deux langues différentes. Les balises HTML des textes anglais possèdent la classe `lang-en`, les balises du français possèdent la classe `lang-fr`. La langue par défaut est le français. Au départ, toutes les balises HTML ayant la classe `lang-en` sont invisibles (elles ont la classe `hidden`).

Lorsqu'on clique sur l'un ou l'autre des boutons de langue, on enlève/ajoute la classe `hidden` aux balises de texte, pour rendre visible ceux d'une langue et pas ceux de l'autre.

C'est donc tout géré localement par le client web. Il n'y a pas besoin d'échanges avec le serveur lors d'un changement de langue. C'est clairement pas comme ça qu'il faut faire pour des vrais sites. Mais dans notre cas, c'est tout à fait adapté.

### Affichage du décompte restant

L'affichage est effectué par la balise HTML ayant l'identifiant `text-countdown` :

    <span id="text-countdown" class="clickable">
      50
    </span>

Le temps initial est de 50 secondes, il est réactualisé toutes les 10 secondes. Lorsqu'on clique sur le temps restant, le décompte s'arrête et la valeur affichée est : +∞ ("plus l'infini").

Tous ces comportements sont gérés par le javascript (voir : `urluth/js/urluth_index.js`).

### Placement des publicités

Tous les encarts publicitaires sont dans une balise `<div>` ayant la classe `ad-placement`. Cette classe est associé à du CSS permettant de placer les encarts les uns à côté des autres.

Il y a deux encarts côte à côte, puis deux autres en dessous et ainsi de suite. Chaque couple d'encarts est placé dans une autre balise `<div>`, ayant la classe `clear-both`. Le CSS de cette classe fait placer les éléments en-dessous et non pas côte à côte. Les autres éléments de la page (le texte en haut, celui en bas, etc.) sont également répartis dans des `<div>` avec `clear-both`. En gros, quand on veut aller à la ligne, on met un `clear-both`.


## urluth/js/urluth\_index.js

Il y a déjà quelques commentaires dans le code qui aident à comprendre.

Comme le projet est très simple, c'est du javascript pur. Pas de jQuery ni quoi que ce soit d'autre.

### Gestion du changement de langue

Fonction `hasClass` : fonction générique, avec deux paramètres : `element`, `cls`. Renvoie true si l'élément HTML `element` possède la classe `cls`

Fonction `change_lang`. Modifie les textes de la page pour mettre en anglais ou en français, en fonction du paramètre `language` (chaîne de caractère). `language='en'` : anglais. `language=<n'importe quoi d'autre>` : français.

Le but de cette fonction (dans le cas où il faut mettre en français) est d'ajouter la classe `hidden` sur tous les éléments HTML ayant la classe `lang-fr`, et d'enlever cette classe `hidden` sur tous ceux ayant la classe `lang-fr`. Dans le cas où il faut mettre en anglais, c'est le contraire.

En javascript pur, il n'y a pas de moyen simple pour enlever une classe à un élément. Il faut réécrire toutes les classes, sauf celle qu'on veut enlever. C'est ce que le code de la fonction fait. Sauf que ça pose un petit problème.

Au début de la page se trouve le texte "voici le lien qui vous intéresse", qui change en fonction de la langue, comme tous les autres. Sauf que pour la bonne disposition dans la page, la balise contenant ce texte doit avoir une classe supplémentaire : `intro-phrase-margin`.

Lorsqu'on réécrit toutes les classes pour changer la langue, il faut vérifier si au départ cette classe `intro-phrase-margin` est présente ou non. Si elle l'est, elle est re-rajoutée. Ça marche uniquement avec cette classe là, d'autres éventuelles noms de classe ne seraient pas gérées.

Par conséquent, le code de la fonction `change_lang` n'est pas générique du tout. Si on a besoin d'avoir d'autres classes dans des éléments qui changent selon la langue, ça ne marchera plus du tout. Mais on ne va pas se prendre la tête plus que ça pour ce projet.

Le code juste après la fonction `change_lang` est exécuté dès le chargement du fichier javascript. Il associe l'exécution de cette fonction (avec le bon paramètre à chaque fois) aux deux images de drapeaux français et anglais qui sont en haut à droite de la page.

La fonction `is_browser_french` utilise les paramètres du navigateur pour déterminer si la langue courante de l'utilisateur est le français ou une autre. Elle renvoie True si c'est français, False sinon. (C'est une fonction un peu chauvine).

Cette fonction n'est pas générique. Si un jour on veut une troisième langue, il faudra la refaire, mais on n'en est pas là.

Le code juste après la fonction `is_browser_french` est également exécuté dès le chargement. Il exécute la fonction, et si le résultat est False (navigateur pas en français), il exécute la fonction `change_lang('en)` pour mettre en anglais.

### Gestion de la décompte du temps et redirection automatique

Le nombre de secondes restant avant la redirection vers l'url finale est stocké dans la variable globale `seconds_left`.

Fonction `redirection_countdown` : cette fonction diminue de 10 secondes la variable `seconds_left`, et réactualise le texte dans la page affichant ce décompte. L'élément HTML affichant ce texte est identifié par l'attribut `id=text-countdown`.

Cette fonction vérifie également la valeur de `seconds_left`. Lorsque celle-ci atteint 0, la fonction récupère la valeur de l'attribut `href` de l'élément `final-url` (c'est à dire l'url vers laquelle l'utilisateur est censé aller), et elle indique au navigateur web qu'il faut aller à cette url.

La ligne de code juste après la fonction `redirection_countdown` déclenche un appel périodique (toutes les 10 secondes) de cette même fonction. Cette appel périodique est stocké dans une variable globale `periodic_exec_redirection`. Cette création d'appel périodique est effectuée dès le chargement.

Le code qui vient après définit le comportement lorsqu'on clique sur l'élément HTML `text-countdown`. Ce comportement est directement implémenté par une espèce de fonction inline (je ne sais pas si ça s'appelle comme ça en javascript). Deux actions sont effectuées :

 - arrêt de l'appel périodique précédemment défini, en désactivant la variable `periodic_exec_redirection`,
 - modification du texte dans l'élément `text-countdown`, en le remplaçant par "+∞".

