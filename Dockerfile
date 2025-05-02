FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install flask pandas scikit-learn

EXPOSE 8099

CMD ["python", "spam_detector.py"]
