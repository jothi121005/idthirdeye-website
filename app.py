from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Create database table on startup
def init_db():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT,
            email   TEXT,
            company TEXT,
            service TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Contact form route
@app.route('/contact', methods=['POST'])
def contact():
    data    = request.json
    name    = data.get('name')
    email   = data.get('email')
    company = data.get('company')
    service = data.get('service')
    message = data.get('message')

    # Save to database
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO contacts VALUES (NULL, ?, ?, ?, ?, ?)',
        (name, email, company, service, message)
    )
    conn.commit()
    conn.close()

    print(f"✅ New enquiry from {name} ({email})")
    return jsonify({"status": "success", "message": "Message received!"})

# View all submissions
@app.route('/submissions', methods=['GET'])
def submissions():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)