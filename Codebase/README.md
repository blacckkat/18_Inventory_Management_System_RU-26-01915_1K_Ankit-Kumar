# Inventory Management System

Ankit Kumar
RU-26-01915
1K

A basic console-based Inventory Management System written in Python 3.

## Features

- Add, view, update, search, and delete inventory items
- Generate item IDs starting at `I101`
- Calculate total stock value
- Report low-stock items (quantity below 5)
- Validate quantities and prices

## Requirements

- Python 3.x or above

## How to Run

From the project directory, run:

```bash
python inventory_management.py
```

## CRUD and Data Structure

The program supports CRUD operations: create, read, update, and delete inventory items. Items are stored in memory as dictionaries inside a list, using the keys `id`, `name`, `quantity`, and `price`. Data is not saved after the program exits.

I took some help for the CRUD operations from internet..!!
