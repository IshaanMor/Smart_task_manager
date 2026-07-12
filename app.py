from flask import Flask, render_template
from flask_login import LoginManager
from config import Config
from models import db, User

# Create Flask App
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

# Initialize Login Manager
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# -------------------- Routes --------------------

# Home Page
@app.route("/")
def home():
    return render_template("base.html")


# Register Page
@app.route("/register")
def register():
    return render_template("register.html")


# Login Page
@app.route("/login")
def login():
    return render_template("login.html")


# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# Add Task Page
@app.route("/add-task")
def add_task():
    return render_template("add_task.html")


# Edit Task Page
@app.route("/edit-task")
def edit_task():
    return render_template("edit_task.html")


# -------------------- Run App --------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)