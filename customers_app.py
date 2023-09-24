from flask import Flask, jsonify, request
from book_model import Book

from customers_model import db, Customer  # Import db and Customer

app = Flask(__name__)

# Database URI Configuration with semicolons
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)  # Initialize SQLAlchemy with your app

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    customer_list = [customer.json() for customer in customers]
    return jsonify(customer_list)

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    return jsonify(customer.json())

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Data is required'}), 400

    customer = Customer(**data)
    db.session.add(customer)
    db.session.commit()

    return jsonify({'message': 'Customer added successfully', 'id': customer.id}), 201

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Data is required'}), 400

        new_customer = Customer(**data)
        new_customer.id = customer_id
        db.session.add(new_customer)
        db.session.commit()

        return jsonify({'message': 'Customer created successfully', 'id': customer_id}), 201

    data = request.get_json()
    if not data:
        return jsonify({'message': 'Data is required'}), 400

    if 'name' in data:
        customer.name = data['name']
    if 'email' in data:
        customer.email = data['email']
    if 'phone_number' in data:
        customer.phone_number = data['phone_number']
    if 'state' in data:
        customer.state = data['state']
    if 'country' in data:
        customer.country = data['country']

    db.session.commit()
    return jsonify({'message': 'Customer updated successfully'})

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404

    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted successfully'})

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = [{'id': book.id, 'name': book.name, 'author': book.author, 'year_published': book.year_published, 'loan_type': book.loan_type} for book in books]
    return jsonify(book_list)



if __name__ == '__main__':
    app.run(debug=True)
