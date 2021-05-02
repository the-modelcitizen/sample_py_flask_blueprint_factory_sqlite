print('sample_app.py')
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

# instantiates an empty SQLAlchemy db object
db = SQLAlchemy()


# receives config data via config_path, instantiates a Flask app,
# configures the app and initializes it with the empty SQLAlchemy
# db and the app's db configurations, which were included in the
# config data
def create_app(config_path):
    app = Flask(__name__)
    app.config.from_pyfile(config_path)
    db.init_app(app)
    
    # Flask's blueprint library is used to help give larger Flask
    # apps, that include multiple smaller apps, a cleaner
    # structure. Below, the blueprint object from app1 and app2
    # are being imported so they can be registered in the app and
    # have prefixes assigned to them if desired (see routes.py in
    # app1 for more details on the prefixes). Once the blueprint is
    # registered in the app, a route for that blueprint can be used
    # by importing the blueprint object in routes.py (i.e. from
    # app1 import myprefix) and creating a route with the following
    # format: @<blueprint name>.route('/'), followed by a function.
    # See app1 or app2 routes.py for examples. 
    from sample_app.app1 import myprefix
    from sample_app.app2 import noprefix
    app.register_blueprint(myprefix, url_prefix='/myprefix')
    app.register_blueprint(noprefix)

    return app
