import time
import os
import users
import pickle

user_list = users.user_list
    
# .append to add
# .remove to remove

# TODO:
# Make system that can change username or password
# Make system that can add and remove users

username_input = ""
password_input = ""

def clear():
    os.system("clear")

# --------------------------------------

try:
    # Loading animaion
    def loading():
        mainCopy()
        print("Checking")
        time.sleep(0.5)
        
        mainCopy()
        print("Checking.")
        time.sleep(0.5)
        
        mainCopy()
        print("Checking..")
        time.sleep(0.5)
        
        mainCopy()
        print("Checking...")
        time.sleep(0.5)
        
        mainCopy()
        print("Checking")
        time.sleep(0.5)
        
        mainCopy()
        print("Checking.")
        time.sleep(0.5)
            
    
    # Copy of main only for loading animation
    def mainCopy():
        clear()
        
        print("******************* LOGIN ********************")
        print("Username: " + username_input)
        print("----------------------------------------------")
        print("Password: " + password_input)
        print("----------------------------------------------")
    
    # ------------------------------------------------------------------------------
    
    def main():
        global username_input
        global password_input
        
        clear()
        
        # For developing purposes only
        # print(users.user_list)
        # print(users.users)
        
        print("******************* LOGIN ********************")
        username_input = input("Username: ")
        print("----------------------------------------------")
        password_input = input("Password: ")
        print("----------------------------------------------")
        
        loading()
        mainCopy()
        
        password = users.user_list.get(username_input)
        
        if username_input in users.user_list:
            if password_input == password:
                print("Checking ✓")
                print()
                print("Authorization Successfull: Access Granted")
                time.sleep(3)
                clear()
                
                # Authenticate sign in
                with open("datafile.dat", "rb") as f:
                    valid_sign_in = pickle.load(f)
                    
                valid_sign_in = 1
                
                with open("datafile.dat", "wb") as f:
                    pickle.dump(valid_sign_in, f)
                    
                # Save current user name
                with open("user.dat", "rb") as f:
                    current_user = pickle.load(f)
                    
                current_user = username_input
                
                with open("user.dat", "wb") as f:
                    pickle.dump(current_user, f)
                    
                # Go to second python file after logging in
                os.system("python3 userData.py")
                
            else:
                print("Checking ✕")
                print()
                print("Authorization Failed: Invalid username or password")
                time.sleep(3)
                main()
                
        else:
            print("Checking ✕")
            print()
            print("Authorization Failed: Invalid username or password")
            time.sleep(3)
            main()
            
            
    # Run this program
    main()
            

# To do if user tries to close program -------------------------
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
        time.sleep(0.5)
        clear()
        exit()

    shutdown_animation()
    