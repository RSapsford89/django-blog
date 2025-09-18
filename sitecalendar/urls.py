from django.urls import path
from .views import MonthlyCalendarView

urlpatterns = [
    path('', MonthlyCalendarView.as_view(), name='sitecalendar'),
    path('<int:year>/<int:month>/', MonthlyCalendarView.as_view(), name='monthly_calendar_by_date'),
]
