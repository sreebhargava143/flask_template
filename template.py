"""
Application Entry point
"""

import sys
from project import create_app
from project.services import db

app = create_app()

@app.shell_context_processor
def make_shell_context():
    """
    setting up flask-shell context which pre-imports models
    """
    return {
        'db':db 
        }

if __name__ == "__main__":
    app.run(debug = True)