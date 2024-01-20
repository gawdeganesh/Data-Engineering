def kthRepeating (input, n) :

    dictionary = { i : input.count(i) for i in input}
    list = [ key for key, value in dictionary.items() if value ==1]

      # now return (k-1)th character from above list
    if len(list) < k:
        return 'Less than k non-repeating characters in input.'
    else:
        return list[k-1]

# Driver function
if __name__ == "__main__":
    input = "geeksforgeeks"
    k = 3
    print (kthRepeating(input, k))    



