import sqlite3
import time
from prettytable import PrettyTable
import tkinter as tk

# Connect to the database
conn = sqlite3.connect('results.db')
cursor = conn.cursor()

# Create a Tkinter window
window = tk.Tk()
window.title("INVENTORY")


# Create a Tkinter Text widget to display the table
table_text = tk.Text(window, width=40, height=20)
table_text.pack()
while True:
    cursor.execute("SELECT * FROM class_counts ORDER BY Products ASC,Available ASC")

    # Fetch the rows
    rows = cursor.fetchall()

    # Create a table instance
    table = PrettyTable()
    table.field_names = ["Products", "Available","InStock"]

    # Add rows to the table
    for row in rows:
        table.add_row(row)

    # Clear the Text widget
    table_text.delete('1.0', tk.END)

    # Insert the table into the Text widget
    table_text.insert(tk.END, str(table))

    # Update the Tkinter window
    window.update()

    # Delay between iterations (e.g., 1 second)
    time.sleep(1)

# Close the cursor and connection
cursor.close()
conn.close()

