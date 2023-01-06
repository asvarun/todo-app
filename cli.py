import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"it is {now}")

while True:
    user_action = input("Type add or edit or show or complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        # todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos, "todos.txt")

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo list item: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, "todos.txt")

        except ValueError:
            print("Your command is invalid. Enter a number")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos, "todos.txt")

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print("Index out of range. Value chosen is incorrect.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Incorrect choice. Please enter a valid choice")

print("Thank You")