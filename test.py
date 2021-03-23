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

print(stats_bar(45))
