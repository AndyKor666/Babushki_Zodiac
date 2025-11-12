from Model.model import ZodiacModel
from View.view import ZodiacView

class ZodiacController:
    def __init__(self, model: ZodiacModel, view: ZodiacView):
        self.model = model
        self.view = view
        self.view.button.config(command=self.on_submit)

    def on_submit(self):
        try:
            d=int(self.view.entry_day.get().strip())
            m=int(self.view.entry_month.get().strip())
            y=int(self.view.entry_year.get().strip())
        except ValueError:
            self.view.set_result("Please enter valid numbers!", "darkred")
            self.view.clear_image()
            return

        if not self.model.is_valid_date(d, m, y):
            self.view.set_result("Invalid date!", "darkred")
            self.view.clear_image()
            return

        zodiac = self.model.get_zodiac(d, m)
        if not zodiac:
            self.view.set_result("Zodiac not found.", "darkred")
            self.view.clear_image()
            return

        self.view.set_result(f"Your Zodiac Sign: {zodiac}")
        try:
            img = self.model.load_image(zodiac)
            self.view.show_image(img)
        except FileNotFoundError:
            self.view.set_result(f"{zodiac} (image not found)", "orange")
            self.view.clear_image()
