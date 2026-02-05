from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_task():
    task = request.json["task"]
    conn = get_db()
    conn.execute("INSERT INTO todo (task) VALUES (?)", (task,))
    conn.commit()
    return jsonify({"status": "added"})

@app.route("/tasks")
def get_tasks():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM todo").fetchall()
    return jsonify([dict(t) for t in tasks])

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_task(id):
    conn = get_db()
    conn.execute("DELETE FROM todo WHERE id=?", (id,))
    conn.commit()
    return jsonify({"status": "deleted"})

if __name__ == "__main__":
    conn = get_db()
    conn.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, task TEXT)")
    conn.close()
    app.run(debug=True)
