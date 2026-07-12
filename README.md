# Smart Task Manager

A polished Flask-based task manager application with user authentication, task CRUD operations, and a modern responsive UI.

## Intern ID

- **CITS2502**

## Features

- User registration and login
- Secure password hashing
- Add, edit, and delete tasks
- Task status, priority, and due date management
- Responsive Bootstrap interface with modern styling
- SQLite database persistence

## Tech Stack

- Python 3
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite
- Bootstrap

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Smart-Task-Manager
   ```
2. Create and activate the virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

1. Ensure the virtual environment is active.
2. Start the Flask app:
   ```bash
   python app.py
   ```
3. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Project Structure

- `app.py` - Main Flask application and route handlers
- `models.py` - Database models for users and tasks
- `config.py` - Flask configuration settings
- `templates/` - HTML templates for the app views
- `static/css/style.css` - Custom styling for the user interface
- `instance/database.db` - SQLite database file

## Notes

- The application creates the SQLite database automatically if it does not exist.
- For production, set a secure `SECRET_KEY` and configure a production-ready database.

## License

This project is provided as-is for academic use.
