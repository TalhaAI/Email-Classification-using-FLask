from flask import Flask, render_template, request, jsonify
from email_utils import model_predict  # Ensure this import matches your module name

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    prediction = None
    email = ""
    if request.method == 'POST':
        email = request.form.get('content')
        prediction = model_predict(email)
    return render_template("index.html", prediction=prediction, email=email)

# Create an API endpoint
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    email = data['content']
    prediction = model_predict(email)
    return jsonify({'prediction': prediction, 'email': email})  # Return prediction

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
