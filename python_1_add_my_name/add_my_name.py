found = False
timeout = 0
canceled = False
filename = ""
file_not_found_meesage = "File Not Found, to cancel type \" cancel \" "
while(not found and (timeout < 5) and not canceled):
    try:
        filename = input("filename: ")
        if(filename == "cancel"):
            canceled = True
        file = open(filename, "r")
        found = True
    except (FileNotFoundError):
        print(file_not_found_meesage)
        timeout = timeout + 1
file_lines = file.readlines()
new_file_lines = ""
print(file_lines)
for line in file_lines:
    new_file_lines += "catoola "  + line.split("\n")[0] + " Shora \r\n"
print(new_file_lines)
file.close()
file = open(filename, "w")
file.write(new_file_lines)
print(file_lines)
