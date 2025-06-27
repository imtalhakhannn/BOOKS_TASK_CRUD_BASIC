from flask import Blueprint, jsonify, request
from app.services import books_insertion, receive_all_books, receive_book_by_id, book_update, book_deletion
import logging

blueprint = Blueprint('blueprint', __name__)


from app.models import Book, Author
from app import db


@blueprint.route('/')
def home():
    return jsonify({"message": "App is working!"})

@blueprint.route('/create-test', methods=['GET'])
def create_test():
    author = Author(name="Tooba", email="tooba987@email.com", contact="03001234567", password="secret")
    db.session.add(author)
    db.session.commit()

    book = Book(title="Internship", year=2024, genre="Learning", author_id=author.id)
    db.session.add(book)
    db.session.commit()

    return {"message": "Author and Book added successfully"}

@blueprint.route('/books', methods=['GET'])
def get_books():
    try:
        books = receive_all_books()
        return jsonify(books)
    except Exception as e:
        logging.error(f"Error in get_books: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@blueprint.route('/books/<int:b_id>', methods=['GET'])
def get_book_by_id(b_id):
    try:
        book = receive_book_by_id(b_id)
        if book:
            return jsonify(book)
        return jsonify({"error": "Book not found"}), 404
    except Exception as e:
        logging.error(f"Error in get_book_by_id: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@blueprint.route('/books', methods=['POST'])
def books_addition():
    try:
        data = request.get_json()
        if not all(key in data for key in ['Title', 'Author', 'Year']):
            return jsonify({"error": "Missing required fields"}), 400
        id = books_insertion(data['Title'], data['Author'], data['Year'])
        return jsonify({"message": f"Book added with id {id}"}), 201
    except Exception as e:
        logging.error(f"Error in books_addition: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@blueprint.route('/books/<int:b_id>', methods=['PUT'])
def change_book(b_id):
    try:
        data = request.get_json()
        if not all(key in data for key in ['Title', 'Author', 'Year']):
            return jsonify({"error": "Missing required fields"}), 400
        book_update(b_id, data['Title'], data['Author'], data['Year'])
        return jsonify({"message": f"Book with id {b_id} updated"})
    except Exception as e:
        logging.error(f"Error in change_book: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@blueprint.route('/books/<int:b_id>', methods=['DELETE'])
def delete_book(b_id):
    try:
        book_deletion(b_id)
        return jsonify({"message": f"Book with id {b_id} deleted"})
    except Exception as e:
        logging.error(f"Error in delete_book: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500