from app import app
from models import db, Car
import json

def fetch_data_to_dict():
    data_dict = {}
    with app.app_context():
        cars = Car.query.all()
        for car in cars:
            driver = car.driver
            if driver:
                data_dict[car.CRegistration] = {
                    'driver_name': f'{driver.DFirstName} {driver.DLastName}',
                    'driver_phone': driver.DTel
                }
            else:
                data_dict[car.CRegistration] = {
                    'driver_name': 'Unknown',
                    'driver_phone': 'Unknown'
                }
    return data_dict

if __name__ == '__main__':
    with app.app_context():
        data_dict = fetch_data_to_dict()
        with open('data.json', 'w') as json_file:
            json.dump(data_dict, json_file)
        print("Data fetched and saved to data.json")
