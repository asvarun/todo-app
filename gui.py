import functions
import PySimpleGUI as psg

label = psg.Text("Type in a To-Do")
input_box = psg.InputText(tooltip="Enter todo", key="todo")
add_button = psg.Button("Add")

window = psg.Window("My To-Do App",
                    layout=[[label], [input_box, add_button]],
                    font=("Helvetica", 14))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case psg.WIN_CLOSED:
            break

window.close()
