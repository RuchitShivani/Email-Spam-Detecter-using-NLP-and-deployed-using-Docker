# 📧 Email Spam Detector using NLP and Deployed using Docker

This is a complete end-to-end **Spam Detection Web Application** built using **Natural Language Processing (NLP)** and **Machine Learning**, served through a Flask API and deployed using **Docker**. It allows users to input email-like messages and get real-time predictions on whether the message is spam or not.

---

## 🚀 Features

- 🧠 Trained on real-world SMS spam dataset
- 🧹 Text preprocessing and cleaning pipeline
- 🔤 TF-IDF vectorization for feature extraction
- 📊 Naive Bayes classifier for spam classification
- 🌐 REST API using Flask
- 🎨 Simple and responsive HTML + CSS frontend
- 🐳 Dockerized for platform-independent deployment

---

## 📁 Project Structure

Email-Spam-Detector/
├── static/
│ └── index.html # Frontend web UI
├── spam.csv # SMS spam dataset
├── app.py # Main Flask app with ML model
├── Dockerfile # Docker image configuration
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🧪 Technologies Used

- Python 3
- Pandas, Scikit-learn, Regex
- Flask (API Framework)
- HTML5, CSS3, JavaScript (Frontend)
- Docker

---

## 🛠️ How It Works

1. **Data Ingestion:** Loads a labeled dataset of SMS messages marked as 'ham' or 'spam'.
2. **Text Cleaning:** Converts text to lowercase, removes digits and special characters.
3. **Vectorization:** Transforms the cleaned text into TF-IDF vectors.
4. **Model Training:** Trains a `Multinomial Naive Bayes` classifier.
5. **Prediction API:** A RESTful `/predict` endpoint returns whether a message is spam.
6. **Frontend UI:** Accepts message input and displays prediction.
7. **Deployment:** Containerized using Docker for consistent deployment across platforms.
