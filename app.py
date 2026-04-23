from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
import re

app = Flask(__name__)
app.secret_key = 'dev-secret-key-for-spam-detector'

#Load the ML files we donwloaded from Colab
model = joblib.load('spam_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_message = request.form['message']
        
        #Clean and vectorize the text
        cleaned_msg = clean_text(user_message)
        vectorized_msg = vectorizer.transform([cleaned_msg])
        
        #Predict using our loaded model
        prediction = model.predict(vectorized_msg)
        prediction_result = "SPAM" if prediction[0] == 1 else "HAM (Safe)"
        
        # Flash the result and redirect
        flash(prediction_result)
        return redirect(url_for('home'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)