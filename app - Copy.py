from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from models import db, Car, Driver
from config import Config
import json
import os

app = Flask(__name__)
##app.config.from_object(Config)
##db.init_app(app)
app.secret_key = 'your_super_secret_key'

# Load data from JSON file into a dictionary
#def load_data_from_json():
    #data_dict = {}
    #if os.path.exists('data.json'):
        #with open('data.json', 'r') as json_file:
            #data_dict = json.load(json_file)
    #return data_dict

# Load data from JSON
with open('data.json', 'r', encoding='utf-8') as json_file:
    data_dict = json.load(json_file)


# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.route('/')
def home():
    return 'Welcome to the License Plate Lookup App!'

@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        reg_number = request.form['license_plate']
        car = Car.query.filter_by(CRegistration=reg_number).first()
        if car and car.driver:
            result = {
                'CRegistration': car.CRegistration,
                'driver_name': f'{car.driver.DFirstName} {car.driver.DLastName}',
                'driver_phone': car.driver.DTel
            }
        else:
            result = 'not_found'
        return render_template('search.html', result=result)
    return render_template('search.html')



if __name__ == '__main__':
    app.run(debug=True)
