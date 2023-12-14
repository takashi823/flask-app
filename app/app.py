from flask import Flask, render_template, redirect, request

from .models.database import init_db, db
from .models.post import Post


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    init_db(app)

    @app.route("/", methods=["GET"])
    def index():
        posts = Post.query.all()
        print(posts)
        return render_template("index.html", posts=posts)

    @app.route("/post", methods=["GET", "POST"])
    def add_task():
        if request.method == "POST":
            postInfo = Post(
                title=request.form["title"],
                content=request.form["content"],
            )
            print(postInfo)
            db.session.add(postInfo)
            db.session.commit()
            return redirect("/")
        else:
            return render_template("post.html")

    @app.route("/login")
    def login():
        return render_template("login.html")


    @app.route("/signup")
    def signup():
        return render_template("signup.html")


    @app.route("/postlist")
    def postList():
        return render_template("postList.html")

    return app

app = create_app()

if __name__ == "__main__":
    app.run()
