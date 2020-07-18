#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    # Init hashtable to hold key:value (source:detination)
    
    ticketHash = {}

    # Init route list; this syntax still confuses me
    
    route = [None] * length

    # Begin for loop to chain tickets using source: "NONE"" as a base

    for i in range(length):
        if tickets[i].source == "NONE":
            
            # check for index with "Source" matching "Destination" of previous index

            route[0] = tickets[i].destination
        ticketHash[tickets[i].source] = tickets[i].destination

    # Begin for loop to check if index -1 is None

    for r in range(length):
        
        if route[r - 1] is not None:

            #add to route

            route[r] = ticketHash[route[r-1]]





    return route
