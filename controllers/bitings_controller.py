from flask import Blueprint, Flask, redirect, render_template, request
from models.zombie import Zombie
import repositories.biting_repository as biting_repository
import repositories.zombie_repository as zombie_repository

bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all()
    return render_template('bitings/index.html', bitings = bitings)

# CREATE
@bitings_blueprint.route("/bitings", methods=["POST"])
def create_biting():
    human = request.form['human_id']
    zombie = request.form["zombie_id"]

def create_zombie_type():
    name = request.form["name"]
    new_zombie_type = ZombieType(name)
    zombie_type_repository.save(new_zombie_type)
    return redirect("/zombietypes")


# EDIT

# UPDATE

# DELETE
