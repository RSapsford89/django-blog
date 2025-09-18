from django.views.generic import TemplateView
import calendar as pycalendar
from datetime import datetime

class MonthlyCalendarView(TemplateView):
    template_name = 'sitecalendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.today()
        year = self.kwargs.get('year', today.year)
        month = self.kwargs.get('month', today.month)
        year = int(year)
        month = int(month)
        cal = pycalendar.HTMLCalendar(pycalendar.MONDAY)
        month_calendar = cal.formatmonth(year, month)
        context.update({
            'today': today,
            'year': year,
            'month': month,
            'month_calendar': month_calendar,
        })
        return context
