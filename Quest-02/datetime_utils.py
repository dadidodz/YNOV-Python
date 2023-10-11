import datetime as dt

def parse_time(time_str):
     return dt.datetime.strptime(time_str, "%d/%m/%Y")

def format_date(date):
    return date.strftime("%A %d %B %Y")