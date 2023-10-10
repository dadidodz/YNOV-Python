def remember_the_milk(shopping_list):
    if 'milk' not in shopping_list and shopping_list:
        shopping_list.append('milk')
    return shopping_list

def clean_list(shopping_list):
    i = 0
    if not shopping_list:
        return shopping_list
    while i < len(shopping_list):
        shopping_list[i] = shopping_list[i].strip()
        i+=1
    remember_the_milk(shopping_list)
    i=0
    while i < len(shopping_list):
        shopping_list[i] = shopping_list[i].capitalize()
        shopping_list[i] = f'{i+1}/ ' + shopping_list[i]
        i+=1    
           
    return shopping_list