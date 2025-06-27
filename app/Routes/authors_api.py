from flask import Blueprint, request, jsonify
from app.models import Author, db

authors_api = Blueprint('authors_api', __name__)  

# Create Author
@authors_api.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    author = Author(
        name=data.get('name'),
        email=data.get('email'),
        contact=data.get('contact'),
        password=data.get('password')
    )
    db.session.add(author)
    db.session.commit()
    return jsonify({"message": "Author created", "id": author.id}), 201

# Get All Authors
@authors_api.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    author_list = [] 

    for a in authors:
        author_list.append({  
            "id": a.id,
            "name": a.name,
            "email": a.email,
            "contact": a.contact
        })

    return jsonify(author_list)  
# Update Author
@authors_api.route('/authors/<int:id>', methods=['PUT'])
def update_author(id):
    data = request.get_json()
    author = Author.query.get_or_404(id)
    author.name = data.get('name')
    author.email = data.get('email')
    author.contact = data.get('contact')
    author.password = data.get('password')
    db.session.commit()
    return jsonify({"message": "Author updated"})

# Delete Author
@authors_api.route('/authors/<int:id>', methods=['DELETE'])
def delete_author(id):
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()
    return jsonify({"message": "Author deleted"})
