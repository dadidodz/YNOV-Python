def do_punishment(first_part, second_part, nb_lines):
    first_part = first_part.strip()
    second_part = second_part.strip()
    phrase = first_part + ' ' + second_part
    if phrase.endswith('.')==False:
        phrase+='.'
   
    phrase *= nb_lines
    phrase.rstrip()
    return phrase
    