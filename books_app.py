from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from book_model import Book,db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db,sqlite:///customers.db'
db.init_app(app)





# Routes for managing books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = [{'id': books.id, 'name': books.name, 'author': books.author, 'year_published': books.year_published, 'loan_type': books.loan_type} for books in books]
    return jsonify(book_list)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    books = Book.query.get(book_id)
    if not books:
        return jsonify({'message': 'Book not found'}), 404
    return jsonify({'id': books.id, 'name': books.name, 'author': books.author, 'year_published': books.year_published, 'loan_type': books.loan_type})

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Data is required'}), 400

    books = Book(**data)
    db.session.add(books)
    db.session.commit()

    return jsonify({'message': 'Book added successfully', 'id': books.id}), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    books = Book.query.get(book_id)
    if not books:
        return jsonify({'message': 'Book not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'message': 'Data is required'}), 400

    if 'name' in data:
        books.name = data['name']
    if 'author' in data:
        books.author = data['author']
    if 'year_published' in data:
        books.year_published = data['year_published']
    if 'loan_type' in data:
        books.loan_type = data['loan_type']

    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})



@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    books = Book.query.get(book_id)
    if not books:
        return jsonify({'message': 'Book not found'}), 404

    db.session.delete(books)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
