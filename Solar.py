import random
import math
from pandas import DataFrame


# The P-Uppgift didn't specify whether to hard-code the area and the sunnumber or not. Can be easily fixed if needed to
area = 450
soltal = 7


# Creating the class for solar where its properties from the methods will be stored
class Solar:

    def __init__(self, months, day_list, latitude):
        self.latitude = latitude
        self.months = months
        self.days = day_list
        self.area_list = [area] * 360
        self.soltal_list = [soltal] * 360
        self.latitude_list = [latitude] * 360
        self.sun_factor = []
        self.energy = []
        self.output = []
        self.table = None

    # Method for calculating the sun factors and creating list for it. Returns list to be stored.
    def sun(self):
        sun_factor = []
        for x in range(1, 361):
            sunx = round(random.random(), 1)
            sun_factor.append(sunx)
        self.sun_factor = sun_factor

    # Method for the energy function. Creates list that stores all of them. Returns list to be stored.
    def energy_function(self):
        energy = []
        for time in range(1, 361):
            v = round(((23.5 * math.sin((math.pi * (time - 80)) / 180) + 90 - self.latitude) / 90), 4)
            if v < 1 or v > 0:
                v = round((v * v), 4)
                energy.append(v)
            elif v >= 1:
                energy += [1]
            elif v <= 0:
                energy += [0]
        self.energy = energy

    # Method for the output function. Creates list to store them. Returns list to be stored
    def output_function(self):
        output = []
        for t in range(0, 360):
            output_value = round((area * soltal * self.sun_factor[t] * self.energy[t]), 2)
            output.append(output_value)
        self.output = output

    # Creating a table for the Solar using pandas DataFrame
    def tables_function(self):

        # Creating the chart for table as a dictionary where each column header has its corresponding list
        solar_chart = {'Area': self.area_list,
                       'Sun Number': self.soltal_list,
                       'Latitude': self.latitude_list,
                       'Day': self.days,
                       'Sun Factor': self.sun_factor,
                       'f(t,latitude)': self.energy,
                       'Output': self.output,
                       'Month': self.months
                       }

        # Using pandas DataFrame create the actual table
        df_solar = DataFrame(solar_chart, columns=['Area',
                                                   'Sun Number',
                                                   'Latitude',
                                                   'Day',
                                                   'Sun Factor',
                                                   'f(t,latitude)',
                                                   'Output',
                                                   'Month'])

        self.table = df_solar
