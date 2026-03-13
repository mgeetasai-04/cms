from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from azure.storage.blob import BlobServiceClient
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# -------------------------------
# Azure Blob Storage Setup
# -------------------------------

blob_service_client = BlobServiceClient.from_connection_string(
    app.config["AZURE_STORAGE_CONNECTION_STRING"]
)

container_client = blob_service_client.get_container_client(
    app.config["CONTAINER_NAME"]
)

# -------------------------------
# Database Models
# -------------------------------

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(200), nullable=False)


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    content = db.Column(db.Text, nullable=False)

    image_url = db.Column(db.String(500))


# Create tables
with app.app_context():
    db.create_all()

# -------------------------------
# Home Page
# -------------------------------

@app.route("/")
def index():

    posts = Post.query.all()

    return render_template("index.html", posts=posts)


# -------------------------------
# Register
# -------------------------------

@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = generate_password_hash(request.form["password"])

        user = User(username=username, email=email, password=password)

        db.session.add(user)

        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")


# -------------------------------
# Login
# -------------------------------

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):

            session["user"] = user.username

            return redirect(url_for("index"))

        else:

            return "Invalid username or password"

    return render_template("login.html")


# -------------------------------
# Logout
# -------------------------------

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("login"))


# -------------------------------
# Create Post
# -------------------------------

@app.route("/create_post", methods=["POST"])
def create_post():

    if "user" not in session:

        return redirect(url_for("login"))

    title = request.form["title"]

    content = request.form["content"]

    image = request.files["image"]

    filename = str(uuid.uuid4()) + image.filename

    blob_client = container_client.get_blob_client(filename)

    blob_client.upload_blob(image)

    image_url = blob_client.url

    post = Post(
        title=title,
        content=content,
        image_url=image_url
    )

    db.session.add(post)

    db.session.commit()

    return redirect(url_for("index"))


# -------------------------------
# Run App
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)