from flask import Flask, request, jsonify
app = Flask(__name__)
users = {
    1: {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob Johnson", "email": "bob@example.com"}
}
next_user_id = 3
@app.route('/users', methods=['GET'])
def get_users():
    """
    Retrieves all users from the in-memory data store.
    """
    return jsonify(list(users.values()))
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieves a single user by their ID.
    Args:
        user_id (int): The ID of the user to retrieve.
    Returns:
        JSON response with user data or an error message.
    """
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404
@app.route('/users', methods=['POST'])
def create_user():
    """
    Creates a new user based on the JSON data provided in the request body.
    Assigns a unique ID to the new user.
    Returns:
        JSON response with the created user data or an error message.
    """
    global next_user_id
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing 'name' or 'email' in request body"}), 400
    new_user = {
        "id": next_user_id,
        "name": data['name'],
        "email": data['email']
    }
    users[next_user_id] = new_user  
    next_user_id += 1              
    return jsonify(new_user), 201
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Updates an existing user's details by their ID.
    Args:
        user_id (int): The ID of the user to update.
    Returns:
        JSON response with the updated user data or an error message.
    """
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided for update"}), 400
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']
    return jsonify(user)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a user by their ID.
    Args:
        user_id (int): The ID of the user to delete.
    Returns:
        JSON response indicating success or an error message.
    """
    if user_id in users:
        del users[user_id]  
        return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404
if __name__ == '__main__':
    app.run(debug=True, port=5000)