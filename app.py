from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

model = pickle.load(open("mom.pkl","rb"))

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/mom" , methods = ["GET","POST"])
def mom():
    sl = float(request.form.get("sepal_length"))
    sw = float(request.form.get("sepal_width"))
    pl = float(request.form.get("petal_length"))
    pw = float(request.form.get("petal_width"))

    result = model.predict([[sl,sw,pl,pw]])
    outcome = result[0]
    if outcome == 0:
        return "akshay"
    elif outcome == 1:
        return "priya"
    else:
        return "ashwini"
    
if __name__=="__main__":
    app.run(debug=True,port=8080,host="0.0.0.0")