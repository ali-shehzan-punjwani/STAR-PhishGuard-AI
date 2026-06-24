# STAR-PhishGuard-AI
AI-based phishing email detection system using Machine Learning (Logistic Regression) and Deep Learning (MLP Neural Network) with NLP preprocessing and Streamlit dashboard.

# 🛡️ STAR PhishGuard AI

### AI-Based Phishing Email Detection System (Machine Learning + Deep Learning)

🚀 **Live Demo:**https://star-phishguard-ai.streamlit.app/
📂 **Repository:** STAR-PhishGuard-AI

---

## 📌 Overview

STAR PhishGuard AI is an intelligent cybersecurity system designed to detect **phishing emails in real-time** using Natural Language Processing (NLP), Machine Learning, and Deep Learning techniques.

It classifies emails as:

* ✅ Legitimate
* 🚨 Phishing

The system is deployed as an interactive **Streamlit web application**, providing real-time predictions, confidence scores, risk levels, and performance analytics.

---

## 🎯 Key Features

* 🧠 AI-powered phishing detection
* ⚡ Real-time email classification
* 📊 Model comparison (ML vs DL)
* 🔍 TF-IDF based feature extraction
* 📉 Confusion matrix visualization
* 🚦 Risk level analysis (Low / Medium / High)
* 📈 Interactive Streamlit dashboard
* 🔐 Cybersecurity-focused NLP pipeline

---

## 🧠 Machine Learning Models

### 1. Logistic Regression (Baseline Model)

* Fast and efficient text classifier
* Works well with TF-IDF features
* High interpretability

### 2. Multilayer Perceptron (MLP Neural Network)

* Deep learning-based classifier
* Captures non-linear patterns
* Architecture:

  * Input: TF-IDF features
  * Hidden Layer 1: 128 neurons (ReLU)
  * Hidden Layer 2: 64 neurons (ReLU)
  * Output: Sigmoid activation

---

## 📊 Dataset

* 📁 Source: Kaggle Phishing Email Dataset
* 🔗 https://www.kaggle.com/datasets/kuladeep19/phishing-and-legitimate-emails-dataset

### Used Columns:

* Email body text
* Label (0 = Legitimate, 1 = Phishing)

---

## ⚙️ System Workflow

```
Email Input
   ↓
Text Cleaning (NLP)
   ↓
TF-IDF Vectorization
   ↓
ML Model (Logistic Regression / MLP)
   ↓
Prediction Output
   ↓
Risk Analysis Engine
   ↓
Streamlit Dashboard
```

---

## 📈 Performance Evaluation

The system evaluates models using:

* Accuracy
* Confusion Matrix
* Prediction Confidence

---

## 📊 Model Results

| Model               | Description              |
| ------------------- | ------------------------ |
| Logistic Regression | Fast baseline ML model   |
| MLP Neural Network  | Deep learning classifier |

---

## 🚦 Risk Classification

| Probability Score | Risk Level     |
| ----------------- | -------------- |
| ≤ 0.30            | 🟢 Low Risk    |
| 0.31 – 0.70       | 🟡 Medium Risk |
| > 0.70            | 🔴 High Risk   |

---

## 🖥️ Web Application

The system is deployed using **Streamlit**, allowing users to:

* Paste email content
* Get instant phishing prediction
* View confidence score
* Analyze risk level
* Compare ML vs DL outputs

---

## 🚀 Live Deployment

👉 Try the live app here:
https://your-streamlit-app-link-here

---

## 🛠️ Technologies Used

* Python 🐍
* Streamlit ⚡
* Scikit-learn 🤖
* TensorFlow / Keras 🧠
* NLTK 📝
* Pandas 📊
* NumPy 🔢
* Matplotlib 📉
* Seaborn 📈

---

## 📁 Project Structure

```
STAR-PhishGuard-AI/
│
├── app.py
├── phishing_legit_dataset.csv
├── requirements.txt
├── README.md
├── LICENSE
```

---

## 🔮 Future Enhancements

* Integration with Gmail / Outlook APIs
* Transformer-based models (BERT / RoBERTa)
* Cloud deployment (AWS / Azure)
* Explainable AI (XAI) for predictions
* Full SOC integration with SIEM tools (Wazuh / Splunk)

---

## 👨‍💻 Authors

* **Ali Shehzan Punjwani** (67158)

---

---

📫 Contact Ali Shehzan Punjwani 
📍 Karachi, Pakistan 
📧 shehzansohail5637@gmail.com
🔗 https://www.linkedin.com/in/ali-shehzan-punjwani/

---


## 📜 License

This project is licensed under the MIT License — free to use for educational and research purposes.

---

