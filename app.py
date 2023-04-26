import asyncio
import requests
from flask import Flask, jsonify, request, render_template

API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
headers = {"Authorization": "Bearer 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"}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/classifier')
def classifier():
    return render_template("classifierPage.html")

@app.route('/classifier/predict', methods=['POST'])
async def predict():
    text = request.form.get('input_text')
    data = {"inputs": text}
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        results = response.json()
    except:
        print("Entry is empty")
    results = results[0][0]
    label = results['label']
    score = results['score']
    rounded_score = round(score*100)
    results['score'] = rounded_score
    await asyncio.sleep(0.1)
    print(label, score)
    return results

@app.route('/anger')
def anger():
    score = request.args.get('score')
    return render_template("anger.html", score=score)

@app.route('/disgust')
def disgust():
    score = request.args.get('score')
    return render_template("disgust.html", score=score)

@app.route('/fear')
def fear():
    score = request.args.get('score')
    return render_template("fear.html", score=score)

@app.route('/joy')
def joy():
    score = request.args.get('score')
    return render_template("joy.html", score=score)

@app.route('/neutral')
def neutral():
    score = request.args.get('score')
    return render_template("neutral.html", score=score)

@app.route('/sadness')
def sadness():
    score = request.args.get('score')
    return render_template("sadness.html", score=score)

@app.route('/surprise')
def surprise():
    score = request.args.get('score')
    return render_template("surprise.html", score=score)

if __name__ == '__main__':
    app.run()
