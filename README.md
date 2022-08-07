# Hero-Scape-App
App to access Hero Scape cards more easily than looking through cards. 

## Python Interface
We need a python interface to work with the sqlite3 database I've made, using sql queries. The initial program I've made will really only allow you to enter new cards, and maybe we'll move on from there later.

## Cards Table
* Name: SMALLTEXT
* Template: SMALLTEXT

* Life: SMALLINT
* Move: SMALLINT
* Range: SMALLINT
* Attack: SMALLINT
* Defense: SMALLINT
* Points: SMALLINT


* Powers: Text


* Species: "Dragon", "Human", "Alien", etc. ENUM?
* Uniqueness: ENUM: "Unique Hero", "Squad"
* Squad Number: if "Unique Hero", 1, else >1.
* Class: "Agent", whatever ***
* Personality: "Tricky", ***
* Size_text: SMALLTEXT (probably, depends on char library) ENUM?
* Size_int again: SMALLINT: 1-whatever it is. Need to figure out good names for the two sizes (word, number)

Additional Columns
* Card jpg:
* Figure jpg:
* Notes: SMALLTEXT
* RowID: primary key

## Initializing
Use the sqlite3 command line by running the setup.sh bash file. This will create the database. And seed it with three cards.

## Web App
I decided not to use SQL-Alchemy or whatever because I had already built a python interface that I like, and I don't feel comfortable with SQL-Alchemy's migration management yet.

### Start
I started just by stealing some code from flasky, and expanding from there. I won't be worrying about users or anything until I actually try to deploy it, and I don't know that I ever will so this might just stay as proof of concept. 

### Displaying Cards
First I need to find a good way to display cards. I made a cards tab in the menu, so we'll go from there. I started reading up on how to make cool tables, and then got overwhelmed, but I'll start at the most basic level haha. TODO: finish adding headings and content.

## References
* Learning SQL 3rd Edition - Beaulieu
* SQLite 3 Built in Functions - https://www.sqlite.org/lang_corefunc.html
* Flask Web Development 2nd Edition - Grinberg
* Beautiful Interactive Tables for your Flask Templates - https://blog.miguelgrinberg.com/post/beautiful-interactive-tables-for-your-flask-templates