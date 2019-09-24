import configparser
import MySQLdb.cursors



config = configparser.ConfigParser()
config.read('config.ini')

def db_connect():
    return MySQLdb.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db']
                           )

