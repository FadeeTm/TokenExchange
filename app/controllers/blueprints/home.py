from flask import Blueprint, render_template, request, redirect
from app import app, db
from app.models.article import Article


mod_home = Blueprint('home', __name__)


@mod_home.route('/')
@mod_home.route('/home')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
