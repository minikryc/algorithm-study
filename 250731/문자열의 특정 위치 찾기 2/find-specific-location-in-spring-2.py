strings = ["apple", "banana", "grape", "blueberry", "orange"]
letter = input()
count = 0

for string in strings:
    if string[2] == letter or string[3] == letter:
        count += 1
        print(string)

print(count)