import calendar
from datetime import date

class CalendarLogic(calendar.HTMLCalendar):
    def __init__(self,today=None):
        super().__init__()
        if today is None:
            today = date.today()
        self.today = today
        self.today_day = today.day
        self.today_month = today.month
        self.today_year = today.year


# date.today().strftime("%d")
# date.today().strftime("%m")
# date.today().strftime("%y")

if __name__ == "__main__":
    cal = CalendarLogic()
    print("Today's date:", cal.today)
    print("Year:", cal.today_year)
    print("Month:", cal.today_month)
    print("Day:", cal.today_day)