from db.run_sql import run_sql
from models.biting import *
from models.human import *
from models.zombie import *

def save(biting):
    sql = "INSERT INTO bitings(zombie_id, human_id) VALUES (%s, %s) RETURNING id"
    values = [biting.zombie.id, biting.human.id]

    results = run_sql(sql, values)

    biting.id =results[0]['id']
    return biting

def select_all():
    bitings = []

    sql = "SELECT * FROM bitings"
    results = run_sql(sql)

    for row in results:
        biting = Biting(row['zombie_id'], row['human_id'], row['id'])
        bitings.append(biting)
    return bitings