from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://asdf0359:zxcv0359@localhost:3306/fastAPItest")

meta = MetaData()

conn = engine.connect()


# engine: 建立連線
# metaData: 建立資料庫
# conn: 建立資料庫連線
