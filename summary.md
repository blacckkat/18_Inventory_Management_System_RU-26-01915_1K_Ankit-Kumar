# Inventory Management System

## Project Overview

The Inventory Management System is a console-based Python 3 application used to manage products in an inventory.

The system allows the user to:

- Add new items
- View all inventory items
- Update item details
- Search for items
- Delete items
- Calculate total stock value
- Generate a low-stock report

Each item is stored as a dictionary inside a list. Every dictionary contains:

- `id`
- `name`
- `quantity`
- `price`

Item IDs start from `I101` and increase automatically for every new item. An item is considered low stock when its quantity is below `5`.

## Main Concepts Used

This project uses the following Python concepts:

- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- User input
- String formatting
- Exception handling
- CRUD operations

## CRUD Operations

CRUD stands for:

- **Create** – Adding a new inventory item
- **Read** – Viewing and searching inventory items
- **Update** – Changing the details of an existing item
- **Delete** – Removing an item from the inventory

The project implements CRUD using separate functions:

- `add_item()` performs Create
- `view_items()` and `search_items()` perform Read
- `update_item()` performs Update
- `delete_item()` performs Delete

## How the Program Works

When the program starts, it displays a menu. The user selects an option by entering a number.

The main menu includes options for:

1. Adding an item
2. Viewing items
3. Updating an item
4. Searching for an item
5. Deleting an item
6. Calculating total stock value
7. Displaying the low-stock report
0. Exiting the program

The program continues running inside a loop until the user selects the exit option.

## Difficulties Faced and How They Were Overcome

One of the main difficulties I faced while building this project was understanding the CRUD concept clearly. At first, I was confused about how the four operations were connected to an inventory system and how each operation should modify or access the list of dictionaries.

I got especially stuck while implementing the Update and Delete operations. I needed to understand how to find a particular item using its ID, change only its required values, and remove the correct dictionary from the list without affecting other items.

To overcome this difficulty, I used internet resources, tutorials, documentation, and programming examples to study the CRUD concept in more detail. I compared different examples and carefully analyzed how Create, Read, Update, and Delete operations are implemented in Python applications.

This research helped me understand that CRUD is not a single Python feature. It is a structured way of organizing the basic operations performed on data. I learned that:

- Create means adding a new dictionary to the list.
- Read means displaying or searching data from the list.
- Update means locating a dictionary and changing its values.
- Delete means finding a dictionary and removing it from the list.

After understanding this structure, I divided the program into separate functions. This made the code easier to understand, test, and maintain.

Another challenge was validating user input. Quantity had to be a non-negative whole number, while price had to be a non-negative number. I solved this by using validation functions and `try-except` blocks to handle invalid input safely.

I also had to make sure that item IDs were generated sequentially. I solved this by starting the ID counter at `101` and increasing it after every successful item addition.

## Data Structure Example

An item is stored like this:

```python
{
    "id": "I101",
    "name": "Pen",
    "quantity": 50,
    "price": 10
}
```

Multiple items are stored inside a list:

```python
items = [
    {
        "id": "I101",
        "name": "Pen",
        "quantity": 50,
        "price": 10
    },
    {
        "id": "I102",
        "name": "Notebook",
        "quantity": 3,
        "price": 40
    }
]
```

## Stock Value Calculation

The stock value of an item is calculated using:

```text
quantity × price
```

For example:

```text
Pen: 50 × 10 = 500
Notebook: 3 × 40 = 120
Total stock value = 620
```

## Low-Stock Report

The program displays an item in the low-stock report when:

```text
quantity < 5
```

For example, an item with quantity `3` is considered low stock, but an item with quantity `5` is not considered low stock.

## Validation

The program validates the following inputs:

- Item name cannot be empty.
- Quantity must be a non-negative whole number.
- Price must be a non-negative number.
- Invalid item IDs are handled with an error message.
- Invalid menu choices are rejected.

## Example Workflow

A normal workflow could be:

1. Add a Pen with quantity `50` and price `10`.
2. Add a Notebook with quantity `3` and price `40`.
3. Calculate the total stock value.
4. Display the low-stock report.
5. Delete the Pen.
6. Exit the program.

The total stock value will be:

```text
Pen: 500
Notebook: 120
Total stock value: 620
```

The low-stock report will display:

```text
Low stock (below 5): I102 | Notebook | Qty: 3
```

## Limitations

This project stores data only in memory. When the program is closed, all inventory data is lost.

It does not currently use:

- A database
- A file for permanent storage
- User login authentication
- Multiple user roles
- A graphical user interface

## Possible Future Improvements

The project could be improved by adding:

- File-based data storage using JSON or CSV
- A database such as SQLite
- Login and authentication
- Sorting and filtering options
- A graphical user interface
- More detailed reports
- Exporting inventory data to a file

## Common Viva Questions and Answers

### What is CRUD?

CRUD stands for Create, Read, Update, and Delete. These are the four basic operations used to manage data.

### Why is a list used in this project?

A list is used to store multiple inventory items in an ordered collection.

### Why is a dictionary used for each item?

A dictionary stores data using key-value pairs. It makes each item's details easy to access using keys such as `id`, `name`, `quantity`, and `price`.

### Why are functions used?

Functions divide the program into smaller, reusable sections. They make the code easier to understand, test, and maintain.

### How are item IDs generated?

The program starts with the numeric value `101`. It creates IDs such as `I101`, `I102`, and `I103`, increasing the number after every successful addition.

### What is the low-stock condition?

An item is considered low stock when its quantity is less than `5`.

### Why is exception handling used?

Exception handling prevents the program from crashing when the user enters invalid data, such as text instead of a number.

### What happens when an invalid item ID is entered?

The program searches for the ID. If it does not exist, it displays an item-not-found message.

### Is the data permanently stored?

No. The data is stored only in memory and is lost when the program exits.

### What type of application is this?

It is a console-based application written in Python 3.

## Conclusion

This project demonstrates how Python can be used to create a simple inventory management application. It helped me understand lists, dictionaries, functions, validation, loops, calculations, and CRUD operations.

The biggest learning outcome was understanding how CRUD operations organize the way data is added, viewed, modified, and deleted. The project also improved my problem-solving skills and my ability to break a larger problem into smaller functions.