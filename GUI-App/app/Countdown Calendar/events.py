from datetime import date, datetime
import database

from collections import OrderedDict

def get_events() :

    return database.query('events','s')

def day_between_dates(date1, date2) :
    time_between = str(date1-date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

def add_event(event, date) :
    datas = [
        'event',
        'date'
    ]

    values = [
        event,
        date + ' 00:00'
    ]
    if database.query('events', 'a', data = datas, value = values) :
        print("Adding event succesfuly!")
