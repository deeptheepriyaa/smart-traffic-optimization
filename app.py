from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("traffic_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = model.predict([[data["vehicle_count"], data["average_speed"]]])[0]
    return jsonify({"congestion_level": prediction})

if __name__ == '__main__':
    app.run(debug=True)

