# Capstone Project - Student Complaint Management System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![Azure](https://img.shields.io/badge/Azure%20Cloud-Deployed-blue?logo=microsoft-azure)
![License](https://img.shields.io/badge/License-MIT-green)

A cloud-based complaint management system for educational institutions, built with Flask and Microsoft Azure services.

## Features

- **Student Portal**
  - Submit complaints with attachments (images/docs)
  - Track complaint status in real-time
  - Receive email notifications
- **Admin Dashboard**
  - View and manage all complaints
  - Assign complaints to staff
  - Update resolution status
- **Cloud Integration**
  - Azure Blob Storage for file uploads
  - Azure SQL Database for complaint data
  - Azure Logic Apps for email automation
  - Application Insights for monitoring

## Tech Stack

**Frontend:**  
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white)

**Backend:**  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)

**Database & Storage:**  
![Microsoft SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?logo=microsoft-sql-server&logoColor=white)
![Azure Blob Storage](https://img.shields.io/badge/Azure%20Blob%20Storage-0078D4?logo=microsoft-azure&logoColor=white)

**DevOps:**  
![Azure Logic Apps](https://img.shields.io/badge/Azure%20Logic%20Apps-0078D4?logo=microsoft-azure&logoColor=white)
![Application Insights](https://img.shields.io/badge/Application%20Insights-0078D4?logo=microsoft-azure&logoColor=white)

## Getting Started

### Prerequisites

- Python 3.8+
- Azure account (for cloud services)
- Git

### Installation

# 1. Clone the repository
* git clone https://github.com/sahutushar/Complaint-management
* cd Capstone Project---Student-Complaint-Management-System

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables (create a .env based on .env.example)
 ── Example (.env) ─────────────────────────────────────────
 AZURE_STORAGE_CONNECTION_STRING="your_azure_blob_connection_string"
 AZURE_SQL_CONN_STRING="your_sql_db_connection_string"
 LOGIC_APP_WEBHOOK_URL="your_logic_app_trigger_url"
 APPINSIGHTS_CONNECTION_STRING="your_app_insights_connection_string"
 ───────────────────────────────────────────────────────────

# 4. Run the application locally
export FLASK_APP=app.py          # use `set` on Windows
export FLASK_ENV=development
flask db upgrade                 # create / migrate tables
flask run                        # starts on http://127.0.0.1:5000

# 5. Live deployment (Azure App Services)
  • Service  : Azure Web Apps
  • Region   : Central India
  • Stack    : Python 3.8
  • URL      : https://6604528tusharsahug3batch3-exczaeg7dec4egfx.centralindia-01.azurewebsites.net/submit

# (Optional) CI/CD via GitHub Actions can be added for automated deploys.








