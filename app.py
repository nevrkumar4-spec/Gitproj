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

@app.route("/query/<json_user_input>")
def query(json_user_input):
    if ( int(json_user_input) % 2 == 0):
        return f" The request variable is even "
    else:
        return f"The request variable is odd"

@app.route("/addition/<inputA>/<inputB>")    
def addition(inputA,inputB):
    return f"The sum of given input numbers are :{int(inputA)+int(inputB)}"
app.run()
