from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from config.db import meta

users = Table(
    'users',meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('password', String(255)),

)

# users: 建立資料表
# meta: 建立資料庫
# Column: 建立資料表欄位