import datetime, calendar

# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message="That day does not exist."):
        super().__init__(message)
        


def meetup(year, month, week, day_of_week):
    weekdays = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}
    first_day = datetime.date(year, month, 1)
    num_week = first_day.weekday()
    _, last_day = calendar.monthrange(year, month)
    start_days = {"first": 1, "second": 8, "third": 15, "fourth": 22, "fifth": 29, "teenth": 13}
    start_day = start_days.get(week)
    result = ()

    if week == "first":
        for i in range(7):
            if num_week > 6:
                num_week = 0 
            if num_week == weekdays[day_of_week]:
                result = datetime.date(year, month, start_day)
                break
            else:
                start_day+=1
                num_week += 1

    elif week == "second":
        for i in range(7):
            if num_week > 6:
                num_week = 0 
            if num_week == weekdays[day_of_week]:
                result = datetime.date(year, month, start_day)
                break
            else:
                start_day+=1
                num_week += 1

    elif week == "third":
        for i in range(7):
            if num_week > 6:
                num_week = 0 
            if num_week == weekdays[day_of_week]:
                result = datetime.date(year, month, start_day)
                break
            else:
                start_day+=1
                num_week += 1

    elif week == "fourth":
        for i in range(7):
            if num_week > 6:
                num_week = 0 
            if num_week == weekdays[day_of_week]:
                result = datetime.date(year, month, start_day)
                break
            else:
                start_day+=1
                num_week += 1 

    elif week == "last":
        _, day = calendar.monthrange(year, month)
        last_day = datetime.date(year, month, day)
        num_week = last_day.weekday()
        for i in range(7):
            if num_week < 0:
                num_week = 6 
            if num_week == weekdays[day_of_week]:
                result = datetime.date(year, month, day)
                break
            else:
                day-=1
                num_week -= 1

    elif week == "teenth":
        day = 13
        weekday = num_week - 2
        if weekday < 0:
            weekday = 7 + weekday 
        for i in range(7):
            if weekday > 6:
                weekday = 0 
            if weekday == weekdays[day_of_week]:
                result = datetime.date(year, month, day)
                break
            else:
                day+=1
                weekday += 1

    elif week == "fifth":
         # Check days 29, 30, 31 for the requested weekday
        found = False
        for day in [29, 30, 31]:
            try:
                test_date = datetime.date(year, month, day)
                if test_date.weekday() == weekdays[day_of_week]:
                    result = test_date
                    found = True
                    break
            except ValueError:
                # Day doesn't exist in this month
                continue
        
        if not found:
            raise MeetupDayException()
    return result


print(meetup(2015, 3, "fifth", "Monday"))# date(2015, 3, 30))