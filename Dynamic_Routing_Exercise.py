#this is a simple Exercide on dynamic Routing
#app.add_url_rule('/','hello',view_func=hello_world) this function can be used instead of the rout decorator
from flask import Flask

app=Flask(__name__)

@app.route('/website/<name>')
def dynamic_Route(name):
    if name[-1]=="y":
        new_name=name[:len(name)-1]+"ifsy"
    else:
        new_name=name+"y"
    return f"Dynamic Routing {new_name}"

def hello_world():
    return "hello world"
app.add_url_rule('/','hello',view_func=hello_world)

if __name__=="__main__":
    app.run(debug=True)
