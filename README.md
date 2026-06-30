# 🎓 Proctor Management System

A robust, full-stack **Proctor Management System** built with **Django**, designed to streamline communication and coordination between students, proctors (teachers), and administrators. It features real-time chat communication via **Django Channels (WebSockets)**, role-based access control, an interactive dashboard, and automated email notifications.

---

## 📋 Table of Contents
1. [Features](#-features)
2. [Tech Stack](#-tech-stack)
3. [Project Structure](#-project-structure)
4. [Local Setup & Installation](#-local-setup--installation)
5. [Deployment Guide](#-deployment-guide)
6. [Security & Best Practices](#-security--best-practices)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 **Role-Based Authentication** | Custom user models with roles: **Admin**, **Teacher (Proctor)**, and **Student**. |
| 💬 **Real-time Chat** | Powered by **Django Channels** and WebSockets for instant student-proctor messaging. |
| 📅 **Meeting Scheduler** | Proctors can schedule meetings and coordinate timetables with assigned students. |
| 📧 **Automated Email Alerts** | Automated SMTP notifications for meeting schedules, attendance marking, and password resets. |
| 🔔 **Notification Center** | In-app unread notification counts and real-time alert updates. |
| 🎨 **Modern Responsive UI** | Built with **Bootstrap 5** and **FontAwesome** for a clean dashboard on mobile and desktop. |

---

## 🛠️ Tech Stack

* **Backend Framework:** Django 5.1
* **Asynchronous Communication:** Django Channels (WebSockets with InMemory Channel Layers)
* **API Support:** Django REST Framework
* **Styling & UI:** HTML5, CSS3, Bootstrap 5, FontAwesome
* **Database:** PostgreSQL (Production) / SQLite (Development)
* **Task/Server Runner:** Daphne (ASGI Server)

---

## 📁 Project Structure

```text
proctor_management/
├── accounts/          # User registration, custom roles (Student/Proctor/Admin)
├── teacher/           # Proctor dashboards, meeting setups, and attendance
├── student/           # Student dashboards and profile tracking
├── proctor/           # Core proctor assignment logic
├── chat/              # Real-time WebSocket chat consumers and routing
├── timetable/         # Schedule and event management
├── notifications/     # Notification creation and dispatching
├── templates/         # Global template layouts (Bootstrap 5)
├── staticfiles/       # Statically collected assets (CSS/JS)
├── manage.py          # Django management console
├── Procfile           # Production startup command for hosting platforms
└── requirements.txt   # Backend dependency checklist
```

---

## ⚙️ Local Setup & Installation

### Prerequisites
* Python 3.10+
* Git

### Step-by-Step Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/19Ankesh/proctor_management.git
   cd proctor_management
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations & Set Up Database:**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Admin Dashboard Access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Open **http://127.0.0.1:8000** in your browser.

---

## 🚀 Deployment Guide

This project is configured to deploy easily on **Render**, **Railway**, or **Heroku**.

### 1. Environment Variables Configured
Ensure the following variables are configured in your hosting dashboard:
* `SECRET_KEY`: A unique random security key.
* `DEBUG`: Set to `False` (production safety).
* `EMAIL_HOST_USER`: Your Gmail address.
* `EMAIL_HOST_PASSWORD`: Your 16-character Google App Password.

### 2. Startup Command
Since this project uses **WebSockets**, you must deploy using an ASGI server. The deployment command is pre-configured in the `Procfile`:
```bash
daphne -b 0.0.0.0 -p $PORT proctor_management.asgi:application
``

