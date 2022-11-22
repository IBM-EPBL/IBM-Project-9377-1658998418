import pickle
from flask import Flask , request, render_template
from math import ceil
import requests

app = Flask(__name__)
#model = pickle.load(open("IBMDT.pkl","rb"))

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def admin():
    Com = request.form["com"]
    Rank = request.form["rank"]
    ComRank = request.form["comr"]
    CutOff = request.form["co"]
    
    #preds=[[Com,Rank,ComRank,CutOff]]
    #xx=model.predict(preds)
	
    API_KEY = "ol1OfHga50TuuERb3SpiogZUo8O2-iMmAtehGzW6Fes3"
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"field": [["COMMUNITY","RANK","COM.RANK","AGGR MARK"]], "values": [[Com,Rank,ComRank,CutOff]]}]}

    response_scoring = requests.post('https://jp-tok.ml.cloud.ibm.com/ml/v4/deployments/afcd0e3a-e61f-4f67-b927-9e01f1ade078/predictions?version=2022-11-22', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})

    prediction = response_scoring.json()['predictions'][0]['values'][0][0]    
    if (prediction == 1):
        return render_template("chance.html")
    return render_template("nochance.html")
if __name__ == '__main__':
    app.run(debug = False, port=4000)