from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'your_super_secret_key'  # Replace with a strong, random secret key for production

# Load data from JSON
with open('data.json', 'r', encoding='utf-8') as json_file:
    data_dict = json.load(json_file)

# Routes
@app.route('/')
def home():
    return 'Welcome to the License Plate Lookup App!'

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        license_plate = request.form['license_plate']
        result = data_dict.get(license_plate, 'not_found')
        return render_template('search.html', result=result, license_plate=license_plate)
    return render_template('search.html')

# Debugging route to list all files in the templates directory
@app.route('/debug')
def debug():
    try:
        files_list = os.listdir('templates')
        return '<br>'.join(files_list)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
