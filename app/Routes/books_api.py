from flask import Blueprint, request, jsonify
from app.models import Book, Author, db

books_api = Blueprint('books_api', __name__) 

# Create Book
@books_api.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    book = Book(
        title=data.get('title'),
        year=data.get('year'),
        genre=data.get('genre'),
        author_id=data.get('author_id')
    )
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book created", "id": book.id}), 201

# Get All Books
@books_api.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = []

    for b in books:
        book_list.append({
            "id": b.id,
            "title": b.title,
            "year": b.year,
            "genre": b.genre,
            "author_id": b.author_id
        })

    return jsonify(book_list)

# Get Books by Author ID
@books_api.route('/books/author/<int:author_id>', methods=['GET'])
def get_books_by_author(author_id):
    author = Author.query.get_or_404(author_id)
    books = Book.query.filter_by(author_id=author_id).all()
    book_list = []

    for b in books:
        book_list.append({
            "id": b.id,
            "title": b.title,
            "year": b.year,
            "genre": b.genre
        })

    return jsonify({
        "author": author.name,
        "books": book_list
    })

# Update Book
@books_api.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    book.title = data.get('title')
    book.year = data.get('year')
    book.genre = data.get('genre')
    book.author_id = data.get('author_id')
    db.session.commit()
    return jsonify({"message": "Book updated"})

# Delete Book
@books_api.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"})
