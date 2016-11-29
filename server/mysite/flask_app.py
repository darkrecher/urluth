from flask import Flask, url_for
from expressionotron.appexpr import app_expressionotron
from urluth.appurluth import app_urluth

app = Flask(__name__)
app.secret_key = 'This is really unique and secret, ou pas'

app.register_blueprint(app_expressionotron, url_prefix="/expressionotron")
app.register_blueprint(app_urluth, url_prefix="/urluth")


@app.route('/')
def mainPage():
    return """
        Il n'y a pas grand-chose ici. Vous pouvez juste<br/>
        <a href="%s">cliquez ici pour aller &agrave; l'expressionotron</a><br/>
        <a href="%s">cliquez ici pour consulter urluth</a><br/>
    """ % (
        url_for("app_expressionotron.expressionotronGet"),
        url_for("app_urluth.urluthGet"),
    )


if __name__ == "__main__":
    app.run(debug=False)
