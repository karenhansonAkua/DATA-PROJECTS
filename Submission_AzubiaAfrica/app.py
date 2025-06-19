from flask import Flask, request, jsonify
import pandas as pd
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the full pipeline (preprocessing + model)
with open('pipeline.pkl', 'rb') as f:
    model_pipeline = pickle.load(f)

@app.route('/')
def home():
    return 'API is running. Use POST /predict to send data.'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON input
        data = request.get_json()

        # Convert JSON to DataFrame
        df = pd.DataFrame([data])

        # Predict using the pipeline
        prediction = model_pipeline.predict_proba(df)[0, 1]  # Probability of "yes"

        # Return the result
        return jsonify({'subscription_probability': round(float(prediction), 4)})

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
