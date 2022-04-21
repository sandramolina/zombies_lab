from flask import Blueprint, Flask, redirect, render_template, request
from models.biting import Biting
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

# NEW
@bitings_blueprint.route("/bitings/new")
def add_new_biting():
    zombies = zombie_repository.select_all()
    humans = human_repository.select_all()
    return render_template('bitings/new.html', humans = humans, zombies = zombies)

# CREATE
@bitings_blueprint.route("/bitings", methods=["POST"])
def create_biting():
    human = request.form['human_id']
    zombie = request.form["zombie_id"]
    new_biting = Biting(human, zombie)
    biting_repository.save(new_biting)
    return redirect('/bitings')

# EDIT

# UPDATE

# DELETE
