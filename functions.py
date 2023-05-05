FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as todo_file:
        func_todos = todo_file.readlines()
    return func_todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, "w") as filepath:
        filepath.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
