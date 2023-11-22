from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/post")
def post():
	return render_template("post.html")

@app.route("/postlist")
def postList():
	return render_template("postList.html")


if __name__ == '__main__':
	app.run()