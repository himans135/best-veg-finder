from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
# This website is for food or any other thing that will be best to search 
app = Flask(__name__)
CORS(app)

def get_db():
    conn = sqlite3.connect("db.sqlite3")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/add_stall", methods=["POST"])
def add_stall():
    data = request.json
    conn = get_db()
    conn.execute("INSERT INTO stalls (name, location, category, rating) VALUES (?, ?, ?, ?)",
                 (data["name"], data["location"], data["category"], data["rating"]))
    conn.commit()
    return jsonify({"status": "success"})

# ...existing code...

@app.route("/", methods=["GET"])
def home():
    return "API is running!"

@app.route("/stalls", methods=["GET"])
def get_stalls():
    location = request.args.get("location")
    conn = get_db()
    rows = conn.execute("SELECT * FROM stalls WHERE location LIKE ?", (f"%{location}%",)).fetchall()
    return jsonify([dict(row) for row in rows])

if __name__ == "__main__":
    app.run(debug=True)
