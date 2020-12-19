import os
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


def start_server():
    file = os.path.join(BASE_DIR, 'manage.py')
    subprocess.call([sys.executable, file, 'runserver'])
