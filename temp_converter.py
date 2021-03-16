try:
    choice = int(input(
        "Enter 1 if you want to convert from Celsius to Fahrenheit\nEnter 2 if you want to convert from Fahrenheit to celsius :\n"))
    if choice == 1:
        c = int(input("Enter the temperature in Celsius : "))
        temp_f = (c * 1.8) + 32
        print(temp_f)
    elif choice == 2:
        f = int(input("Enter the temperature in Fahrenheit : "))
        temp_c = (f - 32) / 1.8
        print(temp_c)
    else:
        print("invalid option entered")
except ValueError:
    print("Enter a number!")
