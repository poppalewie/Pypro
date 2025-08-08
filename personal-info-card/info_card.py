#function that returns a dict with user's data
def get_user_input():
    user_info = {}

#prompt for name
#strip to check if it's non-empty,re-prompt using while and store in user_info["name"]
    
    while True:
        name = input("Enter your full name: ").strip()
        if name:
            user_info["name"] = name
            break
        print("Error: Name cannot be empty.")

#try/except to convert to integer,check if positive(>0),if invalid reprompt & store in user_info["age"]

    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                user_info["age"] = age
                break
            print("Error: Age must be a positive number.")
        except ValueError:
            print("Error: Please enter a valid number for age.")

#check if has @, if invalid reprompt and store in user_info["email"]

    while True:
        email = input("Enter your email: ").strip()
        if "@" in email:
            user_info["email"] = email
            break
        print("Error: Email must contain '@'.")

#hobby   
    while True:
        hobby = input("Enter a hobby: ").strip()
        if hobby:
            user_info["hobby"] = hobby
            break
        print("Error: Hobby cannot be empty.")

    
    return user_info

#define function to accept user_info as parameter
def display_card(user_info):
    card_width = 30
    border = "=" * card_width
    title = "Personal Info Card".center(card_width)

    print(border)
    print(title)
    print(border)
    print(f"Name: {user_info['name']}")
    print(f"Age: {user_info['age']}")
    print(f"Email: {user_info['email']}")
    print(f"Hobby: {user_info['hobby']}")
    print(border)
    
def main():
    print("Welcome to Your Personal Info Card Creator!")
    
    while True:
        #get user input & display the card
        user_info = get_user_input()
        display_card(user_info)

        while True:
            choice = input("Create another card? (y/n): ").lower()
            if choice in ["y", "n"]:
                break
            print("Error: Please enter 'y' or 'n'.")

        if choice == "n":
            break

    print("Thanks for using Info Card Creator!")

if __name__ == "__main__":
    main()

