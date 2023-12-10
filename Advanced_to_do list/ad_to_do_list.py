print("Welcome to the To-Do list application..!!")
print (
    "1. Ad a task \n2. View task \n3. Mark task as completed \n4. Delete Task \n5. Quit"
)
user_task = None

def readFile(name):
  with open (name, "r") as r:
    print(r.read())

def writeFile(name, comment):
  with open (name, "a") as a:
    a.write(comment)
    a.write('\n')

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
        writeFile("t_status.txt", "Pending")
    elif user_task == 2:
      user_input = str(input("Please enter the task name: "))
      fp = open("t_name.txt", "r")
      fp_desc = open("t_desc.txt", "r")
      fp_date = open("due_date.txt", "r")
      for i in fp.readlines():
            desc = fp_desc.readline()
            date = fp_date.readline()
            if user_input.lower() in i.lower():
              print (f"\nThe task is: {i}")
              print (f"The desc is: {desc}")
              print (f"The date is: {date}")
    elif user_task == 3:
        inp_task = str(input("Please enter your task: "))
        inp = int(input("Please choose your status:\n\t1. Pending\n\t2. Completed\n\t"))
        with open("t_name.txt", "r") as file:
            lines = file.readlines()
            if inp_task+'\n' in lines and inp == 1:
                with open("t_name.txt", "r") as file:
                    lines = file.readlines()
                if inp_task+'\n' in lines:
                    index = lines.index(inp_task+'\n')
                    with open("t_status.txt", "r") as file:
                      status_lines = file.readlines()
                    status_lines[index] = "Pending\n"
                    with open("t_status.txt", "w") as file:
                      file.writelines(status_lines)
            elif inp_task+'\n' in lines and inp == 2:
                with open("t_name.txt", "r") as file:
                    lines = file.readlines()
                if inp_task+'\n' in lines:
                    index = lines.index(inp_task+'\n')
                    with open("t_status.txt", "r") as file:
                      status_lines = file.readlines()
                    status_lines[index] = "Completed\n"
                    with open("t_status.txt", "w") as file:
                      file.writelines(status_lines)
            else:
              print ("The task is not available..")
    elif user_task == 4:
      inp = str(input("Enter the task you want to delete:\n\t:"))
      with open("t_name.txt", "r") as file:
          lines = file.readlines()
      if inp+'\n' in lines:
          index = lines.index(inp+'\n')
          lines.pop(index)
          with open("t_name.txt", "w") as file:
              file.writelines(lines)
          for filename in ["t_status.txt", "due_date.txt", "t_desc.txt"]:
              with open(filename, "r") as file:
                  lines = file.readlines()
              lines.pop(index)
              with open(filename, "w") as file:
                  file.writelines(lines)
          print("The Task has been successfully deleted..")
      else:
        print("The task is not exist.")
                
  