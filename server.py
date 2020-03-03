from flask import flask, app

app = Flask(__name__, static_url_path='')

@app.route("/")
def loadHomePage():
    return send_file("index.html")

@app.route("/<string:pageName>")
def loadPage(pageName):
    return 404

if __name__ == "__main__":
    app.run()