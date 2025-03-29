import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

#Character, NumberOfDifCharactersPlayed, MatcTime/m:s, mode, map, Kills/finalhits, damage, deaths, assist, "kills", blocked, healing, Accuracy, RankedPoints, loss/gain, date(date and time), win/loss, mvp
Ranked = [
"Magik, 2, 15:59, Convergence, Symboitic Surface, 9, 19273, 13, 0, 18, 26409, 0, 40.3, 4393, -21, 3/22/25, 1:03 pm, lost, no",
"Magik, 3, 15:25, Convergence, Symbiotic Surface, 3, 13422, 15, 7, 12, 10142, 9610, 28.7, 4414, -21, 3/21/25, 9:51 pm, lost, no",
"Magik, 1, 17:21, Convoy, Spider-Islands, 19, 23494, 12, 0, 33, 15097, 0, 51.8, 4435, -22, 3/21/25, 9:30 pm, lost, no",
"Magik, 1, 8:23, Domination, Royal Palace, 7, 9554, 6, 0, 15, 5425, 0, 51.9, 4456, +20, 3/21/25, 7:47 pm, win, no",
"Magik, 3, 16:26, Convoy, Midtown, 14, 22470, 13, 6, 28, 38654, 0, 31.0, 4426, +23, 3/20/25, 10:52 pm, win, no",
"Magik, 2, 7:52, Domination, Royal Palace, 8, 11692, 7, 0, 16, 8478, 0, 11.2, 4381, -16, 3/20/25, 4:33 pm, lost, svp",
"Magik, 2, 10:13, Convergence, Shin-Shibuya, 11, 18931, 7, 10, 26, 7357, 0, 47.0, 4393, +26, 3/20/25, 3:23 pm, win, no",
"Magik, 1, 5:36, Convergence, Central Park, 8, 8770, 3, 0, 13, 7142, 0, 60.6, 4366, +28, 3/19/25, 9:27 pm, win, no",
"Magik, 1, 14:4, Convergence, Hall of Djalia, 26, 20163, 10, 0, 35, 16184, 0, 39.1, 4312, +26, 3/19/25, 7:44 pm, win, mvp",
"Magik, 1, 6:10, Convoy, Midtown, 12, 12826, 3, 0, 18, 5926, 0, 51.0, 4286, +28, 3/19/25, 7:24 pm, win, mvp",
"Magik, 2, 18:14, Convoy, Midtown, 15, 21773, 16, 15, 28, 15700, 6120, 40.6, 4257, +24, 3/19/25, 5:32 pm, win, no",
"Magik, 1, 10:19, Convergence, Hall of Djalia, 12, 18929, 8, 0, 24, 10931, 0, 59.6, 4233, +25, 3/19/25, 5:03 pm, win, no",
"Magik, 2, 15:34, Convergence, Shin-Shibuya, 17, 18511, 13, 0, 21, 11270, 0, 53.9, 4207, -20, 3/18/25, 6:27 pm, lost, no",
"Magik, 1, 8:59, Domination, Hell's Heaven, 7, 9909, 8, 0, 9, 6474, 0, 50.4, 4240, -18, 3/18/25, 11:57 am, lost, no",
"Magik, 1, 8:15, Domination, Birnin T'Challa, 5, 9717, 7, 0, 11, 5577, 0, 61.7, 4258, -19, 3/18/25, 11:43 am, lost, svp",
"Magik, 1, 16:41, Convergence, Shin-Shibuya, 13, 20641, 12, 0, 29, 11097, 0, 44.8, 4297, +23, 3/17/25, 7:34 pm, win, no",
"Magik, 1, 16:47, Convoy, Yggdrasill Path, 16, 35239, 10, 0, 32, 18734, 0, 52.3, 4273, -20, 3/17/25, 6:44 pm, lost, no",
"Magik, 1, 10:8, Domination, Hell's Heaven, 11, 19920, 5, 0, 26, 7806, 0, 42.5, 4293, +23, 3/17/25, 6:21 pm, win, no",
"Magik, 1, 8:19, Domination, Birnin T'Challa, 11, 13429, 5, 0, 13, 6920, 0, 51.2, 4269, -14, 3/17/25, 5:52 pm, lost, svp",
"Magik, 1, 18:47, Convoy, Yggdrasill Path, 19, 36675, 16, 0, 39, 20314, 0, 59.4, 4283, +24, 3/17/25, 5:23 pm, win, no",
"Magik, 3, 17:10, Convergence, Hall of Djalia, 10, 19624, 14, 1, 24, 24355, 0, 33.5, 4258, -21, 3/17/25, 2:05 pm, lost, no",
"Magik, 1, 16:17, Convergence, Symbiotic Surface, 15, 23883, 11, 0, 25, 1319, 0, 57.8, 4279, 0, 3/17/25, 1:25 pm, win, no",
"Magik, 3, 11:16, Convoy, Spider-Islands, 3, 11145, 12, 7, 16, 8835, 5576, 37.1, 4279, -22, 3/17/25, 1:02 pm, lost, no",
"Magik, 2, 16:15, Convoy, Midtown, 4, 11139, 13, 17, 9, 13186, 19296, 25.6, 4277, -18, 3/17/25, 11:05 pm, lost, no",
"Magik, 1, 13:56, Domination, Royal Palace, 16, 26995, 8, 0, 27, 12280, 0, 49.8, 4317, -20, 3/8/25, 4:27 pm, lost, svp",
"Magik, 1, 10:44, Convergence, Shin-Shibuya, 12, 17594, 7, 0, 19, 8955, 0, 58.1, 4337, +24, 3/8/25, 4:08 pm, win, no",
]

