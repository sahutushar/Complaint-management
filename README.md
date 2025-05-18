# 📝 Complaint-Management  
*A cloud-ready student-complaint portal built with Python (Flask) and Microsoft Azure.*

---

## 🌟 What This Project Does
- **Students** quickly file campus issues, attach a photo or PDF, and watch the status flow  
  **Submitted → Assigned → In Progress → Done**  
- **Admins / staff** view a real-time dashboard, assign jobs, and update progress  
- All data lives on **Azure SQL Database**; files are streamed to **Azure Blob Storage**  
- **Logic Apps** send email/SMS notifications; **Application Insights** captures logs & metrics  

---

## 🛠 Tech Stack
| Layer | Tools & Services |
|-------|------------------|
| **Frontend** | HTML 5 · CSS 3 · Bootstrap |
| **Backend**  | Python 3 · Flask |
| **Database & Storage** | Azure SQL Database · Azure Blob Storage |
| **DevOps & Monitoring** | Azure App Service · Logic Apps · Application Insights |
| **CI/CD** (optional) | GitHub Actions |

---

## 🚀 Quick Start (Local)

```bash
# 1 · clone
git clone https://github.com/sahutushar/Complaint-management.git
cd Complaint-management

# 2 · install packages
pip install -r requirements.txt

# 3 · configure secrets
cp .env.example .env       # then add your own keys
# AZURE_STORAGE_CONNECTION_STRING=...
# AZURE_SQL_CONN_STRING=...
# LOGIC_APP_WEBHOOK_URL=...
# APPINSIGHTS_CONNECTION_STRING=...

# 4 · run
python app.py              # or: flask run
Open http://127.0.0.1:5000 in your browser.

🌐 Live Demo
Deployed on Azure App Service
🔗 https://6604528tusharsahug3batch3-exczaeg7dec4egfx.centralindia-01.azurewebsites.net/submit

Setting	Value
Region	Central India
Runtime	Python 3.8
Scaling	P1v2 (auto-scale)

📂 Project Structure
csharp
Copy
Edit
Complaint-management/
├── app.py                # Flask entry-point
├── templates/            # Jinja2 HTML files
├── static/               # CSS, JS, images
├── requirements.txt
├── .env.example          # variable names (no secrets)
└── README.md
🧰 Useful Make Targets
bash
Copy
Edit
make run          # start local server
make lint         # flake8 code quality
make deploy       # zip & push to Azure
🤝 Contributing
Fork the repo, create a feature branch.

Commit your changes.

Open a pull request—describe why the change is useful.

📄 License
Released under the MIT License – see LICENSE for full text.

“Snap a photo, hit submit, watch it get fixed — powered by Azure.”

csharp
Copy
Edit

**How to use**

1. Save the snippet as `README.md` in the repo root.  
2. Commit & push:

```bash
git add README.md
git commit -m "Add comprehensive project README"
git push origin main   # or master
