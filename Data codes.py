# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:12:51 2023

@author: NCA-PC
"""

import matplotlib.pyplot as plt

# Data
years = [1990, 2000, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
co2_emissions = [0.511428117, 0.637262087, 0.710993637, 0.74061942, 0.778086203, 0.848207169, 0.918472672, 0.85042708, 0.824459652, 0.810360216]

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(years, co2_emissions, marker='o', label='CO2 Emissions (metric tons per capita)')
plt.title('CO2 Emissions Over Time in Pakistan')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (metric tons per capita)')
plt.legend()
plt.grid(True)
plt.show()
