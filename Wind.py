# The formula for calculating the energy produced from the wind power plant were taken directly the study:
# "Wind Turbine Blade Efficiency and Power Calculation with Electrical Analogy", by:
# Asis Sarkar*, Dhiren Kumar Behera**
# * National Institute of Technology, Agarthala, Tripura State, India
# **Dept of Mechanical Engineering, I.G.I.T SARANG, ODISHA, INDIA


# I tried to use the information given by the instructions but I couldn't understand what they meant.
# So I only used the rotor diameter interval which was easily applied to the formula from the research paper.

import random
import math
from pandas import DataFrame

# Hard coded with the number from the research paper
air_density = 1.23


# Creates class Wind and stores the properties given by the methods
class Wind:

    def __init__(self, months, day_list, rotor_diameter):
        self.days = day_list
        self.months = months
        self.rotor_diameter_list = [rotor_diameter] * 360
        self.output = []
        self.table = None

    # Method to calculate the output of the power plant for any given rotor diameter between 25 and 50 per instruction
    def output_function(self, rotor_diameter):
        att = 'output'
        # This could probably have been written better without repetition for each season.
        for time in range(0, 360):
            summer_winter = round(0.5 * 1.23 * ((math.pi * rotor_diameter / 2) ** 2) * 0.48 *
                                  (random.randint(5, 8) ** 3) * 0.593)
            spring_fall = round(0.5 * 1.23 * ((math.pi * rotor_diameter / 2) ** 2) * 0.48 *
                                (random.randint(8, 12) ** 3) * 0.593)
            if time <= 60:
                generated = summer_winter
                self.__dict__[att].append(generated)
            elif 60 < time <= 150:
                generated = spring_fall
                self.__dict__[att].append(generated)
            elif 150 < time <= 240:
                generated = summer_winter
                self.__dict__[att].append(generated)
            elif 240 < time <= 330:
                generated = spring_fall
                self.__dict__[att].append(generated)
            else:
                generated = summer_winter
                self.__dict__[att].append(generated)

    def tables_function(self):

        # Creating lists for the constant which is the rotor diameter so that every row has the diameter next to it.

        # Creating the chart for my table as a dictionary where each header, ex. "Dag" has its corresponding
        # assigned list
        wind_chart = {'Rotor Diameter': self.rotor_diameter_list,
                      'Day': self.days,
                      'Energy': self.output,
                      'Months': self.months
                      }

        # Using pandas DataFrame to create the table
        df_wind = DataFrame(wind_chart, columns=['Rotor Diameter', 'Day', 'Energy', 'Months'])
        self.table = df_wind
