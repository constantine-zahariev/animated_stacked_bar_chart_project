# This script is nearly the same as 'stacked_bar' apart from changing the figure aspect ratio and left padding 

import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
from matplotlib.pyplot import style
from move_figure import move_figure

# One figure with one set of axes
fig, ax = plt.subplots(figsize=(9, 16))
# Adjust spacing
plt.subplots_adjust(left=0.15, right=0.9,
                    top=0.9, bottom=0.1,
                    wspace=0.4, hspace=0.4)

# Width of bars in chart
width = 1

energy_sources = ["Coal", "Oil", "Gas",
                  "Nuclear power", "Hydropower",
                  "Wind", "Solar", "Other renewables"]


# Define function for horizontal stacked bar chart
def stacked_bar(input_dict):

    style.use("seaborn-v0_8-dark")
    plt.clf()
    plt.xlim(0, 80000)
    plt.xticks([t for t in range(0, 80000, 10000)], fontfamily="Jost", fontsize="11")
    move_figure(fig, 5, 5)

    plt.rcParams["font.family"] = 'Jost'

    # style.use("seaborn-v0_8-dark")

    # We need to clear figure otherwise it seems to conflict with previous
    # plot and the bars are not ordered correctly
    # Set colour theme

    for label, value in input_dict.items():

        # For each country label, set starting bar position as 0 on the x-axes
        left = 0
        bar_colours = ['#AC3931', '#2C6E49', '#537D8D', '#D68C45', '#2A4BA4', '#0089D3', '#B46414', '#399E5A']

        # Use a second loop to build up each bar from component bars
        for n in range(len(value)):

            # Starting x-position of a new bar = (previous x-coordinate) + (width of previous bar)
            y = label
            plt.barh(y, width=value[n], left=left, label=label, color=bar_colours[n])
            plt.yticks(fontfamily="Jost", fontsize="12")

            if value[n] > 6000:
                plt.text((left + 0.5*value[n]), y, str(round(value[n], 1)),
                         verticalalignment="center", ha="center", color="white")

            left += value[n]

        plt.legend(energy_sources, loc="lower right")
        plt.text(sum(value)+400, y, str(round(sum(value), 1)) + " kWh",
                 verticalalignment="center", ha="left", color="black")

    # Inverts y-axes so that longest bar is at the top of the chart
    plt.gca().invert_yaxis()

    # Using 'plot()' on its own keeps the program running while 'plt.show()' seems to
    # block execution
    plot()
