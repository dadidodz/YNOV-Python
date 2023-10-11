def create_person(first_name, last_name, /, age, gender, *, size=1.83, job='taxidermist'):
    person = {
    'first_name': first_name,
    'last_name': last_name,
    'age': age,
    'gender': gender,
    'size': size,
    'job': job,
    }
    return person