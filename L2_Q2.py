string = input("Enter the string  ")
char = input("Enter the character to find the character frequency  ")
count = 0
for i in range(len(string)):
    if string[i] == char:
        count = count+1
print ("The number of character frequency is",count)