import tkinter as tk

import findbasisvalueframe
import formulaconverterframe
import findformulasframe


class App(tk.Tk):
    FINDFORMULA = 'Find Formula'
    FINDBASIS = 'Find Basis Value'
    CONVERTFORMULA = 'Convert Formula'

    def __init__(self) -> None:
        super().__init__()

        self.current_frame = None

        self.find_basis_value_frame = findbasisvalueframe.FindBasisValueFrame(self)
        self.find_formulas_frame = findformulasframe.FindFormulaFrame(self)
        self.formula_converter_frame = formulaconverterframe.FormulaConverterFrame(self)

        menubar = tk.Menu()
        self.config(menu=menubar)

        view_menu = tk.Menu(menubar, tearoff=False)
        view_menu.add_command(
            label=App.FINDBASIS,
            command=self.load_find_basis_value_frame,
        )
        view_menu.add_command(
            label=App.FINDFORMULA,
            command=self.load_find_formulas_frame,
        )
        view_menu.add_command(
            label=App.CONVERTFORMULA,
            command=self.load_formula_converter_frame,
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
        self.swap_frames(self.find_formulas_frame, App.FINDFORMULA)

    def load_find_basis_value_frame(self):
        self.swap_frames(self.find_basis_value_frame, App.FINDBASIS)

    def load_formula_converter_frame(self):
        self.swap_frames(self.formula_converter_frame, App.CONVERTFORMULA)


if __name__ == '__main__':
    app = App()

    app.mainloop()
