from src import app, db, User
from flask import request, jsonify

@app.route("/")
def index():
    return "Hello world !"


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validate if the required fields are present
    if not username or not email or not password:
        return jsonify({'error': 'Missing fields'}), 400

    # Check if the username or email already exists in the database
    if db.users.find_one({'$or': [{'username': username}, {'email': email}]}):
        return jsonify({'error': 'Username or email already exists'}), 409

    # Create the User object
    user = User.from_dict(data)

    # Insert the user into the 'users' collection
    db.users.insert_one(user.to_dict())

    return jsonify({'message': 'User created successfully'}), 201



