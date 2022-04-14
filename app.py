from flask import Flask, request, render_template
from flask import json, jsonify
from sklearn import model_selection
from feature_extraction import CountVectorizer
from utils import normalize_text
from simple_naive_bayes import MultinomialNB

import pickle
import os


app = Flask(__name__)

transform = pickle.load(open("models/BOG.pkl", "rb"))
model = pickle.load(open("models/naive_bayes.pkl", "rb"))

def predict(text):
    text = normalize_text(text.strip())
    X = transform.transform([text])
    y_pred = model.predict(X)
    return y_pred[-1]


@app.route("/", methods=["GET", "POST"])
@app.route("/predict", methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        doc = request.form["document"]
        out = predict(doc)
        print(out)
        if out == 0:
            out = "sport"
        elif out == 1:
            out = "education"
        elif out == 2:
            out = "heathy"
        else:
            out = "finance"
        return render_template("index.html", document=doc, message=out.upper())
        


@app.route("/api", methods=["GET", "POST"])
def api():
    if request.method == "GET":
        message = {
            "message": "hello",
            "text": ""
        }
    else:
        doc = request.get_json()["text"]
        out = predict(doc)
        if out == 0:
            out = "sports"
        else:
            out = "education"
        message = {
            "message": out.upper(),
            "text": doc
        }
    return jsonify(message)


if __name__ == '__main__':
	app.run(host="localhost", port=8008, debug=True)