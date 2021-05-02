print('create_db.py')
from sample_app.app1.models import Table1, Table2
from sample_app.app2.models import Table3, Table4
from sample_app.sample_app import db
# from sample_app import app

# calling this file in the Flask app will create a SQLite db with
# 4 tables in it that coincide with the tables imported above
# see sample_run.py for instructions

def create_db(app):
    with app.app_context():
        db.metadata.create_all(db.engine, tables=[
            Table1.__table__,
            Table2.__table__,
            Table3.__table__,
            Table4.__table__
        ])
