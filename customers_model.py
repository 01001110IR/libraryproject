from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from book_model import *

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'state': self.state,
            'country': self.country
        }
        
    def update_customer_id(customer_id):
        customer = customer.query.get(customer_id)
        if customer is None:
         return jsonify({'message': 'customer not found'}), 404

        customer.id = 1
        db.session.commit()
        return jsonify({'message': 'customer updated successfully'})
