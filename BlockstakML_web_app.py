import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

# Initialization of the flask App
app = Flask(__name__)

# Loading the trained model
model = joblib.load(open('E:/Decision_classifier_bank_model.joblib', 'rb'))

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # UI rendering the results
    # Retrieving values from a form
    init_features = [float(x) for x in request.form.values()]
    final_features = [np.array(init_features)]

    # Making a prediction
    prediction = model.predict(final_features)

    # Rendering the predicted result
    return render_template('index.html', prediction_text='Predicted deposit status: {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)