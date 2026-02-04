from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def index():
    search_query = None
    if request.method == "POST":
        search_query = request.form.get("search")

    return render_template(
        "index.html",
        logged_in=session.get("logged_in", False),
        search_query=search_query
    )

@app.route("/login")
def login():
    session["logged_in"] = True
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
