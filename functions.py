FILEPATH = r"todoslistdata.txt"

def get_todos(filepath=FILEPATH ):
    """ Reads a text file and returns
    the list of todos from it
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local
       # same as this file = open(r"todoslistdata.txt", "r")
       # todos = file.readlines()
       # file.close()

def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes to-do item list to a file"""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
#this is a modification function, hence nothing to return

if __name__ == "__main__":
    print("Hello")