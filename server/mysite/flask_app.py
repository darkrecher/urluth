from flask import Flask, url_for

app = Flask(__name__)
app.secret_key = 'This is really unique and secret, ou pas'

try:
    from expressionotron.appexpr import app_expressionotron
except ImportError:
    app_expressionotron = None
else:
    app.register_blueprint(app_expressionotron, url_prefix="/expressionotron")

try:
    from urluth.appurluth import app_urluth
except ImportError:
    app_urluth = None
else:
    app.register_blueprint(app_urluth, url_prefix="/urluth")


def generate_main_page(app_expressionotron, app_urluth):

    html_strings = ["Il n'y a pas grand-chose ici. Vous pouvez juste :<br/>", ]
    urls = []

    if app_expressionotron is not None:
        html_strings.append(
            " - <a href=\"%s\">cliquez ici pour aller &agrave; l'expressionotron</a><br/>")
        urls.append(url_for("app_expressionotron.expressionotronGet"))

    if app_urluth is not None:
        html_strings.append(
            " - <a href=\"%s\">cliquez ici pour consulter urluth</a><br/>")
        urls.append(url_for("app_urluth.urluthGet"))

    if app_expressionotron is None and app_urluth is None:
        html_strings.append(
            " - ne rien faire du tout !!")

    return "".join(html_strings) % tuple(urls)


@app.route('/')
def mainPage():
    return generate_main_page(app_expressionotron, app_urluth)


if __name__ == "__main__":
    app.run(debug=False)
