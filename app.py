from flask import Flask, render_template, request, jsonify
from email_utils import model_predict  # Ensure this import matches your module name
import sqlite3

app = Flask(__name__)

DATABASE = 'email_classification.db'

def save_to_database(email, prediction):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO results (email, prediction) VALUES (?, ?)', (email, prediction))
    conn.commit()
    conn.close()

def fetch_results():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT email, prediction FROM results')
    results = c.fetchall()
    conn.close()
    return results

@app.route("/", methods=['GET', 'POST'])
def home():
    prediction = None
    email = ""
    if request.method == 'POST':
        email = request.form.get('content')
        prediction = model_predict(email)
        save_to_database(email, 'Spam' if prediction == 1 else 'Not Spam')
    return render_template("index.html", prediction=prediction, email=email)

@app.route('/history')
def history():
    results = fetch_results()
    return render_template("history.html", results=results)

# Create an API endpoint
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    email = data['content']
    prediction = model_predict(email)
    save_to_database(email, 'Spam' if prediction == 1 else 'Not Spam')
    return jsonify({'prediction': prediction, 'email': email})  # Return prediction

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
