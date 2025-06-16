import joblib
import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class IntentClassifier:
    def __init__(self):
        self.model_path = "./intent_model.pkl"
        self.vectorizer_path = "./vectorizer.pkl"
        self.data_path = "./robust_synthetic_intents.json"
        if os.path.exists(self.model_path) and os.path.exists(self.vectorizer_path):
            self.model = joblib.load(self.model_path)
            self.vectorizer = joblib.load(self.vectorizer_path)
        else:
            self.train()

    def train(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Dataset not found at {self.data_path}. Please generate it first.")

        with open(self.data_path, "r") as f:
            samples = json.load(f)

        texts, labels = zip(*samples)
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=3000)
        X = self.vectorizer.fit_transform(texts)
        self.model = LogisticRegression(max_iter=1000)
        self.model.fit(X, labels)

        joblib.dump(self.model, self.model_path)
        joblib.dump(self.vectorizer, self.vectorizer_path)
        print(f"Model trained and saved to: {self.model_path}, {self.vectorizer_path}")

    def predict(self, text):
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]
