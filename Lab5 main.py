import TVClass


def tv_data():
    filename = 'TVinfo.txt'  # Open file and read it
    with open(filename, 'r') as file:
        data = file.readlines()
        tvs = []
        for line in data:
            line = line.split(",")
            tvs.append(TVClass.TV(line[0], line[1], line[2]))

    return tvs


def main_menu(tvs):
    menu = []

    for x in tvs:
        menu.append(x.device_name())

    menu.append("Quit")

    print("Welcome!")
    y = 1
    for x in menu:
        print(str(y) + ".", x)
        y += 1
    return menu


def menu_selection(menu):
    while True:
        try:
            choice = int(input("Choose Device: ")) - 1
        except ValueError:
            print("Try again")

        if choice < 0 or choice > len(menu):
            print("Try again")
        elif choice == len(menu):
            quit()
        else:
            break

    return choice


def main():  # Main function
    tvs = tv_data()
    menu = main_menu(tvs)
    choice = int(menu_selection(menu))
    tv_menu(tvs, choice)


def tv_menu(tvs, choice):  # Menu option function
    valid_choice = False
    while not valid_choice:
        print(tvs[choice])

        menu_choice = input('''
        1. Change channel
        2. Lower Volume
        3. Increase Volume
        4. Back to home\n ''')
        valid_choice = menu_choice_control(menu_choice, choice, tvs)


def menu_choice_control(menu_choice, choice, tvs):  # Controls the menu choice for correct values
    if menu_choice == "1":
        try:
            channel = int(input("Choose a channel between 1-99"))
        except ValueError:
            print("Thats wrong!")
            menu_choice_control(menu_choice, device, tv)
            return False

        channel = int(channel)
        if channel < 1 or channel > 99:
            print("Thats wrong!")
            menu_choice_control(menu_choice, device, tv)

        else:
            tvs[choice].change_channel(channel)
            with open("TVinfo.txt", "w") as file:
                for x in tvs:
                    file.write(",".join(map(str, x.tv_list())) + "\n")
                return False

    elif menu_choice == "2":
        tvs[choice].low_vol()

        with open("TVinfo.txt", "w") as file:
            file.writelines(data)
        return False

    elif menu_choice == "3":
        tvs[choice].inc_vol()
        return False

    elif menu_choice == "4":
        main_menu(tvs)

    else:
        print("Choose a number between 1-4")


main()
