from logging import info
from flask import Flask,render_template,request
import requests


api_key = "8a35415abd9c397e8f3135fa2a818093"
url = "http://data.fixer.io/api/latest?access_key=" + api_key
app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")
        amount = request.form.get("amount")
        response = requests.get(url)
        app.logger.info(response)
        infos = response.json()
        app.logger.info(infos)
        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]
        result = (secondValue / firstValue) * float(amount)
        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result
        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)