import logging
import sys

import pymysql

RDS_HOST = 'end_point'
RDS_DATABASE = 'sys'
RDS_USER = 'admin'
RDS_PASSWORD = 'password'


def RDSConnected():
    try:
        conn = pymysql.connect(
            host=RDS_HOST,
            user=RDS_USER,
            db=RDS_DATABASE,
            passwd=RDS_PASSWORD,
            port=3306,
            charset='utf8')
        cur = conn.cursor()
    except:
        logging.error("RDS 연결 안됨")
        sys.exit(1)
    return conn, cur
