# Flask Blog Application

A professional blog web application built with Flask, featuring user authentication, image uploads, search functionality, comments, and dark mode.

## Features

✅ **Login System** - User authentication with Flask-Login  
✅ **Post Images** - Upload and display images for each blog post  
✅ **Search Bar** - Filter posts by title or content  
✅ **Comments** - Add and manage comments on posts  
✅ **Dark Mode** - Toggle between light and dark themes  

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and visit:
```
http://127.0.0.1:5000/
```

## Default Admin Account

- **Username:** admin
- **Password:** admin123

*Please change the default admin password in production!*

## Project Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── blog.db               # SQLite database (created automatically)
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── post.html
│   ├── add_post.html
│   ├── edit_post.html
│   ├── login.html
│   └── register.html
└── static/               # Static files
    ├── style.css         # Custom styles with dark mode
    ├── script.js         # JavaScript for dark mode toggle
    └── uploads/          # Uploaded images (created automatically)
```

## Usage

1. **Register/Login** - Create an account or login with existing credentials
2. **Create Posts** - Click "Add Post" to create new blog posts with optional images
3. **Search** - Use the search bar to find posts by title or content
4. **Comment** - Add comments on any post (requires login)
5. **Dark Mode** - Click the moon/sun icon in the navbar to toggle dark mode
6. **Edit/Delete** - Edit or delete your own posts and comments

## Technologies Used

- **Flask** - Web framework
- **SQLAlchemy** - Database ORM
- **Flask-Login** - User session management
- **Bootstrap 5.3.2** - Frontend framework
- **Bootstrap Icons** - Icon library

## Notes

- The application uses SQLite database for simplicity
- Images are stored in `static/uploads/` directory
- Dark mode preference is saved in browser localStorage
- All passwords are hashed using Werkzeug's security functions

## License

Created for educational purposes.







# HOOPS
