# 🛒 Smart Grocery Store Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Level](https://img.shields.io/badge/Level-Beginner-green)
![Topics](https://img.shields.io/badge/Topics-lists%20%7C%20dictionaries%20%7C%20functions-orange)

## 📌 Project Overview

This repository contains a console-based Python application that helps a local grocery store owner keep track of **products, prices, available stock and sales**. All data is stored in memory using **lists of dictionaries**, and the program runs from a menu until the user chooses to exit.

| # | Application | File | Main Topic |
|---|-------------|------|------------|
| 1 | Smart Grocery Store Management System | `grocery_store_system.py` | Lists, dictionaries, functions, loops |

## 📁 Project Structure

```
smart-grocery-store-system/
├── grocery_store_system.py
└── README.md
```

---

## 🏪 Smart Grocery Store Management System

### Description
A menu-driven application that lets the store owner add products, view and search inventory, update stock, process customer sales, review sales records and generate a store report.

### Application Menu

```
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

### Data Structures

**Products** (list of dictionaries)

```python
products = [
    {"id": 101, "name": "Milk", "category": "Dairy", "price": 250, "stock": 20}
]
```

**Sales records** (separate list of dictionaries)

```python
sales = [
    {"product_id": 101, "product_name": "Milk", "quantity_sold": 3, "total_amount": 750}
]
```

| Product Key | Meaning | Sales Key | Meaning |
|-------------|---------|-----------|---------|
| `id` | Unique product ID | `product_id` | ID of the product sold |
| `name` | Product name | `product_name` | Name of the product sold |
| `category` | Product category | `quantity_sold` | Units sold |
| `price` | Price per unit | `total_amount` | Price × quantity |
| `stock` | Units available | | |

> The program starts with 5 sample products so it can be tested immediately. To start with an empty store, set `products = []`.

### Features

| # | Feature | What it does |
|---|---------|--------------|
| 1 | ➕ Add New Product | Collects ID, name, category, price and stock, then adds the dictionary with `.append()`. **Duplicate IDs are rejected.** |
| 2 | 📋 View All Products | Shows every product in an aligned table. |
| 3 | 🔍 Search Product | Finds a product by **ID** or by **full/partial name** (case-insensitive) and shows complete details. |
| 4 | 📦 Update Product Stock | **Adds** stock to the current quantity or **sets** a new quantity, then shows the updated stock. |
| 5 | 💰 Process Customer Sale | Checks the product exists and has enough stock, calculates the total, deducts stock and prints a purchase summary. |
| 6 | 🧾 View Sales Records | Lists every completed sale with a running number. |
| 7 | 📊 Generate Store Report | Totals, low-stock products and highest/lowest priced products. |
| 8 | 🚪 Exit | Ends the program. |

### Store Report Includes
- Total number of products
- Total available stock
- Total sales transactions
- Total revenue generated
- Products with stock **below 5 units**
- Product with the **highest price**
- Product with the **lowest price**

### Concepts Used
`list`, `dict`, `.append()`, custom functions with parameters and `return`, `while True` loop, `for` loop, `enumerate()`, `if / elif / else`, `try / except`, comparison and logical operators, f-string formatting (`:.2f`, `:<10`, `:>12`), string methods (`.strip()`, `.lower()`, `.isdigit()`), constants (`LOW_STOCK_LIMIT`), `math.isfinite()`, `if __name__ == "__main__"`

### Functions Overview

| Function | Purpose |
|----------|---------|
| `get_text()` | Asks until the user enters non-empty text |
| `get_int()` | Asks until the user enters a valid whole number (with optional minimum) |
| `get_price()` | Asks until the user enters a valid price greater than zero |
| `find_product_by_id()` | Loops through products and returns the match, or `None` |
| `print_product_table()` | Prints products as an aligned table |
| `print_product_details()` | Prints all details of one product |
| `add_product()` | Menu option 1 |
| `view_products()` | Menu option 2 |
| `search_product()` | Menu option 3 |
| `update_stock()` | Menu option 4 |
| `process_sale()` | Menu option 5 |
| `view_sales_records()` | Menu option 6 |
| `generate_report()` | Menu option 7 |
| `show_menu()` | Prints the main menu |
| `main()` | Runs the menu loop until exit |

### ▶️ How to Run
```bash
python grocery_store_system.py
```

On some systems use `python3` instead of `python`.

---

## 🖥️ Sample Execution

**✅ Add a New Product**
```
--- ADD NEW PRODUCT ---
Enter Product ID: 106
Enter Product Name: Soap
Enter Category: Hygiene
Enter Price: 150
Enter Available Stock: 12
  Success: 'Soap' has been added to the store.
```

**❌ Duplicate Product ID**
```
--- ADD NEW PRODUCT ---
Enter Product ID: 101
  Error: a product with ID 101 already exists.
```

**⚠️ Invalid Input While Adding**
```
--- ADD NEW PRODUCT ---
Enter Product ID: abc
  Error: please enter a valid whole number.
Enter Product ID: 107
Enter Product Name: Tea
Enter Category: Beverages
Enter Price: abc
  Error: please enter a valid number (e.g. 250 or 99.50).
Enter Price: -5
  Error: price must be a number greater than zero.
Enter Price: 300
Enter Available Stock: -3
  Error: the value must be at least 0.
Enter Available Stock: 10
  Success: 'Tea' has been added to the store.
```

**📋 View All Products**
```
--- ALL PRODUCTS ---
ID      Name              Category          Price   Stock
---------------------------------------------------------
101     Milk              Dairy            250.00      20
102     Bread             Bakery           120.00      15
103     Eggs (Dozen)      Dairy            380.00       4
104     Basmati Rice 1kg  Grains           450.00      30
105     Cooking Oil 1L    Pantry           520.00       3
106     Soap              Hygiene          150.00      12
107     Tea               Beverages        300.00      10
```

**🔍 Search by ID**
```
--- SEARCH PRODUCT ---
Enter Product ID or Name: 101

  Found 1 matching product(s):

  Product ID : 101
  Name       : Milk
  Category   : Dairy
  Price      : 250.00
  Stock      : 20 units
```

**🔍 Search by Name (partial, case-insensitive)**
```
--- SEARCH PRODUCT ---
Enter Product ID or Name: eggs

  Found 1 matching product(s):

  Product ID : 103
  Name       : Eggs (Dozen)
  Category   : Dairy
  Price      : 380.00
  Stock      : 4 units
```

**❌ Product Not Found**
```
--- SEARCH PRODUCT ---
Enter Product ID or Name: xyz
  No product found matching 'xyz'.
```

**📦 Update Stock: Add Quantity**
```
--- UPDATE PRODUCT STOCK ---
Enter Product ID: 103
  Product: Eggs (Dozen) | Current stock: 4
  1. Add stock to the current quantity
  2. Set stock to a new quantity
  Choose an option (1/2): 1
  Enter quantity to add: 10
  Stock updated! Eggs (Dozen) now has 14 units.
```

**📦 Update Stock: Set New Quantity**
```
--- UPDATE PRODUCT STOCK ---
Enter Product ID: 104
  Product: Basmati Rice 1kg | Current stock: 30
  1. Add stock to the current quantity
  2. Set stock to a new quantity
  Choose an option (1/2): 2
  Enter new stock quantity: 25
  Stock updated! Basmati Rice 1kg now has 25 units.
```

**✅ Successful Sale**
```
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

**❌ Sale Denied (Not Enough Stock)**
```
--- PROCESS CUSTOMER SALE ---
Enter Product ID: 102
Enter quantity to buy (available: 15): 50
  Sale denied: only 15 unit(s) of 'Bread' available, but 50 requested.
```

**❌ Out of Stock**
```
--- PROCESS CUSTOMER SALE ---
Enter Product ID: 105
  Sorry, 'Cooking Oil 1L' is out of stock.
```

**❌ Unknown Product ID**
```
--- PROCESS CUSTOMER SALE ---
Enter Product ID: 777
  Error: no product found with ID 777.
```

**⚠️ Invalid Quantity**
```
--- PROCESS CUSTOMER SALE ---
Enter Product ID: 102
Enter quantity to buy (available: 15): 0
  Error: the value must be at least 1.
Enter quantity to buy (available: 15): abc
  Error: please enter a valid whole number.
Enter quantity to buy (available: 15): 2

  ----- PURCHASE SUMMARY -----
  Product    : Bread (ID 102)
  Unit Price : 120.00
  Quantity   : 2
  Total      : 240.00
  Remaining stock: 13 units
  ----------------------------
```

**🧾 View Sales Records**
```
--- SALES RECORDS ---
No.   Product ID  Product Name              Qty Sold    Total Amount
--------------------------------------------------------------------
1     101         Milk                             3          750.00
2     105         Cooking Oil 1L                   3         1560.00
3     102         Bread                            2          240.00
```

**📊 Store Report**
```
====================================
          STORE REPORT
====================================
Total number of products : 7
Total available stock    : 91 units
Total sales transactions : 3
Total revenue generated  : 2550.00

Products with stock below 5 units:
  - Cooking Oil 1L (ID 105): 0 left

Highest priced product : Cooking Oil 1L (520.00)
Lowest priced product  : Bread (120.00)
====================================
```

**⚠️ Empty Store**
```
--- ALL PRODUCTS ---
  No products available yet.

--- SALES RECORDS ---
  No sales have been made yet.

====================================
          STORE REPORT
====================================
Total number of products : 0
Total available stock    : 0 units
Total sales transactions : 0
Total revenue generated  : 0.00

Products with stock below 5 units:
  None - all products are sufficiently stocked.

No products available to compare prices.
====================================
```

---

## 🧪 Testing Summary

| Feature | Scenario Tested | Result |
|---------|-----------------|--------|
| Add Product | Valid product added with `.append()` | ✅ |
| Add Product | Duplicate product ID rejected | ✅ |
| Add Product | Empty / non-numeric / negative / zero input rejected | ✅ |
| View Products | Aligned table of all products | ✅ |
| View Products | Empty store message | ✅ |
| Search | Search by ID | ✅ |
| Search | Search by partial name (case-insensitive) | ✅ |
| Search | Product not found message | ✅ |
| Update Stock | Add quantity to current stock | ✅ |
| Update Stock | Set a new stock quantity | ✅ |
| Update Stock | Unknown product ID | ✅ |
| Sale | Successful sale, total calculated, stock deducted | ✅ |
| Sale | Quantity greater than stock denied | ✅ |
| Sale | Out-of-stock product denied | ✅ |
| Sale | Unknown product ID / invalid quantity | ✅ |
| Sales Records | Sales recorded and listed | ✅ |
| Report | Totals, revenue, low stock, highest/lowest price | ✅ |
| Report | Empty store handled without crashing | ✅ |
| Menu | Invalid menu choice handled; program runs until Exit | ✅ |

## 🛠️ Requirements

- Python 3.x (3.6 or higher)
- Any terminal and a code editor (VS Code, PyCharm, etc.)
- No external libraries needed (only the built-in `math` module)

## 👤 Author

**Usama Malik** — Smart Grocery Store Management System
