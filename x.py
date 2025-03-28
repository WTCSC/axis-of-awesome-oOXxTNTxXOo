import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

Ranked = [
["Magik, 2, 15:59, Convergence, Symboitic Surface, 9, 19273, 13, 0, 18, 26409, 0, 40.3, 4393, -21, 3/22/25, 1:03 pm, lost, no"],
["Magik, 3, 15:25, Convergence, Symbiotic Surface, 3, 13422, 15, 7, 12, 10142, 9,610, 28.7, 4414, -21, 3/21/25, 9:51 pm, lost, no"],
["Magik, 1, 17:21, Convoy, Spider-Islands, 19, 23494, 12, 0, 33, 15097, 0, 51.8, 4435, -22, 3/21/25, 9:30 pm, lost, no"],
["Magik, 1, 8:23, Domination, Royal Palace, 7, 9554, 6, 0, 15, 5425, 0, 51.9, 4456, +20, 3/21/25, 7:47 pm, win, no"],
["Magik, 3, 16:26, Convoy, Midtown, 14, 22470, 13, 6, 28, 38654, 0, 31.0, 4426, +23, 3/20/25, 10:52 pm, win, no"],
["Magik, 2, 7:52, Domination, Royal Palace, 8, 11692, 7, 0, 16, 8478, 0, 11.2, 4381, -16, 3/20/25, 4:33 pm, lost, svp"],
["Magik, 2, 10:13, Convergence, Shin-Shibuya, 11, 18931, 7, 10, 26, 7357, 0, 47.0, 4393, +26, 3/20/25, 3:23 pm, win, no"],
["Magik, 1, 5:36, Convergence, Central Park, 8, 8770, 3, 0, 13, 7142, 0, 60.6, 4366, +28, 3/19/25, 9:27 pm, win, no"],
["Magik, 1, 14:4, Convergence, Hall of Djalia, 26, 20163, 10, 0, 35, 16184, 0, 39.1, 4312, +26, 3/19/25, 7:44 pm, win, mvp"],
["Magik, 1, 6:10, Convoy, Midtown, 12, 12826, 3, 0, 18, 5926, 0, 51.0, 4286, +28, 3/19/25, 7:24 pm, win, mvp"],
["Magik, 2, 18:14, Convoy, Midtown, 15, 21773, 16, 15, 28, 15700, 6120, 40.6, 4257, +24, 3/19/25, 5:32 pm, win, no"],
["Magik, 1, 10:19, Convergence, Hall of Djalia, 12, 18929, 8, 0, 24, 10931, 0, 59.6, 4233, +25, 3/19/25, 5:03 pm, win, no"],
["Magik, 2, 15:34, Convergence, Shin-Shibuya, 17, 18511, 13, 0, 21, 11270, 0, 53.9, 4207, -20, 3/18/25, 6:27 pm, lost, no"],
["Magik, 1, 8:59, Domination, Hell's Heaven, 7, 9909, 8, 0, 9, 6474, 0, 50.4, 4240, -18, 3/18/25, 11:57 am, lost, no"],
["Magik, 1, 8:15, Domination, Birnin T'Challa, 5, 9717, 7, 0, 11, 5577, 0, 61.7, 4258, -19, 3/18/25, 11:43 am, lost, svp"],
["Magik, 1, 16:41, Convergence, Shin-Shibuya, 13, 20641, 12, 0, 29, 11097, 0, 44.8, 4297, +23, 3/17/25, 7:34 pm, win, no"],
["Magik, 1, 16:47, Convoy, Yggdrasill Path, 16, 35239, 10, 0, 32, 18734, 0, 52.3, 4273, -20, 3/17/25, 6:44 pm, lost, no"],
["Magik, 1, 10:8, Domination, Hell's Heaven, 11, 19920, 5, 0, 26, 7806, 0, 42.5, 4293, +23, 3/17/25, 6:21 pm, win, no"],
["Magik, 1, 8:19, Domination, Birnin T'Challa, 11, 13429, 5, 0, 13, 6920, 0, 51.2, 4269, -14, 3/17/25, 5:52 pm, lost, svp"],
["Magik, 1, 18:47, Convoy, Yggdrasill Path, 19, 36675, 16, 0, 39, 20314, 0, 59.4, 4283, +24, 3/17/25, 5:23 pm, win, no"],
["Magik, 3, 17:10, Convergence, Hall of Djalia, 10, 19624, 14, 1, 24, 24355, 0, 33.5, 4258, -21, 3/17/25, 2:05 pm, lost, no"],
["Magik, 1, 16:17, Convergence, Symbiotic Surface, 15, 23883, 11, 0, 25, 1319, 0, 57.8, 4279, 0, 3/17/25, 1:25 pm, win, no"],
["Magik, 3, 11:16, Convoy, Spider-Islands, 3, 11145, 12, 7, 16, 8835, 5576, 37.1, 4279, -22, 3/17/25, 1:02 pm, lost, no"],
["Magik, 2, 16:15, Convoy, Midtown, 4, 11139, 13, 17, 9, 13186, 19296, 25.6, 4277, -18, 3/17/25, 11:05 pm, lost, no"],
["Magik, 1, 13:56, Domination, Royal Palace, 16, 26995, 8, 0, 27, 12280, 0, 49.8, 4317, -20, 3/8/25, 4:27 pm, lost, svp"],
["Magik, 1, 10:44, Convergence, Shin-Shibuya, 12, 17594, 7, 0, 19, 8955, 0, 58.1, 4337, +24, 3/8/25, 4:08 pm, win, no"],
]

print(Ranked)