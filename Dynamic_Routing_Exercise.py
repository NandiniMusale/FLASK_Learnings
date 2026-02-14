#this is a simple Exercide on dynamic Routing

from flask import Flask

app=Flask(__name__)

@app.route('/website/<name>')
def dynamic_Route(name):
    if name[-1]=="y":
        new_name=name[:len(name)-1]+"ifsy"
    else:
        new_name=name+"y"
    return f"Dynamic Routing {new_name}"

if __name__=="__main__":
    app.run(debug=True)
