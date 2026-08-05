from flask import Flask


## Wsgi Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to this best flask course. This should be an amazing course"

@app.route("/index")
def index():
    return "welcome to this index page"

if __name__=="__main__":
    app.run(debug=True)