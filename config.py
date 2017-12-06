

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(
    username="test",
    password="test1234",
    hostname="testdb.cejowb7jytbs.us-east-2.rds.amazonaws.com:3306",
    databasename="testdb",
)



SQLALCHEMY_POOL_RECYCLE = 3600

