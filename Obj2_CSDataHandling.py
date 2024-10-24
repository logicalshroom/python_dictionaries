# Example ticket structure

# We can initiaize using the sample tickets provided

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

ticketcounter = 3

def new_tic():
    global ticketcounter
    name = input("Please input your name: ")
    issue = input("Please let us know the nature of your issue: ")
    new_ticketID = "Ticket" + "00" + str(ticketcounter)
    ticketcounter += 1
    service_tickets.update({new_ticketID : {"Customer": name, "Issue": issue, "Status":"open"}})
    print(f"Your ticket number is: " + new_ticketID + "! Here are the details:")
    print(service_tickets[new_ticketID])

def up_tic():
    user_name = input("Please type the name of the user who's ticket you'd like to close: ")
    for ticket in service_tickets.values():
        if user_name == ticket["Customer"]:
            ticket["Status"] = "closed"
            print(f"Ticket for {user_name} closed.")

def dis_tic():
    disp_command = input("Type 'View' to see all tickets\nType 'Open' to see all open tickets\nType 'Closed' to see all closed tickets: ")
    try:
        if disp_command.lower() == "view":
            for ticket in service_tickets.items():
                print(ticket)
        if disp_command.lower() == "open":
            for key, item in service_tickets.items():
                if item["Status"] == "open":
                    print(key, item)
        if disp_command.lower() == "closed":
            for key, item in service_tickets.items():
                if item["Status"] == "closed":
                    print(key, item)
    except:
        print("Unexpected Display Menu Error. Try again!")
    
         
def main():
    while True:
        print('''Welcome to the Main Menu:
          1. New Ticket
          2. Update Ticket Status
          3. Display Tickets
          4. Close Program''')
        command = input("Please enter your selection: ")
        try:
            command = int(command)
            if command == 1:
                print(f"Generating a new ticket...")
                new_tic()
            elif command == 2:
                print(f"Updating a ticket...")
                up_tic()
            elif command == 3:
                print(f"Running Ticket Display Interface...")
                dis_tic()
            elif command == 4:
                print(f"Terminating Program...")
                break
        except:
            print(f"Unexcpeted Main Menu Error. Try again!")

main()