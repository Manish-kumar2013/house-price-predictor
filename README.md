# 🏠 Smart Property Assistant - India

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-purple?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.17-blueviolet?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### 🌐 AI-Powered House Price Prediction for 6 Major Indian Cities

**Predict property prices instantly using Machine Learning!**

[🚀 Live Demo](https://house-price-predictor-7kbdrw3dvibthz99bxzmkg.streamlit.app/) • [📊 Features](#-features) •

</div>

---

## 🎯 About The Project

**Smart Property Assistant** is a comprehensive AI-powered web application that leverages Machine Learning to predict residential property prices across 6 major Indian metropolitan cities. The application analyzes 32,000+ property records to provide accurate price predictions, EMI calculations, and buy vs rent comparisons.

### 🌟 Why This Project?

- 🏘️ **Real-Estate Market Complexity**: Indian real estate is one of the largest sectors with complex pricing
- 🤖 **Data-Driven Decisions**: Move beyond subjective valuations to ML-based predictions
- 💡 **User-Friendly**: No technical knowledge required - just click and predict!
- 📱 **Accessible Anywhere**: Web-based, mobile-responsive, 24/7 available

---

## 🌐 Live Demo

### 🔗 **[Click Here to Try Live App](https://house-price-predictor-7kbdrw3dvibthz99bxzmkg.streamlit.app/)**

> No installation required! Just click the link and start predicting prices instantly.

---

## ✨ Features

### 🏙️ Multi-City Support
Predict prices for **6 major Indian cities**:
- 🌆 **Bangalore** - Silicon Valley of India
- 🏙️ **Mumbai** - Financial Capital  
- 🏛️ **Delhi** - National Capital
- 🌊 **Chennai** - Gateway to South India
- 💎 **Hyderabad** - IT Hub
- 🎭 **Kolkata** - Cultural Capital

### 🚀 7 Powerful Features

| Feature | Description |
|---------|-------------|
| 📊 **Home Dashboard** | Overview with KPIs and interactive charts |
| 🔮 **AI Price Predictor** | ML-based instant price predictions |
| 💳 **EMI Calculator** | Home loan EMI calculations with visual breakdown |
| 🏘️ **Buy vs Rent** | Financial comparison to make informed decisions |
| 🏆 **City Comparison** | Compare multiple cities side-by-side |
| 📈 **Market Insights** | Deep analytics for each city |
| ℹ️ **About Page** | Project information and tech stack |

---

## 📊 Model Performance

Our Machine Learning models achieved impressive accuracy across cities:

| City | R² Score | Status |
|------|----------|--------|
| 🥇 Hyderabad | **0.89** | Excellent |
| 🥈 Delhi | 0.61 | Good |
| 🥉 Bangalore | 0.58 | Good |
| Chennai | 0.58 | Good |
| Mumbai | 0.26 | Moderate |
| Kolkata | 0.04 | Needs Improvement |

**Best Model:** Random Forest Regressor with hyperparameter tuning

---

## 🛠️ Technology Stack

### Core Technologies

<table>
<tr>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="48" height="48" alt="Python" />
<br>Python
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="48" height="48" alt="Pandas" />
<br>Pandas
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="48" height="48" alt="NumPy" />
<br>NumPy
</td>
<td align="center" width="96">
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="48" height="48" alt="Scikit-Learn" />
<br>Scikit-Learn
</td>
<td align="center" width="96">
<img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" width="48" height="48" alt="Streamlit" />
<br>Streamlit
</td>
<td align="center" width="96">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="48" height="48" alt="GitHub" />
<br>GitHub
</td>
</tr>
</table>

### 📚 Libraries Used

- **Data Manipulation**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn (Random Forest, Decision Tree, Linear Regression)
- **Web Framework**: Streamlit
- **Model Serialization**: Pickle
- **Deployment**: GitHub + Streamlit Cloud

---

## 📊 Dataset Information

- **Source**: Kaggle - Housing Prices in Metropolitan Areas of India
- **Total Records**: 32,963 properties
- **Features**: 40 columns per property
- **Cities Covered**: 6 major Indian metropolitan cities

### City-wise Data Distribution

| City | Records | Percentage |
|------|---------|------------|
| Mumbai | 7,719 | 23.4% |
| Kolkata | 6,507 | 19.7% |
| Bangalore | 6,207 | 18.8% |
| Chennai | 5,014 | 15.2% |
| Delhi | 4,998 | 15.2% |
| Hyderabad | 2,518 | 7.6% |

### 🔑 Key Features

- **Numerical**: Price, Area (Sqft), BHK, Resale Status
- **Categorical**: Location, City
- **Amenities** (30+ Binary Features):
  - Gymnasium, Swimming Pool, Landscaped Gardens
  - Security, Power Backup, Parking, Lift
  - School, Hospital, Shopping Mall nearby
  - And many more...

---

## 🚀 Installation

### Prerequisites
- Python 3.12 or higher
- pip package manager

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/manishk48259-afk/house-price-predictor.git
   cd house-price-predictor
