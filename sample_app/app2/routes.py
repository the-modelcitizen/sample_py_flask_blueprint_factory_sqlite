print('app2 routes')
from sample_app.app2 import noprefix
from sample_app.sample_app import db
from sample_app.app2.models import Table3, Table4

# myprefix is imported from app1 __init__.py
# prefix 'myprefix' is necessary for all routes in this file
# prefix set in main.py "app.register_blueprint(myprefix,
# url_prefix='/myprefix')"

# When all the routes in this file make requests (are called), they
# automatically receive the app_context from the currently running Flask
# app (which is created in sample_run.py or sample_test.py). The Flask app
# includes the db object that was initialized when create_app was called in
# sample_run.py or sample_test.py. This means if you printed something from
# the db object to terminal outside of a route request, it will only show a
# blank SQLAlchemy db object. When the same db object is called inside a
# route request, the current Flask app will magically include the db object
# that was initialized. This means if you printed something from the db
# object to terminal inside a route request, it will now show data from the
# full db object. This makes querying from db and writing to db in routes
# possible. It also means data from db query is available to be returned
# when a route is called as an endpoint.


# url '/' or '/index' will return 'noprefix index'
@noprefix.route('/')
@noprefix.route('/index')
def index():
    return 'noprefix index'

# url '/table3/<id>' will return the name and email address from
# Table3 that coincides with the <id> given
@noprefix.route('/table3/<id>')
def route2(id):
    result = Table3.query.filter_by(id=id).first()
    if result:
        return f'noprefix result: {result.name}, {result.email}'
    return f'noprefix result: no item with this id in db'

# url '/table3/<name>/<email>' will create and auto-incremented
# Table1 object with a name and email address that coincides with the <name>
# and <email> given and writes it to db
@noprefix.route('/table3/<name>/<email>')
def route3(name, email):
    person = Table3(name, email)
    db.session.add(person)
    db.session.commit()
    return f'''noprefix- this person was added to db- {person.id}, 
    {person.name}, {person.email}'''

# url '/table4/<id>' will return the name and email address from
# Table4 that coincides with the <id> given
@noprefix.route('/table4/<id>')
def route4(id):
    result = Table4.query.filter_by(id=id).first()
    if result:
        return f'noprefix result: {result.name}, {result.email}'
    return f'noprefix result: no item with this id in db'

# url '/table4/<name>/<email>' will create and auto-incremented
# Table4 object with a name and email address that coincides with the <name>
# and <email> given and writes it to db
@noprefix.route('/table4/<name>/<email>')
def route5(name, email):
    person = Table4(name, email)
    db.session.add(person)
    db.session.commit()
    return f'''noprefix- this person was added to db- {person.id}, 
    {person.name}, {person.email}'''
