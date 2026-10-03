from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/tarefas")
def tarefas():
    return render_template("tarefas.html")

if __name__ == "__main__":
    app.run(debug=True)
