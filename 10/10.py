#Count vowels in a given string.
string = str(input("Enter your word: "))

vowels = ["A", "E", "I", "O", "U", "Y", "a", "e", "i", "o", "u", "y"]
sum = 0
for i in string:
    if i in vowels:
        sum += 1
print(sum)