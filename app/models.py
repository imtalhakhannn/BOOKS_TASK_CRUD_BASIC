from flask_sqlalchemy import SQLAlchemy
from app import db

class Author(db.Model):
    __tablename__ = 'authors'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(255),nullable=False)
    contact=db.Column(db.String(50))
    password=db.Column(db.String(200),nullable=False)
    
    books=db.relationship('Book',backref='author',lazy=True)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(100))  # New column added here
    created_by_id=db.Column(db.String(100))
    author_id=db.Column(db.Integer,db.ForeignKey('authors.id'),nullable=False)
    def to_dict(self):
        return {
            'Id': self.Id,
            'Title': self.Title,
            'Author': self.Author_Name,
            'Year': self.Year,
            'Genre':self.Genre
        }
        
        
class Publisher(db.Model):
    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
