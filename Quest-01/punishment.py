def do_punishment(first_part, second_part, nb_lines):
    first_part = first_part.strip()
    second_part = second_part.strip()
    if second_part.endswith('.')==False:
        second_part += '.'

    phrase = f"{first_part} {second_part}"
    phrase = ' '.join([phrase]*nb_lines)
    return phrase