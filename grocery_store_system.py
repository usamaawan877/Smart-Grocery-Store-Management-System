"""
Smart Grocery Store Management System
-------------------------------------
A menu-driven console application that helps a store owner manage
products, stock levels, customer sales and reports.

Data structures used:
    products -> list of dictionaries (one dictionary per product)
    sales    -> list of dictionaries (one dictionary per completed sale)
"""

import math

# Stock level below which a product is flagged as "low stock"
LOW_STOCK_LIMIT = 5

# ---------------------------------------------------------------------------
# Data storage
# ---------------------------------------------------------------------------

# Starter data so the program can be tested immediately.
# New products are added to this list with .append()
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
    {"id": 102, "name": "Bread", "category": "Bakery", "price": 120, "stock": 15},
    {"id": 103, "name": "Eggs (Dozen)", "category": "Dairy", "price": 380, "stock": 4},
    {"id": 104, "name": "Basmati Rice 1kg", "category": "Grains", "price": 450, "stock": 30},
    {"id": 105, "name": "Cooking Oil 1L", "category": "Pantry", "price": 520, "stock": 3},
]

# Every completed sale is stored here as a dictionary
sales = []


# ---------------------------------------------------------------------------
# Input helper functions (validation)
# ---------------------------------------------------------------------------

def get_text(prompt):
    """Keep asking until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Error: input cannot be empty. Please try again.")


def get_int(prompt, minimum=None):
    """Keep asking until the user enters a whole number (>= minimum if given)."""
    while True:
        raw_value = input(prompt).strip()
        try:
            number = int(raw_value)
        except ValueError:
            print("  Error: please enter a valid whole number.")
            continue

        if minimum is not None and number < minimum:
            print(f"  Error: the value must be at least {minimum}.")
            continue
        return number


def get_price(prompt):
    """Keep asking until the user enters a valid price greater than zero."""
    while True:
        raw_value = input(prompt).strip()
        try:
            price = float(raw_value)
        except ValueError:
            print("  Error: please enter a valid number (e.g. 250 or 99.50).")
            continue

        # Reject zero, negatives, and special values such as 'nan' or 'inf'
        if not math.isfinite(price) or price <= 0:
            print("  Error: price must be a number greater than zero.")
            continue
        return price


def find_product_by_id(product_id):
    """Return the product dictionary with this ID, or None if not found."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


# ---------------------------------------------------------------------------
# Display helper functions
# ---------------------------------------------------------------------------

def print_product_table(product_list):
    """Print a list of products as an aligned table."""
    # Size the text columns to fit the longest name / category
    name_width = len("Name")
    category_width = len("Category")
    for product in product_list:
        name_width = max(name_width, len(product["name"]))
        category_width = max(category_width, len(product["category"]))

    header = (f"{'ID':<8}{'Name':<{name_width + 2}}"
              f"{'Category':<{category_width + 2}}{'Price':>12}{'Stock':>8}")
    print(header)
    print("-" * len(header))

    for product in product_list:
        print(f"{product['id']:<8}{product['name']:<{name_width + 2}}"
              f"{product['category']:<{category_width + 2}}"
              f"{product['price']:>12.2f}{product['stock']:>8}")


def print_product_details(product):
    """Print every field of a single product."""
    print(f"  Product ID : {product['id']}")
    print(f"  Name       : {product['name']}")
    print(f"  Category   : {product['category']}")
    print(f"  Price      : {product['price']:.2f}")
    print(f"  Stock      : {product['stock']} units")


# ---------------------------------------------------------------------------
# Menu feature functions
# ---------------------------------------------------------------------------

def add_product():
    """Option 1: add a new product (duplicate IDs are not allowed)."""
    print("\n--- ADD NEW PRODUCT ---")
    product_id = get_int("Enter Product ID: ", minimum=1)

    # Prevent duplicate product IDs
    if find_product_by_id(product_id) is not None:
        print(f"  Error: a product with ID {product_id} already exists.")
        return

    name = get_text("Enter Product Name: ")
    category = get_text("Enter Category: ")
    price = get_price("Enter Price: ")
    stock = get_int("Enter Available Stock: ", minimum=0)

    # Store the product as a dictionary and append it to the list
    new_product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock,
    }
    products.append(new_product)
    print(f"  Success: '{name}' has been added to the store.")


def view_products():
    """Option 2: display all products."""
    print("\n--- ALL PRODUCTS ---")
    if not products:
        print("  No products available yet.")
        return
    print_product_table(products)


def search_product():
    """Option 3: search by product ID or by (part of a) product name."""
    print("\n--- SEARCH PRODUCT ---")
    query = get_text("Enter Product ID or Name: ")

    matches = []
    for product in products:
        # Match by exact ID (only if the query is a number) ...
        id_match = query.isdigit() and product["id"] == int(query)
        # ... or by name (case-insensitive, partial matches allowed)
        name_match = query.lower() in product["name"].lower()
        if id_match or name_match:
            matches.append(product)

    if not matches:
        print(f"  No product found matching '{query}'.")
        return

    print(f"\n  Found {len(matches)} matching product(s):")
    for product in matches:
        print()
        print_product_details(product)


