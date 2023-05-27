"""This is a main file to run the application"""
from init_app import create_app
# -------------------------------------------------------------------------

app = create_app()

if __name__ == '__main__':
    app.run()
