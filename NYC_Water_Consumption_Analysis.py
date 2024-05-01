# DS-542
# Project 1
# Arvind Rambahal

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats

water_file_url = "https://data.cityofnewyork.us/resource/ia2d-e54m.csv"
water_data = pd.read_csv(water_file_url)

# Mean water consumption by decade

water_1980 = [0, 0]     # [sum, length]
water_1990 = [0, 0]
water_2000 = [0, 0]
water_2010 = [0, 0]
water_2020 = [0, 0]

# calculating the sum of water consumption for each decade
for index in range(1, len(water_data)):
    
    if(water_data["year"][index] >= 1980 and water_data["year"][index] < 1990):
        water_1980[0] += water_data["nyc_consumption_million_gallons_per_day"][index]
        water_1980[1] += 1
        
    elif(water_data["year"][index] >= 1990 and water_data["year"][index] < 2000):
        water_1990[0] += water_data["nyc_consumption_million_gallons_per_day"][index]
        water_1990[1] += 1
        
    elif(water_data["year"][index] >= 2000 and water_data["year"][index] < 2010):
        water_2000[0] += water_data["nyc_consumption_million_gallons_per_day"][index]
        water_2000[1] += 1
        
    elif(water_data["year"][index] >= 2010 and water_data["year"][index] < 2020):
        water_2010[0] += water_data["nyc_consumption_million_gallons_per_day"][index]
        water_2010[1] += 1
        
    elif(water_data["year"][index] >= 2020 and water_data["year"][index] < 2024):
        water_2020[0] += water_data["nyc_consumption_million_gallons_per_day"][index]
        water_2020[1] += 1
    else:
        pass

# calculating mean
mean_water_1980s = water_1980[0] / water_1980[1]
mean_water_1990s = water_1990[0] / water_1990[1]
mean_water_2000s = water_2000[0] / water_2000[1]
mean_water_2010s = water_2010[0] / water_2010[1]
mean_water_2020s = water_2020[0] / water_2020[1]

# display mean water consumtion for each decade
print("Mean Water Consumption: 1980s: " + str(mean_water_1980s))
print("Mean Water Consumption: 1990s: " + str(mean_water_1990s))
print("Mean Water Consumption: 2000s: " + str(mean_water_2000s))
print("Mean Water Consumption: 2010s: " + str(mean_water_2010s))
print("Mean Water Consumption: 2020s: " + str(mean_water_2020s))


print("") # new line

# What is median water consumption in the 1990s
water_consumption_1990s = list(water_data["nyc_consumption_million_gallons_per_day"][11:21])

median_water_1990s = stats.median(water_consumption_1990s)

print("Median Water Consumption in 1990s: " + str(median_water_1990s))

print("")

# For each year after 1979, did the water consumption per capita increase, decrease, or stay the same from the previous year?
#previous_capita = 0

for index1 in range(1, len(water_data)):
    
    if(water_data["per_capita_gallons_per_person_per_day"][index1] > water_data["per_capita_gallons_per_person_per_day"][index1 - 1]):
        print(str(water_data["year"][index1 - 1]) + " to " + str(water_data["year"][index1]) + ": Water Capita: Increase")
    
    elif(water_data["per_capita_gallons_per_person_per_day"][index1] < water_data["per_capita_gallons_per_person_per_day"][index1 - 1]):
        print(str(water_data["year"][index1 - 1]) + " to " + str(water_data["year"][index1]) + ": Water Capita: Decrease")
    
    else:
        print(str(water_data["year"][index1 - 1]) + " to " + str(water_data["year"][index1]) + ": Water Capita: Stayed the Same")

print("") # new line        
# What was the total cost per of water processing per decade?
# Cost = consumption in gallons * cost per gallon

processing_cost = {'1970s': 0.17, '1980s': 0.23, '1990s': 0.45, '2000s': 0.76, '2010s': 0.69, '2020s': 0.54}

total_consumption_cost = {
    "1970s": 0,
    "1980s": 0,
    "1990s": 0,
    "2000s": 0,
    "2010s": 0,
    "2020s": 0,
    }

for index3 in range(len(water_data)):
    
    if(water_data["year"][index3] == 1979):
        total_consumption_cost["1970s"] = water_data["nyc_consumption_million_gallons_per_day"][index3] * processing_cost.get("1970s")
    
    elif(water_data["year"][index3] >= 1980 and water_data["year"][index3] < 1990):
        total_consumption_cost["1980s"] += water_data["nyc_consumption_million_gallons_per_day"][index3] * processing_cost.get("1980s")
    
    elif(water_data["year"][index3] >= 1990 and water_data["year"][index3] < 2000):
        total_consumption_cost["1990s"] += water_data["nyc_consumption_million_gallons_per_day"][index3] * processing_cost.get("1990s")
        
    elif(water_data["year"][index3] >= 2000 and water_data["year"][index3] < 2010):
        total_consumption_cost["2000s"] += water_data["nyc_consumption_million_gallons_per_day"][index3] * processing_cost.get("2000s")
        
    elif(water_data["year"][index3] >= 2010 and water_data["year"][index3] < 2020):
        total_consumption_cost["2010s"] += water_data["nyc_consumption_million_gallons_per_day"][index3] * processing_cost.get("2010s")
        
    elif(water_data["year"][index3] >= 2020 and water_data["year"][index3] < 2024):
        total_consumption_cost["2020s"] += water_data["nyc_consumption_million_gallons_per_day"][index3] * processing_cost.get("2020s")

# print total cost for each decade
for key, value in total_consumption_cost.items():
    print("Total Cost for " + key + ": $" + str(value))
    

# Extra Credit
# Graph 1 - NYC Population Over Years
nyc_population = np.array(water_data["new_york_city_population"])
year = np.array(water_data["year"])

plt.plot(year, nyc_population)

plt.title("NYC Population Over the Years")
plt.ylabel("Population (in millions)")
plt.xlabel("Year")

plt.grid()
plt.show()

# Average water consumption in NYC over years
consumption_water_array = np.array(water_data["nyc_consumption_million_gallons_per_day"])
year1 = np.array(water_data["year"])

plt.plot(year1, consumption_water_array, color="green")

plt.title("NYC Water Consumption Over the Years")
plt.ylabel("Water Consumption (millions of gallons per day)")
plt.xlabel("Year")

plt.grid()
plt.show()