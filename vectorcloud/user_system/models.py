from vectorcloud import db, login_manager
from flask_login import UserMixin


# Models-----------------------------------------------------------------------
# -----------------------------------------------------------------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(120), nullable=False)

    password = db.Column(db.String(60), nullable=False)


db.create_all()
db.session.commit()
