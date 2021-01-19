"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

db.create_all()

@app.route("/")
def pet_list():
    """Renders list of pets"""
    all_pets=Pet.query.all()
    return render_template("pet_list.html", all_pets=all_pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """ Allows user to add a pet to the database through a form"""
    form = AddPetForm()

    #executes for a post request
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age=form.age.data
        notes=form.notes.data

        pet= Pet(name=name, species=species, photo_url=photo_url, age = age, notes = notes)

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name} the {species}!")
        return redirect("/")
        
    #executes for a get request, including a failed form submission
    else:
        return render_template("add_pet.html", form=form)

@app.route('/pet/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """Shows detail about a certain pet as well as form to edit pet details"""
    
    pet=Pet.query.get(pet_id)
    form = EditPetForm(obj=pet) #EditPetForm allows the change of photo, notes, and pet availability

    if form.validate_on_submit():
        
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available=form.available.data

        db.session.add(pet)
        db.session.commit()

        flash(f"{pet.name} has been updated!")
        return redirect("/")

    else:
        return render_template("pet_details.html", pet=pet, form=form)
   
        

        
   
   