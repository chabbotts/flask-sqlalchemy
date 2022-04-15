from application import db # import the sqlalchemy object (db) created for our app


#The base class for all your models is called db.Model . It's stored on the SQLAlchemy instance you have to create.


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    cars = db.relationship('Car', backref='person')
    hobbies = db.relationship('Hobby', backref='person')


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_plate = db.Column(db.String(7), nullable=False)
    colour = db.Column(db.String(10), nullable=False)
    make = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)


class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hobbyName = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(30), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

