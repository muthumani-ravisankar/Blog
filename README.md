# Blog API

This project is a  API for a blogging platform, developed using Flask, and pymongo in monogodb. It provides a comprehensive set of endpoints for user management and blog post operations. 

## Features

### User Management

Users can sign up, log in, and have their information securely stored in the database. User passwords are hashed before storage for enhanced security. User can chang their passwords, which are stored and managed in mongodb.

### Blog Post Operations

Users can create, update, view, and delete blog posts. All blog post operations require user authentication.

### Error Handling

The API includes error handling, providing meaningful feedback to clients when errors occur.

### Configuration
make changes in `config.json` file by add your own mongodb connection string to access database and secret key.
```json
{
    "mongodb_string":"mongodb_connection_string",
    "secret_Key":"your_Secret_key"
}
```

## Installation

```bash
# Clone the repository

# Enter the project directory

# Install Python dependencies
pip install -r requirements.txt

# Travers the blog directory  and
# Run the application
python app.py
```
