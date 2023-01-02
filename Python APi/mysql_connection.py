import pymysql
from flask import Flask, jsonify

app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host="localhost", user="username", password="password", db="database")

@app.route("/users")
def get_users():
    # Execute a MySQL query to retrieve the users from the database
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

    # Convert the result to a JSON object and return it
    return jsonify(result)

if __name__ == "__main__":
    app.run()

