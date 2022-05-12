import datetime
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from . import db
from werkzeug.security import check_password_hash,generate_password_hash
class User(UserMixin, db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    password=db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return f'User {self.username} '


class Work(db.Model):
    __tablename__='work'

    id=db.Column(db.Integer,primary_key=True)
    # categoryw=db.Column(db.String)
    work_time=db.Column(db.Integer)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_work(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_work(cls,categoryw):
        works=Work.query.filter_by(categoryw=categoryw).all()
        return works

        
    
    def __repr__(self):
        return f' {self.categoryw} Work '

class Break(db.Model):
    __tablename__='break'

    id=db.Column(db.Integer,primary_key=True)
    categoryb=db.Column(db.String)
    break_time=db.Column(db.Integer)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_break(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_break(cls,categoryb):
        breaks=Break.query.filter_by(categoryb=categoryb).all()
        return breaks

    
    def __repr__(self):
        return f'{self.categoryb} break '