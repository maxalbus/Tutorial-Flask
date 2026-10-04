from flask_login import UserMixin

from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="member")

    created_tasks = db.relationship(
        "Task",
        foreign_keys="Task.created_by",
        back_populates="creator",
    )
    shared_tasks = db.relationship(
        "Task",
        foreign_keys="Task.shared_with",
        back_populates="recipient",
    )


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="pending")
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    shared_with = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    creator = db.relationship(
        "User",
        foreign_keys=[created_by],
        back_populates="created_tasks",
    )
    recipient = db.relationship(
        "User",
        foreign_keys=[shared_with],
        back_populates="shared_tasks",
    )