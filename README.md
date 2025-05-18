# Complaint-management

A cloud-based Complaint Management System where students can quickly file campus issues online. Each complaint—title, description, category, optional photo—is saved in Azure SQL and the image in Azure Blob Storage.

Students get a dashboard that shows their complaints moving through four statuses (Submitted → Assigned → In Progress → Done). Admins have a separate dashboard to view new complaints, assign them to staff, and update status in real time. All traffic is handled by a lightweight Flask API hosted on Azure App Service, with Application Insights for monitoring and Logic Apps/webhooks for optional email/SMS alerts.

In short: snap a photo, submit the issue, watch it get fixed—fully tracked in the cloud.
