from operator import itemgetter


def sort_recipes(recipes, by):
    if by!='title' and by!='persons':
        raise ValueError("Expected title or persons as parameter")
    elif by=='title':
        sortedByTitle = sorted(recipes, key=itemgetter('title'))
        return sortedByTitle
    else:
        sortedByPersons = sorted(recipes, key=itemgetter('persons'))
        return sortedByPersons
    