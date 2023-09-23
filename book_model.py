from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from customers_model import *

db = SQLAlchemy()

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    loan_type = db.Column(db.Integer, nullable=False)

    def __init__(self, name, author, year_published, loan_type):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.loan_type = loan_type
        
    def update_book_id(book_id):
        book = Book.query.get(book_id)
        if book is None:
         return jsonify({'message': 'Book not found'}), 404

        book.id = 1
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'})


