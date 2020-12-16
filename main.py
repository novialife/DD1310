import statistics

import pandas as pd
from Wind import Wind
from Solar import Solar
from Utilities import choice_control, variable_control
from tkinter import *
import matplotlib.pyplot as plt


# Displays the first menu that shows three options for Solar power, Wind power and Exit
def first_menu():
    menu = "first"
    valid_choice = False
    while not valid_choice:
        choice = input("Choose what you want to do: \n1. Select Latitude for Solar and calculate\n" +
                       "2. Select Wind and calculate\n3. Exit\n")
        valid_choice = choice_control(choice, menu)
    return choice


# Asks for the value for the chosen option of energy. Also passes the input to the control function.
def type_chosen(choice):
    valid_choice = False
    if choice == "1":
        while not valid_choice:
            variable = input("Choose latitude between 0 and 90: ")
            variable_type = "latitude"
            print()
            valid_choice = variable_control(variable, variable_type)
        latitude = int(variable)
        return latitude
    else:
        while not valid_choice:
            variable = input("Choose rotor diameter between 25 and 50: ")
            variable_type = "rotor_diameter"
            print()
            valid_choice = variable_control(variable, variable_type)
        rotor_diameter = int(variable)
        return rotor_diameter


# Displays the second menu and also creates the print-out or prints out the table based on the users input
def second_menu(obj, year_average, print_out, month_list, averageval, cell_val):
    menu = "second"
    valid_second_choice = False

    while not valid_second_choice:
        choice = input(
            "1. Would you like a print-out?\n2. Would you like to display it here as a table?\n3. Show graphically\n" +
            "4. Exit\n")

        print()
        valid_second_choice = choice_control(choice, menu)

    if choice == "1":
        with open(print_out, 'w+') as new_file:
            new_file.write(obj.table.to_string(index=False) +
                           "\n--------------------------------------------------------------------\n "
                           "The yearly average is: " + str(year_average), )

        print("Done")

    elif choice == "2":

        print(obj.table.to_string(index=False) +
              '\n--------------------------------------------------------------------\n' + "The year average is: " +
              str(year_average))

    elif choice == "3":
        GUI(month_list, averageval, cell_val)


    elif choice == "4":
        return False


def GUI(month_list, averageval, cell_val):
    # Create the tkinter inferface
    root = Tk()
    root.title("Din farsa")
    root.resizable(False, False)
    # Create the buttons
    graph_button = Button(root, text="Graph", command=lambda: graph(month_list, averageval), height=10, width=20)
    graph_button.grid(row=1, column=0, padx=10)

    table_button = Button(root, text="Table", command=lambda: table_gui(month_list, cell_val), height=10, width=20)
    table_button.grid(row=2, column=0)

    root.mainloop()


def vals_gui(obj):
    # Calculate the values needed for the graphs and table for GUI
    index = 0
    twoD_output = []
    for elem in range(0, 12):
        month_inlist = []
        for thing in range(0, 30):
            month_inlist.append(obj.output[index])
            index += 1
        twoD_output.append(month_inlist)

    # index = 0
    # sliced_output = [[self.output[index] for j in range(30)] for k in range(12)]

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


def graph(month_list, averageval):
    # Creating the graph
    fig = plt.figure(figsize=(14, 6))
    ax1 = fig.add_subplot(111)
    ax1.bar(month_list, averageval)
    plt.show()


def table_gui(month_list, cell_val):
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


#  Main function which is the structure of the program
def main():
    # Sets the display options for the pandas dataframe when printing it out.
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)

    print("Welcome")
    while True:
        print()
        choice = first_menu()

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

        if choice == "1":
            type_of_energy = "Solar"
            variable = type_chosen(choice)

            # Creating object for class and initiating class functions
            obj = Solar(months, day_list, variable)
            obj.sun()
            obj.energy_function(variable)
            obj.output_function()
            obj.tables_function()


        elif choice == "2":
            type_of_energy = "Wind"
            variable = type_chosen(choice)

            # Creating object for class and initiating class functions
            obj = Wind(months, day_list,rotor_diameter=35)
            obj.output_function(variable)
            obj.tables_function(variable)

        elif choice == "3":
            return False

        year_average = round((sum(obj.output) / 360))
        print_out = type_of_energy + "_Plant.txt"
        averageval, cell_val = vals_gui(obj)
        second_menu(obj, year_average, print_out, month_list, averageval, cell_val)


main()
