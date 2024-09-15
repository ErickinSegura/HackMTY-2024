import mysql.connector
import os

class DB:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        credentials_path = os.path.join(base_dir, "credentials.txt")
        # Read credentials
        with open(credentials_path, "r") as file:
            self.credentials = file.read().split("\n")

    def run_query(self, query):
        self.conn = mysql.connector.connect(
            host=self.credentials[0],
            user=self.credentials[1],
            password=self.credentials[2],
            database=self.credentials[3],
            port=int(self.credentials[4]),
            ssl_ca=self.credentials[5]
        )

        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(query)
            self.result = self.cursor.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.result = []
        finally:
            if self.cursor:
                self.cursor.close()
        return self.result

    def get_comments_from_product(self, product):
        self.conn = mysql.connector.connect(
            host=self.credentials[0],
            user=self.credentials[1],
            password=self.credentials[2],
            database=self.credentials[3],
            port=int(self.credentials[4]),
            ssl_ca=self.credentials[5]
        )

        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("CALL get_comments_from_product(%s)", (product,))
            self.result = self.cursor.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.result = []
        finally:
            if self.cursor:
                self.cursor.close()
        return self.result


    def close(self):
        self.cursor.close()
        self.conn.close()
