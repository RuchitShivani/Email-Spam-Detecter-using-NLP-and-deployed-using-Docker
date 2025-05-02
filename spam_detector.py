import pandas as pd
import re
from flask import Flask, request, jsonify, send_from_directory
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

# Load dataset
df = pd.read_csv('spam.csv', encoding='ISO-8859-1', usecols=['v1', 'v2'])
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df['cleaned'] = df['message'].apply(clean_text)

# Feature extraction
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(df['cleaned'])
y = df['label']

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
model = MultinomialNB()
model.fit(X_train, y_train)

# Flask app
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get('email_text', '')
    cleaned = clean_text(message)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    result = "Spam ❌" if prediction == 1 else "Ham ✅"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8099)
