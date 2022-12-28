import tkinter as tk

import adjustformula
import basisvalue
import convertformula
import calculateformulas


class App(tk.Tk):
    CALCULATEFORMULA = 'Calculate Formula'
    FINDBASIS = 'Find Basis Value'
    CONVERTFORMULA = 'Convert Formula'
    ADJUSTFORMULA = 'Adjust Formula'

    def __init__(self) -> None:
        super().__init__()

        self.current_frame = None

        self.find_basis_value_frame = basisvalue.BasisValue(self)
        self.find_formulas_frame = calculateformulas.CalculateFormulas(self)
        self.formula_converter_frame = convertformula.ConvertFormula(self)
        self.adjust_formula_frame = adjustformula.AdjustFormula(self)

        menubar = tk.Menu()
        self.config(menu=menubar)

        view_menu = tk.Menu(menubar, tearoff=False)
        view_menu.add_command(
            label=App.FINDBASIS,
            command=self.load_find_basis_value_frame,
        )
        view_menu.add_command(
            label=App.CALCULATEFORMULA,
            command=self.load_find_formulas_frame,
        )
        view_menu.add_command(
            label=App.CONVERTFORMULA,
            command=self.load_formula_converter_frame,
        )
        view_menu.add_command(
            label=App.ADJUSTFORMULA,
            command=self.load_adjust_formula_frame,
        )

        menubar.add_cascade(
            label='View',
            menu=view_menu,
            underline=0
        )

        self.load_formula_converter_frame()

    def swap_frames(self, frame, title):
        if self.current_frame is not None:
            self.current_frame.forget()
        self.current_frame = frame
        self.current_frame.pack(padx=10, pady=10)
        self.title('Pricing Tool - ' + title)

    def load_find_formulas_frame(self):
        self.swap_frames(self.find_formulas_frame, App.CALCULATEFORMULA)

    def load_find_basis_value_frame(self):
        self.swap_frames(self.find_basis_value_frame, App.FINDBASIS)

    def load_formula_converter_frame(self):
        self.swap_frames(self.formula_converter_frame, App.CONVERTFORMULA)

    def load_adjust_formula_frame(self):
        self.swap_frames(self.adjust_formula_frame, App.ADJUSTFORMULA)


if __name__ == '__main__':
    app = App()

    app.mainloop()
