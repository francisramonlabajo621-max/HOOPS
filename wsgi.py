import sys
from pathlib import Path

# Add your project directory to the path
project_root = Path('/home/mj1404/HOOPS')
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Import your Flask app
from app import app as application

# Optional: Set up logging
import logging
logging.basicConfig(level=logging.INFO)

