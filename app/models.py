from app import db
'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    password = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True, unique=True)


    def is_authenticated(self):
        return True
    def is_active(selt):
        return True
    def is_anonymous(self):
        return False
    def get_auth_token(self):
        return unicode(hashlib.sha1(self.username +
        self.password).hexdigest())
    def get_id(self):
        return unicode(self.id)
    def __repr__(self):
        return '<User %r>' % (self.username)

'''		


