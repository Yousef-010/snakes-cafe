#  the menu of the titles in the restaurant
the_menu = [
    {
        'title': 'Appetizers',
        'subtitle': [
            'Wings',
            'Cookies',
            'Spring Rolls'
        ]
    },
    {
        'title': 'Entrees',
        'subtitle': [
            'Salmon',
            'Steak',
            'Meat Tornado',
            'A Literal Garden'
        ]
    },
    {
        'title': 'Desserts',
        'subtitle': [
            'Ice Cream',
            'Cake',
            'Pie'
        ]
    },
    {
        'title': 'Drinks',
        'subtitle': [
            'Coffee',
            'Tea',
            'Unicorn Tears'
        ]
    }
]

print(
    '**************************************\n**  Welcome to the Snakes Cafe!   **\n**  Please see our menu below.  **\n** To quit at any time, type "quit" **\n**************************************')


# print out the all menu
def print_menu():
    for x in the_menu:
        print(x['title'])
        print('---------')
        for y in x['subtitle']:
            print(y)
        print('\n')


print_menu()

all_dishes = ''
for z in the_menu:
    for j in z['subtitle']:
        all_dishes += j.lower() + ' '
print(all_dishes)
print('***********************************')
print('** What would you like to order? ')
print('***********************************')

order = []
user_order= input('> ')

while user_order != 'quit':
    if user_order in all_dishes and user_order != 'a':
        order.append(user_order)
        print(f'** {order.count(user_order)} order of {user_order} have been added to your meal **')
    else:
        print('please order one of the stuff on the menu!!')
    user_order = input('> ')
