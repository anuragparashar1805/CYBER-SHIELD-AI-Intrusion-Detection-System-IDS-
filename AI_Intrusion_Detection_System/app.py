from flask import Flask, render_template, jsonify
import sqlite3
from packet_sniffer import start_sniffing, latest_metrics

app = Flask(__name__)

# Start background sniffing when app starts
start_sniffing()


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/api/metrics')
def get_metrics():
    # Endpoint to stream real-time data numbers to UI
    return jsonify(latest_metrics)


@app.route('/api/logs')
def get_logs():
    # Endpoint to fetch recent logs from DB
    conn = sqlite3.connect("ids_log.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 10")
    logs = cursor.fetchall()
    conn.close()

    formatted_logs = []
    for log in logs:
        formatted_logs.append({
            "timestamp": log[1],
            "src": log[2],
            "dst": log[3],
            "proto": log[4],
            "type": log[6],
            "severity": log[7]
        })
    return jsonify(formatted_logs)


if __name__ == '__main__':
    app.run(debug=True, port=5000)