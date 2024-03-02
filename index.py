from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ethiopia():
    return render_template("loading.html")
@app.route("/baltina")
def baltina():
    return render_template("baltina.html")
if __name__ == "__main__":
    app.run()