import shopping

if __name__ == '__main__':
    list_with_milk = ['tomatoes', 'pastas', 'milk', 'salt']
    list_without_milk = ['tomatoes', 'pastas', 'salt']

    print(shopping.remember_the_milk(list_with_milk))
    print(shopping.remember_the_milk(list_without_milk))