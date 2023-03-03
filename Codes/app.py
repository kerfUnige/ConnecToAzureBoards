from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! je modifie sa pour un test. Je l'ai fait depuis ma branche</p>"
