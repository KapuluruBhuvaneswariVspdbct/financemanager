import sqlite3

# Database Setup
def setup_database():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Add Expense
def add_expense(date, category, amount, description):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (date, category, amount, description)
        VALUES (?, ?, ?, ?)
    ''', (date, category, amount, description))
    conn.commit()
    conn.close()

# View Expenses
def view_expenses():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('SELECT date, category, amount, description FROM expenses')
    rows = cursor.fetchall()
    conn.close()

    print("\n--- All Expenses ---")
    print(f"{'Date':<15}{'Category':<15}{'Amount':<10}{'Description':<30}")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10.2f}{row[3]:<30}")
    print("-" * 70)

# Calculate Total Expenses by Category
def total_by_category():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    rows = cursor.fetchall()
    conn.close()

    print("\n--- Total Expenses by Category ---")
    print(f"{'Category':<15}{'Total Amount':<15}")
    print("-" * 30)
    for row in rows:
        print(f"{row[0]:<15}{row[1]:<15.2f}")
    print("-" * 30)

# Main Menu
def main():
    setup_database()
    while True:
        print("\n=== Personal Finance Management ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total by Category")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (e.g., Food, Travel): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
            print("Expense added successfully!")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
