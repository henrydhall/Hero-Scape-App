# Hero-Scape-App
App to access Hero Scape cards more easily than looking through cards. 

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

## Seeding
