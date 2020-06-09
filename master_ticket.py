TICKET_PRICE = 10

tickets_remaining = 100

# output tickets remaining
print("There are {} Tickets remaining".format(tickets_remaining))

#gather usere name and assign to var

name = input("What is your name?  ")

# Prompt user by name about ticket amount
ticket_quantity = input("OK {}, How many tickets would you like?  ".format(name))
ticket_quantity = int(ticket_quantity)
# Calculate price (tickets * price) and assign to variable
total_cost = ticket_quantity * TICKET_PRICE

# Output the price to the screen

print("Your total cost is {}.".format(total_cost))