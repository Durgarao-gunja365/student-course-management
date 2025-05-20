
# 🛠️ Django CI/CD with Jenkins, Docker, Prometheus & Grafana

This project demonstrates a full DevOps pipeline: building and deploying a Django web application using Jenkins and Docker, and monitoring the application with Prometheus and Grafana.

---

## 📁 Project Structure

```
.
├── django_project/         # Your Django app
├── Dockerfile              # Container config for Django app
├── docker-compose.yml      # Orchestrates Django, Prometheus, Grafana
├── requirements.txt        # Python dependencies
├── prometheus.yml          # Prometheus scrape config
├── Jenkinsfile             # Jenkins pipeline script
```

---

## 🚀 Features Implemented

- Django web application
- Dockerized using custom `Dockerfile`
- CI/CD pipeline using Jenkins
- Docker image push to Docker Hub
- Real-time monitoring with Prometheus
- Beautiful Grafana dashboards
- Log management & metrics at `/metrics`

---

## ✅ Steps to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/Durgarao-gunja365/student-course-management.git
cd your-repo
```

### 2. Build Docker Image (optional step if running standalone)

```bash
docker build -t your-image-name .
```

### 3. Run with Docker Compose

```bash
docker-compose up --build
```

This will start:
- Django app on port `8000`
- Prometheus on port `9090`
- Grafana on port `3000`

### 4. Configure Prometheus

Ensure `prometheus.yml` contains the correct scrape target:

```yaml
static_configs:
  - targets: ['django:8000']
```

### 5. Access the Services

- Django App → http://localhost:8000
- Prometheus UI → http://localhost:9090
- Grafana UI → http://localhost:3000

> Default Grafana login: `admin / admin`

---

## ⚙️ Jenkins CI/CD Pipeline

- Pulls code from GitHub
- Builds Docker image of Django app
- Pushes image to Docker Hub
- Deploys container

`Jenkinsfile` handles all these steps.

---

## 📊 Monitoring

- Metrics exposed via `django-prometheus` on `/metrics`
- Prometheus scrapes these metrics
- Grafana displays performance dashboards

---

## 📷 Screenshots


---

## 📚 Tech Stack

- Django
- Docker
- Jenkins
- Prometheus
- Grafana
- Python
- GitHub

---

## 🤝 Contributions

PRs are welcome! For major changes, open an issue first to discuss what you'd like to change.
