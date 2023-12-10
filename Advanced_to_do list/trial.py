with open("t_name.txt", "r") as file:
    lines = file.readlines()
if 'Python\n' in lines:
    index = lines.index('Python\n')
    lines.pop(index)
    with open("t_name.txt", "w") as file:
        file.writelines(lines)
    for filename in ["t_status.txt", "due_date.txt", "t_desc.txt"]:
        with open(filename, "r") as file:
            lines = file.readlines()
        lines.pop(index)
        with open(filename, "w") as file:
            file.writelines(lines)
