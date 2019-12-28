import time
import os
import pickle
import users

def clear():
    os.system("clear")
    
new_username = ""
new_password = ""

choose_user = ""

change_name = ""
change_pass = ""
    
# ---------------------------------------------

with open("datafile.dat", "rb") as f:
    valid_sign_in = pickle.load(f)
    
with open("user.dat", "rb") as f:
    current_user = pickle.load(f)
    
# ---------------------------------------------

try:
    # Stuff for user creation -------------------------------------------------------
    def create_user():
        print()
        print("----------------------------------------------")
        
        users.user_list[new_username] = new_password
        users.users.append(new_username)
        users.update_list()
        
        print()
        print("Done! Now you need to restart this system to apply changes")
        print()
        
        input("Press Enter to continue... ")
        clear()
        exit()
        
    
    def add_user2():
        global new_username
        global new_password
        
        clear()
        print("******************* Create new user ********************")
        print()
        
        print("Type username for the new user")
        print()
        new_username = input("Username: ")
        print("----------------------------------------------")
        print("Type password for " + new_username)
        print()
        new_password = input("Password: ")
        
        clear()
        print("******************* Create new user ********************")
        print()
        
        print("New user details:")
        print()
        print("Username: " + new_username)
        print("Password: " + new_password)
        print()
        print("----------------------------------------------")
        print("Are you sure you want to continue? (Y/n)")
        print()
        
        confirmation1 = input("> ")
        
        if confirmation1 == "y":
            time.sleep(1)
            create_user()
            
        elif confirmation1 == "Y":
            time.sleep(1)
            create_user()
            
        elif confirmation1 == "n":
            time.sleep(1)
            userMain()
            
        elif confirmation1 == "N":
            time.sleep(1)
            userMain()
            
        else:
            time.sleep(1)
            userMain()
        
    
    def add_user():
        clear()
        print("******************* Create new user ********************")
        print()
        print("You need to authenticate yourself first before you can add new users!")
        print("Type your password below or type 'cancel' to go back")
        print()
        
        password_input = input("Password: ")
        time.sleep(1)
        print()
        
        password = users.user_list[current_user]
        
        if password_input == password:
            add_user2()
            
        elif password_input == "cancel":
            userMain()
            
        else:
            print("Wrong password!")
            time.sleep(2)
            add_user()
        
        
    # Stuff for removing user --------------------------------------------------------------------
    def delete_user():
        print()
        print("----------------------------------------------")
        
        del users.user_list[choose_user]
        users.users.remove(choose_user)
        users.update_list()
        
        print()
        print("Done! Now you need to restart this system to apply changes")
        print()
        
        input("Press Enter to continue... ")
        clear()
        exit()
        
    
    def remove_user2():
        global choose_user
        
        clear()
        print("******************* Remove user ********************")
        print()
        print("Type the name of the user you want to remove from system or type 'cancel' to go back")
        print(users.users)
        print()
        
        choose_user = input("Username: ")
        time.sleep(1)
        print()
        print("----------------------------------------------")
        
        if choose_user in users.users:
            print()
            print("Are you sure you want to remove user " + choose_user + "? (Y/n)")
            print()
            
            confirmation2 = input("> ")
            
            if confirmation2 == "y":
                time.sleep(1)
                delete_user()
            
            elif confirmation2 == "Y":
                time.sleep(1)
                delete_user()
                
            elif confirmation2 == "n":
                time.sleep(1)
                userMain()
                
            elif confirmation2 == "N":
                time.sleep(1)
                userMain()
                
            else:
                time.sleep(1)
                userMain()
            
        elif choose_user == "cancel":
            time.sleep(1)
            userMain()
            
        else:
            print()
            print("That username doesn't exits! Make sure you type the username correctly")
            time.sleep(5)
            remove_user2()
        
        
    
    def remove_user():
        clear()
        print("******************* Remove user ********************")
        print()
        print("You need to authenticate yourself first before you can remove any user!")
        print("Type your password below or type 'cancel' to go back")
        print()
        
        password_input = input("Password: ")
        time.sleep(1)
        print()
        
        password = users.user_list[current_user]
        
        if password_input == password:
            remove_user2()
            
        elif password_input == "cancel":
            userMain()
            
        else:
            print("Wrong password!")
            time.sleep(2)
            remove_user()
        
        
    # Stuff for changin username -----------------------------------------------------------
    def change_username3():
        print()
        print("----------------------------------------------")
        print()
        
        # Update new name
        users.user_list[change_name] = users.user_list[current_user]
        del users.user_list[current_user]
        
        users.users.remove(current_user)
        users.users.append(change_name)
        
        users.update_list()
        
        print("Done! Now you need to restart this system to apply changes")
        print()
        
        input("Press Enter to continue... ")
        clear()
        exit()
        
    
    def change_username2():
        global change_name
        
        clear()
        print("******************* Change username ********************")
        print()
        print("Type new username for " + current_user)
        print()
        
        change_name = input("Username: ")
        
        print()
        print("----------------------------------------------")
        print()
        print("Your new username will be " + change_name + ". Are you sure you want to continue? (Y/n)")
        print()
        
        confirmation3 = input("> ")
        
        if confirmation3 == "y":
            time.sleep(1)
            change_username3()
            
        elif confirmation3 == "Y":
            time.sleep(1)
            change_username3()
            
        elif confirmation3 == "n":
            time.sleep(1)
            userMain()
            
        elif confirmation3 == "N":
            time.sleep(1)
            userMain()
            
        else:
            time.sleep(1)
            userMain()
        
    
    def change_username():
        clear()
        print("******************* Change username ********************")
        print()
        print("You need to authenticate yourself first before you can change your username!")
        print("Type your password below or type 'cancel' to go back")
        print()
        
        password_input = input("Password: ")
        time.sleep(1)
        print()
        
        password = users.user_list[current_user]
        
        if password_input == password:
            change_username2()
            
        elif password_input == "cancel":
            userMain()
            
        else:
            print("Wrong password!")
            time.sleep(2)
            change_username()
        
        
    # Stuff for changing password -----------------------------------------------------------
    def change_password3():
        print()
        print("----------------------------------------------")
        print()
        
        # Update new password
        users.user_list[current_user] = change_pass
        users.update_list()
        
        print("Done! Now you need to restart this system to apply changes")
        print()
        
        input("Press Enter to continue... ")
        clear()
        exit()
    
    
    def change_password2():
        global change_pass
        
        clear()
        print("******************* Change password ********************")
        print()
        print("Type new password for " + current_user)
        print()
        
        change_pass = input("Password: ")
        
        print()
        print("----------------------------------------------")
        print()
        print("Your new password will be " + change_pass + ". Are you sure you want to continue? (Y/n)")
        print()
        
        confirmation4 = input("> ")
        
        if confirmation4 == "y":
            time.sleep(1)
            change_password3()
            
        elif confirmation4 == "Y":
            time.sleep(1)
            change_password3()
            
        elif confirmation4 == "n":
            time.sleep(1)
            userMain()
            
        elif confirmation4 == "N":
            time.sleep(1)
            userMain()
            
        else:
            time.sleep(1)
            userMain()
        
    
    def change_password():
        clear()
        print("******************* Change password ********************")
        print()
        print("You need to authenticate youself first before you can change your password!")
        print("Type your password below or type 'cancel' to go back")
        print()
        
        password_input = input("Password: ")
        time.sleep(1)
        print()
        
        password = users.user_list[current_user]
        
        if password_input == password:
            change_password2()
            
        elif password_input == "cancel":
            userMain()
            
        else:
            print("Wrong password!")
            time.sleep(2)
            change_password()
    
    # -------------------------------------------------------------------------------------
    
    def userMain():
        clear()
        print("******************* " + current_user + " ********************")
        print()
        print("1 = Add new user")
        print("2 = Remove any existing user")
        print("3 = Change username")
        print("4 = Change password")
        print("5 = Exit")
        print()
        
        user_choise = input("> ")
        
        if user_choise == "1":
            add_user()
            
        elif user_choise == "2":
            remove_user()
            
        elif user_choise == "3":
            change_username()
            
        elif user_choise == "4":
            change_password()
            
        elif user_choise == "5":
            exit()
            
        else:
            print("That isn't an option!")
            time.sleep(3)
            userMain()
        
        
    def main():
        global valid_sign_in
        
        clear()
        
        # Check if user is really signed in
        if valid_sign_in == 1:
            # Set value to 0 so user cannot open this file again without logging in first
            valid_sign_in = 0
            with open("datafile.dat", "wb") as f:
                pickle.dump(valid_sign_in, f)
                
            # And do something in here...
            userMain()
                    
        else:
            print("You need to sign before you can access to this file!")
            
    # Run this program
    main()
        
    
except(KeyboardInterrupt, SystemExit):
    def shutdown_animation():
        clear()
        print("Shutting down: Please wait...")
        print("|##-----------------------------------|")
        time.sleep(0.2)

        clear()
        print("Shutting down: Please wait...")
        print("|###----------------------------------|")
        time.sleep(0.1)

        clear()
        print("Shutting down: Please wait...")
        print("|#######------------------------------|")
        time.sleep(0.2)

        clear()
        print("Shutting down: Please wait...")
        print("|#################--------------------|")
        time.sleep(0.8)

        clear()
        print("Shutting down: Please wait...")
        print("|###################################--|")
        time.sleep(0.4)

        clear()
        print("Shutting down: Please wait...")
        print("|#####################################|")
        time.sleep(1)
        clear()
        exit()
    
    shutdown_animation()