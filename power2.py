# Question 3: Power of Two
def is_power_of_two():
    n = int(input("Enter a number: "))
    result = n > 0 and (n & (n - 1)) == 0
    print(f"{n} => Returns {result}")


is_power_of_two()

