# config.py
from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL", "sqlite:///rent.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STRIPE_API_KEY = getenv("STRIPE_API_KEY")
    STRIPE_PUBLISHABLE_KEY = getenv("STRIPE_PUBLISHABLE_KEY")
