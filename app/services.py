from flask_sqlalchemy import SQLAlchemy
from app import db
from app.models import Book
import logging

def books_insertion(title, author, year):
    try:
        book = Book(Title=title, Author=author, Year=year)
        db.session.add(book)
        db.session.commit()
        logging.info(f"Book inserted: {title} by {author}")
        print("Database connection successful")
        return book.Id
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error inserting book: {str(e)}")
        raise

def receive_all_books():
    try:
        books = [book.to_dict() for book in Book.query.all()]
        logging.info("Retrieved all books")
        print("Database connection successful")
        return books
    except Exception as e:
        logging.error(f"Error retrieving books: {str(e)}")
        raise

def receive_book_by_id(b_id):
    try:
        book = Book.query.get(b_id)
        logging.info(f"Retrieved book with ID {b_id}")
        print("Database connection successful")
        return book.to_dict() if book else None
    except Exception as e:
        logging.error(f"Error retrieving book ID {b_id}: {str(e)}")
        raise

def book_update(b_id, title, author, year):
    try:
        book = Book.query.get(b_id)
        if book:
            book.Title = title
            book.Author = author
            book.Year = year
            db.session.commit()
            logging.info(f"Updated book with ID {b_id}")
        print("Database connection successful")
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error updating book ID {b_id}: {str(e)}")
        raise

def book_deletion(b_id):
    try:
        book = Book.query.get(b_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            logging.info(f"Deleted book with ID {b_id}")
        print("Database connection successful")
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error deleting book ID {b_id}: {str(e)}")
        raise