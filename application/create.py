# This file should be run manually (directly) to pre-populate
# the database
# NOTE! The database MUST exist before we try to connect to it

from application import db
from application.models import Person, Car

# create our database schema
# db.create_all()
# create_all() creates all tables.
# drop_all() drops all tables.

db.drop_all()
db.create_all()

testPerson1 = Person(first_name='Julie',last_name='Dooley')
testPerson2 = Person(first_name='Victoria',last_name='Lloyd')

car1 = Car(number_plate='JU21DOO', person_id=1, colour='Red', make="Ferrari", model='V12')
car2 = Car(number_plate='JU20XXX', person_id=1, colour='Black', make="Mercedes-Benz", model='CLS')
car3 = Car(number_plate='VL21LLO', person_id=2, colour='Grey', make="Ford", model='Focus')

cars = [car1, car2, car3]
# car4 = Car(number_plate='BART21', person_id=3)

db.session.add(testPerson1)
db.session.add(testPerson2)
# db.session.add(car1)
# db.session.add(car2)
# db.session.add(car3)

db.session.add_all(cars)
# db.session.add(car4)
db.session.commit()
