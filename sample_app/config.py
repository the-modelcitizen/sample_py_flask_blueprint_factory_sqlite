print('config.py')
import os
from dotenv import load_dotenv


config_basedir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(config_basedir, 'config.py')


def load_env():
    load_dotenv(os.path.join(config_basedir, '.env')) 
    print(f'test or run: {os.getenv("TEST_OR_RUN")} mode')
    return 'run environment has been loaded'


SECRET_KEY = os.environ.get('SECRET KEY') or 'super_secret_string'
SQLALCHEMY_DATABASE_URI = 'sqlite:///sample.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
