a = int(input("First number: "))
b = int(input("Second number: "))

def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

print(GCD(a, b))
