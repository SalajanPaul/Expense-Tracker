import tkinter
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
import matplotlib.pyplot as plt

class ExpenseTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker")
        self.geometry("1300x600")
        self.expenses = []
        self.categories = [
            "Food",
            "Transportation",
            "Utilities",
            "Entertainment",
            "Other",
        ]
        self.category_var = tk.StringVar(self)
        self.category_var.set(self.categories[0])
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Expense Tracker", font=("Helvelica", 20, "bold"))
        self.label.pack(pady=10)

        self.frame_input = tk.Frame(self)
        self.frame_input.pack(pady=10)

        self.expense_label = tk.Label(self.frame_input, text="Expense Amount:", font=("Helvetica", 12))
        self.expense_label.grid(row=0, column=0, pady=5)

        self.item_label = tk.Label(self.frame_input, text="Item Description", font=("Helvetica", 12))
        self.item_label.grid(row=0, column=2, padx=5)

        self.item_entry = tk.Entry(self.frame_input, font=("Helvetica", 12), width=20)
        self.item_entry.grid(row=0, column=3, padx=5)

        self.category_label = tk.Label(self.frame_input, text="Category:", font=("Helvetica", 12))
        self.category_label.grid(row=0, column=4, padx=5)

        self.category_dropdown = ttk.Combobox(self.frame_input, textvariable=self.category_var,
                                              values=self.categories, font=("Helvetica", 12), width=15)
        self.category_dropdown.grid(row=0, column=5, padx=5)

        self.date_label = tk.Label(self.frame_input, text="Date (YYYY-MM-DD):", font=("Helvetica", 12))
        self.date_label.grid(row=0, column=6, padx=5)

        self.date_entry = tk.Entry(self.frame_input, font=("Helvetica", 12), width=15)
        self.date_entry.grid(row=0, column=7, padx=5)

        self.add_button = tk.Button(self, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=5)

        self.frame_list = tk.Frame(self)
        self.frame_list.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.frame_list)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.expense_listbox = tk.Listbox(self.frame_list, font=("Helvetica", 12), width=70, yscrollcommand=self.scrollbar.set)
        self.expense_listbox.pack(pady=5)

        self.scrollbar.config(command=self.expense_listbox.yview)

        self.edit_button = tk.Button(self, text="Edit Expense", command=self.edit_expense)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self, text="Delete Expense", command=self.delete_expenses)
        self.delete_button.pack(pady=5)

        self.total_label = tk.Label(self, text="Total Expenses:", font=("Helvetica", 12))
        self.total_label.pack(pady=5)

        self.show_chart_button = tk.Button(self, text="Show Expenses Chart", command=self.show_expenses_chart)
        self.show_chart_button.pack(pady=5)

        self.update_total_label()

