import statistics
from tkinter import *
from tkinter import messagebox

import matplotlib.pyplot as plt

from Solar import Solar
from Wind import Wind
from Utilities import variable_control


def print_out(mode, latitudeentry, rotorentry, day_list, months):
    if mode == "Solar":
        sun_factor, energy, output, table = parseInfo(mode, latitudeentry, rotorentry, day_list, months)
    else:
        output, table = parseInfo(mode, latitudeentry, rotorentry, day_list, months)

    with open(mode + ".txt", 'w+') as new_file:
        new_file.write(table.to_string(index=False) +
                       "\n--------------------------------------------------------------------\n "
                       "The yearly average is: " + str(round((sum(output) / 360))), )


def graph(mode, latitudeentry, rotorentry, months, month_list, day_list):
    averageval, cell_vals = vals_gui(mode, latitudeentry, rotorentry, months, day_list)

    # Creating the graph
    fig = plt.figure(figsize=(14, 6))
    ax1 = fig.add_subplot(111)
    ax1.bar(month_list, averageval)
    plt.show()


def table_gui(mode, latitudeentry, rotorentry, months, month_list, day_list):
    averageval, cell_val = vals_gui(mode, latitudeentry, rotorentry, months, day_list)

    # Creating the table
    fig = plt.figure(figsize=(10, 5))
    ax2 = fig.add_subplot(111)
    col_labels = ['Output Average', 'Deviation', 'Minimum Value', 'Maximum Value']
    row_labels = month_list

    the_table = plt.table(cellText=cell_val,
                          rowLabels=row_labels,
                          colLabels=col_labels,
                          loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(1, 1)
    # Making the grid lines not visible
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right', 'top', 'bottom', 'left']:
        plt.gca().spines[pos].set_visible(False)
    plt.show()


def vals_gui(mode, latitudeentry, rotorentry, months, day_list):
    if mode == "Solar":
        sun_factor, energy, output, table = parseInfo(mode, latitudeentry, rotorentry, day_list, months)
    else:
        output, table = parseInfo(mode, latitudeentry, rotorentry, day_list, months)

    # Calculate the values needed for the graphs and table for GUI
    index = 0
    twoD_output = []
    for elem in range(0, 12):
        month_inlist = []
        for thing in range(0, 30):
            month_inlist.append(output[index])
            index += 1
        twoD_output.append(month_inlist)

    averageval = [round(sum(row) / len(row)) for row in twoD_output]

    deviation = [round(statistics.stdev(dev)) for dev in twoD_output]

    minval = list(map(min, twoD_output))

    maxval = list(map(max, twoD_output))

    index = 0
    cell_vals = []
    for elem in range(0, 12):
        row = [averageval[index], deviation[index], minval[index], maxval[index]]
        index += 1
        cell_vals.append(row)

    return averageval, cell_vals


def parseInfo(mode, latitudeentry, rotorentry, day_list, months):
    if mode == "Solar":
        latitude = type_chosen(mode, latitudeentry, rotorentry)
        solar = Solar(months, day_list, latitude)
        solar.sun()
        sun_factor = solar.sun_factor
        solar.energy_function()
        energy = solar.energy
        solar.output_function()
        output = solar.output
        solar.tables_function()
        table = solar.table
        return sun_factor, energy, output, table

    else:
        rotor_diameter = type_chosen(mode, latitudeentry, rotorentry)
        wind = Wind(months, day_list, rotor_diameter)
        wind.output_function(rotor_diameter)
        output = wind.output
        wind.tables_function()
        table = wind.table
        return output, table


def getInfo(mode, latitudeentry, rotorentry):
    if mode == "Solar":
        latitude = latitudeentry.get()
        return latitude
    else:
        rotor_diameter = rotorentry.get()
        return rotor_diameter


def type_chosen(mode, latitudeentry, rotorentry):
    valid_choice = False
    if mode == "Solar":
        while not valid_choice:
            variable = getInfo(mode, latitudeentry, rotorentry)
            variable_type = "latitude"
            print()
            valid_choice = variable_control(variable, variable_type)

        latitude = int(variable)
        return latitude
    else:
        while not valid_choice:
            variable = getInfo(mode, latitudeentry, rotorentry)
            variable_type = "rotor_diameter"
            print()
            valid_choice = variable_control(variable, variable_type)
            if valid_choice == "False":
                messagebox.showerror("Error", "Only numbers between 25-50!")
            else:
                continue
        rotor_diameter = int(variable)
        return rotor_diameter


def main():
        # Creates list for the days ranging from 1 to 360
        day_list = []
        for day in range(1, 361):
            day_list += [day]

        # Creating the list for the months. It is first a list with 360 empty strings, then making every 30th element a
        # month.

        months = [""] * 360
        month_list = ['January', 'February', 'Mars', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']
        monthnumber = 0
        for time in range(0, 360):
            if time % 30 == 0:
                months[time] = month_list[monthnumber]
                monthnumber += 1

        master = Tk()

        Label(master,
              text="Latitude, ONLY NUMBER BETWEEN 0-99").grid(row=0)
        Label(master,
              text="Rotor").grid(row=3)

        latitudeentry = Entry(master)
        latitudeentry.grid(row=0, column=1)
        rotorentry = Entry(master)
        rotorentry.grid(row=3, column=1)

        solar_graph_button = Button(master, text="Solar Graph", command=lambda mode="Solar": [
            parseInfo(mode, latitudeentry, rotorentry, day_list, months),
            graph(mode, latitudeentry, rotorentry, months, month_list,
                  day_list)],
                                    height=10,
                                    width=20).grid(
            row=1, column=1, pady=10)

        solar_table_button = Button(master, text="Solar Table",
                                    command=lambda mode="Solar": [
                                        parseInfo(mode, latitudeentry, rotorentry, day_list, months),
                                        table_gui(mode, latitudeentry, rotorentry, months, month_list, day_list)],
                                    height=10,
                                    width=20).grid(
            row=1, column=2, pady=10)

        solar_printoutbtn = Button(master, text="Solar Printout", command=lambda mode="Solar": [
            parseInfo(mode, latitudeentry, rotorentry, day_list, months),
            print_out(mode, latitudeentry, rotorentry, day_list, months)], height=10,
                                   width=20).grid(
            row=1, column=3, pady=10)

        wind_graph_button = Button(master, text="Wind Graph", command=lambda mode="Wind": [
            parseInfo(mode, latitudeentry, rotorentry, day_list, months),
            graph(mode, latitudeentry, rotorentry, months, month_list,
                  day_list)], height=10,
                                   width=20).grid(
            row=5, column=1, pady=10)

        wind_table_button = Button(master, text="Wind Table", command=lambda mode="Wind": [
            parseInfo(mode, latitudeentry, rotorentry, day_list, months),
            table_gui(mode, latitudeentry, rotorentry, months, month_list, day_list)], height=10,
                                   width=20).grid(
            row=5, column=2, pady=10)

        wind_printoutbtn = Button(master, text="Wind Printout", command=lambda mode="Wind": [
            parseInfo(mode, latitudeentry, rotorentry, day_list, months),
            print_out(mode, latitudeentry, rotorentry, day_list, months)], height=10,
                                  width=20).grid(
            row=5, column=3, pady=10)

        quitbtn = Button(master,
                         text='Quit',
                         command=lambda: exit(), height=10, width=20).grid(row=6,
                                                                           column=1,
                                                                           pady=10)
        master.mainloop()

main()
