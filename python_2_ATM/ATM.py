data_filename = "data"
clients_information_file = open(data_filename, "r")
clients_information = clients_information_file.readlines()
parsed_client_information = []
clients = {}
for client in clients_information:
    parsed_client_information = client.split(" ")[:4]
    clients[parsed_client_information[0]] = parsed_client_information[1:]
for client in clients:
    clients[client][2] = float(clients[client][2])

greeting_message = "Welcome to StealYourMoney Ltd. Inc.\r\nID: "
wrong_id_message = "I donno ya'\r\nID: "
instructions = []
instructions.append("now what?")
instructions.append("q - QUIT")
instructions.append("h - how much we own from you")
instructions.append("g - give us money")
instructions.append("t - take money (give us your soul)")
instructions.append("c - change password")

password = ""
user_id = "0"
action = ""

def print_instructions():
    for i in instructions:
        print(i)

def login():
    global user_id
    global clients
    user_id = input(greeting_message)
    if(user_id != "-1"):
        while(not user_id in clients):
            user_id = input(wrong_id_message)
        password = input("password: ")
        while(not clients[user_id][1] == password):
            password = input("NO.\r\nPassword: ")
        print("welcome " + clients[user_id][0])
        action()
    
    
def how_much_money():
    print(clients[user_id][2])

def take_money():
    global clients
    ammount = float(input("HOW MUCH: "))
    while (ammount < 0):
        print("NO tricksssss")
        ammount = float(input("HOW MUCH: "))
    clients[user_id][2] -= ammount


def give_money():
    global clients
    ammount = float(input("HOW MUCH: "))
    while (ammount < 0):
        print("NO tricksssss")
        ammount = float(input("HOW MUCH: "))
    clients[user_id][2] += ammount

def change_password():
    new_password = input("New password: ")
    clients[user_id][1] = new_password

actions = {}
actions["h"] = how_much_money
actions["t"] = take_money
actions["g"] = give_money
actions["c"] = change_password 

def action():
    print_instructions()
    action = input("WAHT: ")
    while(action != "q"):
        if(not action in actions):
            print("NO.")
        actions[action]()
        print_instructions()
        action = input("WAHT: ")
        






  
while(user_id != "-1"):
    login()

print("bye")
clients_information_file.close()


new_clinet_informatio_data = ""
current_client_data = ""
for client in clients:
    current_client_data = client + " "
    for data_field in clients[client]:
        current_client_data += str(data_field) + " "
    new_clinet_informatio_data += current_client_data + "\n"
    
clients_information_file = open(data_filename, "w")
clients_information_file.write(new_clinet_informatio_data)
         
