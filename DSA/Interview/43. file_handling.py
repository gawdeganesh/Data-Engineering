"""
Make a function which takes filename as a parameter.
Return the number of lines present in that file.
"""


def countLines(filename: str) -> int:
    try:
        """
        Method 1
        file = open(filename, 'r')
        line_count = 0
        for line in file:
            line_count += 1
        file.close()
        return line_count
        """
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        return len(lines)
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to show user there is an error


filename = "hello.txt"
line_count = countLines(filename)
if line_count != -1:
    print(f"Number of lines in {filename} = {line_count}")


"""
Make a function which takes filename as a parameter.
Return the number of lines present in that file which does not start with T or t.
"""


def countLines(filename: str) -> int:
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        count = 0
        for line in lines:
            if not line.strip().lower().startswith("t"):
                count += 1
        return count
    except FileNotFoundError:
        print("File not found!")
        return -1


filename = "hello.txt"
line_count = countLines(filename)
if line_count != -1:
    print(f"Number of lines in {filename} not starting with 'T' or 't' = {line_count}")


"""
Make a function which takes filename as a parameter.
Return the number of time the word the has appeared in that file.
"""


def wordOccurrences(filename: str) -> int:
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        words = data.split()

        word_count = 0
        for word in words:
            if word.lower() == "the":
                word_count += 1
        return word_count
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to indicate an error


filename = "hello.txt"
count = wordOccurrences(filename)
if count != -1:
    print(f"The word 'the' appears {count} times in {filename}")

"""
Make a function which takes filename as a parameter.
Return the count of uppercase characters in that file.
"""


def countUppercaseCharacters(filename: str) -> int:
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        # count = sum(1 for char in content if char.isupper())  # Shortcut
        count = 0
        for char in data:
            if char.isupper():
                count += 1
        return count
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to indicate an error


filename = "hello.txt"
uppercase_count = countUppercaseCharacters(filename)
if uppercase_count != -1:
    print(f"Count of uppercase characters = {uppercase_count}")

"""
There is a file having numbers in each line of that file.
Calculate the total of all numbers.
Example (File Content)
100
250
100
50
98

OUTPUT
598
"""


def calculateTotal(filename: str) -> int:
    try:
        # Shortcut
        # calculate = sum(list(map(int, f.read().split())))
        # return calculate
        file = open(filename, "r")
        total = 0
        for line in file:
            if line.strip().isnumeric():
                total += int(line.strip())
        file.close()
        return total
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to indicate an error


filename = "hello.txt"
total = calculateTotal(filename)
if total != -1:
    print(f"Total = {total}")

"""
Print each line of the file in reverse order.
Example (File Content)
python is great
this is a great course
we are doing dsa

OUTPUT
great is python
course great a is this
dsa doing are we
"""


def printLines(filename: str) -> None:
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            words = line.strip().split()
            reversed_words = words[::-1]
            reversed_line = " ".join(reversed_words)
            print(reversed_line)
    except FileNotFoundError:
        print("File not found!")


filename = "hello.txt"
printLines(filename)


"""
Print each word of the file in reverse order.
Example (File Content)
python is great
this is a great course
we are doing dsa

OUTPUT
nohtyp si taerg
siht si a taerg esruoc
ew era gniod asd
"""


def printWordsInReverse(filename: str) -> None:
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            words = line.strip().split()
            reversed_words = [word[::-1] for word in words]
            print(" ".join(reversed_words))
    except FileNotFoundError:
        print("File not found!")


filename = "hello.txt"
printWordsInReverse(filename)


def reverseLines(input_file: str, output_file: str) -> None:
    try:
        with open(input_file, "r") as file_in:
            lines = file_in.readlines()

        with open(output_file, "w") as file_out:
            for line in lines[::-1]:
                line = line.strip()
                # reversed_line = line[::-1]
                file_out.write(line + "\n")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError:
        print("Error: An I/O error occurred.")


reverseLines("input.txt", "result.txt")


def multiplication(filename, number):
    try:
        with open(filename, "w") as file:
            for i in range(1, 11):
                multiplication = number * i
                file.write(f"{number} * {i} = {multiplication}\n ")

            print(
                f"Multiplication table of {number} is written to '{filename}' successfully."
            )

    except IOError:
        print("Error: An I/O error occurred.")


multiplication("multiply.txt", 7)

def readLastNLines(filename: str, n: int) -> None:
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            total_lines = len(lines)
            if n > total_lines:
                print("Not Enough Lines")
            else:
                last_n_lines = lines[-n:]
                for line in last_n_lines:
                    print(line.strip())
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: An I/O error occurred.")


filename = "example.txt"  # Replace with your filename
n = int(input("Enter the number of lines to read = "))
readLastNLines(filename, n)