FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:      # <-- to open to-do text file
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Here, function write_todos works more like a procedure,
    as it only writes new inputs to the existing file. No need to return a value.
    """
    with open(filepath, 'w') as file:  # <-- to save to-dos to a text file
        file.writelines(todos_arg)

