print('app2 __init__')

# __init__.py files make Python treat containing directory like a package.
# When a file imports from app1, app1's __init__.py is initialized without
# being explicitly called. For example, if a file contained 'from app1 import
# myprefix', the Flask app would run all imports in app1's __init__.py file.
# If this __init__.py file was run, flask Blueprint, myprefix, app1 models
# and app1 routes would all be run. Also, an import statement such as 'from
# app1 import myprefix' becomes possible without having to create a separate
# file (myprefix_file) containing 'myprefix' and importing it as 'from
# app1.myprefix_file import myprefix'.

from flask import Blueprint

# This makes myprefix available for importing into anything in the app1 dir.
# When imported, myprefix will be available to be used as @myprefix.route().
noprefix = Blueprint('noprefix', __name__)

# These are imported after the variable is declared to avoid potential
# circular reference issues.
from sample_app.app2 import models, routes
