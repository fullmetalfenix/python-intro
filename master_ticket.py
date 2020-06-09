TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining >= 1:
    # output tickets remaining
    print("There are {} Tickets remaining  ".format(tickets_remaining))

    #gather usere name and assign to var

    name = input("What is your name?  ")

    # Prompt user by name about ticket amount
    ticket_quantity = input("OK {}, How many tickets would you like?  ".format(name))
    ticket_quantity = int(ticket_quantity)
    # Calculate price (tickets * price) and assign to variable
    total_cost = ticket_quantity * TICKET_PRICE

    # Output the price to the screen

    print("Your total cost is {}.  ".format(total_cost))


    procede_with_purchase = input("Do you want to procede with your purchase? Y/N  ")

    if procede_with_purchase.upper() == "Y":
        tickets_remaining -= ticket_quantity
        # process CC
        print("Sold! ")
    else :
        print("Thank you for your interest {}  ".format(name))
# Close while block
print("Sorry, tickets are all sold out!  ")