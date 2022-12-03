import tkinter as tk

from tkinter import ttk


class ConverterFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # create the labels
        self.multiplier_formula_label = ttk.Label(self, text='Multiplier')
        self.discount_formula_label = ttk.Label(self, text='Discount')
        self.markup_formula_label = ttk.Label(self, text='Markup')
        self.gross_profit_formula_label = ttk.Label(self, text='Gross Profit')

        # create the entries
        self.multiplier_formula_entry = ttk.Entry(self)
        self.discount_formula_entry = ttk.Entry(self)
        self.markup_formula_entry = ttk.Entry(self)
        self.gross_profit_formula_entry = ttk.Entry(self)

        # create the copy buttons
        self.multiplier_formula_button = ttk.Button(self, text="Copy")
        self.discount_formula_button = ttk.Button(self, text="Copy")
        self.markup_formula_button = ttk.Button(self, text="Copy")
        self.gross_profit_formula_button = ttk.Button(self, text="Copy")

        self.place_widgets()

        self.pack()

    def place_widgets(self):

        # place the multiplier widgets
        self.multiplier_formula_label.grid(column=0, row=0, sticky='w')
        self.multiplier_formula_entry.grid(column=1, row=0)
        self.multiplier_formula_button.grid(column=2, row=0)

        # place the discount widgets
        self.discount_formula_label.grid(column=0, row=1, sticky='w')
        self.discount_formula_entry.grid(column=1, row=1)
        self.discount_formula_button.grid(column=2, row=1)

        # place the markup widget
        self.markup_formula_label.grid(column=0, row=2, sticky='w')
        self.markup_formula_entry.grid(column=1, row=2)
        self.markup_formula_button.grid(column=2, row=2)

        # place the gross profit widgets
        self.gross_profit_formula_label.grid(column=0, row=3, sticky='w')
        self.gross_profit_formula_entry.grid(column=1, row=3)
        self.gross_profit_formula_button.grid(column=2, row=3)


if __name__ == '__main__':
    root = tk.Tk()

    root.title("Formula Converter")

    frame = ConverterFrame(root)

    root.mainloop()
