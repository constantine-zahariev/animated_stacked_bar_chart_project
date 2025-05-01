import matplotlib.pyplot as plt
from stacked_bar import stacked_bar
from sort_dict import sort_dict
# Importing the dictionary with all the data
# File can be changed to only show countries closer in per capita consumption
from energy_sources_1 import country_sources_data

# List for the energy source categories
energy_sources = ["Coal", "Oil", "Gas",
                  "Nuclear power", "Hydropower",
                  "Wind", "Solar", "Other renewables"]

# Years list for the x-axis ticks
years = [y for y in range(1993, 2024)]

# Set number of years for which data is presented starting from 1993
time_years = 30

year = 1    # Counter variable

# A 'while' loop to continuously call the 'ordered_dict' and 'stacked_bar' functions
# which order the input dictionary and then plot the stacked bar chart on each iteration
while year <= time_years:
    print("Year: ", year)
    ordered_dict = sort_dict(country_sources_data, year)
    stacked_bar(ordered_dict)
    curr_year = str(years[year])
    plt.title(f"Energy Consumption Per Capita by source in {curr_year}",
               fontfamily="Jost", fontsize="16")
    plt.pause(0.6)
    year += 1

# Call functions one last time so that the animation stops at the last year (2023)
ordered_dict = sort_dict(country_sources_data, 30)
stacked_bar(ordered_dict)
plt.title("Energy Consumption Per Capita by source in 2023",
          fontfamily="Jost", fontsize="16")

plt.show()

