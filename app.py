from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "<h1>Hello</h1>"
@app.route("/home")

def home():
    return "<h1> welcome home </h1>"

@app.route("/dynamic/<user_input>")
def dynamic(user_input):
    #user_input = None
    return f"<h1> The user entered : {user_input} </h1>"


app.run()
