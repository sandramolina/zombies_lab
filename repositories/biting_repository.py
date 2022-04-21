from unittest import result
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
        biting = Biting(row['human_id'], row['zombie_id'], row['id'])
        bitings.append(biting)
    return bitings

def select(id):
    biting = None
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        biting = Biting(result['human_id'], result['zombie_id'], result['id'])
    return biting


def delete(id):
    sql = "DELETE FROM visits WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM bitings WHERE id = %s"
    values = [id]
    run_sql(sql,values)

def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)