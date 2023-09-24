from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from book_model import Book,db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)




# Routes for managing books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = [{'id': book.id, 'name': book.name, 'author': book.author, 'year_published': book.year_published, 'loan_type': book.loan_type} for book in books]
    return jsonify(book_list)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify({'id': book.id, 'name': book.name, 'author': book.author, 'year_published': book.year_published, 'loan_type': book.loan_type})

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Data is required'}), 400

    book = Book(**data)
    db.session.add(book)
    db.session.commit()

    return jsonify({'message': 'Book added successfully', 'id': book.id}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'message': 'Data is required'}), 400

    if 'name' in data:
        book.name = data['name']
    if 'author' in data:
        book.author = data['author']
    if 'year_published' in data:
        book.year_published = data['year_published']
    if 'loan_type' in data:
        book.loan_type = data['loan_type']

    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})



@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
