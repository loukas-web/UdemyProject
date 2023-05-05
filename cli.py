# from functions import get_todos, write_todos
import functions
import time

now: str = time.strftime("%Y-%m-%d, %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # remove whitespace from start and end
    
    if user_action.startswith("add"):
        todo = user_action[4:]
        
        todos = functions.get_todos()
        
        todos.append(todo + "\n")
        
        functions.write_todos(todos)
    elif user_action.startswith("show"):
        todos = functions.get_todos()
        
        new_todos = [item.strip("\n") for item in todos]  # list comprehension
        
        for index, item in enumerate(new_todos):  # enumerate
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = functions.get_todos()
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            
            functions.write_todos(todos)
        except ValueError:
            print("Command is not valid")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            
            index = number - 1
            todos = functions.get_todos()
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            
            functions.write_todos(todos)
            
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye!")
