tasks = []

def addNewTask(task):
    tasks.append(task)
    print("New Task Added: ",task )
    
def removeTask(task):
    if task in tasks:
        tasks.remove(task)
        print("Task Removed: ", task)
    else:
        print("Task Not Found In Tasks")

def displayTask():
    if tasks:
        print("The Tasks Are: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No Tasks To Display")

while True:
    print("\nToDo List Menu: ")
    print("1.Add Task")
    print("2.Remove Task")
    print("3.Display Task")
    print("4.Quit")
    
    select = input("Enter Your Choice: ")
    
    if select == "1":
        task = input("Enter New Task: ")
        addNewTask(task)
    elif select == "2":
        task = input("Enter The Task To Be Removed: ")
        removeTask(task)
    elif select == "3":
        displayTask()
    elif select == "4":
        print("Quit")
        break
    else:
        print("Please Try Again")