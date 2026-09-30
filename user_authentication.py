# User Authentication & Access Control
# Basic Test

users = {
    "cashier1": {
        "email": "cashier1@gmail.com",
        "password": "password123"
    },
    "cashier2": {
        "email": "cashier2@gmail.com",
        "password": "password456"
    }
}


def login():
    print("=== POS LOGIN ===")

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("\nLogin successful!")
        print("Welcome,", username)
        pos_dashboard()
    else:
        print("\nInvalid username or password.")


def pos_dashboard():
    print("\n=== POS DASHBOARD ===")
    print("Welcome to the POS system.")
    print("You have successfully accessed the main dashboard.")


login()