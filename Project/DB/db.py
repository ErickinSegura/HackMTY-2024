import mysql.connector

class DB:
    def __init__(self):
        # Read credentials
        with open("credentials.txt", "r") as file:
            credentials = file.read().split("\n")

        self.conn = mysql.connector.connect(
            host=credentials[0],
            user=credentials[1],
            password=credentials[2],
            database=credentials[3],
            port=int(credentials[4]),
            ssl_ca=credentials[5]
        )

    def run_query(self, query):
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        for row in self.result:
            print(row)
        self.cursor.close()


# # Read credentials
# with open("credentials.txt", "r") as file:
#     credentials = file.read().split("\n")

# conn = mysql.connector.connect(
#     host=credentials[0],
#     user=credentials[1],
#     password=credentials[2],
#     database=credentials[3],
#     port=int(credentials[4]),
#     ssl_ca=credentials[5]
# )

# cursor = conn.cursor()

# cursor.execute("SELECT * FROM opinion")
# result = cursor.fetchall()
# for row in result:
#     print(row)

# cursor.close()
# conn.close()