import sqlite3

# Create connection to database
conn = sqlite3.connect('pokedex.db')

# Create cursor
c = conn.cursor()

# Update Entry
# c.execute("""UPDATE pokedex SET
    name = "Magmar",
    type = "Fire",
    height = "1.3 m",
    weight = "44.5 kg",
    hp = "65",
    attack = "95",
    defense = "57",
    spatk = "100",
    spdef = "85",
    speed = "93",
    img = "126"

    WHERE rowid = 126
    """)

conn.commit()
conn.close()
