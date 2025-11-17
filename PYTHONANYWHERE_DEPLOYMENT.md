# PythonAnywhere Deployment Guide for HOOPS

## Prerequisite: Push Your Code to GitHub

Since your repository at [https://github.com/francisramonlabajo621-max/HOOPS.git](https://github.com/francisramonlabajo621-max/HOOPS.git) is currently empty, you need to push your code first. Run these commands in your local project directory:

```bash
# Navigate to your local HOOPS project directory
cd C:\Users\Stephen\HOOPS

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit files
git commit -m "Initial commit - HOOPS Flask blog application"

# Add remote repository
git remote add origin https://github.com/francisramonlabajo621-max/HOOPS.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note:** You may need to authenticate with GitHub. Use a personal access token if prompted for a password.

## Step 1: Clone Repository and Set Up Virtual Environment

```bash
cd ~
git clone https://github.com/francisramonlabajo621-max/HOOPS.git HOOPS
python3.11 -m venv ~/.virtualenvs/hoops
source ~/.virtualenvs/hoops/bin/activate
pip install --upgrade pip
pip install -r ~/HOOPS/requirements.txt
```

## Step 2: Configure Web App

1. Go to the **Web** tab in PythonAnywhere dashboard
2. Click **"Add a new web app"**
3. Select **"Manual configuration"**
4. Choose **Python 3.11**
5. Set **Working directory** to: `/home/<your-username>/HOOPS`
6. Set **Virtualenv** to: `/home/<your-username>/.virtualenvs/hoops`

## Step 3: Set Environment Variables

In the **Web** tab, scroll down to **Environment Variables** section and add:
- `SECRET_KEY` - Set this to a secure random string (you can generate one using Python: `import secrets; print(secrets.token_hex(32))`)

## Step 4: Create WSGI Configuration File

Create/edit the WSGI file (usually `/var/www/<your-username>_pythonanywhere_com_wsgi.py` or similar) with the following content:

```python
import sys
from pathlib import Path

# Add your project directory to the path
project_root = Path('/home/<your-username>/HOOPS')
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Import your Flask app
from app import app as application

# Optional: Set up logging
import logging
logging.basicConfig(level=logging.INFO)
```

**Important:** Replace `<your-username>` with your actual PythonAnywhere username in both the path and the WSGI file.

## Step 5: Initialize Database

Run these commands in a Bash console:

```bash
cd ~/HOOPS
source ~/.virtualenvs/hoops/bin/activate
python3.11
```

Then in Python:
```python
from app import app, db
with app.app_context():
    db.create_all()
    print("Database initialized!")
exit()
```

## Step 6: Reload Web App

1. Go back to the **Web** tab
2. Click the green **Reload** button to restart your web app

## Step 7: Access Your App

Your app should now be available at: `https://<your-username>.pythonanywhere.com`

## Troubleshooting

- **Check error logs:** Go to Web tab → Error log
- **Check server log:** Go to Web tab → Server log
- **Verify paths:** Make sure all paths use your actual username
- **Database location:** The SQLite database will be created in `/home/<your-username>/HOOPS/instance/blog.db`
- **Static files:** Make sure static files are accessible (PythonAnywhere should handle this automatically)

## Additional Notes

- If you're using a free account, your app will sleep after inactivity
- For file uploads, make sure the `static/uploads` directory has proper permissions
- Consider using MySQL or PostgreSQL for production instead of SQLite

