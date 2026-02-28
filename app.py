from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict():
    data = request.get_json(force=True)
    X = np.array([data["features"]])
    prediction = model.predict(X)[0]
    return jsonify({"prediction": int(prediction)})

app.run(host="0.0.0.0", port=8080)