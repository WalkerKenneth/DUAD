def menu():
    selection = 0
    print(
        """
        Student Control Panel
            1) Add Student
            2) See all students data
            3) Top 3 students
            4) All students average
            5) Export student data to csv
            6) Import data from csv
        """
    )
    while True:
        try:
            selection = int(input('Select an option from the menu "Press 7 to exit": '))
            if selection < 1 or selection > 7:
                raise ValueError('Invalid selection')
            break
        except ValueError as ex:
            print (ex)
    return selection
