
def removeDuplicates(input):
    # convert to set/contains no duplicates
    setWithNoDuplicates = set(input)

    # convert back to list
    return list(setWithNoDuplicates)

# test
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = removeDuplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
