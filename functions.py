FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the list of to-do items list to a text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


#only run if started directly from functions, do not run when imported by main / another script
if __name__ == "__main__":
    print(get_todos())