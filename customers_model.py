from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()

# Define the Customer model
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)  # Include 'age' attribute
    state = db.Column(db.String(50), nullable=False)
    cuntry = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, phone_number, age, state, cuntry):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.age = age  # Initialize 'age'
        self.state = state
        self.cuntry = cuntry
        
        
    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'state': self.state,
            'cuntry': self.cuntry,
            'age' : self.age
        }
    
