import mysql.connector
import os

class DB:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        credentials_path = os.path.join(base_dir, "credentials.txt")
        # Read credentials
        with open(credentials_path, "r") as file:
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
        self.cursor.close()
        return self.result

    def get_comments_from_product(self, product):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"CALL get_comments_from_product({product})")
        self.result = self.cursor.fetchall()
        self.cursor.close()
        return self.result
