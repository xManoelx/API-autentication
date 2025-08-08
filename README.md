# Flask Authentication API

A robust and secure RESTful API built with Flask that provides complete user authentication and management functionality. This API includes user registration, login, logout, and full CRUD operations with session-based authentication using Flask-Login.

## 🚀 Features

- **User Authentication**: Secure login and logout functionality
- **User Management**: Complete CRUD operations (Create, Read, Update, Delete)
- **Session Management**: Built-in session handling with Flask-Login
- **SQLite Database**: Lightweight database solution with SQLAlchemy ORM
- **RESTful Design**: Clean and intuitive API endpoints
- **Security**: Login required decorators for protected routes
- **Error Handling**: Comprehensive error responses with appropriate HTTP status codes

## 🛠️ Tech Stack

- **Framework**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login for session management
- **Language**: Python 3.x

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher installed
- pip (Python package installer)
- Basic knowledge of REST APIs

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/xManoelx/API-autentication.git
   cd API-autentication
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install flask flask-sqlalchemy flask-login
   ```

4. **Initialize the database**
   ```python
   python -c "from app import app, db; app.app_context().push(); db.create_all()"
   ```

## 🚦 Running the Application

1. **Start the development server**
   ```bash
   python app.py
   ```

2. **Access the API**
   - The API will be available at `http://localhost:5000`
   - Debug mode is enabled by default

## 📚 API Documentation

### Authentication Endpoints

#### POST /login
Authenticate a user and start a session.

**Request Body:**
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

**Response:**
- **200 OK**: Login successful
- **400 Bad Request**: Invalid credentials

#### GET /logout
Log out the current authenticated user (requires authentication).

**Response:**
- **200 OK**: Logout successful

### User Management Endpoints

#### POST /user
Create a new user account.

**Request Body:**
```json
{
    "username": "new_username",
    "password": "new_password"
}
```

**Response:**
- **201 Created**: User created successfully
- **400 Bad Request**: Invalid data

#### GET /user/{id}
Retrieve user information by ID (requires authentication).

**Parameters:**
- `id`: User ID (integer)

**Response:**
- **200 OK**: Returns user data
- **404 Not Found**: User not found

#### PUT /user/{id}
Update user information (requires authentication).

**Parameters:**
- `id`: User ID (integer)

**Request Body:**
```json
{
    "password": "new_password"
}
```

**Response:**
- **200 OK**: User updated successfully
- **404 Not Found**: User not found

#### DELETE /user/{id}
Delete a user account (requires authentication).

**Parameters:**
- `id`: User ID (integer)

**Response:**
- **200 OK**: User deleted successfully
- **403 Forbidden**: Cannot delete own account
- **404 Not Found**: User not found

### Utility Endpoints

#### GET /hello-world
Simple endpoint for testing API connectivity.

**Response:**
- **200 OK**: Returns "Hello, World!"

## 🏗️ Project Structure

```
API-autentication/
├── app.py                 # Main application file
├── database.py           # Database configuration
├── models/
│   └── user.py          # User model definition
├── instance/
│   └── database.db      # SQLite database file
└── utilities/
    └── requirements.txt # Project dependencies
```

## 🔒 Security Features

- **Session-based Authentication**: Uses Flask-Login for secure session management
- **Protected Routes**: Login required decorators prevent unauthorized access
- **User Isolation**: Users cannot delete their own accounts via API
- **Input Validation**: Server-side validation for user inputs

## 🧪 Testing the API

You can test the API using tools like:

- **curl**: Command-line HTTP client
- **Postman**: GUI for API testing
- **Insomnia**: Another popular API testing tool

### Example curl commands:

```bash
# Create a user
curl -X POST http://localhost:5000/user \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass"}'

# Login
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass"}' \
  -c cookies.txt

# Get user info (using saved cookies)
curl -X GET http://localhost:5000/user/1 \
  -b cookies.txt

# Logout
curl -X GET http://localhost:5000/logout \
  -b cookies.txt
```

## 📝 Configuration

### Environment Variables

- `SECRET_KEY`: Flask secret key for session management (currently hardcoded)
- `SQLALCHEMY_DATABASE_URI`: Database connection string (SQLite by default)

### Recommended for Production

1. **Use environment variables** for sensitive configuration
2. **Implement password hashing** (bcrypt, werkzeug.security)
3. **Add input sanitization** and validation
4. **Use HTTPS** in production
5. **Implement rate limiting** to prevent abuse
6. **Add logging** for monitoring and debugging

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- [@xManoelx](https://github.com/xManoelx) - Initial work

## 🆘 Support

If you have any questions or run into issues, please:

1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Provide code examples and error messages when applicable

## 🔮 Future Enhancements

- [ ] Password hashing implementation
- [ ] JWT token-based authentication option
- [ ] Email verification for user registration
- [ ] Password reset functionality
- [ ] Rate limiting and API throttling
- [ ] Comprehensive unit and integration tests
- [ ] Docker containerization
- [ ] API versioning
- [ ] Enhanced error handling and logging
