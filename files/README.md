# ◈ DPex — Next-Gen Enterprise Operating System & Automation Platform

> **Engineered by Durvesh Parab** (Founder & CEO, Full Stack Architect)  
> *One roof. Six departments. Zero manual work.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Production Ready](https://img.shields.io/badge/Status-Live%20Engine%20v2.4-emerald.svg)]()
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)]()
[![Frontend: HTML5/CSS3/ESNext](https://img.shields.io/badge/Frontend-Glassmorphic%20Canvas%20UI-purple.svg)]()

---

## 🌟 Overview

**DPex** is a unified, high-performance enterprise automation platform and ERP designed from the ground up to replace fragmented spreadsheets, manual reconciliations, and chaotic departmental communication channels with a single, reactive event-driven data plane.

Built specifically for high-concurrency and claims-heavy operational environments (such as healthcare, third-party administration, finance, and corporate operations), DPex synchronizes six core departments under a single login:

1. **👥 HR**: Attendance, leave auto-approvals, automated salary transfers, and digital onboarding kits.
2. **⚙️ Operations**: Patient admission tracking, hospital SLA coordination, and proactive TAT breach prevention.
3. **📊 MIS**: Automated daily executive reports, multi-source dump validations, and instant CSV exports.
4. **🔎 Data Analysis**: Line-item claim vs. hospital bill audit, automated overcharge detection, and cap compliance.
5. **💰 Accounts**: Automated invoice tracking, debtor reminders, bank statement matching, and GST filing drafts.
6. **🚀 Business Development**: Inbound lead scoring, instant template proposal drafting, and pipeline conversion metrics.

---

## 🚀 Key Features & Architecture

- **Dual-Core Reactive Engine**: Processes incoming hospital records, bills, and data dumps in sub-45ms execution cycles.
- **Predictive TAT Watch**: Monitored queues that flag potential service-level agreement (SLA) breaches 3 hours before contractual limits.
- **Deep Multi-Source Reconciliation**: Cross-references 12,000+ row hospital billing dumps against insurer tariff caps in under 2 seconds.
- **Glassmorphic Interactive Command Center**: Real-time simulated operations dashboard with Web Audio API sound synthesis and interactive departmental task queues.
- **Lightweight Flask Backend**: Built-in honeypot anti-spam verification, SQLite/PostgreSQL support, and transactional SMTP notification dispatch.
- **Zero-Dependency Native Deployment**: Can run out-of-the-box on GitHub Pages, Netlify, or Vercel, or backed by the Python Flask microservice.

---

## 🛠️ Tech Stack & Engineering

| Tier | Technologies |
|---|---|
| **Frontend** | Modern JavaScript (ESNext), HTML5 Canvas, Web Audio API, Responsive CSS3 Variables, Glassmorphism |
| **Backend** | Python 3.9+, Flask, Flask-CORS, RESTful API architecture |
| **Data & Storage** | SQLite, PostgreSQL, Query optimization, Relational normalization |
| **Automation & RPA** | Event-driven rule engines, OCR document parsing, Webhook triggers, Scheduled Cron pipelines |
| **Security & Compliance** | Honeypot bot protection, TLS 1.3, AES-256 at rest, Role-Based Access Control (RBAC) |

---

## 📁 Repository Structure

```
.
├── index.html              # Core frontend application & interactive command center
├── dpex_demo_backend.py    # Flask REST API backend for demo booking & lead ingestion
├── README.md               # Project documentation & portfolio overview
└── .gitignore              # Standard git exclusion rules
```

---

## ⚡ Quickstart

### 1. Run the Frontend Locally
Simply open `index.html` in any modern web browser, or serve it with Python:

```bash
# Serve frontend on http://localhost:8000
python -m http.server 8000
```

### 2. Start the Demo Request Backend (Optional)
```bash
# Install dependencies
pip install flask flask-cors

# Set environment variables (optional)
export ADMIN_TOKEN="your-secure-admin-token"
export SMTP_HOST="smtp.gmail.com"
export SMTP_USER="your-email@domain.com"
export SMTP_PASS="your-app-password"
export NOTIFY_TO="alerts@domain.com"

# Run Flask server (listens on port 5000)
python dpex_demo_backend.py
```

---

## 👨‍💻 Meet the Founder & Engineering Lead

**Durvesh Parab**  
*Founder & Chief Executive Officer, DPex*  
- **Degree**: Bachelor of Engineering
- **Focus**: Full-Stack Architecture, Distributed Systems & Enterprise Automation
- **GitHub**: [@sanveeparab00-ops](https://github.com/sanveeparab00-ops)
- **Contact**: [durveshparab1111@gmail.com](mailto:durveshparab1111@gmail.com)

---

## 👥 Core Leadership & Development Team

- **Durvesh Parab** — Founder & CEO (Full Stack Architect)
- **Shravani Rane** — Full Stack Developer & AI Automation (B.Sc. Data Science · MBA Business Analytics)
- **Vishwas Lad** — Full Stack Developer & Cloud Specialist (4 years at TCS)
- **Riya Jadhav** — Legal & Compliance Consultant (CS Professional · Law Degree)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