Characters = []  # List to store unique characters
CharactersPlayed = []  # List to store number of different characters played during a match
MatchTimes = []  # List to store match times
GameModes = []  # List to store game modes
MapsPlayed = []  # List to store maps played
TotalKills = []  # List to store total kills
TotalDamage = []  # List to store total damage dealt
TotalDeaths = []  # List to store total deaths
TotalAssists = []  # List to store total assists
TotalFalseKills = []  # List to store total false kills
TotalBlocked = []  # List to store total damage blocked
TotalHealing = []  # List to store total healing done
TotalAccuracy = []  # List to store accuracy
RankedPointList = []  # List to store ranked points
PointsGainedorLost = []  # List to store points gained/lost
DateList = []  # List to store dates
DayTimeList = []  # List to store day times
TotalWinLoss = []  # List to store win/loss
TotalMVP = []  # List to store MVP status

# Mapping indices to their respective lists
data_mapping = {
    0: Characters,
    1: CharactersPlayed,
    2: MatchTimes,
    3: GameModes,
    4: MapsPlayed,
    5: TotalKills,
    6: TotalDamage,
    7: TotalDeaths,
    8: TotalAssists,
    9: TotalFalseKills,
    10: TotalBlocked,
    11: TotalHealing,
    12: TotalAccuracy,
    13: RankedPointList,
    14: PointsGainedorLost,
    15: DateList,
    16: DayTimeList,
    17: TotalWinLoss,
    18: TotalMVP,
}

# Optimized loop
for entry in Ranked:
    values = str(entry).split(",")
    for index, value in enumerate(values):
        if index in data_mapping:
            data_mapping[index].append(value.strip())  # Append the value to the corresponding list

#--------
# Convert lists to appropriate data types
something_data = {
   "Total Damage": TotalDamage,
   "Total Kills": TotalKills,
}

df = pd.DataFrame(something_data)  # Create a DataFrame from the data
df["Total Kills"] = df["Total Kills"].astype(int)  # Convert the "Total Kills" column to integers
df["Total Damage"] = df["Total Damage"].astype(int)  # Convert the "Total Damage" column to integers

df = df.sort_values(by="Total Damage", ascending=False)  # Sort the DataFrame by "Total Damage" in descending orders

for xi, yi in zip(df["Total Damage"], df["Total Kills"]):
    plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center', color='black')

plt.plot(df["Total Damage"], df["Total Kills"], marker='o', linestyle='-')  # Plot the data with markers and lines

plt.xlabel("Total Kills")  # Set the x-axis label
plt.ylabel("Damage Dealt")  # Set the y-axis label
plt.title("Total Kills per character")  # Set the title of the plot
plt.grid(True)  # Add a grid to the plot
plt.show()

#--------
something_data = {
   "Total Damage": TotalDamage,
   "Total Kills": TotalKills,
}

df = pd.DataFrame(something_data)  # Create a DataFrame from the data
df["Total Kills"] = df["Total Kills"].astype(int)  # Convert the "Total Kills" column to integers

df = df.sort_values(by="Total Kills")  # Sort the DataFrame by "Total Kills"

plt.plot(df["Total Kills"], df["Total Damage"], marker='o', linestyle='-')  # Plot the data with markers and lines

plt.xlabel("Total Kills")  # Set the x-axis label
plt.ylabel("Damage Dealt")  # Set the y-axis label
plt.title("Total Kills per character")  # Set the title of the plot
plt.grid(True)  # Add a grid to the plot
plt.show()


#---------
# Normalize the data by stripping whitespace and converting to lowercase
normalized_win_loss = [win.strip().lower() for win in TotalWinLoss]
normalized_mvp = [mvp.strip().lower() for mvp in TotalMVP]

