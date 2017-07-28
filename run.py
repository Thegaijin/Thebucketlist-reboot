# run.py

from app import app
from flask_debugtoolbar import DebugToolbarExtension


# Activating flask debug mode, set to false before going live

toolbar = DebugToolbarExtension(app)
# setting up debug toolbar

if __name__ == '__main__':
    app.run(debug=True)