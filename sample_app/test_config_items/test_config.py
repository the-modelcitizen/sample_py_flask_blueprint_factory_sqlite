print('test_config.py')
import os
from dotenv import load_dotenv


config_basedir = os.path.abspath(os.path.dirname(__file__))
test_config_path = os.path.join(config_basedir, 'test_config.py')


def load_env():
    load_dotenv(os.path.join(config_basedir, '.env'))
    print(f'test or run: {os.getenv("TEST_OR_RUN")} mode')
    return 'test environment has been loaded'


SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_string'
SQLALCHEMY_DATABASE_URI = 'sqlite:///test_config_items/sample_test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
