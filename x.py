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

# Loop through each entry in the Ranked list and extract the data
# I chose to do it this way becuase I plann to come back later and use this as a frame for creatig a scanner that can extrat the data into a similar list in a txt file.
# For this reason I want this for loop to be able to read through the data and extract the data into a list that can be used to create a dataframe.
for x in Ranked:
   x = str(x).split(",")
   Character = x[0] # Character played/character we are tracking for
   Characters.append(Character) # Append the character to the list of characters
   NumberOfDifCharactersPlayed = x[1] # Number of different characters played
   CharactersPlayed.append(NumberOfDifCharactersPlayed) # Append the number of different characters played to the list of characters played
   MatcTime = x[2]  # Match time in m:s
   MatchTimes.append(MatcTime)  # Append the match time to the list of match times
   mode = x[3]  # Game mode
   GameModes.append(mode)  # Append the game mode to the list of game modes
   map_played = x[4]  # Map played    
   MapsPlayed.append(map_played)  # Append the map played to the list of maps played
   Actual_kills = x[5]  # keeps track of Kills/finalhits
   TotalKills.append(Actual_kills)  # Append the total kills to the list of total kills
   damage = x[6]  # total Damage dealt during the match
   TotalDamage.append(damage)  # Append the total damage to the list of total damage
   deaths = x[7]  # total Deaths that happend during the match
   TotalDeaths.append(deaths)  # Append the total deaths to the list of total deaths
   assist = x[8]  # total Assists that happened during the 
   TotalAssists.append(assist)  # Append the total assists to the list of total assists
   False_kills = x[9]  # this stat in the game is counted as kills: However its super inflated and lies to the players becuase it counts assists as kills.
   TotalFalseKills.append(False_kills)  # Append the total false kills to the list of total false kills
   blocked = x[10]  # total Damage blocked during the match
   TotalBlocked.append(blocked)  # Append the total blocked damage to the list of total blocked damage
   healing = x[11]  # total Healing done during the match
   TotalHealing.append(healing)  # Append the total healing to the list of total healing
   Accuracy = x[12]  # Accuracy of the character played
   TotalAccuracy.append(Accuracy)  # Append the accuracy to the list of total accuracy
   RankedPoints = x[13]  # total Ranked points you had as a player at the time
   RankedPointList.append(RankedPoints)  # Append the ranked points to the list of ranked points
   Points_gained = x[14]  # points gained/lost during the match
   PointsGainedorLost.append(Points_gained)  # Append the points gained/lost to the list of points gained/lost
   date = x[15]  # date of the match
   DateList.append(date)  # Append the date to the list of dates
   Day_time = x[16]  # time that the match took place
   DayTimeList.append(Day_time)  # Append the day time to the list of day times
   win_loss = x[17]  # win/loss of the match
   TotalWinLoss.append(win_loss)  # Append the win/loss to the list of win/loss
   mvp = x[18]  # if the player was mvp/svp or not
   TotalMVP.append(mvp)  # Append the mvp/svp to the list of mvp/svp

# something_data = {
#    "Total Damage": TotalDamage,
#    "Total Kills": TotalKills,
# }

# df = pd.DataFrame(something_data)  # Create a DataFrame from the data
# df["Total Kills"] = df["Total Kills"].astype(int)  # Convert the "Total Kills" column to integers
# df["Total Damage"] = df["Total Damage"].astype(int)  # Convert the "Total Damage" column to integers

# df = df.sort_values(by="Total Damage", ascending=False)  # Sort the DataFrame by "Total Damage" in descending orders

# for xi, yi in zip(df["Total Damage"], df["Total Kills"]):
#     plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center', color='black')

# plt.plot(df["Total Damage"], df["Total Kills"], marker='o', linestyle='-')  # Plot the data with markers and lines

# plt.xlabel("Total Kills")  # Set the x-axis label
# plt.ylabel("Damage Dealt")  # Set the y-axis label
# plt.title("Total Kills per character")  # Set the title of the plot
# plt.grid(True)  # Add a grid to the plot
# plt.show()

#--------
# something_data = {
#    "Total Damage": TotalDamage,
#    "Total Kills": TotalKills,
# }

# df = pd.DataFrame(something_data)  # Create a DataFrame from the data
# df["Total Kills"] = df["Total Kills"].astype(int)  # Convert the "Total Kills" column to integers

# df = df.sort_values(by="Total Kills")  # Sort the DataFrame by "Total Kills"

# plt.plot(df["Total Kills"], df["Total Damage"], marker='o', linestyle='-')  # Plot the data with markers and lines

# plt.xlabel("Total Kills")  # Set the x-axis label
# plt.ylabel("Damage Dealt")  # Set the y-axis label
# plt.title("Total Kills per character")  # Set the title of the plot
# plt.grid(True)  # Add a grid to the plot
# plt.show()


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
win_loss_mvp_counts = {k: v for k, v in win_loss_mvp_counts.items() if v < 0}

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