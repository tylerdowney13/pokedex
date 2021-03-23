from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# Create initial window
root = Tk()
root.title("Pokédex")
root.iconbitmap("pokeball.ico")
root.geometry("425x450")

name_label_stats = ""
# SEARCH BY NUMBER FUNCTION
def search_by_number():
    # Get number
    row_number = number_box.get()
    # Create connection to database
    conn = sqlite3.connect('pokedex.db')
    # Create cursor
    c = conn.cursor()
    # Query Database
    c.execute("SELECT * FROM pokedex WHERE rowid = " + row_number)
    # Assign data to a variable
    stats = c.fetchone()
    # Assign values to variable names
    stats_name = stats[0]
    stats_type = stats[1]
    stats_height = stats[2]
    stats_weight = stats[3]
    stats_hp = stats[4]
    stats_attack = stats[5]
    stats_defense = stats[6]
    stats_spatk = stats[7]
    stats_spdef = stats[8]
    stats_speed = stats[9]
    stats_img = stats[10]

    # Display name
    name_label_stats = Label(root, text=f"{stats_img}  {stats_name}")
    name_label_stats.grid(row=2, column=0, columnspan=3, ipadx=10, pady=(20, 0))

    # Create image box
    image1 = ImageTk.PhotoImage(Image.open(f"img/{stats_img}.jpg").resize((200, 200)))
    image_box = Label(root, image=image1)
    image_box.grid(row=4, column=0, columnspan=3, pady=(10, 0))

    # Display stats
    # TYPE
    stats_type_label = Label(root, text=f"Type: {stats_type}")
    stats_type_label.grid(row=5, column=0, ipadx=10, pady=(10, 0), sticky="w")

    # HEIGHT
    stats_height_label = Label(root, text=f"Height: {stats_height}")
    stats_height_label.grid(row=6, column=0, ipadx=10, pady=(10, 0), sticky="w")

    # HEIGHT
    stats_weight_label = Label(root, text=f"Weight: {stats_weight}")
    stats_weight_label.grid(row=7, column=0, ipadx=10, pady=(10, 0), sticky="w")

    # HP
    stats_hp_label = Label(root, text=f"HP:  {stats_hp}")
    stats_hp_label.grid(row=5, column=1, ipadx=10, pady=(10, 0))

    # ATK
    stats_attack_label = Label(root, text=f"ATK: {stats_attack}")
    stats_attack_label.grid(row=6, column=1, ipadx=10, pady=(10, 0))

    # DEF
    stats_defense_label = Label(root, text=f"DEF: {stats_defense}")
    stats_defense_label.grid(row=7, column=1, ipadx=10, pady=(10, 0))

    # SP-ATK
    stats_spatk_label = Label(root, text=f"SP-ATK: {stats_spatk}")
    stats_spatk_label.grid(row=5, column=2, ipadx=10, pady=(10, 0), sticky="w")

    # SP-DEF
    stats_spdef_label = Label(root, text=f"SP-DEF: {stats_spdef}")
    stats_spdef_label.grid(row=6, column=2, ipadx=10, pady=(10, 0), sticky="w")

    # SPEED
    stats_speed_label = Label(root, text=f"SPEED:  {stats_speed}")
    stats_speed_label.grid(row=7, column=2, ipadx=10, pady=(10, 0), sticky="w")

    root.mainloop()


# SEARCH BY NAME FUNCTION
def search_by_name():
    # Get number
    name = name_box.get()
    # Create connection to database
    conn = sqlite3.connect('pokedex.db')
    # Create cursor
    c = conn.cursor()
    # Query Database
    c.execute(f"SELECT * FROM pokedex WHERE name = '{name}'")
    # Assign data to a variable
    stats = c.fetchone()
    # Assign values to variable names
    stats_name = stats[0]
    stats_type = stats[1]
    stats_height = stats[2]
    stats_weight = stats[3]
    stats_hp = stats[4]
    stats_attack = stats[5]
    stats_defense = stats[6]
    stats_spatk = stats[7]
    stats_spdef = stats[8]
    stats_speed = stats[9]
    stats_img = stats[10]

    # Display name
    name_label_stats = Label(root, text=f"{stats_name}")
    name_label_stats.grid(row=2, column=0, columnspan=3, ipadx=10, pady=(20, 0))

    # Create image box
    image1 = ImageTk.PhotoImage(Image.open(f"img/{stats_img}.jpg").resize((200, 200)))
    image_box = Label(root, image=image1)
    image_box.grid(row=4, column=0, columnspan=3, pady=(10, 0))

    # Display stats
    # TYPE
    stats_type_label = Label(root, text=f"Type: {stats_type}")
    stats_type_label.grid(row=5, column=0, ipadx=10, pady=(10, 0), sticky="w")

    # HEIGHT
    stats_height_label = Label(root, text=f"Height: {stats_height}")
    stats_height_label.grid(row=6, column=0, ipadx=10, pady=(10, 0), sticky="w")

    # HEIGHT
    stats_weight_label = Label(root, text=f"Weight: {stats_weight}")
    stats_weight_label.grid(row=7, column=0, ipadx=10, pady=(10, 0), sticky="w")

    # HP
    stats_hp_label = Label(root, text=f"HP:  {stats_hp}")
    stats_hp_label.grid(row=5, column=1, ipadx=10, pady=(10, 0))

    # ATK
    stats_attack_label = Label(root, text=f"ATK: {stats_attack}")
    stats_attack_label.grid(row=6, column=1, ipadx=10, pady=(10, 0))

    # DEF
    stats_defense_label = Label(root, text=f"DEF: {stats_defense}")
    stats_defense_label.grid(row=7, column=1, ipadx=10, pady=(10, 0))

    # SP-ATK
    stats_spatk_label = Label(root, text=f"SP-ATK: {stats_spatk}")
    stats_spatk_label.grid(row=5, column=2, ipadx=10, pady=(10, 0), sticky="w")

    # SP-DEF
    stats_spdef_label = Label(root, text=f"SP-DEF: {stats_spdef}")
    stats_spdef_label.grid(row=6, column=2, ipadx=10, pady=(10, 0), sticky="w")

    # SPEED
    stats_speed_label = Label(root, text=f"SPEED:  {stats_speed}")
    stats_speed_label.grid(row=7, column=2, ipadx=10, pady=(10, 0), sticky="w")

    root.mainloop()


# Create Entry Boxes
# Create text boxes
number_box = Entry(root, width=30)
number_box.grid(row=0, column=1, pady=(15, 0))

name_box = Entry(root, width=30)
name_box.grid(row=1, column=1, pady=(15, 0))

# Create text box labels
number_label = Label(root, text="Number")
number_label.grid(row=0, column=0, pady=(15, 0))

name_label = Label(root, text="Name")
name_label.grid(row=1, column=0, pady=(15, 0))

# Create buttons
search_number_button = Button(root, text="Search by Number", command=search_by_number)
search_number_button.grid(row=0, column=2, pady=(15, 0))

search_name_button = Button(root, text="Search by Name", padx=8, command=search_by_name)
search_name_button.grid(row=1, column=2, pady=(15, 0))



# Run startscreen mainloop
root.mainloop()
