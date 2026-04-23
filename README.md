# Spam SMS Detector

A machine learning web application that classifies text messages as either Spam or Ham.
COLLAB LINK: https://colab.research.google.com/drive/1ldwYSgxznRepdRQpUNudnzLRShaE1dGN?usp=sharing

## Setup
1. Ensure Python is installed.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install flask joblib scikit-learn
   ```

## Files
- app.py: Flask backend handling requests and model prediction.
- spam_model.pkl: Trained machine learning model.
- vectorizer.pkl: TfidfVectorizer for text processing.
- templates/index.html: Frontend interface.
- static/style.css: Application styling.

## How to Run
1. Navigate to the project directory.
2. Start the server:
   ```bash
   flask run
   ```
3. Open http://127.0.0.1:5000 in your browser.

## Usage
Paste any text message into the input field and click Analyze. The result will display as either SPAM or HAM.
