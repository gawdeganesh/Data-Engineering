# Initializing string
test_str = "abcaaaacbbaa"

# Printing original String
print("The original string is : " + test_str)

# Initializing K
K = "a"
current_count = 0
max_count = 0

for char in test_str:
    if char == K:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

print(max_count)
