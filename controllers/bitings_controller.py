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

# NEW
@bitings_blueprint.route("/bitings/new")
def add_new_biting():
    zombies = zombie_repository.select_all()
    humans = human_repository.select_all()
    return render_template('bitings/new.html', humans = humans, zombies = zombies)

# CREATE
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

# UPDATE

# DELETE
