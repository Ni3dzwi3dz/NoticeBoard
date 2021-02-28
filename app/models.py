from app import  app, db, login
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32),index=True, unique= True)
    city = db.Column(db.String(32))
    password_hash= db.Column(db.String(64))
    email= db.Column(db.String(64), index=True, unique=True)
    about= db.Column(db.String(200))

    def __repr__(self):
        return f'{username} of {city}'

    def set_pass(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_pass(self,password):
        return check_password_hash(self.password_hash,password)

    def avatar(self,size):
        idstring= md5(self.email.lower().encode('UTF-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{idstring}?d=wavatar&s={size}'




@login.user_loader
def user_load(id):
    return User.query.get(int(id))
    
