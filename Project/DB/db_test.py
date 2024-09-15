from db import DB

db = DB()

db.run_query("SELECT * FROM opinion")