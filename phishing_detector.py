import streamlit as st
import pandas as pd
import numpy as np
import re
import nltk
import seaborn as sns
import matplotlib.pyplot as plt

from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

st.set_page_config(page_title="STAR PhishGuard AI Analyzer", layout="wide")

# NLTK SETUP
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# UI HEADER

st.title("📧 AI-Based Phishing Email Detection System")
st.subheader("Logistic Regression vs MLP Neural Network")

# TEXT CLEANING
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# LOAD DATASET
df = pd.read_csv("phishing_legit_dataset.csv")

text_col = df.columns[0]  # auto detect first column
df[text_col] = df[text_col].fillna("")
df['cleaned'] = df[text_col].apply(clean_text)


# DATASET METRICS
st.subheader("📁 Dataset Overview")

total = len(df)
phishing = df['label'].sum()
legit = total - phishing

st.write("Total Emails:", total)
st.write("Phishing Emails:", phishing)
st.write("Legitimate Emails:", legit)

# CLASS DISTRIBUTION GRAPH
st.subheader("📊 Class Distribution")

fig, ax = plt.subplots()
ax.bar(["Legitimate", "Phishing"], [legit, phishing])
ax.set_ylabel("Count")
st.pyplot(fig)

# TF-IDF
X = df['cleaned']
y = df['label']

tfidf = TfidfVectorizer(max_features=5000)
X_tfidf = tfidf.fit_transform(X)

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, y, test_size=0.2, random_state=42
)

st.subheader("📦 Dataset Split")

# FIXED ERROR HERE 👇
st.write("Training Samples:", X_train.shape[0])
st.write("Testing Samples:", X_test.shape[0])

# LOGISTIC REGRESSION

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)
lr_acc = accuracy_score(y_test, lr_pred)

# MLP MODEL
X_train_arr = X_train.toarray()
X_test_arr = X_test.toarray()

model = Sequential([
    Dense(128, activation='relu', input_dim=X_train_arr.shape[1]),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train_arr, y_train, epochs=5, batch_size=32, verbose=0)

ann_prob = model.predict(X_test_arr)
ann_pred = (ann_prob > 0.5).astype(int)

ann_acc = accuracy_score(y_test, ann_pred)

# SIDEBAR METRICS
st.sidebar.title("📊 Model Performance")

st.sidebar.metric("Logistic Regression Accuracy", round(lr_acc, 4))
st.sidebar.metric("MLP Accuracy", round(ann_acc, 4))

# ACCURACY TABLE
st.subheader("📈 Model Comparison")

metrics_df = pd.DataFrame({
    "Model": ["Logistic Regression", "MLP"],
    "Accuracy": [lr_acc, ann_acc]
})

st.table(metrics_df)


# ACCURACY GRAPH
fig, ax = plt.subplots()
ax.bar(metrics_df["Model"], metrics_df["Accuracy"])
ax.set_ylabel("Accuracy")
st.pyplot(fig)

# CONFUSION MATRIX LR
st.subheader("📊 Confusion Matrix (Logistic Regression)")

fig, ax = plt.subplots()
sns.heatmap(confusion_matrix(y_test, lr_pred), annot=True, fmt='d', ax=ax)
st.pyplot(fig)

# CONFUSION MATRIX MLP

st.subheader("📊 Confusion Matrix (MLP)")

fig, ax = plt.subplots()
sns.heatmap(confusion_matrix(y_test, ann_pred), annot=True, fmt='d', ax=ax)
st.pyplot(fig)

# RISK FUNCTION
def risk_level(prob):
    if prob <= 0.3:
        return "LOW 🟢"
    elif prob <= 0.7:
        return "MEDIUM 🟡"
    else:
        return "HIGH 🔴"

# PREDICTION SYSTEM
st.subheader("🔍 Test Your Email")

email = st.text_area("Enter email text here:")

if st.button("Predict"):

    cleaned = clean_text(email)
    vector = tfidf.transform([cleaned])

    # Logistic Regression
    lr_result = lr.predict(vector)[0]
    lr_conf = lr.predict_proba(vector)[0][1]

    # MLP
    ann_conf = model.predict(vector.toarray())[0][0]
    ann_result = int(ann_conf > 0.5)

    st.write("### 🤖 Logistic Regression")
    st.write("Prediction:", "🚨 Phishing" if lr_result else "✅ Legitimate")
    st.write("Confidence:", lr_conf)
    st.write("Risk:", risk_level(lr_conf))

    st.write("### 🧠 MLP Neural Network")
    st.write("Prediction:", "🚨 Phishing" if ann_result else "✅ Legitimate")
    st.write("Confidence:", ann_conf)
    st.write("Risk:", risk_level(ann_conf))