import datetime
time = datetime.datetime.now()
name = input("What is your name?\n")
allowed_users= ["Patrick", "Love", "Kumi"]
allowed_password = ['passwordPatrick', 'passwordLove', 'passwordKumi']

if(name in allowed_users):
    password = input("What is your password\n")
    userID = allowed_users.index(name)

    if(password == allowed_password[userID]):
        print("Welcome %s" % name)
        print(time)
    while True:
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")

        selected_option = int(input("Please select an option:"))

        if (selected_option == 1):
            print("You selected %s" % selected_option)

            withdrawal = int(input("How much would you like to withdraw?"))
            print("Take your cash.")

        elif(selected_option == 2):
            print("You selected %s" % selected_option)
            deposit = int(input("How much would you like to deposit?"))
            print(f"Your balance is now {deposit}")
        elif(selected_option == 3):
            print("You selected %s" % selected_option)
            complaint = input("What issue would you like to report?")
            print("Thank you for contacting us.")
        else:
            print("Invalid option selected, please try again")

    else:
        print("Password Incorrect, please try again")

else:
    print("Name not found, please try again")