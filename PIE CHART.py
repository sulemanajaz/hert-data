# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 15:30:34 2023

@author: NCA-PC
"""

import matplotlib.pyplot as plt

# Data for CO2 emissions in 2020
labels = ['Low', 'Moderate', 'High']
sizes = [5, 45, 50]  # Example data, you should replace with actual data
colors = ['lightcoral', 'lightblue', 'lightgreen']
explode = (0, 0.1, 0)  # To emphasize a slice (e.g., 'Moderate')

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('CO2 Emissions Distribution in Pakistan (2020)')
plt.show()
