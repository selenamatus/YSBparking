from app import app, db
from models import Car, Driver  # Import models here

with app.app_context():
    db.create_all()
    print("Database initialized!")
