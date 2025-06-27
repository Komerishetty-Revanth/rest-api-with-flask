Flask User Management REST API
This project provides a simple RESTful API for managing user data. It's built with Flask and uses an in-memory dictionary as its data store, making it a great starting point for understanding fundamental API development concepts.

Features
Create Users: Add new users with a unique ID.

Retrieve Users: Get a list of all users or a specific user by ID.

Update Users: Modify existing user details.

Delete Users: Remove users from the system.

JSON API: All requests and responses are handled in JSON format.

Technologies Used
Python 3.x

Flask (Web Framework)

Setup and Installation
Follow these steps to get the API running on your local machine.

Prerequisites
Python 3.6+ installed on your system.

pip (Python package installer)

1. Clone the Repository (or Save the File)
If you have the code as a single file, save it as app.py. If this were a repository, you would clone it:

# Assuming your code is in a file named app.py
# No cloning needed, just save the app.py file.

2. Create a Virtual Environment (Recommended)
It's good practice to use a virtual environment to manage dependencies.

python -m venv venv

3. Activate the Virtual Environment
On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

4. Install Dependencies
Install Flask using pip:

pip install Flask

How to Run the Application
Ensure your virtual environment is active.

Navigate to the directory where your app.py file is located.

Run the Flask application:

python app.py

You should see output similar to this:

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

The API will be accessible at http://127.0.0.1:5000. Keep this terminal window open as long as you want the server to run.

API Endpoints
The API interacts with user resources. All endpoints return JSON responses.

Base URL
http://127.0.0.1:5000

1. Get All Users
URL: /users

Method: GET

Description: Retrieves a list of all existing users.

Response:

[
    {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
    {"id": 2, "name": "Bob Johnson", "email": "bob@example.com"}
]

2. Get a Single User by ID
URL: /users/<int:user_id> (e.g., /users/1)

Method: GET

Description: Retrieves details of a specific user.

Response (Success):

{"id": 1, "name": "Alice Smith", "email": "alice@example.com"}

Response (Not Found - Status 404):

{"error": "User not found"}

3. Create a New User
URL: /users

Method: POST

Description: Creates a new user with a unique ID.

Request Body (JSON):

{
    "name": "Charlie Brown",
    "email": "charlie@example.com"
}

Response (Success - Status 201 Created):

{
    "id": 3,
    "name": "Charlie Brown",
    "email": "charlie@example.com"
}

Response (Bad Request - Status 400):

{"error": "Missing 'name' or 'email' in request body"}

4. Update an Existing User
URL: /users/<int:user_id> (e.g., /users/1)

Method: PUT

Description: Updates the name and/or email for an existing user.

Request Body (JSON):

{
    "name": "Alicia Smith",
    "email": "alicia.s@example.com"
}

(You can provide one or both fields.)

Response (Success):

{
    "id": 1,
    "name": "Alicia Smith",
    "email": "alicia.s@example.com"
}

Response (Not Found - Status 404):

{"error": "User not found"}

Response (Bad Request - Status 400):

{"error": "No data provided for update"}

5. Delete a User
URL: /users/<int:user_id> (e.g., /users/1)

Method: DELETE

Description: Deletes a user from the data store.

Response (Success - Status 200):

{"message": "User with ID 1 deleted successfully"}

Response (Not Found - Status 404):

{"error": "User not found"}

Testing the API
You can test the API using tools like Postman (graphical interface) or curl (command-line tool). Refer to the Mini Guide: Running and Testing the API for detailed instructions and curl examples.

Limitations
In-Memory Data: All user data is stored in memory and will be lost when the Flask application is stopped. For persistent storage, you would integrate a database (e.g., SQLite, PostgreSQL, MongoDB).

No Authentication/Authorization: This API does not implement any user authentication or authorization. All endpoints are publicly accessible.

Basic Error Handling: Error handling is minimal.

No Input Sanitization: Input data is not sanitized, which could lead to security vulnerabilities in a production environment.

Future Enhancements
Integrate a persistent database (e.g., SQLAlchemy with SQLite).

Add user authentication and authorization (e.g., using Flask-Login or Flask-JWT-Extended).

Implement more robust input validation and error handling.

Add logging capabilities.

Deploy the application to a production server (e.g., using Gunicorn and Nginx).