import configparser

config = configparser.ConfigParser()
config.read_file(open("dev.ini"))
username = config.get('DATABASE', 'username')
password = config.get('DATABASE', 'password')
host = config.get('DATABASE', 'host')
port = config.get('DATABASE', 'port')
database = config.get('DATABASE', 'database')

DB_URI = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True