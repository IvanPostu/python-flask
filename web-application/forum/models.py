from flask_login import UserMixin

from forum import db, login_manager


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)

    def __init__(self, text, tags):
        self.text = text
        self.tags = [
            Tag(text=tag.strip()) for tag in tags.split(',')
        ]


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey(
        'message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
