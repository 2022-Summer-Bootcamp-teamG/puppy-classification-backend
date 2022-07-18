import pymysql

RDS_HOST = 'end_point'
RDS_DATABASE = 'summer-bootcamp-2022'
RDS_USER = 'admin'
RDS_PASSWORD = 'password'

def getConnection():
    return pymysql.connect(
        host=RDS_HOST,
        user=RDS_USER,
        db=RDS_DATABASE,
        password=RDS_PASSWORD,
        charset='utf8'
    )