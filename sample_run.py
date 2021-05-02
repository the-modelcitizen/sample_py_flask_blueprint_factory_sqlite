print('sample_run.py')
import os
from sample_app.config import load_env, config_path

# loads environment variables set in .env file found in root dir
load_env()

# this will initialize sample_app by running everything in the __init__.py file
# found in the sample_app directory
from sample_app import app

# if the following prints 'flask app name: sample app' to terminal, the
# app was successfully loaded
print(f'flask app name: {os.getenv("FLASK_APP")}')

# if you want to create a new sample.db (in sample_app directory), delete the
# current sample.db and uncomment the following code block before running 
# 'python sample_run.py' in the terminal. a new sample db (sample.db) will be
# created in the app root dir.
# after db is created, comment the code block out again and restart the
# Flask app.

# from sample_app.db_creator import create_db
# create_db(app)

if __name__=='__main__':
    app.run(debug=True, use_reloader=False)
