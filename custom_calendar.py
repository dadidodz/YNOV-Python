semaine = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    7 : 'Sunday',
}

def day_from_number(day_number):
    if day_number == None or 0>day_number>8:
        return None
    key_list = list(semaine.keys())
    if day_number not in key_list:
        return None
    if 0<day_number<=len(key_list):
        return semaine[day_number]
    else:
        return None

def day_to_number(day):
    key_list = list(semaine.keys())
    val_list = list(semaine.values())
    if day not in val_list:
        return None
    else:
        position = val_list.index(day)
        if 0<position<8:
            return (key_list[position])
