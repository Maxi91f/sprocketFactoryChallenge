"""
Simple script to start the application
"""
from sprocket_factory import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
