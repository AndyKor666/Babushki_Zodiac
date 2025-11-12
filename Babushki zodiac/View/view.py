import tkinter as tk
from PIL import ImageTk

class ZodiacView:
    def __init__(self, root):
        self.root = root
        self.root.title("Zodiac Finder (MVC)")
        self.root.geometry("500x600")
        self.root.configure(bg="#e6e6e6")

        self.title_label = tk.Label(
            root, text="ZODIAC FINDER", 
            font=("Times New Roman", 20, "italic"), bg="#e6e6e6"
        )
        self.title_label.pack(pady=(20, 10))

        frame = tk.Frame(root, bg="#e6e6e6")
        frame.pack(pady=10)

        tk.Label(frame, text="Day:", font=("Times New Roman", 14), bg="#e6e6e6").grid(row=0, column=0, padx=5)
        self.entry_day = tk.Entry(frame, width=5, font=("Times New Roman", 14), justify="center")
        self.entry_day.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Month:", font=("Times New Roman", 14), bg="#e6e6e6").grid(row=0, column=2, padx=5)
        self.entry_month = tk.Entry(frame, width=5, font=("Times New Roman", 14), justify="center")
        self.entry_month.grid(row=0, column=3, padx=5)

        tk.Label(frame, text="Year:", font=("Times New Roman", 14), bg="#e6e6e6").grid(row=0, column=4, padx=5)
        self.entry_year = tk.Entry(frame, width=8, font=("Times New Roman", 14), justify="center")
        self.entry_year.grid(row=0, column=5, padx=5)

        self.button = tk.Button(
            root, text="PRESS HERE", font=("Times New Roman", 13, "italic"),
            bg="#d9d9d9", relief="raised", borderwidth=2
        )
        self.button.pack(pady=20)

        self.label_result = tk.Label(
            root, text="Enter your birth date",
            font=("Times New Roman", 14, "italic"),
            bg="#e6e6e6", fg="#666666"
        )
        self.label_result.pack(pady=10)

        self.image_label = tk.Label(root, bg="#e6e6e6")
        self.image_label.pack(pady=10)

    def set_result(self, text, color="#1c355e"):
        self.label_result.config(text=text, fg=color)

    def show_image(self, image):
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def clear_image(self):
        self.image_label.config(image="")
        self.image_label.image = None
