import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect('hospital.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        disease TEXT
    )
''')
conn.commit()

# Add patient to DB
def add_patient():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    disease = entry_disease.get()

    if name and age and gender and disease:
        cursor.execute('INSERT INTO patients (name, age, gender, disease) VALUES (?, ?, ?, ?)',
                       (name, age, gender, disease))
        conn.commit()
        messagebox.showinfo("Success", "Patient added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill all fields")

def view_patients():
    top = tk.Toplevel()
    top.title("All Patients")
    cursor.execute('SELECT * FROM patients')
    records = cursor.fetchall()

    text = tk.Text(top)
    text.pack()

    for row in records:
        text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Disease: {row[4]}\n")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_disease.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Hospital Management System")

tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Age").grid(row=1, column=0)
tk.Label(root, text="Gender").grid(row=2, column=0)
tk.Label(root, text="Disease").grid(row=3, column=0)

entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_gender = tk.Entry(root)
entry_disease = tk.Entry(root)

entry_name.grid(row=0, column=1)
entry_age.grid(row=1, column=1)
entry_gender.grid(row=2, column=1)
entry_disease.grid(row=3, column=1)

tk.Button(root, text="Add Patient", command=add_patient).grid(row=4, column=0, pady=10)
tk.Button(root, text="View Patients", command=view_patients).grid(row=4, column=1, pady=10)
tk.Button(root, text="Exit", command=root.quit).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()

# Close DB when done (optional)
conn.close()
