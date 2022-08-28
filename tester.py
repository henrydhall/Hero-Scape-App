# Basic flask libraries
from crypt import methods
from pickle import NONE
from pipes import Template
from weakref import ref
from flask import Flask, render_template, url_for

# Bootstrap
from flask_bootstrap import Bootstrap

# TODO: figure out what this is
from flask_moment import Moment

# Web forms stuff
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange

# Proprietary library
import python_interface

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard string to guess'

bootstrap = Bootstrap(app)

class Card_Form(FlaskForm):
    # A form to add cards to the database. 
    card_name = StringField("Card Name", validators=[DataRequired()])
    card_template = StringField("Template") 
    card_life = IntegerField('Life', validators=[DataRequired(), NumberRange(min=1)])
    card_movement = IntegerField('Move', validators=[DataRequired(), NumberRange(min=0)])
    card_range = IntegerField('Range', validators=[DataRequired(), NumberRange(min=0)])
    card_attack = IntegerField('Attack', validators=[DataRequired(), NumberRange(min=0)])
    card_defense = IntegerField('Defense', validators=[DataRequired(), NumberRange(min=0)])
    card_points = IntegerField('Points', validators=[DataRequired(), NumberRange(min=1)])
    card_powers = StringField('Powers/Descriptions')
    card_species = StringField('Species')
    card_uniqueness = BooleanField('Unique Hero')
    card_squad_number = IntegerField('Squad Number')
    card_class = StringField('Class')
    card_personality = StringField('Personality')
    card_size_text = StringField('Size as word')
    card_size_int = IntegerField('Size as number')
    card_notes = StringField('Notes')
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    return render_template('index.html' )

@app.route('/cards', defaults={'extended':False})
@app.route('/cards/<extended>')
def cards(extended):
    cards = python_interface.read_cards()
    urls = []
    for card in cards:
        urls.append( url_for( 'view_card', ref=card[0] ) )
    for i in range(len(cards)):
        new_card = list(cards[i])
        new_card.append(urls[i])
        cards[i] = new_card
    if not extended:
        return render_template('cards.html', cards=cards )
    else:
        return render_template('cards_extended.html', cards=cards )

@app.route('/new_card', methods = ['GET','POST'])
def add_card():
    form = Card_Form()
    card_name = None
    if form.validate_on_submit():
        card_name = form.card_name.data
        form.card_name.data = ''
        print(card_name)
        if form.card_uniqueness.data == True:
            card_uniqueness = 'Hero'
            card_squad_number = "NULL"
        else:
            card_uniqueness = 'Squad'
            card_squad_number = form.card_squad_number.data
        python_interface.add_card(card_name, form.card_template.data, form.card_life.data, \
            form.card_movement.data, form.card_range.data, form.card_attack.data, form.card_defense.data, \
            form.card_points.data, form.card_powers.data, form.card_species.data, card_uniqueness, \
            card_squad_number, form.card_class.data, form.card_personality.data, \
            form.card_size_text.data, form.card_size_int.data, form.card_notes.data)
    return render_template('new_card.html', form = form, card_name = card_name)

@app.route('/card/<ref>')
def view_card(ref):
    return render_template('card.html', card = python_interface.search_cards_by_key(ref)[0] )
