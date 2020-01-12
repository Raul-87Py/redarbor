# DB
db_conf = { 
    'db' : 'mysql',
    'host' : 'db',
    'puerto' : '33060',
    'mysql_database' : 'redarbor_employeers',
    'login': { 
        'root': {
        'user_name' : 'root',
        'password' : 'siyu7e'
        },
        'user_rol': {
        'user_name' : 'redarbor',
        'password' : '9oi76gA'
        }
    }
}

SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".format(
    db_conf['db'],
    db_conf['login']['root']['user_name'],
    db_conf['login']['root']['password'],
    db_conf['host'],
    db_conf['puerto'],
    db_conf['mysql_database'])

# APP

HOST = '127.0.0.1'
PORT = 3700
