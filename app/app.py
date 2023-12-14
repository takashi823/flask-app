from flask import Flask, render_template

# importの追加
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# DBの接続設定 
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8".format(
    **{"user": "test", "password": "test", "host": "db", "db_name": "test"}
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# DBインスタンス作成
db = SQLAlchemy(app)

# migrateインスタンスを定義
migrate = Migrate(app, db)

# モデルの作成
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


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


if __name__ == "__main__":
    app.run()
