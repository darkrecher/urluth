import os
from flask import Blueprint, request
from .build_dict_urls import final_urls_from_key_urls

# http://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
app_urluth = Blueprint("app_urluth", __name__)

# REC TODO : mettre ça dans un fichier de config
#TEMPLATE_FILE_PATH = "urluth" + os.sep + "template.html"
# non. Il faut utiliser les templates, comme tout le monde.
# http://flask.pocoo.org/docs/0.11/api/#flask.render_template
# http://flask.pocoo.org/docs/0.11/blueprints/
TEMPLATE_FILE_PATH = "/home/Recher/mysite/urluth/template.html"
# RECTODO : debug. Serveur local.
TEMPLATE_FILE_PATH = 'C:\\Recher\\git\\urluth\\server\\mysite\\urluth\\template.html'

FINAL_URL_TEXT_ID = "{{final_url}}"


def init_templates_html():

    template_html = "failed reading template html"
    with open(TEMPLATE_FILE_PATH, encoding="utf-8") as template_file:
        template_html = template_file.read()

    PAGE_STATIC_TEXTS = (
        (
            "found", "{{here_is_link_fr}}",
            "Voici le lien qui vous intéresse :"),
        (
            "found", "{{here_is_link_en}}",
            "Here is the desired link :"),
        (
            "not_found", "{{here_is_link_fr}}",
            "Désolé, le lien que vous voulez est introuvable. En voici un autre :"),
        (
            "not_found", "{{here_is_link_en}}",
            "Sorry, your link can not be found. Here is another one :"),
        (
            "not_found", FINAL_URL_TEXT_ID,
            "http://recher.wordpress.com"),
    )

    tplh_key_found = template_html
    tplh_key_not_found = template_html

    for (is_found, text_id, text) in PAGE_STATIC_TEXTS:
        if is_found == "found":
            tplh_key_found = tplh_key_found.replace(text_id, text)
        else:
            tplh_key_not_found = tplh_key_not_found.replace(text_id, text)

    return tplh_key_found, tplh_key_not_found

tplh_key_found, tplh_key_not_found = init_templates_html()


# Si on a besoin de router n'importe quelle adresse et de l'analyser après :
# http://flask.pocoo.org/snippets/57/
# Mais là c'est pas ça que je veux faire.

@app_urluth.route('/',  methods=["GET"])
def urluthGet():

    key_url = request.args.get("u", "")
    if not key_url.isalnum():
        return tplh_key_not_found

    final_url = final_urls_from_key_urls.get(key_url)
    if final_url is None:
        return tplh_key_not_found
    else:
        return tplh_key_found.replace(FINAL_URL_TEXT_ID, final_url)