# Count occurrences of each combination of TotalWinLoss and mvp
win_loss_mvp_counts = {
    "Win & MVP": sum(1 for win, mvp in zip(normalized_win_loss, normalized_mvp) if win == "win" and mvp == "mvp"),
    "Win & No MVP": sum(1 for win, mvp in zip(normalized_win_loss, normalized_mvp) if win == "win" and mvp == "no"),
    "Loss & SVP": sum(1 for win, mvp in zip(normalized_win_loss, normalized_mvp) if win == "lost" and mvp == "svp"),
    "Loss & No MVP": sum(1 for win, mvp in zip(normalized_win_loss, normalized_mvp) if win == "lost" and mvp == "no"),
}

# Remove entries with zero counts
win_loss_mvp_counts = {k: v for k, v in win_loss_mvp_counts.items() if v > 0}

# Prepare data for the pie chart
labels = list(win_loss_mvp_counts.keys())
sizes = list(win_loss_mvp_counts.values())
colors = ["#4CAF50", "#FFC107", "#2196F3", "#F44336", "#FF9800", "#9C27B0"]  # Custom colors
explode = [0.1 if "MVP" in label else 0 for label in labels]  # Highlight MVP-related slices

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=colors, explode=explode)
plt.title("Comparison of TotalWinLoss to MVP Status")
plt.show()

#https://www.geeksforgeeks.org/plot-a-pie-chart-in-python-using-matplotlib/



#------- 
# Define valid combinations of GameModes and MapsPlayed
valid_combinations = {
    "Convergence": ["Symbiotic Surface", "Shin-Shibuya", "Hall of Djalia"],
    "Convoy": ["Midtown", "Yggdrasill Path", "Spider-Islands"],
    "Domination": ["Royal Palace", "Hell's Heaven", "Birnin T'Challa"]
}

# Manually combine GameModes and MapsPlayed based on valid combinations
game_mode_map = []
for mode, map_ in zip(GameModes, MapsPlayed):
    mode = mode.strip()
    map_ = map_.strip()
    if mode in valid_combinations and map_ in valid_combinations[mode]:
        game_mode_map.append(f"{mode} - {map_}")
    else:
        game_mode_map.append("Invalid Combination")  # Mark invalid combinations

# Filter out invalid combinations
filtered_game_mode_map = []
filtered_win_loss = []
for gmm, win in zip(game_mode_map, TotalWinLoss):
    if gmm != "Invalid Combination":
        filtered_game_mode_map.append(gmm)
        filtered_win_loss.append(1 if win.strip().lower() == "win" else 0)

# Create a DataFrame with valid combinations
data = pd.DataFrame({
    "GameMode_Map": filtered_game_mode_map,
    "Win": filtered_win_loss
})

# Group by GameMode_Map and calculate total wins and losses
total_wins = data.groupby("GameMode_Map")["Win"].sum()
total_losses = data.groupby("GameMode_Map")["Win"].count() - total_wins  # Total matches minus wins equals losses

# Combine wins and losses into a single DataFrame
win_loss_data = pd.DataFrame({
    "Wins": total_wins,
    "Losses": total_losses
})

# Group by GameMode_Map and calculate total wins and losses
total_wins = data.groupby("GameMode_Map")["Win"].sum()
total_matches = data.groupby("GameMode_Map")["Win"].count()
total_losses = total_matches - total_wins  # Total matches minus wins equals losses

# Calculate win percentage
win_percentage = (total_wins / total_matches * 100).clip(lower=0, upper=100)  # Cap at 100% and set lower bound to 0%

# Combine wins, losses, and win percentage into a single DataFrame
win_loss_data = pd.DataFrame({
    "Wins": total_wins,
    "Losses": total_losses,
    "Win Percentage": win_percentage
})

# Sort by total wins for better visualization
win_loss_data = win_loss_data.sort_values(by="Wins", ascending=False)

# Update x-tick labels to include win percentage
xtick_labels = [
    f"{index} ({int(row['Win Percentage'])}%)"
    for index, row in win_loss_data.iterrows()
]

# Plot the grouped bar graph
ax = win_loss_data[["Wins", "Losses"]].plot(
    kind="bar", figsize=(12, 6), color=["#4CAF50", "#F44336"], edgecolor="black"
)
plt.xlabel("Game Mode and Map", fontsize=12)
plt.ylabel("Total Matches", fontsize=12)
plt.title("Total Wins and Losses by Game Mode and Map", fontsize=14)
plt.xticks(ticks=range(len(xtick_labels)), labels=xtick_labels, rotation=45, ha="right", fontsize=10)
plt.legend(title="Result", labels=["Wins", "Losses"])
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()