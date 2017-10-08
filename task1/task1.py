#!/usr/bin/env python
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


file = pd.read_excel("data.xls").to_dict()

features = {"size": [], "rooms_amount": []}
target = {"price": []}

for i in file["Житлова площа"]:
    features["size"].append(float(str(file["Житлова площа"][i]).replace(",", ".")))

for i in file["Кімнат "]:
    features["rooms_amount"].append(int(file["Кімнат "][i]))

for i in file["Ціна "]:
    target["price"].append(float(file["Ціна "][i]))

plt.plot(features["size"], target["price"])