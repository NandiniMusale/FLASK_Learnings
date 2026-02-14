#this 

from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
#jinja template technique for just for variables we can use {{variable}} this sytanx for just variable
def index():
    variable="nandini"
    return render_template('basic.html',name=variable)
#its not only variables we can also pass loops also 
@app.route("/home1")
def index1():
    l=["nandini","Btech","TCS"]
    return render_template('basic.html',list_name=l)

if __name__=="__main__":
    app.run()
