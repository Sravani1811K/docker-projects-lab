from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "testdb")
    )

@app.route("/")
def home():
    return "Flask + MySQL running inside Docker 🚀"

@app.route("/users")
def users():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    cursor.execute("INSERT INTO users (name) VALUES ('Docker User')")
    conn.commit()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
