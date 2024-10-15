"""Sample for printing the App version"""
from app import create_app
from app.config import Config

app = create_app()

if __name__ == '__main__':
    app.run(debug=Config.DEBUG_MODE, host=Config.HOST, port=Config.PORT)
