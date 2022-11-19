import pickle
from flask import Flask , request, render_template
from math import ceil
app = Flask(__name__)
model = pickle.load(open("IBMDT.pkl","rb"))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def admin():
    Com = request.form["com"]
    Rank = request.form["rank"]
    ComRank = request.form["comr"]
    CutOff = request.form["co"]
    
    preds=[[Com,Rank,ComRank,CutOff]]
    xx=model.predict(preds)
    if (xx == 1):
        return render_template("chance.html")
    return render_template("nochance.html")
if __name__ == '__main__':
    app.run(debug = False, port=4000)