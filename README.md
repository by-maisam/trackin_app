# Trackin — IT Asset Management & Compliance Platform

Trackin is a localized, high-fidelity IT Asset Management (ITAM) platform built with Flask, SQLAlchemy, and Tailwind CSS. The system allows administrative users to inventory corporate physical hardware and software subscriptions while providing a dual-gated view matrix for standard employees to inspect their assigned equipment parameters seamlessly.

---

## 🛠️ Core Technology Stack

* **Backend Engine:** Flask (Python 3.14+)
* **Database Layer:** SQLAlchemy ORM (Configured dynamically for SQLite/PostgreSQL)
* **Frontend Matrix:** Jinja2 HTML Templates styled natively via Tailwind CSS
* **Security Mechanics:** Session-bound route protection and cryptographic password hashing (Werkzeug)

---

## 📁 System Architecture Directory

```text
trackin_app/
├── app/
│   ├── auth/
│   │   ├── __init__.py
│   │   └── routes.py           # Handles Registration and Secure Login
│   ├── routes/
│   │   ├── __init__.py         # Registers Admin/Inventory Blueprint namespaces
│   │   ├── admin.py            # High-fidelity dashboard aggregations & item binding
│   │   └── inventory.py        # Baseline CRUD actions for hardware & licenses
│   ├── templates/
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html   # Role selection layout interface
│   │   ├── admin/
│   │   │   └── ui/
│   │   │       └── dashboard.html # Splitted Role UI Panel (Admin vs Employee)
│   │   ├── inventory/
│   │   │   ├── assets.html     # Hardware listing and modal entry matrix
│   │   │   └── licenses.html   # Software asset lookup table
│   │   └── base.html           # Core responsive global wrapper structure
│   ├── __init__.py             # Application Factory pipeline
│   └── models.py               # Database ORM classes (User, Asset, License)
├── venv/                       # Isolated Virtual Environment storage
├── config.py                   # Central environment & database URI handling
├── requirements.txt            # Component package dependency manifest
└── run.py                      # Local server boot orchestration entrypoint
