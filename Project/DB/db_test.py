from db import DB

db = DB()

result = db.run_query("SELECT * FROM opinion")

print(result)