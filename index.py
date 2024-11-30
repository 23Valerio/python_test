# print tasks
def print_tasks(tasks_list: dict):
    command = ""
    while command not in  ["1", "2", "3", "4"]:
        command = input(
            "Please enter option from below:\n 1 - Print all task\n 2 - Sort tasks by status\n 3 - Sort tasks by priority\n 4 - Print task by some keyword\n: ")
        match command:
            case "1":
                for key, value in tasks_list.items():
                    print(f"ID: {key}\n Name: {value["name"]}\n Description: {value["description"]}\n Priority: {value["priority"]}\n Status: {value["status"]}")
            case "2":
                for i in ["1", "2", "3"]:
                    for key, value in tasks_list.items():
                        if i == value["status"]:
                            print(f"ID: {key}\n Name: {value["name"]}\n Description: {value["description"]}\n Priority: {value["priority"]}\n Status: {value["status"]}")
            case "3":
                for i in ["1", "2", "3"]:
                    for key, value in tasks_list.items():
                        if i == value["priority"]:
                            print(f"ID: {key}\n Name: {value["name"]}\n Description: {value["description"]}\n Priority: {value["priority"]}\n Status: {value["status"]}")
            case "4":
                text = input("Please enter keyword for searching: ").lower()
                found = False
                for key, value in tasks_list.items():
                    if value["name"].lower().find(text) != -1 or value["description"].lower().find(text) != -1:
                        print(f"ID: {key}\n Name: {value["name"]}\n Description: {value["description"]}\n Priority: {value["priority"]}\n Status: {value["status"]}")
                        found = True
                if not found:
                    print("No match found\n")
            case _:
                print("Wrong option! Please retry\n")
 
# delete task by ID
def delete_task(tasks_list: dict):
    success = False
    while success == False:
        id = input("Please enter ID for delete: ")
        try:
            if int(id) in tasks_list.keys():
                del tasks_list[int(id)]
                success = True
                print(f"Task with ID:{id} was deleted")
            else:
                print("No such ID in TODO list")
                success = True
        except ValueError:
                print('Wrong ID value')

# check is input value in range_list
def check_input(message: str, range_list: list):
    option = True
    while option:
        value = input(message)
        if value in range_list:
            option = False
        else:
            print("Wrong option! Please retry")
    return value

# add new task
def add_task(tasks_list: dict):
    id = max(tasks_list.keys()) + 1
    name = input("Please enter the name of new task: ")
    description = input("Please enter the description of new task: ")
    priority = check_input("Please enter the priority (1 - LOW, 2 - MEDIUM or 3 - HIGH): ", ["1", "2", "3"])
    status = check_input("Please enter the status (1 - New, 2 - In process or 3 - Done): ", ["1", "2", "3"])
    tasks_list[id] = {
        "name": name,
        "description": description,
        "priority": priority,
        "status": status
    }
    print(f"The new task with ID:{str(id)} was created")

# save todo_list to file
def save_tasks(tasks_list: dict):
    with open("todo.txt", "w") as file:
        for id, task in tasks_list.items():
            file.write(f"{id}:\n")
            for key, value in task.items():
                file.write(f"{key}:{value}\n")

# download todo_list from file
def download_tasks():
    tasks_list = {}
    with open("todo.txt", "r") as file:
        id = 0
        for line in file:
            line = line.strip()
            if line.endswith(":"):
                id = int(line[:-1])
                tasks_list[id] = {}
            else:
                item = line.split(":", 1)
                tasks_list[id][item[0]] = item[1]
    return tasks_list

# update task
def update_task(tasks_list: dict):
    id = input("Please enter task ID for update: ")
    try:
        if int(id) in tasks_list.keys():
            command = input(
            "Please select an option from below:\n 1 - Update name\n 2 - Update description\n 3 - Update priority\n 4 - Update status\n: ")
            match command:
                case "1":
                    tasks_list[int(id)]["name"] = input("Please enter the new name for task: ")
                case "2":
                    tasks_list[int(id)]["description"] = input("Please enter the new description for task: ")
                case "3":
                    priority = check_input("Please enter the priority (1 - LOW, 2 - MEDIUM or 3 - HIGH): ", ["1", "2", "3"])
                    tasks_list[int(id)]["priority"] = priority
                case "4":
                    status = check_input("Please enter the status (1 - New, 2 - In process or 3 - Done): ", ["1", "2", "3"])
                    tasks_list[int(id)]["status"] = status
            print(f"Task with ID:{id} was updated")
            save_tasks(todo_list)
        else:
            print("No such ID in TODO list")
    except ValueError:
        print('Wrong ID value')

# main program
todo_list = download_tasks()
command = ""

while command != "0":
    command = input(
        "Please enter option from below:\n 1 - Create new task\n 2 - Show tasks\n 3 - Update task\n 4 - Delete task\n 0 - Exit\n: ")
    match command:
        case "1":
            add_task(todo_list)
            save_tasks(todo_list)
        case "2":
            print_tasks(todo_list)
        case "3":
            update_task(todo_list)
        case "4":
            delete_task(todo_list)
            save_tasks(todo_list)
        case "0":
            print("Program closed")
        case _:
            print("Wrong option! Please retry\n")