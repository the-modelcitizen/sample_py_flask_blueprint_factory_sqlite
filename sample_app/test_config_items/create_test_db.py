print('create_test_db.py')
from sample_app.app1.models import Table1, Table2
from sample_app.app2.models import Table3, Table4
from sample_app.sample_app import db
print('before import of sample test in create test db')
from sample_test import app

print(app.config['SQLALCHEMY_DATABASE_URI'])

# calling this file in the Flask app will create a SQLite db with
# 4 tables in it that coincide with the tables imported above
# see sample_test.py for instructions

with app.app_context():
    db.metadata.create_all(db.engine, tables=[
        Table1.__table__,
        Table2.__table__,
        Table3.__table__,
        Table4.__table__
    ])
