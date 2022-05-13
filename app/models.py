import datetime
from flask_login import UserMixin
from . import db, login_manager
from werkzeug.security import check_password_hash,generate_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
class User(UserMixin, db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    pass_code=db.Column(db.String(255))
    # works = db.relationship('Work', backref='user', lazy='dynamic')
    breaks = db.relationship('Break', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_code = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_code,password)

    def __repr__(self):
        return f'User {self.username} '


# class Work(db.Model):
#     __tablename__='works'

#     id=db.Column(db.Integer,primary_key=True)
    
#     user_id=db.Column(db.Integer, db.ForeignKey('users.id'))

#     def save_work(self):
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_work(cls,categoryw):
#         works=Work.query.filter_by(categoryw=categoryw).all()
#         return works

        
    
#     def __repr__(self):
#         return f' {self.categoryw} Work '

class Break(db.Model):
    __tablename__='breaks'

    id=db.Column(db.Integer,primary_key=True)
    work_time=db.Column(db.Integer)
    break_time=db.Column(db.Integer)
    categoryb=db.Column(db.String)
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