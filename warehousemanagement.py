import csv
import os

PRODUCT_FILE = 'products.csv'
USER_FILE = 'users.csv'

def authenticate():
    print("Welcome to the Warehouse Management System")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if user exists in the user file
    try:
        with open(USER_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    print("Authentication successful!")
                    return True
            print("Authentication failed! Please register or check your credentials.")
            return False
    except FileNotFoundError:
        print("No users found. Please register a new user.")
        return False

def register_user():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open(USER_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    print(f"User '{username}' registered successfully!")

def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    category = input("Enter Product Category: ")
    quantity = input("Enter Product Quantity: ")
    price = input("Enter Product Price: ")

    # Validate quantity and price
    if not quantity.isdigit() or not price.replace('.', '', 1).isdigit():
        print("Invalid quantity or price. Please enter valid numbers.")
        return

    with open(PRODUCT_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product_id, name, category, quantity, price])
    print(f"Product '{name}' added successfully.")

def view_products():
    try:
        with open(PRODUCT_FILE, mode='r') as file:
            reader = csv.reader(file)
            print("\n{:<10} {:<30} {:<20} {:<10} {:<10}".format('ID', 'Name', 'Category', 'Quantity', 'Price'))
            print("=" * 80)
            for row in reader:
                print("{:<10} {:<30} {:<20} {:<10} {:<10}".format(row[0], row[1], row[2], row[3], row[4]))
            print("=" * 80)
    except FileNotFoundError:
        print("Products file not found.")

def update_product():
    product_id = input("Enter Product ID to update: ")
    updated = False
    products = []

    try:
        with open(PRODUCT_FILE, mode='r') as file:
            reader = csv.reader(file)
            products = list(reader)

        for row in products:
            if row[0] == product_id:
                row[1] = input(f"Enter new name (current: {row[1]}): ") or row[1]
                row[2] = input(f"Enter new category (current: {row[2]}): ") or row[2]
                row[3] = input(f"Enter new quantity (current: {row[3]}): ") or row[3]
                row[4] = input(f"Enter new price (current: {row[4]}): ") or row[4]
                updated = True

        with open(PRODUCT_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(products)

        if updated:
            print("Product updated successfully.")
        else:
            print("Product ID not found.")
    except FileNotFoundError:
        print("Products file not found.")

def delete_product():
    product_id = input("Enter Product ID to delete: ")
    products = []

    try:
        with open(PRODUCT_FILE, mode='r') as file:
            reader = csv.reader(file)
            products = list(reader)

        products = [row for row in products if row[0] != product_id]

        with open(PRODUCT_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(products)

        print("Product deleted successfully.")
    except FileNotFoundError:
        print("Products file not found.")

def search_product():
    product_id = input("Enter Product ID to search: ")
    found = False

    try:
        with open(PRODUCT_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == product_id:
                    print("\nProduct Found:")
                    print(f"ID: {row[0]}, Name: {row[1]}, Category: {row[2]}, Quantity: {row[3]}, Price: {row[4]}")
                    found = True
                    break

        if not found:
            print("Product ID not found.")
    except FileNotFoundError:
        print("Products file not found.")

def generate_report():
    try:
        with open(PRODUCT_FILE, mode='r') as file:
            reader = csv.reader(file)
            total_quantity = 0
            total_value = 0.0
            print("\nProduct Report:")
            print("\n{:<10} {:<30} {:<20} {:<10} {:<10}".format('ID', 'Name', 'Category', 'Quantity', 'Price'))
            print("=" * 80)
            for row in reader:
                print("{:<10} {:<30} {:<20} {:<10} {:<10}".format(row[0], row[1], row[2], row[3], row[4]))
                total_quantity += int(row[3])
                total_value += int(row[3]) * float(row[4])

            print("=" * 80)
            print(f"Total Quantity: {total_quantity}")
            print(f"Total Inventory Value: Rs. {total_value:.2f}")
    except FileNotFoundError:
        print("Products file not found.")

def export_products():
    output_file = input("Enter the filename to save products (e.g., products_report.txt): ")
    try:
        with open(PRODUCT_FILE, mode='r') as file:
            reader = csv.reader(file)
            with open(output_file, mode='w') as outfile:
                for row in reader:
                    outfile.write(f"ID: {row[0]}, Name: {row[1]}, Category: {row[2]}, Quantity: {row[3]}, Price: {row[4]}\n")
        print(f"Products exported successfully to '{output_file}'.")
    except FileNotFoundError:
        print("Products file not found.")

def import_products():
    input_file = input("Enter the filename to import products from (e.g., new_products.csv): ")
    try:
        with open(input_file, mode='r') as file:
            reader = csv.reader(file)
            with open(PRODUCT_FILE, mode='a', newline='') as products_file:
                writer = csv.writer(products_file)
                for row in reader:
                    writer.writerow(row)
        print(f"Products imported successfully from '{input_file}'.")
    except FileNotFoundError:
        print("Input file not found.")

def main():
    while True:
        print("\nWarehouse Management System")
        print("1. Register User")
        print("2. Authenticate User")
        print("3. Add Product")
        print("4. View Products")
        print("5. Update Product")
        print("6. Delete Product")
        print("7. Search Product")
        print("8. Generate Report")
        print("9. Export Products")
        print("10. Import Products")
        print("11. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            if not authenticate():
                continue
        elif choice == '3':
            add_product()
        elif choice == '4':
            view_products()
        elif choice == '5':
            update_product()
        elif choice == '6':
            delete_product()
        elif choice == '7':
            search_product()
        elif choice == '8':
            generate_report()
        elif choice == '9':
            export_products()
        elif choice == '10':
            import_products()
        elif choice == '11':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
