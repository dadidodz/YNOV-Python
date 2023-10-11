import datetime as dt
import datetime_utils

if __name__ == '__main__':
    print(datetime_utils.parse_time('31/07/2022'))
    print(datetime_utils.format_date(dt.date(2022, 7, 31)))