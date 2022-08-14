from re import template
import sqlite3
import py
import pyinputplus

def view_cards():
    print(read_cards())

def read_cards():
    """
    Read all cards in the database. 
    TODO: make it readable.
    """
    connection = sqlite3.connect('cards')
    results = None
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM all_cards;')
        results = cursor.fetchall()
    except sqlite3.Error:
        connection.rollback()
        raise
    else:
        connection.commit()
    finally:
        connection.close()
    return results

def add_card_console():
    # Get card stats
    card_name = pyinputplus.inputStr('Card name: ')
    card_template = pyinputplus.inputStr('Template: ')
    card_life = pyinputplus.inputInt('Life: ', greaterThan=0)
    card_movement = pyinputplus.inputInt('Move: ')
    card_range = pyinputplus.inputInt('Range: ')
    card_attack = pyinputplus.inputInt('Attack: ')
    card_defense = pyinputplus.inputInt('Defense: ')
    card_points = pyinputplus.inputInt('Points: ')
    card_powers = pyinputplus.inputStr('Powers/Description: ')
    card_species = pyinputplus.inputStr('Species: ')
    card_uniqueness = pyinputplus.inputChoice(['Hero','Squad'])
    if card_uniqueness == 'Squad':
        card_squad_number = pyinputplus.inputInt('Squad Number: ')
    else:
        card_squad_number = 'NULL'
    card_class = pyinputplus.inputStr("Class: ")
    card_personality = pyinputplus.inputStr('Personality: ')
    card_size_text = pyinputplus.inputStr('Size as word: ')
    card_size_int = pyinputplus.inputInt('Size as number: ')
    card_notes = pyinputplus.inputStr('Notes: ')

    # Add it to the database.
    connection = sqlite3.connect('cards')
    results = None
    try:
        cursor = connection.cursor()
        query_string = f'INSERT INTO all_cards (name, template, life, movement, ranged, attack, defense, points, powers, species, uniqueness, squad_number, class, personality, size_text, size_int, notes)    \
            VALUES    ( \"{card_name}\", \"{card_template}\", {card_life}, {card_movement}, {card_range}, {card_attack}, {card_defense}, {card_points}, \"{card_powers}\", \"{card_species}\", \"{card_uniqueness}\", {card_squad_number}, \"{card_class}\", \"{card_personality}\", \"{card_size_text}\", {card_size_int}, \"{card_notes}\");'
        cursor.execute(query_string)
    except sqlite3.Error:
        connection.rollback()
        raise
    else:
        connection.commit()
    finally:
        connection.close()

def add_many_cards():
    print('Adding many cards.')
    if input('Enter Q now to exit, enter anything else to continue: ') != 'Q':
        add_card_console()

def add_card(card_name, card_template, card_life, card_movement, card_range, card_attack, card_defense, \
        card_points, card_powers, card_species, card_uniqueness, card_squad_number, card_class, \
            card_personality, card_size_text, card_size_int, card_notes):
    # We have a ton of inputs, but we just need them.
    # TODO: verify inputs (either here or in the front end
    # TODO: consider SQL Injection attack?
    connection = sqlite3.connect('cards')
    try:
        cursor = connection.cursor()
        # Now we add them via this query string
        query_string = f'INSERT INTO all_cards (name, template, life, movement, ranged, attack, defense, points, powers, species, uniqueness, squad_number, class, personality, size_text, size_int, notes)    \
            VALUES    ( \"{card_name}\", \"{card_template}\", {card_life}, {card_movement}, {card_range}, {card_attack}, {card_defense}, {card_points}, \"{card_powers}\", \"{card_species}\", \"{card_uniqueness}\", {card_squad_number}, \"{card_class}\", \"{card_personality}\", \"{card_size_text}\", {card_size_int}, \"{card_notes}\");'
        print(query_string)
        cursor.execute(query_string)
    except sqlite3.Error:
        connection.rollback()
        raise
    else:
        connection.commit()
    finally:
        connection.close()
    pass

if __name__ == '__main__':
    add_many_cards()