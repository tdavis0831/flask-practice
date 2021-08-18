from flask import Flask   #this line and next line are needed for flask
app = Flask(__name__)      #nameneeded to know what module to scan

@app.route("/") #ornimates gives the route in the url each page needs one 
def index():
    return "<h1>Hello Puppy!<h1>"

@app.route("/information")
def info():
    return "<h1> puppies are cute </h2>"


@app.route("/puppy/<name>")      #for dynamic variables 
def puppy(name):
    return f"<h1> this is a page for {name} </h1>" #this will take the name from the argument and pass it through to the fstring. this will display "this page is for WHATEVER NAME WAS PASSED THROUGH THE FUNCTION"


if __name__=="__main__":   #excute code if youre running from sript directly
    app.run()