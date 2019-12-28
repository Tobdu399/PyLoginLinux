import pickle

# Load user list
with open("data.dat", "rb") as f:
   user_list = pickle.load(f)
   
with open("userlist.dat", "rb") as f:
    users = pickle.load(f)

# Update user list -function
def update_list():
    with open("data.dat", "wb") as f:
        pickle.dump(user_list, f)
        
    with open("userlist.dat", "wb") as f:
        pickle.dump(users, f)

# Prevent unwanted running with this:       
if __name__ == "__main__":
    update_list()
