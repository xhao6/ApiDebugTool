import sys
import os

sys.path.insert(0, 'var/www/html/ApiDebugTool')

activate_this = '/home/ubuntu/workspace/ApiDebugTool/venvlinux/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

path = os.path.join(os.path.dirname(__file__), os.pardir)
if path not in sys.path:
    sys.path.append(path)

from app.server import app as application
