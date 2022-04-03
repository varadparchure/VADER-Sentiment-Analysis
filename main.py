
from email import message
from turtle import home
from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def main():

    if request.method == 'POST':
        inp= request.form.get('inp')
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)

        neutral=score['neu']*100
        nu=score['neg']*100
        po=score['pos']*100
        
        if score["compound"] <= -0.05:
            return render_template('home.html', message="Negative",pos=po, neu=nu, nut=neutral)
            
        elif score["compound"] >= 0.05 :
            return render_template('home.html', message="Positive", pos=po, neu=nu,nut=neutral)
        else:
            return render_template('home.html', message="Neutral", pos=po, neu=nu,nut=neutral)



    return render_template("home.html")



