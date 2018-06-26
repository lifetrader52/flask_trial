from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<span style='color:red;'>Hello World!</span>"
    

print("ini yap")