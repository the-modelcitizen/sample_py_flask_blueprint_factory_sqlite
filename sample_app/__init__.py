print('sample_app __init__.py')
import os, __main__

if __main__.__file__ == 'sample_test.py':
    from sample_app.test_config_items.test_config import test_config_path as config_path
else:
    from sample_app.config import config_path


# create_app is imported after load_env() is called to ensure any necessary
# environment variables are loaded before the Flask app is created
from sample_app.sample_app import create_app

# this is where the actual Flask app is created via the create_app() app
# factory found in sample_app.py
app = create_app(config_path)
