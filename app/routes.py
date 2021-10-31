from app import app
from flask import render_template, request
import exchange

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def calculte():
    result = [0, 0]
    if request.method == 'POST':
        if request.form['submit-button'] == 'CALCULATE':
            token1 = request.form['input-token1']
            token2 = request.form['input-token2']
            value = request.form['input-value']
            result = exchange.main(token1, token2, value, "sell")
    return render_template("result.html", result = result)

