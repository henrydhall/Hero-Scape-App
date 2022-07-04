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

## References
Learning SQL 3rd Edition - Beaulieu
SQLite 3 Built in Functions - https://www.sqlite.org/lang_corefunc.html
