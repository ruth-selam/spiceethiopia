from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ruth():
    return render_template("loading.html")
if __name__ == "__main__":
    app.run()