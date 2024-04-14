from flask import Flask, request, jsonify

app = Flask(__name__)

books = []

# Create
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book = {
        'id': len(books) + 1,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books.append(book)
    return jsonify(book), 201

# Read
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Update
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    for book in books:
        if book['id'] == book_id:
            book['book_name'] = data.get('book_name', book['book_name'])
            book['author'] = data.get('author', book['author'])
            book['publisher'] = data.get('publisher', book['publisher'])
            return jsonify(book), 200
    return 'Book not found', 404

# Delete
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for i, book in enumerate(books):
        if book['id'] == book_id:
            del books[i]
            return '', 204
    return 'Book not found', 404

if __name__ == '__main__':
    app.run(debug=True)
