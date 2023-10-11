import datetime as dt
from decorator import with_current_date

@with_current_date
def log_message(message: str, current_date: dt.date):
    # this is an example function
    # you can imagine any other functions
    return f'{current_date}: {message}'

if __name__ == '__main__':
    print(log_message('hello'))
    print(log_message('world'))