CREATE TABLE all_cards
    (
        id INTEGER PRIMARY KEY,
        name SMALLTEXT,
        template SMALLTEXT,
        
        life SMALLINT,
        movement SMALLINT,
        ranged SMALLINT,
        attack SMALLTEXT,
        defense SMALLINT,
        points SMALLINT,

        powers TEXT,

        species SMALLTEXT,
        uniqueness SMALLTEXT CHECK( uniqueness in ('Hero','Squad') ),
        squad_number SMALLINT,
        class SMALLTEXT,
        personality SMALLTEXT,
        size_text SMALLTEXT,
        size_int SMALLINT,

        notes SMALLTEXT
    );

INSERT INTO all_cards
    ( -- columns to insert data into
        name, template, life, movement, ranged, attack, defense, points, powers, species, uniqueness, squad_number, class, personality, size_text, size_int, notes
		)
    VALUES
    ( -- first row: values for the columns in the list above
        "Thanos", NULL, 6, 6, 6, 6, 7, 420, "Random stuff go.", "Eternal", "Hero", NULL, "Conqueror", "Nihilist", "Medium", 5, "Way OP: don't allow"
		),
    (
        "Airborne Elite", "Jandar", 1, 4, 8, 3, 2, 110, "Grenade stuff", "Human", "Squad", 4, "Soldiers", "Disciplined", "Medium", 5, "Freaking hilarious"
    );