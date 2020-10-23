from utils.app import db

class User (db.Model):
    __table__ = db.Model.metadata.tables['authme']

    def __repr__(self):
    	return self.username

