# 使用 SQLAlchemy + PyMySQL 操作数据库

from pymysql import install_as_MySQLdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Use pymysql to replace mysqldb
install_as_MySQLdb()

# DB INFO
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'test'
PASSWORD = 'test'

# Create DB Engine
db_url = 'mysql://%s:%s@%s:%s/%s?charset=utf8' \
    % (USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(db_url, encoding='utf-8', echo=True)

# Base Class
Base = declarative_base(bind=engine)

# Session Object
# SessionPool = sessionmaker(bind=engine)
# session = SessionPool()
