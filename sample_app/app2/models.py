print('app2 models.py')
from sqlalchemy import Integer, String
from sample_app.sample_app import db
from flask_sqlalchemy import SQLAlchemy

# 'from sample_app.sample_app import db' imports an empty SQLAlchemy db object


# db.Model is Flask-SQLAlchemy's base model and needs to be passed
# into every class
class Table3(db.Model):
    __tablename__ = 'table3'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    email = db.Column(String)

    def __repr__(self):
        return f'<id {self.id}'

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Table4(db.Model):
    __tablename__ = 'table4'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    email = db.Column(String)

    def __repr__(self):
        return f'<id {self.id}'

    def __init__(self, name, email):
        self.name = name
        self.email = email       
