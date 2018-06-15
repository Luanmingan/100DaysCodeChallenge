from flask import Flask, render_template
from data import favorite_beer


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html",
                           favorite_beer=favorite_beer)


if __name__ == '__main__':
    app.run()
