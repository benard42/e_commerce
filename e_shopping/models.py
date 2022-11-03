from e_shopping import db
from datetime import datetime
import hashlib
from flask_login import UserMixin

class ExtraMixin(object):
    id = db.Column(db.Integer,primary_key =True )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class E_shopping(db.Model,ExtraMixin):
    __tablename__ = 'shopping'
    product_name = db.Column(db.String(100),nullable=False)
    product_type = db.Column(db.String(100),nullable=False)
    Product_quality = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Integer,nullable=False)
    Total = db.Column(db.Integer,nullable= False)
    
    @classmethod
    def get_all(cls):
        return cls.query.all()

class User(UserMixin, db.Model, ExtraMixin):
    __tablename__ = 'users'
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password,hashed_password):
        return User.hash_password(password) == hashed_password

    @classmethod
    def get_user_email(cls,email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_user_username(cls,username):
        return cls.query.filter_by(username=username).first()

class Post_product(db.Model, ExtraMixin):
    __tablename__ = 'products'
    action_on_product = db.Column(db.String(100),nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)

    def delete_instance(self, using_transaction = True, keep_parents= False):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_action(cls):
        return cls.query.all()

    @classmethod
    def get_action_by_id(cls,user_id):
        return cls.query.filter_by(created_by=user_id).all()

    @classmethod
    def get_by_id(cls,action_id):
        return cls.query.filter_by(id=action_id).first()