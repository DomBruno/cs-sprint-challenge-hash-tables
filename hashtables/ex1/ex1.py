def get_indices_of_item_weights(weights, length, limit):
    
    # Initialize Hash to hold key:value (weight:index)
    
    weightHash = {}

    # Loop through list and compare weights to Limit

    for i in range(length):

        currVal = limit - weights[i]

        # Check table for currVal

        if currVal in weightHash:

            # Conform to zeroth and first requirement

            first = weightHash[currVal]
            solution = (i, first)
            return solution

        # If currVal not present, proceed

        else:
                weightHash[weights[i]] = i

    # exit if limit is never matched

    return None





    





    return None
