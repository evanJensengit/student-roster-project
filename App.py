from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("Index.html")

# @app.route("/test")
# def test():
#     return render_template("new.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr =user))
    else:
        return render_template("Login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr} </h1>"
    
if __name__ == "__main__":
     app.run(debug =True)