class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance


class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount


class TransactionHistory:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def display_history(self):
        if len(self.transactions) == 0:
            print("No transaction history.")
        else:
            print("Transaction History:")
            for transaction in self.transactions:
                print("Type:", transaction.transaction_type)
                print("Amount:", transaction.amount)
                print()


class ATM:
    def __init__(self):
        self.users = []  # List to store user objects
        self.transaction_history = TransactionHistory()

    def add_user(self, user):
        self.users.append(user)

    def authenticate_user(self, user_id, pin):
        for user in self.users:
            if user.user_id == user_id and user.pin == pin:
                return True
        return False

    def display_menu(self):
        print("ATM Menu:")
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def perform_transaction(self, user):
        choice = input("Enter your choice: ")
        if choice == '1':
            self.transaction_history.display_history()
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= user.balance:
                user.balance -= amount
                self.transaction_history.add_transaction(Transaction("Withdrawal", amount))
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        elif choice == '3':
            amount = float(input("Enter the amount to deposit: "))
            user.balance += amount
            self.transaction_history.add_transaction(Transaction("Deposit", amount))
            print("Deposit successful.")
        elif choice == '4':
            amount = float(input("Enter the amount to transfer: "))
            if amount <= user.balance:
                target_user_id = input("Enter the target user ID: ")
                for target_user in self.users:
                    if target_user.user_id == target_user_id:
                        user.balance -= amount
                        target_user.balance += amount
                        self.transaction_history.add_transaction(Transaction("Transfer", amount))
                        print("Transfer successful.")
                        break
                else:
                    print("Target user not found.")
            else:
                print("Insufficient balance.")
        elif choice == '5':
            print("Thank you for using the ATM.")
            exit()
        else:
            print("Invalid choice.")

    def run(self):
        while True:
            user_id = input("Enter your user ID: ")
            pin = input("Enter your PIN: ")

            if self.authenticate_user(user_id, pin):
                for user in self.users:
                    if user.user_id == user_id:
                        print("Authentication successful. Welcome,", user.user_id)
                        while True:
                            self.display_menu()
                            self.perform_transaction(user)
            else:
                print("Invalid user ID or PIN.")


# Example usage:
atm = ATM()

# Create user accounts
user1 = User("Rajeeb", "1111", 5000)
user2 = User("Behera", "2222", 3000)
atm.add_user(user1)
atm.add_user(user2)

# Run the ATM system
atm.run()
