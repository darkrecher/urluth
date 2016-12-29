// Gestion du changement de la langue français/anglais

function change_lang(language)
{
    var classes_en;
    var classes_fr;
    if (language == 'en') {
        classes_en = 'lang-en';
        classes_fr = 'lang-fr hidden';
    }
    else
    {
        classes_en = 'lang-en hidden';
        classes_fr = 'lang-fr';
    }

    // http://stackoverflow.com/questions/195951/change-an-elements-class-with-javascript
    // C'est moche, car je redéfinis toutes les classes au lieu de juste enlever/ajouter le hidden.
    // Mais je veux pas me prendre la tête avec du code compliqué de regex ou de jquery.
    // C'est pas non plus le projet du siècle.
    var texts_en = document.getElementsByClassName('lang-en');
    for (var i=0; i<texts_en.length; i++)
    {
        texts_en[i].className = classes_en;
    }
    var texts_fr = document.getElementsByClassName('lang-fr');
    for (var i=0; i<texts_fr.length; i++)
    {
        texts_fr[i].className = classes_fr;
    }

}

var elem_flag_fr = document.getElementById('flag-fr');
elem_flag_fr.addEventListener('click', function() {
    change_lang('fr');
});

var elem_flag_en = document.getElementById('flag-en');
elem_flag_en.addEventListener('click', function() {
    change_lang('en');
});

// Détermination initiale de la langue français/étranger
// http://stackoverflow.com/questions/1043339/javascript-for-detecting-browser-language-preference/4079798#4079798

function is_browser_french()
{
    var language = window.navigator.userLanguage ||
                   window.navigator.language;
    language_splitted = language.split('-');
    for (var i=0 ; i<language_splitted.length ; i++)
    {
        var language_part = language_splitted[i];
        if ((language_part == 'fr') || (language_part == 'FR'))
        {
            return true;
        }
    }
    return false;
}

if (is_browser_french())
{
    // Pas besoin de changer la langue vers le français. C'est la langue par défaut.
    //change_lang('fr');
}
else
{
    change_lang('en');
}

// Décompte du temps et redirection automatique

seconds_left = 50;

function redirection_countdown()
{
    seconds_left -= 10;
    var elem_to_change = document.getElementById('text-countdown');
    elem_to_change.innerHTML = seconds_left.toString();
    if (seconds_left == 0)
    {
        clearInterval(periodic_exec_redirection);
        var link_node = document.getElementById('final-url');
        var final_url = link_node.getAttribute('href');
        // http://stackoverflow.com/questions/503093/how-can-i-make-a-redirect-page-using-jquery#506004
        window.location.href = final_url;
    }
}

periodic_exec_redirection = setInterval(redirection_countdown, 10000);

// Arrêt du décompte du temps si on clique sur les secondes restantes.

var elem_text_countdown = document.getElementById('text-countdown');
elem_text_countdown.addEventListener('click', function() {
    clearInterval(periodic_exec_redirection);
    var elem_to_change = document.getElementById('text-countdown');
    elem_to_change.innerHTML = '+&infin;';
});


