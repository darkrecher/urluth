import os
from flask import Blueprint, request, render_template
from .build_dict_urls import final_urls_from_key_urls

# http://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
# Il faut utiliser les templates html, comme tout le monde.
# http://flask.pocoo.org/docs/0.11/api/#flask.render_template
# http://flask.pocoo.org/docs/0.11/blueprints/
app_urluth = Blueprint('app_urluth', __name__, template_folder='templates')


# Si on a besoin de router n'importe quelle adresse et de l'analyser après :
# http://flask.pocoo.org/snippets/57/
# Mais là c'est pas ça que je veux faire.

DICT_PARAMS_URL_OK = {
    'here_is_link_fr':
    "Voici le lien qui vous intéresse :",

    'here_is_link_en':
    "Here is the desired link :",
}

DICT_PARAMS_URL_NOT_FOUND = {
    'here_is_link_fr':
    "Désolé, le lien que vous voulez est introuvable. En voici un autre :",

    'here_is_link_en':
    "Sorry, your link can not be found. Here is another one :",
}

@app_urluth.route('/',  methods=['GET'])
def urluth_get():

    key_url = request.args.get('u', '')
    if not key_url.isalnum():
        final_url = None
    else:
         final_url = final_urls_from_key_urls.get(key_url)

    if final_url is None:
        params_template = DICT_PARAMS_URL_NOT_FOUND
        params_template['final_url'] = 'http://recher.wordpress.com'
    else:
        params_template = DICT_PARAMS_URL_OK
        params_template['final_url'] = final_url

    return render_template('template_urluth.html', **params_template)
