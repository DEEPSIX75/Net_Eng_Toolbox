#This is the file that will be our FLASK_APP and will kick off the instantiation of the application.
from flask import Flask

app = Flask(__name__)

@app.route("/")
def obligatory_hello():
    return "<h1>World, Hello!</h1>"