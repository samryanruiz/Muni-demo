import asyncio
import requests
from flask import Flask, jsonify, request, render_template

API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
headers = {"Authorization": "Bearer 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"}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
async def predict():
    text = request.form.get('input_text')
    data = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=data)
    results = response.json()
    results = results[0][0]
    label = results['label']
    score = results['score']
    rounded_score = round(score*100, 4)
    results['score'] = rounded_score
    await asyncio.sleep(0.1)

    return results

if __name__ == '__main__':
    app.run()
