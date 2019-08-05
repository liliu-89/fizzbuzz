print("Enter a number between 1 and 100. This FizzBuzz program starts to count to that number.")
print("In case the number is divisible with 3, it prints 'fizz' instead of the number.")
print("If the number is divisible with 5, it prints 'buzz'. If it's divisible with both 3 and 5, it prints 'fizzbuzz'.")

number = int(input("Please enter a number between 1 and 100: "))

for x in range(1, number+1):
    if x % 3 == 0 and x%5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
