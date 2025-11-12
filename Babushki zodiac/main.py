import tkinter as tk
from Model.model import ZodiacModel
from View.view import ZodiacView
from Controller.controller import ZodiacController

def main():
    root = tk.Tk()
    model = ZodiacModel()
    view = ZodiacView(root)
    controller = ZodiacController(model, view)
    root.mainloop()
if __name__ == "__main__":
    main()
