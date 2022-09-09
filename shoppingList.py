print('''
Welcome to your Shopping List App.

Type help for a list of actions.
''')

command = input('command: ')

if command.lower() == 'help':
    print('''
    create -- creates a new shopping list in which you can name
    delete -- deletes a created shopping list
    add -- adds an item onto your shopping list
    clear -- removes all items in your list
    remove -- removes a specific item in your list
    ''')

if command.lower() == 'create':
    name = input('what would you like to call this shopping list: ')
    class shoppingList:
        def __init__(self,name):
            self.name = name
    
    