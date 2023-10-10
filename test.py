import custom_calendar

if __name__ == '__main__':
    print(custom_calendar.day_from_number(2))
    print(custom_calendar.day_from_number(1))
    print(custom_calendar.day_from_number(1000))
    print(custom_calendar.day_to_number('Sunday'))
    print(custom_calendar.day_to_number('invalid day'))