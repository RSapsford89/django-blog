import calendar
from datetime import date, datetime

class CalendarLogic(calendar.HTMLCalendar):
    def __init__(self,today=None):
        super().__init__()
        if today is None:
            today = date.today()
        self.today = today
        self.today_day = today.day
        self.today_month = today.month
        self.today_year = today.year

    def formatHtmlDates(self,year,month,day):
        #if the year and month are this year's year and month, 
        #find the day in the htmlcalendar and add the highlight class
        if datetime.now().strftime("%Y-%m-%d") == date.today:
            return f'<td class ="today">{day}</td>'
        else:
            print(f"failed {self.today} and {datetime.now().strftime("%Y-%m-%d")}")
    

# date.today().strftime("%d")
# date.today().strftime("%m") # returns '09' for Sept
# date.today().strftime("%d%m%y") #returns 070925 for 7th Sep 25
#datetime_today=datetime.now()
#datetime_today.strftime("%Y-%m-%d")

if __name__ == "__main__":
    cal = CalendarLogic()

    print("Today's date:", cal.today)
    print("Year:", cal.today_year)
    print("Month:", cal.today_month)
    print("Day:", cal.today_day)
    CalendarLogic.formatHtmlDates(0,2025,9,5)