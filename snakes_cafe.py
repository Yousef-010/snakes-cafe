
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


print('**************************************\n**  Welcome to the Snakes Cafe!   **\n**  Please see our menu below.  **\n** To quit at any time, type "quit" **\n**************************************')


def print_menu():
    for x in the_menu:
        print(x['title'])
        print('---------')
        for y in x['subtitle']:
            print(y)
        print('\n')


print_menu()

all_dishes =''
for z in the_menu:
    for j in z['subtitle']:
        all_dishes += j.lower() +' '

print('***********************************')
user_order = input(' What would you like to order?  ').lower()




def make_order(user_input):
    counters = 1
    orders = ''
    quit = False
    for x in the_menu:
        for y in x['subtitle']:
           if y.lower() == user_input:

               orders += user_input + ' '
               print(f'{counters} order of {orders} have been added to your meal')
               exit_msg = input('type quit to finish or no to complete your order : ')
               quit = True

               while exit_msg != 'quit':
                  user_order=''
                  if y.lower() == user_input:

                      user_order = input(' What would you like to order?  ').lower()
                      if user_order in all_dishes:
                          counters += 1
                          orders += user_order + ' '
                          print(f'{counters} order of {orders} have been added to your meal')
                          exit_msg = input('type quit to finish or no to complete your order : ')
                          quit = True
                      else:
                          print('invalid input plwase select again ')
                          quit = False

    if quit:
        print(f'your order {orders} has been added :)  :')
    else:
        print(f'your order is not available in our menu please check our menu :')

make_order(user_order)
