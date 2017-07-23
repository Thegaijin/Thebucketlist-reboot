# /run.py

from app import app
from flask_debugtoolbar import DebugToolbarExtension

app.run(debug=True)
# Activating flask debug mode, set to false before going live

toolbar = DebugToolbarExtension(app)
# setting up debug toolbar
