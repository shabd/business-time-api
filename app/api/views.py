from django.shortcuts import render
import datetime
from datetime import timedelta
import holidays


# Given two dates work out the time difference in secs

ZA_HOLIDAYS = holidays.SouthAfrica(years=2021)


def is_public_holiday(given_datetime):
    if(given_datetime in ZA_HOLIDAYS):
        return True
    return False


def is_weekend(given_datetime):

    #  during a weekday (Monday - Friday)
    weekend = [5, 6]
    if(given_datetime.weekday() in weekend):
        return True

    return False


def is_business_second(given_datetime):

    # Business hours run from 8:00 to 17:00
    start = datetime.time(8, 0, 0)
    end = datetime.time(17, 0, 0)

    given_time = given_datetime.time()

    # A business second is defined as any whole second that elapses after 08:00 and before 17:00
    return start <= given_time < end


def get_business_seconds(start_datetime, end_datetime):

    business_seconds = 0

    while(start_datetime < end_datetime):

        if(is_public_holiday(start_datetime) == False):
            if(is_weekend(start_datetime) == False):
                if(is_business_second(start_datetime)):
                    business_seconds += 1

        start_datetime = start_datetime + timedelta(seconds=1)

    return business_seconds


def business(request, start_time, end_time):
    pass
