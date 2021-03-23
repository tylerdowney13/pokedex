import sqlite3

# Create connection to database
conn = sqlite3.connect('pokedex.db')

# Create cursor
c = conn.cursor()

# Update Entry
# c.execute("""UPDATE pokedex SET
    name = "Chansey",
    type = "Normal",
    height = "1.1 m",
    weight = "34.6 kg",
    hp = "150",
    attack = "5",
    defense = "5",
    spatk = "35",
    spdef = "105",
    speed = "50",
    img = "113"

    WHERE rowid = 113
    """)

conn.commit()
conn.close()
