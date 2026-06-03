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
    conn.execute(
        "INSERT INTO stalls (name, state, city, location, phone, category, rating, style) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (
            data["name"],
            data.get("state", ""),
            data.get("city", ""),
            data.get("location", ""),
            data.get("phone", ""),
            data["category"],
            data["rating"],
            data.get("style", "Traditional")
        )
    )
    conn.commit()
    return jsonify({"status": "success"})

# ...existing code...

@app.route("/", methods=["GET"])
def home():
    return "API is running!"

@app.route("/stalls", methods=["GET"])
def get_stalls():
    state = request.args.get("state")
    city = request.args.get("city")
    style = request.args.get("style")
    location = request.args.get("location")

    query = "SELECT * FROM stalls"
    filters = []
    params = []

    if state:
        filters.append("state = ?")
        params.append(state)
    if city:
        filters.append("city = ?")
        params.append(city)
    if style:
        filters.append("style = ?")
        params.append(style)
    if location:
        filters.append("location LIKE ?")
        params.append(f"%{location}%")

    if filters:
        query += " WHERE " + " AND ".join(filters)

    conn = get_db()
    rows = conn.execute(query, params).fetchall()
    return jsonify([dict(row) for row in rows])

if __name__ == "__main__":
    app.run(debug=True)
