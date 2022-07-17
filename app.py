from flask import Flask


app = Flask(__name__)



@app.route('/', methods=["Get", "Post"])
def index():
    return "Starting ML Project"


if __name__=="__main__":
    app.run(debug=True)