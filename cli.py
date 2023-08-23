from functions import get_todos, write_todos

print('To-Do App' '\n'
      'To show To-dos, type "show" \n'
      'To add a To-do, type "add" \n'
      'To edit a To-do, type "edit" \n'
      'To complete a To-do, type "complete" \n'
      'To exit, type "exit" \n\n')

# todos = []


while True:
    user_action = input('Your command: ')

    user_action = user_action.strip()   # <--to remove trailing spaces after a command

    # match user_action:
    if user_action.startswith('add'):
        # todo = input('Enter a to-do: ') + '\n'
        todo = user_action[4:]

        todos = get_todos(filepath='todos.txt')

        todos.append(todo + '\n')

        write_todos(filepath='todos.txt', todos_arg=todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]  #<-- list comp to strip \n from todos output

        for index, item in enumerate(todos):      # <-- to index a list output
            row = f'{index + 1} - {item}'
            print(row.strip('\n'))

    # case _:                 # <-- _: can be used to execute the line when none of the cases are matched
    #     print('Unknown command')

    elif user_action.startswith('edit'):
        # number = int(input('Which to-do item to edit?: '))
        try:
            number = int(user_action[5:])
            number = number - 1         # <-- a workaround for indexing

            todos = get_todos()

            new_todo = input('New to-do: ')
            todos[number] = new_todo + '\n'

            write_todos(todos, 'todos.txt')

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            # number = int(input('Which to-do item to complete?: '))
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos, 'todos.txt')

            print(f'Selected to-do {todo_to_remove} was completed')
        except IndexError:
            print('A to-do item does not exist.')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Unknown command')
