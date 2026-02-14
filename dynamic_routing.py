#this Explains the dynamic Routing with Examples

## often we will want to URL Route Extentions to be dynamic based on the situation
## for this we will use the Du=ynamic Routing 

from flask import Flask

app=Flask(__name__)

@app.route('/website/<name>')
def dynamic_Route(name):
    return f"Dynamic Routing {name}"

if __name__=="__main__":
    app.run(debug=True)
