import sqlite3

# Create a SQLite database
conn = sqlite3.connect('reservation_system.db')
c = conn.cursor()

# Create the tables
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS reservations (
        reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        train_number INTEGER NOT NULL,
        class_type TEXT NOT NULL,
        date_of_journey TEXT NOT NULL,
        source TEXT NOT NULL,
        destination TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (user_id)
    )
''')

# Function to handle user registration
def register_user(username, password):
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    print("User registered successfully.")

# Function to handle user login
def login(username, password):
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    if user:
        print("Login successful.")
        return user[0]  # Return the user_id
    else:
        print("Invalid username or password.")
        return None

# Function to make a reservation
def make_reservation(user_id, train_number, class_type, date_of_journey, source, destination):
    c.execute('INSERT INTO reservations (user_id, train_number, class_type, date_of_journey, source, destination) VALUES (?, ?, ?, ?, ?, ?)', (user_id, train_number, class_type, date_of_journey, source, destination))
    conn.commit()
    print("Reservation made successfully.")

# Function to cancel a reservation
def cancel_reservation(reservation_id):
    c.execute('DELETE FROM reservations WHERE reservation_id = ?', (reservation_id,))
    conn.commit()
    print("Reservation cancelled successfully.")

# Usage example
def main():
    while True:
        print("1. Register")
        print("2. Login")
        # print("3. Make Reservation")
        # print("4. Cancel Reservation")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = login(username, password)
            if user_id:
                logged_in_menu(user_id)

        elif choice == '3':
            if user_id:
                train_number = input("Enter train number: ")
                class_type = input("Enter class type: ")
                date_of_journey = input("Enter date of journey: ")
                source = input("Enter source: ")
                destination = input("Enter destination: ")
                make_reservation(user_id, train_number, class_type, date_of_journey, source, destination)

        elif choice == '4':
            if user_id:
                reservation_id = input("Enter reservation ID to cancel: ")
                cancel_reservation(reservation_id)

        elif choice == '5':
            break

        else:
            print("Invalid choice. Try again.")

# Additional menu for logged-in users
def logged_in_menu(user_id):
    while True:
        print("1. Make Reservation")
        print("2. Cancel Reservation")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            train_number = input("Enter train number: ")
            class_type = input("Enter class type: ")
            date_of_journey = input("Enter date of journey: ")
            source = input("Enter source: ")
            destination = input("Enter destination: ")
            make_reservation(user_id, train_number, class_type, date_of_journey, source, destination)

        elif choice == '2':
            reservation_id = input("Enter reservation ID to cancel: ")
            cancel_reservation(reservation_id)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Try again.")

# Run the main function
if __name__ == '__main__':
    main()

# Close the database connection
conn.close()
