from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Car(db.Model):
    __tablename__ = 'TbCars'
    CRegistration = db.Column(db.String(15), primary_key=True)
    CSeqMainDriver = db.Column(db.Integer, db.ForeignKey('TbDrivers.DSeqNum'))
    driver = db.relationship('Driver', back_populates='cars')

class Driver(db.Model):
    __tablename__ = 'TbDrivers'
    DSeqNum = db.Column(db.Integer, primary_key=True)
    DFirstName = db.Column(db.String(100), nullable=False)
    DLastName = db.Column(db.String(100), nullable=False)
    DTel = db.Column(db.String(50), nullable=False)
    cars = db.relationship('Car', back_populates='driver', uselist=False)

    def __repr__(self):
        return f'<Driver {self.name}>'
