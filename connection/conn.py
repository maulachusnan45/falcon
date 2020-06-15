from config import driverDB, userDB, passwordDB, hostDB, portDB, dbName
from pony.orm import *
db = Database()
db.bind(driverDB, host=hostDB, user=userDB, passwd=passwordDB, db=dbName)
sql_debug(True)
