from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_BINDS'] = {'two':'sqlite:///customers.db'}

db = SQLAlchemy

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    loan_type = db.Column(db.Integer, nullable=False)
    
class Customer(db.Model):
    __bind_key__= 'two'  
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))    

if __name__=='__main__':
      app.run(debug=True)



