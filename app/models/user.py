# coding: utf-8 
from app import db


class User(db.Model):
    '''
    用户表
    '''
    __tablename__ = "flasky_user"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(50), nullable = False)
    phone = db.Column(db.String(20), nullable = False)

    def __str__(self):
        return "User: {}".format(self.name) 
    


class Role(db.Model):
    __tablename__ = "flasky_role"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    description = db.Column(db.String(250), nullable=True)
    
    def __str__(self):
        return "Role: {}".format(self.name) 


class UserAndRole(db.Model):
   
    __tablename__ = "flasky_user_and_role"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user_id = db.Column(db.Integer, nullable = False)
    role_id = db.Column(db.Integer, nullable = False)

    def __str__(self):
        return "UserAndRole: {}".format(self.id) 

    
class Group(db.Model):
    __tablename__ = "flasky_group"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String(30), nullable = False)

    def __str__(self):
        return "Group: {}".format(self.name) 
    
class GroupAndUser(db.Model):
   
    __tablename__ = "flasky_group_and_user"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    group_id = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, nullable = False)

    def __str__(self):
        return "GroupAndUser: {}".format(self.id) 

class GroupAndRole(db.Model):
    __tablename__ = "flasky_group_and_role"
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    group_id = db.Column(db.Integer, nullable = False)
    role_id = db.Column(db.Integer, nullable = False)

    def __str__(self):
        return "GroupAndRole: {}".format(self.id) 