f = open("hello.txt", "r")

r = f.read()

print(r)


"""# Print how many lines are there
x = f.readlines()
print(len(x))"""

"""
Print how many words are there
"""
lines = f.readlines()
print(lines)
count = 0
for line in lines:
    words = line.strip().split()
    count = count + len(words)
print(count)
f.close()


"""
good morning hello
ok bye
done
have a great day


hello morning good
bye ok
done
day great a have

"""

f = open("hello.txt", "r")
lines = f.readlines()
for line in lines:
    words = line.strip().split()[::-1]
    print(" ".join(i for i in words))


f.close()
