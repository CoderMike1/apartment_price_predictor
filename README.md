# 🏡 Apartment Price Predictor in Krakow

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?style=for-the-badge&logo=django)
![Docker](https://img.shields.io/badge/Docker-4.38.0-blue?style=for-the-badge&logo=docker)

## 📝 **Table of contents**
* [General info](#-general-info)
* [Setup](#-setup-and-run)
* [SCREENSHOTS](#-screenshots)
---
## 🚀 **General info**
- Predictions based on 1k+ offers in polish marketplace service 'OLX'
- App can be run as a container via Docker

---

## 📦 **Setup and run**

### 🔹 **1. Run docker container (recommended)**
```bash
docker login
docker pull mihas011/apartment_price_predictor
docker run -p 8080:8875 mihas011/apartment_price_predictor
```
**Then open http://localhost:8080**

### 🔹 **2. Run on your device**
```bash
git clone https://github.com/CoderMike1/apartment_price_predictor.git
cd apartment_price_predictor
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8877
```
**Then open http://localhost:8877**

---
## 📷 **Screenshots**
<p align="center">
  <img src="screenshots/screenshot1.png"  width="300" style="margin: 10px;">
  <img src="screenshots/screenshot2.png"  width="300" style="margin: 10px;">
  <img src="screenshots/screenshot3.png"  width="300" style="margin: 10px;">
</p>
