import csv
import hashlib


class AccountManager:
    ACCOUNTS_FILE = "accounts.csv"

    @staticmethod
    def hash_password(password):
        """Hashes a password for secure storage."""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def register_account(username, password):
        """Register a new account."""
        accounts = AccountManager.load_accounts()

        # Check if the username already exists
        if username in accounts:
            print("Username already exists. Please try a different username.")
            return False

        hashed_password = AccountManager.hash_password(password)
        with open(AccountManager.ACCOUNTS_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, hashed_password])
        print("Account registered successfully!")
        return True

    @staticmethod
    def authenticate(username, password):
        """Authenticate a user with username and password."""
        accounts = AccountManager.load_accounts()
        hashed_password = AccountManager.hash_password(password)

        if username in accounts and accounts[username] == hashed_password:
            print("Login successful!")
            return True
        print("Invalid username or password.")
        return False

    @staticmethod
    def load_accounts():
        """Load accounts from the CSV file."""
        accounts = {}
        try:
            with open(AccountManager.ACCOUNTS_FILE, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        accounts[row[0]] = row[1]
        except FileNotFoundError:
            # Create the file if it doesn't exist
            with open(AccountManager.ACCOUNTS_FILE, mode="w", newline="") as file:
                pass
        return accounts