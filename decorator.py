import datetime as dt

def with_current_date(func):
    def wrapper(*args, **kwargs):
        current_date = dt.date.today()
        return func(*args, current_date=current_date, **kwargs)
    return wrapper