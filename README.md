# Capstone Project - Student Complaint Management System

A cloud-based Complaint Management System where students can quickly file campus issues online. Each complaint—title, description, category, optional photo—is saved in Azure SQL and the image in Azure Blob Storage.

Students get a dashboard that shows their complaints moving through four statuses (Submitted → Assigned → In Progress → Done). Admins have a separate dashboard to view new complaints, assign them to staff, and update status in real time. All traffic is handled by a lightweight Flask API hosted on Azure App Service, with Application Insights for monitoring and Logic Apps/webhooks for optional email/SMS alerts.

In short: snap a photo, submit the issue, watch it get fixed—fully tracked in the cloud.

Capstone - Student Complaint Management System
Python Flask Azure License

A cloud-based complaint management system for educational institutions, built with Flask and Microsoft Azure services.

🌟 Features
Student Portal

Submit complaints with attachments (images/docs)
Track complaint status in real-time
Receive email notifications
Admin Dashboard

View and manage all complaints
Assign complaints to staff
Update resolution status
Cloud Integration

Azure Blob Storage for file uploads
Azure SQL Database for complaint data
Azure Logic Apps for email automation
Application Insights for monitoring
🛠 Tech Stack
Frontend:
HTML5 CSS3 Bootstrap

Backend:
Python Flask

Database & Storage:
MicrosoftSQLServer Azure Blob Storage

DevOps:
Azure Logic Apps Application Insights

🚀 Getting Started
Prerequisites
Python 3.8+
Azure account (for cloud services)
Git
Installation
Clone the repository
git clone https://github.com/sahutushar/Complaint-management
cd Capstone---Student-Complaint-Management-System
2.Install dependencies

pip install -r requirements.txt
3.Set up environment variables Create a .env file based on .env.example:

AZURE_STORAGE_CONNECTION_STRING="your_azure_blob_connection_string"
AZURE_SQL_CONN_STRING="your_sql_db_connection_string"
LOGIC_APP_WEBHOOK_URL="your_logic_app_trigger_url"
APPINSIGHTS_CONNECTION_STRING="your_app_insights_connection_string"
🌐 Live Deployment
The application is deployed on Azure App Services and can be accessed at:
🔗 https://6604528tusharsahug3batch3-exczaeg7dec4egfx.centralindia-01.azurewebsites.net/submit

Deployment Details:
Service: Azure Web Apps
Region: Central India
Runtime Stack: Python 3.8
CI/CD: GitHub Actions (optional - add if used)
