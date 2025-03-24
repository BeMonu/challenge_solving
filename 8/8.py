#Find the sum of digits in a number.
n = int(input("Enter number: "))
 
sum = 0
while n > 0:
    sum += n % 10
    n = n//10

print(sum)