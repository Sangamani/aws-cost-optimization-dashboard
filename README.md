# AI AWS Cost Detective 🚀

An AI-powered cloud cost optimization platform built using AWS, Terraform, FastAPI, React, and Python.

This platform provisions real AWS infrastructure, scans live EC2 resources, analyzes infrastructure usage, and generates optimization recommendations through a real-time dashboard.

---

# 📌 Features

✅ Real-time AWS EC2 scanning
✅ Terraform Infrastructure-as-Code provisioning
✅ FastAPI backend APIs
✅ React dashboard frontend
✅ AI-based optimization recommendations
✅ Live cloud infrastructure analysis
✅ AWS IAM authentication integration
✅ Full-stack cloud architecture

---

#  Architecture

Terraform → AWS EC2 → FastAPI Backend → React Dashboard → AI Recommendations

---

#  Tech Stack

## Cloud

* AWS EC2
* AWS IAM
* AWS CLI

## Infrastructure as Code

* Terraform

## Backend

* Python
* FastAPI
* Boto3

## Frontend

* React
* Vite
* Axios

## DevOps & Tools

* Git
* GitHub
* VS Code

---

# 📂 Project Structure

```bash
aws-cost-detective/
│
├── frontend/
│   ├── src/
│   └── package.json
│
├── src/
│   ├── aws_client.py
│   ├── scanner.py
│   ├── recommendations.py
│   ├── main.py
│   └── test_scanner.py
│
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── ec2.tf
│   └── outputs.tf
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

#  Setup Guide

## 1. Clone Repository

```bash
git clone https://github.com/Sangamani/ai-aws-cost-detective.git
cd ai-aws-cost-detective
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure AWS CLI

```bash
aws configure
```

Enter:

* AWS Access Key
* AWS Secret Key
* Region

---

## 5. Run FastAPI Backend

```bash
uvicorn src.main:app --reload
```

Backend URL:

```bash
http://127.0.0.1:8000
```

---

## 6. Run Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```bash
http://localhost:5173
```

---

#  AI Recommendation Engine

The platform analyzes AWS EC2 instances and generates optimization recommendations.

Example:

```json
{
  "issue": "Low utilization possible",
  "recommendation": "Stop instance during non-working hours",
  "estimated_savings": "$10/month"
}
```

---

# Dashboard Features

* Total EC2 instances
* Running instance count
* Live AWS infrastructure table
* AI recommendation cards
* Real-time backend integration

---

#  Demo Screenshots

## Dashboard
![image alt](https://github.com/Sangamani/ai-aws-cost-detective/blob/main/Screenshot%202026-05-31%20123510.png?raw=true)


(Add screenshot here)

## AWS EC2 Console

(Add screenshot here)

## Terraform Apply

(Add screenshot here)

---

# Future Improvements

* CloudWatch metrics integration
* AWS Cost Explorer integration
* GPT-powered recommendation summaries
* Multi-cloud support
* Cost forecasting charts
* User authentication

---

#  Author

Sangamani Mohanty

GitHub:
https://github.com/Sangamani

---

# ⭐ Project Goal

This project was built to gain hands-on experience with:

* Cloud infrastructure automation
* Terraform provisioning
* AWS services
* Backend API development
* React frontend integration
* Real-time cloud optimization workflows
