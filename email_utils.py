import warnings
from sklearn.exceptions import InconsistentVersionWarning
import pickle

# Suppress InconsistentVersionWarning warnings
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

# Load the CountVectorizer and Classifier
cv = pickle.load(open("F:/Web Development/Email-Classification-using-FLask/models/cv.pkl", 'rb'))
clf = pickle.load(open("F:/Web Development/Email-Classification-using-FLask/models/clf.pkl", 'rb'))

def model_predict(email):
    if email == "":
        return ""
    tokenized_email = cv.transform([email])  # Transform the email using CountVectorizer
    prediction = clf.predict(tokenized_email)  # Predict using the classifier
    prediction = 1 if prediction == 1 else -1  # If the email is spam, prediction should be 1
    return prediction
