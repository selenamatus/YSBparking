from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from models import db, Car, Driver
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# User model
class User(db.Model, UserMixin):
    __tablename__ = 'tbUsers'
    id = db.Column('UidCard', db.String(10), primary_key=True) 
    first_name = db.Column('UFirstName', db.String(80), nullable=False)
    password = db.Column('UPassword', db.String(120))

    def check_password(self, password):
        # Here, we're assuming passwords are stored in plaintext, which is not recommended.
        return self.password == password

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Routes
@app.route('/')
def home():
    return 'Welcome to the License Plate Lookup App!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        first_name = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(first_name=first_name).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('search'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    if request.method == 'POST':
        reg_number = request.form['license_plate']
        car = Car.query.filter_by(CRegistration=reg_number).first()
        if car and car.driver:
            return render_template('search.html', result=car)
        else:
            return render_template('search.html', result='not_found')
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
