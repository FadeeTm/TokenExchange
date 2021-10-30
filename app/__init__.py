from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import *

# https://flasktestblog1.herokuapp.com/
# https://habr.com/ru/post/346306/
# https://www.youtube.com/watch?v=jgAVGtkk03Q&list=PL0lO_mIqDDFXiIQYjLbncE9Lb6sx8elKA
# https://dashboard.heroku.com/apps
# https://getbootstrap.com/
# https://www.youtube.com/watch?v=tP09rxKbNMU&list=PLA0M1Bcd0w8yrxtwgqBvT6OM4HkOU3xYn&index=3 session - request

app = Flask(__name__)

db = SQLAlchemy(app)

from app.models import metadata

session = db.session


from app.controllers.excel_parser import mod_excel_parser
import app.controllers.api as api
app.register_blueprint(mod_excel_parser)
app.register_blueprint(api.company_module)
app.register_blueprint(api.country_module)


