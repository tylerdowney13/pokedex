from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# Create initial window
root = Tk()
root.title("Pokédex")
root.iconbitmap("pokeball.ico")
root.geometry("425x575")


# Stats bar function
def stats_bar(stat):
    global stats_bar_img
    if stat <= 25:
        stat_bar_img = "stats_bar_red.png"
    elif stat in range(25, 51):
        stat_bar_img = "stats_bar_orange.png"
    elif stat in range(51, 76):
        stat_bar_img = "stats_bar_yellow.png"
    elif stat in range(76, 101):
        stat_bar_img = "stats_bar_green.png"
    elif stat in range(101, 126):
        stat_bar_img = "stats_bar_teal.png"
    elif stat >= 126:
        stat_bar_img = "stats_bar_blue.png"
    return stat_bar_img


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
    image_box.grid(row=5, column=0, columnspan=3, pady=(10, 0))

    # Display stats
    # TYPE
    stats_type_label = Label(root, text=f"Type: {stats_type}")
    stats_type_label.grid(row=4, column=0, ipadx=10, pady=(10, 0), sticky="w")

    # HEIGHT
    stats_height_label = Label(root, text=f"Height: {stats_height}")
    stats_height_label.grid(row=4, column=1, ipadx=10, pady=(10, 0))

    # HEIGHT
    stats_weight_label = Label(root, text=f"Weight: {stats_weight}")
    stats_weight_label.grid(row=4, column=2, ipadx=10, pady=(10, 0), sticky="w")

    # HP
    stats_hp_label = Label(root, text=f"HP:         {stats_hp}")
    stats_hp_label.grid(row=6, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=6, column=1, pady=(10, 0), sticky="w")
    hp_value = int(stats_hp)
    hp_stat_bar_color = stats_bar(hp_value)
    hp_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{hp_stat_bar_color}").resize((hp_value, 20)))
    hp_stats_bar_pack = Label(root, image=hp_stats_bar)
    hp_stats_bar_pack.grid(row=6, column=1, pady=(10, 0), sticky="w")

    # ATK
    stats_attack_label = Label(root, text=f"ATK:       {stats_attack}")
    stats_attack_label.grid(row=7, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=7, column=1, pady=(10, 0), sticky="w")
    attack_value = int(stats_attack)
    attack_stat_bar_color = stats_bar(attack_value)
    attack_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{attack_stat_bar_color}").resize((attack_value, 20)))
    attack_stats_bar_pack = Label(root, image=attack_stats_bar)
    attack_stats_bar_pack.grid(row=7, column=1, pady=(10, 0), sticky="w")

    # DEF
    stats_defense_label = Label(root, text=f"DEF:       {stats_defense}")
    stats_defense_label.grid(row=8, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=8, column=1, pady=(10, 0), sticky="w")
    defense_value = int(stats_defense)
    defense_stat_bar_color = stats_bar(defense_value)
    defense_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{defense_stat_bar_color}").resize((attack_value, 20)))
    defense_stats_bar_pack = Label(root, image=defense_stats_bar)
    defense_stats_bar_pack.grid(row=8, column=1, pady=(10, 0), sticky="w")

    # SP-ATK
    stats_spatk_label = Label(root, text=f"SP-ATK: {stats_spatk}")
    stats_spatk_label.grid(row=9, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=9, column=1, pady=(10, 0), sticky="w")
    spatk_value = int(stats_spatk)
    spatk_stat_bar_color = stats_bar(spatk_value)
    spatk_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{spatk_stat_bar_color}").resize((spatk_value, 20)))
    spatk_stats_bar_pack = Label(root, image=spatk_stats_bar)
    spatk_stats_bar_pack.grid(row=9, column=1, pady=(10, 0), sticky="w")

    # SP-DEF
    stats_spdef_label = Label(root, text=f"SP-DEF: {stats_spdef}")
    stats_spdef_label.grid(row=10, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=10, column=1, pady=(10, 0), sticky="w")
    spdef_value = int(stats_spdef)
    spdef_stat_bar_color = stats_bar(spdef_value)
    spdef_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{spdef_stat_bar_color}").resize((spdef_value, 20)))
    spdef_stats_bar_pack = Label(root, image=spdef_stats_bar)
    spdef_stats_bar_pack.grid(row=10, column=1, pady=(10, 0), sticky="w")

    # SPEED
    stats_speed_label = Label(root, text=f"SPEED:   {stats_speed}")
    stats_speed_label.grid(row=11, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=11, column=1, pady=(10, 0), sticky="w")
    speed_value = int(stats_speed)
    speed_stat_bar_color = stats_bar(speed_value)
    speed_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{speed_stat_bar_color}").resize((speed_value, 20)))
    speed_stats_bar_pack = Label(root, image=speed_stats_bar)
    speed_stats_bar_pack.grid(row=11, column=1, pady=(10, 0), sticky="w")

    root.mainloop()


