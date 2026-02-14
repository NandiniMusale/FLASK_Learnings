#this is the basic understanding of the Falsk


from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
   return "Hello World Welcome to Falsk!!!!"

@app.route("/information")
def info():
   return "Hello World We"

if __name__=="__main__":
    app.run(debug=True)
    