def count_friends(friendships):
    # Initialize a dictionary to keep track of friends count
    friend_count = {}
    
    # Process each friendship pair/list
    for group in friendships:
        if len(group) == 1:  # Handle solitary entries
            if group[0] not in friend_count:  # Only set to 0 if not already in the dictionary
                friend_count[group[0]] = 0
        else:
            for friend in group:
                # Increment friend count
                friend_count[friend] = friend_count.get(friend, 0) + 1
          
    return friend_count

# Example usage
friendships = [[2,3],[3,4],[5]]
print(count_friends(friendships))

friendships = [[2, 2, 3], [3, 4]]
print(count_friends(friendships))