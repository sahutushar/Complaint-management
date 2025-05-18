

from flask import Flask, request, render_template, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient
import pyodbc
import os
import uuid
import requests
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)          # ← use __name__

app.secret_key = os.urandom(24)

# ── Azure Blob ────────────────────────────────────────────────────────────────
blob_service_client = BlobServiceClient.from_connection_string(
    os.getenv("AZURE_STORAGE_CONNECTION_STRING")
)
container_name = "tushar"

# ── Azure SQL ────────────────────────────────────────────────────────────────
conn_str = os.getenv("AZURE_SQL_CONN_STRING")  # store full string in .env

# ── Logic App Webhook URL ────────────────────────────────────────────────────
logic_app_url = os.getenv("LOGIC_APP_WEBHOOK_URL")

# ── Application Insights ─────────────────────────────────────────────────────
logger = logging.getLogger(__name__)
logger.addHandler(
    AzureLogHandler(connection_string=os.getenv("APPINSIGHTS_CONNECTION_STRING"))
)
logger.setLevel(logging.INFO)

# ── Routes ───────────────────────────────────────────────────────────────────
@app.route("/")
def home():
    return redirect(url_for("submit_complaint"))

@app.route("/submit", methods=["GET", "POST"])
def submit_complaint():
    if request.method == "POST":
        try:
            title = request.form["title"]
            description = request.form["description"]
            type_ = request.form["type"]
            file = request.files["file"]

            file_url = None

            # upload to Blob
            if file and file.filename:
                filename = secure_filename(file.filename)
                blob_name = f"{uuid.uuid4()}_{filename}"
                blob_client = blob_service_client.get_blob_client(
                    container=container_name, blob=blob_name
                )
                blob_client.upload_blob(file)
                file_url = blob_client.url

            # save to SQL
            with pyodbc.connect(conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO Complaints
                          (title, description, type, file_url, status)
                    VALUES (?,     ?,           ?,    ?,       ?)
                    """,
                    (title, description, type_, file_url, "Submitted"),
                )
                conn.commit()

            # notify Logic App
            requests.post(logic_app_url, json={
                "title": title,
                "description": description,
                "type": type_,
                "file_url": file_url,
                "status": "Submitted",
            })

            logger.info("Complaint submitted successfully")
            return redirect(url_for("student_dashboard"))

        except Exception as e:
            logger.error("Error while submitting complaint", exc_info=True)
            return jsonify(success=False, error=str(e)), 500

    return render_template("submit_complaint.html")

@app.route("/dashboard")
def student_dashboard():
    return render_template("student_dashboard.html")

@app.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html")

@app.route("/get_complaints")
def get_complaints():
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, title, description, type, file_url, status, submitted_at
                FROM Complaints ORDER BY submitted_at DESC
                """
            )
            rows = cursor.fetchall()
            complaints = [
                {
                    "id": r.id,
                    "title": r.title,
                    "description": r.description,
                    "type": r.type,
                    "file_url": r.file_url,
                    "status": r.status,
                    "submitted_at": r.submitted_at.strftime("%Y-%m-%d %H:%M:%S")
                                 if r.submitted_at else "N/A",
                }
                for r in rows
            ]
            return jsonify(complaints=complaints)
    except Exception as e:
        logger.error("Error fetching complaints", exc_info=True)
        return jsonify(error="Could not fetch complaints"), 500

@app.route("/assign_complaint", methods=["POST"])
def assign_complaint():
    try:
        data = request.get_json()
        with pyodbc.connect(conn_str) as conn:
            conn.execute(
                """
                UPDATE Complaints
                   SET status = ?, assigned_to = ?
                 WHERE id = ?
                """,
                ("Assigned", data["assignee"], data["id"]),
            )
            conn.commit()
        return jsonify(success=True, message="Complaint assigned successfully.")
    except Exception as e:
        logger.error("Error assigning complaint", exc_info=True)
        return jsonify(success=False, error=str(e)), 500

@app.route("/update_status", methods=["POST"])
def update_status():
    try:
        data = request.get_json()
        with pyodbc.connect(conn_str) as conn:
            conn.execute(
                "UPDATE Complaints SET status = ? WHERE id = ?",
                (data["status"], data["id"]),
            )
            conn.commit()
        return jsonify(success=True, message="Complaint status updated successfully.")
    except Exception as e:
        logger.error("Error updating complaint status", exc_info=True)
        return jsonify(success=False, error=str(e)), 500

# ── Run ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
