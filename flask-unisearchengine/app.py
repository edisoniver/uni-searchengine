from flask import Flask, request, json, render_template

app = Flask(__name__)

@app.route("/")
def main():
    title = 'THIS IS A TITLE'
    return render_template("index.html", title = title)


app.run(host="0.0.0.0", port = 5000, debug = True)
g