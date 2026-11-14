# Smart Grocery Store Management System

A menu-driven Python console application that helps a local grocery store owner manage products, prices, stock levels and customer sales. All data is kept in memory using **lists of dictionaries**.

---

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [How to Run](#how-to-run)
4. [Application Menu](#application-menu)
5. [Data Structures](#data-structures)
6. [Functions Overview](#functions-overview)
7. [Input Validation](#input-validation)
8. [Sample Session](#sample-session)
9. [Project Structure](#project-structure)
10. [Possible Improvements](#possible-improvements)
11. [Author](#author)

---

## Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Add New Product** | Enter ID, name, category, price and stock. The product is stored as a dictionary and added with `.append()`. Duplicate product IDs are rejected. |
| 2 | **View All Products** | Displays every product in an aligned table (ID, name, category, price, stock). |
| 3 | **Search Product** | Search by exact ID or by full/partial name (case-insensitive). Shows complete details, or a message if nothing is found. |
| 4 | **Update Product Stock** | Add stock to the current quantity, or set a completely new quantity. Shows the updated stock. |
| 5 | **Process Customer Sale** | Checks the product exists and has enough stock, calculates the total, deducts stock, records the sale and prints a purchase summary. |
| 6 | **View Sales Records** | Lists every completed sale (product ID, name, quantity sold, total amount). |
| 7 | **Generate Store Report** | Total products, total stock, total transactions, total revenue, low-stock products (below 5 units), and the highest and lowest priced products. |
| 8 | **Exit** | Closes the program. |

---

## Requirements

- **Python 3.6 or higher** (uses f-strings)
- No external libraries needed. Only the built-in `math` module is used.

---

## How to Run

1. Save the code as `grocery_store_system.py`.
2. Open a terminal in the same folder.
3. Run:

```bash
python grocery_store_system.py
```

On some systems you may need to use `python3` instead:

```bash
python3 grocery_store_system.py
```

The program keeps running until you choose **8. Exit** (or press `Ctrl + C`).

---

## Application Menu

```text
====================================
SMART GROCERY STORE SYSTEM
====================================

1. Add New Product
2. View All Products
3. Search Product
4. Update Product Stock
5. Process Customer Sale
6. View Sales Records
7. Generate Store Report
8. Exit

Enter your choice:
```

---

## Data Structures

### Products: list of dictionaries

```python
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20},
]
```

| Key | Type | Meaning |
|-----|------|---------|
| `id` | `int` | Unique product ID |
| `name` | `str` | Product name |
| `category` | `str` | Product category |
| `price` | `float` / `int` | Price per unit |
| `stock` | `int` | Units currently available |

### Sales: list of dictionaries

```python
sales = [
    {"product_id": 101, "product_name": "Milk", "quantity_sold": 3, "total_amount": 750},
]
```

| Key | Type | Meaning |
|-----|------|---------|
| `product_id` | `int` | ID of the product sold |
| `product_name` | `str` | Name of the product sold |
| `quantity_sold` | `int` | Units sold in this transaction |
| `total_amount` | `float` / `int` | Price × quantity |

> The program starts with five sample products so it can be tested immediately. To start with an empty store, change the list to `products = []`.

---

## Functions Overview

### Input helpers

| Function | Purpose |
|----------|---------|
| `get_text(prompt)` | Keeps asking until the user enters non-empty text. |
| `get_int(prompt, minimum)` | Keeps asking until the user enters a valid whole number (optionally at or above a minimum). |
| `get_price(prompt)` | Keeps asking until the user enters a valid price greater than zero. |
| `find_product_by_id(product_id)` | Loops through `products` and returns the matching dictionary, or `None`. |

### Display helpers

| Function | Purpose |
|----------|---------|
| `print_product_table(product_list)` | Prints products as an aligned table. |
| `print_product_details(product)` | Prints all fields of a single product. |

### Menu features

| Function | Menu option |
|----------|-------------|
| `add_product()` | 1: Add New Product |
| `view_products()` | 2: View All Products |
| `search_product()` | 3: Search Product |
| `update_stock()` | 4: Update Product Stock |
| `process_sale()` | 5: Process Customer Sale |
| `view_sales_records()` | 6: View Sales Records |
| `generate_report()` | 7: Generate Store Report |

### Program control

| Function | Purpose |
|----------|---------|
| `show_menu()` | Prints the main menu. |
| `main()` | Runs the menu loop until the user exits. |

---

## Input Validation

The program handles invalid input without crashing:

- **Empty text:** rejected, and the user is asked again.
- **Non-numeric values** where a number is expected (ID, price, stock, quantity): rejected with an error message.
- **Negative or zero values:** price must be greater than zero; stock may be `0` or more; sale and stock-addition quantities must be at least `1`.
- **Special float values** such as `nan` and `inf`: rejected as invalid prices.
- **Duplicate product IDs:** the new product is not added.
- **Unknown product IDs:** an error message is shown for updates and sales.
- **Insufficient stock:** the sale is denied and stock is left unchanged.
- **Out-of-stock products:** cannot be sold.
- **Invalid menu choice:** an error message is shown and the menu is displayed again.
- **Empty store:** the report and product views handle having no products without crashing.

---

## Sample Session

### Processing a sale

```text
--- PROCESS CUSTOMER SALE ---
Enter Product ID: 101
Enter quantity to buy (available: 20): 3

  ----- PURCHASE SUMMARY -----
  Product    : Milk (ID 101)
  Unit Price : 250.00
  Quantity   : 3
  Total      : 750.00
  Remaining stock: 17 units
  ----------------------------
```

### Sale denied (not enough stock)

```text
--- PROCESS CUSTOMER SALE ---
Enter Product ID: 101
Enter quantity to buy (available: 20): 50
  Sale denied: only 20 unit(s) of 'Milk' available, but 50 requested.
```

### Viewing all products

```text
--- ALL PRODUCTS ---
ID      Name              Category          Price   Stock
---------------------------------------------------------
101     Milk              Dairy            250.00      20
102     Bread             Bakery           120.00      15
103     Eggs (Dozen)      Dairy            380.00       4
104     Basmati Rice 1kg  Grains           450.00      30
105     Cooking Oil 1L    Pantry           520.00       3
```

### Store report

```text
====================================
          STORE REPORT
====================================
Total number of products : 6
Total available stock    : 79 units
Total sales transactions : 2
Total revenue generated  : 2310.00

Products with stock below 5 units:
  - Cooking Oil 1L (ID 105): 0 left

Highest priced product : Cooking Oil 1L (520.00)
Lowest priced product  : Bread (120.00)
====================================
```

---

## Project Structure

```text
grocery-store-system/
├── grocery_store_system.py   # Main application
└── README.md                 # Project documentation
```

---

## Possible Improvements

- Save and load products and sales from a JSON or CSV file so data persists between runs.
- Add a feature to delete or edit product details (name, price, category).
- Support multiple items in a single customer sale (a shopping cart).
- Record the date and time of each sale.
- Add a bill or receipt export.

---

## Author

**Usama Malik**
