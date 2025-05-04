![Screenshot 2025-05-02 032332](https://github.com/user-attachments/assets/3297cc45-ea7f-4e4c-875f-8c617621d8c5)# 📧 Email Spam Detector using NLP and Deployed using Docker

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
5. **Prediction API:**
A RESTful `/predict` endpoint returns whether a message is spam.
6. **Frontend UI:** Accepts message input and displays prediction.
7. **Deployment:** Containerized using Docker for consistent deployment across platforms.

## Screenshots

![Screenshot 2025-05-02 034232](https://github.com/user-attachments/assets/7ca8ea1c-2b9a-4d77-8749-3bc00c5a6cc0)
![Screenshot 2025-05-02 033709](https://github.com/user-attachments/assets/be43556c-faad-48f8-8cd8-ae54bc7adb24)
![Screenshot 2025-05-02 032405](https://github.com/user-attachments/assets/ee7d6d68-6403-455e-8e35-370725742f62)
![Screenshot 2025-05-02 032332](https://github.com/user-attachments/assets/e02e54a9-ef2f-465b-95bd-3ea20983c9e0)

![download (5)](https://github.com/user-attachments/assets/79a95e9f-4e55-492f-950a-ad60d44853bf)
![download (7)](https://github.com/user-attachments/assets/96a18aa0-2974-40b6-be47-dd5cb337692b)
![download (6)](https://github.com/user-attachments/assets/5b7742c6-8e15-46ae-9e33-987147abdca2)
![download (4)](https://github.com/user-attachments/assets/cb59ba1d-0ade-43f9-8b51-d2ddf117b6dc)

