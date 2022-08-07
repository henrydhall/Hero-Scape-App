from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import python_interface

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard string to guess'

bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    return render_template('index.html' )

@app.route('/cards')
def cards():
    cards = python_interface.read_cards()
    return render_template('cards.html', cards=cards)