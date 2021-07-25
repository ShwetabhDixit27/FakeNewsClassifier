from flask import Flask , render_template , request
from sklearn.linear_model import PassiveAggressiveClassifier
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
loaded_model = pickle.load(open('final.pickle', 'rb'))
loaded_vectorizer = pickle.load(open('vecfile.pickle', 'rb'))
app = Flask(__name__)

@app.route("/")
def home():
    #return "<p>Hello, World!</p>"
    return render_template('index.html')

@app.route("/predict",methods=["POST"])
def fake_news_det():
    message=""

    input=[request.form.get("experience")]
    input_data =loaded_vectorizer .transform(input)
    prediction = loaded_model.predict(input_data)
    k=prediction[0]
    if (k==0):
        message="This is a fake news"
    else:
        messgae="This is a real news"
    return render_template('index.html',text=message)


if __name__=="__main__":
    app.run(debug=True)
