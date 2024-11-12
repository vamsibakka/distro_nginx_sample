from flask import Flask, jsonify  # flask class is imported to create web app
import mysql.connector

app = Flask(__name__)

# Database connection settings
db_config = {
    "host": "mysql-db",
    "user": "root",
    "password": "password",
    "database": "shop"
}

@app.route("/items")
def items():
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM items")
    items = [{"id": item[0], "name": item[1], "price": item[2]} for item in cursor.fetchall()]
    cursor.close()
    connection.close()
    return jsonify(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
