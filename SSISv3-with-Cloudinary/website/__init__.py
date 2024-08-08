from flask import Flask
from flask_mysql_connector import MySQL
import os
from dotenv import load_dotenv
from config import Config
import cloudinary
import cloudinary.uploader
import cloudinary.api

load_dotenv()

# Create the MySQL instance outside the Flask app
mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cloudinary.config(
        cloud_name=Config.CLOUDINARY_CLOUD_NAME,
        api_key=Config.CLOUDINARY_API_KEY,
        api_secret=Config.CLOUDINARY_API_SECRET
    )

    # Initialize the MySQL extension
    mysql.init_app(app)

    # Import and register blueprints here
    from website.routes.collegeRoute import collegeRoute
    app.register_blueprint(collegeRoute)

    from website.routes.courseRoute import courseRoute
    app.register_blueprint(courseRoute)

    from website.routes.studentRoute import studentRoute
    app.register_blueprint(studentRoute)

    return app
