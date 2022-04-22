from flask import Blueprint, Flask, redirect, render_template, request
from models.biting import Biting
from models.human import Human
from models.zombie import Zombie
import repositories.biting_repository as biting_repository
import repositories.zombie_repository as zombie_repository
import repositories.human_repository as human_repository

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all()
    return render_template('bitings/index.html', bitings = bitings)

# NEW - render the form
@bitings_blueprint.route("/bitings/new")
def add_new_biting():
    zombies = zombie_repository.select_all()
    humans = human_repository.select_all()
    return render_template('bitings/new.html', humans = humans, zombies = zombies)

# CREATE - what would happen when we save the form in the new webpage
@bitings_blueprint.route("/bitings", methods=["POST"])
def create_biting():
    human_id = request.form['human_id']
    zombie_id = request.form["zombie_id"]

    human_object = human_repository.select(human_id)
    zombie_object = zombie_repository.select(zombie_id)

    new_biting = Biting(human_object, zombie_object)
    biting_repository.save(new_biting)
    return redirect('/bitings')

# EDIT
#Render the edit webpage
@bitings_blueprint.route('/bitings/<id>/edit', methods=['GET'])
def edit_biting(id):
    biting = biting_repository.select(id)
    bitings = biting_repository.select_all()
    humans = human_repository.select_all()
    zombies = zombie_repository.select_all()
    return render_template('bitings/edit.html', bitings = bitings, biting = biting, humans = humans, zombies = zombies)

# UPDATE
#route after the submit button is clicked on
@bitings_blueprint.route('/bitings/<id>', methods = ['POST'])
def update_biting(id):
    human_id = request.form['human_id']
    zombie_id = request.form["zombie_id"]

    human_object = human_repository.select(human_id)
    zombie_object = zombie_repository.select(zombie_id)

    biting_to_update = Biting(human_object, zombie_object, id)
    biting_repository.update(biting_to_update)
    return redirect('/bitings')

# DELETE
@bitings_blueprint.route('/bitings/<id>/delete', methods=["POST"])
def delete_biting(id):
    biting_repository.delete(id)
    return redirect('/bitings')