def update_stock():
    """Option 4: add stock to a product or set its stock to a new quantity."""
    print("\n--- UPDATE PRODUCT STOCK ---")
    product_id = get_int("Enter Product ID: ", minimum=1)
    product = find_product_by_id(product_id)

    if product is None:
        print(f"  Error: no product found with ID {product_id}.")
        return

    print(f"  Product: {product['name']} | Current stock: {product['stock']}")
    print("  1. Add stock to the current quantity")
    print("  2. Set stock to a new quantity")
    choice = input("  Choose an option (1/2): ").strip()

    if choice == "1":
        extra = get_int("  Enter quantity to add: ", minimum=1)
        product["stock"] += extra
    elif choice == "2":
        product["stock"] = get_int("  Enter new stock quantity: ", minimum=0)
    else:
        print("  Invalid option. Stock was not changed.")
        return

    print(f"  Stock updated! {product['name']} now has {product['stock']} units.")


def process_sale():
    """Option 5: sell a product to a customer and record the sale."""
    print("\n--- PROCESS CUSTOMER SALE ---")
    product_id = get_int("Enter Product ID: ", minimum=1)
    product = find_product_by_id(product_id)

    # Check that the product exists
    if product is None:
        print(f"  Error: no product found with ID {product_id}.")
        return

    # A product with no stock cannot be sold at all
    if product["stock"] == 0:
        print(f"  Sorry, '{product['name']}' is out of stock.")
        return

    quantity = get_int(f"Enter quantity to buy (available: {product['stock']}): ",
                       minimum=1)

    # Do not allow the sale if the quantity exceeds available stock
    if quantity > product["stock"]:
        print(f"  Sale denied: only {product['stock']} unit(s) of "
              f"'{product['name']}' available, but {quantity} requested.")
        return

    # Calculate total price and deduct the purchased quantity from stock
    total_amount = product["price"] * quantity
    product["stock"] -= quantity

    # Record the completed sale in the separate sales list
    sales.append({
        "product_id": product["id"],
        "product_name": product["name"],
        "quantity_sold": quantity,
        "total_amount": total_amount,
    })

    # Purchase summary
    print("\n  ----- PURCHASE SUMMARY -----")
    print(f"  Product    : {product['name']} (ID {product['id']})")
    print(f"  Unit Price : {product['price']:.2f}")
    print(f"  Quantity   : {quantity}")
    print(f"  Total      : {total_amount:.2f}")
    print(f"  Remaining stock: {product['stock']} units")
    print("  ----------------------------")


def view_sales_records():
    """Option 6: display every completed sale."""
    print("\n--- SALES RECORDS ---")
    if not sales:
        print("  No sales have been made yet.")
        return

    header = (f"{'No.':<6}{'Product ID':<12}{'Product Name':<24}"
              f"{'Qty Sold':>10}{'Total Amount':>16}")
    print(header)
    print("-" * len(header))

    for number, sale in enumerate(sales, start=1):
        print(f"{number:<6}{sale['product_id']:<12}{sale['product_name']:<24}"
              f"{sale['quantity_sold']:>10}{sale['total_amount']:>16.2f}")


def generate_report():
    """Option 7: display a summary report of the whole store."""
    print("\n====================================")
    print("          STORE REPORT")
    print("====================================")

    # Totals calculated by looping through the products and sales
    total_stock = 0
    for product in products:
        total_stock += product["stock"]

    total_revenue = 0
    for sale in sales:
        total_revenue += sale["total_amount"]

    print(f"Total number of products : {len(products)}")
    print(f"Total available stock    : {total_stock} units")
    print(f"Total sales transactions : {len(sales)}")
    print(f"Total revenue generated  : {total_revenue:.2f}")

    # Products with stock below the low-stock limit
    print(f"\nProducts with stock below {LOW_STOCK_LIMIT} units:")
    low_stock_found = False
    for product in products:
        if product["stock"] < LOW_STOCK_LIMIT:
            print(f"  - {product['name']} (ID {product['id']}): "
                  f"{product['stock']} left")
            low_stock_found = True
    if not low_stock_found:
        print("  None - all products are sufficiently stocked.")

    # Highest and lowest priced products (need at least one product)
    if products:
        highest = products[0]
        lowest = products[0]
        for product in products:
            if product["price"] > highest["price"]:
                highest = product
            if product["price"] < lowest["price"]:
                lowest = product

        print(f"\nHighest priced product : {highest['name']} "
              f"({highest['price']:.2f})")
        print(f"Lowest priced product  : {lowest['name']} "
              f"({lowest['price']:.2f})")
    else:
        print("\nNo products available to compare prices.")
    print("====================================")


# ---------------------------------------------------------------------------
# Main program
# ---------------------------------------------------------------------------

def show_menu():
    """Print the main menu."""
    print("\n====================================")
    print("SMART GROCERY STORE SYSTEM")
    print("====================================\n")
    print("1. Add New Product")
    print("2. View All Products")
    print("3. Search Product")
    print("4. Update Product Stock")
    print("5. Process Customer Sale")
    print("6. View Sales Records")
    print("7. Generate Store Report")
    print("8. Exit\n")


def main():
    """Run the menu loop until the user chooses to exit."""
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            process_sale()
        elif choice == "6":
            view_sales_records()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("\nThank you for using the Smart Grocery Store System. Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter a number from 1 to 8.")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram closed. Goodbye!")
