
# 🖥️ System Monitoring App (Flask + psutil)

A lightweight Dockerized monitoring web app built using **Flask** and **psutil**, providing real-time system metrics like CPU, memory, disk usage, and more. Designed to be easily deployed to **AWS EKS**.

## 🚀 Features

- Real-time CPU, memory, disk, and swap usage
- Network I/O and process count display
- System uptime
- Alerts for high CPU or memory usage
- Simple and clean web interface

## 🛠️ Built With

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [psutil](https://pypi.org/project/psutil/)
- [Docker](https://www.docker.com/)
- [AWS EKS](https://aws.amazon.com/eks/)

## 📸 Screenshot

![Monitoring Dashboard](A_clean_and_modern_2D_digital_illustration_serves_.png)

## 📂 Project Structure

```
.
├── app.py
├── requirements.txt
├── Dockerfile
├── templates
│   └── index.html
└── README.md
```

## 🧪 Local Development

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/monitoring-app.git
cd monitoring-app
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## 🐳 Docker

### Build the image:

```bash
docker build -t monitoring-app .
```

### Run the container:

```bash
docker run -d -p 5000:5000 monitoring-app
```

## ☁️ Deployment to AWS EKS (Simplified)

1. **Push image to Amazon ECR**
2. **Create EKS Cluster & Nodegroup via AWS Console**
3. **Deploy app using Kubernetes manifests (e.g., Deployment & Service)**

> *For full EKS setup and deployment steps, see [this article](https://medium.com/your-eks-guide).*

## 🧾 License

This project is open-source and available under the [MIT License](LICENSE).

## 🙌 Acknowledgements

- Powered by Flask and psutil
- Deployed on AWS EKS
