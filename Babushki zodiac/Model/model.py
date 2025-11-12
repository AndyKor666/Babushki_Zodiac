import os
from PIL import Image

class ZodiacModel:
    IMAGE_FOLDER = "znaki"
    def __init__(self):
        self.zodiacs = [
            ("Aries",  (3, 21, 4, 19)),
            ("Taurus", (4, 20, 5, 20)),
            ("Gemini", (5, 21, 6, 20)),
            ("Cancer", (6, 21, 7, 22)),
            ("Leo",    (7, 23, 8, 22)),
            ("Virgo",  (8, 23, 9, 22)),
            ("Libra",  (9, 23, 10, 22)),
            ("Scorpio",(10,23,11,21)),
            ("Sagittarius",(11,22,12,21)),
            ("Capricorn",(12,22,1,19)),
            ("Aquarius",(1,20,2,18)),
            ("Pisces",(2,19,3,20))
        ]
    def is_valid_date(self, day: int, month: int, year: int) -> bool:
        if year < 1900 or year > 2100: return False
        if month < 1 or month > 12: return False
        days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        return 1 <= day <= days[month]

    def get_zodiac(self, day: int, month: int) -> str | None:
        for sign, (m1, d1, m2, d2) in self.zodiacs:
            if (month == m1 and day >= d1) or (month == m2 and day <= d2):
                return sign
        return None

    def get_image_path(self, zodiac: str) -> str:
        return os.path.join(self.IMAGE_FOLDER, f"{zodiac.lower()}.png")

    def load_image(self, zodiac: str, size=(230, 300)):
        path = self.get_image_path(zodiac)
        if os.path.exists(path):
            img = Image.open(path)
            img = img.resize(size)
            return img
        else:
            raise FileNotFoundError(f"Image for {zodiac} not found!")
