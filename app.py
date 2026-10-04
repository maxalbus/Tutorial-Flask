from flask import Flask, abort, flash, redirect, render_template, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from sqlalchemy import or_
from werkzeug.security import check_password_hash, generate_password_hash

import models
from extensions import db


app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-change-before-deployment"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        return db.session.get(models.User, int(user_id))
    except (TypeError, ValueError):
        return None


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if not username or not password:
        flash("Username and password are required.", "error")
        return "Username and password are required.", 400

    if models.User.query.filter_by(username=username).first() is not None:
        flash("That username is already registered.", "error")
        return "That username is already registered.", 409

    user = models.User(
        username=username,
        password=generate_password_hash(password),
        role="member",
    )
    db.session.add(user)
    db.session.commit()

    flash("Registration successful. Please log in.", "success")
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    user = models.User.query.filter_by(username=username).first() if username else None

    if user is None or not check_password_hash(user.password, password):
        flash("Invalid username or password.", "error")
        return "Invalid username or password.", 401

    login_user(user)
    flash("Login successful.", "success")

    if user.role == "admin":
        return redirect(url_for("admin"))
    return redirect(url_for("dashboard"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    tasks = (
        models.Task.query.filter(
            or_(
                models.Task.created_by == current_user.id,
                models.Task.shared_with == current_user.id,
            )
        )
        .distinct()
        .order_by(models.Task.id.asc())
        .all()
    )
    return render_template("dashboard.html", tasks=tasks)


@app.route("/admin")
@login_required
def admin():
    if current_user.role != "admin":
        abort(403)

    tasks = models.Task.query.order_by(models.Task.id.asc()).all()
    return render_template("admin.html", tasks=tasks)


@app.route("/add_task", methods=["GET", "POST"])
@login_required
def add_task():
    allowed_statuses = ["pending", "in progress", "completed"]
    available_users = (
        models.User.query.filter(models.User.id != current_user.id)
        .order_by(models.User.username.asc())
        .all()
    )

    if request.method == "GET":
        return render_template(
            "add_task.html",
            users=available_users,
            statuses=allowed_statuses,
            form_data={},
        )

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    status = request.form.get("status", "")
    raw_shared_with = request.form.get("shared_with", "").strip()
    errors = []
    shared_with_id = None

    if not title:
        errors.append("O título é obrigatório.")
    elif len(title) > 200:
        errors.append("O título deve ter no máximo 200 caracteres.")

    if status not in allowed_statuses:
        errors.append("Selecione um status válido.")

    if raw_shared_with:
        try:
            shared_with_id = int(raw_shared_with)
        except ValueError:
            errors.append("O usuário selecionado para compartilhamento não existe.")
        else:
            if shared_with_id == current_user.id:
                errors.append("Você não pode compartilhar uma tarefa consigo mesmo.")
            elif db.session.get(models.User, shared_with_id) is None:
                errors.append("O usuário selecionado para compartilhamento não existe.")

    if errors:
        for error in errors:
            flash(error, "error")
        return (
            render_template(
                "add_task.html",
                users=available_users,
                statuses=allowed_statuses,
                form_data=request.form,
            ),
            400,
        )

    task = models.Task(
        title=title,
        description=description,
        status=status,
        created_by=current_user.id,
        shared_with=shared_with_id,
    )
    db.session.add(task)
    db.session.commit()

    flash("Tarefa criada com sucesso.", "success")
    return redirect(url_for("dashboard"))


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    task = db.session.get(models.Task, task_id)
    if task is None:
        abort(404)

    can_edit = current_user.role == "admin" or (
        current_user.role == "member" and task.created_by == current_user.id
    )
    if not can_edit:
        abort(403)

    allowed_statuses = ["pending", "in progress", "completed"]
    available_users = (
        models.User.query.filter(models.User.id != current_user.id)
        .order_by(models.User.username.asc())
        .all()
    )
    form_data = {
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "shared_with": str(task.shared_with or ""),
    }

    if request.method == "GET":
        return render_template(
            "edit_task.html",
            task=task,
            users=available_users,
            statuses=allowed_statuses,
            form_data=form_data,
        )

    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    status = request.form.get("status", "")
    raw_shared_with = request.form.get("shared_with", "").strip()
    errors = []
    shared_with_id = None

    if not title:
        errors.append("O título é obrigatório.")
    elif len(title) > 200:
        errors.append("O título deve ter no máximo 200 caracteres.")

    if status not in allowed_statuses:
        errors.append("Selecione um status válido.")

    if raw_shared_with:
        try:
            shared_with_id = int(raw_shared_with)
        except ValueError:
            errors.append("O usuário selecionado para compartilhamento não existe.")
        else:
            if shared_with_id == current_user.id and shared_with_id != task.shared_with:
                errors.append("Você não pode compartilhar uma tarefa consigo mesmo.")
            elif db.session.get(models.User, shared_with_id) is None:
                errors.append("O usuário selecionado para compartilhamento não existe.")

    if errors:
        for error in errors:
            flash(error, "error")
        return (
            render_template(
                "edit_task.html",
                task=task,
                users=available_users,
                statuses=allowed_statuses,
                form_data=request.form,
            ),
            400,
        )

    task.title = title
    task.description = description
    task.status = status
    task.shared_with = shared_with_id
    db.session.commit()

    flash("Tarefa atualizada com sucesso.", "success")
    return redirect(url_for("dashboard"))


@app.route("/delete_task/<int:task_id>", methods=["POST"])
@login_required
def delete_task(task_id):
    task = db.session.get(models.Task, task_id)
    if task is None:
        abort(404)

    can_delete = current_user.role == "admin" or (
        current_user.role == "member" and task.created_by == current_user.id
    )
    if not can_delete:
        abort(403)

    db.session.delete(task)
    db.session.commit()

    flash("Tarefa excluída com sucesso.", "success")
    return redirect(url_for("dashboard"))