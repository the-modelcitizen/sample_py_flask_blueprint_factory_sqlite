print('sample_test.py')
import os
from sample_app.test_config_items.test_config import load_env, test_config_path

# loads environment variables set in .env file found in root dir
print(load_env())

# this will initialize sample_app by running everything in the __init__.py file
# found in the sample_app directory
from sample_app import app


# if the following prints 'flask app name: sample app' to terminal, the
# app was successfully loaded
print(f'flask app name: {os.getenv("FLASK_APP")}')

# if you want to create a new sample_test.db (in test_config_items directory),
# delete the current sample_test.db and uncomment the following code block
# before running 'python sample_test.py' in the terminal. a new sample db
# (sample_test.db) will be created in the sample_app/test_config_items
# directory.
# after db is created, comment the code block out again and restart the
# Flask app.

# from sample_app.db_creator import create_db
# create_db(app)

if __name__=='__main__':
    app.run(debug=True, use_reloader=False)
 