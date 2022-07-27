from datetime import datetime
from rest_framework import status
from django.conf import settings


User = settings.AUTH_USER_MODEL
def format_date_created(model):
    """ This returns the date (day and month) and add the year only if it's not the current year"""
    date = model.date_created
    current_year = datetime.utcnow().year
    if date.year != current_year:
        return date.strftime("%b %d %Y")
    else:
        return date.strftime("%b %d")



