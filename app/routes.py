from app import app
from flask import render_template, request
import exchange

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def calculate():
    result = [0, 0]
    if request.method == 'POST':
        token1 = request.form['input-token1']
        token2 = request.form['input-token2']
        value = request.form['input-value']
        if request.form['submit-button'] == 'CALCULATE SELLING':
            result = exchange.main(token1, token2, value, "sell")
        elif request.form['submit-button'] == 'CALCULATE BUYING':
            result = exchange.main(token1, token2, value, "buy")
    request_data = request.form
    print(request_data)
    return render_template("result.html", result = result, form = request_data)


# @app.route('/', methods=["GET", "POST"])
# @app.route('/index', methods=["GET", "POST"])
# def buy():
#     result = [0, 0]
#     if request.method == 'POST':
#         if request.form['button-buy'] == '1':
#             token1 = request.form['input-token1']
#             token2 = request.form['input-token2']
#             value = request.form['input-value']
#             result = exchange.main(token1, token2, value, "buy")
#     return render_template("result.html", result = result)



# @app.route('/', methods=["GET", "POST"])
# @app.route('/index', methods=["GET", "POST"])
# def sell():
#     result = [0, 0]
#     if request.method == 'POST':
#         if request.form['button-sell'] == '1':
#             token1 = request.form['input-token1']
#             token2 = request.form['input-token2']
#             value = request.form['input-value']
#             result = exchange.main(token1, token2, value, "sell")
#     return render_template("result.html", result = result)
