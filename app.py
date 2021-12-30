from flask import Flask,jsonify,request
from classifier import get_prediction 
#giving the app name
app=Flask(__name__)
#changing the api from get to post and giving the route to the app
@app.route("/predict-alphabet",methods=["POST"])
#creating the function for predicting the data
def predict_data():
    image=request.files.get("alphabet")
    prediction=get_prediction(image)
    return jsonify({
        "prediction":prediction
    }),200
if __name__="__main__":
    app.run(debug=True)
    