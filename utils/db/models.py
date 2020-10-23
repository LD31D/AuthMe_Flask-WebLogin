from flask_login import UserMixin

from utils.app import db, manager


class User(db.Model, UserMixin):
    __table__ = db.Model.metadata.tables['authme']

    def __repr__(self):
    	return self.username


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