# SEARCH BY NAME FUNCTION
def search_by_name():
    # Get number
    name = name_box.get()
    # Create connection to database
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
    name_label_stats = Label(root, text=f"{stats_img}  {stats_name}")
    name_label_stats.grid(row=2, column=0, columnspan=3, ipadx=10, pady=(20, 0))

    # Create image box
    image1 = ImageTk.PhotoImage(Image.open(f"img/{stats_img}.jpg").resize((200, 200)))
    image_box = Label(root, image=image1)
    image_box.grid(row=5, column=0, columnspan=3, pady=(10, 0))

    # Display stats
    # TYPE
    stats_type_label = Label(root, text=f"Type: {stats_type}")
    stats_type_label.grid(row=4, column=0, ipadx=10, pady=(10, 0), sticky="w")

    # HEIGHT
    stats_height_label = Label(root, text=f"Height: {stats_height}")
    stats_height_label.grid(row=4, column=1, ipadx=10, pady=(10, 0))

    # HEIGHT
    stats_weight_label = Label(root, text=f"Weight: {stats_weight}")
    stats_weight_label.grid(row=4, column=2, ipadx=10, pady=(10, 0), sticky="w")

    # HP
    stats_hp_label = Label(root, text=f"HP:         {stats_hp}")
    stats_hp_label.grid(row=6, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=6, column=1, pady=(10, 0), sticky="w")
    hp_value = int(stats_hp)
    hp_stat_bar_color = stats_bar(hp_value)
    hp_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{hp_stat_bar_color}").resize((hp_value, 20)))
    hp_stats_bar_pack = Label(root, image=hp_stats_bar)
    hp_stats_bar_pack.grid(row=6, column=1, pady=(10, 0), sticky="w")

    # ATK
    stats_attack_label = Label(root, text=f"ATK:       {stats_attack}")
    stats_attack_label.grid(row=7, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=7, column=1, pady=(10, 0), sticky="w")
    attack_value = int(stats_attack)
    attack_stat_bar_color = stats_bar(attack_value)
    attack_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{attack_stat_bar_color}").resize((attack_value, 20)))
    attack_stats_bar_pack = Label(root, image=attack_stats_bar)
    attack_stats_bar_pack.grid(row=7, column=1, pady=(10, 0), sticky="w")

    # DEF
    stats_defense_label = Label(root, text=f"DEF:       {stats_defense}")
    stats_defense_label.grid(row=8, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=8, column=1, pady=(10, 0), sticky="w")
    defense_value = int(stats_defense)
    defense_stat_bar_color = stats_bar(defense_value)
    defense_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{defense_stat_bar_color}").resize((defense_value, 20)))
    defense_stats_bar_pack = Label(root, image=defense_stats_bar)
    defense_stats_bar_pack.grid(row=8, column=1, pady=(10, 0), sticky="w")

    # SP-ATK
    stats_spatk_label = Label(root, text=f"SP-ATK: {stats_spatk}")
    stats_spatk_label.grid(row=9, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=9, column=1, pady=(10, 0), sticky="w")
    spatk_value = int(stats_spatk)
    spatk_stat_bar_color = stats_bar(spatk_value)
    spatk_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{spatk_stat_bar_color}").resize((spatk_value, 20)))
    spatk_stats_bar_pack = Label(root, image=spatk_stats_bar)
    spatk_stats_bar_pack.grid(row=9, column=1, pady=(10, 0), sticky="w")

    # SP-DEF
    stats_spdef_label = Label(root, text=f"SP-DEF: {stats_spdef}")
    stats_spdef_label.grid(row=10, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=10, column=1, pady=(10, 0), sticky="w")
    spdef_value = int(stats_spdef)
    spdef_stat_bar_color = stats_bar(spdef_value)
    spdef_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{spdef_stat_bar_color}").resize((spdef_value, 20)))
    spdef_stats_bar_pack = Label(root, image=spdef_stats_bar)
    spdef_stats_bar_pack.grid(row=10, column=1, pady=(10, 0), sticky="w")

    # SPEED
    stats_speed_label = Label(root, text=f"SPEED:   {stats_speed}")
    stats_speed_label.grid(row=11, column=0, ipadx=10, pady=(10, 0), sticky="w")
    clear_stats_bar = ImageTk.PhotoImage(Image.open("statsbar/stats_bar_blank.png").resize((200, 20)))
    clear_stats_bar_pack = Label(root, image=clear_stats_bar)
    clear_stats_bar_pack.grid(row=11, column=1, pady=(10, 0), sticky="w")
    speed_value = int(stats_speed)
    speed_stat_bar_color = stats_bar(speed_value)
    speed_stats_bar = ImageTk.PhotoImage(Image.open(f"statsbar/{speed_stat_bar_color}").resize((speed_value, 20)))
    speed_stats_bar_pack = Label(root, image=speed_stats_bar)
    speed_stats_bar_pack.grid(row=11, column=1, pady=(10, 0), sticky="w")

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
