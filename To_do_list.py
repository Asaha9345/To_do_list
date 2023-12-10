print("Welcome to the To-Do list application..!!")
print (
    "1. Ad a task \n2. View task \n3. Mark task as completed \n4. Edit the task \n5. Quit"
)
user_task = None

def readFile(name):
  with open (name, "r") as r:
    print(r.read())

def writeFile(name, comment):
  with open (name, "w") as w:
    w.write(comment)

while user_task != 5:
    user_task = int(input("Please enter your choice (1/2/3/4/5): "))
    if user_task > 5 or user_task <= 0:
        print("Please enter a valid number..!!")
    elif user_task == 1: 
        t_name = input("Enter your task name: ")
        t_desc = input("Enter your task description: ")
        due_date = input("Enter task due date: ")
        print("Your task is successfully entered..")
        writeFile("t_name.txt" , t_name)
        writeFile("t_desc.txt" , t_desc)
        writeFile("due_date.txt" , due_date)
    elif user_task == 2:
        readFile("t_name.txt")
        readFile("t_desc.txt")
        readFile("due_date.txt")
    elif user_task == 3:
        with open ("t_name.txt" , "r") as t_n_1:
            a = t_n_1.read()
        with open ("t_status.txt" , "r") as t_sts:
            t_s = t_sts.read()
        task_dict = {
            a : t_s
        }
        print(f"The name status of the task is: {task_dict}")
        b = int(input("Enter yout status of the task.. 1(Pending), 2(Completed): "))
        if b == 1:
            writeFile("t_status.txt" , "Pending")
        elif b == 2:
            writeFile("t_status.txt" , "Completed")
        else:
            print("Enter a valid value.!!")
    elif user_task == 4:
        e_task = input("Enter the new name: ")
        writeFile("t_name.txt" , e_task)
        print("Your task has been updated successfully..!!")