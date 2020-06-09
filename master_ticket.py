TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining >= 1:
    print("There are {} Tickets remaining  ".format(tickets_remaining))
    name = input("What is your name?  ")
    ticket_quantity = input("OK {}, How many tickets would you like?  ".format(name))
    # Handle ValueError here
    try:
        ticket_quantity = int(ticket_quantity)
        # raise WalueError if sake is form more tickets then available
        if ticket_quantity > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no there has been an error {}, please try again!".format(err))
    else:
        total_cost = ticket_quantity * TICKET_PRICE
        print("Your total cost is {}.  ".format(total_cost))
        procede_with_purchase = input("Do you want to procede with your purchase? Y/N  ")
        if procede_with_purchase.upper() == "Y":
            tickets_remaining -= ticket_quantity
            # process CC
            print("Sold! ")
        else :
            print("Thank you for your interest {}  ".format(name))
print("Sorry, tickets are all sold out!  ")