# loans_model.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    loan_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    return_date = db.Column(db.DateTime, nullable=True)

    def json(self):
        return {
            'id': self.id,
            'cust_id': self.cust_id,
            'book_id': self.book_id,
            'loan_date': self.loan_date.strftime('%Y-%m-%d %H:%M:%S'),
            'return_date': self.return_date.strftime('%Y-%m-%d %H:%M:%S') if self.return_date else None
        }

    @classmethod
    def find_by_id(cls, loan_id):
        return cls.query.get(loan_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
