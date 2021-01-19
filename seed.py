"""Seed file to make sample data for pet adoption app."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Create some pets
pet1 = Pet(name='Mochi', species='dog', photo_url='https://d3544la1u8djza.cloudfront.net/APHI/Blog/2016/11_November/11-07/Meet+the+Dachshund+_+Personality+Health+and+Care+_+ASPCA+Pet+Health+Insurance+_+red+wiener+dog+sitting+on+a+couch-min.jpg',
age = 1, notes = 'Long-haired brown dachshung good with children')

pet2 = Pet(name='Zucchini', species='cat', photo_url='https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png',
age = 2, notes = 'Fiesty cat that likes to hunt mice')

pet3 = Pet(name='Loki', species='dog', photo_url='https://www.pitbullinfo.org/uploads/7/8/9/7/7897520/pitbull-dog-4-article_4_orig.jpg',
age = 1, available =False)

pet4 = Pet(name='Jimmy', species='porcupine', photo_url='https://media.npr.org/assets/img/2019/04/08/dl607_porcupines_penelope_med_custom-1c215dc255d853ec396b8c6d8e2a740adcc46243.jpg',
age = 3, notes = 'Jimmy is a low-maintence parakeet that enjoys music and looking at himself in the mirror')

#  add pets to the session
db.session.add(pet1)
db.session.add(pet2)
db.session.add(pet3)
db.session.add(pet4)

# Commit
db.session.commit()