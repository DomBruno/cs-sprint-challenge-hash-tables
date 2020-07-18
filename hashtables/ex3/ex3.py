def intersection(arrays):
    
    # Initialize interHash to hold key:value (int:occurrences)
    
    interHash = {}

    # nested for loop to check if int is in interHash
    # increment count or add to interHash if not previously entered

    for a in arrays:
        for b in a:
            if b in interHash:
                interHash[b] += 1
            else:
                interHash[b] = 1

    # init result

    result = []

    # count number of arrays

    numArray = len(arrays)

    # if int occurrences equal number of arrays, return it

    for c in interHash:
        if interHash[c] == numArray:
            result.append(c)

    return result



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
