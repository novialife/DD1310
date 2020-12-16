# Control for the choices given in the first menu and second menu. Checks for input as integers and withn interval.
def choice_control(choice, menu):
    try:
        choice = int(choice)
    except ValueError:
        print("Write a number")
        print()
        return False

    if menu == "first":
        if choice < 1 or choice > 3:
            print("Choose a number between 1 and 3")
            print()
            return False

        elif choice == 3:
            print("Bye")
            quit()
        else:
            return True
    else:
        if choice < 1 or choice > 4:
            print("Choose a number between 1 and 4")
        elif choice == 4:
            quit()
        else:
            return True


# Control for the variables given for the latitude or rotor diameter. Checks for integer and for interval.
def variable_control(variable, variable_type):
    try:
        variable = int(variable)
    except ValueError:
        print("Write a number")
        print()
        return False

    if variable_type == "rotor_diameter":
        if variable < 25 or variable > 50:
            print("Choose a number between 25 and 50!")
            print()
            return False
        else:
            return True

    else:
        if variable <= 0 or variable >= 90:
            print("Choose a number between 0 and 90!")
            print()
            return False

        else:
            return True
